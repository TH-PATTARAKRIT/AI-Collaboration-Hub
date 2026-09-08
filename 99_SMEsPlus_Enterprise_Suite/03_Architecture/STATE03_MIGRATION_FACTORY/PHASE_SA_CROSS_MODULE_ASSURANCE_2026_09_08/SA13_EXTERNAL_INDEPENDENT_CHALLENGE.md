# SA13 — EXTERNAL AND INDEPENDENT CHALLENGE

Status: **HOLD** — challenge executed, and **this session's challenge does not satisfy the
programme's own independence standard.** §1 states why, before any result is reported.

---

## 1. The independence limit of this challenge — stated first, not in a footnote

Two standing rules bear directly on the challenge performed in this session.

**Boss decision `04_BOSS_DECISION_SMT_GRC_ASSURANCE_STRUCTURE` (`fa57d10f`, `APPROVED`)** sets the
independence constitution, quoted:

> **DESIGNER != INDEPENDENT CERTIFIER**
> **IMPLEMENTER != SOLE VERIFIER OF OWN CONTROL**
> **AI AGENT != INDEPENDENT ASSURANCE AUTHORITY**

and `GRAO-03 — DESIGNER MUST NOT SELF-DECLARE INDEPENDENT CERTIFICATION.`

**The programme has already ruled on same-model verification.** `XRD-009` is recorded
`NOT SATISFIED` on the ground that *same-model verification is not structural independence*, and
`PHASE-S/Q-BOSS-02` — who may act as an eligible challenger — is **raised and unanswered**.

**Consequence for this register.** The challenge layers used in this session are agents of the
same model as the author. Under the two rules above they are:

- a **legitimate internal challenge** — they found real defects the author had not seen, and
  those are reported below;
- **not** independent assurance, **not** certification, and **not** a discharge of any veto.

`SA13` therefore reports findings and claims no independence. Whether an eligible independent
challenger exists is `PHASE-S/Q-BOSS-02`, which is Boss-owned and open.

---

## 2. Defects this challenge found in the author's own work

Reported because a challenge that reports only other people's defects has not been performed.

| # | Defect in this session's package | Disposition |
|---|---|---|
| CH-01 | The Inventory R4 package was cited to a branch that does not carry it | Corrected by population, `SA01-C-01`; re-verified independently before adopting |
| CH-02 | The multi-tenant invariant set was referred to by one figure when two live totals exist (50 and 58) | Corrected, `SA01-C-02` |
| CH-03 | `SA11-F-03` claimed no consolidated standards map exists. An applicability register and a traceability specification **do** exist at Boss-decision level | Corrected and narrowed to `SA11-F-04`, `SA11` §7.5 |
| CH-04 | Four instrument defects in the author's own measurement — a false positive, a false negative, a corpus of 2,722 empty files that passed its own coverage assertion, and a delimiter collision | All corrected before any result was relied on; published in `SA00` §3 |
| CH-05 | A miscount in the author's own `SA15` traversability table | Corrected; the table now enumerates identifiers and a check confirms 4 + 7 + 7 = 18 with no duplicate or missing identifier |
| CH-06 | A vendor token introduced into `SA06` by the author's own edit | Caught by the pre-commit sweep and removed; count returned to 0 |
| CH-07 | An awk-based count of the cross-module dependency matrix returned 12 where visual enumeration gives 13 | Corrected; the peer's figure was right and the author's instrument was wrong |
| **CH-08** | **The author did not consume an existing readiness artefact present on this very branch** — `ACCOUNT_PHASE_SA_INPUT_OUTPUT_READINESS_PACK.md`, which already classifies all eleven Account interfaces | **Material.** Consumed and reconciled at §4 below |

`CH-08` is the most serious of these. It is the same defect class the programme has recorded
before: *an evidence base is itself a claim*, and the author asserted a baseline without first
enumerating what the branch already carried.

---

## 3. SA13-F-01 — the gate that authorized Phase SA entry declares a verdict the constitution prohibits

