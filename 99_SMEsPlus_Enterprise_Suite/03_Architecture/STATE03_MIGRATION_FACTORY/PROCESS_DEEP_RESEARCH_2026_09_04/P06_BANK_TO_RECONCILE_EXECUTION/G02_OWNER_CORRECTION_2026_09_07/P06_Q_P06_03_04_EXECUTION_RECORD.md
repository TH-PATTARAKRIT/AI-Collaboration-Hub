# P06_Q_P06_03_04_EXECUTION_RECORD.md

**Dispatch:** PHASE S — OWNER CORRECTION DISPATCH, items `Q-P06-03` and `Q-P06-04`
**Authorization:** `PHASE-S/Q-BOSS-01 = APPROVED`, verified at `audit/account-phase-s-closure-2026-09-06-001` @ `1bf9b40`
**Queue:** `07_OWNER_BOUNDED_CORRECTION_QUEUE.md` @ `audit/account-xrecon-2026-09-06-001` `3291210` (`07_`/`08_` byte-identical at the current head `2af14d4`)
**Track:** P06 — SOURCE, branch `research/account-p06-bank-to-reconcile-2026-09-04-001` @ `1b018c1`
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 0. Surfaces re-verified before starting

| | Required | Measured | |
|---|---|---|---|
| Source branch head | `1b018c1` | `1b018c104001eb4683166518a6161a8cd8ab5cee` | **UNMOVED** |
| IEV branch head | `b423eff` | `b423eff…` at start | **UNMOVED** |
| Working tree | clean | 0 dirty | **CLEAN** |

**No audit-branch file was touched from here.** The IEV items were executed separately on `audit/p06-independent-verifier-2026-09-06-001`.

## 1. `Q-P06-03` — **REPAIR EXECUTED. COMPLETION GATED on `RC-04`.**

Every count re-executed at publication. **Command and output published, not a total.**

