# P08_P11_RECONCILIATION_BOUNDARY_HANDOFF

Prompt `[SMEPLUS-26-09-06-P08-R2R-DOMAIN-PURE-BOUNDED-CLOSURE-002]` · **PHASE S** · answers `CQ-P08-09`

> **P08 states what the ledger can and cannot supply to a reconciliation. P08 does NOT define the reconciliation architecture. Every item is a CANDIDATE awaiting PHASE B.**

---

## 1. What P08 can supply

| # | Supplied | Quality | Class |
|---|---|---|---|
| 1 | Every posted monetary fact, at item granularity | **arithmetically sound, and the claim is TOLERANCE-INDEPENDENT.** Re-run in exact decimal arithmetic (`Q-P08-01`, 2026-09-07): **0 unbalanced posted entries in the reporting currency at exact equality, at 1e-7, at 1e-4 and at 0.005** — on **both** the computed debit-minus-credit and the **stored** balance column, and across ~~**all three** deployed databases (169,143 + 16 + 6 posted entries)~~ → **`P08-C1`, 2026-09-08: the FOUR FROZEN RC-05 DATABASE EXTRACTS** (`DB-SM` 169,143 · `DB-BK` 16 · `DB-EV` 6 · **`DB-T2` 5** posted entries with lines; **417,700 + 563 + 15 + 14 posted lines**). **"four frozen RC-05 database extracts" is the correct wording and "the complete deployed estate" is NOT claimed** — deployment completeness is unproven and is not tested by this measurement. The three-DB figure is preserved above as lineage; it was never wrong, it was **incomplete against the frozen population**. **The previously published *"at 1e-7 the answer is 3, all float artefacts"* is DELETED — the figure had no referent** (`P08-CONTRA-75`). **The word "complete" remains WITHDRAWN (`P08-CONTRA-73`)**: a module installed on ~~all three databases~~ → **all FOUR frozen RC-05 extracts (`P08-C4`, 2026-09-08 — executed, see below)** deletes the ledger in raw SQL (§5) | `CANDIDATE OUTPUT`, qualified |
| 2 | The settlement graph | **63,773 records, 100,580 lines.** Residual drift **0 at tolerance ≥ 1e-6**; re-run at **exact equality it is 2,354 lines, worst residual 2.1 × 10⁻⁹** — a stored-float artefact of the settlement amount column. **Unlike row 1, this claim IS tolerance-dependent, and the tolerance must travel with it** | `CANDIDATE OUTPUT` |
| 3 | Company and journal attribution on every item | mirrors agree **447,384 of 447,384** — *unit note: this is the all-states item population; the posted population is 417,700* | `CANDIDATE OUTPUT` |
| 4 | Posting state and date | present on every entry | `CANDIDATE OUTPUT` |
| 5 | Origin pointers where they exist | **CORRECTED — `P08-CONTRA-63`.** **78.03%** of posted entries carry a *structured* origin pointer. The 96.1% previously published counted **free-text reference** as an origin pointer, while another file in the same package treats reference as a separate thing. For a reconciliation consumer the difference is ~30,750 entries whose only provenance is unparsed text | `CANDIDATE OUTPUT`, predicate now declared |

## 2. What P08 cannot supply, and why

**This is the more important half.**

| # | Not supplied | Why | Class |
|---|---|---|---|
| 1 | **An independent record to reconcile the ledger against** | for the party dimension there is none — the subledger **is** the ledger filtered by account, so agreement is **true by construction and unverifiable** | `FACT VERIFIED` |
| 2 | **A reconciliation obligation for the genuinely separate stores** | the asset register and the inventory valuation record **are** separate stores; **the kernel imposes no tie-out, no periodic proof and no exception** | `FACT VERIFIED` — `P08-RQ-KRN-01` |
| 3 | **An as-of reconstruction of any balance** | no bitemporal record; `amount_residual` is current state only | `FACT VERIFIED` |
| 4 | **A period to reconcile within** | **RE-SCOPED — `P08-CONTRA-68`.** No accounting-period object exists **in the declared 18.0 root set**. **The 19.0 line carries a dated, recurring return object, and both 19.0 deployed databases carry its linking column on the entry table.** It is a tax return, not a general accounting period — but P11 must not receive the absolute | `A VERIFIED ABSENCE`, **scope: the declared 18.0 root set only** |
| 5 | ~~A trustworthy settlement chronology~~ **WITHDRAWN — `P08-CONTRA-57`.** The as-of date is **computed by the accounting kernel** as the later of the two items' accounting dates. The 46.4%/44.3% split compared a system write timestamp against that derived date and **contains no defect** | — | `CONTRADICTED — CORRECTED` |
| 6 | **A durable event identity to reconcile on** | identity exists on **one** inbound channel, on a nullable column, **unpopulated on all 13,814 rows** | `FACT VERIFIED` — base narrowed in `48` §2.2 |
| 7 | **Provenance at the level a reconciliation would read** | 41.89% of items cannot name their entry; 17.00% carry no origin mark | `FACT VERIFIED` |
| 8 | **A closed period as a stable comparison basis** | close is a date comparison; **0 of 6 transacting companies** set one | `FACT VERIFIED` |

