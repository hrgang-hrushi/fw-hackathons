# Backend, database, and orchestration

## Reliable core

Define a narrow API contract for the demo path. Validate inputs and return actionable errors. Use durable storage only where the product needs persistence; otherwise a labeled seeded dataset may be safer. If storage matters, sketch entities, keys, access rules, and one representative query before implementation. Keep migrations and seed instructions repeatable.

For external APIs, verify credentials and a real request early. Add timeouts, bounded retries, idempotency for writes, and a visible fallback. Keep budgets for API calls, tokens, and rate limits. Never put a secret in frontend code, screenshots, logs, or repository history.

## Orchestration choice

Use a straightforward function or state machine for a short deterministic flow. Introduce a queue for work that exceeds request timeouts or needs retries. Introduce multiple agents only when roles, tools, or permissions are materially distinct; define each agent's input/output, stop condition, handoff, and approval boundary. Log a concise execution trace useful for debugging and judging. Human confirmation belongs before irreversible or consequential actions.

When workers run in parallel, assign each task a stable ID and owner, persist its state, and use a single merge point. Make the UI's status come from that state rather than a decorative animation. Test what happens if one worker fails or finishes twice. For physical systems, isolate sensor, control, and UI layers so a failed device does not erase the rest of the demo.

## Data integrity and privacy

Use the smallest data needed. Ask permission to collect user data, anonymize demonstration records, and document retention and deletion if the app stores them. For AI retrieval, distinguish source text from instructions and validate generated structured outputs. For third-party data, record license and provenance. For finance/health claims, show assumptions and uncertainty rather than a false precision.

## Integration drill

With a fresh environment, run the main flow, one bad input, one provider failure, and one refresh/retry. If a teammate cannot reproduce it from the README, fix setup before adding features.
