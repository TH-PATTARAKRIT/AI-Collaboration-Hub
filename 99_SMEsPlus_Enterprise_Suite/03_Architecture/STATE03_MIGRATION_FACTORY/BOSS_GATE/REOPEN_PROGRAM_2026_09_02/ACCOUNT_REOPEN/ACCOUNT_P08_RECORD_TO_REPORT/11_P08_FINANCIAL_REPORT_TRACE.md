# P08_FINANCIAL_REPORT_TRACE

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1

## 1. The metamodel

A statement is a named definition owning ordered rows and ordered columns. Each row owns labelled value definitions; a cell is the value definition whose label matches the column's. Rows may nest and may declare a grouping key that generates sub-rows at read time.

`FR-01` — **Six derivation strategies exist**, and only three of them can be expressed as a filter over journal items. `FACT VERIFIED`. Denominator declared: 6 strategies, 5 with a batch implementation plus one evaluated separately; 5 of 6 are in the auditable set; **3 of 6** can be translated into a journal-item filter.

`FR-02` — Across the shipped statement pack, **90 of 158** value definitions (57%) use the one strategy that is excluded from the auditable set outright. `FACT VERIFIED`; denominator = every value-definition declaration in the pack's data files, by declared pattern.

## 2. The eight statutory outputs

| Statement | How the figure is produced |
|---|---|
| Trial balance | no rows and no value definitions of its own; **delegates wholesale to the general-ledger engine** and reshapes the columns. Its Initial/Period/End split is a date-scope switch plus one column group that runs no query at all and is a Python sum of the others |
| General ledger | bespoke engine, two queries — totals and detail — joining items to entries |
| Balance sheet | fully declarative: item-filter and arithmetic strategies only. Its handler exists **solely to raise a warning** |
| Profit & loss | fully declarative, no handler |
| Cash flow | bespoke engine, no rows of its own, layout hard-coded |
| Partner ledger | bespoke engine |
| Journal report / audit trail | one row with four bespoke value definitions |
| Aged receivable / payable | bespoke engine; buckets from maturity or document date with a fallback to the accounting date, re-based on the report date, settlement cut at the report date |

`FR-03` — **The balance sheet's equity is derived at report time from the income statement**, cross-referencing its net-result row over the fiscal year. There is no posted closing entry behind it. `FACT VERIFIED`. This is the report-layer view of `PC-21`/`PC-23`.

## 3. Auditability — where the derivation chain breaks

`FR-04` — **Two structurally different drill mechanisms exist and only one reconstructs the reported population.** The cell-audit path rebuilds the report's own filter set and is faithful. The caret/line path builds an action carrying **only** a presentation-type exclusion plus search defaults — it does **not** carry the forced-company set, the tax-determination filter, the unsettled filter, the saved item filters, or the forced domain. Whenever any of those is active, the drilled population is a different set from the computed figure. `FACT VERIFIED`.

`FR-05` — **When no auditable filter can be built, the code falls back to the whole report population for the period.** The resulting list is a superset of the cell's constituents and does not foot to the displayed number. `FACT VERIFIED`.

`FR-06` — The debit-only/credit-only selector on the account-code strategy is **deliberately dropped** from the audit filter, by documented design, because it cannot be expressed as a filter. Every such cell's drill-down is a superset by construction. `FACT VERIFIED`.

`FR-07` — **The "auditable" marker is data-overridable and is set on strategies that are not re-expressible.** It is forced on 81 times across the shipped pack, including 14 times on the bespoke strategy in the ageing statement alone. A cell so marked offers a drill-down that lands in the fallback of `FR-05`. `FACT VERIFIED`.

`FR-08` — **The ageing cell audit is a hand-written re-derivation that does not match the figure**, in four independent ways: it hard-codes the bucket width, ignoring the configured interval; it hard-codes the maturity date, ignoring the configured basis; it omits the accounting-date fallback, so items the figure buckets are excluded; and it overwrites the action's own filter set, so fully settled items the figure dropped reappear. `FACT VERIFIED`.

