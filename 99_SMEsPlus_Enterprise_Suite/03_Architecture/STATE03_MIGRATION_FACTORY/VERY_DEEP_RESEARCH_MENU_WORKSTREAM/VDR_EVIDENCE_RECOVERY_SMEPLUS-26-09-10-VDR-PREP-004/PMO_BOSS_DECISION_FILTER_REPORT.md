# PMO_BOSS_DECISION_FILTER_REPORT.md
# Every proposed Boss decision, filtered — and most of them sent back

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 14.

---

## 1. The test applied

§15 admits a proposed decision to the Boss **only** when all six hold:

1. factual evidence is complete · 2. technical analysis is complete · 3. independent challenge is
complete · 4. alternatives remain legitimately open · 5. the remaining choice is governance, business
or architecture policy · 6. **no further evidence can objectively decide it**.

Anything else is **TEAM RESPONSIBILITY MISROUTED TO BOSS**, and is removed and returned.

## 2. The inherited list — six proposed decisions from PREP-003

| # | Proposed to the Boss in PREP-003 | Verdict | Disposition |
|---|----------------------------------|---------|-------------|
| 1 | *"Accept the HOLD, or direct otherwise."* | **TRUE BOSS DECISION** | **retained** — governance approval, criterion 5 |
| 2 | *"`BOSS-DEC-10` — is stop-at-one-hop the universal boundary rule?"* | **SPLIT** | see §3 |
| 3 | *"`BOSS-DEC-01` — must the valuation conclusions be re-derived?"* | **MISROUTED** | **REMOVED.** §2 lists *"Should this conclusion be re-derived?"* verbatim as forbidden. **It was re-derived this round** — the answer is in the revalidation report, and it overturned the explanation the prior round had accepted |
| 4 | *"Tenant isolation — accept design without reference, or seek another reference?"* | **SPLIT** | see §3 |
| 5 | *"Evidence base — authorise examination of the discovered databases, or bound it."* | **MISROUTED** | **REMOVED.** §5 forbids it explicitly. **All were examined and classified**; not one is a target-generation deployment |
| 6 | *"Next round scope."* | **MISROUTED** | **REMOVED.** Scoping follows from the measurement; the measurement now names the three weakest dimensions itself |

**Four of six removed. Two split. One retained unchanged.**

## 3. The two split decisions — the team half done, the policy half retained

### `BOSS-DEC-10` — the boundary rule

| Half | Owner | State |
|------|-------|-------|
| *What would a second hop cost, and is the current boundary even complete at hop 1?* | **TEAM** | **MEASURED THIS ROUND** — see below. It was never measured in three prior rounds; it took one query against the deployment's own field registry |
| *Is one-hop adopted as the universal standard for every future subject?* | **BOSS** | **TRUE** — this is a programme-wide method policy, and it stays open even after the measurement above, because it trades research cost against boundary completeness for domains not yet studied |

**The measurement, from the deployment's own field registry — the authority on what actually relates to
what at runtime:**

| Boundary | Objects | Multiple of the owned set |
|----------|--------:|--------------------------:|
| owned objects (current population) | **96** | 1.0× |
| hop 1 — directly related to an owned object | 83, of which **39 already carried** and **44 not** | — |
| **extending the boundary to hop 2** | **+132 further objects → 272 total** | **2.8×** |
| full relational closure | 369 objects, depth 6 | 3.8× |

**Two results, and the second was not expected:**

1. **Hop 2 costs 2.8×.** The one-hop rule is doing real work; the alternative is not a marginal widening.
2. **The boundary is not even complete at hop 1 under a second, equally defensible edge definition.**
   **44 objects directly related to an owned object are not carried** — including a withholding-tax
   object, a fiscal-position object, a price-list object and a payment-method-line object, all of which
   are financially material. Conversely **51 carried boundary objects are not outbound-related** to any
   owned object; they were derived by a different edge direction. The two definitions overlap on 39.

> **This is a finding about the current denominator, not only about a future one.** It was found by
> measuring the question rather than referring it, and it is the strongest single argument that
> `BOSS-DEC-10` could not have been decided at the time it was proposed: **criterion 1 — factual
> evidence complete — was not met, and nobody had checked.**

