# 02 — `RC-05` (P08) — INDEPENDENT CHALLENGE

**Verifier session** `[SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]` · branch `audit/account-phase-s-iv-rc-verify-2026-09-07-001`
**Executing model:** Claude Opus 5 · **Appointed verifier:** ChatGPT GPT-5.6 Sol

## 1. Exact scope restated before testing (§4.A)

Bounded to `corr/p08-phase-s-rc05-prep-2026-09-07-001` @ `e368d11` (base `c7cfd8a`, not rewritten):
`RC05_REPRODUCIBILITY/` — instrument `rc05_balance.py`, `EXPECTED_CONTROL_BEHAVIOUR.md`,
`MANIFEST.md`, four owner preparation run logs.
**Governed by `Q-BOSS-03`: documentary inspection alone is insufficient; independent execution of the
instrument against the frozen inputs is mandatory.**

## 2. Result

```
RC-05 = RC-HOLD — STRUCTURAL INDEPENDENCE NOT PROVEN
        (explicitly NOT 'HOLD — MISSING REPRODUCIBLE EVIDENCE' — see §3)
```

**Reason:** `Q-BOSS-02` §1 control 1 (Model / Agent Separation) and control 2 (Appointment
Independence) both fail for this executor. The repair under review at `e368d11` carries
`Co-Authored-By: Claude Opus 5`, which is the model executing this session. Per `Q-BOSS-01` §2,
*"A challenge run by the same model that authored the repair it challenges does not satisfy `RC-*`."*

**No falsification was attempted and none is reported.** A same-model attempt could not have produced
`RC` evidence whichever way it came out, and publishing one under an `RC` filename would invite the
inference `Q-BOSS-02` §5 prohibits. See `00_` §3.

## 3. Readiness verified (does NOT certify this RC)

**This is the one section of this package with a materially useful positive result.**
`Q-BOSS-03` §2 directs `RC-05 = HOLD — MISSING REPRODUCIBLE EVIDENCE` *if any required input is absent
or inaccessible*. **Every input was independently located and hash-verified. That condition is NOT met.**

| Required by `Q-BOSS-03` §2 | Verified | Evidence |
|---|---|---|
| executable instrument | **YES** | `e368d11:…/RC05_REPRODUCIBILITY/instrument/rc05_balance.py`, tracked, 264 lines |
| frozen reproducible inputs | **YES — 4 of 4** | table below |
| population / denominator / unit | **YES** | printed by the run; population is **FOUR** databases, not three |
| predicates + tolerance semantics | **YES** | both computed and stored balance; exact `Decimal` precision 60 |
| controls capable of firing | **published** | positive · negative · **graded injection** · 4 fail-closed · discriminating set · cross-version · determinism |
| expected control behaviour | **YES** | `EXPECTED_CONTROL_BEHAVIOUR.md`, **hashed before first execution** |
| immutable SHA | **YES** | `e368d11` on remote |

### Frozen inputs — independently hashed on this host

| Label | File | Published bytes | Measured bytes | SHA-256 | Result |
|---|---|---|---|---|---|
| `DB-SM` | `/Users/admin/Downloads/iSMEs_2026-07-11_05-03-27.dump` | 155,443,710 | **155,443,710** | `ca77818b…5118ae2` | **MATCH** |
| `DB-BK` | `/Users/admin/Downloads/BK12MAY26_2026-08-03_05-48-30.dump` | 35,679,594 | **35,679,594** | `1a673474…70e151a3` | **MATCH** |
| `DB-EV` | `/Users/admin/Downloads/iEVING_2026-07-23_10-31-06.dump` | 24,911,161 | **24,911,161** | `eade5512…3a85cb0f` | **MATCH** |
| `DB-T2` | `/Users/admin/Downloads/iTEST02_2026-07-14_16-34-51.dump` | 64,303,340 | **64,303,340** | `84a75479…adb837a4` | **MATCH** |

**4 of 4 present · 4 of 4 byte-size match · 4 of 4 SHA-256 match.** Measured with `shasum -a 256` and
`stat -f%z` per file by exact filename, after `IV-INSTR-02` (`00_` §4) produced a false negative on
this same population.

| Tool | Required | Present |
|---|---|---|
| `pg_restore` 16.x | for `DB-SM`/`DB-BK`/`DB-EV` | `/opt/homebrew/bin/pg_restore` — **16.15** |
| `pg_restore` 18.x | **required for `DB-T2`** | `/opt/homebrew/opt/postgresql@18/bin/pg_restore` — **18.6** |

