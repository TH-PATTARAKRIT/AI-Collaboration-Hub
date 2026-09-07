# 01 — `CO-F-01` PIN-HONOURING INSTRUMENT REPAIR (controller record)

**Repair published on** `corr/p11-phase-s-remediation-2026-09-07-001` @ **`9d4ecdc`**
**Base** `corr/p11-phase-s-final-2026-09-07-001` @ `002748d` — **not rewritten**
**Full owner record** `P11_CENTRAL_CORE_RECONCILIATION/P11_CO_F_01_PIN_INSTRUMENT_REPAIR.md`

> **Owner repair. Not verification. `RC-02` must test it, including the possibility that it is wrong.**

---

## 1. Instrument and wrappers — the search, not just the finding

**POPULATION** every file in the P11 package at `002748d` (**88** tracked).
**PATTERN** (a) `git grep origin/` over `*.py`/`*.sh`; (b) **shebang on the first two bytes of every
file regardless of extension**; (c) fixed-string search for each of the **11** pin SHAs.
**UNIT** one file.

| Candidate | Resolves peer trees? | Consumes a pin table? | Disposition |
|---|---|---|---|
| `corr3_instrument/intake_derivations.py` | **yes, twice** | **declares one and never reads it** | **THE DEFECT** |
| `p11_scripts/peer_intake.sh` | yes, over **all** refs | **no — declares "every ref reachable from origin"** | **out of scope, floating BY DECLARATION**; inspected, reason stated |
| `p11_scripts/peer_wip_snapshot.sh` | no — local clones only | no | out of scope; declares snapshot semantics |
| `p11_scripts/mkmanifest.sh` | no | no | out of scope |

**Exactly one instrument consumes a pin table.** That is a searched result over a declared
population, **not an assumption that the named file was the only one**.

> **A tool failure caught inside this sweep, and reported.** The first pin-token search used
> `git grep -E '\b(sha|…)\b'` and returned **0 files — including the file that visibly contains them**.
> `git grep`'s ERE does not support `\b` here; the positive control `\bPEERS\b` → **0** against
> `PEERS` → **2** proves it. Re-run as fixed strings the answer is **15 files**. **A zero from a
> pattern that cannot match is indistinguishable from a zero from an empty population**, and this one
> would have silently understated the blast radius by fifteen files.

## 2. The defect, proven by changing the pin

| Run | Change | Result |
|---|---|---|
| `RUN A` | none (file as published) | `D1 58 · D2 50 · D3 159 · UNION 216` |
| `RUN B` | **`P09` pin `4778792` → `92de8a1`** | `D1 58 · D2 50 · D3 159 · UNION 216` |

**Byte-identical stdout and union file.** The declared `sha` is never read. **`RUN A` today also
returns `216` where CORR3 returned `212` and `002748d` returned `214` — the same code, three
answers, because it reads whatever the branch heads point to at the instant of execution.**

## 3. Repair, and the controls that could have failed it

Both resolutions honour the pin; the table is validated **fail-closed before any derivation** on
missing · malformed · unresolvable · not-a-commit · duplicate · **non-ancestor of the declared
branch** · **non-substantive under `P11-G-10`**. **Six classes, six distinct firings** — plus a
pin-sensitivity control (`UNION 214 → 211`, three named members drop) and a
**behaviour-preservation** control that reproduces CORR3's published *before* — `55/48/155/212`,
`19/36/29` — **exactly**.

> **Two first-draft controls fired for the wrong reason and were discarded and rebuilt.** The
> intended non-ancestor pin was another peer's and tripped the duplicate check; the intended
> "valid alternative pin" `4778792~1` **is** the prompt commit and tripped the substantiveness check.
> **Both are recorded. A control that fires for a reason other than its own is not a control**, and
> the only reason these were caught is that the firing message names its cause.

## 4. Provenance of the published figures

`RUN E` — pins set to the branch heads current when `002748d` was written — returns
**`D1 57 · D2 49 · D3 157 · UNION 214 · 20/37/29`**, which is P11's published "after" table exactly,
and a union file **byte-identical to the published `union_212.txt`**.
**The published post-repair figures were produced by floating heads. Confirmed, not inferred.**

## 5. The finding that a count could not have caught

| | Published (floating) | Pin-honoured |
|---|---|---|
| members | **214** | **214** |
| sha256 | `94e7d59…` | `80d18bd…` |
| out | — | `P08 \| 64_P08_NOTIFICATION_TO_P11_Q_P08_01.md` |
| in | — | `P08 \| 59_P08_METHOD_AND_REQUIREMENT_REGISTER.md` |

**One member left as another entered and the total did not move.** A reader comparing cardinality
would have seen `214 = 214` and concluded the population was unchanged.

**And the member the floating run silently pulled in is the very P08 notification P11's prose
simultaneously calls "Not received" (`CO-F-02`).** **P11's own published population contained the
document its text declared absent. The two defects are one event seen from two sides**, and each
made the other harder to see.

## 6. Claims re-stated, bounded

`D1` **57→56** · `D2` **49→48** · `D1∩D2` **20→19** · `D3` and `UNION` unchanged in count, **union
set corrected**. `P11-E-47`'s verification sentence **withdrawn as false** — the instrument cannot
"re-run at `4778792`", and a pin-honoured run there gives `56/48/157/214`. **The defect `P11-E-47`
reported, and `P11-G-11`, both stand.**

**Not widened:** `B-35`, `B-37`, `B-38`, `AAS+-VETO-04`, `S06`, `Q-P11-02/03/04` — none turns on the
post-re-pin population. **Terminal `TERMINAL B` unchanged.**

**New:** `P11-E-48` · `P11-G-12` (a population is its members, never its cardinality) ·
`P11-G-13` (an edit to a value a program never reads is not a repair — change the pin to a wrong
value and prove the output moves).
