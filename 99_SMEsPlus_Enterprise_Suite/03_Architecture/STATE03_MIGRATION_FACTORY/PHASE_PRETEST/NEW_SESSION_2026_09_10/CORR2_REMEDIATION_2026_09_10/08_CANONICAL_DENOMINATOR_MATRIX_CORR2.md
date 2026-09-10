# 08 — CANONICAL DENOMINATOR MATRIX · `CORR2`

# `21 MEMBERSHIP CLAIMS AUDITED · 10 SOUND · 11 DEFECTIVE · 47.6 %`

## `CHECKPOINT I`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Baseline: `c91d5840` · **Supersedes `10_PRETEST_CANONICAL_RECOVERED_MATRIX.md` §1** · Boss: **SOLE FINAL APPROVER**

> **`10_` opens *"ALL DENOMINATORS RESTATED WITH NAMED MEMBERSHIP"* and closes *"`0` denominators
> without named membership."* **Measured against its own file, that closing assertion is false.**

---

## 1. THE AUDIT RULE

A denominator is **SOUND** only if all four hold:

```
DENOMINATOR  a number
NAMED MEMBERSHIP  every member identifiable  -- A RANGE EXPRESSION IS NOT AN ENUMERATION
NUMERATOR    a number, with the same unit as the denominator
EVIDENCE     a citation resolving to a file inside the declared PATH SET
```

**Unit declared: one row of `10_` §1 making a membership claim.** `10_` §1 holds `27` rows; `6` carry
`—` in the membership column (numerator rows); **`21` make a membership claim.** That is the denominator
of this audit, and it is derived from the file, not chosen.

**Positive control on the enumeration instrument, run before any zero is reported:**
```
PTX-01…PTX-11 -> 11 distinct ids in 2 files against a declared denominator of 11   THE INSTRUMENT FIRES
```

---

## 2. THE MATRIX

