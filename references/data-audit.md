# Four-source audit: Devpost submissions, READMEs, winner index, galleries

Audit performed 2026-10-05. Counts below are from processing the downloaded source files, not the web preview. Public records and GitHub READMEs can change after a hackathon. These findings describe the observed collections; they do not establish what causes a team to win.

## 1. `twangodev/devpost-hacks`: complete pass over the released `all` table

[Dataset and card](https://huggingface.co/datasets/twangodev/devpost-hacks). File SHA-256: `dd4e1e564333c305f6faa029dbbe6ca99dfa99f32b8e9c8e45c88ea8d6d9a565`.

The released table has **2,222 rows, 2,222 distinct project URLs, and 363 rows with `is_winner=true`** across nine event configurations. The 363 labeled rows contain **252 distinct result strings**. The flag means Devpost marked *some* award as a win; it combines overall, sponsor, track, beginner, runner-up, and honorable-mention results. It is not a label for first overall or an exhaustive record of every award a project received. All rows had a nonempty description and a result string in this snapshot.

| Event slug | Rows | Labeled winners | README-bearing projects |
| --- | ---: | ---: | ---: |
| `cal-hacks-12-0` | 694 | 100 | 352 |
| `hackgt-12` | 272 | 25 | 171 |
| `hacktech-by-caltech-2026` | 61 | 0 | 46 |
| `madhacks` | 55 | 10 | 32 |
| `madhacks-fall-2025` | 111 | 13 | 77 |
| `pennapps-xxv` | 98 | 25 | 63 |
| `treehacks-2024` | 319 | 58 | 192 |
| `treehacks-2025` | 248 | 70 | 185 |
| `treehacks-2026` | 364 | 62 | 240 |

The Hacktech 2026 dataset card says winners had not been announced when scraped, so its zero is **missing outcome data**, not evidence that no one won. The [Cal Hacks 12.0 public gallery](https://cal-hacks-12-0.devpost.com/project-gallery) currently displays 699 projects, versus 694 in this snapshot. Do not call the released table a complete live census. The TreeHacks 2026 table has second- and third-place grand-prize labels but no first-place grand-prize label; do not infer that first place did not exist.

### What the full-table comparison says

These are simple proportions/means, not adjusted causal estimates. The mean event difference is the **unweighted average** of winner-minus-other differences within the eight events that contain both labels; it prevents one large event from fully determining the direction, but does not control for prize requirements or project quality.

| Public artifact signal | Labeled winners | Other submissions | Mean within-event difference |
| --- | ---: | ---: | ---: |
| Video link present | 87.1% | 76.8% | +14.6 percentage points |
| GitHub link present | 87.6% | 78.1% | +9.6 points |
| Embedded GitHub README present | 71.1% | 59.2% | +12.8 points |
| Mean description length | 808 words | 635 words | +145 words |
| Mean technology-tag count | 9.26 | 8.00 | +1.15 tags |

Descriptions often use Devpost's suggested sections regardless of outcome: a “challenges” phrase appeared in 80.4% of labeled winners and 79.6% of other entries. That phrase should not be treated as a differentiator. Longer writeups and more tags are **not** instructions to pad prose or stack complexity. Video, GitHub, and README availability may reflect event requirements, team resources, or judging selection. The actionable lesson is to meet the event's required evidence and make the core work inspectable.

Self-reported stack tags also fail to identify a universal recipe: `react` appeared on 131/363 labeled winners and 667/1,859 other entries (both about 36%); `python` appeared on 216/363 winners (60%) and 1,013/1,859 others (54%). Those differences do not account for event theme, sponsor tracks, or team skill. Choose a stack for the task and demo constraints, not because it appeared on a winning page.

## 2. GitHub READMEs linked in that table

The table contains **1,405 README objects for 1,358 projects**, representing **1,403 distinct repositories**. The dataset excerpts stop at 6,000 characters; 351 projects have at least one flagged truncated excerpt. We processed the text of all embedded excerpts and requested the current public `README.md` (with case variants) from each distinct repository. **1,363 full current READMEs were retrieved; 40 were unavailable** at those paths. A current README may differ from the judged version, and “unavailable” does not prove the repository is gone.

Among the retrieved current READMEs linked to labeled winners, median length was 401 words; among those linked to other submissions, 382 words. Using broad keyword checks, winner-linked READMEs mentioned setup in 48.7%, demos/media in 35.6%, architecture/stack in 33.7%, tests in 20.2%, limitations/future work in 4.1%, and licenses in 21.0%. For other-linked READMEs, the corresponding rates were 52.8%, 29.5%, 36.4%, 21.7%, 3.7%, and 21.6%. These are **current-document text signals**, not quality grades. They do not show a universal winner README template.

Deep reads of [FaceTimeOS](https://devpost.com/software/facetime-macos-ai-agent), [Dose](https://devpost.com/software/dose-ebmo9z), [3Docs](https://devpost.com/software/3docs), [HawkWatch](https://devpost.com/software/hawkwatch), [CodeCrack](https://devpost.com/software/codecrack), and [ChromaChord](https://devpost.com/software/chromachord) show different project shapes: voice-controlled desktop, sensor plus dashboard, PDF-to-3D guidance, video surveillance workflow, interview practice, and MIDI/music reasoning. The useful common denominator is a judge-visible user journey; no framework or algorithm is shared by all. The [3Docs README](https://github.com/r-thak/3Docs-MadHacks2025-Winner) explicitly describes cached API outputs for its reproducible demo, which illustrates why simulation and cached results must be labeled honestly.

## 3. HackWinnerDB

[Repository and data schema](https://github.com/notsointresting/hackwinnerdb), inspected at commit `dce17b1b222e9e3ad4d251f93e008c63527c2edb`. The checkout contains **4,174 entry YAML files, 3,936 project files, and 658 hackathon files**. Every entry has a source URL, but **4,163 entries are marked `unverified` and 11 `verified`** in the repository's own `verification.status` field. All 4,174 current entry files list Devpost as the source platform, despite the project's stated multi-platform scope. Use this as a discovery index and check each source URL before calling an award verified. Its data is [CC BY 4.0](https://github.com/notsointresting/hackwinnerdb/blob/main/DATA_LICENSE.md); retain attribution if using records.

## 4. Larger Devpost corpus and official galleries

[Large Hugging Face collection](https://huggingface.co/datasets/alvanlii/devpost-hackathon-projects), file SHA-256: `de43060e0a1c48d97e9e8dd963ca98d02270dc74031defc63179894f7ddb90b`. Its card says last updated January 2025. The downloaded Parquet has **261,940 project-event rows, 251,065 distinct project links, and 7,136 distinct event IDs**. There are 10,875 repeated project links across events but **no duplicate project-event pairs**. The accompanying event metadata has 9,207 entries, so not every listed event has a row in the project table. Only 474 of the 2,222 smaller-table URLs appear in this older/broader table.

The large table has 55,790 rows with a nonempty `prize` list, but that is **not a clean winner count**: the field includes participation awards and other noncompetitive labels. Team and prize data are serialized strings and need parsing/normalization. Its card does not state a reusable data license. Use it for broad historical coverage and candidate discovery, then verify outcome labels against event pages. Do not redistribute its descriptions or treat all `prize` values as victories.

For an event-level ground truth check, open its [public Devpost gallery](https://treehacks-2025.devpost.com/project-gallery), [rules](https://treehacks-2025.devpost.com/rules), and project pages. Galleries display current public submissions and award markers but may differ from an older snapshot. If you organize a Devpost event, its [management export](https://help.devpost.com/article/86-metrics-export-projects-data) supplies a project CSV, including custom form answers, subject to organizer access and privacy settings. No single public dataset found here covers every hackathon, every judged artifact, and every unpublished scoring note.

## Implications for this skill

1. Separate **overall placement**, **sponsor/track award**, **honorable mention**, **participation award**, and **missing outcome** before comparing projects.
2. Use within-event comparisons and published rubrics; do not infer causality from winner-page polish or tag counts.
3. Plan an accessible video, repository, and reproducible demo when required or beneficial, but never substitute documentation for a functioning product.
4. Treat current GitHub README content and team-authored Devpost descriptions as self-reports, and label cached or simulated data.
5. Refresh rules, prize definitions, and project links for every new event. Maintain source URL, capture date, and uncertainty with each example.
