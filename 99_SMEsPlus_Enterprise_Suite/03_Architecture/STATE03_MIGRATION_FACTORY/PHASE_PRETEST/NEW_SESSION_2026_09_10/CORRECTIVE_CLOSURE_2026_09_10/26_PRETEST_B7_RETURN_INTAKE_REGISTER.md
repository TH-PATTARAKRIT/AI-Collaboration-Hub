# 26 — B-7 RETURN INTAKE REGISTER

## `CHECKPOINT A + B — INDEPENDENT EVIDENCE INGESTED AND FROZEN · 18 FINDINGS VERIFIED INDIVIDUALLY`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7-RETURN-CORR1-001]`
Canonical session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]` · Parent: `…-BOSS-RESOLUTION-001`
Branch head consumed: **`c94839e8`** · Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **B-7 evidence is IMMUTABLE INPUT. `0` characters of B-7's finding text are edited here.
> `0` corrections were requested from B-7. Every disposition below is a *canonical* verification
> against primary evidence, published beside B-7's original claim, never over it.**

---

## 1. `CHECKPOINT A` — the independent evidence, located and pinned

| Field | Value |
|---|---|
| Independent session | `[SMEPLUS-26-09-10-PHASE-PRETEST-B7-INDEPENDENT-001]` |
| Challenger | Independent OpenAI GPT-5.6 Sol — different vendor/model, new clean session, no authoring role |
| **Evidence channel** | `refs/heads/audit/b7-independent-2026-09-10` — **a separate branch; not the canonical branch** |
| **Commit SHA** | **`5bd36d62fc3e4c105996dd5560871ba7c8caaae5`** |
| Timestamp | **`2026-09-10 18:53:25 +0700`** |
| Artefact | `…/INDEPENDENT_REVIEW/B7_PHASE_PRETEST_2026_09_10/B7_INDEPENDENT_CHALLENGE_VERDICT.md` |
| **Blob SHA (immutable pointer)** | **`81f9aa53f6a560495c253876ac2805e3392b38f3`** |
| **SHA-256 of content** | **`2de832a470d7951a109b588a35c342510e1e70682e1d89265c0cc4bce2c5f9dc`** |
| Size | `429` lines · `34,916` bytes |
| Verdict | **`HOLD`** |
| Finding population | **`18`** — `B7-F-01`…`B7-F-18`, enumerated by command, no gap |
| Targets attacked | `12 of 12` · succeeded `6` · failed `6` |
| Re-grades / vetoes discharged / PASS | **`0` · `0` · `0`** |

**Non-interference test, executed:**

```
$ git diff --stat c94839e8 origin/audit/b7-independent-2026-09-10 -- '…/PHASE_PRETEST/'
  (0 lines)