| # | Denominator | Value | Named membership | Source | Numerator | Coverage | Threshold | Critical | Membership proof | Current gate | Contradictions | **Status** |
|---:|---|---:|---|---|---:|---:|---|:---:|---|---|---|---|
| `1` | Boundary classes | **`12`** | **YES** — `12` labels verbatim | **Boss `B4′`**, `22_` §1 | `11` reached by a contract row | **`91.7 %`** | `96 %` | **YES** | read at the Boss text (`06_`) | Pre-Test | class `12` uncovered | **SOUND — coverage HOLD** |
| `2` | `XMC-H` handoff rows | **`18`** | **YES** — `-01`…`-18` | `SA_CORR3_08` | `0` contract-sufficient of `16` applicable | **`0 %`** | `96 %` | **YES** | `grep -oE 'XMC-H-[0-9]{2}' \| sort -u \| wc -l` → `18` | Pre-Test | — | **SOUND — coverage HOLD** |
| `3` | — mapped to a class | `12` | **YES** | `05_`, re-derived `06_` | `12` | `100 %` | — | `1:1` verified label by label | Pre-Test | — | **SOUND** |
| `4` | — `N/A` evidence-backed | `2` | **YES** — `-15`, `-16` | `SA_CORR3_08` | `0` carry their defeating condition | **`0 %`** | `100 %` (`ZT-04`) | **YES** | grep → `0`/`0`; control fires at `3` | Pre-Test | primary source ordered it *"in the row"* | **DEFECTIVE — CONDITIONAL `N/A`** |
| `5` | — gap-carrying, outside the set | **`4`** | members named | `05_` | — | — | — | **YES** | **population bound UNDECLARED** | Pre-Test | **`5` under the union; floor not ceiling** | **DEFECTIVE — UNDECLARED UNIT** |
| `6` | `SA_CORR4_02` contract rows | **`10`** | **YES** | `SA_CORR4_02` §5 | `2` contract-sufficient; **`0` compliant** | **`20 %` / `0 %`** | `96 %` | **YES** | enumerated at §5 | Pre-Test | — | **SOUND — coverage HOLD** |
| `7` | Canonical vetoes | **`7`** | **YES** | **Boss `B3′`** | `0` discharged | — | — | **YES** (`ZT-02`) | second-line attack failed; re-measured | Pre-Test | — | **SOUND** |
| `8` | `PTX` exit controls | **`11`** | **YES** — `PTX-01`…`-11` | **Boss `B6`** | `0` satisfied | **`0 %`** | `96 %` | **YES** | **`11` distinct ids in `2` files — proved** | Pre-Test | — | **SOUND — coverage HOLD** |
| `9` | `IR` flows | **`20`** | **NO** | Boss `B9′` | `14` claimed reconciled | — | `96 %` | **YES** | **max `6` distinct `IR-nn` in the path set** | Pre-Test | `MF-03` exclusion falsified (`07_`) | **DEFECTIVE — UNSUPPORTED** |
| `10` | — `IR` reconciled | `14` | **NO** | `SA_CORR2_05` — **outside the frozen path set** | — | — | — | — | not resolvable in package | Pre-Test | — | **DEFECTIVE — EVIDENCE OUTSIDE PATH SET** |
| `11` | `AR` flows | **`30`** | **NO** | Boss `B9′` | `15` claimed reconciled | — | `96 %` | **YES** | **max `10` distinct `AR-nn`** | Pre-Test | as above | **DEFECTIVE — UNSUPPORTED** |
| `12` | — `AR` reconciled | `15` | **NO** | `SA_CORR2_06` — outside path set | — | — | — | — | — | Pre-Test | — | **DEFECTIVE — EVIDENCE OUTSIDE PATH SET** |
| `13` | Verification items | **`48`** | **YES** — `X-01…22` (`22`) + `E2E-01…18` (`18`) + `PT-S-01…07` (`7`) + `PT-C-01` (`1`) | `11_` §1, with provenance and an **author-chosen flag per sub-population** | **`0 PASS`** | **`0 %`** | `96 %` | **YES** | decomposed, `22+18+7+1 = 48` ✔ | **Build/Test** (`03_`) | — | **SOUND — coverage HOLD, phase-placed** |
| `14` | `EC-04` boundaries | **`3`** | **YES** | `8C-CLARIFICATION-01` | `0` closed | **`0 %`** | `100 %` | **YES** (`ZT-06`) | — | **State gate** (`03_`) | — | **SOUND — coverage HOLD, phase-placed** |
| `15` | `EC-07` passes | **`2`** | **`—` ON THE FILE'S OWN FACE** | `SC-AUTH-02` Reading C | `0` clean | **`0 %`** | `100 %` | **YES** (`ZT-05`) | **neither B-7 round is independent (`02_`)** | **Module + State** (`03_`) | closing assertion false on this row alone | **DEFECTIVE — NOT NAMED** |
| `16` | Readiness split | **`18 / 4 / 0`** | **YES** — `04_` §3 | **NONE — `B5′` unruled** | `18` writable of `22` | **`81.8 %`** | `96 %` | **YES** | **mechanically re-extracted; overlap `∅`, missing `∅`, extra `∅`; `X-99` injection control fires** | Pre-Test | — | **MEMBERSHIP SOUND · AUTHORITY ABSENT — `PROVISIONAL`** |
| `17` | Exit conditions | **`17`** | **YES** | master prompt §19 | `7` claimed satisfied | — | `96 %` | **YES** | — | Pre-Test | **superseded by `13` and by `14`; NO supersession marker** | **DEFECTIVE — STALE** |
| `18` | Open Boss decisions | **`1`** | **YES** — `POH-D-02` | `B1` | — | — | `100 %` | **YES** (`ZT-09`) | **measured `4` open, `0` closures** | Pre-Test | `34_` had corrected `1 → 3` | **DEFECTIVE — WRONG VALUE** |
| `19` | FD blockers | **`3`** | *"YES — §2"* | — | — | — | — | **YES** | **`10_`'s own §2 lists `3` + *"plus `2` new"* = `5`** | Pre-Test | self-contradicting inside one file | **DEFECTIVE — SELF-CONTRADICTING** |
| `20` | B-7 findings | **`18`** | **YES** — `B7-F-01…18` | `5bd36d62` | `18` confirmed | `100 %` | — | **NO** | enumerated | Pre-Test | — | **SOUND** |
| `21` | SMEs Core obligations | **`4`** | **NO** — *"`CORE-04`…`-06`, `CORE-05` held"* = **`3` members** | rulings | — | — | — | **YES** | **three memberships for one count:** `10_` `{04,05,06}` · resume L55 `{04,05,06,07}` · resume L93 `{04,05,06,X-14}` | Pre-Test | — | **DEFECTIVE — WRONG MEMBERSHIP** |
| `22` | External-authority items | **`14`** | **NO** — *"`X-01…X-14`"* | `19_`, `36_` | — | — | — | **YES** | **actual set is `X-01…X-13` + `X-15`;** the range **adds non-member `X-14`** and **drops member `X-15`** | Pre-Test | `X-14` is an `X-nn` collision (`R2-F-09`) | **DEFECTIVE — WRONG MEMBERSHIP** |

