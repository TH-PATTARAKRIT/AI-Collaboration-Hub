# P06_TARGETED_CLOSURE_AUTHOR_ERROR_REVISION.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S18)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Continues:** `14_` (round 2, REV-E-01…04) and `39_` (round 3, REV-E-05…08). **Neither is superseded.**

> This round recorded **six** further author errors, and **four of them overturn conclusions this package published**. That is the highest correction rate of any P06 round, and it is a consequence of two things: peer packages arriving, and searches that round 3 declared unnecessary being run.

---

## REV-E-09 — The authorisation conclusion was right for the wrong reason

**Original** (`20_` Appendix A, CMD-F-18): *"The methods are plain `type="object"` handlers on `res.config.settings`, **a `TransientModel` with a broad default ACL**."*
**Wrong denominator:** the ACL was asserted without reading `ir.model.access.csv`.
**Command that exposed it:** `grep -n "model_res_config_settings" $V18E/base/security/ir.model.access.csv` → **one row, `base.group_system`, and `unlink` is 0** — the narrowest grant in the system.
**Corrected result:** the conclusion (`NO SERVER-SIDE AUTHORIZATION VERIFIED`) **stands**, on a different and stronger basis: *the path never performs an ORM operation on its own model, so the model's permissions are never invoked.*
**Why it matters more than a footnote:** under the wrong reasoning the remedy would be *"tighten the ACL"* — which would achieve **nothing**. `45_` §3.

---

## REV-E-10 — The v19 source tree existed and was not searched

**Original** (`24_` DME-F-03, `40_` `B-44`): the generation gap framed as unanswerable without a database export, on the premise that only v19 *deployment* evidence existed.
**Wrong boundary:** round 3 searched `~/Downloads` and the v18 tree. It did **not** search the workstation for a v19 source tree.
**Command that exposed it:** `find /Volumes/iMacSys -maxdepth 4 -type d \( -iname "*odoo-19*" -o -iname "*19.0*" \)` → **five hits, including a complete Odoo 19 Enterprise tree named `SMEsPlus19`** (`version_info = (19,0,0,FINAL,0)`, 1422 addons, 514 l10n).
**Corrected result:** six core P06 findings re-tested against v19 — **all six cross-version invariant** (`51_` §2). The research risk `B-44` implied is **measured and largely retired**; `B-44` severity **HIGH → MEDIUM**.
**This is the third time in the P06 programme a conclusion rested on an unsearched evidence base.**

---

## REV-E-11 — The `is_matched` branch count was wrong, and internally inconsistent

**Original:** `25_` said *"Three branches"*; `35_` said *"the same four-branch mechanism"*; **the same package said both.**
**Command that exposed it:** a peer's citation. P02 published *"four branches"* over `:428-456`. Re-printing `$V18E/account/models/account_payment.py:427-457` line by line gives **four top-level branches (`:436`, `:439`, `:442`, `:445`) and five assignment sites.** `25_` had silently omitted `:439-441`.
**Corrected result:** finding **strengthened** — of five sites, **two assert `is_matched = True` unconditionally with no statement**, one asserts it circularly, one is always False, and **only one tests anything resembling a bank match**.
**P06 did not catch this by re-reading itself.** A peer's number did.

---

## REV-E-12 — Two denominators from different processes were summed

**Original** (`35_` PH-F-05, `40_` `B-53`): *"P05 supplies an **eighth** settlement door P06 did not count."*
**Wrong unit:** P06's 7 counts **bank-event ingestion doors**; P05's 7 counts **expense settlement paths**. Different units, different populations. And **P05 had already counted `SR-04` as path 5 of its own 7** — P06 implied P05 had missed it.
**Corrected result:** *"eighth door"* **withdrawn**. `B-53` restated as inherited from P05, severity LOW to P06, flagged for P11 deduplication. **The substantive finding survives intact** (`55_` SDD-F-04): cash moves through a bank journal with no payment object, and P06's matching model keys on payments.
**Fourth instance of the `count unit vs population` defect in this programme.**

---

## REV-E-13 — The copy denominator was 4; it is 17

**Original** (`20_`, `44_`): *"present in all four custom roots"*.
**Wrong population:** four roots were **declared**, so four were **searched**.
**Command that exposed it:** `find /Volumes/iMacSys -type d -name "om_data_remove"` → **17 directories**, across four Odoo generations, plus two zips and a staging folder.
**Corrected result:** the statement was true and **materially understated**. Seven copies carry `19.0.1.x` — matching the installed version — and **three are rebranded `SMEsPlus Remove Data`, two of them inside this programme's own `SMEsPlus ENTERPRISE SUITE/ACCOUNT/` workspace.**
**A declared path set is not a population.** The path set was declared honestly; the question it was answering was "which of these four has it", not "where does this exist".

---

## REV-E-14 — The sequence-rewind damage was attributed to the wrong mechanism

**Original** (`20_` CMD-F-17, `40_` `B-50`): *"then rewinds the bank/cash/invoice sequences to 1"*, presented as the cause of renumbering.
**Wrong mechanism:** v18 does **not** number journal entries from `ir.sequence`. `account.move` uses `sequence.mixin`, which derives the next number by **querying the table for the greatest existing name** (`sequence_mixin.py:267-300`, `account_move.py:3479-3500`). PATTERN `ir\.sequence` over `$V18E/account`: **4 hits, none journal numbering.** The prefixes the module targets (`BNK1/`, `INV/`, `MISC/`…) are **v12/v13-era artefacts**.
**Corrected result:** the `ALTER SEQUENCE … RESTART WITH 1` is real but **largely inert against v18 accounting**. The renumbering is caused by **`delete from account_move` emptying the table the numbering reads**.
**The corrected finding is worse:** it cannot be prevented by protecting `ir.sequence`, it is silent, and it applies to every `sequence.mixin` consumer. `61_` SRF-F-06.
**A remediation built on the round-3 wording would have protected the wrong object.**

