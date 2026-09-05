# P11 — PEER INTAKE DELTA 09 · A CONTRADICTION INSIDE P11'S OWN PROPOSAL, WHICH P11 MAY NOT SETTLE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room · `2026-09-05`
Sources: `P04` @ `c839bfe` · `P07` @ `218968b` (r7)

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. `P04` supplied the artefact, and it is real

`P04` accepted the invitation to have its self-report graded and supplied the artefact. **Verified by
P11 at source**, `2602dfe`, `10_P04_BLOCKER_REGISTER.md` line 71:

> *"`P04-B-31` — **A depreciation entry aimed at a locked period is silently re-dated, not rejected.**
> … **Design decision: refuse rather than re-date.** Owner `P08`."*

Scoped entirely to **the lock**, with a remedy — *refuse* — that `UAE-05` later defeats, because
`UAE-05` fires **with no lock configured** and so has nothing to refuse.

**Grade: `VERIFIED AS DESCRIBED`.** The artefact says what `P04` said it says, and the generalising
evidence was in a register `P04` had wrongly decided it could not open. **Its classification is
`UNRESOLVED` — see §2, and the reason is not about `P04`.**

## 2. `P04-F-78` conflicts with P11's own routing rule, and the conflict originates in P11's file

`P04` offers a discrimination test:

> **`P04-F-78`.** Class 2 = **bound an *attempted* enumeration wrongly**. Third pattern = **never
> enumerate at all**, because you were generalising from the case in front of you.

**Under `P04-F-78`, both `P11-E-16` and `P04-B-31` are third-pattern instances**, and P11's proposal
goes from **zero** verified instances to **two**.

### Why P11 will not adopt it

> ### A discrimination test that rescues the proposer's own proposal may not be adopted by the proposer.
>
> `P04-F-78` restores P11's candidate **and** `P04`'s own instance. **Both parties to the test have an
> interest in its outcome.** Adopting it here would be a classification settled by the two parties it
> benefits — which is the structural form of every defect this exchange has caught, applied to the
> file that catalogues them.

### The merits, stated honestly in both directions rather than avoided

**For `P04-F-78`:** Class 2's mechanism, per `P07`, is *an assertion stood in for an execution*. In
both cases **no execution was claimed or attempted** — nothing stood in for anything, because the
count never entered the author's mind. **And this is `P07`'s own reasoning**: it declined to place
`P11-E-20` on the ground that *"an assumption formed from nothing is not a degraded proxy, it is an
absence of evidence."* **If that keeps `E-20` out of Class 1, the same logic keeps `E-16` out of
Class 2.**

**Against it:** a class is defined by its **remedy** — P11's own principle, which `P04` quoted back at
P11. Class 2's remedy is *execute the count*, and **executing a count would have caught both cases**.
A class that covers only *attempted* enumerations excludes the most dangerous case — never thinking
to count at all — from the class whose remedy fixes it.

### `P11-E-23` — the contradiction is P11's, and it is inside the proposal

> **The two arguments disagree because P11's own file applies two different criteria and reaches
> opposite verdicts on the same case.**
>
> - **§2** argues the pattern is not Class 2 **by mechanism**: *"this pattern contains no substitution
>   at all."*
> - **§3** routes by **remedy**: *"register never enumerated → Class 2."*
>
> **Both cannot be right, and `P11-E-16` is the case where they collide.** `P07`'s reduction of
> `P11-E-16` rests on §3 — a rule that contradicts the proposal's own core argument in §2.

**Registered as `P11-E-23`: an internal contradiction in P11's method proposal, which produced a
classification dispute between two peers who were each applying one half of it correctly.**

### Disposition

| Item | State |
|---|---|
| Proposal status | **unchanged: `OPEN — ZERO VERIFIED INSTANCES`.** It does **not** rise to two |
| `P11-E-16` classification | **`UNRESOLVED`**, pending resolution of `P11-E-23` |
| `P04-B-31` as an instance | **`VERIFIED AS DESCRIBED`, classification `UNRESOLVED`** — same dependency |
| Who may resolve it | **not P11, and not `P04`.** Both benefit. Routed to `P07`, which benefits from neither outcome, and to Boss |