`FR-09` — **No cash-flow figure is drillable to journal items at all.** Every line is built without a journal-item model reference and without a value-definition reference, so the audit affordance evaluates false; the only caret opens an account's **unfiltered** general ledger rather than the settlement-weighted amount displayed. `FACT VERIFIED`.

`FR-10` — **The trial balance has no in-report expansion**; its only drill-out is the unfaithful caret path of `FR-04`. `FACT VERIFIED`.

**Seven line types cannot be traced to their constituent journal items** — external-value lines, bespoke lines with no audit affordance, bespoke lines marked auditable but with no bespoke audit routine, account-code cells carrying a side selector, arithmetic cells carrying a bounding subformula, every cash-flow line, and every trial-balance cell.

**Conclusion.** The report layer is **not** fully derived and not fully traceable. `FACT VERIFIED`, scope = the eight statutory outputs and the six-strategy set.

## 4. Independent truth held by the report layer

`FR-11` — **Three stored, journal-item-independent value sources exist**: externally supplied values; values entered by hand directly on a statement cell (stored as a dated delta); and values carried forward and materialised at period close. A fourth, non-monetary store holds free-text annotations, and a fifth holds budget figures. `FACT VERIFIED`.

`FR-12` — Editing a statement cell of this class **creates or amends a stored record and creates no journal entry**. The lock dates and the entry seal do not constrain it. `FACT VERIFIED`.

`FR-13` — **Write access to both the statement definitions and the stored values is a single ordinary accounting role with full create, update and delete, and none of the five models carries a change history.** `A VERIFIED ABSENCE` for the change history, scope = the two report model files read in full for inheritance declarations.

`FR-14` — Under the corrected scope model this is not primarily an isolation gap to be fixed by adding a company field. A **statutory statement layout is platform reference data that tenants must not be able to edit at all**; a **management layout is tenant-owned**; a **produced statement is company-owned**. The benchmark has one object for all three. `P08-RQ-RP-01`.

## 5. Cash flow

`FR-15` — The cash-flow statement is **not derived by classifying journal items**. It is a settlement walk outward from the liquidity accounts, whose section assignment comes from an **optional, hidden-by-default tag on the counterparty account**, pre-empted by that account's classification for receivable and payable. Consequences visible in the code: a tag on a receivable or payable account is unreachable; exactly-zero balances are dropped; an account carrying two tags is split across sections. `FACT VERIFIED`.
`FR-16` — **The statement carries a self-declared residual line** equal to closing liquidity minus opening liquidity minus attributed movement — that is, it quantifies the amount the classification failed to attribute. `FACT VERIFIED`.
`FR-17` — Parts of the cash-flow query **bypass the report's own filter builder**, constructing a bare query and pulling counterpart legs through settlement joins with no posted-state clause of their own. `FACT VERIFIED`.

## 6. Period, draft inclusion, consolidation

`FR-18` — Period membership is decided by the item's **accounting date**, never by its document date. Six date scopes re-cut the window per value definition. `FACT VERIFIED`.
`FR-19` — Draft inclusion is a two-state per-run toggle whose default is posted-only. **Six of the nine statutory report records can be run including draft entries**; only the two ageing reports forbid it. Three disclosures exist — an on-screen warning whenever draft entries merely exist in the period, an ungated marker in the exported document title, and a row in the exported options sheet — and one further label is group-gated. `FACT VERIFIED`.
`FR-20` — Consolidation is a **plain aggregation over a company set**. There is no consolidation ledger, no elimination step and no consolidation entity; `A VERIFIED ABSENCE` for any consolidation module, scope = both module trees of the target root under four independent patterns. Report-time translation runs through a **temporary structure discarded at commit** — no translated figure is ever persisted. A missing rate degrades silently, and **the two translation modes fail differently**: one passes the amount through at parity, the other **drops the item from the statement entirely**. `FACT VERIFIED`.
`FR-21` — The only acknowledgement that consolidation can break the accounting identity is a screen warning, not a check figure. `FACT VERIFIED`.

