# SA_CORR3_10 — STRUCTURAL INDEPENDENCE STATUS
## CP-SA-C3-90 — STRUCTURAL INDEPENDENCE STATUS VERIFIED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR3-PROOF-001]`
Branch: `architecture/phase-sa-corr3-proof-verification-2026-09-09-001`
Master prompt commit: `5953ce26`
Boss: **SOLE FINAL APPROVER**

---

## 1. The headline, and it corrects the parent

CORR2's Boss pack listed as **blocker 7**:

> *"**No structurally independent challenge exists.** `PHASE-S/Q-BOSS-02` open | Owner: **Boss** |
> Can research close it? **No**"*

and `SA13` §1, carried into `SA19` and `SA_CORR2_11`, states:

> *"`PHASE-S/Q-BOSS-02` — who may act as an eligible challenger — is **raised and unanswered**."*

### `C3-IND-01` — **`PHASE-S/Q-BOSS-02` is not open. It was APPROVED on 2026-09-07.**

Primary text, read at source:

```
File   : .../PHASE_S_CLOSURE/BOSS_DECISION_PHASE_S_Q_BOSS_02_2026_09_07.md
Commit : 2930723fbd45d8c4dada26197963ad6285d6c502   (verified: git cat-file -t -> commit)
Date   : Mon Sep 7 09:08:26 2026 +0700
Subject: Record Boss decision PHASE-S Q-BOSS-02 structural independence authority
Status : **APPROVED — STRUCTURAL INDEPENDENCE AUTHORITY DEFINED**
```

The ruling answers precisely the question `SA13` describes as unanswered — *who may act as an
eligible challenger* — and answers it with **ten named controls**, not a gesture:

| # | Control (`Q-BOSS-02` §1, verbatim headings) |
|---|---|
| 1 | **Model / Agent Separation** — not the same model/agent that authored or executed the repair |
| 2 | **Appointment Independence** — appointed by Boss or an independent governance authority, **not selected by the correction owner** |
| 3 | **Evidence Isolation** — separate isolated session, frozen evidence surface, bounded `RC-*` scope |
| 4 | **Read-Only Boundary** — read-only on owner evidence; must not edit the owner's repair artifacts |
| 5 | **Independent Reproduction** — independently reproduces the tests, counts, predicates and conclusions |
| 6 | **Independent Publication** — publishes its own artifact, branch and immutable commit SHA |
| 7 | **No Owner Mutation** |
| 8 | **No Self-Discharge** — must not self-discharge any Veto |
| 9 | **No Self-Pass** — must not self-declare Phase S PASS, Gate closure, release, merge or production readiness |
| 10 | **Boss Final Authority** — Boss remains the sole Final Approver |

It further rules, verbatim: *"A different session alone is insufficient. A different model alone is
insufficient."* and *"Eligibility is determined **per repair / challenge pair**. No verifier is
presumed independent merely because it is a different session or model."*

### `C3-IND-02` — a verifier **is** appointed

```
File   : .../PHASE_S_CLOSURE/BOSS_DECISION_Q_BOSS_03_AND_INDEPENDENT_VERIFIER_APPOINTMENT_2026_09_07.md
Commit : 6cb99464c4a3b9065c7cd9ae5014c13a7d6968b7
§1     : "Boss appoints **ChatGPT GPT-5.6 Sol** as the structurally independent verifier/challenger
          for the current Phase S RC-01 through RC-06 verification programme"
Lineage: audit/account-phase-s-independent-gpt56sol-2026-09-07-002 @ 9a5699e
```

**So the programme has both an independence standard and an appointed independent party.** Two
Boss acts, two commits, both resolvable.

### Why the stale negative survived four rounds

`SA13` was written **2026-09-08**; the ruling it calls unanswered was issued **2026-09-07**. The
statement was true when first written in an earlier package and **was never re-tested when carried
forward**. It then propagated into `SA19`, `SA_CORR2_11` and CORR2's Boss pack as a live
Boss blocker.

> **The rule this pays for again:** a negative about a Boss decision's *status* must be re-read
> against the decision's own status field at its own commit, every round. A peer's summary of a
> ruling is not the ruling. **This is the same defect the programme has recorded before, committed
> against a document that a one-line `git cat-file` would have resolved.**

