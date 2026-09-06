# P10 — CORRECTION / REVERSAL / CANCELLATION ALGEBRA  (`CQ-P10-07`)

**Terminal disposition: `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for the reference algebra · **`DESIGN CANDIDATE`** for the SMEsPlus algebra.

---

## 1. The Reference Has No Algebra — it has four behaviours

| | Deferral, validation | Deferral, grouped | Asset | Loan |
|---|---|---|---|---|
| In-flight amendment | **none** — only teardown of the source document | n/a — regenerated each run | pause, resume, revalue, change duration, dispose | reset and re-confirm |
| Catch-up | **none** | **structural** — recomputed cumulatively from an unbounded earliest date, so a skipped or wrong period is absorbed by the next run | a **stub entry cut at the modification date**, then prospective re-derivation | full re-derivation |
| What stands | nothing guaranteed | everything; the position is restated | posted entries stand | nothing |
| Teardown integrity | per-entry, mixed outcomes | as validation | future draft entries removed, posted retained | **three paths reverse first; a fourth orphans posted entries** |

**Two consequences carried forward:**

1. **The most correction-resilient behaviour is on the path nobody uses.** The cumulative grouped model self-heals; the validation model cannot correct at all without disturbing closed periods. Every deployed company is configured for the fragile one.
2. **A corrective reversal can land in a different period from the entry it corrects** — verified with an executed positive control: a January entry's reversal dated end of February. **So a correction made under a lock does not restore the period it was meant to fix.**

## 2. The Unreachable Branch

The shared teardown declares three outcomes — unlink, cancel, reverse. Reaching *cancel* requires one expression to be simultaneously true and false, so **the cancel branch is unreachable**. With the audit trail enabled a previously-posted recognition entry is **always reversed**.

Any SMEsPlus design assuming a cancel outcome would be designing against behaviour that never occurs.

## 3. Destructive History — what must not be normalised

The Boss policy boundary is explicit: *correction must preserve audit lineage; do not normalise destructive benchmark behavior into a SMEsPlus requirement.* Three reference behaviours fall under it:

| Behaviour | Destructive? |
|---|---|
| Teardown **unlinks** entries where permitted | **YES** — the entry ceases to exist |
| A schedule teardown that **orphans** posted entries with their back-reference nulled | **YES** — the entries survive, invisible to the schedule and to its own entry list |
| Board recompute **deletes and rebuilds** draft entries | Not destructive of posted history; destructive of the prior schedule version |

> **None of the three is a SMEsPlus requirement.** They are reference behaviours that a clean-room design must decline.

## 4. The Three Primitives — the algebra P10 proposes

Reduced from four behaviours to three outcomes, and it is a **candidate**, not a fact:

| Primitive | Meaning |
|---|---|
| **STANDS** | A posted recognition event whose period is closed and whose amount is unchanged by the correction |
| **RE-DERIVED** | A future event replaced by a new version, with the prior version preserved |
| **CATCH-UP DELTA** | The arithmetic difference arising in the current period from everything that STANDS but should not have |

**The evidence for it, and against it.** Rows 2–4 of §1 support the reduction. **Row 1 does not**: in-flight amendment differs by **domain lifecycle**, not by algebra — pausing an asset is not a deferral operation and never will be. The prior round's own falsification test for the kernel fired here and was not read.

> **Corrected position: the three *outcomes* are common; *which* outcome applies is domain-specific, and the *operations* that trigger them are not shared at all.**

## 5. What Lineage Must Be Preserved

Separating the original fact from the derived accounting effect:

| Must survive a correction | Why |
|---|---|
| The **origin fact reference** — which document, which line | Without it a correction cannot be attributed |
| The **original recognition period** of every event, including superseded ones | Otherwise a re-dated or re-derived event cannot be reconciled to what it replaced |
| The **version** of the schedule that produced each event | Four behaviours produce four different histories; without versioning they are indistinguishable |
| The **reason** and the **actor** | The reference records neither for a recognition correction |
| **Prior versions of events that were re-derived** | `No silent correction; preserve complete revision lineage` |

**The reference preserves the first, partially. It preserves none of the other four.**

## 6. Disposition

- The four reference behaviours and the unreachable branch: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**
- The three-primitive algebra: **`DESIGN CANDIDATE`**, with its own counter-evidence recorded
- Destructive behaviours: **`BOSS-APPROVED POLICY INPUT`** — the Boss's non-normalisation boundary already governs them
- Lineage requirements: **`FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** — each is derived from an observed absence

