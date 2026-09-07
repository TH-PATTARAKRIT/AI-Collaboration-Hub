# P08 — `RC-05` REPRODUCIBILITY PACKAGE

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-REMEDIATION-002]`
**Authority** Boss ruling `Q-BOSS-03` §2 — *"documentary inspection alone is not sufficient"*
**Base** `corr/p08-phase-s-final-2026-09-07-001` @ `c7cfd8a` — read-only, never rewritten
**Published on** `corr/p08-phase-s-rc05-prep-2026-09-07-001`

> ## THIS IS NOT `RC-05`, AND NOTHING HERE CERTIFIES IT
>
> The owner ran the instrument **only to establish that it executes and that its controls fire**.
> That is **preparation evidence** and it **cannot satisfy structural independence** — `XRD-009`
> settled that a verification by the model that authored the repair is not a verification.
> **The independent verifier must re-execute this instrument and reach a conclusion without relying
> on any number below.** The owner's figures are published so they can be **contradicted**.

---

## 1. What the closeout said was missing, and what is now supplied

| Required by `Q-BOSS-03` §2 | Status at `c7cfd8a` | Status now |
|---|---|---|
| executable instrument / exact procedure | **absent — the surface carried no executable file at all** | **`instrument/rc05_balance.py`**, 264 lines |
| frozen reproducible inputs | **not established** | **4 dumps located on the host, SHA-256 below** |
| SHA-256 per frozen input | absent | **§3** |
| population / unit / denominator | stated in prose only | **§4 — printed by the run itself** |
| predicates, computed **and** stored balance | prose figures | **§5, both columns, every run** |
| Decimal / tolerance semantics | asserted | **§5 — `Decimal`, prec 60, no float constructed at any step** |
| positive control | **not established** | **§6.1** |
| negative control | **not established** | **§6.2** |
| failure / discriminating control | **not established** | **§6.3 — injection, graded across the tolerance ladder** |
| expected behaviour **before** execution | absent | **`EXPECTED_CONTROL_BEHAVIOUR.md`, written and hashed before the first run** |
| invocation + output schema | absent | **§7** |
| immutable evidence SHA | — | **§9** |

## 2. The evidence was on the host — the closeout's caution was right

`10_` §3 recorded that the P08 surface *"does not carry"* the instrument and inputs, and warned
explicitly: **"Do not read item 2 as 'the evidence does not exist' … Sweep before concluding absence."**

**The sweep found all four dumps.** They are not in the repository and not in any session clone; they
are in **`/Users/admin/Downloads/`**.

**PATH SET swept, declared in full:** every `/Volumes` entry — `/Volumes/iMac`,
`/Volumes/iMacSys`, `/Volumes/ChatGPT Installer` — and `$HOME` (`/Users/admin`).
**PATTERN:** exact filename; then `*.dump`/`*.sql` by extension; then **`PGDMP` magic bytes on every
file over 4 MB**, because extension is not format.
**DECLARED EXCLUSION:** `~/Library` was pruned (≈855 application-data directories, each a TCC
consent prompt). **This is stated as an exclusion, not omitted** — a blanket `~/Library` prune has
previously hidden whole source distributions from three sweeps in this programme. **If the verifier
needs certainty about that subtree, it is unswept and this package says so.**

**Had the sweep not been run, this package would have declared the evidence missing — and been
wrong.** `P08-RC05-PREP-C` is **NOT** raised.

## 3. Frozen inputs

| Label | File | Bytes | SHA-256 |
|---|---|---|---|
| `DB-SM` | `/Users/admin/Downloads/iSMEs_2026-07-11_05-03-27.dump` | 155,443,710 | `ca77818b6daa1184199018add4e695cb75112e25608b0a664bfbf3ada5118ae2` |
| `DB-BK` | `/Users/admin/Downloads/BK12MAY26_2026-08-03_05-48-30.dump` | 35,679,594 | `1a67347491a056d1e86675568a68473aa239c96396988d21493b805970e151a3` |
| `DB-EV` | `/Users/admin/Downloads/iEVING_2026-07-23_10-31-06.dump` | 24,911,161 | `eade5512bbab1bd06f4f3a521c9468eadc08facaeb7e551631ae51be3a85cb0f` |
| **`DB-T2`** | `/Users/admin/Downloads/iTEST02_2026-07-14_16-34-51.dump` | 64,303,340 | `84a75479e432be21bc23e4986821f0307e4035e97d6398985ee5de52adb837a4` |

**All four are PostgreSQL custom-format archives (`PGDMP`), read with `pg_restore -f -`. No server is
started and no database is created; the archives are opened read-only.**

> ### `DB-T2` — `P08-U-22` closed, and the population was one database short
>
> P08 carried a *"fourth deployed dump — **still unread**"* as `P08-U-22`, *"declared unreadable by
> one tool and not retried."* **It is readable.** `pg_restore` **16.15** fails with
> *"unsupported version (1.16) in file header"*; `pg_restore` **18.6**, installed on the same host at
> `/opt/homebrew/opt/postgresql@18/bin`, reads it — **26,815 TOC entries, 165 `account_*` tables**.
> The archive was written by a newer `pg_dump` than the tool that was tried.
>
> **The negative was about the tool, not the artefact**, and it stood unretried for a full round.
> **`RC-05`'s population is four databases, not three** — and P08's claim is scoped *"in any deployed
> database."* **`DB-T2` is included below.**
>
> **Positive control for that probe:** the identical command returns **162** `account_*` tables on
> `DB-EV`, so the `0` on `DB-T2` under `pg_restore` 16 was a tool failure and is distinguishable
> from an empty archive.

## 4. Population, unit, denominator

| | |
|---|---|
| **POPULATION** | every `account_move_line` whose `move_id` resolves to an `account_move` with `state = 'posted'`, in the named extract |
| **UNIT** | **one accounting entry (`account_move`)** — not one line, not one journal |
| **DENOMINATOR** | posted moves having at least one line, printed per database as `POSTED_MOVES_WITH_LINES` |
| **SCOPE** | **reporting currency.** `debit` / `credit` / `balance` are company-currency columns here. `amount_currency` is out of scope and is not read |
| **COMPANY** | not partitioned — every company in the extract is in the population |

**The authority for "posted" is `account_move.state`, joined to.** `account_move_line.parent_state`
is a stored related field and can be stale, so it is **not** used as the filter; instead the
instrument counts lines whose `parent_state` disagrees with the authority and prints it
(`PARENT_STATE_DISAGREE`). **It is 0 in all four databases** — reported as an observation, not as a
control that passed.

> **A named uncertainty, settled by the run rather than by the owner.** P08 states the figure as
> *"across **169,143**"* **without naming its unit**, and this package predicted, in writing and
> before executing, that the run might show `169,143` to be **lines** rather than **entries** — which
> would have made P08's denominator wrong in unit. **It did not.** `POSTED_MOVES_WITH_LINES` is
> **169,143** and posted *lines* are **417,700**. **P08's unit is correct.** Recorded because the
> check could have found a defect and did not, and a control only reported when it fires is not a
> control.

## 5. Predicates and exact semantics

For each posted entry, two **independent** sums, both exact:

```
COMPUTED   Σ(debit) − Σ(credit)      the derived balance
STORED     Σ(balance)                the stored balance column
```

An entry is **UNBALANCED at tolerance `t`** when `abs(sum) > t`, evaluated at
**`t = 0` (exact equality)**, `1e-7`, `1e-4`, `0.005`.

**Arithmetic:** Python `decimal.Decimal`, context precision **60**. Every value is constructed from
the COPY text token directly into `Decimal`; **no `float` is constructed at any step**, so no
representation error can enter and then be attributed to the data. `NULL` (`\N`) reads as `0`.

**Schema is resolved by name, never by position.** The deployed generations differ — `DB-SM` is
**16.0** and carries `account_root_id` and `tax_audit`; `DB-BK`/`DB-EV`/`DB-T2` are **19.0** and carry
`invoice_date` and `extra_tax_data` instead — so **column order is not the same between extracts**.
Column indices are read from each dump's own `COPY` header and the instrument **fails closed** if a
required column is absent. **Positional parsing here would read a real number out of the wrong column
and return a plausible answer that passes every control.**

## 6. Controls — and what each one can detect

### 6.1 Positive — the extraction reached real data
Non-zero posted lines and non-zero `Σ|debit|+|credit|` in every database
(`DB-SM` **278,703,722,656.58**; `DB-BK` 29,420.00; `DB-EV` 1,600.00; `DB-T2` 1,832.08).
**Without this, a `0 unbalanced` is indistinguishable from a pipeline that read nothing.**

### 6.2 Negative / discriminating population
`DB-BK` (**16** posted entries) and `DB-EV` (**6**) hold **22 between them**, against `DB-SM`'s
**169,143**. The instrument reports radically different populations for databases that **should**
differ. `DB-T2` adds **5**. **Three of the four are near-empty ledgers, and the spread is published
rather than a single headline zero.**

### 6.3 Failure / injection — the only proof the predicate CAN fire
`--inject-unbalanced AMOUNT` adds one synthetic entry off by `AMOUNT`.

| Injection | exact | `1e-7` | `1e-4` | `0.005` | Reads |
|---|---|---|---|---|---|
| none | 0 | 0 | 0 | 0 | the measurement |
| **`0.01`** | **1** | **1** | **1** | **1** | fires at every tolerance below 0.01 |
| **`0.001`** | **1** | **1** | **1** | **0** | **fires below `0.005` and stops at it** |

**The graded row is the important one.** It proves not merely that the predicate can return non-zero,
but that **the tolerance ladder itself discriminates** — an instrument that returned `1` at `0.005`
for a `0.001` error, or `0` at exact for any error, would be silently wrong in a way a single
injection could not reveal. Verified on both `DB-EV` and the material `DB-SM`.

### 6.4 Fail-closed
| Condition | Exit | Message |
|---|---|---|
| required column absent | **3** | names the column and the dump |
| table absent / extract unreadable | **3** | names the table and the dump |
| input file missing | **2** | names the path |
| `pg_restore` not on `PATH` | **2** | names the tool |

### 6.5 Discriminating set — the non-posted population
Printed for every database whether zero or not. `DB-SM` carries **14,427** draft/other entries with
lines and **0 unbalanced at every tolerance**; `DB-T2` carries 5, likewise 0.
**A tolerance effect that appears in neither population is not evidence about tolerance**, and
publishing the spread stops a bare zero being read as a finding on its own.

### 6.6 Cross-version control
The three shared databases were measured under **`pg_restore` 16.15 and 18.6** and the outputs are
**identical**. The extraction is not an artefact of one tool version.

### 6.7 Determinism
Two full runs from clean state, **byte-identical output**
(`owner_preparation_run/RUN_1_all_three.txt`, `RUN_2_all_three.txt`).

## 7. Invocation and output schema

```
export PATH=/opt/homebrew/opt/postgresql@18/bin:$PATH      # 18.x required for DB-T2 only