```

**B-7 wrote nothing to the challenged tree. `STATUS = EVIDENCE INGESTED` — not `HOLD EVIDENCE INGESTION`.**
**Nothing below is reconstructed from a summary; every claim was re-tested at primary source.**

---

## 2. `CHECKPOINT B` — the 18 findings, verified individually

**Disposition vocabulary:** `CONFIRMED` — verified at primary evidence · `MODIFIED` — the observation
holds, the conclusion does not, or the reverse · `DISPROVED` — falsified at primary evidence ·
`HOLD` — cannot be determined at this phase.

### 2.1 `T1` family — the readiness split

| ID | B-7's exact claim | Sev | Falsification method | Canonical verification | **Disposition** |
|---|---|---|---|---|---|
| **`B7-F-03`** | `β5` (`X-05`) is `NOT ESTABLISHED` on a test `SC-BD-07`'s structure defeats; `F2` was ruled `3 of 3` as one principle and the **governing** `SA17 V2` §2d maps `F2 → rows 5, 10` | MATERIAL | re-read `SC-BD-07` at primary text; dated the three `SA17` generations by commit | **CONFIRMED — and the executor's underlying finding `CC-F-01` is DISPROVED outright.** `CC-F-01` claimed the `3` `F2` members are *"never enumerated in the ruling, in `SC-11`, or in any `SC-*` record."* **They are enumerated in at least six places** (§3.1) | **CONFIRMED** |
| **`B7-F-04`** | `β8` (`X-09`) graded `WRITABLE` while its own row records `Average`-costing residual → Boss, an open **BOSS-ONLY DECISION** (`SC-SMT-01`) | MATERIAL | traced `SC-SMT-01` to `SC-03`, `SC-BD-05` §8.1, `SC-11` §6 obl. 3, `PT-11` L109 | **CONFIRMED.** `SC-03`: *"BOSS-ONLY DECISION"*; `SC-BD-05` §8.1: *"a **live obligation, not a closed condition** … **not** discharged by this ruling"*; `SC-11` §6 owner **Boss**; `PT-11` carries it **OPEN** | **CONFIRMED** |
| **`B7-F-05`** | `β7` (`X-08`) lists a dependency the same ruling closed, and omits the `Average` residual, which `JT-05` raises for **both** return rows | MATERIAL | read `SA_CORR5_10` row 8 note; read `SC-SMT-01`'s subject | **CONFIRMED.** Row 8's note states the return-basis conflict *"is `JT-05` seen from Inventory"* — closed by the ruling on its own row. `SC-SMT-01`'s subject is *"a **returns-costing difference**"*, generic to `JT-05`, therefore rows **8 and 9 alike** | **CONFIRMED** |
| **`B7-F-06`** | `19` is not reproducible as a membership; errors run in both directions so the total can survive while cells are wrong | MATERIAL | per-cell re-derivation | **CONFIRMED.** Re-derived from zero at `27_`: **`18 WRITABLE / 4 GATED / 0 NOT ESTABLISHED`** | **CONFIRMED** |

### 2.2 `T3` family — the boundary denominator

| ID | B-7's exact claim | Sev | Falsification method | Canonical verification | **Disposition** |
|---|---|---|---|---|---|
| **`B7-F-07`** | The declared `12` is exactly `XMC-H-01…12`; `6 of 18` map to no class and `4` of those (`H-13`, `-14`, `-17`, `-18`) carry `HOLD — EXACT GAP` outside the declared set | MATERIAL | mechanical name-match of the 18 rows against the 12 declared classes | **CONFIRMED.** Reproduced independently and extended to the `10` contract rows at `28_`. The `10`-row set additionally **adds** `Purchase → Inventory` and **drops** class `12` | **CONFIRMED** |
| **`B7-F-08`** | `B9′` admits `MF-01`/`MF-02` onto a boundary (`XMC-H-18`) that `B4′` excludes from the contract and Pre-Test denominator; `22_` applied both without testing the interaction | MATERIAL | cross-read `22_` §1 vs §7.1 against `SA_CORR3_08` `XMC-H-18` | **CONFIRMED.** `XMC-H-18` is the migration/replay handoff, is `HOLD — EXACT GAP` with *"elements 14 and 15 `NOT SUPPLIABLE`"*, and is outside the declared `12` | **CONFIRMED** |

### 2.3 `T7` family — migration admission

| ID | B-7's exact claim | Sev | Falsification method | Canonical verification | **Disposition** |
|---|---|---|---|---|---|
| **`B7-F-09`** | `CC-F-11`'s universal clause *"no existing valuation rule reaches `MF-01`"* is falsified by `BD-ACC-03B`'s `Standard` branch | MATERIAL | tested the universal against each ruled costing method | **CONFIRMED — and EXTENDED.** `Standard` **and** `Average` both reach it (`29_` §2). The extension: **`FIFO` does not, for a reason neither the executor nor B-7 identified** — `HX-24` carries *"quantity and value"* as an **aggregate**, and `FIFO` is layer-ordered. **A narrower, sharper gap survives where a false universal stood** | **CONFIRMED** |
| **`B7-F-10`** | `MF-03`'s exclusion rests on a zero-effect property guaranteed by `RT-E15-05`, an unbuilt control at `0 of 11` | MATERIAL | traced the cited authority to `B6`'s own `0 of 11` | **MODIFIED.** **The objection to the reasoning is CONFIRMED and the reasoning is withdrawn.** The **conclusion survives on an evidence-independent basis** re-derived at `29_` §8: `MF-03` originates **no target-state transition of its own**. The non-idempotency risk B-7 exposed is real and is **re-routed** to the idempotency control family (`X-22`, element 15, `RT-E15`) where it is testable | **MODIFIED** |

### 2.4 `T8` / `T9` family — separation of duties

| ID | B-7's exact claim | Sev | Falsification method | Canonical verification | **Disposition** |
|---|---|---|---|---|---|
| **`B7-F-11`** | `B8′` Structure A routes the re-grade to a party the evidence declares is **not** separate from the executor, and `22_` accepted it untested | MATERIAL | read `SC-03` §0 and `SC-04` §5 at primary text | **MODIFIED.** **The observation is CONFIRMED**: SMT is *"internal first-line challenge by specialist role … one corpus assembled by one party"*, and `10_` line 86's *"NOT SMEs Core"* is **wrong and is corrected at `30_`**. **The structural conclusion is DISPROVED on Boss's own wording**: `B8′` states the bar as *"the party performing the re-grade **shall not certify its own independent verification**"* — a **certification** bar, which Structure A satisfies. `SC-03`/`SC-04` bar SMT's output from **counting as** independent assurance; they do not bar SMT from **performing** technical work | **MODIFIED** |
| **`B7-F-12`** | Exit condition `16` is not established because `CC-F-08` is closed only as a routing question | MATERIAL | traced `23_` §2 row 16's evidence | **MODIFIED.** **Correct at intake.** The residual contradiction was `10_`'s mis-statement of SMT's party identity, **not** Structure A. `30_` corrects it; condition `16` is re-graded on the recount at `31_` with `30_` as closing evidence | **MODIFIED** |

### 2.5 `T11` — circular proof

| ID | B-7's exact claim | Sev | Falsification method | Canonical verification | **Disposition** |
|---|---|---|---|---|---|
| **`B7-F-13`** | Exit condition `2` is certified `SATISFIED` on the executor's own figure, which `22_` §7 records as `NO RULING — PROVISIONAL — B-7 attack target #1` | MATERIAL | read `15_` row 2's evidence cell against `22_` §7 | **CONFIRMED.** The criterion as worded (*"freshly re-derived"*) grades an **act**, and the act occurred; **but its output is unratified**, and a criterion that a party satisfies by performing its own unratified act is a weak criterion. Recorded at `31_` as **`SATISFIED — QUALIFIED`**, with the qualification travelling on the same line, and named as a Round-2 target | **CONFIRMED** |

