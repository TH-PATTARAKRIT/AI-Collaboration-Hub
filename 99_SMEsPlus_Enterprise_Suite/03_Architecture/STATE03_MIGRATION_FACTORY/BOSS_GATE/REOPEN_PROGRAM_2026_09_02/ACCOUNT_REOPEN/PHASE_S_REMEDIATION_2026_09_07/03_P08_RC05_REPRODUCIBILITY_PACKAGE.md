# 03 — `RC-05` REPRODUCIBILITY PACKAGE (controller record)

**Published on** `corr/p08-phase-s-rc05-prep-2026-09-07-001` @ **`e368d11`**
**Base** `corr/p08-phase-s-final-2026-09-07-001` @ `c7cfd8a` — **not rewritten**
**Full package** `ACCOUNT_P08_RECORD_TO_REPORT/RC05_REPRODUCIBILITY/`

> **`RC-05` WAS NOT RUN AND IS NOT CERTIFIED.** The owner executed the instrument only to establish
> that it runs and that its controls fire. That is preparation evidence and **cannot** satisfy
> structural independence.

---

## 1. `P08-RC05-PREP-C` is **NOT** raised — and the closeout's caution is why

The dispatch §5 required the token `P08-RC05-PREP-C — MISSING REPRODUCIBLE PRIMARY INPUT` **if** the
primary evidence were absent. **It is not absent.**

`10_` §3 asserted only that the P08 **surface** does not carry the instrument and inputs — and warned
in terms: *"Do not read item 2 as 'the evidence does not exist' … Sweep before concluding absence."*
**That warning was correct.** All four database extracts are on the host, in `/Users/admin/Downloads/`.

**Declared PATH SET:** every `/Volumes` entry (`/Volumes/iMac`, `/Volumes/iMacSys`,
`/Volumes/ChatGPT Installer`) and `$HOME`.
**PATTERN:** exact filename → `*.dump`/`*.sql` → **`PGDMP` magic bytes on every file over 4 MB**,
because **extension is not format**.
**DECLARED EXCLUSION:** `~/Library`, pruned for the TCC consent storm — **stated as an exclusion, not
omitted**, because a blanket `~/Library` prune has previously hidden whole source distributions from
three sweeps in this programme. **That subtree is unswept and the package says so.**

**Had this session published the "missing input" token without sweeping, it would have published a
false negative about the evidence base** — the single most repeated defect class in this programme.

## 2. What is now supplied

Executable instrument (**`rc05_balance.py`**, 264 lines) · four frozen inputs with **SHA-256** ·
population/unit/**denominator printed by the run** · **both** predicates (computed *and* stored
balance) · exact `Decimal` at precision 60 with **no float constructed at any step** · positive,
negative, injection, fail-closed, discriminating-set, cross-version and determinism controls ·
**expected behaviour written and hashed before the first execution** · invocation and output schema ·
immutable SHA.

## 3. The control that matters, and why it is graded

| Injection | exact | `1e-7` | `1e-4` | `0.005` |
|---|---|---|---|---|
| none | 0 | 0 | 0 | 0 |
| `0.01` | **1** | **1** | **1** | **1** |
| `0.001` | **1** | **1** | **1** | **0** |

**The `0.001` row is the one that earns its place.** A single injection proves only that the
predicate can return non-zero. The graded pair proves **the tolerance ladder itself discriminates** —
an instrument that reported `1` at `0.005` for a `0.001` error would be wrong in a way one injection
could never reveal. **Without this, "0 unbalanced at every tolerance" is indistinguishable from a
predicate that cannot fire.**

## 4. `P08-U-22` closed — the negative was about the tool

P08 carried a *"fourth deployed dump — still unread … declared unreadable by one tool and not
retried."*

| | |
|---|---|
| `pg_restore` **16.15** | **fails** — *"unsupported version (1.16) in file header"* |
| `pg_restore` **18.6**, same host, `/opt/homebrew/opt/postgresql@18/bin` | **reads it — 26,815 TOC entries, 165 `account_*` tables** |
| Positive control for the probe | the same command returns **162** on `DB-EV`, so the `0` under 16.15 is distinguishable from an empty archive |

**The archive was written by a newer `pg_dump` than the tool that was tried, and the negative stood
unretried for a full round.** **`RC-05`'s population is four databases, not three** — P08's claim is
scoped *"in any deployed database"* — and `DB-T2` is now measured.

## 5. A stated uncertainty, settled against the owner's own doubt

P08 states the figure as *"across **169,143**"* **without naming its unit**. This package predicted
**in writing, before executing**, that the run might show it to be **lines** rather than **entries**,
which would have made P08's denominator wrong in unit.

**It did not.** `POSTED_MOVES_WITH_LINES` = **169,143**; posted lines = **417,700**. **P08's unit is
correct.** **Published because the check could have found a defect and did not** — a control reported
only when it fires is not a control.

## 6. Owner preparation figures — for contradiction, not adoption

| Database | Denominator | `COMPUTED` @ exact/`1e-7`/`1e-4`/`0.005` | `STORED` |
|---|---|---|---|
| `DB-SM` | **169,143** | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| `DB-BK` | 16 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| `DB-EV` | 6 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| **`DB-T2`** | **5** | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |

Consistent with P08's corrected, **tolerance-independent** claim and with deleting the *"at `1e-7`
the answer is 3"* figure as having no referent. **One execution by the disqualified owner. It
certifies nothing.**

## 7. Declared not covered

Settlement reconstruction (a different measurement over a different table, `SUPPORTED
INTERPRETATION` on P08's own marking) · foreign-currency balance · per-company partition ·
`~/Library` · **and whether these four are in fact the complete deployed set — the sweep found four;
that they are *the* set is P08's prior claim and is not re-verified here.**
