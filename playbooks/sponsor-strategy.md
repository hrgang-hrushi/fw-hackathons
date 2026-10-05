# Sponsor challenge strategy

Sponsor prizes are event-specific. Read the current official prize text, technical docs, eligibility, required tags, and any track-entry limits. Do not assume a recurring MLH prize is present this year. Prefer one main prize and at most a small number of naturally compatible sponsor tracks.

| Challenge type | Product use that can matter | Demo proof | Pitfall |
| --- | --- | --- | --- |
| Gemini / multimodal AI | Understand a real image, document, audio, or workflow and produce an actionable result | Show input, model output, verification/human correction | Generic chat with no task improvement |
| ElevenLabs / voice | Voice is necessary for accessibility, hands-free work, or conversational practice | Live turn-taking, latency, interruption and fallback | Decorative narration |
| GoDaddy Registry / domain | Memorable domain tied to the product and accessible demo | Show registration and live route if rules require it | Buying a domain without product relevance |
| Auth0 / identity | Role-specific or protected workflow | Login, permissions, access boundary | Auth added solely as a badge |
| MongoDB Atlas / data | Meaningful persistence, search, aggregation, or sync | Create/retrieve real records | Database label with static content |
| Cloudflare / cloud app | Deployed app with edge or platform capability central to experience | Public route and platform trace | Untested deployment |
| Hardware / ARM | Physical device is essential to sensing or actuation | Device doing the task, recorded backup | Hardware dependency blocks demo |

Examples of these categories appeared on [HackTX 2025](https://hacktx2025.devpost.com/) and [LA Hacks 2025](https://la-hacks-2025.devpost.com/). TreeHacks 2025's ElevenLabs description explicitly favored creative and impactful voice uses. Treat these as examples, not current requirements.

## Sponsor fit test

Remove the sponsor tool from the architecture. If the outcome is effectively unchanged, either redesign the use or skip that track. Verify that a free tier or trial actually supports the planned demo, and record fallback behavior for quota or outage. Save a truthful integration receipt: relevant code path, sample input/output with secrets removed, screenshot or short clip, and limitations.