### 2.6 `T6` — the `48` denominator

| ID | B-7's exact claim | Sev | Falsification method | Canonical verification | **Disposition** |
|---|---|---|---|---|---|
| **`B7-F-14`** | `PT-S-01`'s *"`VAT` `0` and `WHT` `0` in all three scenario registers"* is false against `SA_CORR5_10` (`VAT=2`, `WHT=2`), and *"the three"* are never named | MODERATE | measured each candidate register with a firing control | **CONFIRMED.** Re-measured: `SA15 V2` `0/0` · `SA17 V2` `0/0` · `SA15 CORR5` `0/0` · **`SA_CORR5_10` `2/2`**. The path set was stated as a description. **`PT-S-01`'s substance survives** — both occurrences are statutory period references inside `S` markers, not a scenario carrying a tax determination — **the published measurement does not**, and is restated at `34_` §4 | **CONFIRMED** |

### 2.7 Arithmetic and package-integrity findings

| ID | B-7's exact claim | Sev | Canonical verification (command-tallied) | **Disposition** |
|---|---|---|---|---|
| **`B7-F-01`** | `15_`'s *"`5` SATISFIED · `12` FAIL"* contradicts its own table, which enumerates `3`; `23_`'s *"up from `5`"* inherits it | MATERIAL (arithmetic) | Tally of `15_` §1: **`13` FAIL · `1` PARTIAL-treated-as-FAIL · `3` SATISFIED**, 17 rows ✔. `23_`'s BEFORE column: identical. **The true baseline is `3`. The round's own gain was understated** | **CONFIRMED** |
| **`B7-F-02`** | `23_` §2 states *"`3` conditions moved"* while enumerating `1, 5, 6, 7, 16` | MODERATE | Rows moving `FAIL → SATISFIED`: **`1 5 6 7 16` — count `5`** | **CONFIRMED** |
| **`B7-F-15`** | `25_` states the manifest has `23` entries; it has `24` | MODERATE | `grep -cE '^[0-9a-f]{64}' 24_…txt` → **`24`**; `shasum -c` → **`24 of 24 OK`** | **CONFIRMED** |
| **`B7-F-16`** | `23_` §5 inventories *"Artefacts `24` — `01_`…`23_` + manifest"*, omitting `25_` although `24_` lists it | MINOR | The manifest's `24` entries are `01_`…`23_` **plus `25_`**; `23_` §5's `24` is `01_`…`23_` **plus the manifest**. Two different sets of the same size | **CONFIRMED** |
| **`B7-F-17`** | `22_` §8 totals *"`5` denominators"* over a table moving `6` | MINOR | Distinct denominators moved: boundary, veto, open Boss decisions, `PTX`, `IR`, `AR` = **`6`**, across **`5`** rulings. Unit stated ≠ unit counted | **CONFIRMED** |
| **`B7-F-18`** | `23_` §6 *"`5` moved on rulings, `8` did not"* vs §1's own tally | MINOR | §1 `Moved?`: `5` `YES` + `1` `YES (count only)` = **`6` moved, `7` not**. The veto count **did** move `6 → 7` | **CONFIRMED** |

---

## 3. Intake result

| Disposition | n | Findings |
|---|---:|---|
| **`CONFIRMED`** | **`15`** | `B7-F-01`, `-02`, `-03`, `-04`, `-05`, `-06`, `-07`, `-08`, `-09`, `-13`, `-14`, `-15`, `-16`, `-17`, `-18` |
| **`MODIFIED`** | **`3`** | `B7-F-10`, `-11`, `-12` |
| **`DISPROVED`** | **`0`** | — |
| **`HOLD`** | **`0`** | — |
| **Total** | **`18`** ✔ | **`0` findings disappeared. `0` findings merged. `0` findings downgraded to make a count.** |