The SMEsPlus constitution forbids a session declaring `PASS`. The eleven Account owner packages
observe it scrupulously — across all eleven package roots, `PASS` appears only in negation or
prohibition, with **no affirmative-verdict use**.

The **Final Independent Gate of 2026-09-08** — the gate whose closure produced
`CP-SC-15 — PHASE S CONDITIONALLY CLOSED / PHASE SA ENTRY AUTHORIZED`, and therefore the
authority under which this session runs — uses it as its verdict. Verified on this branch:

| File | Line |
|---|---|
| `00_FINAL_GATE_AUTHORITY_AND_POINTER_INTEGRITY.md` | `**Status: PASS.** No stale authority pointer was used for this gate.` |
| `01_GATE01_P06_RC04_DELTA.md` | `**Status: PASS. …**` |
| `02_GATE02_P09_RC01_M2_DELTA.md` | `**Status: PASS. …**` |
| `03_GATE03_P08_RC05_INDEPENDENT_RUN.md` | `**Status: PASS. …**` |
| `04_GATE04_P11_RC06_DELTA.md` | `**Status: PASS. …**` |
| `06_GATE06_B37_CLOSURE_TEST.md` | `**Status: PASS. …**` |
| `08_FINAL_CROSS_PACKAGE_RECONCILIATION.md` | `**Status: PASS.**` |
| `11_FINAL_PHASE_S_CLOSURE_CRITERIA_TEST.md` | `**Closure recommendation: PASS TO BOSS FINAL DECISION.**` |
| `FINAL_GATE_AUTO_RESUME_STATE.md` | `Gate results: G01 PASS; G02 PASS; G03 PASS; G04 PASS; … cross-package PASS.` |

**Why this matters, and what it does not mean.** It does **not** mean the gate's work was wrong;
the underlying deltas were executed and are citable. It means the **verdict vocabulary of the
authorizing gate is one the programme prohibits precisely because it is read as approval** —
and the entry authorization derived from it now carries that reading.

**Compounding factor.** Four owner packages (P06, P08, P09, P11) each closed on an owner
self-test of the form *"… DELTA SELF-TEST PASS"*, each immediately qualified *"owner self-test
only. Not independent certification"*, and each sits beneath a parent verifier result recorded as
`RC-04 = FAIL`, `RC-01 = FAIL` and `RC-06 = FAIL` respectively.

**Disposition.** Recorded, not corrected — this session has no authority to edit another gate's
verdict. Carried to `SA19` as a governance item for Boss. **SMEs Core is the first detector.**

---

## 4. Reconciliation with the readiness pack this session had not consumed (`CH-08`)

`ACCOUNT_PHASE_SA_INPUT_OUTPUT_READINESS_PACK.md`, on this branch at `b1d24eea`, classifies
eleven Account interfaces and states its posture explicitly:

> **There is no global Account HOLD in this pack, and that is a deliberate correction of the
> prior posture.**

