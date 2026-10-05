# Technical architecture

## Start with the demo path

Draw: **user action → UI → API/function → data/model/service → returned result → user decision**. Mark which parts are live, cached, mocked, or future. Identify the slowest and most fragile boundary. Make the first version run end to end with representative input before adding more components.

## Stack selection

Choose tools the team can deploy and debug within the event. Evaluate familiarity, sponsor requirement, deployment friction, latency, offline needs, cost, data sensitivity, and teammate ownership. Typical valid shapes include a single web app with server routes and managed storage; a mobile client with a small API; or a browser UI with a Python service when ML libraries are central. No stack is inherently prize-winning.

## Boundary contracts

- Define one shared example request and response for each important boundary, including error and loading states.
- Keep secrets on the server. Use an environment template, not committed keys.
- Separate domain logic from vendor adapters so an API failure can return a useful fallback.
- Add telemetry only for what helps diagnose demo failures; avoid collecting sensitive data unnecessarily.
- Use a seeded demo dataset when access to real data is unreliable, label it, and preserve a live path through the core transformation.
- Make setup reproducible: pinned or locked dependencies, one documented start path, and test credentials or instructions when permitted.

## Architecture review

Can a judge use the product unaided? Can a teammate explain each component's necessity? What happens on timeout, malformed input, lost network, duplicate request, and refresh? What would be cut if only two hours remained? A clean vertical slice is stronger evidence than a diagram of unbuilt services.
