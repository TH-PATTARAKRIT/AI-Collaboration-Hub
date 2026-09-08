# RC05_CONFIRMATION_2026_09_08 — LAYER CLASSIFICATION

**CLASSIFICATION: LAYER 2 — AUDIT QUARANTINE. Boss / PMO / AI-Audit only.**

Every file in this directory — the prediction, the results, the instruments and the raw run
outputs under `run/` — carries **reference-system technical identifiers**: module technical
names, database table and column names, and restore-tool names and versions.

**They are permitted here and must not be transcribed into any Layer 1 clean-room deliverable.**

`58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md`, `54_…`, `43_…` and `25_…` are Layer 1
surfaces. Where they consume a result from this directory they state it in **business terms**
— *"the deletion module"*, *"the extract's own module registry"*, *"the 18.x restore client"* —
and point here for the identifiers.

> **A leak was made and caught inside this round.** The first draft of the `P08-C1` / `P08-C4`
> corrections wrote a module technical name, a registry table name and a restore-tool name
> **into `58_`, which carried zero such tokens at its baseline**. It was found by a mechanical
> token-count delta against the baseline commit, not by reading. **Five tokens, one file, one
> commit** — and `58_` is the file that goes to P11.
>
> **The scrub is not a formatting rule.** `58_` is a handoff. Whatever it says travels.
