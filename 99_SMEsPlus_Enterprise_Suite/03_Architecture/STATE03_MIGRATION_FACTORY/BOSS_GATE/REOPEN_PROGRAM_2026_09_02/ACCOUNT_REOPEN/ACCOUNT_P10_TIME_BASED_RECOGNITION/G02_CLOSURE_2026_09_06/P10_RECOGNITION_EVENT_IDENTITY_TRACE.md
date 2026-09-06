# P10 — RECOGNITION EVENT IDENTITY TRACE  (`CQ-P10-01`)

**Terminal disposition: `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for the reference behaviour · **`BOSS DECISION REQUIRED`** for the SMEsPlus canonical identity, which is owned by `D-5` and not by P10.

---

## 1. The Question

Does time-based recognition have an explicit durable event identity, or does it collapse identity into posting, document, date and state?

## 2. Answer — anchoring is **graduated**, not binary

The prior round's first answer ("three of eight have no anchor") was arithmetically wrong on its own table and was corrected under challenge. The verified position:

| Mechanism | What a generated entry resolves to | Grade |
|---|---|---|
| Loan amortisation | **the individual schedule line**, by an indexed reference with a deletion rule | **line-level — the strongest in the reference** |
| Asset depreciation | the asset object **and** a stored period-beginning date, written at two sites and read at eight | **object + period** |
| Deferral, validation path | the **source move**, set on every generated entry | **move-set level** |
| Deferral, grouped path | the **set** of source moves, accumulated, stored, and written as a full cross-product against both generated entries | **move-set level** |
| Accrual | **nothing.** Transient wizard; the collection meant to link back to the order is initialised empty and never appended to | **none** |

**Of the five, only the accrual has no anchor at all.** Three of the four re-verified anchor cells came back different from P10's first draft — that correction is preserved, not overwritten.

## 3. What Is Genuinely Absent

What *is* missing, precisely, and it is narrower than "no identity":

| Element | Present? |
|---|---|
| A reference from the entry back to **something** | yes, in four of five |
| A reference to the **source line**, not just the source document | **no**, for deferrals |
| The recognition **period** as a stored attribute of the entry | **no** for deferrals; **yes** for depreciation |
| The **period start** | **no** — only the period end reaches the entry, as its date |
| A durable **event** object distinct from the entry | **no**, in any mechanism |
| An accounting-event object anywhere in the reference root | **no** — executed search, 0 against a positive control of 216 |

> **The collapse is real but narrow: what collapses is the *period*, not the *identity*.** A deferral entry knows which document it came from and does not know which period it belongs to, because its only period carrier is the field the posting layer will overwrite.

**This scoping is itself a correction.** The claim "the recognition event is collapsed into the posting act" holds for the two deferral paths and the accrual; it does **not** hold for depreciation or the loan, both of which carry a period independently of their posting date.

## 4. Duplicate Prevention, Idempotence, Replay

| Mechanism | Duplicate control | Keyed on | Defeated by |
|---|---|---|---|
| Deferral, validation | source-document state | the document's lifecycle | reset-and-repost is handled; the *other* path is the exposure |
| Deferral, grouped | a **date-and-state proxy** plus a cumulative self-correcting model plus a conflict-tolerant relation write | `(source move, period-end date, acceptable state)` | an entry left **draft with a past date**; an unkeyed result cache shared across report types and periods |
| Accrual | **none of any kind** | — | repeat execution reproduces identical entries; exposure bounded to the accrual-to-reversal interval, and that bound is an **operator-editable field** |
| Depreciation | posted entries are never rewritten; only draft board entries are replaced | asset state | the pause/resume/revaluation/disposal paths — **class `C`, not searched** |
| Loan | none inside the confirmation path | — | re-entrant confirmation; a teardown path that orphans posted entries; an off-by-one against its own documented boundary |

**Idempotence is achieved nowhere by identity.** Where it is achieved it is achieved by *state* (a document's lifecycle) or by *cumulative arithmetic* (the grouped path recomputes the whole position each run, so a skipped period self-heals). Both are proxies.

**Replay:** no mechanism supports replaying a recognition event. The grouped path's cumulative model is the closest thing to it and is the only one that survives a missed period without manual intervention.

## 5. Correction Implications

Because the event has no identity distinct from its entry, a correction cannot address *the event*. It must address *the entries*, and the reference decides per entry — unlink, cancel, or reverse — with the **cancel branch unreachable** (reaching it requires one expression to be simultaneously true and false). So with the audit trail enabled a previously-posted recognition entry is **always reversed**, and the intended middle ground does not exist.

Consequence: **one contract's twelve periods can be resolved by two different mechanisms, and nothing records that they were.**

## 6. Convergence With P02 — reached independently

P02's design-candidate list, produced without reading P10 this round, contains **event identity** and a **two-date model**. P10 reached both from the recognition side; P02 reached them from the order-to-cash side. **Two processes, disjoint evidence, same two candidates.**

P02 also records that the invariant *one business fact → one canonical event owner → one accounting effect path* is **not satisfied by the reference at the correction/reversal stage** — which is exactly §5 above, observed from the other end.

## 7. What P10 Does Not Decide

The accounting-event object belongs to **`D-5`** — *introduce a layer-3 event object, or not* — a Boss decision already named by P11. **P10 withdrew its proposal to author a competing identity** and attaches an acceptance condition instead:

> **`AASP-COND-01`** — P10's acceptance of an accounting-event object is conditional on that object satisfying the **graduated anchor grades** in §2, carrying a **period independently of the posting date**, and **excluding point-in-time estimates** from the recognition abstraction rather than modelling them as degenerate schedules.

## 8. Disposition

- Reference behaviour: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**, bounded to the declared root and to the four databases in which the mechanism has **never executed**.
- SMEsPlus canonical identity: **`BOSS DECISION REQUIRED`** — `D-5`, owner P11/Boss. Handoff published.

---

## RE-STATEMENT REQUIRED BY A PEER, PERFORMED — `G02-R-01` (second instance)

The ledger peer withdrew, as **contradicted**, the claim that no accounting-event object exists across
the declared root set — and recorded, in a row addressed to P10 by name, that P10 had *"adopted the
claim and relocated its central design element on it"*, that P10's conclusion *"largely survives on the
corrected fact… but now rests on different and weaker ground and **must be re-stated**"*. P10's closure
round consumed the pre-correction version and performed no re-statement. Performed here.

> **Re-stated.** P10's conclusion — *do not author a competing identity in this layer; the identity
> decision is `D-5` and it is Boss-reserved* — **stands**, and its ground is now narrower. It rests on
> P10's **own** search of the declared reference root, which returns no accounting-event model against
> a firing positive control: **class `A` within one root**. It does **not** rest on the peer's
> withdrawn universal claim over the whole root set, whose correctly-scoped successor is
> **`UNTESTED across the root set`**. A per-channel key populated nowhere is still not a platform
> identity — but that is a weaker premise than the one P10 relied on, and the difference is recorded
> rather than absorbed.

## ANCHOR GRADES QUALIFIED — `G02-R-07`

The grading above records that the deferral entry references its source in four of five mechanisms.
Two qualifications, both verified at source and neither held by P10 when the grading was written:

1. **The move-set anchor is load-bearing and silently erasable.** The grouped path's duplicate filter
   reads the source-link relation. Deleting a deferral entry **clears that relation on every original
   document**, not only the link to the entry deleted — so deleting one entry **re-arms duplicate
   generation for every document grouped with it**. A weak reference nothing depends on would be safer
   than a strong one that can be wiped.
2. **The anchor is at the wrong granularity.** The unit of work is the item; the unit of exclusion is
   the document. A document with a second deferrable item picked up later is thereafter excluded
   whole, and the never-deferred sibling becomes permanently unreachable by the generator, unreported.

> **Consequence for the design question.** A document-set anchor supports **neither idempotence, nor
> replay, nor correction**: idempotence breaks at the wrong granularity; replay is impossible because
> the anchor points at the source rather than the event and the period is not stored; and correction
> cannot say *which of the twelve* it corrects, because the link carries no per-link payload.
