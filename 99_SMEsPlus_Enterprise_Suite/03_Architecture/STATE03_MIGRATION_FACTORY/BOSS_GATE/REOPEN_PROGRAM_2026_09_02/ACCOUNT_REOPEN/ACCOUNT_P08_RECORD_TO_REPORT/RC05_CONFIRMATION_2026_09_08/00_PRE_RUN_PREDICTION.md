# P08 RC-05 CONFIRMATION — PRE-RUN PREDICTION AND FROZEN CONTROL SET

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` §7 · item **`P08-C3`**
**Owner:** P08 Record-to-Report · **Baseline:** `e368d11da6f7e4973469ff5608d676ec2d13811c`
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 0. What this file is, and why it exists as its own commit

`RC05-F3` did not challenge the balance result. It challenged the **provenance of the control**:

> *"The package asserts `EXPECTED_CONTROL_BEHAVIOUR.md` was hashed before first execution at `2026-09-07T11:40:26+0700`. In repository history, the expected-behaviour file, instrument, owner run outputs, manifest, the hash, and that timestamp first appear together in commit `e368d11` at `11:45:05+0700`. Git alone does not establish that the prediction was immutably frozen before the run."*

**That challenge is accepted, and it is not answerable by argument.** No wording added to `EXPECTED_CONTROL_BEHAVIOUR.md` can make Git prove something Git did not record. The only repair is to **do it again, visibly**:

1. this file and the one new instrument are committed **alone**, with **no run output of any kind**;
2. that commit's SHA and this file's content digest are recorded **in the result file, not here**;
3. only then is anything executed;
4. the results land in a **later commit**, whose parent is the prediction commit.

**Ancestry, not assertion.** A reader checks `git log` and sees an empty-of-results commit preceding a results commit. If the results had been written first, the graph would show it.

> **The prediction commit cannot contain its own SHA.** That is why the linkage is recorded in the *result* file pointing backwards, and why this file names no commit.

## 1. The instrument set, frozen here

| Instrument | SHA-256 | Status |
|---|---|---|
| `RC05_REPRODUCIBILITY/instrument/rc05_balance.py` | `2151cd445a4ddb11df7b86315bcaf46b17035d7f29b62adc38ece1b00a2c9ea1` | **UNCHANGED** from `e368d11`; matches the RC-05 manifest byte for byte |
| `RC05_CONFIRMATION_2026_09_08/instrument/module_state.py` | `22f348a1d064f7b52c9d515758363f5ef83e6587d2d2463b171d9043b79b3212` | **NEW — delta disclosed below** |

**Disclosed delta.** `module_state.py` is new because `P08-C4` requires an install-state answer over the **four** frozen inputs and no published instrument produced one. It reads `ir_module_module` and shares exactly two properties with the balance instrument — **columns resolved by name from each dump's own COPY header**, and **fail-closed on a missing table or column**. It distinguishes three outcomes that a naive check collapses into two: `state='installed'`, a row in some other state, and **NOT PRESENT** (no row at all). **Reporting "not installed" for a module the database never knew is the defect it exists to avoid.**

## 2. Frozen inputs — four extracts, and what they are NOT

| Label | Path | Size (bytes) |
|---|---|---:|
| `DB-SM` | `/Users/admin/Downloads/iSMEs_2026-07-11_05-03-27.dump` | 155,443,710 |
| `DB-BK` | `/Users/admin/Downloads/BK12MAY26_2026-08-03_05-48-30.dump` | 35,679,594 |
| `DB-EV` | `/Users/admin/Downloads/iEVING_2026-07-23_10-31-06.dump` | 24,911,161 |
| `DB-T2` | `/Users/admin/Downloads/iTEST02_2026-07-14_16-34-51.dump` | 64,303,340 |

**These are four frozen RC-05 database extracts. They are NOT established to be the complete deployed estate,** and nothing produced from this run may be worded as if they were. `DB-T2` is a fourth extract that entered the frozen population at RC-05 preparation; whether the deployment population is exactly four is **unproven and is not tested by this run**.

## 3. The predictions — each stated so that it can be wrong

### 3.1 Reproduction predictions (values taken from `RUN_4` at `e368d11`)

These are **not** discoveries. They pre-register that an **unchanged instrument, on unchanged inputs, under a different `pg_restore` major version** returns the same numbers. Falsified by any single cell differing.

| DB | posted moves with lines | posted lines | unbalanced COMPUTED @ exact/1e-7/1e-4/0.005 | unbalanced STORED @ same | PARENT_STATE_DISAGREE |
|---|---:|---:|---|---|---:|
| `DB-SM` | **169,143** | **417,700** | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | **0** |
| `DB-BK` | **16** | **563** | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | **0** |
| `DB-EV` | **6** | **15** | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | **0** |
| `DB-T2` | **5** | **14** | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | **0** |

Input digests are predicted to equal those recorded in `RUN_4`:
`DB-SM ca77818b…`, `DB-BK 1a673474…`, `DB-EV eade5512…`, `DB-T2 84a75479…`.
**A digest mismatch falsifies every downstream number in this file** and would mean the frozen inputs are not frozen.

### 3.2 Control predictions

| # | Control | Predicted BEFORE the run |
|---|---|---|
| C1 | injection `0.01` on `DB-T2` | unbalanced rises **0 → 1 at all four tolerances** (0.01 exceeds every one of them) |
| C2 | injection `0.001` on `DB-T2` | **0 → 1 at exact, 1e-7, 1e-4** and **0 at 0.005** — the tolerance boundary must be visible, not asserted |
| C3 | missing input path | exit **2**, `FAIL-CLOSED: input not found` |
| C4 | a real file that is not a PostgreSQL archive | exit **3**, `no COPY block for table account_move` — **an unreadable extract must never read as an empty ledger** |
| C5 | `PATH` emptied of `pg_restore` | exit **2** |
| C6 | two consecutive clean four-DB runs | **byte-identical** after stripping the tool-version banner |
| C7 | `pg_restore` **16.15** vs **18.6**, same four inputs | **identical** balance figures; the banner line is the only permitted difference |
| C8 | positive control, every DB | `sum(\|debit\|+\|credit\|)` **> 0** — a zero means the extraction failed, not that the ledger balances |
| C9 | discriminating set (non-posted entries) | printed for all four DBs whether zero or not |

### 3.3 The genuinely open prediction — install state, four inputs

**The owner does not know this answer at the time of writing.** `E00_EVIDENCE_BASE_AND_ROOT_SET.md`:132 records `om_data_remove` as **installed** in three databases and has no column for a fourth; `RC-05` reports that `DB-T2` shows it installed but P08 has not executed that itself.

> **Prediction:** `om_data_remove` resolves to **`state='installed'` in all four extracts.**
>
> **Falsified by:** any extract returning `NOT PRESENT`, or a row in any state other than `installed`.

Two further modules are read in the same pass as **discriminating controls**, chosen because their expected answers differ from each other:

> **Prediction:** `account` (the base accounting module) is **`installed` in all four** — if it were not, the ledger tables the balance instrument reads would not exist, so this is a **coherence check on the whole run**.
>
> **Prediction:** `smesplus_nonexistent_control_module` is **`NOT PRESENT` in all four.** This is the negative control: it proves the reader can return the *third* answer and is not simply reporting whatever it is asked about. **Without it, "installed" is indistinguishable from "the reader echoes its argument."**

### 3.4 What this run does NOT claim, whatever it returns

- It does **not** establish that four extracts are the complete deployed estate.
- It does **not** establish that `om_data_remove` was ever **executed** anywhere. Install state is capability, not act. `P08-HO-13` stays **capability confirmed, execution NOT evidenced**.
- It does **not** discharge any Veto.
- It is an **owner** confirmation run. It is not RC-05, and it is not independent.

---

**Nothing in this file is a result.** The next commit that touches this directory contains the results, and its parent is this commit.
