# Repository hygiene and open-source release

During the event, aim for a repository a stranger can run: concise README with problem, demo image, architecture sketch, prerequisites, exact setup, environment template, sample data, and known limitations. Include a license when permitted or required, credits for libraries/assets/datasets, and clear teammate contributions. Keep main branch deployable; use small branches or integration checkpoints that fit team size.

## README structure to fill in

```markdown
# Project name — one-sentence user outcome
Demo: [video] · Try it: [live URL] · Devpost: [submitted entry]

## Problem and user
[Specific job, current workaround, evidence.]
## What works today
[Numbered three-step user journey; distinguish experimental and planned work.]
## How it works
[Diagram or compact flow, key algorithm and sponsor service's exact role.]
## Run locally
[Prerequisites; copy .env.example; install; seed; start; test input.]
## Demo data and limitations
[What is live/cached/simulated; known failure modes; cost or hardware requirements.]
## Tests and evidence
[One meaningful test command, sample size, metric, and baseline if claimed.]
## Team, credits, license
[Contributions; data/assets attribution; license if allowed.]
```

The 2,222-submission audit found README presence more common among labeled winners, while current README content varied widely and did not reveal a universal template. This structure is for reproducibility and honest review, not a promise of judging points. See [data audit](../references/data-audit.md).

Before making the repo public, inspect for keys, tokens, personal data, proprietary material, large generated files, and borrowed assets with incompatible licenses. If a secret reached history, revoke it; merely deleting a line is insufficient. Pin dependencies or commit a lockfile, run the main flow from a clean checkout, and confirm links work.

For discoverability, use a descriptive repository name, useful short description, relevant topics, a high-quality screenshot/GIF, a three-step quick start, and an honest feature list. Ask for stars or follows only after delivering value; do not manipulate engagement or inflate metrics. Invite issues and contributions with a small first-task list.