---

## 2. What is therefore genuinely open — and it is much narrower

| Question | Status |
|---|---|
| What satisfies structural independence? | **ANSWERED** — `Q-BOSS-02`, ten controls, `2930723` |
| Is a party appointed for the **Phase S RC programme**? | **YES** — ChatGPT GPT-5.6 Sol, `6cb9946` |
| Has that party executed the Phase S `RC-01`…`RC-06`? | **NO.** `0 PASS · 0 FAIL · 6 HOLD`. Its device was offline; it held all six lanes, and a later session found the hold **over-scoped** — `RC-02`/`RC-03`/`RC-04` need only a clone of the repository, no host at all |
| Is a party appointed for **Phase SA / this CORR3 package**? | **NO.** The appointment at `6cb9946` is scoped, in its own words, to *"the current Phase S `RC-01` through `RC-06` verification programme"* |

### `C3-IND-03` — the open item is an **appointment act**, not a research question

Nothing about Phase SA independence requires investigation. It requires Boss to extend or issue an
appointment covering this package. That is a one-line governance act, and CORR2 was right that
research cannot close it — but wrong about **what** is open and **how large** it is.

---

## 3. What was actually run in this round, and what each layer is worth

| Layer | Relationship to this author | Label | `Q-BOSS-02` controls satisfied |
|---|---|---|---|
| Seven parallel study/register executors | **Same model** (Claude Opus 5), same session lineage, briefed by the author, corpus supplied by the author | **`INTERNAL ADVERSARIAL SELF-CHALLENGE`** | 3, 4, 7 only. **Fails 1 and 2 — decisively** |
| The author's own re-measurement of every inherited claim | self | **`SELF-VERIFICATION`** | fails 1, 2, 5 |
| Cross-reading between the seven executors | same model | **`INTERNAL ADVERSARIAL SELF-CHALLENGE`** | fails 1, 2 |

**Control 2 is the one that cannot be engineered around in this session.** The executors were
selected, scoped, briefed and read by the correction owner. `Q-BOSS-02` §1 control 2 exists
precisely to forbid that arrangement from counting as independence, and it does not count here.

**No independence claim is made anywhere in this package.** Every internal challenge layer is
labelled at the point of use.

### 3.1 Why a different Claude model was not used to manufacture control 1

A different Anthropic model was available and was **deliberately not used** to claim control 1.
`Q-BOSS-02` §1 rules *"A different model alone is insufficient"* and requires **all ten controls
together**. Swapping the model would satisfy control 1 while control 2 still failed, and would
produce an artifact that *looks* independent. **That is the failure mode `Q-BOSS-02` §5 names —
inference of assurance from the shape of the evidence — and it is avoided deliberately, which is a
decision and not an omission.**

---

## 4. Terminal independence status

> # `EXTERNAL INDEPENDENT CHALLENGE — PENDING STRUCTURALLY INDEPENDENT REVIEW`

with the exact basis, which differs from CORR2's:

- the **standard** exists and is approved (`Q-BOSS-02`, ten controls);
- an **appointed verifier** exists for the adjacent Phase S programme (`Q-BOSS-03`);
- **no appointment covers this Phase SA package**, and this session may not select its own — control 2;
- this package is **frozen and handover-ready** so that an appointed challenger can execute without
  re-deriving anything (§5).

**No independence is fabricated. No veto is discharged. No `RC-*` result is asserted or implied.**

---

## 5. Handover package for an eligible challenger

Prepared so the challenge can be executed without inheriting the author's framing — which is the
defect `ND-12` recorded, where *"the corpus frame defect survived a full internal challenge … because
every reviewer inherited the author's corpus."*

