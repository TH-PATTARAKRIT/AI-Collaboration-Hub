# 30 — COGS Material Unknown / Conflict Register

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `OPEN-ITEM REGISTER — NOTHING BELOW IS CLOSED BY THIS SESSION`

---

## 1. Purpose and Severity Legend

This register consolidates every material `HOLD`, `PROVISIONAL`, and `CONFLICTING` item raised across files `02`–`29` into one place, so nothing is lost between files and nothing is silently resolved by omission. Every item here is surfaced again in file `33` (Final Report) and file `34` (Next Controlled Action and Owner Matrix). Nothing in this register is resolved, accepted, or closed by this session.

- `BLOCKING` — a downstream Joint decision or design step cannot proceed without it.
- `MATERIAL` — must be decided before a COGS Final Solution can be produced, does not block this package itself.
- `CONFLICTING` — two or more sources in this package's own evidence disagree and were not reconciled.
- `WATCH` — monitor; no decision needed yet, but could become material.

---

## 2. Version / Terminology Instability

| ID | Item | Severity | Source Files | Routed To |
|---|---|---|---|---|
| `CGS-U01` | The reference ERP's "Perpetual" accounting pattern is not one stable mechanism across its major-version history — pre-19 posts real-time at every physical stock movement; version-19+ posts at the invoice/bill level only, with the closing process demoted from primary mechanism to gap-filler. Independently corroborated across at least seven files. | `BLOCKING` | `02`, `06`, `09`, `12`, `13`, `14`, `16`, `18` | `JT-03`, `JT-04` |
| `CGS-U02` | "Manual/Automated" (pre-19) is not confirmed to be a simple rename of "Periodic/Perpetual" (19.0) — the ownership model itself flips: pre-19 is category-native with a company-level visibility gate only; 19.0 (reconstructed) is company-default with category-level override. | `MATERIAL` | `02` §4.1, `03` §4 | `JT-01` |
| `CGS-U03` | Price Difference Account scope is `CONFLICTING` across the version range: one source ties it to Standard Price only; another describes it applying to FIFO/AVCO "cost adjustments" also; a further secondary source describes removal-then-reintroduction with narrower scope, and a distinct "Variation Account" reported new in 19.0 that may or may not be the same concept. | `MATERIAL` / `CONFLICTING` | `02` §7, `04` field `B-08`, `15` §6, `17` §6, `21` §4.3 | `JT-02` |
| `CGS-U04` | The entire version-19.0 Finance/Accounting Menu A field set rests on search-index reconstruction, not a successful direct page fetch (two attempts failed with empty-content errors). Every `19.0`-specific field/default in files `02`, `03`, `04` carries `PROVISIONAL, REQUIRES DIRECT-FETCH RE-VERIFICATION`. | `BLOCKING` for any `19.0`-pinned design | `02`, `03` §3, `04` | Pre-Joint re-fetch pass |
| `CGS-U05` | Whether pre-19 category-level `Automated`/`Manual` labels still exist as-is on the 19.0 category form, or were collapsed into the company-level setting only, is `UNKNOWN`. | `MATERIAL` | `13` §3 | `04` follow-up |

---

## 3. Menu A–D (Settings / Category / Product / Chart of Accounts)

