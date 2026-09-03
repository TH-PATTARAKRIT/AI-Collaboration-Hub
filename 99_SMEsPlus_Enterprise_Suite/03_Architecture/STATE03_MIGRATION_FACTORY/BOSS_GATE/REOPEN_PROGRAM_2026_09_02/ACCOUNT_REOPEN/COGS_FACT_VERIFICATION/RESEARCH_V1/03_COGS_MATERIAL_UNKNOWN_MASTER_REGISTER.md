# 03 — COGS Material Unknown Master Register (Verified Reconstruction)

Source of record: `30_COGS_MATERIAL_UNKNOWN_CONFLICT_REGISTER.md` (Session `SMEPLUS-26-09-02-COGS-DR-001`, branch `audit/cogs-deep-research-2026-09-02-001`). Every ID, severity, and source-file citation below is copied verbatim from that register; this session adds Reason-Unknown-Exists, Evidence Ceiling, and Status columns, and reconfirms nothing is closed.

Status legend: `OPEN — EVIDENCE REQUIRED` (documentation-only research cannot close it further), `OPEN — LIVE INSTANCE REQUIRED` (explicitly needs a live reference-ERP walkthrough), `OPEN — BOSS/BUSINESS RULING REQUIRED` (a design/policy choice, not a fact), `OPEN — THAI STATUTORY TRACK` (needs external accounting authority).

## Section A — Version / Terminology Instability (5)

| ID | Item (verbatim, condensed) | Severity | Reason Unknown Exists | Status |
|---|---|---|---|---|
| `CGS-U01` | Reference ERP's "Perpetual" pattern is not one stable mechanism across versions (pre-19 real-time; 19.0+ invoice/bill-level). | BLOCKING | The benchmark system itself changed behavior across major versions; no single "correct" pattern to adopt by imitation. | OPEN — BOSS/BUSINESS RULING REQUIRED (SMEsPlus must decide its own timing, not copy a moving target) |
| `CGS-U02` | "Manual/Automated" (pre-19) may not be a simple rename of "Periodic/Perpetual" (19.0) — ownership model flips (category-native vs. company-default). | MATERIAL | Terminology and ownership model changed simultaneously across versions; not disambiguated in any single source. | OPEN — EVIDENCE REQUIRED |
| `CGS-U03` | Price Difference Account scope conflicts across sources (Standard-only vs. also FIFO/AVCO "cost adjustments"; a distinct "Variation Account" possibly unrelated). | MATERIAL / CONFLICTING | Multiple documentation sources describe the same account differently. | OPEN — EVIDENCE REQUIRED (contradiction, see file `19`) |
| `CGS-U04` | The entire 19.0 Finance/Accounting Menu A field set rests on search-index reconstruction; two direct-fetch attempts failed. | BLOCKING (for any 19.0-pinned design) | Primary source page could not be retrieved; secondary reconstruction is not the same evidence tier. | OPEN — EVIDENCE REQUIRED (re-fetch pass) |
| `CGS-U05` | Whether pre-19 category-level Automated/Manual labels persist on the 19.0 category form, or collapsed into company-level only. | MATERIAL | Not directly observed on a 19.0 instance. | OPEN — LIVE INSTANCE REQUIRED |

## Section B — Menu A–D Field-Level Items (8)

| ID | Item | Severity | Reason Unknown Exists | Status |
|---|---|---|---|---|
| `CGS-U06` | "Expense Account" field may hold structurally different account types (Current-Asset vs. Expense/Cost-of-Revenue) under the same label depending on Periodic/Perpetual mode. | BLOCKING control risk | Same UI label overloaded with different accounting meaning by mode; not resolvable from docs alone. | OPEN — BOSS/BUSINESS RULING REQUIRED (SMEsPlus must design explicit mitigation) |
| `CGS-U07` | No evidence on whether existing accumulated Stock Valuation Account balance is auto-reclassed when a product's category changes. | BLOCKING | Explicitly stated in source as unresolvable without a live-instance test. | OPEN — LIVE INSTANCE REQUIRED |
| `CGS-U08` | No confirmed mechanical answer for effect of changing category/policy/account on existing stock and posted transactions. | MATERIAL | Same as above — behavior not documented anywhere reviewed. | OPEN — BOSS/BUSINESS RULING REQUIRED |
| `CGS-U09` | Whether a Journal-level fallback account exists below Category when Product/Category accounts are blank. | MATERIAL | Community-repeated claim, not officially confirmed; plausible alternative (hard block) exists. | OPEN — EVIDENCE REQUIRED |
| `CGS-U10` | Whether "Show Accounting Features" visibility gate existed identically pre-19.0. | WATCH | Confirmed only for one version. | OPEN — EVIDENCE REQUIRED (informational) |
| `CGS-U11` | Whether Fiscal Position tax/account mapping can override an explicit product-level account, or only substitutes at fallback levels. | MATERIAL | Not directly documented. | OPEN — EVIDENCE REQUIRED |
| `CGS-U12` | Full field-by-field 19.0 account model mapping incomplete (one 19.0 claim discarded as fetch-summarization artifact). | MATERIAL | Same 19.0 fetch-failure root cause as `CGS-U04`. | OPEN — EVIDENCE REQUIRED (re-fetch pass) |
| `CGS-U13` | Whether Continental/Anglo-Saxon accounting-package setting is strictly company-level-exclusive with no category override. | MATERIAL | Not independently re-verified. | OPEN — EVIDENCE REQUIRED |