*(Rows `3`, `4`, `5`, `10` and `12` are sub-rows of their parents and are audited as membership claims because `10_` §1 makes a membership claim on each.)*

---

## 3. TALLY

**The unit is one `10_` §1 row making a membership claim.** `10_` §1 holds `27` rows; **`6` carry `—`**
in the membership column (they are numerator rows): *vetoes discharged*, *`PTX` satisfied*,
*verification `PASS`*, *`EC-04` closed*, ***`EC-07` passes***, *`EC-07` clean*.
**`27 − 6 = 21` membership-claiming rows.** That is the denominator, derived from the file.

*(The matrix above carries `22` numbered entries: the `21` membership-claiming rows, plus row `15`
`EC-07 passes` — a `—` row, included because `10_`'s closing assertion covers it. **Row `15` is audited
and is excluded from the `21`.**)*

```
MEMBERSHIP-CLAIMING ROWS                       21
SOUND      rows  1, 2, 3, 6, 7, 8, 13, 14, 16, 20                     = 10
DEFECTIVE  rows  4, 5, 9, 10, 11, 12, 17, 18, 19, 21, 22              = 11
CHECK      10 + 11                                                    = 21   OK
ZT-03 COVERAGE (denominators with sound named membership)  10 / 21 = 47.6 %
REQUIRED   100 %                                                      HOLD

SEPARATELY: row 15 (EC-07) carries "-" in the membership column, so
            10_'s closing assertion "0 denominators without named membership"
            is false on the file's own face, before any audit is run.
```

**Row `16` (readiness `18 / 4 / 0`) is counted `SOUND`** because `ZT-03` measures **membership**, and its
membership is exact under a firing injection control. **Its *authority* is absent (`B5′` unruled) and it
is carried as `PROVISIONAL` in `09_` and `12_`.** The two properties are recorded separately rather than
blended, because blending them is the defect this file exists to correct.

**Defect classes — the `11`:**

| Class | n | Rows |
|---|---:|---|
| **WRONG MEMBERSHIP** — named set ≠ actual set | `2` | `21` SMEs Core · `22` External |
| **WRONG VALUE** — count contradicted by evidence | `2` | `18` Open Boss · `19` FD blockers |
| **UNSUPPORTED** — range asserted, no enumeration inside the path set | `2` | `9` `IR` · `11` `AR` |
| **EVIDENCE OUTSIDE PATH SET** | `2` | `10` `IR` reconciled · `12` `AR` reconciled |
| **UNDECLARED UNIT** — count valid inside an undeclared bound | `1` | `5` gap-carrying outside |
| **CONDITIONAL `N/A`** — defeating condition dropped | `1` | `4` `-15`/`-16` |
| **STALE** — superseded value, no marker | `1` | `17` exit conditions |
| **Total** | **`11`** ✔ | |

**And separately, outside the `21`:** row `15` `EC-07 passes` — **NOT NAMED on its own face**, which
falsifies `10_`'s closing assertion before the audit begins.

## 4. DENOMINATORS OUTSIDE `10_` — audited for completeness