| ID | Item | Severity | Source Files | Routed To |
|---|---|---|---|---|
| `CGS-U06` | The "Expense Account" field is expected to hold two structurally different account types depending on configuration — Current-Asset type under Periodic/Manual, Expense/Cost-of-Revenue type under Perpetual/Automated — under the *same field label*. A configuration carried across modes without re-pointing this field misclassifies the account on the financial statements. | `BLOCKING` control risk | `03` §2.5, `04` field `B-04`, `05` §7 | `JT-01`, `JT-02` — SMEsPlus must design an explicit mitigation, not inherit the ambiguity |
| `CGS-U07` | No evidence confirms whether the reference ERP automatically re-classes an existing product's accumulated Stock Valuation Account balance when its Product Category is reassigned (Case 8, precedence matrix). If it does not, category reassignment risks stranding un-reconciled inventory value. | `BLOCKING` | `11` §4, `28` V-4 | `JT-01`; needs live-instance verification, documentation-only research cannot resolve |
| `CGS-U08` | Consolidated "effect of changing category/policy/account on existing stock and already-posted transactions" — costing method, valuation cadence, account re-pointing — has no confirmed documented mechanical answer anywhere in the material reviewed (automatic revaluation vs. silent divergence vs. prospective-only). | `MATERIAL` | `04` §12, `05` §11, `07` field sheet, `08` §2.6 | `JT-01`, `JT-02`; SMEsPlus must decide this on its own terms |
| `CGS-U09` | Whether a Journal-level fallback account exists below Category when both Product and Category Income/Expense Account fields are blank is `PROVISIONAL` — community-repeated but not officially confirmed; an alternative reading (hard block requiring configuration) is equally plausible and arguably more control-conscious. | `MATERIAL` | `05` §7 | `JT-01` |
| `CGS-U10` | Whether the "Show Accounting Features" visibility gate on the category form existed identically pre-19.0 is `PROVISIONAL` — confirmed only for 19.0 Community Edition. | `WATCH` | `04` field `B-00` | none — informational |
| `CGS-U11` | Whether Fiscal Position tax/account mapping can override even an explicit product-level Income/Expense Account, or only substitutes for the Category/Journal fallback levels, is `HOLD`. | `MATERIAL` | `05` §7 | `JT-01` |
| `CGS-U12` | Full field-by-field mapping of the 19.0 account model ("Stock Input Account" reported Cost-of-Revenue-typed in one fetch summary, but the reliable directly-quoted 18.0 citation says Current Assets — the 19.0 claim is discarded as a fetch-summarization artifact, not treated as unresolved conflict, but the underlying 19.0 field-by-field mapping remains incomplete). | `MATERIAL` | `06` §2.2, §3 | Pre-Joint re-fetch pass |
| `CGS-U13` | Whether the Continental/Anglo-Saxon accounting-package setting is strictly company-level-exclusive, with no per-category override, is `PROVISIONAL`, not independently re-verified. | `MATERIAL` | `06` §2.8 | `JT-01`, `25` |

---

## 4. Menu E–H (Reporting / Closing / Vendor-Customer Flow / Loss-Production)

