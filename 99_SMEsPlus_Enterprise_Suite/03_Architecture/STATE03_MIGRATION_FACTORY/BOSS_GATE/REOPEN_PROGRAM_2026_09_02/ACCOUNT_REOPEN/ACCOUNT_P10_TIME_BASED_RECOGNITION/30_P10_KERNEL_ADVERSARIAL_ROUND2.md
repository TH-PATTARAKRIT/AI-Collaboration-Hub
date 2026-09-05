# P10 — SHARED KERNEL vs SEPARATE ENGINES — ADVERSARIAL ROUND 2

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1

The parent round recommended **Option B-minus**: one shared *semantic kernel* plus separate *domain engines*. This round re-tests that recommendation against the peer evidence that did not exist when it was written. The Boss's constraint stands: the decision may not be made on code-reuse convenience.

---

## 1. The Kernel's Six Elements, Re-tested

The parent kernel claimed six elements. Peer evidence has moved four of them.

| # | Kernel element as proposed | Status after reconciliation |
|---|---------------------------|------------------------------|
| 1 | The recognition event with identity | **REMOVED from P10's kernel.** `P08` owns the accounting-event object; P10 specialises it. Authoring it in P10 would create two identities for one fact (`27` §4) |
| 2 | The period grid, from the owning company's fiscal calendar | **BLOCKED.** The ledger has no period object; a period is a date range (`25` §2). The grid cannot be a kernel service until `P08` provides the concept |
| 3 | The allocation convention library | **STANDS.** Nothing in peer evidence touches it. Still the clearest kernel-shaped element |
| 4 | The correction algebra | **STANDS, and strengthened.** `29` §3 shows four mechanisms with four different correction behaviours, two of which are demonstrably wrong under a lock. Nothing in the peer packages contradicts the case for unifying it |
| 5 | Scope resolution | **PARTLY RELOCATED.** `P09`'s `MA-11` and `P11`'s `SCP-08`/`SCP-09` are programme-wide positions, not P10 inventions. P10 adopts them rather than owning them |
| 6 | Separation of recognition period from posting act | **RELOCATED to `P08`** as obligations `OB-02` and `OB-03` |

**Two of six stand as P10-owned. Two are relocated. One is blocked. One is adopted from elsewhere.**

## 2. The Adversarial Case — the kernel's strongest arguments have been taken from it

The parent round rested the kernel case on six criteria and found three of them decisive: auditability, correction behaviour, period-close behaviour. Reconciliation has removed two of the three.

- **Auditability** was the strongest argument. It rested on the kernel owning the event identity. It now depends entirely on an object `P08` has not authored and that is a named Boss decision. **A kernel cannot be justified by a capability it does not own.**
- **Period-close behaviour** was the second. `24` §6 establishes that the silent re-date is produced by the shared posting layer, **below the kernel line**. A recognition kernel spanning the mechanisms would not have prevented it and would not fix it.
- **Correction behaviour** survives intact and is now the strongest surviving argument.

So the honest re-statement is:

> **The kernel case is materially weaker after reconciliation than before it.** Two of its three decisive arguments belong to another process. What remains is a convention library and a correction algebra — real, but a smaller thing than "a semantic kernel".

## 3. The Counter-Case — what reconciliation added in the kernel's favour

Argued as strongly as the case against:

1. **The defect class transferred.** `P10-F-38` was found by taking a defect verified in the asset mechanism and testing whether the deferral mechanism had it. It did. That is exactly the leverage a shared kernel provides: a defect found once is a defect found everywhere. Under separate engines it had to be found twice, by two processes, by accident of a cross-process round.
2. **Four independent agreements** (`24` §2) show the mechanisms failing in the *same shapes* despite sharing no code. Independent re-implementation did not produce independent failure modes; it produced identical ones, four times.
3. **Three processes are blocked on one undefined object.** That is an argument for shared semantics at the programme level, even though the object in question belongs to `P08`.
4. **The correction algebra argument got stronger, not weaker.** `29` §3 now shows four mechanisms, four correction behaviours, and two of them wrong under exactly the condition the close produces.

## 4. Where This Leaves the Recommendation

| Option | Status after round 2 |
|--------|----------------------|
| **A — separate domain engines** | Strengthened. The reconciliation showed the two most valuable shared elements are not P10's to share |
| **B — one generalised kernel** | Weakened further. It would now have to reach into `P08`'s layer to deliver its main benefits |
| **B-minus — shared semantic kernel + separate engines** | **Narrowed, not withdrawn.** Its scope shrinks to the allocation convention library and the correction algebra, sitting above `P08`'s accounting-event object and below the domain engines |

**P10's recommendation, restated and reduced:**

> A **thin** shared recognition layer owning exactly two things — the allocation convention library and the correction algebra — specialising `P08`'s accounting-event object, with separate domain engines owning objects, lifecycles, posting patterns and business rules.

This is a smaller claim than the parent round made, and it is smaller **because of evidence, not because of caution**. It is still a recommendation. The Boss decides.

## 5. The Condition That Governs Everything

None of A, B or B-minus can be specified until `D-5` — the accounting-event identity — is taken. Every option's shape depends on whether a shared event object exists to specialise.

**P10 therefore records that `P10-D-01` is not independently decidable and must be sequenced after `D-5`.** That is a change from the parent round, which presented `P10-D-01` as ready for decision. Recorded in `35` §5 and `36`.

## 6. What Would Falsify This Position

Stated so a later round can test it:
1. If `P08` authors an accounting-event object that already carries an allocation policy and a correction algebra, the thin recognition layer has nothing left and Option A wins outright.
2. If the correction algebra proves genuinely domain-specific — if the three named strategies cannot be expressed as one algebra with policies — the last surviving kernel argument fails.
3. If a fifth recognition domain appears whose anchor does not fit the taxonomy in `27` §2, the shared abstraction is not general and should not be built.

None of the three has been tested. All three are testable.
