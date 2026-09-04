# P11 — PEER INTAKE DELTA 04 · `T0-13` WIDENED, AND AN ATTRIBUTION CORRECTED

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Source: `research/account-p04-acquire-to-retire-2026-09-04-001` @ `fcfa1077` (`20` §4.2.2)
Corroborating: `research/account-p07-th-tax-compliance-2026-09-04-001` @ `ecc6059`

> **Recommendation only. Boss is the sole Final Approver.**
> **P04 raised three points. P11 verified all three independently and accepts all three.
> Two of them are corrections against P11.**

---

## 1. `T0-13` was scoped too narrowly. Widened.

### What P04 established

> **`P04-F-68` — `FACT VERIFIED`** at `fcfa1077`: *"The silent re-dating requires **no tenant boundary
> and no company hierarchy** to do damage. Inside a **single company**, an entry aimed at a locked
> period is already mutated into an open one with **no refusal and no trace** — the estate's own test
> asserts a charge migrating into the following fiscal year at full value. The cross-tenant case is
> the **worst** instance of the defect, not its only one."*

**Their consequence is correct and decisive:** `T0-13` as P11 drafted it *"would be satisfied by a
system that still misstates a fiscal year inside one company today."* A boundary that can be met while
the defect persists is not a boundary.

### `T0-13` — restated

| id | Boundary | Status |
|---|---|---|
| **`T0-13`** *(widened)* | **An accounting fact may not be silently mutated, at any scope.** No mechanism may re-date, re-attribute or otherwise alter an accounting fact without **either refusing, or leaving an attributable trace** — at `PLATFORM`, `TENANT` and `COMPANY` scope alike. **The cross-tenant crossing is the aggravated case, not the defining one.** | **`UNRESOLVED`** |

P11 chose to **widen rather than open a sibling**. The boundary asserts one property — *a mutation of
an accounting fact is never silent* — and the scopes differ in blast radius, not in the property. A
sibling would have split one invariant into two that must be kept in step, which is the
`SCP-03` shape P11 argues against elsewhere.

### Three consequences P11 must state

1. **`T0-13` is no longer contingent on `D-12`.** As drafted it read as downstream of the tenant-span
   ruling. It is not. **It is reachable today, inside one company, with no hierarchy** — so it stands
   whatever the Boss rules on `D-12`. `P11-B-16` is re-stated accordingly.
2. **`T0-13` moves from a prospective risk to a present defect.** That is a change in kind.
3. **`P04-B-31`'s close condition** is restated as P04 has it: not *"refuse rather than re-date"*,
   which is half of it, but **"refuse OR record an attributable trace"**. Silence satisfies neither.

### `P11-E-16` — the evidence for the wider scope was already in P11's own register

This is the part P04 could not see, and P11 must state it rather than accept the correction as
purely external.

`P11_UNIFIED_ACCOUNTING_EVENT_REGISTER.md` §2 already records **four accounting events that are
invisible at the moment they occur**, and **two of them are single-company re-datings**:

- `UAE-04` — entry re-dated on posting; *"the posted record carries no trace that its date was moved"*;
- `UAE-05` — entry re-dated on document-date change; **`no`** under *Visible?*; *"**fires with no lock
  configured** and no accounting justification"*.

> **Neither needs a tenant boundary. Neither needs a hierarchy. Both were in P11's own register when
> P11 drafted `T0-13` narrowly.**
>
> P04 found the wider scope in their evidence. **P11 already had it in its own and did not use it.**
> That is a worse failure than the one P04 reported, and it is recorded as such.

The cause is identifiable: `T0-13` was drafted *while* composing the cross-tenant compound, and took
its scope from the case in front of it rather than from the register that already generalised it.
**A boundary derived from its triggering instance inherits that instance's scope.** Registered as a
method note, not merely an erratum.

## 2. `P11-E-17` — the attribution was wrong, and P11 verified it against itself

### What P11 published

> *"the composition is P11's, the components are P04's… neither was composed by its owner, because
> `P04-F-66` and `P04-B-31` sit in different files answering different questions — **which is the
> whole argument for a cross-process seat existing at all**."*