| # | File | Was | Now | Command re-executed at publication | Output |
|---|---|---|---|---|---|
| 1 | `13_`:94 | `~~58~~ → 65` | **67** | `grep -oh 'P06-B-[0-9]\+' *.md \| sort -u \| wc -l` *(the row's own printed command)* | **67** |
| 2 | `13_`:95 | **66** | **68** | `grep -oh 'P06-OQ-[0-9]\+' *.md \| sort -u \| wc -l` *(the row states "same")* | **68** |
| 3 | `46_`:124 | *"returns 65 on the current tree"* | **67** | `grep -oh 'P06-B-[0-9]\+' *.md G02_CLOSURE_2026_09_06/*.md \| sort -u \| wc -l` | **67** |
| 4 | `18_`:214 | *"three vetoes"* · 65 blockers | **seven vetoes** · **67 blockers** | `grep -oh 'AASP-VETO-[0-9]\+' *.md G02_*/*.md \| sort -u` | `AASP-VETO-01…07` = **7** |
| 5 | `70_`:108 | *"four active vetoes"* · 65 blockers · *"16 recorded author errors"* | **seven** · **67** · **21** | as above, plus the author-error enumeration below | |
| 6 | `40_`:288 | **23** author errors | **21** | see §1.1 | **23 ids, 21 defined** |
| 7 | `40_`:188 `P06-B-58` | *"16 author errors"* | **21** — **RE-SCALED** | inherits §1.1 | |

**`13_`:95 was in no prior correction population** — it is `IEV-D-19`, an untouched row one line below a repaired one, using the same command.

### 1.1 The author-error count — the unit, enumerated

```
distinct REV-E-* identifiers                  → 23
of which carry a definition line in any file  → 21
undefined: REV-E-22, REV-E-23
```
**`REV-E-22` and `REV-E-23` are repair-marker families applied BY the verification and recovery rounds — not author errors.** `40_`:288's row is headed *"Author errors"*; **the unit is author error, not identifier.** Corrected to **21**, with the identifier count retained in the cell so both are legible.

### 1.2 Verification — no stale figure survives as a current claim

```
"→ **65 blockers"          uncorrected → 0
"| **66** |"               uncorrected → 0
"three vetoes"             uncorrected → 0
"four active vetoes"       uncorrected → 0
"16 recorded author errors" uncorrected → 0
"| 22 | **23** |"          uncorrected → 0
```
Superseded wording is struck through and retained in every case.

### 1.3 Downstream notification — **ISSUED**

`18_` and `70_` are the two P11-bound handoffs and both carried wrong figures. **P11 is notified in writing at `G02_OWNER_CORRECTION_2026_09_07/P06_TO_P11_COUNT_CORRECTION_NOTICE.md`. P11's package was not edited.**

## 2. `Q-P06-04` — **REPAIR EXECUTED. COMPLETION GATED on `RC-04`.** And the negative did not survive.

### 2.1 The published search could not fire — demonstrated, both modes

The pattern at `56_`:99 was published with **no command, no `-E`/`-F` flag and no path expression**.

```
fixture: "dishonour cheque" / "dishonor cheque" / "dishonou?r literal"
  BRE  'dishonou?r'                       → 1   (the LITERAL line only; '?' is not a metacharacter in BRE)
  ERE  whole original pattern             → 0   ('\|' is a literal pipe in ERE — the alternation is dead)
  ERE  corrected 'dishonou?r'             → 2   (both real spellings; the branch fires once corrected)
```

### 2.2 The re-run — population unchanged, controls stated

```
POPULATION  $V18E/../addons_archive — 961 directories (declared; NOT widened)
TOOL/MODE   /usr/bin/grep -rlE   (ERE, stated explicitly)
COMMAND     /usr/bin/grep -rlE 'payment_return|bounce|dishonou?r|post_dated|postdated' $AR
RESULT      76 files
PER BRANCH  payment_return 0 · bounce 66 · dishonou?r 10 · post_dated 0 · postdated 0
POSITIVE CONTROL, INSIDE THE POPULATION   'bounce' → 66 files
NEGATIVE CONTROL                          impossible token → 0 files
WIDENED SPELLING, same population         'post-dated' (hyphenated) → 2 files
```

### 2.3 The result overturns the finding

**`FTB-F-07` is withdrawn as published and restated.** Three artefacts the dead pattern could not see:

| Concept | Artefact | What it is |
|---|---|---|
| Dishonoured payment | `l10n_nz_eft/models/account_batch_payment.py` — `l10n_nz_dishonour_account_id = fields.Many2one(…)`, help *"fallback account in case of dishonored payment"* | **a real ORM field**, with a view and a test |
| Dishonoured instrument | `l10n_kr/data/template/account.account-kr.csv` — account `121504` *"dishonored bills and checks"* | a chart-of-accounts row |
| Post-dated cheque | `l10n_latam_check/__manifest__.py` — *"'Check Cash-In Date' for **post-dated checks**"* | a module feature |

**Restated boundary:** the concepts **exist in the v18 distribution, in `addons_archive` only**. `odoo.conf:67` excludes `addons_archive`; `l10n_nz_eft` is absent from the 791 loadable addons. **Not missing from Odoo 18 — missing from this deployment's loadable set.**

**`P06-B-34` / `P06-B-35`: FLAGGED, NOT DISPOSED.** Their basis becomes *"absent from the loadable set"*, not *"absent from the distribution"* — a weaker claim with a different remedy. **`Q-P06-04` authorises restating `FTB-F-07`, not re-adjudicating the blockers it feeds. Routed to the owner.**

## 3. What was NOT done

**`RC-04` was not run, not selected and not self-satisfied**, for either item. Boss ruling `XRECON/Q-BOSS-01` (`XRD-009`) = **NOT SATISFIED**; `PHASE-S/Q-BOSS-02` is raised and unanswered. **Both items' completion conditions are unmet by ruling, not by omission.**

**`AASP-VETO-07` remains PRESERVED.** No research finding was re-opened beyond the one restatement `Q-P06-04` explicitly authorises. No root was widened. No peer package was edited.