**`BOSS-DEC-10` is REMOVED from this round's Boss list.** The team half is now measured; the remaining
work is to settle the edge definition and reconcile the 44 and the 51, which is a bounded team task.
The universal-standard half is re-proposed to the Boss only after that reconciliation, when the cost of
each option is known for a boundary that is itself complete.

### Tenant isolation

| Half | Owner | State |
|------|-------|-------|
| *Does the reference system have a tenant concept?* | **TEAM** | **ANSWERED: no.** A census over the whole frozen population found no element whose subject is a tenant boundary. This is a determined absence, evidenced |
| *Does SMEsPlus accept a multi-tenant design derived with no reference population, and at what evidenced residual risk?* | **BOSS** | **TRUE BOSS DECISION** — criterion 6 is satisfied: no further evidence can decide it, because the evidence that would decide it does not exist anywhere in the reference system |

### `CRITICAL-GAP-03` and `CRITICAL-GAP-04` — promoted, not inherited

Both were **CLOSED as research items** this round. What remains in each is a policy choice with the
facts complete:

- **`-03`**: does SMEsPlus permit role-dependent default filtering on audit-relevant screens? The mechanism is fully characterised — a visible, removable facet, not a silent injection.
- **`-04`**: does SMEsPlus adopt the prohibition *no transactional record without an owning scope*? The reference system admits 16 rules that permit company-less transactional records; the measurement is complete and the response is a design act.

**These satisfy all six criteria and are the only two new items admitted to the Boss list.**

## 4. Items the team took back this round, with what was actually done

| Question previously routed upward | What the team did instead |
|-----------------------------------|---------------------------|
| Should the discovered databases be examined? | **Examined all of them.** Generation read from each deployment's own module record. **None is a target-generation deployment**; the lab that appeared able to run the missing counterfactual is the wrong generation *and* holds no movement data |
| Should the valuation conclusion be re-derived? | **Re-derived.** The unreconciled 3,680-vs-14,441 denominator is **resolved** — both figures were right and one column heading was wrong. The *"every current-generation deployment runs periodic"* premise is **false**: the transacted deployment is configured perpetual on 27 of 37 categories |
| Is this evidence sufficient? | Replaced with a **grade**: element-observed, indirect, or module-level — published per class, with the weaker never reported as the stronger |
| Is this runtime path reachable? | **Measured.** 2,854 of 3,319 element-observable items observed on real deployments |
| Does this configuration change behaviour? | **Measured at the presence axis across five deployments.** Gate presence is **necessary but not sufficient**: 4 gates are present where their gated elements are absent; **0 gates are absent where their elements are present** |
| Does prior research remain valid? | **Classified by evidence** — two VALID, one VALID WITH DELTA, one SUPERSEDED, two CONTRADICTED |

## 5. The filtered Boss decision list

| # | Decision | Type | All six criteria met? |
|---|----------|------|----------------------|
| 1 | Accept the disposition, or direct otherwise | governance | **yes** |
| 2 | Multi-tenant design with no reference population — accept the evidenced residual risk, or direct another course | architecture policy | **yes** — criterion 6 satisfied by a determined absence |
| 3 | Role-dependent default filtering on audit screens — permit or prohibit in SMEsPlus | business policy | **yes** |
| 4 | Adopt *no transactional record without an owning scope* as a design prohibition | architecture policy | **yes** |
| 5 | A challenger's disclosed conduct — continuing a sweep after a stop signal | governance, non-technical | **yes** — the only item here that is not a research question at all |

**Five items. Not one is a technical fact, and not one is a question the team could have answered by
looking harder.**

## 6. PMO statement

**Filter result: 4 removed, 2 split with the team half returned, 3 admitted, 2 promoted from closed
research.** No unresolved technical matter is carried to the Boss in this package.

The removals are not a courtesy. Each was removed because the team had not finished, and in four cases
**the work has now been done and the answer changed the package** — most sharply in the valuation
re-derivation, where the explanation the prior round accepted turned out to be contradicted by the
deployment's own configuration records.