### What is actually true

**False, and verified false by P11 this session** by opening the file it had already cited.
`20_P04_SCOPE_OWNERSHIP_MATRIX.md` at `3c10b4e` — **the same commit P11 cited as the source of
`P04-F-66`** — carries, under the heading **"Compounding with `P04-B-31`"**:

> *"the lock that cannot be reversed and cascades across the hierarchy is the same lock that **does
> not refuse** — it moves the entry into an open period instead. A cross-tenant hierarchy would
> therefore not produce a visible failure; it would produce **silently mis-periodised entries in the
> other tenant's books**."*

**The composition, and the exact phrase P11 published as its own headline, are P04's.** It was also
sent to P11 verbatim in the message that prompted the intake, under an explicit heading.

**And it appeared in P11's own terminal output.** The grep P11 ran to verify `P04-F-66` printed lines
232–234 of that file, including the `Compounding with P04-B-31` heading. **P11 saw the heading, did
not open the passage, and published an attribution claim about it.**

> **This is the class P11 logged against itself as `P11-E-15` — a claim published without its
> evidence opened — committed in the same message that logged `P11-E-15`.**
>
> By the declared unit that makes a **seventh** instance across **five** actors. P04's framing is
> exact: *"It confirms your rule rather than undermining it."*

### The true claim, which is smaller and survives

The cross-process seat **did** contribute here, and P04 identified what: **P11's question is what sent
P04 to read the lock-date implementation in the first place. The value was the prompt, not the
composition.** P11 adopts that formulation and publishes it in place of the overclaim. It is kept
*because* it is smaller — a reconciliation function that inflates its own contribution is worth less
than one that states it exactly.

### The replacement example — verified independently before adoption

P04 proposed a better illustration. **P11 did not adopt it on P04's word**; it read P07's package at
`ecc6059` and confirms it:

- `21_P07_PEER_EVIDENCE_INTAKE_P04.md` is a dedicated intake of P04's statutory evidence;
- `P07-D-30` records that P04 *"framed the question on deductibility alone; **the VAT limb is P07's
  and is the half that would otherwise be missed**"* — an unevidenced destruction as a **deemed sale
  carrying output tax**, distinct from deductibility;
- `P07-F-59` records that a hire-purchase or instalment sale carries a tax point and a tax invoice on
  **every instalment due date**, and that *"the researched system has no instalment tax point, no
  tax-invoice object to issue, and no mapping to route the contract; **the three gaps compound rather
  than overlap**"*.

> **That is genuine cross-boundary composition:** a statutory definition P04 had read and P07 had not,
> producing in P07's model two gaps neither party could have produced alone — a missing deemed-supply
> row, and a *"no instalment tax point found"* recorded **without knowing the rule it was measuring
> against**. The second is a negative claim whose boundary was unknowable from inside one process.
>
> **The lock-date compound is not an example of this. The `P04`↔`P07` VAT exchange is.** P11 replaces
> the example.

## 3. Adopted without amendment

- **`SCP-09`** — P04 confirms both instances (machine register, work centre) now carry their expiry
  trigger explicitly. P11's note stands: P04 found the pattern twice and named it once, in prose.
- **The count reconciliation** — adopted by P04 verbatim in substance. Now at **seven instances across
  five actors**, per §2.

## 4. Net effect

| Measure | Before | After |
|---|---|---|
| `T0-13` scope | tenant crossings | **every scope; present defect, not prospective risk** |
| `T0-13` contingent on `D-12`? | read as yes | **no — stands whatever the Boss rules** |
| Tolerance-zero boundaries | 13, 0 resolved | **13, 0 resolved** — widened, not added |
| Session errors logged | 15 | **17** — `P11-E-16`, `P11-E-17` |
| Enumeration-defect instances | 6 across 5 actors | **7 across 5 actors** |
| Recommendation | `HOLD` | **`HOLD` — unchanged** |

**Two of this delta's three items are corrections against P11, one of which P11 should have caught
from its own register and one of which was visible in its own terminal output.** Both are published
at source rather than as footnotes, per `P11-G-01`.
