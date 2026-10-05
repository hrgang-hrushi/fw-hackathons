# Frontend, UI/UX, branding, and motion

Design the judging route first: a clear landing or start state, one obvious action, visible progress, result, and a next step. Use realistic copy and data. Give the project a short memorable name, one-line value proposition, simple wordmark or icon, consistent palette/type, and a legible thumbnail. Visual identity should clarify the product, not consume the build window.

If the backend runs a sequence of steps, map those steps to interface states. A polished dashboard earns its space by revealing decisions, progress, and evidence; each view should answer a specific user question. Use the [proof chain](judge-visible-proof.md) to keep the screens aligned with what the system actually does.

## Minimum usable interface

- Establish a small design system: spacing scale, type hierarchy, 2–3 semantic colors, button/input/card states.
- Keep text contrast, focus visibility, labels, keyboard flow, and touch targets usable. Include responsive layout for the demo screen size.
- Design empty, loading, success, error, and partial-result states. Show what data is simulated.
- Put proof near the result: source, comparison, confidence, or calculation when relevant.
- Test the real judge journey on the actual browser/device and projector resolution.

## Motion

Animate state changes that explain cause and effect: input accepted, process advancing, result revealed. Prefer short, consistent transitions; support reduced-motion preferences. Avoid long intros, scroll tricks, and effects that hide latency or interfere with screen recording. If animation breaks, the workflow must remain understandable.

## Quick critique

Have someone unfamiliar with the project attempt the core task without instruction. Note the first wrong click, unreadable label, delayed feedback, and unclear result. Repair those before cosmetic refinement.