## Section C — Menu E–H Items (11)

| ID | Item | Severity | Reason Unknown Exists | Status |
|---|---|---|---|---|
| `CGS-U14` | No dedicated "Close the Stock Period" wizard exists; closing is cadence config plus server-action or manual journal entry. | MATERIAL (informational — genuine negative finding) | Confirmed absence, not a gap. | RESOLVED AS NEGATIVE FINDING — informs `JT-07`, not itself open |
| `CGS-U15` | Whether documented closing mechanisms describe routine closing, one-time Periodic→Perpetual migration, or both. | BLOCKING for `JT-07` scoping | Ambiguous heading groups both concepts together in source. | OPEN — EVIDENCE REQUIRED |
| `CGS-U16` | No mechanism to attribute a late-arriving supplier cost back to the specific prior-period COGS it should have affected. | BLOCKING | Documented behavior (absorption into current-period Variation account) is a genuine negative finding, but SMEsPlus's own treatment is undecided. | OPEN — BOSS/BUSINESS RULING REQUIRED |
| `CGS-U17` | Whether Lock Date mechanism correctly interacts with a scheduled Periodic closing entry attempting to post into an already-locked period. | MATERIAL | Not documented. | OPEN — EVIDENCE REQUIRED |
| `CGS-U18` | Negative/zero-cost exception handling confirmed only for AVCO/Perpetual/19.0; FIFO and Standard-Price unconfirmed. | MATERIAL | Partial evidence only. | OPEN — EVIDENCE REQUIRED |
| `CGS-U19` | Whether valuation-report drill-down reaches the source bill/invoice line or only the stock move. | WATCH | Not documented. | OPEN — EVIDENCE REQUIRED (informational) |
| `CGS-U20` | Invoicing-policy (ordered vs. delivered) interaction with Periodic/Perpetual value-trigger table undocumented. | MATERIAL | Two independently documented axes never cross-referenced in any source. | OPEN — EVIDENCE REQUIRED |
| `CGS-U21` | Whether any version enforces a hard block on bill-before-receipt / invoice-before-delivery at the accounting layer. | MATERIAL | Not documented; may be left to a separate procurement control. | OPEN — EVIDENCE REQUIRED |
| `CGS-U22` | "Loss is not COGS" separation is configuration-dependent; no documented fallback account for an unconfigured loss. | BLOCKING control risk | Confirmed as configuration-dependent, but no evidence of a safe default. | OPEN — BOSS/BUSINESS RULING REQUIRED (SMEsPlus must design an explicit safe default) |
| `CGS-U23` | Whether location-level accounting overrides generalize beyond the Inventory Loss location case. | MATERIAL | Only one case independently confirmed. | OPEN — EVIDENCE REQUIRED |
| `CGS-U24` | Whether a third, location-keyed precedence axis is needed alongside Category and Product. | MATERIAL | Flagged, not decided. | OPEN — BOSS/BUSINESS RULING REQUIRED |

## Section D — Periodic/Perpetual/Costing Model Items (7)

| ID | Item | Severity | Reason Unknown Exists | Status |
|---|---|---|---|---|
| `CGS-U25` | Whether Periodic has any dedicated "received-not-billed" / "billed-not-received" accrual visibility mechanism, or only discovers the gap at close. | BLOCKING | Single most material item for `JT-06`; not documented. | OPEN — EVIDENCE REQUIRED |
| `CGS-U26` | Return handling before/after closing under Periodic specifically. | MATERIAL | Evidence exists mainly for Perpetual/Anglo-Saxon, not Periodic. | OPEN — EVIDENCE REQUIRED |
| `CGS-U27` | Whether write-down/loss/scrap/adjustment is distinguished from ordinary COGS under Periodic, vs. collapsed into one Variation Account. | MATERIAL | Not documented for Periodic specifically. | OPEN — EVIDENCE REQUIRED |
| `CGS-U28` | Exact literal formula wording for "COGS as period residual" not found verbatim anywhere. | WATCH | Pattern is corroborated, not directly quoted. | OPEN — EVIDENCE REQUIRED (informational) |
| `CGS-U29` | Existing-stock conversion mechanics on a costing-method change confirmed only away from Standard Cost; AVCO/FIFO-specific behavior unconfirmed. | MATERIAL | Partial evidence only. | OPEN — EVIDENCE REQUIRED |
| `CGS-U30` | Bill-before-receipt under Perpetual is the weakest-evidenced purchase-side timing sub-case; inferred only by structural symmetry. | MATERIAL | Never independently confirmed. | OPEN — LIVE INSTANCE / RE-FETCH REQUIRED |
| `CGS-U31` | Whether invoice-before-delivery is permitted, gated, or warned against under Perpetual. | MATERIAL | Not documented; strict reading of 19.0+ rule raises a matching-principle risk. | OPEN — EVIDENCE REQUIRED |

