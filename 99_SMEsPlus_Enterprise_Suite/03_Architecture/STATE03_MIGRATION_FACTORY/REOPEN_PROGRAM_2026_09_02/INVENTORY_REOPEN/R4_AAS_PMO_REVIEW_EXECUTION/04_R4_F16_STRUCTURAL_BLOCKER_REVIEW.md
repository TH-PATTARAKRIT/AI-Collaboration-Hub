# [SMEPLUS-26-09-04-INV-R4-AAS-PMO-REVIEW-001]
# 04 — `R4-F-16` Structural Blocker Review

Control Level: `/L9999.9999`
Status: `R4-F-16 CONCLUSION CONFIRMED — SUPPORTING REASONING REFINED ON ONE ELEMENT — THE THREE BLOCKERS ARE NOT EQUALLY LOAD-BEARING`

---

## 1. Why This File Exists

`R4-F-16` is the finding R4 asks Boss to read first, and PMO's first recommendation follows directly from it. It is an **inference from a Boss-approved control**, not an observation. An inference is reviewable in a way an observation is not: the reviewer can read the same control and re-derive it.

This review read the Minimum Handoff Data Contract at commit `d9e845e` and the 22-Scenario Cross-Proof Baseline at commit `296b495` **in full and at source**, and re-derived the finding independently rather than accepting R4's reading of them.

---

## 2. What `R4-F-16` Claims

> The contract requires sixteen elements per material handoff. Inventory can supply eleven. Two are blocked by the Accounting COGS Gap. **Three cannot be supplied because the underlying capability does not exist** — element 15 (deterministic idempotency identity, `RISK-C02`), element 14 (migration or replay batch identity, `GAP-FS-08`), element 10 (company and tenant context as a guarantee, `RISK-U03`). None of the three is caused by the COGS Gap. Therefore no material handoff can be declared verified and **0 of the 22 Boss-approved cross-proof scenarios can be proven, even if `JT-01` through `JT-12` were all resolved tomorrow.**

---

## 3. Re-Derivation Against The Contract As Written

### 3.1 The enforcement rule

Contract §4 states that a scenario may not be declared verified if any **material required** handoff element is missing, ambiguous, unsupported, contradictory, dependent on an unapproved assumption, unable to link reversal to original, *"unable to prevent duplicate/replayed effects when idempotency is required"*, or *"missing company/tenant isolation context"*.

Contract §3 additionally states: *"If a field is not applicable, record `N/A` plus reason. If it is unknown or unsupported, record `HOLD / EVIDENCE REQUIRED`; do not infer or fabricate."*

That last sentence matters. The contract distinguishes **not applicable** from **missing**. An element that is `N/A` with a stated reason is not a defect. An element that is required and absent is.

### 3.2 Element-by-element test

| Element | Contract wording at §3 | Baseline wording at §3 (`296b495`) | Conditional? | Absent capability | Reach |
|---:|---|---|---|---|---|
| **10** — Company / Tenant | *"**mandatory** company and tenant context"* | *"tenant / company context"* — **no qualifier** | **NO — unconditional in both controls** | `RISK-U03` — invariant set does not exist | **Every material handoff, all 22 scenarios** |
| **15** — Idempotency identity | *"deterministic identity used to prevent duplicate processing/effect"* — no qualifier at §3 | *"idempotency / duplicate-protection identity"* — **no qualifier** | **Effectively no.** Only the §4 enforcement bullet adds *"when idempotency is required"* | `RISK-C02` — no stable identity exists | **Every handoff where a retry is possible; squarely and unavoidably scenario 22** |
| **14** — Migration / replay batch | *"migration/replay package or batch identity **where the handoff is created/replayed through migration or recovery**"* | *"migration / replay batch identity **where applicable**"* | **YES — explicitly conditional in both controls** | `GAP-FS-08` — provenance reference does not exist | **Migration, replay and recovery handoffs — scenarios 20, 21, and the certified opening balance** |

### 3.3 The refinement

R4 asserts at `16_PROCESS_HANDOFF_MAP.md` §3 that elements 10, 14 and 15 fail on **every single one** of the ten material Inventory-to-Accounting handoffs, and its table marks element 14 as failing on all ten — including live operational handoffs such as the receipt valuation fact and the cost-release fact on delivery.

**For element 14 that is asserted, not contract-grounded.** Both Boss controls scope element 14 conditionally, to handoffs created or replayed through migration or recovery. A live purchase receipt in a running system is not such a handoff. Under the contract's own §3 rule, element 14 on that handoff is `N/A` **with reason** — which is compliant — rather than missing.

R4's own emphasis is in fact consistent with the narrower reading: file `16` bolds element **14** only on the certified opening balance (`HO-24`), which is exactly the handoff where it is genuinely material. Its §3.1 justification quotes the contract for elements 10 and 15 and offers **no contractual quotation for element 14's universality**. The over-generalisation appears to be a drafting compression rather than a substantive misreading.

### 3.4 What the refinement does and does not change

