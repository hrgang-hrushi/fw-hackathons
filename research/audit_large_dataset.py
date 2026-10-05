#!/usr/bin/env python3
"""Audit the historical Devpost corpus without treating every prize as a win.

Usage: python research/audit_large_dataset.py /path/to/combined_hackathons.parquet
Requires pyarrow. Prints aggregate JSON; does not copy project text into output.
"""

import ast
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pyarrow.parquet as pq


PLACEMENT = re.compile(
    r"^(?:(?:1st|2nd|3rd|first|second|third)\s+(?:place|prize|overall)|"
    r"(?:1st|2nd|3rd|first|second|third)\s+place\s+overall|"
    r"(?:overall\s+)?grand\s+prize|best\s+overall(?:\s+hack)?|"
    r"(?:1st|2nd|3rd|first|second|third)\s+overall|"
    r"overall\s+(?:winner|first|second|third|1st|2nd|3rd))$",
    re.I,
)
PARTICIPATION = re.compile(
    r"participat|all\s+(?:eligible\s+)?(?:participants|submissions)|"
    r"every(?:one|body|\s+participant)|anyone\s+who|"
    r"\b(?:swag|sticker|certificate\s+of\s+participation)\b",
    re.I,
)
HEADING = re.compile(r"\b(?:inspiration|what it does|how we built it|challenges we ran into|what's next)\b", re.I)
URL = re.compile(r"https?://|github\.com|youtu\.be|youtube\.com", re.I)


def parse_list(value):
    try:
        parsed = ast.literal_eval(value or "[]")
    except (SyntaxError, ValueError):
        return None
    return parsed if isinstance(parsed, list) else None


def category(prizes):
    if not prizes:
        return "no_prize_listed"
    labels = [str(p).strip() for p in prizes if str(p).strip()]
    if not labels:
        return "no_prize_listed"
    if any(PLACEMENT.fullmatch(p) for p in labels):
        return "placement_label"
    if all(PARTICIPATION.search(p) for p in labels):
        return "participation_only"
    return "other_award_or_ambiguous"


def features(row, tags, team):
    desc = row.get("full_desc") or ""
    return {
        "description_words": len(desc.split()),
        "brief_words": len((row.get("brief_desc") or "").split()),
        "tag_count": len(tags or []),
        "team_count": len(team or []),
        "has_url_text": bool(URL.search(desc)),
        "has_template_heading": bool(HEADING.search(desc)),
    }


def main(path):
    counts = Counter()
    labels = Counter()
    event_groups = defaultdict(lambda: defaultdict(list))
    links = set()
    pairs = set()
    invalid_lists = Counter()
    total = 0

    for batch in pq.ParquetFile(path).iter_batches(
        columns=["hackathon_id", "project_link", "full_desc", "brief_desc", "team_members", "prize", "tags"],
        batch_size=2000,
    ):
        for row in batch.to_pylist():
            total += 1
            prizes = parse_list(row["prize"])
            tags = parse_list(row["tags"])
            team = parse_list(row["team_members"])
            if prizes is None:
                invalid_lists["prize"] += 1
                prizes = []
            if tags is None:
                invalid_lists["tags"] += 1
            if team is None:
                invalid_lists["team_members"] += 1
            group = category(prizes)
            counts[group] += 1
            for label in prizes:
                labels[str(label).strip()] += 1
            link = row["project_link"]
            links.add(link)
            pairs.add((row["hackathon_id"], link))
            event_groups[row["hackathon_id"]][group].append(features(row, tags, team))

    # Only compare within events with both a placement-like label and a substantial no-prize pool.
    matched = [groups for groups in event_groups.values()
               if len(groups["placement_label"]) >= 3 and len(groups["no_prize_listed"]) >= 10]
    measures = ["description_words", "brief_words", "tag_count", "team_count", "has_url_text", "has_template_heading"]
    differences = {}
    for measure in measures:
        per_event = []
        for groups in matched:
            a = groups["placement_label"]
            b = groups["no_prize_listed"]
            per_event.append(sum(float(x[measure]) for x in a) / len(a) -
                             sum(float(x[measure]) for x in b) / len(b))
        differences[measure] = round(sum(per_event) / len(per_event), 3) if per_event else None

    result = {
        "rows": total,
        "distinct_events": len(event_groups),
        "distinct_project_links": len(links),
        "distinct_project_event_pairs": len(pairs),
        "prize_bearing_rows": total - counts["no_prize_listed"],
        "categories": dict(counts),
        "unique_prize_strings": len(labels),
        "invalid_serialized_lists": dict(invalid_lists),
        "matched_events": len(matched),
        "matched_event_mean_placement_label_minus_no_prize": differences,
        "frequent_labels": labels.most_common(20),
        "caveat": "Placement regex is deliberately narrow but may include track placements; it does not certify overall awards. No-prize means unlisted in this snapshot, not confirmed loss. Differences are descriptive, not causal.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not Path(sys.argv[1]).is_file():
        raise SystemExit("Usage: audit_large_dataset.py /path/to/combined_hackathons.parquet")
    main(sys.argv[1])