## Section E — Returns / Adjustment / Scrap / Landed Cost / Manufacturing (8)

| ID | Item | Severity | Reason Unknown Exists | Status |
|---|---|---|---|---|
| `CGS-U32` | **JT-05/C-03.** AVCO returns valued at current (not original) average cost, average never recalculated; FIFO layer-consumption on return only community-corroborated; documented unreconciled discrepancy between credit-note financial reversal and inventory-valuation reversal ("manual adjustment" is the reference system's own stated fix); three independently-settable dates on a later-period return with no forced alignment. | BLOCKING | Genuinely undecidable from reference-ERP documentation alone (source's own conclusion). See file `15` (JT-05 Fact Package). | OPEN — BOSS/BUSINESS RULING REQUIRED, PARTIALLY LIVE-INSTANCE DEPENDENT |
| `CGS-U33` | Reference ERP's own "Returns and refunds" feature documentation is silent on cost basis; answer must be assembled from a non-cross-referenced source. | MATERIAL (informational) | Genuine documentation gap in the benchmark system itself. | OPEN — EVIDENCE REQUIRED |
| `CGS-U34` | Landed-cost residual posting on fully-sold stock is CONFLICTING — one source: auto-books to COGS; another (19.0+): requires manual entry via Landed Cost Clearing account. | BLOCKING for `JT-08` | Two sources directly disagree. | OPEN — EVIDENCE REQUIRED (contradiction, see file `19`) |
| `CGS-U35` | Whether Standard-Price products can receive landed cost at all. | MATERIAL | Feature eligibility documented as gated to AVCO/FIFO; no worked example for Standard-Price. | OPEN — EVIDENCE REQUIRED |
| `CGS-U36` | **Scenario 11 (landed cost after full sale)** — version-inconsistent destination account, at least one reported case with no journal entry generated at all. | BLOCKING | Documented control break in the benchmark system across versions. | OPEN — BOSS/BUSINESS RULING REQUIRED; flagged as an Audit VETO concern |
| `CGS-U37` | No documented production/manufacturing standard-cost variance posting mechanism exists. | MATERIAL | Sharp asymmetry against the well-evidenced purchase-side pattern; no reference precedent. | OPEN — ORIGINAL DESIGN WORK REQUIRED (not a fact gap — no fact to find) |
| `CGS-U38` | Whether two documented WIP mechanisms coexist or are mutually exclusive on the same manufacturing order. | MATERIAL | Not found in any page retrieved. | OPEN — EVIDENCE REQUIRED |
| `CGS-U39` | NRV/write-down/impairment not present as a named reference-ERP feature across any version searched, but is AUTHORITATIVE under Thai TAS 2. | BLOCKING | No reference-UI pattern exists to study; this is original design territory. | OPEN — ORIGINAL DESIGN WORK REQUIRED, Thai evidence is the only source |

## Section F — Period Close / Cut-Off / Multi-Company (5)

| ID | Item | Severity | Reason Unknown Exists | Status |
|---|---|---|---|---|
| `CGS-U40` | Inventory-side movement-date period guard is necessary but not sufficient for an Accounting close (does not supply unmatched-fact query surface, late-cost period authority, or closing-snapshot ownership). | BLOCKING | Structural gap identified by comparing two independently-built control layers. | OPEN — BOSS/BUSINESS RULING REQUIRED |
| `CGS-U41` | Whether the Boss-approved 16-field Minimum Handoff Data Contract already includes an as-of-date "unmatched fact" query capability. | MATERIAL | Contract's content was not re-opened in the DR session. | OPEN — EVIDENCE REQUIRED (verify against the contract directly — this is answerable without new research, just a contract re-read) |
| `CGS-U42` | Whether Product Category (the policy-carrying record) is company-scoped by default could not be confirmed against official documentation. | BLOCKING | Only secondary/non-official sources address it. | OPEN — LIVE INSTANCE / OFFICIAL-SOURCE REQUIRED |
| `CGS-U43` | If Category is not company-isolated, a shared category could silently force the same costing method onto both companies' legs of an inter-company transfer. | BLOCKING | Direct consequence of `CGS-U42` being unresolved. | OPEN — dependent on `CGS-U42` |
| `CGS-U44` | Whether Journals are company-scoped. | WATCH | Inferred only by analogy to Chart-of-Accounts pattern. | OPEN — EVIDENCE REQUIRED (informational) |