| Claim | Status After Re-Derivation |
|---|---|
| **0 of 22 Boss-approved scenarios can be declared verified** | **CONFIRMED.** Element 10 is unconditional in both controls and its capability is absent. **Element 10 alone is sufficient to produce the 0-of-22 result.** The conclusion does not depend on element 14 at all |
| No material Inventory-to-Accounting handoff can be declared verified | **CONFIRMED**, on the same basis |
| The result holds even if `JT-01` .. `JT-12` were all resolved tomorrow | **CONFIRMED.** None of the three absent capabilities is a Joint decision, and none is caused by the COGS Gap |
| All three elements block all ten material handoffs | **REFINED.** Element 10 does. Element 15 does wherever a retry is possible, which in practice is everywhere and unarguably in scenario 22. **Element 14 does not** — it is contractually conditional and blocks migration, replay and recovery handoffs |
| Therefore three capabilities must be commissioned | **CONFIRMED — all three are still required.** Scenarios 20, 21 and the certified opening balance are Boss-approved mandatory scenarios, so element 14 must exist regardless. What changes is **sequence**, not scope |

Recorded as `REV-F-02`, severity `MATERIAL`, Lane A. It is a refinement of reasoning, **not** a challenge to the headline conclusion.

---

## 4. The Consequence Boss Should Take From The Refinement

R4 and PMO both present the three missing capabilities as a single undifferentiated commission. The contract does not treat them as equivalent, and neither should the work order.

**Ranked by contractual reach:**

| Rank | Capability | Standing Item | Contractual Reach | Why This Rank |
|---:|---|---|---|---|
| **1** | Inventory-side multi-tenant invariant set | `RISK-U03` / `GAP-FS-10` | **Unconditional. Blocks all 22 scenarios and all 10 material handoffs on its own** | The single highest-leverage missing artifact in the Inventory scope. It is also the precondition for all 8 L9 isolation proofs (`0 of 8`) and for `L14-01` traceability. Nothing else in the register unblocks as much |
| **2** | Deterministic movement attempt identity | `RISK-C02` / `IV-06` | Unconditional at §3 of both controls; qualified only by §4's *"when idempotency is required"* | Blocks scenario 22 unavoidably — a Boss-approved mandatory scenario whose subject matter *is* this capability. Also the root of `L15-01` paths and of `R4-F-17`. **Its severity classification is a live Boss decision (`C-02`)**, which is why it is ranked second rather than first: rank 1 needs no ruling to begin |
| **3** | Migration / replay provenance reference | `GAP-FS-08` / `CN-36` | **Conditional** — migration, replay and recovery handoffs | Blocks scenarios 20 and 21 and the certified opening balance, which prior evidence names the highest fabrication-risk point in the Inventory scope. Genuinely required — but it does not block the live operational handoffs, so it can be sequenced after ranks 1 and 2 without holding them up |

**This is the practical difference the refinement makes.** Rank 1 requires no Boss ruling to commission and unblocks the most. Rank 2 is entangled with the outstanding `C-02` severity ruling. Rank 3 is genuinely required but has the narrowest contractual reach and lands with the migration workstream rather than the core ledger design.

---

## 5. Are The Three Blockers Real, And Correctly Owned?

| Test | Result |
|---|---|
| Are the three absences real, or are they R4 restating old items? | **Real, and R4 concedes they are not new.** AAS+ Track 04 forced this correction and R4 accepted it: the three components have each been carried for multiple rounds. **What is new is their conjunction under a contract that did not exist when they were last argued** — and therefore the consequence. This review confirms the concession is correct and that the consequence is genuinely newly stateable |
| Are they caused by the Accounting COGS Gap? | **No — verified.** None of `RISK-U03`, `RISK-C02` or `GAP-FS-08` appears anywhere in the COGS dependency chain as a COGS-dependent item, and none is among the twelve Joint decisions. All three are Inventory-side or SaaS-Foundation-side absences |
| Is "Lane A" the correct ownership? | **Under R4's own vocabulary, yes.** Under the authorization's vocabulary, ranks 1 and 3 are **Lane A**, and rank 2 is **Lane A for the build and Lane D for the `C-02` severity ruling that gates it**. See `05` |
| Is the owner "Boss" correct? | **Yes for the commissioning decision.** These are unfunded work items, not technical unknowns. Nobody below Boss can commission them |
| Does the finding overstate itself anywhere? | **Once — element 14's universality.** Corrected at §3.3. No other overstatement found |

---

## 6. Is `R4-F-16` Material?

Yes, and this review regards it as the most consequential single finding in the Inventory reopen programme to date, for one reason that survives the refinement intact:

**It relocates the critical path.** The programme has recorded Inventory as waiting on Accounting across several rounds. That remains true. What `R4-F-16` establishes is that Inventory is **not only** waiting on Accounting, and that three of its own preconditions were never commissioned. Resolving the entire COGS Gap tomorrow would move the Inventory cross-proof result from 0 of 22 to 0 of 22.

That is a statement about programme sequencing, and it is arithmetic rather than argument. This review re-derived it from the Boss controls and reaches the same result.

---

## 7. Verdict

| Question From The Authorization | Answer |
|---|---|
| Is `R4-F-16` valid? | **Yes — independently re-derived from `d9e845e` and `296b495`** |
| Is it material? | **Yes — it relocates the programme critical path** |
| Are the three non-COGS structural blockers real? | **Yes — all three verified as real, current, and not COGS-caused** |
| Are they correctly owned? | **Yes**, with rank 2 carrying an additional Lane D dependency on the `C-02` ruling |
| Is `0 / 22 cross-proof scenarios verified` contractually correct? | **Yes — and it follows from element 10 alone, independently of the refinement at §3.3** |
| Any correction required? | **One — `REV-F-02`.** Element 14 is contractually conditional. The three capabilities are all required but are **not equally load-bearing**, and should be commissioned in the ranked order at §4 |

**`R4-F-16` STANDS. NOT CLOSED BY THIS REVIEW.**

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
