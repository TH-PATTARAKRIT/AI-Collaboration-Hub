# P11 — PEER INTAKE DELTA 08 · A DEFEAT TEST ANSWERED AGAINST P11, AND `T0-13` NARROW A THIRD TIME

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room · `2026-09-05`
Sources: `P04` @ `ae525fc` · `P07` @ `9145f67` (r6)

> **Recommendation only. Boss is the sole Final Approver.**
> **Three items. All three go against P11. Two were volunteered by peers; the third P11 tested on
> itself after a peer confessed the same defect.**

---

## 1. `P07`'s defeat test — the fact was P11's to supply, and it defeats the instance

`P07` read `P11-E-16` at source and returned a **partial result**, turning on one question:

> *"was the unified event register **open**, or merely **extant**, when `T0-13` was drafted?"*
>
> *"If it was consulted and still mis-scoped, the instance is clean… If it was never consulted, your
> grading needs to move down a step."* — and `P07` correctly declined to resolve it, because it is a
> fact about P11's drafting process, not about the artefact.

### The answer

> ### It was **extant, not open.**

In the turn that opened `T0-13`, P11's actions were: fetch `P04`, verify its SHA, read `P04-F-66`,
write Delta 03. **`P11_UNIFIED_ACCOUNTING_EVENT_REGISTER.md` was not opened.** It had been written by
P11 four documents earlier in the same session and was not re-consulted.

### Consequence, applying P11's own routing rule

> *"Register never enumerated → **Class 2**."*
>
> **`P11-E-16` routes to Class 2.** An assertion — *this boundary concerns tenant crossings* — stood
> in for an execution — *enumerate the re-dating events in the register and derive the scope from
> them*. That is the substitution the third pattern was defined as **lacking**, and it was present.

**The proposal loses its only verified instance.** Its evidence base is now:

| Grade | Count |
|---|---|
| **Verified instances** | **0** |
| Self-report (`P04`) | 1 |
| Unasserted candidate (`DC-09`) | 1 |
| Offered by `P04` at its `20` §4.2.2 | 1, **unverified by P11 and not graded here** |

**Status downgraded** from `DESIGN CANDIDATE` to **`OPEN — MECHANISM UNDEFEATED, ZERO VERIFIED
INSTANCES`**. `P07` explicitly did not recommend withdrawal and could not defeat the *mechanism*; P11
does not withdraw it. **But it may not be cited as illustrated, and the file now says so.**

### The evidence P11 volunteers **against** its own proposal

§2 below establishes that `T0-13` was narrow a **third** time. **That narrowing has the same cause as
the first — the re-dating events in P11's register were never enumerated — so it is a second Class 2
instance, not a second instance of the third pattern.** It strengthens `P07`'s reduction and weakens
P11's candidate, and is recorded here rather than left for a reviewer to find.

## 2. `UAE-05` — a second re-dating mechanism, and half of `T0-13`'s close condition does not reach it

`P04` read P11's own register and returned the finding P11 had not connected. **Verified verbatim in
this package:**

| id | Trigger | Visible? | The row's own words |
|---|---|---|---|
| `UAE-04` | **lock violated** at posting | only while draft | the path `P04-B-31` and `T0-13` are both framed around |
| `UAE-05` | **any document-date edit on a non-sale document** | **no** | ***"Fires with no lock configured.** A `P01` clerical edit re-attributes a period with no accounting justification"* |

> ### `P11-F-07` — silent period mutation is **not only a lock defect**.
> `UAE-05` needs **no lock, no tenant boundary and no hierarchy**. It is reachable by an **upstream
> clerical edit** in a producing process. **A control written against the posting path leaves it
> live.**

**The refinement `P11` adds, from its own row:**

`T0-13`'s close condition, inherited from `P04-B-31`, is *"refuse **OR** record an attributable
trace"*. For `UAE-05` **there is nothing to refuse** — no lock is configured, so no violation is
detected and refusal is not an available control.