---

## REV-E-15 — The bytecode evidence was misread

**Original** (`49_` REACH-F-03): *"three of the four copies have at some point been on an `addons_path` of a running interpreter."*
**Wrong method:** file `mtime` was read; the **PEP-552 header** was not.
**What the header decode shows:** every embedded source mtime is **2022 or 2024** — years before the 2026 file mtimes — and one CUST14 `.pyc` encodes a source size (12,701 B) that **matches no file on the volume**. These `__pycache__` directories were **shipped inside vendor archives and copied with the source**. None evidences a local import.
**The one genuine local compilation** is `om_data_remove_fix`, whose `.pyc` embedded mtime **exactly matches** its `.py` and was written two minutes later — CPython 3.10, 2026-05-27, Asia/Bangkok.
**Corrected result:** the bytecode claim is **withdrawn**. It was weak evidence read weakly. The installation evidence is **registry evidence** (`58_`), and it is far stronger.

---

## REV-E-16 — The "filtered distribution" finding was substantially wrong

**Original** (`38_` UER-F-03, `P06-B-55`): *"the v18 tree has been filtered to the Thai deployment … 791 addons, 2 localisation packs."*
**Wrong conclusion from a right observation.** The counts were correct. The **inference** was not: the localisations were not *removed*, they were **relocated**.
**What was missed:** `$V18E/../addons_archive/` holds **961 directories, 904 of them `l10n_*`** — and the project's own `odoo.conf:14` states, in Thai, *"addons_archive must not be in addons_path"*. **`l10n_th` and `l10n_th_reports` are NOT in the archive** — the Thai packs were deliberately promoted to the live path and the rest archived.
**Corrected result, and it splits in two:**
- **For any claim about the *loadable* population, 791 is correct** and every negative scoped to it stands. That is the population that runs.
- **For any claim about "Odoo 18", the population is 791 + 961 = 1752**, and **904 localisation packs were reachable on disk and were not searched.**

**And re-running the negatives against the archive found one real hit.** PATTERN `commission_amount|bank_fee|bank_charge|transaction_fee|merchant_fee|processing_fee` over 961 archived modules: two `commission_amount = fields.Monetary()` field definitions, in an archived marketplace connector (`sale_amazon`, **not on the live addons path**), plus chart-of-account rows in `l10n_fr` / `l10n_lu`.
**This does not overturn `B-17`** — a marketplace commission is not a bank fee, and the module is not loadable. **But it narrows the permitted wording:** the claim is *"no bank fee, interest or commission concept in the loadable v18 population"*, not *"no commission field exists in Odoo 18"*. `57_` amended.
**Returned/bounced concepts in the archive: NOT FOUND** — the hits are email-bounce and SMS tracking. `B-34`/`B-35` survive the enlarged population.

---

## Consolidated error record

| # | Round | Defect | Detected by | Effect |
|---|---|---|---|---|
| REV-E-01 | 2 | denominator misstated (6 vs 7 doors) | independent pass | corrected |
| REV-E-02 | 2 | count asserted before execution | executing it | corrected |
| REV-E-03 | 2 | four unbounded negatives | named audit step | repaired |
| REV-E-04 | 2 | source tree ambiguity accepted | register assembly | flagged |
| REV-E-05 | 3 | two units summed | executing the count | corrected |
| REV-E-06 | 3 | arithmetic + unit + unrun command | executing it | corrected |
| REV-E-07 | 3 | executable gap deferred | reconsideration | executed |
| REV-E-08 | 3 | counts went stale before close | re-running at close | corrected |
| **REV-E-09** | **4** | **right conclusion, wrong reason** | **reading the ACL file** | **reasoning replaced** |
| **REV-E-10** | **4** | **v19 tree unsearched** | **one `find`** | **6 findings re-tested, `B-44` downgraded** |
| **REV-E-11** | **4** | **branch count wrong and self-inconsistent** | **a peer's citation** | **finding strengthened** |
| **REV-E-12** | **4** | **two denominators summed** | **reading P05's own table** | **claim withdrawn** |
| **REV-E-13** | **4** | **copy population 4 → 17** | **one `find`** | **materially understated** |
| **REV-E-14** | **4** | **damage attributed to the wrong mechanism** | **reading `sequence.mixin`** | **finding worsened** |
| **REV-E-15** | **4** | **bytecode misread** | **PEP-552 header decode** | **claim withdrawn** |
| **REV-E-16** | **4** | **"filtered" was "relocated"** | **listing `addons_archive`** | **scope split; 904 packs searched** |

**16 author errors across four rounds.**

| Detected by | Count |
|---|---|
| Independent pass (subagent, peer package) | **6** |
| Executing a command the author had only declared | **6** |
| Author, unaided | **4** |

**Twelve of sixteen were caught by something other than the author re-reading their own work.** The pattern is stable across four rounds and it is the single most reliable finding this programme has about its own method.

---

## The recurring defect, named once

**Ten of the sixteen are the same defect in different clothes: a boundary drawn and then not stated, or stated and then not executed.**
- REV-E-01, 05, 06, 08, 12, 13 — population or unit
- REV-E-02, 07 — declared and not run
- REV-E-10, 16 — evidence base assumed rather than measured

**The remedy is not more care. It is the discipline this package already states and repeatedly failed to apply: run the command, print the count, name the population, and do it last.**
