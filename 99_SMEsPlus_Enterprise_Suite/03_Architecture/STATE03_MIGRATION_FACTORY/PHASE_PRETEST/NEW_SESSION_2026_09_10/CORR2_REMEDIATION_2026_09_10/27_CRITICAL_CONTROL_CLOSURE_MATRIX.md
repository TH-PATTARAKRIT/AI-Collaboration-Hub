# 27 — CRITICAL / ZERO-TOLERANCE CONTROL CLOSURE MATRIX

# `7 of 9 AT 100 % · 2 REMAIN · WAS 3 of 9`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: `§17` and `§23` of the ruling prompt · Boss: **SOLE FINAL APPROVER**

> **`§5`/`§17`: no `99.x %` acceptance, no average, no aggregate.** Each control is attacked
> individually and reported individually. **`§23`: every claimed `100 %` carries a recorded
> falsification attempt, including the ones that now claim `100 %` for the first time.**

---

## 1. THE CLOSURE TABLE

| ID | Critical control | Denominator | Named membership | Was | **Now** | Missing member / control | Authority | Corrective action | Proof | **Status** |
|---|---|---:|:-:|---:|---:|---|---|---|---|---|
| **`ZT-01`** | No canonical artefact overwritten by an audit or remediation channel | `0` violations | ✔ | `100 %` | **`100 %`** | none | programme rule | none required | `git diff --name-status`: this package is **purely additive**; `0` files outside `CORR2_REMEDIATION_2026_09_10/` touched | **MEETS** |
| **`ZT-02`** | No veto self-discharged | `0` violations | ✔ | `100 %` | **`100 %`** | none | `SC-42`, `AAS-V-02` | none required | `3` instrument shapes + firing synthetic injection → **`0` AAS+-authored records**; vetoes `7` · `0` discharged | **MEETS** |
| **`ZT-03`** | Every denominator has named membership | **`26`** | ✔ | `47.6 %` | **`100 %`** | was `11` defective of `21` | `§9` | `30_` §2 re-derives the **current** `26` denominators, each with members enumerated; `4` of the old failures were **my own path-set error** (`26_` §2) | `30_` §2, row by row | **MEETS** |
| **`ZT-04`** | No unsupported or conditional `N/A` | **`0` `N/A` claims** | ✔ | `0 %` | **`100 %`** | was `2` conditional `N/A`s carrying no defeating condition | **`BOSS-CORR1-01` §2.3** | `XMC-H-15`/`-16` **re-classified `CONDITIONAL APPLICABILITY — UNRESOLVED`**, all `8` attributes determined, **kept in the denominator** | `20_` §4; population of `N/A` claims is now **`0` by Boss ruling**, not by omission | **MEETS** |
| **`ZT-05`** | **Independent assurance established** | `2` passes | ✔ | `0 %` | **`0 %`** | **both passes** | `SC-AUTH-02` Reading C | **not closable by this session** — it is what the rerun exists to supply | neither B-7 round is independent (`02_`, as corrected by `17_` §5) | **`HOLD` — INDEPENDENT** |
| **`ZT-06`** | **Tenant / company isolation proven** | `48` verification items · `X-15` | ✔ | `0 %` | **`0 %`** | **element `10` — the isolation semantic itself** | `SA17` §2b | **semantic is specifiable now and is not specified**; the proof is Build/Test | `X-15`: *"this scenario **is** element `10`; **`0 of 8` isolation proofs**; **two** lock-defeat paths, the second leaving no record"* | **`HOLD` — SMEs CORE SEMANTIC** |
| **`ZT-07`** | Evidence integrity — immutable and verifiable | `15` (`CORR2`) + `16` (post-ruling) | ✔ | `100 %` | **`100 %`** | none | manifest discipline | manifest regenerated; composition stated **by** the manifest | `33_`: `shasum -c` all OK; one-byte corruption control **fires**; coverage complete by set-difference | **MEETS** |
| **`ZT-08`** | No authority act without a durable artefact | **`3` acts in force** | ✔ | `0 %` | **`100 %`** | was `R-D-01`, `0 of 1` | `§4` of the ruling prompt | **`17_` created BEFORE `18_`**; `R-D-01` has **no residual independent effect** — every act it performed is now performed by a recorded ruling (`26_` §4) | `17_` exists; `18_` applies it; separation enforced | **MEETS** |
| **`ZT-09`** | No Boss-reserved obligation leaves the count without a closure act | **`4`** | ✔ | `25.0 %` | **`100 %`** | was `3` uncounted | `§16` | count **open**; record **askable** as a separate field | `05_` §5, `13_` §1: `POH-D-02` · `SC-SMT-01` · `BOSS-CORR1-01`\* · `BOSS-CORR2-RD01`\* — all `4` carried; \* now **RULED**, with closure acts at `17_` | **MEETS** |

