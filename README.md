# Hackathon Win Kit

An open-source, evidence-led agent skill for choosing, building, demoing, and submitting a hackathon project. It turns event rules into a build plan and makes the final demo the center of execution. **It improves decision quality; it cannot guarantee placement.**

## Quick start

Clone the repository and point your coding agent at its root `SKILL.md`, or place the folder in your tool's skills directory if it supports skill discovery. Tools that read repository instructions can use `AGENTS.md`. For other IDEs/CLIs, include the `SKILL.md` path in the prompt and ask the agent to read only the relevant playbooks. No scripts, credentials, or service accounts are required.

```bash
git clone https://github.com/hrgang-hrushi/fw-hackathons.git
```

Starter prompt:

> Use `SKILL.md` for [official event URL]. We have [hours] hours, [team and skills], and want to target [prizes]. Read current rules, compare three ideas, then give us a one-page build contract, milestone board, demo path, and submission risks. Mark anything unverified.

## What is inside

| Path | Use |
| --- | --- |
| `SKILL.md`, `AGENTS.md` | Agent entry points and decision rules |
| `playbooks/idea-generation.md`, `judging-rubric.md` | Select a feasible idea against the actual rubric |
| `playbooks/sponsor-strategy.md` | Map sponsor requirements to meaningful product use |
| `playbooks/architecture.md`, `algorithms-and-math.md` | Choose a defensible technical core |
| `playbooks/frontend-ui-ux.md`, `backend-data-orchestration.md` | Ship a clear, reliable end-to-end product |
| `playbooks/judge-visible-proof.md` | Align product screens, backend traces, and submission evidence |
| `playbooks/roadmap-and-risk.md` | Pre/during/post schedule, ownership, cuts, fallbacks |
| `playbooks/comprehensive-checklist.md` | Full-cycle gap scan from eligibility through follow-up |
| `playbooks/working-templates.md` | Copyable event, prize, build, demo, and submission records |
| `playbooks/demo-and-video.md`, `slides.md`, `devpost-submission.md` | Communicate and submit what actually works |
| `playbooks/repo-hygiene.md`, `post-hackathon.md` | Make it reproducible and maintainable |
| `references/data-audit.md`, `winner-patterns.md`, `sources.md` | Four-source audit, examples, and source trail |
| `research/` | Optional reproducible audit of the downloaded 2,222-row table |

## How to use it

1. Paste the official event URL and deadline into your agent. Confirm eligibility, build window, prior-work policy, track restrictions, judging format, and required artifacts.
2. Ask for three ideas, a scorecard, and a clear reason to kill each losing option.
3. Pick one user workflow. Build a working vertical slice, then run a mock judge demo halfway through.
4. Start a draft submission as soon as the idea is selected. Keep it current while building.
5. Stop feature work before the deadline, record the real workflow, submit, and verify the exact entry judges will see.

The included time allocations and sample rubric are heuristics. A 24-hour in-person event and a six-week online challenge need different schedules. Rules, rubric weights, and sponsor terms can change; recheck official pages for each event.

## Evidence standard

The [data audit](references/data-audit.md) processes 2,222 Devpost submissions, their embedded GitHub README excerpts, **all 261,940 rows in a larger historical corpus**, a winner index, and official galleries. The [reproducible large-corpus audit](research/README.md#reproduce-the-large-corpus-audit) separates placement-like, participation, and ambiguous prize text and compares projects within events. Project pages are self-reported descriptions, not independent audits. Patterns are hypotheses to test against a new event, not causal proof or a recipe guaranteed to win. Current recommendations about a specific API, prize, or submission format require fresh verification.

## Contributing

Open a focused issue or pull request with the event date, official rule/rubric URL, named winner URL, proposed guidance change, and whether the point is a fact, a winner's self-report, or an inference. Avoid universal claims from one result. Keep the entry skill short and put details in the relevant playbook. See [CONTRIBUTING.md](CONTRIBUTING.md).

MIT licensed. See [LICENSE](LICENSE).