## 3. What P11 must decide — stated, not answered

| # | Question P11 owns |
|---|---|
| 1 | Whether reconciliation is a **derivation** over one ledger or a **comparison** between two independent records — the benchmark makes the first structurally unavoidable for the party dimension |
| 2 | What a control-account tie-out means when the subsidiary record is the same rows |
| 3 | How a reconciliation is expressed **as of** a date when no as-of reconstruction exists |
| 4 | Whether the failure of a tie-out is itself an accounting event |
| 5 | How two Pxx truth sets are compared at all — **`EXTERNAL DOMAIN BOUNDARY — ROUTE TO P11 / PHASE B`** |

**P08 answers none of these and offers no preferred option.**

## 4. Boundary discipline observed

- P08 did **not** open P11's package, define its architecture, or rank its options.
- P08 did **not** research any producer's lifecycle to characterise what it emits.
- Every peer-supplied fact used here is **attributed and marked as received**, never restated as P08's own.
- **`AAS+-VETO-01` applies to this handoff.** No item here may be relied upon for design until its two conditions are met.

**Disposition: `EXTERNAL DOMAIN BOUNDARY — CANDIDATE HANDOFF RECORDED`.**


---

## 5. Correction after the bounded AAS-03 challenge — a destroyer of reconcilable facts

**`P08-CONTRA-55`. The single most consequential omission from this handoff.**