| ID | Item | Severity | Source Files | Routed To |
|---|---|---|---|---|
| `CGS-U14` | No dedicated "Close the Stock Period" wizard exists anywhere in the reference ERP's documentation across the versions reviewed. Closing is a cadence configuration (Manual/Daily/Monthly) plus either a server-action or a fully manual journal entry. | `MATERIAL` (informational — a genuine negative finding, not a gap in this research) | `08` §1 | `JT-07` |
| `CGS-U15` | Whether the documented "Option 1 (server action)/Option 2 (manual journal entry)" closing mechanisms describe routine recurring closing, a one-time Periodic-to-Perpetual migration procedure, or both, is unresolved — they appear under a heading complex that also covers an "Upgrade process for Anglo-Saxon Perpetual." | `BLOCKING` for `JT-07` scoping | `08` §2.3 | `JT-07` |
| `CGS-U16` | No mechanism was found to attribute a late-arriving supplier cost back to the specific prior-period COGS it should have affected — it is simply absorbed into the current period's Variation account at the next close. | `BLOCKING` | `08` §2.7 | `JT-06` |
| `CGS-U17` | Whether the general Lock Date mechanism interacts correctly with a scheduled (Daily/Monthly) Periodic closing entry attempting to post into an already-locked period (refuse vs. auto-redate) is `HOLD`. | `MATERIAL` | `08` §2.6, `09` §9 | `JT-06`, `JT-12` |
| `CGS-U18` | Negative/zero-cost exception handling is confirmed only for AVCO under Perpetual, version 19.0. FIFO and Standard-Price negative-cost behavior, and true zero-cost-basis behavior, are unconfirmed. | `MATERIAL` | `07` §2.9 | file `15` follow-up |
| `CGS-U19` | Whether a drill-down from a valuation-report row reaches directly into the source vendor bill/customer invoice line, or only as far as the stock move, is `HOLD`. | `WATCH` | `07` §2.6 | informational |
| `CGS-U20` | Invoicing-policy (ordered vs. delivered quantities) interaction with the Periodic/Perpetual value-trigger table is entirely undocumented in evidence retrieved — a material unresolved interaction between two independently documented configuration axes. | `MATERIAL` | `09` §7.1 | `05`, `18` follow-up |
| `CGS-U21` | Whether any reference version enforces a hard block on bill-before-receipt or invoice-before-delivery posting at the accounting layer, versus leaving it entirely to a separate 3-way-match procurement control, is `HOLD`. | `MATERIAL` | `09` §4 | `JT-06` |
| `CGS-U22` | The reference ERP's "loss is not COGS" separation is configuration-dependent (a distinct Inventory Loss location + Loss Account must be deliberately set up); no documented fallback account was found for an *unconfigured* loss. "Scrap defaults to non-COGS" is not a safe unconditional reading. | `BLOCKING` control risk | `10` §2.4, `20` §5 | `JT-01`; SMEsPlus must design an explicit safe default |
| `CGS-U23` | Whether "Accounting Information" location-level overrides generalize beyond the Inventory Loss location case to every location type is `PROVISIONAL` — only the Inventory Loss case was independently confirmed with a quoted field. | `MATERIAL` | `10` §5.1 | `11` follow-up (third inheritance axis) |
| `CGS-U24` | Whether SMEsPlus's Product-Category/Product precedence matrix must be extended to a third, location-keyed axis (alongside Category and Product) is flagged but not decided — `C-H4`. | `MATERIAL` | `10` §9, `29` S3 | `11` follow-up |

---

## 5. Periodic / Perpetual / Costing Method Models

| ID | Item | Severity | Source Files | Routed To |
|---|---|---|---|---|
| `CGS-U25` | Whether Periodic has any dedicated "received, not billed" or "billed, not received" accrual visibility mechanism, or only discovers the gap at close, is `HOLD` — the single most material item file `12` surfaces for `JT-06`. | `BLOCKING` | `12` §6, §11 | `JT-06` |
| `CGS-U26` | Return handling before/after closing under Periodic specifically is `HOLD` — Layer A evidence for this exists mainly under the Perpetual/Anglo-Saxon pattern, not Periodic. | `MATERIAL` | `12` §5 row 8 | `19` follow-up |
| `CGS-U27` | Whether write-down/loss/scrap/adjustment is distinguished from ordinary COGS under Periodic specifically (as opposed to collapsed into the single Variation Account) is `HOLD`. | `MATERIAL` | `12` §5 row 9 | `20` follow-up |
| `CGS-U28` | Exact literal formula wording (or its absence) for "COGS as a period residual" was not found verbatim in any documentation page reviewed — the identity is a corroborated pattern, not a directly-quoted statement. | `WATCH` | `12` §9 | `27` |
| `CGS-U29` | Existing-stock conversion mechanics on a costing-method change are confirmed *away from* Standard Cost only (existing stock keeps its old value; only forward movement adopts the new method); AVCO- and FIFO-specific change behavior (both directions) is `HOLD`. | `MATERIAL` | `15` §7 | `JT-02` |
| `CGS-U30` | Bill-before-receipt under Perpetual is the weakest-evidenced purchase-side timing sub-case in the whole package — inferred only by structural symmetry, never independently confirmed. | `MATERIAL` | `17` §7, §10 item 1 | `JT-06` follow-up fetch |
| `CGS-U31` | Whether invoice-before-delivery is permitted, gated, or warned against under either Perpetual regime is `HOLD` — if the literal 19.0+ rule is read strictly, COGS could be recognized before goods leave the seller's control, a matching-principle risk. | `MATERIAL` | `13` §7 row 6, `18` §6.2 | `JT-04` |

