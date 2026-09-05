# P06_AAS_PLUS_VETO_SUPPLEMENTAL_RECHECK.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S21)
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## AASP-VETO-01 — reliance veto

**Authoritative wording:** P06 is admissible as *evidence for a decision*, not as a design specification.
**Prior state:** PARTIALLY RESOLVED. Revised lift conditions were **(b′)** second-pass search on five remaining single-pass tree-scope negatives; **(c′)** P01 published and read; **(d′)** the filtered-build boundary accepted or resolved.

| Condition | Status now |
|---|---|
| (b′) five single-pass negatives re-searched | **NOT MET** — `is_internal_transfer`, `destination_journal_id`, `paired_internal_transfer`, `provider_reference` uniqueness, `chargeback\|dispute` still have one pass each |
| (c′) P01 read | **NOT MET** — still unpublished |
| (d′) filtered-build boundary | **RESOLVED, and the premise was wrong** — the tree was not filtered, it was **relocated**; 904 archived packs have now been searched (REV-E-16) |

**RECHECK: `VETO REMAINS`, materially narrowed.**
Released additionally this round: the **company-boundary position** (already released), the **version-invariance position** (six findings re-tested against v19), and the **evidence-base boundary** (archive searched, one wording change).
Still vetoed: anything resting on the five single-pass negatives, and anything requiring P01.

---

## AASP-VETO-02 — implementation veto

**Prior state:** REMAINS on three new grounds — the generation gap, `B-50`, and 26 undecided design items.

| Ground | Status now |
|---|---|
| **1. Generation gap** | **MATERIALLY WEAKENED.** Six core findings are cross-version invariant (`51_`). The research-invalidation risk is measured and largely retired. **Ground reduced but not removed** — the target generation is still undeclared, and `iEVING` evidence is v19 while the FK, sequence and numbering analyses are v18-only. |
| **2. `B-50`** | **STRENGTHENED, decisively.** The module is **`installed`** on a real Odoo 19 database (`58_`), exists in **17** copies, and a remediation module written in this programme states the destructive path **was exercised and produced user-visible breakage**. |
| **3. 26 design decisions undecided** | **UNCHANGED** |

**RECHECK: `VETO STRENGTHENED`.**
One ground weakened, one strengthened far more, one unchanged. **A design that adds settlement controls while a module capable of deleting the ledger by unauthorised SQL is installable in the same estate is not a design — it is decoration.** `DPG-R-01` / P08 `P08-T0-08` must be satisfied first.

---

## AASP-VETO-03 — evidence-base boundary at P11

**Prior state:** NEW. P11 must record the filtered-evidence-base boundary alongside each P06 negative.

**RECHECK: `VETO SUPERSEDED — MATERIAL NEW EVIDENCE`, and replaced.**
The premise — a *filtered* build — was wrong. The correct boundary is different and still real: **the live `addons_path` population is 791, the full v18 distribution is 1752, and P06's negatives were scoped to the loadable set.** Whether peers used the same boundary is unknown.

**Replaced by `AASP-VETO-04` — VETO on any P11 aggregation of negatives across processes until each declares its addons-path population.**
A unified "not found in v18" row built from one process searching 791 modules and another searching 1752 is a `count unit vs population` defect at programme scale. **P06 raises this against its own contribution.**

---

## AASP-VETO-05 — NEW: veto on treating this package's self-correction rate as settled quality

Sixteen author errors across four rounds; **twelve caught by something other than the author**. Four of this round's six overturned published conclusions.

**AAS+ position:** the correction rate is evidence of a working challenge process **and** an unresolved reliance question. **From inside the package the two cannot be distinguished.** `P06-B-58`.

**`VETO` on any statement that P06 is "well-verified" absent an independent audit.** The package may be relied on **finding by finding, with its citations checked** — which is what a Layer 2 audit package is for — and not as a whole on its reputation.

---

## Consolidated

| Veto | Prior | **Now** |
|---|---|---|
| **VETO-01** reliance | PARTIALLY RESOLVED | **REMAINS, narrowed** — two conditions unmet |
| **VETO-02** implementation | REMAINS on new grounds | **STRENGTHENED** |
| **VETO-03** evidence boundary | NEW | **SUPERSEDED — replaced by VETO-04** |
| **VETO-04** cross-process negative aggregation | — | **NEW** |
| **VETO-05** package-level reliance | — | **NEW** |

**One superseded, one strengthened, one narrowed, two new. No veto closed.**

---

## AAS+ position on the round

**AASP-F-12 — This round's most valuable output is a correction, not a discovery.**
`B-50` was already the headline. What this round added is that it is **installed**, in **17** copies, **rebranded**, **locally extended**, and **already cleaned up after once**. The finding did not change; **its status moved from a code reading to an operational fact.**

**AASP-F-13 — And the second most valuable output is that four published conclusions were overturned by searches round 3 declared unnecessary.**
The v19 tree, the addons archive, the PEP-552 headers, the database dump — **all were on the same disk the whole time.** Round 3 did not fail to find them; it failed to look, and said so confidently.

**AASP-F-14 — The severity model was built and it immediately earned its keep.**
Ranked by impact, `B-50` leads. Ranked by reachability, `B-10` leads — *"import a file twice"*. **Two different first actions.** A single list would have hidden one of them, and this package carried a single list for two rounds.
