# 05 — `RC-05` P08 CHALLENGE

**Frozen surface** `corr/p08-phase-s-rc05-prep-2026-09-07-001` @ `e368d11da6f7e4973469ff5608d676ec2d13811c`
**Lane** B — host-dependent
**Result** `RC-HOLD — REQUIRED EVIDENCE OR INDEPENDENCE UNAVAILABLE`
**Cause** independence **only**. Explicitly **NOT** `RC-HOLD — MISSING REPRODUCIBLE EVIDENCE`.

## 1. Exact scope restated before testing (prompt §9)

Population is **FOUR** databases, not three. Verify published SHA-256 for all four frozen inputs;
independently re-execute the published instrument over all four dumps; use the compatible
`pg_restore` 18.x path required for `DB-T2`; execute positive, negative, graded-injection,
fail-closed, discriminating-set, cross-version and determinism controls; verify the prediction hash
was frozen **before** execution; reproduce the in-scope result **without relying on P08's
conclusion**.

## 2. Not run

`RC-05` was **NOT RUN**. `instrument/rc05_balance.py` was **not executed**, not once, with or without
injection. **No figure in P08's §8 table was reproduced or contradicted.** `169,143`, `417,700` and
every `0` in the tolerance ladder remain **owner preparation figures published to be contradicted**,
and this session neither contradicted nor adopted them.

## 3. `Q-BOSS-03` §2 requirement inventory — measured, not asserted

Boss ruled that documentary inspection alone is insufficient and listed the minimum P08 must publish
before `RC-05` may be executed. Each requirement was checked against `e368d11` by reading the frozen
tree. **This tests whether the lane is executable, not whether its answer is right.**

| `Q-BOSS-03` §2 requirement | Present at `e368d11`? |
|---|---|
| executable instrument / exact procedure | **YES** — `RC05_REPRODUCIBILITY/instrument/rc05_balance.py` |
| frozen reproducible evidence inputs | **YES** — 4 dumps named with absolute paths, §4 below |
| exact population / denominator / unit | **YES** — package §4, unit = one `account_move`, printed by the run |
| predicates and tolerance semantics | **YES** — package §5, `Decimal` prec 60, ladder `0 / 1e-7 / 1e-4 / 0.005` |
| controls capable of firing | **YES** — package §6.1–6.7, incl. **graded** injection at `0.01` and `0.001` |
| expected control behaviour | **YES** — `EXPECTED_CONTROL_BEHAVIOUR.md` |
| immutable correction/evidence SHA | **YES** — `e368d11`, `MANIFEST.md` roll-up `904a8fde…3f3554e` |
| provenance to reproduce without P08's conclusion | **YES** — invocation line, output schema, per-input SHA-256 |

**8 of 8 present.**

## 4. Frozen input verification — independently recomputed on this host, 2026-09-08

Every dump was hashed by this session. **A SHA-256 is executor-neutral: the number does not depend on
who computes it.** Magic bytes read directly rather than trusting the `.dump` extension, per
`[[smeplus-archive-denominator-key]]` (*search by format, not extension*).

| Label | File | Declared bytes | Measured bytes | SHA-256 | Magic |
|---|---|---|---|---|---|
| `DB-SM` | `/Users/admin/Downloads/iSMEs_2026-07-11_05-03-27.dump` | 155,443,710 | **155,443,710** | **MATCH** `ca77818b…5118ae2` | `PGDMP` |
| `DB-BK` | `/Users/admin/Downloads/BK12MAY26_2026-08-03_05-48-30.dump` | 35,679,594 | **35,679,594** | **MATCH** `1a673474…70e151a3` | `PGDMP` |
| `DB-EV` | `/Users/admin/Downloads/iEVING_2026-07-23_10-31-06.dump` | 24,911,161 | **24,911,161** | **MATCH** `eade5512…3a85cb0f` | `PGDMP` |
| `DB-T2` | `/Users/admin/Downloads/iTEST02_2026-07-14_16-34-51.dump` | 64,303,340 | **64,303,340** | **MATCH** `84a75479…adb837a4` | `PGDMP` |

**4 of 4 present · 4 of 4 byte-size match · 4 of 4 SHA-256 match · 4 of 4 `PGDMP`.**

Byte-size alone would not distinguish a truncated from an intact archive, and per
`[[smeplus-control-that-cannot-detect-its-failure]]` a size check cannot detect its own failure —
which is why the full hash and the magic were both taken.

## 5. `pg_restore` toolchain — the `DB-T2` requirement

| Requirement | Found on this host |
|---|---|
| `pg_restore` **18.x** (required for `DB-T2`) | **`/opt/homebrew/Cellar/postgresql@18/18.6/bin/pg_restore`** — present, and the declared `/opt/homebrew/opt/postgresql@18/bin` symlink target resolves to it |
| `pg_restore` **16.x** (for the §6.6 cross-version control) | **`/opt/homebrew/Cellar/postgresql@16/16.15/bin/pg_restore`** — present |

Both versions the cross-version control needs are installed. Also present but **not** the declared
path: `libpq 18.4` and pgAdmin's bundled binary — noted so a verifier does not silently pick one up
from `PATH` and then attribute a version effect to the data.

## 6. Determination

**`RC-05` is evidence-complete and executor-blocked.** Routing it back to P08 as
`HOLD — MISSING REPRODUCIBLE EVIDENCE` would be wasted work and would misstate the cause: nothing is
missing. What is missing is an **eligible executor**.

## 7. Not covered — stated so it is not assumed

P08's own §9 exclusions stand untested by this session: settlement reconstruction, `amount_currency`,
per-company partition, the unswept `~/Library` subtree, and **whether these four are all deployed
databases** — which P08 explicitly marks *not established*. `AAS+-PS-VETO-01` `C-6` remains
**NOT DISCHARGED**.