---

## 6. Returns / Adjustment / Scrap / Landed Cost / Manufacturing

| ID | Item | Severity | Source Files | Routed To |
|---|---|---|---|---|
| `CGS-U32` | **JT-05/C-03 — the single most material carried-forward item in this package.** Reference evidence shows AVCO returns are valued at *current* average cost (not original), with the average never recalculated on return; FIFO layer-consumption on return is only community-corroborated, not primary-documented; a documented, un-reconciled discrepancy exists between a credit note's financial-reversal amount and the independently-computed inventory-valuation reversal ("manual adjustment" is the reference system's own stated resolution); a later-period return carries three independently-settable dates (original sale, physical return, credit-note reversal date) with no forced alignment. | `BLOCKING` | `19` §2, §6, `09` §7.3 | `JT-05`/`C-03` |
| `CGS-U33` | The reference ERP's own feature-level "Returns and refunds" documentation is completely silent on cost basis; the valuation answer must be assembled from a separate, non-cross-referenced documentation surface — a genuine usability/evidence gap in the reference system itself. | `MATERIAL` (informational) | `19` §2 | `JT-05` |
| `CGS-U34` | Exact posting mechanism for a landed-cost residual on fully-sold stock is `CONFLICTING` — one source says it auto-books to COGS; another, attributed to 19.0+, says it requires a manually-generated entry via a dedicated Landed Cost Clearing account. | `BLOCKING` for `JT-08` | `21` §3.3, `30` (this item) | `JT-08` |
| `CGS-U35` | Whether Standard-Price products can receive landed cost at all is `HOLD` — the documented Landed Costs feature's eligibility is gated to AVCO/FIFO categories; no worked example was found for a landed-cost-shaped bill applied to a Standard-Price product. | `MATERIAL` | `21` §4.2 | `JT-08` |
| `CGS-U36` | **Scenario 11 (landed cost after full sale) is the single most material item in the 32-scenario register**: version-inconsistent destination account (COGS vs. remaining in the original freight/expense account vs. at least one reported case with no journal entry generated at all — a control break). | `BLOCKING` | `16` Scenario 11, `21` §3.3 | `JT-04`, `JT-08`; Audit VETO concern |
| `CGS-U37` | No documented production/manufacturing standard-cost variance posting mechanism exists — a sharp asymmetry against the well-evidenced purchase-side Price Difference Account. If SMEsPlus ever supports Standard Cost for manufacturing, no reference precedent exists to adapt. | `MATERIAL` | `22` §6 | `JT-02`, `JT-09`; original design work required |
| `CGS-U38` | Whether the two documented WIP mechanisms (always-on Production-location clearing vs. 19.0-only manual "Post WIP Accounting Entry") coexist or are mutually exclusive on the same manufacturing order was not found in any page retrieved. | `MATERIAL` | `22` §4.2 | `JT-09` |
| `CGS-U39` | NRV/write-down/impairment is `NOT PRESENT IN THIS VERSION` as a named reference-ERP feature across all versions searched — but is independently `AUTHORITATIVE` under Thai TAS 2 (full worked examples, file `24` §2.3). SMEsPlus has no reference-UI pattern to study for this and must design it from Thai evidence alone. | `BLOCKING` | `20` §6, §7, `24` §2.3 | Original design work; Thai evidence is the only source |

---

## 7. Period Close / Cut-Off / Multi-Company

