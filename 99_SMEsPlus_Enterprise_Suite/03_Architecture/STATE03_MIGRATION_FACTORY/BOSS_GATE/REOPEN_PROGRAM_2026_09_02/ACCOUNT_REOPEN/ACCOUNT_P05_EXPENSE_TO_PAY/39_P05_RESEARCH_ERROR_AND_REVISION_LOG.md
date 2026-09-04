# 39 — P05 RESEARCH ERROR AND REVISION LOG (CONTINUATION)

`LAYER 2 — AUDIT QUARANTINE`
Continues `15`, which remains the authoritative log for the original round (`RE-01`..`RE-06`,
`GR-01`..`GR-03`). This file adds the continuation's errors and revisions. **Per `ER-AASR-1` this
file governs over any headline table in the package.**

## 1. Research Errors Found in This Continuation

### `RE-07` — **the package asserted that evidence did not exist, when it did** *(most serious)*

| | |
|---|---|
| **The claim as published** | `13 §5`: *"Live database access this session: **NONE.** No connection was attempted or available."* and *"**No P05-equivalent dump exists.**"* `20 U-02`: *"**No runtime or database evidence exists for P05.** Every behavioural claim is derived from source reading."* `19 §9`: `EC-02` **NOT MET** — *"no runtime evidence"*. |
| **What was actually true** | Six real `ir_module_module` registries and four production database dumps were sitting in the operator's own `~/Downloads` directory and in `~/OCC_Odoo18_Simulation_Lab/snapshots/`, readable offline with `pg_restore -f`, no server and no connection required. One of them holds **183,590 journal entries and 5,201 withholding certificates**. |
| **How it was found** | Only because this continuation's directive ordered the *highest available evidence class* for `U-01` and forbade inferring deployment from source directories. That instruction forced a search the original round never ran. |
| **Why it happened** | The original round searched for a **live database** — `psql`, a running server, a connection — found none, and generalised that to "no database evidence exists". It never searched for **database evidence at rest**. A dump file is not a live database, and it is not source code either; it fell between the two categories the session was looking in. |
| **Class of error** | Exactly the class the project standard names: a negative claim published at class **A** (*"no evidence exists"*) when the search boundary supported only class **B** (*"no live connection found"*). The scope was never declared, so nobody could see the gap. |
| **Impact if it had stood** | `U-02` would have remained a permanent gating unknown routed to Boss for a runtime authorisation that was never needed. Two findings that are now empirically confirmed at production scale (`TX-13`, `TX-20`) would have stayed at `SUPPORTED INTERPRETATION`. The severity inversion at `26 §5` — which is the single most decision-relevant output of the whole package — would never have been discovered. |
| **Correction** | `13 §5` and `20 U-02` are superseded by `24` and `25`. `EC-02`'s basis is restated in `27`. |

> **This is the third time in this programme that a session has declared "no access" from a search
> that did not cover where the evidence actually was.** The project memory records the 2026-09-03
> Asset session concluding "no source code or database access exists" after searching only its working
> tree. The rule derived then — *report negatives with their scope attached, never as absolutes* —
> was written down, was available, and was still not applied here. Writing the rule is evidently not
> sufficient to make it operate; only a directive that forces the search has worked.

### `RE-08` — a shell-glob defect recurred, in a second form

The original round's `RE-06` was an unquoted `--include=*.py` expanded by zsh. This continuation hit
the same class again in the clean-room scan: an unbounded token `quant` matched the ordinary English
word *quantity*, reported as a vendor-token leak. Re-run with `\bquant\b` the count was zero.
Recorded at `18 §6` rather than silently dropped.

**Both instances share one root cause: a pattern that does not mean what its author intended, and no
second form run to catch it.** The standing control adopted after `RE-06` — *a zero result is never
accepted without re-running the same query in a second form* — was applied to zero results, but
`RE-08` was a **non-zero** false positive, which that control does not cover. The control is
extended: **a surprising result in either direction is re-run in a second form.**

### `RE-09` — the peer-session table went stale during execution

Recorded at commit `9b1006b`. The table said P01/P02/P03 had no committed output; five peers pushed
while the session ran. Accurate when written, wrong at publication. Corrected in `12 §3`.

## 2. Revisions Forced by the New Evidence

| ID | Revision | Effect |
|---|---|---|
| `GR-04` | `U-01` re-dispositioned from `BOSS DECISION REQUIRED` (a blanket unknown) to **PARTIALLY RESOLVED** — resolved for the deployed estate at class A, `HOLD — DATABASE EVIDENCE REQUIRED` for the v18 target at class D. | `24 §5` |
| `GR-05` | `U-02` split into a database half (**closed**) and a runtime-execution half (**`HOLD — RUNTIME EVIDENCE REQUIRED`**), with the specific write authorisation named rather than assumed. | `25 §6` |
| `GR-06` | **Severity inversion.** Two axes introduced — `DEFECT STATUS` and `REACH`. Six boundaries reclassified `LATENT`; the purchase-advance and WHT boundaries reclassified `LIVE`. **No boundary was closed on deployment evidence**, and the position defending that is stated at `26 §2`. | `26` |
| `GR-07` | `TX-13`, `TX-20`, `TX-15` promoted from `SUPPORTED INTERPRETATION` to `FACT VERIFIED` **for the v16 database only**; the v18 inference is held at `SUPPORTED INTERPRETATION` and explicitly **not** upgraded. | `25 §3-§4` |
| `GR-08` | `HE-08` (non-deductible) re-dispositioned from a reported gap to `NOT APPLICABLE — EVIDENCE VERIFIED`. | `28 §3` |
| `GR-09` | `EC-07` measured against its quoted definition rather than asserted: the counter reads **0 of 2**, and the reason is structural — pass 1 was not clean, so even a clean pass 2 gives one clean pass, not two consecutive. | `29` |

## 3. What This Continuation Did **Not** Do

Per the continuation directive: no reset, no restart at L1, no discarded evidence, no re-run of
unaffected research. Preserved unchanged: all source findings and citations (`01`–`13`), the original
four challenge verdicts and the 18 brief errors they found (`16`), the 20 typed contradictions and 6
self-corrections (`11`, `15`), the `CORR1` revalidation (`22`, confirmed in `31`, not re-derived),
and the full commit lineage.

## 4. Corrections Made to the Continuation's Own Artefacts

Recorded after the four fresh AAS-03 challenges reported; see `36 §3`.

## 5. Standing Method Controls, updated

| Control | Origin | Status |
|---|---|---|
| A zero result is re-run in a second form | `RE-06` | in force; **extended by `RE-08`** to any surprising result |
| Declare POPULATION + PATTERN + PATH SET + UNIT for every enumeration | project standard | in force; the unit omission was itself caught by a reviewer (`16 §3` #14) |
| Never upgrade a class B/C/D negative to class A | project standard | in force |
| **Search for evidence at rest, not only for live access** | **`RE-07`, new** | **adopted.** Before any "no access" claim: enumerate dumps, exports, snapshots and archives, and state the search boundary. |
| Independent review inside the phase, disjoint, adversarial, briefed to report errors in the brief | project standard | in force; produced 18 brief errors in round 1 |