## Section G — Migration / Idempotency / Reconciliation Identities (6)

| ID | Item | Severity | Reason Unknown Exists | Status |
|---|---|---|---|---|
| `CGS-U45` | Accounting-side duplicate-posting risk not automatically solved by Inventory-side movement-fact idempotency (cardinality mismatch); `GAP-FS-08` does not yet exist. | BLOCKING | Structural mismatch between two independently-designed idempotency layers, plus a missing prerequisite artifact. | OPEN — BOSS/BUSINESS RULING REQUIRED (design work, `GAP-FS-08` must be created first) |
| `CGS-U46` | Whether the reference ERP's initial-stock quantity action also carries a value/cost input, and what account any resulting entry uses. | MATERIAL | Retrieved documentation is quantity-only. | OPEN — EVIDENCE REQUIRED |
| `CGS-U47` | Whether the reference ERP has any structural (system-enforced) duplicate-import block for opening-inventory-value posting. | MATERIAL | Beyond documented sequencing discipline, not confirmed. | OPEN — EVIDENCE REQUIRED |
| `CGS-U48` | Naive Periodic COGS identity (`Opening + Purchases − Closing = COGS`) silently absorbs scrap/shrinkage/write-down unless separately provenanced. | BLOCKING | Identity is CANDIDATE only, depends on SMEsPlus's own future capture granularity. | OPEN — BOSS/BUSINESS RULING REQUIRED |
| `CGS-U49` | Cross-System Reconciliation identity holds only at the close boundary, by the reference system's own design. | MATERIAL (informational — a scope condition) | Documented design intent, not a gap. | RESOLVED AS SCOPE CONDITION — informs `JT-03`/`JT-07` |
| `CGS-U50` | Classification rule set deciding COGS vs. another approved financial classification for a released cost is HOLD. | BLOCKING | Cost Release identity verified only as a governing constraint, never as evidence any specific classification scheme satisfies it. | OPEN — BOSS/BUSINESS RULING REQUIRED |

## Section H — Thailand Statutory Track (9, per source roll-up)

| ID | Item | Severity | Reason Unknown Exists | Status |
|---|---|---|---|---|
| `TH-HOLD-COGS-01` | No quantitative/qualitative threshold for "normal" vs. "abnormal" waste under Revenue Department Order Por.79/2541. | MATERIAL | No primary source states a numeric threshold. | OPEN — THAI STATUTORY TRACK |
| `TH-HOLD-COGS-02` | Whether category-level write-down posting can coexist with TAS 2's item-level NRV testing obligation. | MATERIAL | Not researched; requires accounting-tax track input. | OPEN — THAI STATUTORY TRACK |
| `TH-HOLD-COGS-03` | Whether Section 65 bis (6) costing-method consistency rule binds at entity level only, or could bind at category granularity. | BLOCKING for `JT-02` | Every primary source frames it at entity level only; none confirms or excludes category-level granularity. | OPEN — THAI STATUTORY TRACK |
| `TH-HOLD-COGS-04` | DBD income-statement presentation-sequence finding is interpretation-only, reconstructed from search synthesis. | MATERIAL | Not directly-extracted primary text. | OPEN — THAI STATUTORY TRACK (does not close unrelated Account-module blocker `N-04`) |
| `TH-HOLD-05-residual` | Gazetted TAS 2 standard text itself (vs. TFAC's explanatory manual) could not be extracted this pass. | WATCH | Time-boxed research pass did not reach the gazetted text. | OPEN — THAI STATUTORY TRACK |
| `TH-HOLD-01, 04, 06, 08, 09` (carried) | Carried forward unchanged from Inventory Final Solution v1.0 — not advanced this pass. | MATERIAL (carried) | Out of this pass's advance list. | OPEN — THAI STATUTORY TRACK (unchanged) |

---

## Population Reconciliation

| Metric | Count |
|---|---:|
| Total distinct register items (source-authored total) | **59** |
| Closed | **0** |
| Resolved as negative finding / scope condition (informative, not a fact gap — `CGS-U14`, `CGS-U49`) | 2 |
| Requiring Boss/business ruling (a decision, not a missing fact) | 13 |
| Requiring live reference-instance verification | 5 |
| Requiring original design work (no reference precedent exists) | 3 |
| Requiring Thai statutory track input | 9 |
| Remaining — documentation re-verification / evidence-gathering only | 27 |

This session did not close any item, because closing requires exactly what this register shows is missing: a live instance, a Boss ruling, original design work, or Thai statutory research — none of which is "more reading of the same documents already reviewed." This matches the parent session's verified 0/59 and is not a regression.
