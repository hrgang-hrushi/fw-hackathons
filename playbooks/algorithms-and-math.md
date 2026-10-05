# Algorithms, math, and evidence

Use formal methods when they explain the product's advantage. Avoid adding an algorithm merely to sound technical.

## Choose the right core

| Task | Candidate method | Baseline and proof |
| --- | --- | --- |
| Ranking or matching | Weighted features, constraints, bipartite matching | Compare against first-come or simple keyword match |
| Routes or schedules | Shortest path, integer constraints, heuristic search | Compare travel/time/cost and check feasibility |
| Forecast or classification | Simple rule/statistical model before complex ML | Holdout examples, confusion matrix or error |
| Retrieval over documents | Keyword baseline, embedding retrieval, cited answers | Known-question set, source accuracy, abstention |
| Optimization | Explicit objective, constraints, sensitivity analysis | Feasible baseline and changed objective value |
| AI agents | State machine/tool workflow before multi-agent split | Task completion, latency, cost, failure rate |

## Mathematical contract

Write the input set, output, objective, hard constraints, units, assumptions, complexity or latency budget, and one failure case. For example, a recommendation score `S(x)=Σ w_i f_i(x)` is useful only if features are normalized, weights are justified, and hard exclusions are checked separately. Report measured values from a reproducible sample; label illustrative numbers.

For several competing objectives, define a quality floor and compare feasible options across latency, cost, energy, or another meaningful quantity. A Pareto chart can show which choices are dominated; the UI should still explain the recommended tradeoff in ordinary user terms. Record how each quantity was measured and avoid presenting a calculated estimate as a sensor reading.

For LLM features, create a small fixed evaluation set with positive, negative, and adversarial examples. Track whether the model completed the user task and whether its claims are supported. Show uncertainty, citations, or human approval when wrong output has consequences. Do not expose private chain-of-thought or claim validated accuracy without a test.
