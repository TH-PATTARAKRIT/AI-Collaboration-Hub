# 73 — P11 SUPPLEMENT: RUNTIME INVERSION

**LAYER 1 — CLEAN ROOM.** No vendor model, field, path, module or internal database name.

> **SUPPLEMENT TO THE PRIOR P03 HANDOFF — NOT A REPLACEMENT.**
> The prior handoff (`24`) stands. This adds what runtime evidence changed.

---

## 1. What changed since the prior handoff

Four deployed databases were read, read-only. Previously three were readable; the fourth was
opened this round with tooling already present on the host. **Opening it overturned three
prior conclusions and confirmed a fourth.**

## 2. The deployed picture

| | Production-scale database | Test database |
|---|---|---|
| Completed manufacturing orders | **9,807** | 8 |
| Work centres | **none** | 60 |
| Routing operations / work orders / time records | **none** | 154 / 204 / 27 |
| Inventory valuation records | 74,982 | **none** |
| General-ledger lines | 447,384 | **32** |
| Valuation mode | automated | manual |

> **The two things conversion cost needs — resources carrying a rate, and automated
> valuation — have never existed together in any examined deployment.** One database has the
> valuation and no resources; the other has the resources and no valuation.

## 3. The two live failures

**A — cost is never created.** Finished goods carry the cost of their materials and nothing
else. Not merely missing overhead: missing labour and machine cost entirely. Additionally
**49 completed production receipts carry no valuation record at all** and 280 more are
valued at zero; on the input side 1,386 component consumptions are unvalued.

**B — cost is created and is absurd.** Thirty inventory-valuation records carry values up to
**±1.5 × 10²¹**. They distort total inventory valuation by **−48.7 %**.

- The general ledger is **balanced and sane** and contains none of these amounts.
- **25 of them name a journal entry that exists and carries a completely different amount —
  25 mismatched, 0 matched.** The inventory subsidiary ledger and the general ledger have
  **diverged**.
- Origin: a **goods-receipt and vendor-bill revaluation** on an average-costed raw material
  — unit cost jumping from ~31 to 712,186 in one receipt, then compounding daily to 10¹⁶
  while ordinary receipts at ~30 continued alongside.
- **Manufacturing did not cause it.** Manufacturing **amplified** it: 18 of the 30 corrupt
  records are production-origin, 12 of them from dismantling completed output.

## 4. The property that governs remediation

The thirty corrupt records **nearly cancel**: gross exposure near 10²¹, residual −195
million.

> **Any partial correction — reversing one dismantling, revaluing one product, deleting one
> entry — breaks the cancellation and releases an error of astronomical size into the
> ledger.**

The position is not "wrong by 195 million". It is "wrong by 10²¹ in both directions,
currently almost cancelling". **Remediation sequencing is a decision, not a task**, and it
is above P03.

## 5. Exposure classification

Fifteen material defects: **1 live, 11 latent, 3 unreachable in the verified deployments.**

The eleven are latent **because the system is unconfigured, not because it is controlled**:
59 of 60 resources carry no rate, 60 of 60 carry no absorption account, none carries a cost
allocation, and automated valuation is off. Each is a field an installation is expected to
complete.

> **A costing model whose safety property is "nobody has finished configuring it" has no
> safety property.**

## 6. Decisions this supplement puts to P11

| # | Decision | Why it is P11's |
|---|---|---|
| `P11-D-4` | **Which ledger is authoritative** where the inventory subsidiary ledger and the general ledger disagree, and how divergence is detected | Cross-process; neither P03 nor the inventory track may set it |
| `P11-D-5` | **Remediation sequencing** for a corrupt position that currently self-cancels | Any single-process fix breaks the cancellation |
| `P11-D-6` | Whether a defect with **zero measured incidence** but a permitted mechanism can be closed | The general form of the scope question already open; recurs for every latent defect |
| `P11-D-2` | *(carried forward)* what closes a scope defect whose evidence returns an empty population | unchanged |
| `P11-D-1` | *(carried forward)* whether a scope narrowing for one object reads across to a related object | unchanged; P03's dissent preserved |

## 7. What P03 does **not** conclude

- **Not** that the reference product's defects are harmless because they are latent.
- **Not** that SMEsPlus may omit labour, machine cost, depreciation or overhead because a
  deployed system does. The accounting requirement is unaffected by what an operator
  configured.
- **Not** that material-only costing was an error rather than a policy. **No evidence of
  intent exists and none is inferred.**
- **Not** any statutory determination. Those are routed, unchanged.

## 8. Status

Prior blockers closed: **none.** Gates closed: **none.** Nothing merged, frozen, approved or
authorised for implementation. The standing costing veto is **strengthened**.