| ID | Item | Severity | Source Files | Routed To |
|---|---|---|---|---|
| `CGS-U40` | The Inventory-side movement-date period guard, even fully in force, is necessary but not sufficient for an Accounting close — it does not by itself supply a population-query surface for unmatched valuation facts (GAP-1), late-cost period authority (GAP-2), or closing-snapshot ownership (GAP-3). | `BLOCKING` | `23` §5.2 | `JT-06`, `JT-07` |
| `CGS-U41` | Whether the Boss-approved 16-field Minimum Handoff Data Contract already includes an as-of-date "unmatched fact" query capability is `UNKNOWN` — the contract's content was not re-opened in this session. | `MATERIAL` | `23` §5.2 GAP-1, §9 | Verify against the contract directly |
| `CGS-U42` | Whether Product Category (the policy-carrying record for Costing Method and Stock accounts) is company-scoped by default could not be confirmed against official documentation — only secondary/non-official sources address it, and the confirmed analogous case (product Cost, company-specific even on a shared product) shows the reference ERP is capable of this narrow carve-out without proving it exists here. | `BLOCKING` | `25` §2.4, §5 | `RISK-U03`/`GAP-FS-10` (re-scoped, not new) |
| `CGS-U43` | If Category is not company-isolated, a shared category could silently force the same costing method onto both companies' legs of an inter-company transfer, even while the transfer itself is correctly modeled as two independent financial events. | `BLOCKING` | `25` §6 | `RISK-U03`/`GAP-FS-10`, `JT-10` |
| `CGS-U44` | Whether Journals are company-scoped is `HOLD`, inferred only by analogy to the confirmed Chart-of-Accounts pattern, not directly evidenced. | `WATCH` | `25` §7 | informational |

---

## 8. Migration / Idempotency / Reconciliation Identities

| ID | Item | Severity | Source Files | Routed To |
|---|---|---|---|---|
| `CGS-U45` | Accounting-side duplicate-posting risk is not automatically solved by Inventory-side movement-fact idempotency — a cardinality mismatch exists (Periodic posts one aggregate closing entry covering many facts). `GAP-FS-08` (migration provenance reference) does not yet exist and is the single blocking prerequisite for the `AC-01`–`AC-05` candidate requirements. | `BLOCKING` | `26` §5, §9 | `GAP-FS-08`, Joint Accounting × Inventory design session |
| `CGS-U46` | Whether the reference ERP's initial-stock quantity action also carries a value/cost input, and what account any resulting entry uses, is `HOLD` — the retrieved documentation is quantity-only. | `MATERIAL` | `26` §2.2 | Further Layer A research |
| `CGS-U47` | Whether the reference ERP has any *structural* (system-enforced) duplicate-import block for the opening-inventory-value posting, beyond documented sequencing discipline, is `HOLD`. | `MATERIAL` | `26` §2.3, §9 | Further Layer A research |
| `CGS-U48` | The naive Periodic COGS candidate identity (`Opening + Purchases − Closing = COGS`) silently absorbs scrap/shrinkage/write-down into COGS unless those are separately provenanced and subtracted first — the identity's corrected form is `CANDIDATE` only, not `VERIFIED`, and depends on SMEsPlus actually capturing non-COGS releases at the required granularity. | `BLOCKING` | `27` §5.2 | `JT-01`, `20` |
| `CGS-U49` | The Cross-System Reconciliation identity holds only at the close boundary, by the reference system's own documented design (a closing entry exists precisely because the two sides are expected to diverge between closings) — not continuously, under either accounting model. | `MATERIAL` (informational — a scope condition, not a gap) | `27` §6.4 | `JT-03`, `JT-07` |
| `CGS-U50` | Classification rule set deciding COGS vs. another approved financial classification for any given released cost is `HOLD` — the Cost Release identity is verified only as a governing constraint, never as evidence any specific classification scheme satisfies it. | `BLOCKING` | `27` §4.2, `H-27-01` | `12`, `20` |

---

## 9. Thai Statutory Track