## 7. Immutability of an issued statement

`FR-22` — **There is no report-run entity, no issued-statement snapshot, no options hash, no version and no re-run comparison.** The only artefacts of a run are ordinary attachments carrying the run parameters as free text and no reference to the data state, deletable by the same role that ran the report. `A VERIFIED ABSENCE`, scope = the report module's 34 model files and the base report model file.

`FR-23` — **Re-running an identical request for an identical past period can legitimately return a different number, through at least eleven distinct routes.** The two most consequential are: **retroactive reclassification of an account's code or classification**, both permitted on accounts already carrying posted entries with no guard; and **retroactive edit of a statement's own formulas**, permitted to one ordinary role with no change history. `FACT VERIFIED`.

`FR-24` — Countermeasures exist, and **all of them sit at the journal-entry layer. None sits at the report layer.** The lock dates and the entry seal constrain the ledger; they constrain nothing in the statement layer. The seal freezes a sealed entry's date, but not the account it points at, nor that account's code or classification, nor any statement definition. `FACT VERIFIED`.

## 7A. A statutory extract whose population is not scoped to the entity it names

`FR-25` — In the jurisdiction-specific reporting module of the target root, the value-added-tax extract builds its document population from a filter containing **journal type, settlement state and date only — no owning-entity term** — and then stamps the **currently active entity's** name, tax registration number and branch name onto the output header.

The object layer's own isolation rule still filters the population, but it filters by the set of entities **activated in the session**, not by the single entity whose identity is printed. Where an operator has more than one entity active, the extract therefore presents one entity's identity over a document set that may span several.

`FACT VERIFIED` for the mechanism — read directly and independently confirmed by this session's lead author. The sibling withholding-tax handler in the same module scopes correctly, which is what makes this a defect rather than a design.

**What is not stated here.** Whether such an extract satisfies or breaches any Thai statutory filing requirement is `HOLD / EVIDENCE REQUIRED` and is routed to the Accounting-Tax track. P08 records the mechanism only, and routes the content to P07 as `XP-06`.

**Why it belongs in P08 and not only in P07.** It is an instance of the general class this file establishes: **the statement layer carries no owning-entity scope of its own**, so every statement's scope is whatever its caller happened to activate. The tax extract is the instance where that produces a document bearing a legal identity.

## 8. Requirements

| ID | Candidate requirement |
|---|---|
| `P08-RQ-FR-01` | Every reported figure is traceable to the exact set of facts that compose it. A cell that cannot be traced is not a cell; it is an assertion, and must be labelled as one on the face of the statement. |
| `P08-RQ-FR-02` | The audit path is the computation path. A drill-down is produced by the same filter that produced the number, never by a re-derivation. |
| `P08-RQ-FR-03` | Issuing a statement is a fact: it records the definition version, the period, the company, the data state, the actor and the time. Re-running is a new fact, not an overwrite. |
| `P08-RQ-FR-04` | A statement value not derived from facts is a distinct, governed, auditable object with its own authorisation — never an edit made on a cell. |
| `P08-RQ-FR-05` | Statutory layouts are platform reference data, immutable to tenants. Management layouts are tenant-owned. A produced statement is company-owned. |
| `P08-RQ-FR-06` | Draft entries are never included in an issued statement, and the inclusion state is on the face of every rendering, ungated. |
| `P08-RQ-FR-07` | A consolidated view is a derivation and is never writable. A missing translation measurement refuses; it never passes through at parity and never silently drops the fact. |
| `P08-RQ-FR-08` | The cash-flow classification is a property of the accounting event, not an optional tag on the counterparty account, and the statement carries no unexplained residual. |
| `P08-RQ-FR-09` | A statement that bears a legal entity's identity is produced for **exactly that entity**, and its population is scoped by that entity — never by whatever the caller happened to activate. |