python3 instrument/rc05_balance.py \
    DB-SM=/Users/admin/Downloads/iSMEs_2026-07-11_05-03-27.dump \
    DB-BK=/Users/admin/Downloads/BK12MAY26_2026-08-03_05-48-30.dump \
    DB-EV=/Users/admin/Downloads/iEVING_2026-07-23_10-31-06.dump \
    DB-T2=/Users/admin/Downloads/iTEST02_2026-07-14_16-34-51.dump

# controls
python3 instrument/rc05_balance.py --inject-unbalanced 0.01  DB-SM=...
python3 instrument/rc05_balance.py --inject-unbalanced 0.001 DB-EV=...
```

Per database the run prints: tool versions and Decimal precision · each input's size and SHA-256 ·
`account_move` rows · posted moves · **`POSTED_MOVES_WITH_LINES` (the denominator)** ·
`account_move_line` rows · posted lines · `PARENT_STATE_DISAGREE` · the positive-control money total ·
a 4×2 tolerance table (`COMPUTED` × `STORED`) · the non-posted discriminating set.
**Runtime ≈ 3 s for three databases; no network, no server, no write to any input.**

## 8. The owner's preparation figures — published to be contradicted, not adopted

| Database | Denominator (posted entries) | Posted lines | `COMPUTED` unbalanced @ exact / `1e-7` / `1e-4` / `0.005` | `STORED` same |
|---|---|---|---|---|
| `DB-SM` | **169,143** | 417,700 | **0 / 0 / 0 / 0** | **0 / 0 / 0 / 0** |
| `DB-BK` | 16 | 563 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| `DB-EV` | 6 | 15 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| **`DB-T2`** | **5** | 14 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |

**Consistent with P08's corrected claim** that the balance measurement is **tolerance-independent**,
and consistent with the deletion of the *"at `1e-7` the answer is 3"* figure as having no referent.

> **This does not certify `RC-05` and does not close `Q-P08-01`.** It is one execution by the
> disqualified owner. **`AAS+-PS-VETO-01` `C-6` remains NOT DISCHARGED.** What the owner has
> established is only that **`RC-05` is now executable by someone else** — which is exactly what
> `Q-BOSS-03` required and no more.

## 9. What is NOT covered, stated so it is not assumed

| | |
|---|---|
| **Settlement reconstruction** | P08's `58_` §1 row 2 — **2,354 lines at exact equality, 0 at ≥ `1e-6`** — is a **different measurement over a different table** and **this instrument does not measure it**. It is `SUPPORTED INTERPRETATION` on P08's own marking and is **not** reproduced here |
| **Foreign-currency balance** | `amount_currency` is out of scope by declaration |
| **Per-company partition** | not partitioned; a verifier wanting it must extend the instrument |
| **`~/Library`** | **unswept**, declared in §2 |
| **Whether these four are all deployed databases** | **not established.** The sweep found four; that they are *the* deployed set is P08's prior claim, **not re-verified here** |

## 9a. Proof that the prediction was not written afterwards

`EXPECTED_CONTROL_BEHAVIOUR.md` was hashed **before the instrument was executed even once**, at
`2026-09-07T11:40:26+0700`:

```
8ddac6fc670617fae48d4ace87365d0855ce3fd314012fd8e16d1f5d85c03599  EXPECTED_CONTROL_BEHAVIOUR.md
2151cd445a4ddb11df7b86315bcaf46b17035d7f29b62adc38ece1b00a2c9ea1  instrument/rc05_balance.py
```

**Both hashes are unchanged in `MANIFEST.md`.** Neither the prediction nor the instrument was
edited after any result was seen. **A verifier can check this without taking the owner's word for
it**, and if either hash had moved, the prediction would be worthless.

`RUN_1_all_three.txt` and `RUN_2_all_three.txt` share the hash
`3a13a4cdc761085697249714ed1f5c3f4311990ed0f9305194f68501eec5130b` — the determinism claim in §6.7,
checkable from the manifest alone.

## 10. Standing

| | |
|---|---|
| `P08-RC05-PREP-C` | **NOT RAISED** — the reproducible primary input exists and is named |
| `RC-05` | **READY FOR THE INDEPENDENT VERIFIER — NOT RUN, NOT CERTIFIED** |
| `P08-U-22` | **CLOSED as a tool defect** — `DB-T2` is readable under `pg_restore` 18.6 |
| Population correction | **`RC-05` covers four databases, not three** |
| `AAS+-PS-VETO-01` `C-6` | **NOT DISCHARGED** |

**No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.**
