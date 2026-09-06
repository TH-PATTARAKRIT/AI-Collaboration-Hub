# P11 — ACCOUNTING TRUTH CONVERGENCE MATRIX

`[SMEPLUS-26-09-06-…-CORR2-PHASES-001]` · `CP-P11C2-08` · **PHASE S** · Layer 1 clean-room

> Each row is a **candidate accounting truth** reconciled from published peer evidence.
> **Scope** is `PLATFORM` / `TENANT` / `COMPANY`. **Class** is the evidence class of the *reconciled*
> statement, never the strongest contributing source. **Nothing here is final.**

---

## 1. Converged — independent processes reaching one accounting statement

| id | Candidate accounting truth | Converging processes | Scope | Class |
|---|---|---|---|---|
| `P11-C-09` | ~~**Reached separately, with separate evidence, by three processes**~~ — **CONVERGENCE LABEL WITHDRAWN (`X3-X1`).** P06's own basis column shows the topology is **one responder satisfying two requesters**: `P07-R-01` closes *"`X-07`, **and P08's `XP-05`**"*; `P07-R-03` closes *"`X-09`, **and P08's `KRN-INV-01`**"*; and **`PBD-F-04`: "`P07-R-01` and `P07-R-03` are the same two requirements P08 asked for."** P11 relayed P06's word *"converge"* **without testing it, and never read P07 at its frozen SHA**. Further: **none of the five cited ids asserts *identity*** — that leg enters only through P06's summary sentence, and `KRN-INV-01` is a duplicate-detection invariant, not a settlement-reversal one. **What survives: a settlement event needs a date and a reversal link, requested by P07 and P08, committed to by P06 — a requirement with two requesters, not a convergence** | `P06` (responder) ← `P07`, `P08` (requesters) | `PLATFORM` | **`CANDIDATE HANDOFF` — not a convergence** |
| `P11-C-12` | **RE-SCOPED (`X1-C1`, `X1-2`).** The generalisation *"the estate has reconciliation where it is vacuous"* **equivocates on two mechanisms**: the *exists* half is **open-item matching** (P01, AP 97.89 %), the *vacuous* half is **control-account tie-out** (P08). They are different objects. **And the party-dimension identity is empirically falsifiable and falsified** — P01 measures **10 of 1,904** vendor bills balancing to a non-payable account, *"a subledger-to-ledger reconciliation difference — **P11's and P08's scope**"*. **What survives, within P08's own scope:** where the subledger *is* the ledger filtered by account, agreement is **not evidence**; and the two genuinely separate stores carry **no kernel tie-out**. **P11's "second route" is not independent** — its rule tests `S3`/`S4` and **expressly excludes `S2`, the tie-out criterion** (`X1-2`); and the count is *0 of 7 **unqualified***, not 0 (`X1-3`) | `P08` (kernel, within its stated scope) | `PLATFORM` | **`SUPPORTED INTERPRETATION — P11`** (downgraded from `FACT VERIFIED`) · **carries `P08 AAS+-VETO-01`** |
| `P11-C-13` | **One configuration decision with five consequences.** `property_valuation = manual_periodic`, **126 of 126 categories, 4 companies** — closes the valuation-accounting gate and makes four downstream mechanisms unreachable. **Accepted for carriage as one item.** `P01`'s accompanying claim that *P11 was already carrying five* was **checked against P11's registers and is false** — P11 carried **none** as blockers (`P11-E-37`). **The collapse is `0 → 1`** | `P01` (own correction); P11 verified the register claim | `COMPANY` | `FACT VERIFIED` (the setting) · `CONTRADICTED` (the register claim) |
| `P11-C-10` | **A named evidence hold carried by two processes may already be discharged by a third.** `P04-B-51`/`P03` hold on series-16 source vs `P01` `ERR-P01-41` | `P01` vs `P03`/`P04` | — | `EXTERNAL / PEER OWNER — HANDOFF PUBLISHED` |
| `P11-C-11` | **An unresolved P11 boundary was adopted by a peer as programme policy and eliminated a Boss option.** Withdrawn at both ends | `P10` (`41_`) · **P11** | `PLATFORM` | `CONTRADICTED — CORRECTED AND CLOSED` |
| `P11-C-14` | **Correction-as-immutable-reversal is the one measured-clean accounting behaviour — and the deletion path bypasses it entirely** | `P01` (5,115 pairs, 0 unresolvable) · `P06`/`P01` (deletion) | `COMPANY` / `PLATFORM` | `FACT VERIFIED` + `UNRESOLVED` |

