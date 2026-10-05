# Make the work visible to a judge

A technically ambitious project can lose its meaning in a short demo if the interface only shows a final answer. Design the product, backend trace, and submission as three views of the **same user journey**. This is an execution pattern, not a claim that any one presentation choice causes a win.

## The proof chain

| Stage | Product screen | System evidence | Submission evidence |
| --- | --- | --- | --- |
| Need | Concrete user situation and input | Input schema, source or sensor | One-sentence problem and representative visual |
| Action | A clear button, command, or physical interaction | Request/job ID and accepted state | Short video clip of the real action |
| Work | Progress, current step, and any human decision | Named stages, timestamps, data/model/tool calls with secrets removed | Architecture sketch and one technical difficulty |
| Result | Output in the user's units, comparison, and next action | Stored result, calculation or trace, error bounds | Screenshot and measured result with method |
| Failure | Recoverable error or honest partial result | Timeout, retry, fallback, and reason | Limitation and what still needs work |

The three views must agree. If a dashboard shows live autonomous behavior while the backend uses a fixed sample, label it on screen, in the narration, and in the entry. If an ambitious physical sequence is unreliable, show the portion that works and identify the failed boundary; a truthful partial demo is better than an invented end-to-end claim.

## Interface rules

- Show the transformation, not only an attractive landing screen. A route, timeline, state board, comparison plot, or step list should correspond to real backend state.
- Translate technical quantities into the user's decision. Put the unit, baseline, and source beside a metric. Avoid impressive numbers with no measurement method.
- Use multiple views only when each answers a different judge question: *What is happening? Why did it happen? What can the user do next?*
- Keep the critical path short enough to complete in the judging window. Allow a safe reset so the same input can be demonstrated again.

## Backend rules

- Define each stage's input, output, success check, and error state. For concurrent work, show task ownership, completion state, and where results are merged.
- Use a state machine or job table when progress matters: `created → accepted → running → needs_review → completed/failed` is a useful starting vocabulary, adapted to the product.
- Record enough trace to prove a sponsor tool or algorithm contributed to the outcome. Remove credentials, private data, and internal reasoning from judge-facing logs.
- Test the exact demo fixture repeatedly, including one failure path. A successful screen recording alone does not prove an integration is reliable.

## Submission rules

Use a coherent sequence of visuals: **hero/result → input → process → outcome → architecture → limitation**. Caption each image with what the judge is seeing. The written story should answer why this user needs the product, what actually worked, how it was built, what broke and changed, and what is future work. Give collaborators specific credit. Include one direct demo route and a repository that explains how to reproduce it.

## Review gate

Ask a teammate unfamiliar with the project to watch the video with sound off, open the entry, and answer: Who is it for? What input went in? What system operation happened? What changed? Which claim is measured? What was simulated? If any answer is unclear, repair the product state or evidence before adding motion or extra features.