| Item | Value |
|---|---|
| Branch | `architecture/phase-sa-corr3-proof-verification-2026-09-09-001` |
| Frozen at | the publication commit recorded in `PHASE_SA_CORR3_AUTO_RESUME_STATE.md` |
| Integrity | `PACKAGE_MANIFEST_SHA256.txt`, verifiable with `shasum -a 256 -c` |
| Evidence frame | `SA_CORR3_00` §2 — **and the challenger is asked NOT to inherit it.** Rebuild the PATH SET independently; `C3-I-01` was found only by refusing to inherit the parent's |
| The three claims to attack first | `SA_CORR3_05` §8, `SA_CORR3_00` §6, and §1 of this register |

### 5.1 What a challenger should attack in **this** register first

1. **`C3-IND-01` rests on a status field.** The ruling says `APPROVED`. A challenger should test
   whether any **later** Boss act reopened, narrowed or superseded `Q-BOSS-02` — the search
   performed here was over the identifier `Q-BOSS-02` across 3,900 blobs, and a supersession
   phrased without that identifier would have been missed.
2. **`C3-IND-03` asserts that no appointment covers Phase SA.** That is a negative. The pattern was
   the appointment document's own scope sentence; a second appointment elsewhere in the corpus,
   phrased differently, would not have been caught.

---

## 6. One adjacent verification, performed because it would otherwise be raised as a contradiction

Two records appear to conflict on whether Phase S is closed:

| Record | Date | States |
|---|---|---|
| `PHASE_S_FAST_IV_2026_09_08/11_…EVIDENCE_PACK.md` | committed **2026-09-08 09:45** `53fd951b` | *"**`PHASE S` — NOT CLOSED**"*, `CP-SC-14` **NOT REACHED**, closure criteria TRUE **4 of 10** |
| `.../BOSS_CLOSURE_AND_PHASE_SA_ENTRY_2026_09_08/04_PHASE_S_CONDITIONAL_CLOSURE_AND_PHASE_SA_ENTRY.md` | committed **2026-09-08 21:10** `eb3d7dbb` | *"**ACCOUNT PHASE S — CONDITIONALLY CLOSED**"*, *"**ACCOUNT PHASE SA — AUTHORIZED TO START**"*, terminal `CP-SC-15` |

**`C3-IND-04` — not a contradiction; a sequence, and the Boss act is later.** The first is a
technical session reporting the state of the `RC` programme within its own scope. The second is a
**Boss act** (*"Authority: Boss — Sole Final Approver"*), issued **11 hours 25 minutes later**, and
after the parent independent gate `be5d1595` (**20:19**) that it cites. It states that the
carry-forward conditions *"do not block Phase SA entry unless a material delta proves otherwise"*.

**Phase SA entry authority is valid.** This is recorded because a challenger reading the two
documents without their commit times would reasonably allege that Phase SA was entered over an
open Phase S, and the answer should be in the package rather than discovered adversarially.

### 6.1 Two consequences of that Boss act, carried into this round

1. It lists rulings that are **"now Boss-approved and must not be re-asked without material delta"**
   — including **`BD-ACC-03A`** and **`BD-ACC-03B`**. Any CORR3 escalation touching category-level
   valuation or costing must therefore first prove a **material delta**, not merely an ambiguity.
   This is applied in `SA_CORR3_02`.
2. It sets a **clean-room acceptance gate for Phase SA**: every material function must demonstrate
   (1) learned facts and semantics, (2) what was **not** inherited from reference systems,
   (3) alternatives considered, (4) SMEsPlus-specific rationale, (5) Tenant/Company/control/audit
   boundaries, (6) what SMEsPlus does better or differently, (7) whether further Very Deep Research
   is required. **The four targeted studies in this round are scored against these seven criteria in
   `SA_CORR3_12` §3.**

---

## 7. Checkpoint

# `CP-SA-C3-90 — STRUCTURAL INDEPENDENCE STATUS VERIFIED`

`CLOSED (execution status)`. Checkpoint completion is **NOT** Boss approval.

| | |
|---|---|
| Independence claimed by this package | **none** |
| Internal challenge layers, all labelled | 7 executors + author self-verification |
| `Q-BOSS-02` controls satisfied by any layer used | **3, 4, 7** of 10; **1 and 2 fail** |
| Vetoes discharged | **0** |
| `RC-*` results asserted | **0** |
| Findings raised | `C3-IND-01` … `C3-IND-04` |
