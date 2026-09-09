# SA_FINAL_01 — CORR5 REPRODUCTION AND DELTA

## CP-SA-FG-10 — CORR5 FINAL BASELINE REPRODUCED

Session: `[SMEPLUS-26-09-09-PHASE-SA-FINAL-BOSS-GATE-001]`
Branch: `architecture/phase-sa-final-boss-gate-readiness-2026-09-09-001`
Parent CORR5 publication: `379fd07359eca9b9792630d97f5bf627c89a5ec7`
Boss: **SOLE FINAL APPROVER**

---

## 1. Parent verified

| Check | Result |
|---|---|
| Parent commit resolves | **YES** — `379fd073` is a commit, headline *"Phase SA CORR5: rename the CP-120 header (CHB-09 class) and refresh manifest"* |
| This control branch descends from it | **YES** — `git merge-base --is-ancestor 379fd073 HEAD` succeeds; the branch adds exactly one file, the master prompt (`ee479751`, +503 lines) |
| CORR5 package present at the parent | **22 files** |
| Manifest verification at the parent | **21 of 21 `OK`** (the manifest does not hash itself) |
| Empty or unreadable files | **0** |

---

## 2. Frame — `FG-FRAME`, declared once

| Clause | Declaration |
|---|---|
| **POPULATION** | Every branch on `origin` at fetch, this session. **n = 188.** Three shapes agree: `for-each-ref refs/remotes/origin` less the `origin` HEAD alias and `origin/HEAD` = 188 · `branch -r` less `HEAD` = 188 · `ls-remote --heads` = 188. *(CORR5 published 187; the delta is this session's control branch.)* **The `origin` alias defect `C5-I-01` is filtered with `grep -vx origin`, not `grep -v HEAD`** |
| **PATH SET** | Every path in the tree of every one of the 188 branch heads |
| **UNIT** | Stated per measurement; branch, path and row units are never conflated |
| **COMPLEMENT** | Non-head-history blobs; non-`.md`/`.txt`/`.csv` files; reference-ERP source trees and runtime dumps outside this clone — **not re-entered this session**; CORR5's two bounded evidence-at-rest passes stand as published and are not re-run |
| **DELTA-FIRST** | Only the delta since `379fd073` is re-measured from scratch (§4); CORR5's own figures are reproduced from its rows (§3), not re-derived from the corpus |

---

## 3. Every controlling CORR5 figure, reproduced

Reproduced from the parent commit's own rows, not from a summary line.

| # | CORR5 claim | Reproduction method | Result |
|---:|---|---|---|
| 1 | Material SMEs Core open items = **0** | `SA_CORR5_14` §3 verbatim; §2.1 rows 1–13 all `closed`; rows 15–18 marked non-material with owners | **REPRODUCED** |
| 2 | Material document-owner open items = **0** | `SA_CORR5_14` §3; the two controlled versions and the controlled anchor patch are published *in* the CORR5 package | **REPRODUCED — and see `FG-F-01` (§5), which adds a document-owner item CORR5 did not detect** |
| 3 | Material Phase SA specification gaps owned by SMEs Core = **0** | `SA_CORR5_10` §4.1 dimension row: `G` column = **0** | **REPRODUCED** |
| 4 | Material PMO open items = **1** | `SA_CORR5_14` §2.1 row 14 | **REPRODUCED — still 1** (`SA_FINAL_00`) |
| 5 | 22-scenario dimensional distribution | grep of the 22 register rows: `**B**` cells = **13**; `GATED` = **12**; `WRITABLE` = **10**; `S` markers = **9** | **REPRODUCED** — matches `SA_CORR5_10` §4.1's `185 / 13 / 9 / 0` over 198 cells |
| 6 | Boss-gated scenario count | enumerated rows 1–6, 8, 9, 10, 16, 17, 18 | **12** — REPRODUCED |
| 7 | Runtime-proof-only scenario count | enumerated rows 7, 11, 12, 13, 14, 15, 19, 20, 21, 22 | **10** — REPRODUCED |
| 8 | `SA-SPEC COMPLETE / PRE-TEST READY` under the CORR5 definition | register column | **0** — REPRODUCED. *(CORR5's definition requires an implementation to exist; none does. §6 of this pack re-states why that is not a Phase SA gap.)* |
| 9 | Active veto count, owner and type | `SA_CORR5_09` §2 rows read individually | **6** — `AAS-V-01` and `CF-V-01` `RE-SCOPED — RUNTIME PROOF OBLIGATION`; `RC-V-01` `RE-SCOPED — PRE-TEST OBLIGATION`; `AAS-V-03` and `CF-V-02` `STILL ACTIVE` on Boss-gated grounds; `AAS-V-02` `SUPERSEDED BY BOSS RULING`, discharge act pending. **0 discharged** — REPRODUCED |
| 10 | Runtime-only proof obligations | `SA17` controlled §2c, eight families | **8 families** — REPRODUCED |
| 11 | Pre-Test-only obligations | `SA_CORR5_15` §16 | the `RC-V-01` independent check; `XCR-02` test data once `MTI-D-04` is ruled; the three prohibitions verbatim — **REPRODUCED** |
| 12 | Independent-challenge status | `SA_CORR5_12` §1 | `EXTERNAL INDEPENDENT CHALLENGE — PENDING STRUCTURALLY INDEPENDENT REVIEW` — **REPRODUCED and re-tested at `SA_FINAL_06`** |
| 13 | Evidence manifest integrity | `shasum -a 256 -c` at the parent | **21 of 21** — REPRODUCED |

**Headline figures differing from CORR5: none.** One **addition** is made, not a difference: `FG-F-01`.

---

## 4. Delta since the parent commit

| Delta | Measurement | Bearing |
|---|---|---|
| Branch population 187 → **188** | three shapes | This session's control branch. No other branch created or deleted |
| `origin/SMEsPlus` `27717bde` → **`784f60a2`** | `git log 27717bde..origin/SMEsPlus` | **one commit, one added file**: the `ERPPLUS-152` Core Resource Governance **new session prompt**. Not a Boss ruling — it is a session commissioning document whose own §0 records *"Final Approver: Boss only"* and *"Build / Team C / production authorization: NOT GRANTED"*. It mentions Phase SA **0** times |
| Compliance split | two shapes | `188 / 5 / 183 / 0` — §3 of `SA_FINAL_00` |
| PR #63 | `gh` | still `OPEN` — `SA_FINAL_00` |
| CORR5 package content | manifest | unchanged, 21 of 21 |

### 4.1 The one material consequence of the mainline delta

`ERPPLUS-152` opens a Boss-authorized architecture session whose scope includes **`WS-09` Prepaid Wallet
& Capacity Authorization**, gate **`G6` Metering / Wallet Gate** (*"Close usage evidence, prepaid
authorization and customer transparency model"*), deliverable **`10_USAGE_LEDGER_METERING_AND_PREPAID_
AUTHORIZATION_MODEL.md`**, and its own **`G11` Boss Final Decision Gate**. Its §2 preserves parent
decisions 12–20 (prepaid before usage, 30-day notice is not credit, no unsecured postpaid overage,
wallet does not reset, usage counters may reset with evidence preserved).

> **This gives the prepaid-wallet accounting-character question an owner outside Phase SA.** Its
> disposition is at `SA_FINAL_02` §5 (Test C/E removal). It is the only Boss-list movement the delta
> produces.

---

## 5. `FG-F-01` — the one addition to the CORR5 baseline

> **`SA_CORR3_02` §12 is a table of eight consequences the kit/category proof states *"for their owners,
> not applied here"*. Three rounds have passed and two of the eight have never been applied — and both
> change a Pre-Test readiness grade.**

**Sweep.** Pattern `stated for (their|its) owners | not applied here | carried to other registers` over
the CORR2, CORR3, CORR4 and CORR5 branch heads. **Result: one substantive table — `SA_CORR3_02` §12** —
plus CORR5's own already-recorded `ARC-WP-010` wording note and two boilerplate hits in an inherited
document register. The residual is therefore bounded, not open-ended.

| `SA_CORR3_02` §12 row | Proposed by CORR3 | Applied by CORR4? | Applied by CORR5? | Applied here |
|---|---|:---:|:---:|---|
| `SA05` `BN-07` Kit / bundle → **`DETERMINED`** (*"the components carry the cost; the parent is not a valued object"*) | yes | no | no | **YES** — `SA_FINAL_04` §4 |
| **`SA15` `E2E-07` → `TRAVERSABLE`** — *"both stated blockers now closed"* | yes | no | **no** — CORR5's controlled `SA15` still reads `NOT TRAVERSABLE` | **YES** |
| `SA_CORR2_02` §3.4 `BN-07` residual → **`RESOLVED — NO BOSS DECISION REQUIRED`** | yes | no | no | **YES** — removes a Boss item that was never on the CORR5 list but was live in CORR2's register |
| `SA_CORR2_06` `AR-25` → `RECONCILED` | yes | no | no | recorded, **non-material** — changes no dimension cell (row 18 cites `AR-26`) |
| `SA_CORR2_04` row 11 → `ADVANCED — DE-ESCALATED` (valuation half only) | yes | no | no | recorded, non-material |
| `CORR-007B` §11 gaps 1–3 → `SUPERSEDED — EVIDENCE-BACKED` | yes | no | no | recorded, non-material (peer package) |
| P01's kit-control re-run recommendation → `DISCHARGED` | yes | no | no | recorded, non-material (peer package) |
| `C2-D-03` classification `D` → `A`, resolved | yes | **yes** | yes | already applied |

**And the second instance, found by the same test applied to `E2E-04`:** CORR5's controlled `SA15`
grades `E2E-04` `NOT TRAVERSABLE` on *"shortage→purchase trigger undetermined (`BN-04`, `TVDR-01`)"*.
`SA_CORR2_03` re-graded **`BN-04` to `PARTIAL`** with the trigger evidenced, and `SA_CORR3_08`
`XMC-F-03` established that the SMEsPlus-owned functional design carries the routing for `BN-04` under
its own vocabulary — *"buy-on-reorder-point; **make-or-buy on demand**; … and the system resolves the
movement chain from that choice"*. **The trigger is not undetermined. What remains is `C2-D-01`, a
Boss confirmation of a stated design position** (*"Hard trigger, soft binding — Inventory does not know
who will respond"*).

> **Class: the programme's recorded *a revision log is not a correction* / *stranded work* defect, at
> its fourth consecutive occurrence, and this time inside the artefact that hands work to Pre-Test.**
> CORR5 corrected `SA15`/`SA17` for the CORR2 consequences and for `E2E-15`; it did not sweep for the
> CORR3 consequences. **Both instances are applied in this package** (`SA15`/`SA17` controlled **v2**),
> and the effect is stated at `SA_FINAL_04`: **`NOT TRAVERSABLE` falls from 2 to 0.**

---

## 6. What this session does not re-open

`C4-01`/`C4-02`/`C4-03`; the four CORR5 workstream closures (`G1`, `G3`, `G5`, revocation); the element
15 adjudication; `MTI-05`/`-22`/`-33`; the 22-scenario dimension grades other than as §5 requires; the
two evidence-at-rest passes; `TVDR-04`/`TVDR-06`; `C2-D-03`; the compliance-retraction **decision**.

## 7. Checkpoint

> ## `CP-SA-FG-10 — CORR5 FINAL BASELINE REPRODUCED`
> **13 of 13 controlling figures reproduced · 0 differ · manifest 21 of 21 · frame re-declared at 188
> with three shapes · 1 mainline commit assessed (`ERPPLUS-152`, one Boss-list consequence) ·
> 1 addition (`FG-F-01`): two unapplied CORR3 consequences that change Pre-Test readiness.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
