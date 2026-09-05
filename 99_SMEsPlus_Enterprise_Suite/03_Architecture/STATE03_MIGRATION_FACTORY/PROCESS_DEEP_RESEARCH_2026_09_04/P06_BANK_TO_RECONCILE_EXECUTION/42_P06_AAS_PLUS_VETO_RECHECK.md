# P06_AAS_PLUS_VETO_RECHECK.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C13)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Rule observed:** *"Do not close veto merely because the underlying blocker count fell."* The blocker count **rose**, so that particular temptation did not arise — but the substantive test is applied regardless.

---

## 1. AASP-VETO-01 — reliance veto on using P06 as a specification

**Original terms.** P06 is admissible as *evidence for a decision*, not as a design specification. Three lift conditions were named:
- **(a)** `P06-B-27` answered;
- **(b)** the second independently-worded search run over every Class-A negative;
- **(c)** at least the P01, P02 and P05 packages read and reconciled.

**Condition-by-condition assessment:**

| Condition | Status | Evidence |
|---|---|---|
| **(a)** `P06-B-27` | **MET** | Closed on source evidence. The delegated set is five fields; `vat` and `company_registry` are not among them; no constraint forces branch VAT equality. `22_`, `23_`. |
| **(b)** second search over **every** Class-A negative | **PARTIALLY MET** | Run on the **two principal** negatives (identity, fees) with deliberately disjoint vocabularies; both survived. Also run on the localisation surface (`OQ-90`), which survived. **But not on every Class-A negative** — `is_internal_transfer`, `destination_journal_id`, `paired_internal_transfer`, `chargeback\|dispute` and the `provider_reference` uniqueness search have had **one** pass each. |
| **(c)** P01, P02, P05 read | **PARTIALLY MET** | **P02 and P05 read** — plus P03, P04, P07, P09, P10 and P11. **P01 is unpublished and cannot be read.** |

**And a condition that did not exist when the veto was written now applies:**
`P06-B-55` — the evidence tree is a **filtered distribution** (791 addon directories, 2 localisation packs). Every tree-scope negative inherits that boundary. **This materially affects condition (b)**: a second search over a filtered tree is a second search over the same filter.

**RECHECK VERDICT: AASP-VETO-01 — VETO PARTIALLY RESOLVED.**

**What is now lifted:** the veto no longer applies to P06's **company-boundary position**. `SCOPE-R-02`, `RM-R-10` and the A4a classification rest on a closed, source-verified fact and may be relied upon.

**What remains vetoed:** everything resting on a single-pass Class-A negative, and everything requiring P01. Specifically, the following may **not** be relied upon as specification:
- the internal-transfer findings (`P06-B-16`), which rest on three single-pass tree-scope negatives;
- the provider-reference uniqueness finding (`PPT-F-10`);
- the absence of a chargeback/dispute concept;
- any vendor-side payment ownership.

**Revised lift conditions:** (b′) second-pass search on the five remaining single-pass tree-scope negatives; (c′) P01 published and read; (d′) `P06-B-55`'s filtered-build boundary either accepted by the Boss or resolved with a complete distribution.

---

## 2. AASP-VETO-02 — veto on any implementation start for P06

**Original reason:** *"the target cannot implement four independent states, an owned bank-confirmation fact, and a company-scoped identity system while the boundary those things are scoped to is undetermined."*

**The stated reason is now discharged.** The boundary **is** determined: the financial boundary is COMPANY, the hierarchy is a TENANT-scoped grouping, and no financial guard may be written at the grouping level (`22_` §7).

**But the veto is not lifted, and the reason has changed rather than disappeared.**

**RECHECK VERDICT: AASP-VETO-02 — VETO REMAINS, ON NEW GROUNDS.**

Three grounds, none of which existed in the original wording:

1. **`P06-B-44` — the generation gap.** The only deployment evidence available is from **Odoo 19** databases while the entire P06 research target is the **v18** line. **Implementing against a researched generation that may not be the target generation is the largest avoidable error available here**, and it is cheap to rule out with one registry export.

2. **`P06-B-50` — the ledger is deletable by unauthorised SQL.** A module present in all four custom roots deletes bank statements, payments, moves, partial reconciles and chatter with no server-side authorisation, then rewinds the document sequences. **No settlement or reconciliation design can hold while that module is installable**, because it defeats every control the design would add.

3. **Twenty-six `HOLD — DESIGN DECISION REQUIRED` items are undecided.** Implementation cannot begin on a design that has not been decided. This is not an evidence deficit — it is the ordinary sequence of work.

**Lift conditions for AASP-VETO-02:** target generation confirmed; `P06-B-50` remediated or the module confirmed absent from the target; and Boss decisions on the design-decision population.

---

## 3. New veto raised by this continuation

**AASP-VETO-03 — VETO on any P11 reconciliation that treats P06's tree-scope negatives as Odoo 18 negatives.**

`P06-B-55` establishes that the evidence tree is a filtered distribution. P11's unified registers will consume P06's negatives alongside peers'. If a peer researched against a **complete** distribution and P06 against a **filtered** one, a unified "not found in v18" row would be built from two incompatible denominators.

**This is the `count unit vs population` defect at programme scale**, and P06 raises it against its own contribution rather than waiting for it to surface at reconciliation.

**Condition to lift:** P11 records the evidence-base boundary alongside each P06 negative, or the peers confirm they used the same filtered build.

---

## 4. Consolidated veto status

| Veto | Prior | Now |
|---|---|---|
| **AASP-VETO-01** reliance | UPHELD | **PARTIALLY RESOLVED** — company-boundary position released; five single-pass negatives and all P01-dependent items remain vetoed |
| **AASP-VETO-02** implementation | UPHELD | **REMAINS — on new grounds**; the original ground is discharged |
| **AASP-VETO-03** evidence-base boundary at P11 | — | **NEW** |

**One veto partially resolved, one sustained with changed reasoning, one newly raised.** A recheck that produced only releases would not have been a recheck.

---

## 5. AAS+ position on the continuation itself

**AASP-F-08 — This continuation did what a targeted closure round should do, and its most valuable output is not a closure.**
Four blockers and four open items closed on evidence. But the round's three most consequential products are **new**: `P06-B-50` (the ledger is deletable), `P06-B-44` (the generation gap), and `P06-B-55` (the evidence base is filtered). **None of the three would have been found by working the existing blocker list in order** — they came from following the evidence where it went.

**AASP-F-09 — The package's self-correction rate improved, and the mechanism matters.**
Seven author errors are now recorded across two rounds. Five of seven were caught by something other than the author re-reading their own work: three by an independent pass, two by executing a command that had only been declared. **The two caught unaided were both caught this round.** That is a real improvement, and it is attributable to running counts rather than asserting them.

**AASP-F-10 — The standing defect is unchanged and is now two rounds old.**
There is still **no severity model**. AAS+ recommended ranking by *precondition reachability* at the prior round; twelve blockers were added this round without ranking. **Fifty-four blockers with no ordering is a list, not a register**, and the Boss cannot act on a list. This is the single most useful thing a successor round could produce, and it requires no new evidence at all.

**AASP-F-11 — One dissent from the package's own framing.**
The handoff will say P06 is ready as evidence. AAS+ agrees. But the package still leads with *"seven confirmed defects"*, and after this continuation the honest headline is different: **the bank half of P06 runs on unmodified reference behaviour, and the custom estate can delete the ledger without authorisation.** The second clause is new, it is worse than the first, and it should lead. Recorded as `DIS-11`.
