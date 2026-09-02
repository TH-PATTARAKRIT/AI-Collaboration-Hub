# 08 — Menu F: Accounting Inventory Valuation / Stock Closing / Closing Entry Flow Deep Research

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE IN PROGRESS — CP-03 (Menu F) — Layer A populated with an explicit negative finding on wizard existence; Layer B pointer only; Layer C candidate-only`

---

## 1. Scope and the honest negative finding required by the governing prompt

Governing-prompt §6 Menu F requires this file to state explicitly whether a formal "stock closing" wizard/menu is or is not a distinct reference-ERP concept. Layer A evidence gathered this session supports the following finding:

**There is no dedicated single "Close the Stock Period" wizard/button documented anywhere in the reference-ERP official documentation fetched this session (versions 13.0–19.0).** What exists instead is:

1. A **configuration setting** (`Accounting -> Configuration -> Settings -> Inventory Valuation`) that selects Periodic vs Perpetual valuation and, for Periodic, a **cadence** (Manual / Daily / Monthly) for when a closing-type journal entry is produced.
2. For the **Manual** cadence specifically, the documentation describes the closing entry as something the accountant builds themselves, using the Inventory Valuation report (file `07`) as the evidentiary basis, via one of two documented options: a **server action that generates the journal entry** (an administrator-configured automated action, not a menu button visible to an ordinary accounting user by default), or a **fully manual journal entry** typed by the accountant.
3. For the **Daily/Monthly** cadence, the documentation describes a scheduled/automatic generation of the same kind of entry, without describing a separate approval or review step beyond ordinary journal-entry posting controls.

This matches the governing prompt's flagged possibility directly: under the Periodic model, "closing" is **a manual accountant workflow driven by the accountant's own reading of the physical/valuation evidence, optionally scheduled**, not a discrete closing wizard comparable to, for example, a formal period-lock ceremony. This finding is reported honestly per governing-prompt instruction, not assumed in either direction before evidence was gathered.

Feeds open Joint decisions: `JT-03` (continuous vs periodic timing), `JT-06` (late supplier bill after close), `JT-07` (period close design — this file is a primary evidence source for that decision), `JT-12` (period lock policy).

---

## 2. Layer A — Reference ERP Observed Behavior

### 2.1 Close initiation

| Aspect | Evidence |
|---|---|
| Is there a single "close" action? | Not found. Closing is the emergent result of (a) the Periodic Valuation cadence setting plus (b) either a scheduled action or a manually authored journal entry. `Fact Status: VERIFIED (absence, within evidence gathered)` |
| Who initiates it under Manual cadence? | The accounting user, by creating a journal entry (Option 2) or by triggering the configured server action (Option 1). `PROVISIONAL` — exact user-facing trigger point (a button vs. a scheduled-actions admin screen) for the server-action option was not resolved to full certainty this session; recorded `HOLD`. |
| Who/what initiates it under Daily/Monthly cadence? | A scheduled process, per the cadence setting. `VERIFIED` (existence of the setting) / `HOLD` (exact scheduling mechanics, run time, failure handling — not documented in pages fetched). |

Evidence: Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02.

### 2.2 Closing date

No dedicated "closing date" field distinct from the ordinary journal-entry accounting date was found in Layer A evidence. The closing entry's date is, by inference, the accounting date the accountant (or scheduled action) assigns to the journal entry it creates — i.e., an ordinary journal-entry date, not a specialized "period close date" concept with its own field. This is `HOLD / EVIDENCE REQUIRED` as a confirmed negative (no dedicated field found) rather than a confirmed absence proven exhaustively — a further targeted fetch of the "Configuration" section fields was not performed at field-by-field depth for this specific point.

### 2.3 Entry generation mechanics

| Option | Description (Layer A) | Fact Status |
|---|---|---|
| Option 1 — Server action journal entry | Section heading confirmed present ("Option 1: Server action journal entry") under the Accounting-side Inventory Valuation documentation page; described at a heading level as an automated/administrator-configured action that produces the closing journal entry. Full step-by-step content of this section was not captured to line-level depth this session. | PROVISIONAL (heading and general nature confirmed; procedural detail HOLD) |
| Option 2 — Manual journal entry | Section heading confirmed present ("Option 2: Manual journal entry"); general nature (accountant hand-builds the entry using the valuation report as the basis) is consistent with the periodic-valuation definition documented elsewhere on the same page and corroborating pages. Full step-by-step content not captured to line-level depth this session. | PROVISIONAL |

Both options appear, per the table-of-contents evidence, under a broader heading complex that also includes an **"Upgrade process for Anglo-Saxon Perpetual"** context — meaning at least part of this documented procedure may be specifically about **migrating** from Periodic to Perpetual (a one-time conversion), not solely about routine recurring closing. This is a material ambiguity: this session cannot yet confirm whether "Option 1"/"Option 2" describe (a) the routine recurring Periodic closing entry, (b) a one-time valuation-method migration entry, or (c) both by the same mechanism. Recorded `HOLD / EVIDENCE REQUIRED — MATERIAL`, because it directly affects how JT-07 (period close design) should be scoped.

Evidence: Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 (section-heading enumeration).

### 2.4 Periodic cadence

Confirmed options at the `Accounting -> Configuration -> Settings -> Inventory Valuation -> Periodic Valuation` field: **Manual**, **Daily**, **Monthly**. `Fact Status: VERIFIED`, evidence: Reference ERP official documentation — Inventory valuation, version 19.0, and Automatic inventory valuation, version 17.0/18.0, retrieved 2026-09-02.

No quarterly, annual, or custom-cadence option was found in evidence gathered. Absence is recorded as `PROVISIONAL` (not exhaustively tested against every version) rather than asserted as a permanent product limitation.

### 2.5 Valuation vs Variation treatment

| Concept | Role | Continental | Anglo-Saxon Perpetual | Fact Status |
|---|---|---|---|---|
| Valuation (Stock) account | Balance-Sheet asset carrying current inventory value | Same role | Same role | VERIFIED |
| Variation account | Buffer/counterpart account absorbing timing gaps between physical movement and financial posting | Functions as an **expense account** specifically for variation recording at close | Functions as either a **current asset** account (interim-tracking preference) or an **expense** account (documented alternative) | VERIFIED |
| Expense (Continental) / COGS (Anglo-Saxon Perpetual) | Where the cost ultimately lands in P&L | Debited when the **vendor bill** posts, independent of sale timing | Debited when the **customer invoice** posts, i.e., tied to the sale event | VERIFIED |

This is the single clearest Layer A finding in this file: **the reference ERP ties the accounting-standard choice (Continental vs Anglo-Saxon) to the valuation-timing choice (Periodic vs Perpetual) as a paired configuration concept**, not two independent settings free to combine arbitrarily in the documentation's own framing (though the underlying field structure may technically allow other combinations — that combinatorial completeness was not tested this session and is `HOLD`).

Evidence: Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02.

### 2.6 Prior-period handling

No Menu-F-specific "reopen a closed inventory period" mechanic was found. The only prior-period control mechanism documented at the Accounting level generally (not Inventory-valuation-specific) is the **Lock Date** system: a "Lock Everything" date prevents journal entries dated on or before it from being created or modified, with an **administrator-only exception** mechanism (scoped to current user or everyone, for a defined duration, with a required reason, and logged in the company record's audit chatter), plus a separate **Hard Lock** date described as irreversible for jurisdictions requiring inalterability.

This general Lock Date mechanism is the closest documented control to "prior-period handling" for inventory closing specifically, but it is a **general Accounting control, not an Inventory-valuation-specific one** — it locks all journal entries dated in the locked range, not specifically closing entries. This scope distinction is material and must not be silently collapsed into a COGS-specific claim.

Fact Status: `VERIFIED` (general Lock Date mechanism exists, with exception and Hard Lock) / `HOLD` (whether/how it interacts specifically with a Periodic closing entry that spans a lock boundary, e.g., a Monthly-cadence scheduled entry attempting to post into an already-locked prior month).

Evidence: Reference ERP official documentation — Year-end closing, version 19.0 (lock-date mechanics), retrieved 2026-09-02; corroborating secondary community sources not used as authority, only as pointers confirming the documentation page exists.

### 2.7 Late cost handling

No dedicated "insert a late-arriving supplier cost into an already-closed period" wizard was found. Two partial mechanisms exist in evidence:

1. **Negative-inventory compensation** (file `07`, §2.9): when a later receipt's real cost differs from an earlier estimated cost used because stock had gone negative, the reference ERP creates a compensating valuation line, which under Perpetual/Automated valuation would generate its own journal entry at the time the later receipt is processed — regardless of whether an intervening "close" happened. This is a **transaction-timing** correction, not a **period-reopening** action; it does not touch the prior closed period's posted balances, it posts the correction in the current period.
2. Under **Periodic** valuation, since no per-transaction posting occurs until the next closing entry, a late-arriving vendor bill or cost simply becomes part of what the next closing entry's variance calculation must absorb — there is no evidence of a mechanism to "go back" and correct an already-generated closing entry; the correction is expected to flow through the next cycle's Variation account movement.

Fact Status: `VERIFIED` (both mechanisms exist as described) / `HOLD` (whether the reference ERP offers any way to attribute a late cost back to the specific prior-period COGS it should have affected, versus simply absorbing it in the current period — no such attribution mechanism was found in evidence, which is itself a material finding for `JT-06`).

### 2.8 Reversal / reopening behavior

No inventory-closing-specific reversal or reopening wizard was found. The only reversal concept in evidence is the general Accounting **reversing journal entry** capability (standard double-entry reversal, not inventory-specific), and the Lock Date **exception** mechanism (§2.6), which permits a privileged user to post into an otherwise-locked period rather than "reopening" it wholesale.

Fact Status: `HOLD / EVIDENCE REQUIRED` — this session found no Layer A evidence either confirming or ruling out an inventory-closing-specific reopening concept beyond the general controls named above. Recorded as an honest gap, not a negative claim asserted with unwarranted confidence.

### 2.9 Audit trail

Documented audit-trail elements found:

- Lock-date exceptions are logged in the company record's chatter (who granted the exception, to whom, for how long, and the stated reason).
- Ordinary journal entries (including closing entries, whichever option produced them) carry standard authorship/date/reference metadata as any other journal entry in the system.

No inventory-closing-specific audit trail beyond these general Accounting-level mechanisms was found in evidence gathered this session.

Fact Status: `VERIFIED` (general mechanisms) / `HOLD` (closing-specific audit trail beyond the general journal-entry and lock-exception logging).

### 2.10 Permissions / approval

- Viewing the valuation-to-accounting linkage requires **access rights on the accounting module** (file `07`, §2.7) — a role-gate, confirmed.
- Lock-date exceptions require **administrator access rights**.
- No evidence was found of a multi-step approval workflow (e.g., a maker-checker or submit-for-approval flow) specifically for the closing entry itself, under either Option 1 or Option 2. Absence recorded as `HOLD`, not asserted as proof no such workflow exists in the product — this session's evidence pool (official documentation pages) may simply not describe an optional approval-workflow add-on if one exists.

### 2.11 Effect on Balance Sheet / P&L

| Element | Statement | Continental | Anglo-Saxon Perpetual |
|---|---|---|---|
| Valuation account | Balance Sheet | Current-asset inventory balance | Same |
| Variation account | Either | P&L (expense) | Balance Sheet (current asset, preferred) or P&L (expense, alternative) |
| Expense / COGS account | P&L | Debited at vendor-bill posting (receipt-timed) | Debited at customer-invoice posting (sale-timed) |
| Inventory Loss account | P&L (debit) / Balance Sheet (credit to Valuation) | Same structure both standards, per Layer A | Same |
| Cost of Production account | Bridges Balance Sheet (WIP/valuation) and P&L (production expense) depending on completion state | Same structure both standards, per Layer A, at the conceptual level; WIP-vs-finished-goods line mechanics not resolved to full depth (`HOLD`, cross-reference file `22`) | Same |

Fact Status: `VERIFIED` for the account-role table; `HOLD` for exact WIP staging mechanics (owned by file `22`, not re-derived here).

Evidence for §2.5–§2.11 collectively: Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02; Reference ERP official documentation — Year-end closing, version 19.0, retrieved 2026-09-02.

---

## 3. Field Evidence Sheet (governing-prompt §7 format)

| Field | Menu Path | Field Label | Purpose | Values/Options | Default | Visibility | Scope | Inherits From | Override Precedence | Transaction Consumer | Periodic Behavior | Perpetual Behavior | Account Type Impact | Financial Statement Impact | Change Impact | Version Delta | Evidence | Fact Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Inventory Valuation (model) | Accounting -> Configuration -> Settings -> Inventory Valuation | `Inventory Valuation` | Selects the valuation-timing model | Perpetual (at invoicing) / Periodic (at closing) | Periodic (per default-behavior description) | Always (may require Inventory/Accounting apps installed) | Company | N/A | N/A | Every stock/bill/invoice event | Defines the whole closing narrative of this file | Defines real-time posting instead of closing narrative | N/A (policy field) | Both, structurally | Changing mid-stream implies a migration event (§2.3 ambiguity) not a simple toggle | Labeled "Automated"/"Manual" at category level in 13.0–17.0 evidence and "Perpetual"/"Periodic" at settings level from at least 17.0 evidence onward; the two vocabularies coexist without a single reconciling page found | Reference ERP official documentation — Inventory valuation, v19.0; Automatic inventory valuation, v17.0, retrieved 2026-09-02 | VERIFIED (options) / HOLD (exact version the settings-level wording first appeared) |
| Periodic Valuation (cadence) | same | `Periodic Valuation` | Sets how often the Periodic closing entry is produced | Manual / Daily / Monthly | Manual (inferred; not separately re-confirmed as explicit default this session) | Conditional — visible only when Inventory Valuation = Periodic | Company | N/A | N/A | Scheduled or manual closing entry generation | This IS the closing mechanism | Not applicable (Perpetual does not use this field) | N/A | Drives when the closing journal entry posts | N/A | Present at least 17.0–19.0 evidence; earlier versions not independently confirmed | Reference ERP official documentation — Inventory valuation, v19.0, retrieved 2026-09-02 | VERIFIED (17.0–19.0) / HOLD (13.0–16.0) |
| Inventory Cost Method | same | `Inventory Cost Method` | Company/category-level costing method | Standard Price / FIFO / Average Cost (AVCO) | Standard Price | Always | Company/category-resolved | Product Category (Menu B) | Category over company default where override permitted; product-level override boundary owned by file `05`/`11` | Every valued transaction | Same computation, deferred posting | Same computation, real-time posting | N/A | Drives Unit Value, therefore BS/P&L indirectly | N/A | Stable option set 13.0–19.0 | Reference ERP official documentation — Automatic inventory valuation, v18.0, retrieved 2026-09-02 | VERIFIED |
| Valuation Account | same | `Valuation Account` | Balance-Sheet account holding current stock value | Any Current Asset-type account | None until Automated/Perpetual is enabled, at which point mandatory | Conditional — mandatory when Automated/Perpetual is active | Company/category | Category | Category over company default | Every valued transaction posting | Updated at close only | Updated per transaction | Asset | Balance Sheet | Changing account does not retroactively repost historical entries (inferred; not directly documented — `HOLD`) | Stable field concept 14.0–19.0 | Reference ERP official documentation — Inventory valuation configuration, v14.0, retrieved 2026-09-02 | VERIFIED (existence, mandatory-when-automated) / HOLD (retroactivity) |
| Variation Account | same | `Variation Account` | Buffer/counterpart for timing gaps at close or between physical/financial events | Expense-type (Continental) or Current-Asset/Expense-type (Anglo-Saxon Perpetual) | None until relevant model enabled | Conditional | Company | N/A | N/A | Closing entry (Periodic); ongoing true-up (Perpetual) | Central mechanism | Ongoing, smaller role | Expense or Asset, standard-dependent | P&L or Balance Sheet, standard-dependent | N/A | Present in 19.0 evidence with clear dual role; earlier-version equivalent (possibly under a different label such as an interim account) not reconciled this session | Reference ERP official documentation — Inventory valuation, v19.0, retrieved 2026-09-02 | VERIFIED (19.0) / HOLD (label continuity into 13.0–16.0) |
| Other Accounts — Inventory Loss | Accounting -> Configuration -> Settings -> Inventory Valuation -> Other Accounts (location-scoped) | `Inventory Loss` | Absorbs scrap/shrinkage/write-off value releases distinct from COGS | Expense-type account | None until configured | Conditional | Location | N/A | N/A | Scrap/write-off event | Same conceptual role | Same conceptual role | Expense (debit) / Asset reduction (credit to Valuation) | P&L + Balance Sheet | N/A | 19.0 evidence only this session | Reference ERP official documentation — Inventory valuation, v19.0, retrieved 2026-09-02 | VERIFIED (19.0) / HOLD (earlier versions) |
| Other Accounts — Cost of Production | same | `Cost of Production` | Bridges valuation and production expense for manufacturing consumption/output | Expense or WIP-type account | None until configured | Conditional | Location | N/A | N/A | Manufacturing consumption/output event | Same conceptual role | Same conceptual role | Asset (WIP) and/or Expense depending on stage | Balance Sheet and/or P&L | N/A | 19.0 evidence only this session; cross-reference file `22` for full manufacturing depth | Reference ERP official documentation — Inventory valuation, v19.0, retrieved 2026-09-02 | VERIFIED (existence) / HOLD (staging mechanics) |
| Lock Dates (Lock Everything / Hard Lock) | Accounting -> Accounting -> Lock Dates | `Lock Everything` / exception fields / `Hard Lock` | Prevents posting/editing journal entries dated on or before the lock, with a controlled admin exception | Date fields + exception scope (user/everyone) + duration + reason | None (unset) | Always (general Accounting feature, not Inventory-specific) | Company | N/A | Hard Lock overrides even the exception mechanism (irreversible) | Any journal entry dated in range, including a closing entry | Directly gates when a Periodic closing entry can post into a prior period | Same general gate applies to any correction journal entry Perpetual might need | N/A (control field) | Governs BS/P&L period integrity generally | N/A | General mechanism; not Inventory-Valuation-page-specific, cross-checked separately | Reference ERP official documentation — Year-end closing, v19.0, retrieved 2026-09-02 | VERIFIED (general mechanism) / HOLD (specific interaction with a scheduled Periodic closing entry) |

---

## 4. Layer B — Thai Accounting/Tax/Statutory Evidence

`N/A for this file — pointer only.` Thai-specific period cut-off evidence requirements, and any statutory requirement for a formal physical-count-driven closing procedure, belong to file `24` (not yet produced this session) and file `23` (`PERIOD_CLOSE_CUTOFF_RECONCILIATION_MODEL`, also not yet produced this session). No Thai statutory claim is made in this file. In particular, the question of whether Thai practice expects a documented physical-count trigger before any Periodic closing entry is posted is `HOLD / EVIDENCE REQUIRED`, not answered here.

---

## 5. Layer C — SMEsPlus Clean-Room Candidate Semantics (CANDIDATE / HOLD only — never final)

1. `CANDIDATE` — A SMEsPlus period-close concept, if adopted for a Periodic-style valuation policy, should separate three distinct roles the reference ERP's evidence conflates under one setting: (a) the valuation-timing policy choice (Periodic/Perpetual), (b) the cadence of when a resulting entry is produced, and (c) the mechanism (manual vs scheduled) that produces it. Treating these as three separately auditable decisions, rather than one combined field, is offered as a candidate design principle only — subject to Joint review (`JT-03`, `JT-07`).
2. `HOLD` — Whether SMEsPlus needs a genuine "reopen a closed period" capability, distinct from the reference ERP's general lock-date exception, is undecided. This session found no reference-ERP precedent for inventory-specific period reopening, which is itself evidence the Joint team should weigh, not a reason to assume SMEsPlus doesn't need one.
3. `HOLD` — Late-cost attribution to the specific prior-period COGS it should have affected (§2.7) is an unresolved control gap in the reference ERP evidence itself. This is flagged as a material open question for `JT-06`, not resolved by assuming either "absorb in current period" or "restate prior period" is correct.
4. `HOLD` — Whether a maker-checker/approval step should gate the closing-entry mechanism is undecided; the reference ERP shows no evidence of one, but that is evidence of the reference's own design choice, not proof SMEsPlus (operating under Thai audit expectations, still pending file `24`) does not need one.
5. `CANDIDATE` — The reference ERP's pairing of accounting-standard choice (Continental/Anglo-Saxon) with valuation-timing choice (Periodic/Perpetual) as one coupled decision (§2.5) is offered as a candidate framing question for `JT-01`/`JT-03`: should SMEsPlus allow these to vary independently, or intentionally couple them the way the reference does? Not decided here.

---

## 6. Reconciliation Identity Status (governing-prompt §14 cross-check)

| Identity | Status here | Note |
|---|---|---|
| `Periodic COGS Candidate: Opening Inventory + Net Purchases/Capitalizable Costs - Closing Inventory = COGS` | `CANDIDATE` | Consistent in shape with the Periodic model described in §2.1–§2.5 (expense recognized at vendor-bill time, then trued up via the Variation account at close), but no single fetched page states this exact formula in these terms; assembled from the account-role evidence. |
| `Cross-System Reconciliation: Inventory valuation as-of-date <-> Accounting inventory balance + reconciling items` | `CANDIDATE` | Same status as file `07` §2.7/§6 — this file adds that under Periodic, the "reconciling items" are structurally larger and only resolved at the closing event, whereas under Perpetual they are the smaller, ongoing Variation-account gap. |

---

## 7. Contradictions / Evidence Gaps Found This Session

1. **Material — Option 1/Option 2 scope ambiguity (§2.3):** cannot yet confirm whether the documented "server action" and "manual journal entry" options describe routine recurring closing, a one-time Periodic-to-Perpetual migration procedure, or both. This must be resolved (targeted re-fetch of the full section content) before file `08`'s findings are used to design any SMEsPlus closing mechanism.
2. **Material — no late-cost-to-prior-period attribution mechanism found (§2.7):** flagged for `JT-06` as an open question the reference ERP itself does not appear to answer, not merely an evidence-gathering gap.
3. Lock Date mechanism confirmed only as a general Accounting control; its precise interaction with a scheduled (Daily/Monthly) Periodic closing entry attempting to post into an already-locked period was not found in evidence and is `HOLD`.
4. Terminology-pairing gap between category-level ("Automated"/"Manual") and settings-level ("Perpetual"/"Periodic") wording, shared with file `07`, not re-resolved here.

---

## 8. Checkpoint Status

`CP-03` (Menu A-H coverage) — Menu F portion: Layer A populated including an explicit, evidence-based negative finding on wizard existence per the governing prompt's own flagged possibility; two material HOLD items raised for `JT-06`/`JT-07`. Layer B pointer-only (files `23`/`24` not yet produced). Layer C candidate/HOLD only. Not a completion claim for CP-03 as a whole.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