```
CRITICAL CONTROLS            9
AT 100 %                     7    ZT-01, ZT-02, ZT-03, ZT-04, ZT-07, ZT-08, ZT-09   (was 3)
BELOW 100 %                  2    ZT-05, ZT-06                                       (was 6)
CHECK  7 + 2                 9    OK
CLOSED THIS ROUND            4    ZT-03, ZT-04, ZT-08, ZT-09
```

---

## 2. `§23` — FALSIFICATION ATTEMPTED ON EVERY CLAIMED `100 %`

**Including the four newly claimed. A control that has just moved to `100 %` is the one most worth
attacking.**

| Control | Attack | Result |
|---|---|---|
| `ZT-01` | search for any modification outside this package's own directory across the whole commit | **`0` found. Attack FAILED** |
| `ZT-02` | `3` instrument shapes; synthetic injection of *"Issued by: AAS+"* and *"AAS+ has performed the discharge act"* | injection **fires**; real corpus returns **`0`**. **Attack FAILED** |
| **`ZT-03`** | **hunt for a denominator in this package whose membership is a range expression rather than an enumeration** | `30_` §2 audited all `26`. **`D-11` (`48`) is stated as `4` sub-ranges** — attacked specifically: each sub-range carries its own provenance **and an author-chosen flag**, and `22+18+7+1 = 48` ✔. **Ruled sound. Attack FAILED** |
| **`ZT-04`** | **is the `N/A` population really `0`, or has an `N/A` been renamed to hide it?** | `XMC-H-15`/`-16` are **counted in the conditional population and enter any scenario whose enable condition holds** — they were **not** removed from any denominator. **Attack FAILED.** But see §3 |
| **`ZT-08`** | **does any act still rest on `R-D-01` alone?** | every one of the `4` re-placements is ruled by `BOSS-CORR2-RD01`; `3` also stand on `SC-54`/`SA17` independently. **`0` residual. Attack FAILED** |
| **`ZT-09`** | **is there a fifth Boss-reserved obligation not in the count?** | swept `B1`…`B10′`, `POH-D-*`, `SC-SMT-*`, `BD-ACC-*`, `CC-D-*` for items with an unfired closure act. **`B5′` surfaced** — see §3 |
| `ZT-07` | one-byte corruption; unlisted-file addition | corruption **detected**; addition **not** detected by `shasum -c`, so coverage proved by set-difference instead. **Attack FAILED** |

### 2.1 Attacks that succeeded in part — published

**`ZT-09` — `B5′`.** The readiness split `18 / 4 / 0` carries **`NO BOSS RULING`**, and `10_` records
its authority as **`NONE — B5′ unruled`**. **Is `B5′` a fifth open Boss decision?**

| | |
|---|---|
| Measured | `B5′` was **put to Boss in the `22_` ruling round and deliberately left `PROVISIONAL`** — *"`B5′` deliberately left PROVISIONAL"* (resume state) |
| Is that an **open decision** or a **ruled deferral**? | **a ruled deferral.** Boss saw it and declined to adopt the re-derived split. It has a closure act: the decision not to decide |
| Disposition | **NOT a fifth open Boss decision.** It is recorded as a **`PROVISIONAL` figure with a ruled authority state**, and the readiness row stays at `81.8 %` and `PROVISIONAL` |
| Recorded because | the distinction between *unasked* and *asked-and-deferred* is exactly the `open` vs `askable` conflation `05_` §3 found. **`B5′` is asked-and-deferred, so it is not re-asked** (`§20`) |

**`ZT-04` — the residual the control does not measure.** The `N/A` population is genuinely `0`, so the
control passes. **But `CORR2-CND-01` stands: the conditional items' flip is *undetectable* —
`SA06-F-05`: *"protected only by configuration; **no independent check exists**"*.** That is **not** an
`N/A`-support failure; it is a **missing control**, carried as **FD blocker `FD-08`** and as
`CORR2-CFG-02`. **`ZT-04` at `100 %` must not be read as *"the neutrality is safe"*.**

---

## 3. THE `2` THAT REMAIN — exact dependency