## 2. Reconciled facts — single-owner, received and attributed

| Candidate truth | Owner | Scope | Class |
|---|---|---|---|
| Event identity exists on **one** inbound channel, nullable, **unpopulated on all 13,814 rows**; absent as a **platform property** | `P08` | `PLATFORM` | `FACT VERIFIED` — class **`C`** for the absence claim |
| **No accounting-period object.** A period is a date range on a company record | `P08` | `PLATFORM` | `A VERIFIED ABSENCE`, 7-observation limit |
| **No as-of reconstruction** of any balance; `amount_residual` is current state only | `P08` | `PLATFORM` | `FACT VERIFIED` |
| **0 of 6** transacting companies set a close; **no lock date on 3 surfaces / 169,143 entries** | `P08` · `P01` | `COMPANY` | `FACT VERIFIED` |
| Settlement chronology untrustworthy: **46.4 %** after, **44.3 %** before as-of date, max **594 days** | `P08` | `COMPANY` | `FACT VERIFIED` |
| Ledger arithmetic sound: **0 unbalanced posted entries / 169,143**; attribution **447,384 of 447,384**; settlement residual drift **0** | `P08` | `COMPANY` | `FACT VERIFIED` |
| Provenance gap: **41.89 %** of items cannot name their entry; **17.00 %** carry no origin mark | `P08` | `COMPANY` | `FACT VERIFIED` |
| GRNI is a **swept suspense account, not an item-matched bridge** — 13,666 posted items, **−฿7,048,692.08**, `reconcile='f'` | `P01` | `COMPANY` | `FACT VERIFIED` |
| Price differences: **1,175 of 1,267 never reach the GL**; the 92 that do net **−฿7,267,712.95 against Raw material**; **1,082 of 1,175** sit on a bill line posted to **P&L** | `P01` | `COMPANY` | `FACT VERIFIED` — replaces a statement *"FALSE IN BOTH HALVES"* |
| Conversion cost **zero in every examined deployment**; **no fixed overhead exercised anywhere**; resources-with-rate and automated valuation **never co-exist** | `P03` | `COMPANY` | `FACT VERIFIED` (measured half) |
| **30 valuation records to ±1.5 × 10²¹**, inventory valuation distorted **−48.7 %**, 25 diverge from the ledger | `P03` | `COMPANY` | `FACT VERIFIED` |
| Cost centres bear **≈ zero net depreciation**; margin **overstated by the amount erased**; **12 of 23** net exactly 0.00 | `P09` | `COMPANY` | `FACT VERIFIED` — **`CONFIRMED` at generation 4** |
| Gross cross-centre movement **154,922,194.55** ≈ **43×** the scalar net; displacement **2,019,008.49 each way** inside zero-netting entries | `P09` | `COMPANY` | `FACT VERIFIED` |
| Petty cash is the **dominant** expense mode — **634 of 993 (63.8 %)**; reimbursement path used **twice** | `P05` | `COMPANY` | `FACT VERIFIED` |
| A WHT rate record **named `WHT3%` valued `0`**; **2,038 payments / ฿21,556,228.06** posted after zeroing; amounts **hand-entered** | `P01` | `COMPANY` | `FACT VERIFIED` |
| The reference asset engine **cannot post off-balance** | `P04` | `PLATFORM` | `FACT VERIFIED` |
| `om_data_remove` **installed** (`16.0.1.0.1`, series-16 — P01), raw `DELETE FROM` + commit, **no server-side authorisation**; valuation↔entry FK is **`ON DELETE SET NULL`** (series-16 schema). P06's `REACHABLE — DEPLOYMENT VERIFIED` is **on a v19 database *not confirmed to be the SMEsPlus target*** (`iEVING`, a BHPRO database), with the **v18 source chain `SOURCE-REACHABLE / RUNTIME UNVERIFIED`**. **A first-party remediation module states the path *has already been run and produced user-visible breakage*** | `P01` (series-16) · `P06` (v19, non-target) | ~~`PLATFORM`~~ **`COMPANY` / series-16 · plus one non-target v19 deployment** | `FACT VERIFIED` **within those scopes** |