> **`15 of 18` independent findings survived canonical verification unchanged, and `3` were modified —
> two of them in the executor's favour on Boss's own wording, one against the executor's reasoning while
> preserving its conclusion. `0` were disproved.** A `0`-disproval rate against an adversarial round is
> not a compliment to this package; it is a measurement of how much of it was asserted rather than derived.

### 3.1 `CORR1-F-01` — an executor finding DISPROVED by the intake it triggered

**`CC-F-01` — *"a family ruled `3 of 3` whose `3` members are never named"* — is FALSE.**

**Its declared search population was *"the ruling, `SC-11`, or any `SC-*` record."* The `F2` membership is
enumerated at primary text in at least six documents, including two inside that very population:**

| Source | Text | Inside `CC-F-01`'s population? |
|---|---|:--:|
| **`SA_FINAL_03` §2 `F2` card** | *"**Decision IDs** \| `XD1-P1` (sell-side cancellation gate) · `TV6-BOSS-01` (credit exposure at commitment confirmation) · **over-receipt tolerance default**"* | no — **and this is the document that CONSTITUTED the family the ruling then ruled** |
| **`SC-01` §2 row `F2`** | *"`F2` Commercial control-default policy \| `XD1-P1`, `TV6-BOSS-01`, over-receipt tolerance default \| … **3**"* | **YES** |
| **`SC-29`** | *"`XD1-P1`, `TV6-BOSS-01`, tolerance default (`SC-BD-07`)"* — listed under ***"Already ruled and controlling — `16`"*** | **YES** |
| `SC-38` · `SC-56` | `SC-BD-07` \| `F2` \| `XD1-P1`, `TV6-BOSS-01`, tolerance default | **YES** |
| `SA_FINAL_03` §1 | *"a reader had to reconstruct that `XD1-P1`, `TV6-BOSS-01` and the tolerance default are **one principle asked three times**, which is `F2`"* | no |

> **Defect class: search population drawn narrower than the claim.** `CC-F-01` searched for the
> *enumeration* inside the *ruling chain* and concluded it did not exist, when it lives in the
> *constitution* chain — and, as it happens, in the ruling chain too. **This is the same defect shape the
> package has recorded under `PATH SET` discipline, committed by the finding that exists to police
> denominators.**

**`CC-F-01` is WITHDRAWN.** Its original text is preserved at `01_` §3.1 and `02_` §3 as Audit Lineage and
is **not edited**; this register supersedes its conclusion. **Consequence: `X-05` is `WRITABLE`, and the
`NOT ESTABLISHED` class is empty.**

---

## 4. Routing

| Finding(s) | Correction artefact | Boss ruling required? | Round-2 re-challenge? |
|---|---|:--:|:--:|
| `B7-F-03`, `-04`, `-05`, `-06`, `CORR1-F-01` | **`27_`** readiness cell re-derivation | **NO** — all determinable at primary text | **YES** |
| `B7-F-07`, `-08` | **`28_`** boundary crosswalk | **YES** — `BOSS-CORR1-01`, denominator correction | **YES** |
| `B7-F-09` | **`29_`** `MF-01` valuation + counterpart | **NO** — architecture act, §15 | **YES** |
| `B7-F-10` | **`29_`** §8 `MF-03` re-classification | **NO** | **YES** |
| `B7-F-11`, `-12` | **`30_`** `E2E-04` role and independence | **NO** — resolved on `B8′`'s own wording | **YES** |
| `B7-F-01`, `-02`, `-13` | **`31_`** 17-condition recount | **NO** | **YES** |
| `B7-F-14` | **`34_`** §4 restated measurement | **NO** | **YES** |
| `B7-F-15`, `-16`, `-17`, `-18` | **`34_`** §5 integrity corrections | **NO** | **YES** |
| all | **`33_`** disposition register | — | — |

---

## 5. Checkpoint

> ## `CHECKPOINT A + B`
>
> **B-7 evidence ingested and pinned by commit, blob SHA and SHA-256; `0` writes by B-7 to the challenged
> tree, verified by diff · `18 of 18` findings verified individually at primary evidence —
> **`15 CONFIRMED · 3 MODIFIED · 0 DISPROVED · 0 HOLD`, `0` disappeared** ·
> **`CORR1-F-01`: the intake DISPROVED an executor finding (`CC-F-01`) that B-7 had accepted as true**,
> on evidence in six documents, two of them inside `CC-F-01`'s own declared search population ·
> `1` Boss item routed, `0` manufactured · `0` B-7 finding text edited.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass. Boss is the sole Final Approver.