Its result: **9 `READY-WITH-DELTA` · 2 `EXTERNAL-DECISION-PENDING` · 0 blocked on Account
research.** The two pending are Inventory/COGS (a business policy decision — *"no further
evidence changes it"*) and Thailand Tax (a Boss-owned routed question).

### 4.1 Is this in conflict with this package's many `HOLD` rows?

**No, and the distinction is important enough to state precisely.**

| The readiness pack asserts | This package asserts | Relationship |
|---|---|---|
| Account's **interfaces** are usable, per interface, with named deltas | Account's **cross-module routes** cannot all be traversed | Different units — an interface being usable does not make an end-to-end route traversable |
| No global Account HOLD | 7 of 18 business natures `HOLD` | The seven `HOLD` natures are blocked by **SA-D05, D17, D18, D19, D20** — none of which is an Account interface |
| Zero interfaces blocked on Account research | `XD-01` blocks a Group A item on Accounting authority | `XD-01` is a **decision**, not research. The readiness pack's own rule — *"this attribute waits for a decision, not for more research"* — is exactly the right classification for it |

**Adopted.** This package adopts the readiness pack's per-interface classification and its rule
that **a classification is per interface, never per package**. `SA02` and `SA03` are read
subject to it: where they record an Account-side gap, that gap is a **named delta on one
interface**, not a reason to hold Account as a whole.

### 4.2 The pack's gap set, carried

`G-01` source business event identity — absent as a platform property, **eight processes depend
on it** · `G-02` accounting date system-derived in at least one estate generation ·
`G-03` tax point (external) · `G-04` recognition collapsed into posting — the estate reliably
carries one of four distinct times · `G-05` currency measurement frame ·
`G-06` valuation/cost basis (external — one configuration decision, five consequences) ·
`G-07` tenant scope · `G-08` analytic attribution must be consumed **gross per cost object,
never net** · `G-09` the settlement event's own date, required and unsourced ·
**`G-10` reversal/correction lineage — immutable reversal measures clean, but *a deletion path
bypasses it and leaves no trace by design*** · **`G-11` period / cut-off membership — *no
accounting-period object*, no company observed closing** · **`G-12` statutory grouping scope,
Boss-owned external**.

*(CORR1: G-10, G-11 and G-12 were dropped from the first version of this section, which was headed
"carried". A register that says "carried" and carries 9 of 12 is a false assurance about the other
three. G-10 bears directly on `SA09`'s reversal row; G-11 on `SA07` AR-20, `SA15` E2E-14 and
`SA17` priority 8.)*

`G-01` is the same root object this package records at `XD-06`, and the same one the Boss has
since ruled as `BD-ACC-01`. **The design position is closed; the eleven packages still carry it
as their gating dependency.** That gap between a settled ruling and unsettled packages is itself
a finding, and it belongs to Boss.

---

## 5. SA13-F-02 — a cross-programme reconciliation that was authorized, contracted, and never convened

Established by challenge search across all 183 branches:

- a **16-element Inventory → Accounting Minimum Handoff Data Contract** exists and is
  `BOSS APPROVED / EFFECTIVE`;
- a **22-scenario joint cross-proof baseline** is Boss-approved;
- a joint session agenda exists with eleven topics;
- the execution record states, verbatim: **"no session has yet occurred"**, and every agenda
  topic reads `PENDING JOINT SESSION 3`;
- a Boss directive gates the joint work behind full accounting-core closure;
- the joint closure branch is recorded as **a governance container only — four files, no closure
  deliverable**.

Measured cross-reference between the two programmes: across the eleven Account package roots,
content search for the Group A programme returns **0 files in ten of eleven roots**, and in the
eleventh a **single** Layer 1 line, itself `HOLD — STATUTORY EVIDENCE REQUIRED`. A positive
control on the same command shape fires in every root.

**This is `SA00-F-03` confirmed by a second, independent instrument** — a different searcher,
different patterns, different unit — and extended: the reconciliation was not merely omitted, it
was **formally constituted and then never held.**

---

## 6. Challenge classes executed

| Class | Result |
|---|---|
| Arithmetic and counting | 2 author defects found (`CH-05`, `CH-07`), corrected |
| Citation integrity | 1 author defect found (`CH-01`), corrected by population |
| Unsupported negatives | Author negatives re-tested with declared patterns and firing controls; one narrowed (`CH-03`) |
| Status-field fidelity | Statuses re-quoted verbatim from source; no promotion of another party's open item found in this package |
| Evidence-base completeness | 1 **material** author defect (`CH-08`) — an artefact on the author's own branch was not consumed |
| Governance / verdict wording | `SA13-F-01` — prohibited verdict wording in the authorizing gate |
| Cross-programme reconciliation | `SA13-F-02` — constituted, never convened |
| Independence of the challenge itself | **Does not satisfy the programme's standard** — §1 |

An adversarial challenge of this package's internal consistency was commissioned and its
findings are carried into `SA18`.

---

`SA13 — HOLD`. Challenge executed and reported, including eight defects in the author's own
work. The challenge is internal, not independent, and says so.

Boss remains the sole Final Approver.