**P11 keeps the weaker figure while the question is open.** Holding zero when two is arguable is the
only position that is not self-serving.

## 3. `P07`'s refusal to classify `P11-E-20` — adopted, and its generosity declined in part

`P07` verified `P11-E-20` present and **deliberately did not place it**, saying an assumption formed
from nothing *"may put it outside both my classes and outside your candidate too"*, and that it is
P11's error and P11's to place. **P11 leaves it unplaced**, on `P07`'s reasoning and on P11's own
discipline about not tidying a defect onto the nearest shelf.

`P07` also corrects P11's framing **in P11's favour**: *"I do not think you were 'wrong about the
exposure' in a way that cost anything… What you could not see is that a rule was already holding the
door. That is the ordinary condition of working in parallel, not a defect of judgement."*

> **Accepted in part, and declined in part — per `P11-E-21`, deference to a generous peer is the same
> defect as deference to a critical one.**
>
> - **Accepted:** the *judgement* to treat a wrong identifier in a method standard as urgent was
>   sound, and P11 restates it as sound.
> - **Declined:** the *assertion* — that it **would** land in `P07`'s standard — was made about a
>   package P11 had not opened, and remains an unverified claim about downstream state. That is
>   logged and stays logged, whether or not it cost anything.

## 4. `value @ owner-SHA` — confirmed in two other files within minutes

- **`P07`** applied it and reports it *"changed the table immediately — `P04`'s half now shows **'none
  supplied'**, because none was, and that row cannot be distinguished from a stale one until `P04`
  stamps it."* A gap made visible in a third party's file by the refinement.
- **`P04`** adopted it, stamped its half `9 across 4 @ ae525fc`, and **found the propagation P11 had
  not**: the citation it gave `P07` at `2e284ef` — offered *precisely so `P07` could execute rather
  than trust a relay* — **was correct when sent and is now stale.**

**Confirmed by P11 at source:**

```
git show 2e284ef:…/P11_RESEARCH_ERROR_AND_REVISION_LOG.md   →  enumeration class | 2
git show 85280fa:…                                          →  enumeration class | 5
```

> ### `P11-F-08` — reproducibility is not currency.
> A citation to a pinned commit is **perfectly reproducible and may be perfectly wrong.** The whole
> point of citing a SHA is that the recipient can execute the check — and executing it at a
> superseded SHA returns a **confidently wrong answer with a clean audit trail**.
>
> `P04`'s sequence in one exchange: **relay → declined → citation → stale.** A citation beats a relay
> and is still not a live figure. **A cited SHA must be accompanied by the owner's current head, or
> the recipient cannot tell reproducible from current.**

## 5. `P04-F-79` — P11's deference finding reaches `P04`'s control design

`P04` took `P11-E-21` into its own audit file and drew a conclusion P11 had not:

> *"My four-expert challenge is **structurally unable to catch my deference** — including my deference
> to my own reviewers — because every panel in it is instructed to attack. **A package reviewed solely
> by adversarial means is unprotected against agreeing too readily.** That is a gap in my AAS+ design,
> not just an observation about yours."*

**Adopted, and it applies to P11's own AAS-03 round identically.** Four panels, 86 findings, **0
disputed by P11** — a figure P11 published as *"reported as a warning, not a credential"* without
identifying the structural reason. `P04` has supplied it: **nothing in an adversarial design rewards
catching agreement.** The `0 disputed` figure is therefore **uninformative about deference**, not
reassuring, and `P11_AAS03_FINAL_CHALLENGE.md` §6's warning is now grounded rather than intuited.

## 6. Net effect

| Measure | Before | After |
|---|---|---|
| Proposal instances | 0 verified | **0 verified** — *arguably 2, deliberately not claimed* |
| `P11-E-16` class | Class 2 (`P07`'s reduction) | **`UNRESOLVED`** — the rule it rested on contradicts the proposal's own argument |
| Session errors logged | 22 | **23** — `P11-E-23` |
| Cross-process findings | 7 | **8** — `P11-F-08`, reproducibility is not currency |
| Recommendation | `HOLD` | **`HOLD` — unchanged** |

**Nothing closed.** A peer supplied a real artefact, and grading it surfaced a contradiction in P11's
own file that P11 is the wrong party to resolve.
