# P01 — CURRENT STATE RECONCILIATION

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-TARGETED-CROSS-PROCESS-CLOSURE-001`
Execution: **TARGETED CONTINUATION — NO RESET.**
Layer: **1.**

This document reconciles what P01 held at the end of the previous round with what this
continuation established. **Nothing from rounds 1 or 2 is discarded.** Superseded conclusions
are marked superseded and their originals are preserved in
`P01_RESEARCH_ERROR_AND_REVISION_LOG.md`.

---

## 1. LINEAGE

| Round | Prompt | Outcome | Commits |
|---|---|---|---|
| P01#01 / #02 | `…-ACC-P01-P2P-REV2-001` | 25 files; `RECOMMEND HOLD`; 11 contradictions, 0 closed | `6069921`, `46146a4`, `8e1dfb0` |
| Mid-round correction | `…-ACC-REV2-CORR1` (SCOPE-AWARE) | Applied as a delta; scope matrix added; 2 findings restated | in the above |
| **This round** | `…-TARGETED-CROSS-PROCESS-CLOSURE-001` | this document and its siblings | this commit |

**All three commits remain unpushed** — see §6.

---

## 2. WHAT THIS ROUND CHANGED IN P01's OWN CONCLUSIONS

| Prior conclusion | Status now | Why |
|---|---|---|
| *"The receipt-to-bill bridge has no physical structure to run on in the v19 deployments"* | **SUPERSEDED — refined** | v19 has a complete receipt-valuation mechanism; the counter-account moved from the item category to the **location**, and the valuation record onto the movement. The bridge is **unconfigured**, not absent. `ERR-P01-07` |
| *"14,441 movements, zero journal links"* offered as proof the bridge never fires | **SUPERSEDED — qualified** | That database has **16 journal entries in total**. The zero is corroborating, not decisive; the **configuration** evidence carries the finding. `ERR-P01-08` |
| Module denominator = direct dependencies | **SUPERSEDED — corrected** | Transitive closure: 12→35 (`R1`), 17→45 (`R3`). Landed cost and subcontract purchase were both outside the old set. `ERR-P01-04` |
| Three-way match is a report, not a control | **RE-SCOPED, then CORRECTED** | First re-scoped as installed nowhere; **that was false** — it is installed in the fourth database, which this package wrongly recorded as unreadable (`ERR-P01-15`). The *advisory, not a control* finding itself is unaffected |
| The custom effective-date backdating tool is a severe risk | **RE-SCOPED — latent** | Not installed in any readable deployment |
| A second withholding mechanism exists | **RE-SCOPED** | The multi-payment withholding module is installed **nowhere**; the single installed path is the one carrying the arithmetic defect |
| Cross-company auto-generation is tolerance-zero | **ESCALATED — LIVE** | Both intercompany bridges are **installed in both v19 deployments** and in neither v18 one |
| Vendor advances are bill-first in the base | **EXTENDED** | The project's custom vendor-advance module is **installed in all three** deployments, and its two copies **behave differently** |
| "No peer process exists" | **SUPERSEDED** (already corrected in round 2's addendum) | Ten peer packages are published |

**Nothing above withdraws a verified fact.** Every superseded item was superseded by *more*
evidence, not by reinterpretation of the same evidence.

---

## 3. WHAT THIS ROUND ADDED

| # | Addition |
|---|---|
| 1 | **Installed-module evidence** from the deployed databases — the single most useful new instrument, because it separates *source capability* from *deployed reality* for all 65 population members |
| 2 | The v19 receipt mechanism traced positively, not just as an absence |
| 3 | **The v19 valuation chart is entirely unwired**: category valuation account 0/37, category valuation journal 0/37, location valuation account 0/525, account-level variation account 0/544 — while **perpetual valuation is declared on 27–28 of 37 categories** |
| 4 | **A regression in failure behaviour**: v18 refuses a receipt when accounts are missing; v19 silently posts nothing |
| 5 | Peer intake across ten published packages, with two peer findings independently re-derived |
| 6 | The vendor-advance ownership question answered for P05 |
| 7 | Two further self-caught research defects logged (`ERR-P01-07`, `ERR-P01-08`) |

---

## 4. WHAT REMAINS EXACTLY AS IT WAS

Preserved unchanged, as audit lineage:

- All 53 evidence items `EV-P01-01`…`EV-P01-53` from the previous round.
- All 11 contradictions — **none was closed by the previous round, and this round closes none
  either**; it adds evidence to several and escalates two.
- All six prior research-error records.
- The scope matrix and its seven unresolved scope questions.
- The tolerance-zero disposition on cross-company financial ownership — **now escalated from
  latent to live**.

---

## 5. THE CENTRAL FINDING, STATED ONCE

> The two deployed v19 systems declare **perpetual inventory valuation** and wire **no accounts
> to receive it**. Goods are received, a value is computed and stored on the movement, and
> **nothing reaches the ledger** — with no error and no warning, because the generation that
> would have refused the receipt was replaced by one that silently does nothing.
>
> The **v16** deployment, by contrast, shows a receipt-time bridge operating on about half its
> receipts. **There is no readable deployed v18 database in this estate** — see `ERR-P01-09`.

---

## 6. PUBLICATION STATE

**PUBLISHED.** The push was refused by the environment's permission classifier in the previous
round; it **succeeded in this round**. All four P01 commits are on the remote research branch
`research/account-p01-procure-to-pay-2026-09-04-001`, head `366a6ea`, 48 package files.

This discharges P01's part of P11's `DEP-23` (*P01–P10 publication — peer dependency open × 10*).

Peer **P06** recorded that its P01-facing ownership assignments were made against the Boss
prompt rather than a published P01 package, and that any conflict discovered on publication
supersedes its file. **That caveat is now actionable**: P06 should re-read its P01 assignments
against this package.
