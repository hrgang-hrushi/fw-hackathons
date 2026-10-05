#!/usr/bin/env python3
"""Print a compact, descriptive audit of the Devpost Hacks `all` Parquet table."""

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

import pyarrow.parquet as pq


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("parquet", type=Path, help="Downloaded data/all/train.parquet")
    args = parser.parse_args()
    rows = pq.read_table(args.parquet).to_pylist()
    by_event = defaultdict(list)
    for row in rows:
        by_event[row["hackathon"]].append(row)

    def summary(items):
        return {
            "submissions": len(items),
            "winner_labels": sum(row["is_winner"] is True for row in items),
            "video_links": sum(bool(row.get("video_link")) for row in items),
            "github_links": sum(
                any("github.com/" in link.lower() for link in (row.get("other_links") or []))
                for row in items
            ),
            "embedded_readme_projects": sum(bool(row.get("readmes")) for row in items),
        }

    urls = [row["url"] for row in rows]
    repos = [entry.get("repo") for row in rows for entry in (row.get("readmes") or [])]
    report = {
        "all": summary(rows),
        "events": {event: summary(items) for event, items in sorted(by_event.items())},
        "quality": {
            "duplicate_url_rows": len(urls) - len(set(urls)),
            "missing_result_rows": sum(not row.get("results") for row in rows),
            "embedded_readme_objects": len(repos),
            "distinct_repositories": len(set(repos)),
            "projects_with_truncated_readme": sum(
                any(entry.get("truncated") for entry in (row.get("readmes") or []))
                for row in rows
            ),
        },
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
