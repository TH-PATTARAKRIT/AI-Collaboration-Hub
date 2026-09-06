# P08_METHOD_AND_REQUIREMENT_REGISTER

Prompt `[SMEPLUS-26-09-06-P08-R2R-DOMAIN-PURE-BOUNDED-CLOSURE-002]` · **PHASE S** · bookkeeping artefact, no new research

## 0. Why this file exists

A sweep of every identifier family P08 owns found **20 identifiers, across four families, defined in the artefact that raised them and never rolled into any register.** Three of the four families **had no register at all.**

**Precision on the finding, because the first framing was wrong.** The sweep's first instrument reported *"ORPHAN: none"* for all eight families with `defined=1` in each — an impossible result that the instrument could not detect as a failure. Rebuilt with two positive controls (a fabricated id must be reported undefined; a known id must be reported defined), it returned 20. **Then spot-checking showed the label was still too strong**: every one of the 20 *is* substantively defined in prose. They are **unregistered**, not undefined.

`P08-CONTRA-47`. **Two defects, recorded separately:**
1. A sweep instrument returned a clean result it was structurally incapable of failing.
2. Four identifier families accumulated across three rounds with no roll-up.

**`P08-BD-19` was worse than either** and is recorded separately as `P08-CONTRA-45`: it was defined **and** a register for its family existed **and** it was still missing from it.

---

## 1. Method lessons — `P08-M-01` … `P08-M-17`

| ID | Lesson | Raised in |
|---|---|---|
| `P08-M-01` | A reviewer verdict must name the roll-up digest of the package it reviewed | `20` |
| `P08-M-02` | **A finding held only in the evidence quarantine cannot reach the design layer.** The discipline that protects the clean room can also strand a defect | `22` |
| `P08-M-03` | A declared pattern must be tested against the mechanism it is meant to exclude | `22` |
| `P08-M-04` | Independent contact remains the only control that reliably finds these | `22` |
| `P08-M-05` | **Reviewers disagree with each other, and that is signal** — not noise to be averaged away | `22` |
| `P08-M-06` | **Never declare "source-only" without searching.** A session declared it with readable database evidence present on the host | `33` |
| `P08-M-07` | **A positive control must demonstrate the pattern can match the thing being denied**, not merely that it produces output | `39` |
| `P08-M-08` | Evidence layers carry versions; a finding spanning two layers must state the version of each | `40` |
| `P08-M-09` | A context-key register built on a direct-read pattern alone is incomplete by construction | `44` |
| `P08-M-10` | A word-boundary pattern that could not fire returned zero across eight peer packages — the third instance in one session | `46` |
| `P08-M-11` | **A population with a machine signature must be tested for one before it is read as human behaviour** | `47` |
| `P08-M-12` | A mirror is not verified by testing some of its columns | `47` |
| `P08-M-13` | A measurement that bounds an exposure by a control's absence is only as good as the assumption that the control is the sole cause | `46` |
| `P08-M-14` | **The trace a snapshot supposedly cannot hold may already be in it.** A denormalised parent number settled two claims ruled untestable | `56`, from `48` |
| `P08-M-15` | **Arithmetic discipline does not protect against predicate error**, and a control that tests the instrument does not test the claim | `48` |
| `P08-M-16` | A package must establish that its source tree matches the system it describes **before** describing it | `49` |
| `P08-M-17` | **A re-framing pass is a distinct control from a re-search pass** and catches a class the others do not — both self-caught defects this round came from changing the question | `21` |
| `P08-M-18` | **NEW. A sweep instrument that cannot fail is not a control.** Publish the instrument's own positive controls beside its result, or the zero means nothing | this file |

## 2. Accounting-event identity findings — `P08-AEI-01` … `-04`

| ID | Finding | Standing after challenge |
|---|---|---|
| `P08-AEI-01` | Durable accounting-event identity exists where the event **originates outside the system**, and is absent where it originates inside | **BASE NARROWED.** One counterexample was struck (`P08-CONTRA-32`); one is a 1:1 delegate, not an event object; one was never independently read and its module is uninstalled in both 19.0 databases |
| `P08-AEI-02` | For every internally-originated posting path, **the only barrier to double posting is a state field**, and it fails three ways | `FACT VERIFIED` |
| `P08-AEI-03` | **The tamper seal does not close this.** No provenance field is sealed; a duplicate entry hashes exactly as validly as the original | `FACT VERIFIED` |
| `P08-AEI-04` | Duplicate detection on documents is **detective and advisory** — it declines only to *auto*-post | `FACT VERIFIED`, and its measured reach was corrected to **677 of 36,961** (`P08-CONTRA-35`) |

## 3. Kernel requirements P08 raises — `P08-RQ-KRN-01` … `-03`

| ID | Requirement | Origin |
|---|---|---|
| `P08-RQ-KRN-01` | **Every subsidiary store carrying an independently maintained value must have a stated control-account relationship and a periodic proof that the two agree — and the failure of that proof must be an accounting event** | inbound peer finding, verified |
| `P08-RQ-KRN-02` | **A financial fact carries its measurement basis**, and the kernel supports more than one basis over one set of accounting events without duplicating the events | inbound peer finding; see `P08-BD-11` |
| `P08-RQ-KRN-03` | **A period attribution that governs a statutory obligation must sit on the financial fact the statements aggregate, and must be complete over the fact set it claims to cover** | `49` §3 — 61,157 entries carry a tax period; **0** propagate it to their full item set |

**These are requirements P08 places on a future kernel. They are not design decisions and P08 does not choose how to satisfy any of them.**

## 4. Standing

| | |
|---|---|
| Identifier families swept | **8** |
| Families with no register before this file | **3** — method, event-identity, kernel-requirement |
| Identifiers registered here | **24** |
| Identifiers found defined-but-unregistered | **20** |
| Identifiers found **defined and missing from an existing register** | **1** — `P08-BD-19`, `P08-CONTRA-45` |
| Sweep instruments rebuilt after returning an unfailable clean | **1** — `P08-M-18` |