A module ~~**installed in all three deployed databases**~~ → **installed in ALL FOUR FROZEN RC-05 EXTRACTS** **[`P08-C4`, 2026-09-08 — `om_data_remove` returns `state=installed` in `DB-SM`, `DB-BK`, `DB-EV` and `DB-T2`, read from each extract's own `ir_module_module`. This is a statement about the FOUR FROZEN EXTRACTS, not about the deployed estate, whose size is unproven. Install state is **capability**; whether the path was ever executed is still NOT evidenced.]** deletes, in unqualified raw SQL and in this order: the **settlement table**, then the **journal item table**, then the **journal entry table** — with **no company predicate, no state predicate, a commit after each table**, and a reset of the entry-number sequence to **1**.

| Consequence for P11 | |
|---|---|
| §1 item 2 offers the **settlement graph** as reconcilable | it is deletable outside the object layer |
| §1 items 1 and 4 offer **posted facts and their state** | posted entries are removed exactly as drafts are |
| `56` §2 ranked settlement referential integrity as the one control that **holds** | it does not |
| `PR-04` entry numbering | a sequence reset permits previously-issued numbers to be re-issued |

**Handed to P11 and to P06 as **`P08-HO-13`** (re-numbered under `Q-P08-02`).** P08 records the mechanism and the install state. **Whether it has ever been executed on any deployment is not verified by P08** — a peer has published an observation to that effect and it is recorded as **received and attributed, not re-derived**.

## 6. Handoffs added after challenge

| ID | To | Content |
|---|---|---|
| `P08-HO-13` | **P11, P06** | the deletion path above |
| `P08-HO-14` | **P07** | the statutory register family selects on **two different period bases** — two handlers on the tax period, two on the accounting date — so the 5,228 entries where the two differ can appear in one and not the other |


## 7. Version standing of this handoff — stated plainly because it was measured against it

**This file carries zero version markers across 29 table rows.** `53` claimed version discipline on every row; a challenger measured **84.3% of rows across `53`–`58` unmarked**, and this artefact and `57` at **100% unmarked**.

**Every kernel claim in this handoff rests on the 18.0 line. No deployed database runs it.** `DB-SM` (99.987% of the estate's posted entries) runs 16.0, whose core source **is not on this host at all**; `DB-BK` and `DB-EV` run 19.0, whose source **is on this host, was never searched, and already contradicts one absolute in this file** (§2 row 4).

**P11 must read every row of this handoff as an 18.0 statement until it is re-derived on the line the consumer actually runs.** `P08-U-28`.


---

## 8. `Q-P08-01` — re-issue of §1 item 1, and the full exact-arithmetic re-run

Executed 2026-09-07 under Boss authorization `PHASE-S/Q-BOSS-01` (branch `audit/account-phase-s-closure-2026-09-06-001` @ `1bf9b40`), against queue item `Q-P08-01` (branch `audit/account-xrecon-2026-09-06-001` @ `3291210`). Source baseline `00ccd66`.

### 8.1 What was wrong

§1 item 1 published: *"at 1e-7 the answer is 3, all float artefacts on eight-figure sums."*

**The figure had no referent.** It is **deleted**, not re-scoped. `P08-CONTRA-75`.

### 8.2 The mandated re-run — every balance measurement, exact decimal arithmetic, no floats

**INSTRUMENT:** `decimal.Decimal`, precision 50, parsed from the deployed COPY extracts. **UNIT:** one posted entry. **POPULATION:** ~~every posted entry in all three deployed databases~~ → **`P08-C1`, 2026-09-08: every posted entry with lines in the FOUR FROZEN RC-05 DATABASE EXTRACTS.** **Four frozen extracts, NOT an established deployment census.** **CONTROL:** the same instrument returns non-zero on the transaction-currency frame and on the settlement reconstruction, so it is capable of reporting a defect.

| Measurement | exact | 1e-7 | 1e-4 | 0.005 |
|---|---|---|---|---|
| Unbalanced posted entries, reporting currency — **`DB-SM`** (169,143), debit−credit | **0** | **0** | **0** | **0** |
| — same, on the **stored balance** column | **0** | **0** | **0** | **0** |
| — **`DB-BK`** (16) and **`DB-EV`** (6), both columns | **0** | **0** | **0** | **0** |
| — **`DB-T2`** (**5** posted entries with lines, **14** posted lines), both columns **[`P08-C1`, 2026-09-08 — fourth frozen RC-05 extract, added to this table]** | **0** | **0** | **0** | **0** |

> **`P08-C1a` — a tool-version precondition travels with the four-input figure.** `DB-T2` is written in archive format **1.16** and `pg_restore` **16.15** refuses it: `unsupported version (1.16) in file header`. The other three extracts are readable by both **16.15** and **18.6**; **`DB-T2` is readable only by 18.6.** A verifier on `pg_restore` 16 therefore gets **fail-closed exit 3 on `DB-T2`**, not a fourth zero — **the instrument refuses rather than reporting an unreadable extract as an empty ledger**, which is the behaviour its `C4` control exists to guarantee. **Reproducing the four-input result requires `pg_restore` ≥ 18.** Executed evidence: `RC05_CONFIRMATION_2026_09_08/run/C7_archive_version_boundary.txt`.

> **There is no tolerance at which the count is non-zero, on either column, in any deployed database.** The claim is **tolerance-independent**, and stating a tolerance beside it was itself the error.

**Other balance measurements re-run in the same pass, reported for completeness:**

| Measurement | Exact-arithmetic result |
|---|---|
| Transaction-currency: non-netting posted entries | **1,851** (`DB-SM`); 0 in the two 19.0 databases |
| — carrying a company-currency counter-leg (exculpated) | **1,847** |
| — **genuine** | **4** — unchanged, and **not re-opened**; sound under five predicate forms and a 1,847-row discriminating control |
| Settlement reconstruction, 63,773 settlements over 100,580 lines | drift **0 at ≥ 1e-6**; **2,354 lines at exact equality**, worst residual **2.1 × 10⁻⁹** |
| Posted entries with every line zero — reporting frame | **38** (`DB-SM`), **5** (`DB-BK`), 0 (`DB-EV`) |
| — same, **both frames** | **36** (`DB-SM`), **5** (`DB-BK`), 0 (`DB-EV`) |

### 8.3 An observation the re-run supports, stated as an interpretation and not as a fact

**The balance measurement has no float artefact at any tolerance. The settlement measurement does** — 2,354 lines at 2.1 × 10⁻⁹, because the settlement amount is stored as a floating-point column.

**A float artefact belonging to the settlement measurement appears to have been attached to the balance measurement.** `SUPPORTED INTERPRETATION` — the mechanism was not traced, and the round that published the figure is closed. What is `FACT VERIFIED` is only that the balance figure has no referent and the settlement figure does.

### 8.4 Bounds and what this does not do

- The all-zero row above is **reported, not repaired.** The claim *"38 … in both frames"* stands elsewhere in the package as a **registered defect** (`IVR-F-08`) belonging to no authorized queue item. **Correcting it here would be re-scoping and is not done.**
- **`RC-05` is REQUIRED for this item and is NOT satisfied.** No structurally independent challenger exists (`PHASE-S/Q-BOSS-02`, raised and unanswered). **This repair is executed; the item does not close.**
- **P11 notification is a separate completion condition** — issued as `P08_NOTIFICATION_TO_P11_Q_P08_01.md`.
