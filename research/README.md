# Reproduce the small-dataset audit

This research utility is optional. The skill itself needs no dependencies. The original dataset and GitHub READMEs are **not bundled** because their content does not share one reusable license. Download from [the dataset's source page](https://huggingface.co/datasets/twangodev/devpost-hacks), read its licensing notes, and retain the source URL when publishing analysis.

1. Install Python 3.10+ and `pyarrow` in a separate research environment.
2. Download `data/all/train.parquet` from the linked dataset into a local file.
3. Run `python research/audit_small_dataset.py /path/to/train.parquet` from this package's parent directory.

The script processes every row and embedded README excerpt, checks duplicate project URLs, and reports per-event winner, video, GitHub-link, and README coverage. Compare its output with [the dated audit](../references/data-audit.md). The dated audit also used current GitHub READMEs, the larger historical dataset, HackWinnerDB, and event galleries; this small script does not refresh those sources or verify prize categories.

The original files audited on 2026-10-05 had these SHA-256 values:

- Small Parquet: `dd4e1e564333c305f6faa029dbbe6ca99dfa99f32b8e9c8e45c88ea8d6d9a565`
- Large Parquet: `de43060e0a1c48d97e9e8dd963ca98d02270dc74031defc63179894f7ddb90b1`
- HackWinnerDB Git commit: `dce17b1b222e9e3ad4d251f93e008c63527c2edb`

An updated release can yield different counts. Verify any current winner, sponsor, or rule claim on the corresponding official event page.