| Denominator | Value | Membership | Source | Status |
|---|---:|---|---|---|
| **Pre-Test exit conditions, corrected** | **`14`** | `{1,2,3,4,5,6,7,8,11,13,14,15,16,17}` | `03_` | **SOUND — re-derived from named instruments** |
| **Open Boss decisions, corrected** | **`4`** | `POH-D-02`, `SC-SMT-01`, `BOSS-CORR1-01`, `BOSS-CORR2-RD01` | `05_` | **SOUND** |
| **FD blockers, corrected** | **`7`** | see `10_` | `10_` | **SOUND** |
| **Round-2 second-line findings** | **`17`** | `R2-F-01…17` | `d878a603`, `01_` | **SOUND** — `17` in, `17` out |
| **Round-1 findings** | **`18`** | `B7-F-01…18` | `5bd36d62` | **SOUND** |
| **Circular gate defects, corrected** | **`2`** genuine + `1` misclassified + `1` relocated | `{9, 12}`; `10`; `11-D` | `03_` §5 | **SOUND — replaces two incompatible sets** |
| **Gap-carrying flows outside the declared set** | **`5`** floor, up to **`7`** | `XMC-H-13/-14/-17/-18` + contract row `4`; `+ -15/-16` if configuration defeats them | `06_` | **SOUND — with its population declared** |
| **Coverage dimensions** | **`5`** | Source Presence · Runtime Reachability · Configuration Reachability · Optional Function Reachability · Critical Control | `§6`, `09_` | **SOUND** |
| **Critical / Zero-Tolerance controls** | **`9`** | `ZT-01`…`ZT-09` | `09_` §5 | **SOUND — constituted this session** |
| **Manifest entries, recovery package** | **`15`** | listed in `16_` | measured `4` command shapes | **SOUND** — `17_`'s *"`14`"* is wrong |
| **Recovery package artefacts** | **`16`** | `01_`…`12_`, `14_`…`17_` | directory listing | **SOUND** — `15_`'s *range* is wrong, its count is right |

---

## 5. WHAT SURVIVES — recorded because refusals and correct work are evidence

| Item | Re-measured | Held |
|---|---|---|
| Manifest content integrity | `15 / 15 OK`; one-byte corruption control **fires**; addition-blindness demonstrated and answered by set-difference | **YES — `100 %`** |
| Manifest coverage | `16` present, `15` listed, `1` uncovered = the manifest itself; `0` listed-but-absent | **YES — complete** |
| `0` competing canonical writers | corrected instrument (writes vs merge-base) reproduces | **YES** |
| `18 / 4 / 0` membership | mechanically re-extracted; `X-99` injection control fires | **YES — exact** |
| `48` decomposition | `22 + 18 + 7 + 1 = 48`, provenance and author-chosen flag per sub-population | **YES — a model membership statement** |
| `PTX 11` | `11` distinct ids in `2` files | **YES** |
| `B4′` `12` | `12` labels verbatim at the Boss text | **YES** |
| `AAS-V-02` `NOT DISCHARGED` | `0` AAS+-authored records | **YES** |

> **`11_` §1's `48` decomposition and `04_` §3's readiness membership are the two rows in this package
> that meet the standard `10_` claims for all of them.** They are the pattern the rest must follow.

---

## 6. REQUIRED CORRECTION

1. **A range expression is not an enumeration.** `X-01…X-14` hid one non-member and one missing member.
2. **Declare the population with every count.** *"`4` outside"* is true and incomplete.
3. **Numerator and denominator must share a unit.** `IR`/`AR` count flows; their membership evidence counts files.
4. **Evidence must resolve inside the declared `PATH SET`**, or the path set must be widened and re-declared.
5. **A superseded value carries a supersession marker** naming what replaced it.
6. **A file asserting `0` exceptions must audit itself first.** `10_`'s own `EC-07` row carries `—`.
7. **Pre-commit sweep, four disjoint units:** (a) identifier defined-vs-cited · (b) count-vs-membership per row · (c) supersession markers on replaced values · (d) evidence citations resolve inside the path set. **All four are run at `12_` §4.**

---

## 7. CHECKPOINT

> ## `CHECKPOINT I — ALL DENOMINATORS AUDITED`
>
> `21` membership claims audited row by row · **`10` SOUND · `11` DEFECTIVE — `47.6 %` against a
> `100 %` floor** · `8` defect classes named · `11` further denominators audited outside `10_` ·
> positive control **fires** (`PTX 11/11`) · `10_` §1 **SUPERSEDED by this file** · `10_` itself
> **NOT MODIFIED** · **`0` denominators invented · `0` members hidden · `0` self-certified completeness.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the sole Final Approver.**
