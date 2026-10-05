# Working templates

Copy only the sections the current event needs. Replace every bracketed field with observed information or `unverified`. Keep one owner and timestamp per artifact.

## Event contract

| Field | Value / proof |
| --- | --- |
| Official event, organizer, rules URL | [ ] |
| Hacking start/end, timezone | [ ] |
| Registration and final submission cutoff, timezone | [ ] |
| Eligibility and team roster | [ ] |
| Prior work / AI assistance / open-source policy | [ ] |
| Judging format, time, location, attendance | [ ] |
| Exact published rubric and weights | [ ] |
| Required video, repo, deck, screenshots, tags | [ ] |
| Eligible overall and sponsor tracks; entry limits | [ ] |
| Question to organizer, owner, answer URL | [ ] |

## Prize evidence map

| Criterion / sponsor requirement | Planned feature | Evidence the judge can see | Source / owner | Status |
| --- | --- | --- | --- | --- |
| [exact rubric phrase] | [ ] | [live action, screenshot, measured value, code path] | [official rule URL / person] | [unverified / working / tested] |

Score a project only against the event's own criteria. For each criterion, record a 0–5 mock-judge score, confidence, gap, and next repair. If the event publishes weights, calculate `Σ(weight × score / 5)`; otherwise show the per-criterion scores without a fabricated overall number.

## Build and integration contract

```text
User input:
Output and next decision:
Minimum path (numbered):
Representative sample input/output:
Required data and its license:
Algorithm/model objective, baseline, units, failure case:
UI states: empty / loading / success / error / partial:
Client ↔ server contract and example JSON:
External API role, quota, timeout, fallback:
Storage entities, access rules, and seed method:
Privacy/security boundary and approval point:
Deployment URL and clean-start instructions:
One measurable test and its result:
```

## Task board and risk gate

| Task | Owner | Dependency | Demo impact | Cuttable? | Due before | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Core end-to-end route | [ ] | [ ] | Critical | No | [ ] | [ ] |
| Sponsor proof | [ ] | Core route | [ ] | Maybe | [ ] | [ ] |
| Submission draft | [ ] | Idea choice | Critical | No | [ ] | [ ] |

At each integration checkpoint, ask: **Does the core flow work on the demo device? Is the current submission valid? What one change raises the event rubric score most?** A failed core flow stops optional features. A submitted draft should stay valid while final polish continues.

## Demo storyboard

| Seconds | Screen/action | Spoken claim | Evidence | Backup |
| ---: | --- | --- | --- | --- |
| 0–10 | User scenario | [specific pain] | [real or cited input] | [static screenshot] |
| 10–30 | Input | [what is entered] | [visible app] | [recorded clip] |
| 30–90 | Transformation and result | [what changed and why] | [output / comparison] | [cached labeled run] |
| 90–120 | Technical proof and close | [mechanism, sponsor role, limitation] | [trace / metric] | [diagram] |

This is a two-minute *example*, not an event rule. Re-time it for the actual judging window. Record whether the live route and recording match the submitted entry.

## Reproducibility receipt

```text
Judged commit and timestamp:
Public repository URL and license:
Demo URL / test account instructions:
Required services, environment variables, and budget:
One-command or numbered setup:
Seeded/demo data declaration:
Tested browser/device and date:
Known limitations and fallback:
Video URL and visibility check:
Devpost submitted URL / timestamp / confirmation:
```
