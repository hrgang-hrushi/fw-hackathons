# Full-cycle coverage checklist

Use this as a gap scan, **not** as an instruction to build every feature. Each line needs an owner and an evidence link or a clear “not applicable.” The event rules decide what is mandatory. Consult the focused playbook for implementation detail.

## Event contract and people

- [ ] Official event URL, organizer contact, hacking start/end, submission cutoff, timezone, and judging slot recorded.
- [ ] Eligibility checked: age, student status, geography, team size, account registration, attendance, and team-member addition.
- [ ] Build-window, prior-work, open-source, AI-assistance, hardware, data, and cross-submission rules understood.
- [ ] Track categories, sponsor entry limit, required technology, tags, evidence, and prize stacking checked.
- [ ] Judging format, time limit, rubric weights, accessibility needs, and presentation equipment known.
- [ ] Team roles, decision owner, conflict resolution, working hours, meals, rest, and handoff rhythm agreed.
- [ ] Accounts, credits, API access, device access, venue network, power, adapters, and backup connectivity verified.

## Problem and plan

- [ ] Target user and painful job stated with direct evidence or explicitly labeled hypothesis.
- [ ] Existing alternatives and precise difference documented; no unsupported “first ever” claim.
- [ ] Three ideas compared against eligibility, rubric, time, technical risk, and visible demo.
- [ ] One measurable outcome and a baseline chosen; measurement method can run within the event.
- [ ] One narrow judge-visible workflow sketched with input, transformation, result, and decision.
- [ ] Minimum build, cut list, ownership, integration checkpoint, freeze, and submission target set.
- [ ] Sponsor tool has a necessary role; account quota and fallback are known.

## Research, data, and algorithm

- [ ] Data source, license, provenance, freshness, consent, and permitted storage checked.
- [ ] Demo data is representative, anonymized if needed, and visibly marked when simulated.
- [ ] Algorithm inputs, outputs, assumptions, units, objective, constraints, and failure cases written down.
- [ ] Simple baseline implemented before advanced ML/agent/optimization claim.
- [ ] Evaluation examples include ordinary, edge, invalid, and adversarial inputs as relevant.
- [ ] Metrics report sample size, test method, uncertainty, and comparison, not invented impact.
- [ ] AI output is checked for unsupported claims; consequential actions have human review.

## Product and design

- [ ] Project name, one-line promise, logo/wordmark, screenshot/thumbnail, and visual system are coherent.
- [ ] First action is obvious; loading, empty, success, partial, and error states are legible.
- [ ] Text contrast, keyboard/focus behavior, labels, responsive layout, and motion reduction work.
- [ ] Animations explain a state change and do not delay task completion.
- [ ] The real device, browser, and projector view have been tested with a first-time user.
- [ ] Copy distinguishes live, cached, simulated, experimental, and future behavior.

## Engineering and operations

- [ ] One end-to-end path works before secondary features or platforms are added.
- [ ] Shared request/response contract and one integration fixture are agreed between teammates.
- [ ] Secrets remain server-side; `.env.example` exists; exposed credentials have been revoked.
- [ ] Inputs are validated; duplicate writes, timeout, API quota, provider outage, and retry behavior are handled.
- [ ] Storage schema, access rules, seeded records, and refresh behavior match the demo.
- [ ] Authentication/authorization is used only where needed and tested for role boundaries.
- [ ] Agent steps or jobs have explicit state, tools, stop conditions, error path, and execution trace.
- [ ] Deployment is reachable from a fresh browser and can be restarted from documented steps.
- [ ] Core flow, one bad input, one external failure, and a teammate's clean checkout have been tested.
- [ ] Hardware has spare power/components and a recorded fallback; sensors/calibration are labeled.
- [ ] Security/privacy review covers secret leakage, personal data, unsafe outputs, and third-party terms.

## Judging and submission

- [ ] Event rubric converted into evidence rows, including a visible sponsor integration receipt.
- [ ] Mock judge sees the app first, completes the workflow, and identifies top confusion points.
- [ ] Live demo script fits the actual time limit; backup video/screenshots exist.
- [ ] Video shows real use, readable UI, clear audio/captions, correct hosting/visibility, and required event intro.
- [ ] Slide deck is used only if required/useful and contains current behavior, architecture, evidence, limitations.
- [ ] Devpost draft has honest story, images, links, tech tags, tracks, team roster, and required fields.
- [ ] Submission owner verifies **the exact submitted entry** in a fresh browser before cutoff.
- [ ] Repo has working setup, lockfile, environment template, architecture note, license/credits, and known limits.
- [ ] Final deadline receipt, judged video link, repository commit, and demo URL are preserved.

## After the event

- [ ] Feedback mapped to the published rubric; judges and users are not quoted without permission.
- [ ] Public writeup credits teammates/assets and states what worked at judging time.
- [ ] Security and privacy shortcuts are fixed before inviting real users.
- [ ] Decide to archive or maintain; if maintaining, set one user metric and small contributor tasks.
- [ ] Data-source and sponsor terms are rechecked before using the project commercially.
