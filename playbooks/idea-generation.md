# Idea generation and selection

## Intake questions

Who has a painful task? What happens today? What can the team access and demonstrate legally within the build window? What single action should a judge be able to perform? Which event criteria and sponsor requirements apply? What prior work is allowed?

## Generate three different approaches

For each, write: **user → trigger → input → transformation → visible outcome**. Include (1) a simple dependable idea, (2) a differentiated technical idea, and (3) a surprising interface or workflow idea. Search for existing solutions and cite them when novelty matters. Avoid treating a technology label as the problem.

## Filter and score

Reject any idea that violates eligibility or requires unavailable private data, hardware, approval, or API access. Then score 0–5 on problem evidence, rubric fit, feasibility, visible demo, technical differentiation, sponsor fit, and risk. A possible planning score is `0.20 problem + 0.20 rubric + 0.20 feasibility + 0.15 demo + 0.15 differentiation + 0.10 sponsor`; change weights to the actual rubric. Add a confidence note beside each score. The goal is to expose tradeoffs, not create fake precision.

Test the winner with a 30-second verbal pitch, a paper sketch, and one real input. If the judge-visible outcome cannot be explained in one sentence, narrow it. Interview or observe at least one relevant user when feasible; never claim validation from an invented persona.

Before committing, answer three linked questions: **What will the user care about? What nontrivial operation produces that result? What screen or physical action proves it happened?** A concept with only a striking interface or only a sophisticated backend is missing part of the judge-visible path.

## One-page build contract

```text
Event / deadline / timezone / rules URL:
Target prize(s) and explicit eligibility:
User and painful job:
Current workaround and why it fails:
One-sentence product promise:
Demo input → computation → result:
Core metric and baseline:
Minimum live path (3–5 steps):
Data and permissions:
Sponsor tool's indispensable role:
Architecture sketch and owner per component:
Must work / may cut / will not build:
Integration checkpoint / feature freeze / submission target:
Failure fallback and honest disclosure:
```