### `ZT-05` — independent assurance · `0 %`

| | |
|---|---|
| Denominator | `2` consecutive clean structurally independent passes |
| Numerator | **`0`** |
| Why | Round 1 and Round 2 both carry `Co-Authored-By: Claude Opus 5`, which `17_` §5 confirms **is evidence the reasoning executor was not GPT-5.6 Sol** |
| Owner | **INDEPENDENT PARTY** — outside SMEs Core, Architecture, PMO and Boss |
| Closable by this session? | **NO, and attempting it would repeat the defect** |
| Eligibility effect | **permitted to remain** under `§25` criterion `10` (*"all remaining blockers are explicitly external/Boss/independent"*). **Requiring independence before the independence round would be a circular gate** |
| Closes when | `34_`'s rerun executes under a proven reasoning-executor identity, **twice** |

### `ZT-06` — tenant / company isolation · `0 %`

| | |
|---|---|
| Denominator | `48` verification items; scenario `X-15` |
| Numerator | **`0`** |
| Missing | **element `10` — the isolation semantic itself.** *"This scenario **is** element `10`"* |
| Evidence | `X-15`: **`0 of 8` isolation proofs**; `SA10-F-05`: **two lock-defeat paths, the second leaving no record** |
| Phase split | **the SEMANTIC is `S` and specifiable now — it is not specified.** The PROOF is `I` and correctly Build/Test-placed |
| Owner | **SMEs Core / Architecture** |
| Closable below Boss? | **YES** |
| Eligibility effect | **BLOCKS.** `§25` criterion `9`: *"no missing semantic within SMEs Core / Architecture authority."* **Element `10` is exactly that** |
| Carried as | **FD blocker `FD-14`** (`29_`); business semantic `BS-14` (`28_`) |

> **`ZT-06` is the control that decides `§25` eligibility.** `ZT-05` is permitted to remain open; `ZT-06`
> is not. **A dimension whose *semantic* is missing is a current-phase failure even when its *proof* is
> correctly deferred** — `§8`: *"An undeclared population is NOT a valid deferral."* Here the population
> is declared and the **semantic it must satisfy is not.**

---

## 4. DOWNSTREAM CONTRACTS FOR CRITICAL CONTROLS WHOSE PROOF IS DEFERRED

| Control | Population | Future gate | Evidence contract | Owner | Trigger | Success criterion |
|---|---|---|---|---|---|---|
| `ZT-06` proof | `48` items; `X-15` | **Build / Test** | with `2` companies configured, no fact of company `A` is readable, postable or aggregable from company `B`, **and both lock-defeat paths are closed and leave a record** | Architecture | first multi-company Build/Test cycle | **`8 of 8` isolation proofs**, and the negative case: an attempted cross-company act **fails and is recorded** |
| `ZT-02` continuous | vetoes | **State gate** | no veto discharged other than by its issuer | AAS+ | any discharge attempt | issuer-authored record exists |
| `ZT-07` continuous | every package | **each freeze** | manifest verifies; coverage complete by set-difference | executing session | each commit | `0` failures, `0` uncovered files but the manifest itself |

---

## 5. MOVEMENT SUMMARY

| | Was (`09_`) | **Now** |
|---|---:|---:|
| At `100 %` | `3` | **`7`** |
| Below `100 %` | `6` | **`2`** |
| Falsification attempts that succeeded against the package | `5` | **`0` outright; `2` in part** (§2.1) |

**Cause attribution for the `4` closures:** `ZT-03` — `[E]` my path-set error + `[W]` re-derivation ·
`ZT-04` — `[R]` Boss ruling + `[W]` attribute determination · `ZT-08` — `[R]` ruling recorded durably +
`[W]` record-before-application · `ZT-09` — `[W]` counting unit corrected.
**`0` closed by relaxing a definition.**

---

## 6. CHECKPOINT

> **`9` critical controls, each attacked individually · **`7` at `100 %`, `2` remain** (was `3` / `6`) ·
> `4` closed this round, **`0` by relaxing a definition** · every claimed `100 %` carries a recorded
> falsification attempt, **including all `4` new ones** · `2` attacks succeeded **in part** and are
> published — `B5′` is asked-and-deferred, not a fifth open decision; `ZT-04` passes while its residual
> **missing control** is carried as `FD-08` ·
> **`ZT-05` permitted open under `§25`(10); `ZT-06` BLOCKS eligibility — element `10` is a missing
> semantic within SMEs Core authority.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
