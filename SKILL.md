---
name: hackathon-win-kit
description: Plan, build, demonstrate, and submit a hackathon project against a specific event's rules and judging criteria. Use for hackathon strategy, project selection, execution, sponsor tracks, demos, and submissions.
---

# Hackathon Win Kit

Help a team maximize its chance of a strong, eligible submission. Never promise a prize: judging is subjective and event rules control.

## First move: establish the event contract

Ask for or find the official event URL, hacking window and timezone, team size, eligibility, allowed prior work/AI, submission deadline, judging format, prize tracks, video and repository requirements. Read the **current official rules and rubric** before recommending a stack or sponsor. Record uncertain items as questions to organizers, not assumptions. For a live event, recheck rules before final submission.

If the team has no event yet, use the generic framework and label all timelines and scores as planning heuristics. Do not confuse a past sponsor prize with a current one. Consult [research and evidence](references/winner-patterns.md) for sourced examples and limits of inference.

## Operating loop

1. Run a short intake: event URL, hours left, team skills, target users, available data/hardware, budget, accessibility needs, target tracks, and definition of a live demo. If information is missing, make explicit provisional assumptions and proceed with reversible planning.
2. Convert the event rubric into a project scorecard. Reject ineligible ideas first. Generate three materially different concepts with [idea selection](playbooks/idea-generation.md), then choose one narrow user journey.
3. Write a one-page build contract: user/problem, testable outcome, judge-visible moment, sponsor fit, system diagram, data source, baseline, success metric, owners, milestones, cutoff times, demo fallback, and submission owner.
   Use [working templates](playbooks/working-templates.md) when a team needs copyable tables and receipts.
4. Build a vertical slice before broadening scope. Keep a working demo, screenshots, and a backup recording. Use the relevant technical playbooks only: [architecture](playbooks/architecture.md), [algorithms](playbooks/algorithms-and-math.md), [frontend](playbooks/frontend-ui-ux.md), [backend](playbooks/backend-data-orchestration.md).
   For ambitious systems, use [judge-visible proof](playbooks/judge-visible-proof.md) so UI state, backend behavior, and submission evidence match.
5. Run rubric checks at milestones. If the core path fails, stop features and repair it. If it works, improve evidence, usability, and sponsor proof. Use [risk and timeboxing](playbooks/roadmap-and-risk.md).
6. Draft and submit early enough to catch form, media, and eligibility errors. Use [demo and video](playbooks/demo-and-video.md), [Devpost](playbooks/devpost-submission.md), and [slides](playbooks/slides.md) only where the event requires or benefits from them.
7. After the event, use [follow-up](playbooks/post-hackathon.md) for honest documentation, feedback, and open-source maintenance.

Before declaring the plan complete, scan the [full-cycle checklist](playbooks/comprehensive-checklist.md) and mark each item done, assigned, or not applicable. It is a coverage audit, not a mandate to add features.

## Decision rules

- Optimize the event's *published* criteria. The generic [rubric](playbooks/judging-rubric.md) is only a stand-in.
- Prefer a complete, observable before/after workflow over a list of partial features. Show the actual product before architecture slides.
- A sponsor integration must change the user outcome and be visible in the demo. Verify account access, pricing, rate limits, allowed uses, and track-specific evidence with current official sources.
- Separate implemented behavior, simulated data, experimental components, and future work in every artifact.
- Use the simplest architecture that proves the claim. Add agents, RAG, blockchain, hardware, or elaborate animations only when they solve a real constraint or differentiate the experience.
- For claims in medicine, finance, public safety, or other consequential domains, use credible data and make uncertainty and human review visible.
- Respect event rules, attribution, licenses, privacy, and teammate consent. Do not fabricate users, metrics, integrations, or live behavior.
- Distinguish overall podium placements from sponsor/track awards, honorable mentions, participation awards, and unpublished results when learning from prior projects. See the [four-source data audit](references/data-audit.md).
- When mining historical projects, compare examples within the same event and verify award type on its official page. The [large-corpus audit](references/data-audit.md#full-corpus-label-audit-and-event-matched-comparison) found that prize text and missing labels are too noisy for a winner classifier. Treat description length, tag count, and team size as descriptive signals, never targets to inflate.

## Outputs to produce for a team

At minimum: event rule matrix, three-idea comparison, chosen one-page build contract, timeboxed task board, working demo route, rubric gap list, and a submission checklist with an owner. Add architecture/algorithm notes, sponsor evidence, video script, and deck when relevant. Keep outputs brief enough to use under deadline pressure.
