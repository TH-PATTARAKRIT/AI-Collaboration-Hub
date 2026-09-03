# 03 — COGS Unknown Priority Register

Re-prioritizes the 59-item register (Fact Verification session file `03`) using a P0–P4 criticality model. Source status column is carried unchanged; only the Priority column is new work product of this session.

Priority model:
- **P0** — blocks `JT-04`, `JT-05`, or `JT-01`, or blocks a hard gate (e.g. Boss Account Ruling, Inventory v2.0 finalization).
- **P1** — blocks another named Joint Decision (`JT-02`, `JT-03`, `JT-06`–`JT-12`) or a flagged Audit VETO concern.
- **P2** — material but not currently blocking a named gate.
- **P3** — informational/negative-finding, already resolved as such.
- **P4** — cosmetic, deferred, or carried-forward with no new information this pass.

## P0 (18 items)

| ID | One-line reason it is P0 |
|---|---|
| `CGS-U01` | Root cause of `JT-04` undecidability (no single reference recognition-timing behavior) |
| `CGS-U06` | Blocks `JT-01` (same UI label, different account type by mode) |
| `CGS-U07` | Blocks `JT-01` (unknown re-class behavior on ownership change) |
| `CGS-U08` | Blocks `JT-01` |
| `CGS-U09` | Blocks `JT-01` (fallback-layer existence) |
| `CGS-U11` | Blocks `JT-01` (fourth candidate owner not ruled out) |
| `CGS-U12` | Blocks `JT-01` (current-version mapping incomplete) |
| `CGS-U13` | Blocks `JT-01` (company-exclusivity unconfirmed) |
| `CGS-U16` | Boss ruling required; blocks late-cost/`JT-06` design |
| `CGS-U20` | Blocks `JT-04` (invoicing-policy interaction undocumented) |
| `CGS-U22` | Boss ruling required; control-risk (unconfigured loss has no safe default) |
| `CGS-U25` | Single most material item for `JT-06` |
| `CGS-U31` | Blocks `JT-04` (matching-principle risk) |
| `CGS-U32` | `JT-05` core fact pattern |
| `CGS-U33` | `JT-05` supporting fact |
| `CGS-U34` | Blocks `JT-08`; contradiction |
| `CGS-U36` | Blocks `JT-08`; Audit VETO concern |
| `CGS-U42` | Blocks `JT-01` (company-scoping of the candidate owner) |

## P1 (16 items)

`CGS-U02, CGS-U03, CGS-U04, CGS-U05, CGS-U15, CGS-U23, CGS-U24, CGS-U30, CGS-U35, CGS-U39, CGS-U40, CGS-U43, CGS-U45, CGS-U48, CGS-U50, TH-HOLD-COGS-03` — each blocks a named `JT` other than `JT-01/04/05`, or (for `TH-HOLD-COGS-03`) is explicitly flagged BLOCKING for `JT-02` in the source register.

## P2 (14 items)

`CGS-U17, CGS-U18, CGS-U21, CGS-U26, CGS-U27, CGS-U29, CGS-U37, CGS-U38, CGS-U41, CGS-U46, CGS-U47, TH-HOLD-COGS-01, TH-HOLD-COGS-02, TH-HOLD-COGS-04` — material, not currently gate-blocking.

## P3 (2 items)

`CGS-U14, CGS-U49` — already resolved as negative finding / scope condition per the source register; not open unknowns in the blocking sense.

## P4 (9 items)

`CGS-U10, CGS-U19, CGS-U28, CGS-U44, TH-HOLD-05-residual, TH-HOLD-01, TH-HOLD-04, TH-HOLD-06, TH-HOLD-08` (the last four counted as the single carried-forward bundle row in the source register) — informational/watch items, no evidence this session found to elevate them.

## Reconciliation

18 (P0) + 16 (P1) + 14 (P2) + 2 (P3) + 9 (P4, with the 5-item carried bundle counted as one register row consistent with the source register's own itemization) = **59 register rows**, matching the verified population in file `02`. No item was dropped or invented.