## 2b. Facts P11 held and did not carry — accepted from the challenge

| Fact | Owner | Why it matters |
|---|---|---|
| **`฿29,029,467.66` received-not-invoiced**, 1,580 PO lines, *"recognised nowhere in the ledger — no receipt entry, no clearing balance, no accrual"*; accrual control **0 of 15,522** | `P01`, in a section headed ***"THE NUMBER P11 AND P08 BOTH NEED"*** | **The largest unrecognised position in the frozen evidence.** A pure completeness / cut-off item — P11's own core subject |
| **10 of 1,904** vendor bills balancing to a non-`liability_payable` account, **฿12,969.27** | `P01`, routed explicitly as *"P11's and P08's scope"* | Falsifies the unqualified form of `P11-C-12` |
| ***"The general ledger is intact and sane"* is WITHDRAWN** → **8 posted items > ฿1bn; ฿39.2m misallocated** | `P01` | Internal unsoundness invisible to balance arithmetic, while `CQ-P11-08` concluded *"internally sound"* |
| **GRNI gross: ฿1.9bn swept manually**; **−฿1,742,591,244.82** of chart-of-accounts reclassification across 51 items / 28 manual entries; only ~45 % of gross movement is PO-driven | `P01` | P11 carried the **net −฿7,048,692.08** one day after publishing `P11-F-15`: *"a net of zero is not evidence that nothing happened."* **P11's own lesson, unapplied, in the round that wrote it** |
| `47,801` valuation layers are **96.2 % migrated series-14**; the defensible series-18 runtime set is **558** (`ERR-P01-27`) | `P01` | P11 computed a series-18 zero-signature over a population that is overwhelmingly series-14 |
| The series-18 and series-19 zeros are **same shape, different cause** — P01 heads the warning ***"THE ITEM MOST LIKELY TO BE MIS-CARRIED"***: merging them makes *"both errors available and both wrong"* | `P01` | `B-26` merged them |

**`P11-B-28`. None of these is P11's discovery; all were in artefacts P11 declared consumed.**

## 3. Withheld — evidence insufficient, and deliberately left so

| Withheld | Why |
|---|---|
| **30 producer debit/credit cells** | Not derivable from convention. `P01` `ERR-P01-49` demonstrates the convention would have been **wrong in both halves** |
| Any statement that a zero means "never happened" | `OC-10` — the deletion explanation is unexcluded |
| Any deployed-estate conclusion from an 18.0 source line | `P11_B17_SCOPE_REPAIR_CORR2.md` |
| Any P09 mechanism claim as describing a running system | `P09 AAS+-VETO-04` |
| Any aggregation of negatives across processes | `P06 AASP-VETO-04` — each peer must first declare its addons-path population |

## 4. Counts

| | |
|---|---|
| Converged candidate truths | **6** |
| Reconciled single-owner facts | **17** |
| Withheld classes | **5** |
| Decided by P11 | **0** |
| `FINAL`-class labels used | **0** |

**`CP-P11C2-08` — COMPLETE — EVIDENCE VERIFIED.**