**Both tool versions the cross-version control needs are on this host.** `P08-U-22`'s "fourth dump
unreadable" was a tool defect, and the population really is four.

### 3.1 Surface-set check — `IV-R-01/RC-05`: **narrowest miss of the five, but not clean**

`git show --name-only e368d11` changes **8** files. The matrix declares *"`RC05_REPRODUCIBILITY/` —
instrument, prediction, 4 run logs, manifest"* — **7 by role**. The one it does not account for is
`00_RC05_REPRODUCIBILITY_PACKAGE.md`, the package record itself.

**Correction to this session's own first reading.** This section initially recorded `RC-05` as a clean
negative control at `declared = changed = 7`. That was wrong twice: the changed count is **8**, not 7,
and the declared description covers **7**, not 8. **`RC-05` understates by one file, not by none.**
The error is recorded rather than overwritten, per §4.H. Its cause is `IV-INSTR-03` (`07_` §4) —
the count was taken from the package's own `MANIFEST.md` header instead of being measured.

**`IV-R-01` therefore fires in all five lanes, with no passing control.** That weakens it as a
*discriminating* instrument and the ranking in `07_` §3 is by magnitude for that reason:
`RC-04` 6 of 8 · `RC-02` 6 of 10 · `RC-03` 4 of 7 · `RC-01` 4 of 8 · **`RC-05` 1 of 8.**
`RC-05`'s single miss is a package record, carries no count and no disposition, and this session
does **not** call it material.

### 3.2 `IV-R-04` — the RC-05 manifest coverage assertion is false, **MATERIAL**

`MANIFEST.md` @ `e368d11` declares:

> **POPULATION:** every file under `RC05_REPRODUCIBILITY/` · **PATTERN:** `find . -type f` · **UNIT:** one file.
> … **Coverage assertion:** `find` returned **7**, manifest processed **7**.

**Measured — two independently shaped counts, both 8:**

| Instrument | Result |
|---|---|
| `git ls-tree -r --name-only e368d11 \| grep -c RC05_REPRODUCIBILITY/` | **8** |
| `git archive e368d11 …` → extract → `find . -type f \| wc -l` | **8** |

The eight: `00_RC05_REPRODUCIBILITY_PACKAGE.md` · `EXPECTED_CONTROL_BEHAVIOUR.md` · **`MANIFEST.md`** ·
`instrument/rc05_balance.py` · `owner_preparation_run/RUN_{1,2,3,4}_*.txt`.
`MANIFEST.md` lists **7** and **does not list itself** (`grep -c 'MANIFEST.md' MANIFEST.md` → `0`).

**The defect is the assertion, not the omission.** A manifest cannot contain its own hash; excluding
itself is correct. Declaring the population as *every file under the directory* with pattern
`find . -type f`, and then asserting *"find returned 7, manifest processed 7"*, is not — `find`
returns 8. The true statement is **population 8, manifest scope 7, one excluded by self-reference**,
with the exclusion declared. A stated exclusion stops the audit; a silent one nets the count.

**Why it is material, and sharply so:** this is the exact shape of **`P11-E-49`** — a manifest coverage
assertion carried forward and false, which the remediation session raised itself, repaired at the
packaging level, and registered as a lead: *"Check whether any other package in this programme carries
the same shape. Not swept here — outside the remit."* **It carries the same shape in the package that
same session published in the same commit.** The lead was correct and its nearest instance was one
directory away.

**Effect on `RC-05`'s evidence contract: none.** All four frozen inputs are present and hash-verified
(§3), the instrument is tracked, and the controls are published. `IV-R-04` is a packaging-coverage
defect. It does **not** convert `RC-05` to `HOLD — MISSING REPRODUCIBLE EVIDENCE`, and it is reported
here so it is not later mistaken for one.

**Routed to P08 owner.** Not edited here.

## 4. Findings

**None issued.** No `SUPPORTED`, `CONTRADICTED`, `NARROWED` or `ROUTED` disposition is recorded
against this surface by this session. **Absence of findings here is absence of testing, not absence
of defects** — and under §2.10 of the governing prompt it may not be read as a discharge of anything.

## 5. What the appointed verifier must still do

Execute `rc05_balance.py` independently against all **four** frozen inputs, reproduce the balance and
tolerance results and every published control — including the **graded injection**, whose `0.001`/`0.005`
row is the only one that proves the tolerance ladder discriminates. Re-verify the pre-execution hash of
`EXPECTED_CONTROL_BEHAVIOUR.md` **before** the first run, not after. Do not accept the owner's four
preparation run logs as the reproduction — `Q-BOSS-03` §3.B forbids P08 self-certification.