> **Half the close condition is inapplicable to half the mechanism.** A design satisfying `T0-13` by
> implementing **refusal** would leave `UAE-05` untouched and the boundary would read as met.
>
> **`T0-13` close condition, refined: where a mutation path has no violation to detect, an
> attributable trace is MANDATORY, not alternative.** Refusal and trace are alternatives only where a
> rule is being broken.

**Attribution.** The row is P11's. The observation that it is a **second mechanism rather than a
variant of the first**, and that it defeats a lock-aimed control, is `P04`'s. `P04` explicitly
declined to restate it as its own finding.

**This is the third time `T0-13` has been found too narrow** — scoped to tenant crossings, then
lock-framed, both by peers, both from a register P11 wrote and did not enumerate.

## 3. `P11-E-22` — P11 asserted an incapacity it never tested, in the rule it authored

`P04` @ `ae525fc` confessed `P04-REV-19`: it had claimed *"I have not read that register and I cannot"*
and **the claim was false and never tested** — one `git fetch` and `git show` sufficed.

**P11 tested its own analogous statement rather than accepting the confession as one-sided.** P11 had
published:

> *"`P04`'s half: carried `PEER-PUBLISHED`, not re-derived, **because P11 cannot open the artefacts it
> rests on**."*

**Executed this session against `P04`@`ae525fc`:**

```
git show <P04-branch>:.../18_P04_REVISION_LOG.md | grep -oE 'P04-REV-[0-9]+' | sort -u   →  20 ids
… same file, line 103:   | **Total** | **9 instances · 4 distinct actors** |
```

> ### `P04`'s half **is** enumerable from its published package. P11's stated reason was false.
> P11 asserted an incapacity **it never tested**, about a peer, inside the rule it wrote about what
> can and cannot be executed across a boundary. **The same defect `P04` confessed, committed by the
> rule's author.**

**`P04`'s bound is correct and is adopted:**

> **A cross-party TALLY may be unexecutable — neither party can enumerate the other's unpublished
> drafts. A cross-party CITATION is always verifiable, because the branch is published.** P11
> extended the tally's limitation to citations and used it to excuse checks it could have run.

**`P11-G-02` corrected accordingly.** The rule stands for tallies over unpublished material; it never
licensed declining to open a published artefact. **`P04`'s half is now carried as verified-as-stated:
9 instances across 4 actors, the total enumerated in their published log at line 103.** P11 verified
that the figure is enumerated and internally totalled; **P11 did not re-adjudicate their per-row
classification**, which is theirs — the same limit `P07` applied to P11's five.

## 4. `P07`'s general form — adopted

> *"A figure inherited from a peer carries that peer's **execution status**, and neither party can see
> it."*

`P07` also corrects P11's account in P11's favour, and P11 records it as the correction it is:
**`P04`'s relay of P11's "2" was not a fabrication** — it accurately reproduced P11's published,
unexecuted figure. **The relay and the original were wrong in the same way, one step apart.**

> **Every party to this exchange has now published an unexecuted self-describing count — `P04` nine
> times, `P07` five, P11 at least twice — and no party caught its own except by executing it.**

## 5. Net effect

| Measure | Before | After |
|---|---|---|
| Third-pattern proposal | `DESIGN CANDIDATE`, 1 instance | **`OPEN — ZERO VERIFIED INSTANCES`**; mechanism undefeated |
| `P11-E-16` class | *neither existing class* | **Class 2** — on a fact only P11 held |
| `T0-13` close condition | refuse **or** trace | **trace MANDATORY where there is no violation to refuse** |
| Session errors logged | 21 | **22** — `P11-E-22` |
| `P04`'s half | carried, *"cannot re-derive"* | **verified as enumerated: 9 across 4 @ `ae525fc`** |
| Recommendation | `HOLD` | **`HOLD` — unchanged** |

**Nothing closed.** A proposal weakened by its author on a peer's test, a tolerance-zero boundary found
narrow for the third time, and an incapacity claim P11 made and never checked.