| ID | Item | Severity | Source Files | Routed To |
|---|---|---|---|---|
| `TH-HOLD-COGS-01` | No quantitative or qualitative threshold located for where "normal" waste (absorbed silently into cost) ends and "abnormal" waste (requires witnessed destruction procedure) begins under Revenue Department Order Por.79/2541. | `MATERIAL` | `24` §4 | Accounting-Tax track |
| `TH-HOLD-COGS-02` | Whether a category-level (or account-group-level) write-down posting structure can coexist with TAS 2's item-level NRV testing obligation is unresearched. | `MATERIAL` | `24` §4 | Accounting-Tax track, `11` |
| `TH-HOLD-COGS-03` | Whether Thailand's Section 65 bis (6) costing-method consistency/change-approval rule applies only at the whole-entity level or could bind at product-category granularity — every primary source located frames it at the taxpayer-entity level only; no evidence located either confirming or excluding category-level granularity. | `BLOCKING` for `11`/`JT-02` | `24` §4 | Accounting-Tax track, `11`, `JT-02` |
| `TH-HOLD-COGS-04` | The DBD income-statement presentation-sequence finding (revenue-and-cost-of-sales together, then gross profit, then other income, then operating expenses) is `INTERPRETATION — REVIEW REQUIRED` only, reconstructed from search synthesis, not directly-extracted primary text — and explicitly does **not** close the pre-existing, unrelated Account-module blocker `N-04` (Source Class F remains `EVIDENCE_MISSING`). | `MATERIAL` | `24` §2.10, §4 | Account-module track (`N-04`), not this session's to close |
| `TH-HOLD-05-residual` | The gazetted TAS 2 standard text itself (as opposed to TFAC's own explanatory manual) could not be extracted in the time available this session; the manual is treated as `AUTHORITATIVE` on TFAC's own standard-setter authority, but a reviewer needing the exact numbered gazetted paragraph should re-attempt extraction. | `WATCH` | `24` §2.4 caveat | Future evidence pass |
| `TH-HOLD-01`, `04`, `06`, `08`, `09` | Carried forward unchanged from the Inventory Final Solution v1.0 package — not in this session's advance list, not researched in this pass. | `MATERIAL` (carried, not new) | `24` §1 | Accounting-Tax track (unchanged) |

---

## 10. Register Roll-Up

| Category | Count |
|---|---:|
| Version / terminology instability | 5 |
| Menu A–D field-level items | 8 |
| Menu E–H items | 11 |
| Periodic/Perpetual/Costing model items | 7 |
| Returns/Adjustment/Scrap/Landed Cost/Manufacturing | 8 |
| Period close / multi-company | 5 |
| Migration / idempotency / reconciliation identities | 6 |
| Thai statutory track (new `TH-HOLD-COGS-*` plus residual/carried) | 9 |
| **Total distinct items registered** | **59** |

| Severity | Count |
|---|---:|
| `BLOCKING` | 15 |
| `MATERIAL` | 36 |
| `CONFLICTING` (subset of the above, called out explicitly) | 3 (`CGS-U03`, `CGS-U12` discarded-not-conflicting, `CGS-U34`) |
| `WATCH` | 6 |
| **Closed by this session** | **0** |

---

## 11. The Single Most Material Cross-Cutting Finding

Repeated across §2 (`CGS-U01`), §5 (`CGS-U25`, `CGS-U30`), §6 (`CGS-U32`, `CGS-U36`), and the Special Team convergence note (file `29`): **the reference ERP does not supply one stable, adoptable answer to COGS recognition timing, return cost basis, or landed-cost-after-sale posting — across its own version history, it changed its mind on all three.** This is not a research shortfall; it is the research's strongest finding. `JT-03` and `JT-04` in particular cannot be resolved by "match what the reference does" and must be decided on SMEsPlus's own evidence and judgment.

---

## 12. What Would Change This Register

Only a written Boss ruling, a Joint Accounting ↔ Inventory session that closes its own rows, an Accounting-Tax track response carrying authoritative Thai evidence, a completed direct-fetch re-verification pass on the `19.0` `PROVISIONAL` items, or a live reference-instance walkthrough for the items this documentation-only session could not resolve (`CGS-U07`, `CGS-U32` FIFO sub-case, `CGS-U30`). This session performs none of those and closes nothing.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