---

## 7. CORRECTIONS FROM ADVERSARIAL CHALLENGE — `G02-R-06`, `G02-R-07`

### 7.1 "In-flight amendment: none" is contradicted at source. The row is struck.

§1 row 1 recorded in-flight amendment as **"none — only teardown of the source document"**. That is a
universal negative about operator routes, and it was never tested against the route an operator tries
first: **editing the window on the posted line.** P10 verified all four legs at source:

| Leg | Result |
|---|---|
| Change tracking on the two window fields | **none** — the edit does not reach the chatter |
| Membership of the integrity-hash field set | **absent** — the edit does not break the inalterability hash |
| Membership of the lock-date protected field sets | **absent** — the edit is not refused on a posted or locked entry |
| The module's own write guard | raises for **the account field only** |

Generation fires from the posting routine alone. **Nothing re-derives when the window changes.**

> **Corrected statement.** *There is no in-flight amendment path that **re-derives**. There is one
> that **diverges**.* The ledger keeps the original slices; the two deferral reports recompute the
> expected spread from the two date fields on every render. **A posted, hashed, lock-eligible entry
> set and its own report disagree, with nothing recording that they do.**

**Reachability, verified by P10 and narrower than first reported.** At **model level** the field is
writable by any import, API call or server action, unconditionally. Through the **UI**, the Journal
Items list carries a `readonly` gate once deferral entries exist; the invoice form's line list does
**not**, but its parent field is state-gated to draft. The hole therefore opens in the
**reset-to-draft window** — where the deferral entries have been *reversed rather than removed*, so
the gate flag remains true and the state gate is satisfied. Two clicks present as an amendment and
are in fact a teardown-and-regenerate, with the reversals landing in whatever period they land in.

### 7.2 A fourth correction outcome

The three primitives — `STANDS`, `RE-DERIVED`, `CATCH-UP DELTA` — are **necessary and not exhaustive**:

> **`SILENTLY DIVERGENT`** — the plan changes, nothing is re-derived, nothing stands as a decision,
> no delta is computed, and the schedule report and the ledger disagree with no record that they do.

It is not a correction outcome; it is the **absence** of one, and it is the default result of the
most natural operator gesture. **`DESIGN CANDIDATE`: the algebra must be closed — every amendment
gesture resolves to one of the three primitives, or is refused. A gesture resolving to none of them
is the defect.**

### 7.3 The anchor is silently wiped — `G02-R-07`

Deleting a deferral entry executes a clear of the **entire** source-link relation on every original
move, not only the link to the move being deleted. The grouped path's duplicate filter reads exactly
that relation. **Deleting one deferral entry re-arms duplicate generation for every invoice that was
grouped with it.** P10 did not hold this; it is the sharpest counter-example to the identity trace's
"the entry references something in four of five".

### 7.4 Two further bounds on the grouped path

- **It is idempotent in its arithmetic and not in its population.** The cumulative restatement is
  line-wise in its work and **move-wise in its exclusion**, so a source move with a second deferrable
  line picked up later is thereafter excluded whole, and the never-deferred sibling is permanently
  unreachable. "Recomputes the whole position each run" is true of the amount only.
- **The path P10 calls most correction-resilient is the one that makes the source document
  irreversible.** Reset-to-draft raises outright for any invoice grouped with another into a deferral
  entry — which, on the grouped path, is the normal case.

### 7.5 Partial recognition is unrepresentable, not merely unimplemented — `G02-R-19`

The reference has no partial primitive: the only amount override exists to plug the final period's
rounding residue. **The design pack forecloses it too** — amounts across a schedule must sum to the
base, and events are superseded, never edited. Those rules are right for immutability and, taken
together, make a partially-recognised event impossible to express.

Unreachable today, and each is an ordinary SMB case: recognising part of a bundled line (setup plus
twelve months' support); an amount revised mid-window by a change order, which is a re-measurement
and not a new schedule; partial cancellation or partial refund; milestone or percentage-of-completion
recognition; and partial performance against a billed-ahead line. **None of the thirteen closure
questions covers any of it.** `CQ-P10-03` covers *partial periods*, which is pro-rating, a different
thing. **This is an unasked question, not an unanswered one, and P10 does not add closure questions —
it is routed to the Boss as such.**
