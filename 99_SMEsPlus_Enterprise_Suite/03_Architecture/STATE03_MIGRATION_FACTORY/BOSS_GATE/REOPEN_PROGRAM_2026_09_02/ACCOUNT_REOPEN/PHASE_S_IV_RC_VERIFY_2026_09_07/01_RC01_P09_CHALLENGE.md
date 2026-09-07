# 01 — `RC-01` (P09) — INDEPENDENT CHALLENGE

**Verifier session** `[SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]` · branch `audit/account-phase-s-iv-rc-verify-2026-09-07-001`
**Executing model:** Claude Opus 5 · **Appointed verifier:** ChatGPT GPT-5.6 Sol

## 1. Exact scope restated before testing (§4.A)

Bounded to the P09 corrected surface at `corr/p09-phase-s-final-2026-09-07-001` @ `2079a25`:
`OWNER_QUEUE_2026_09_07/Q_P09_01_L4_AUTHORITY_RESOLUTION.md`,
`Q_P09_02_CHALLENGE_SCOPE_PREPARED_NOT_RUN.md`,
`LAYER2_AUDIT_QUARANTINE/q1.py`, `q1_results.json`.
**Not in scope:** the whole P09 package; the six XRECON corrections beyond truth-at-location,
superseded lineage, single authoritative disposition, no new contradiction, no peer mutation.

## 2. Result

```
RC-01 = RC-HOLD — STRUCTURAL INDEPENDENCE NOT PROVEN
```

**Reason:** `Q-BOSS-02` §1 control 1 (Model / Agent Separation) and control 2 (Appointment
Independence) both fail for this executor. The repair under review at `2079a25` carries
`Co-Authored-By: Claude Opus 5`, which is the model executing this session. Per `Q-BOSS-01` §2,
*"A challenge run by the same model that authored the repair it challenges does not satisfy `RC-*`."*

**No falsification was attempted and none is reported.** A same-model attempt could not have produced
`RC` evidence whichever way it came out, and publishing one under an `RC` filename would invite the
inference `Q-BOSS-02` §5 prohibits. See `00_` §3.

## 3. Readiness verified (does NOT certify this RC)

| Check | Result |
|---|---|
| Frozen ref head == asserted SHA | `corr/p09-phase-s-final-2026-09-07-001` = `2079a2594a6a76eb91bdb528f22eaf928d42c0d6` — **MATCH**, read from `git ls-remote`, full 40 chars |
| Source root exists | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons` — **EXISTS** |
| `.py` population reproduces | independent `find`/`wc -l` count → **13,515**. The matrix asserts 13,515. **Reproduced exactly, by an independent count** |
| `k1_population.json` provenance | matrix §2 states `q1.py` reads it from a **local peer clone** and that the in-repo copy at `2079a25` is byte-identical. **The in-repo copy is the one to use.** Byte-identity **not re-verified here** — that is an RC-scope check |

### 3.1 Provenance claim independently verified — `IV-R-03`

The matrix asserts the in-repo `k1_population.json` is byte-identical to the peer-clone copy
`q1.py` actually reads, at `sha256 54edc214…bbbdc569`. **Measured, not accepted.**

`q1.py` @ `2079a25` lines 21–24 hardcode its input to
`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_P09_PLAN_TO_ANALYZE_2026_09_04_EXECUTION/…/L1_L8_BOUNDED_CORRECTION_2026_09_06/LAYER2_AUDIT_QUARANTINE/INSTRUMENTS`
— a peer session clone outside the repository, exactly as the matrix declares.

| Copy | SHA-256 |
|---|---|
| in-repo `…/L1_L8_BOUNDED_CORRECTION_2026_09_06/…/k1_population.json` @ `2079a25` | `54edc214594d8e9f41a5943fc3f0bac0c4bdf9083c3ab42ae0e3cb38bbbdc569` |
| in-repo `…/FINAL_BOUNDED_COMPLETION_2026_09_06/…/k1_population.json` @ `2079a25` | **identical** — same git blob `85f3fa63` |
| peer clone, `L1_L8_…` path (the one `q1.py` reads) | `54edc214…bbbdc569` |
| peer clone, `FINAL_BOUNDED_…` path | `54edc214…bbbdc569` |

**4 of 4 identical. The matrix's claim is SUPPORTED by independent measurement.**
Two consequences the challenger should carry:
1. **There are two in-repo copies, not one.** The matrix names one. They are byte-identical, so the
   ambiguity is currently harmless — **but it is an ambiguity, and it is unstated.**
2. The peer clone **does currently exist on this host**, so `q1.py` would run unmodified. It should
   still be re-pointed in-repo: a path outside the frozen evidence contract is not reproducible for a
   verifier who does not have that clone, and this session cannot know it will still be there.

### 3.2 Declared surface ≠ changed surface — `IV-R-01/RC-01`, **MATERIAL**

The matrix declares four files. `git show --name-only 2079a25` changes **eight**.

| Declared (4) | Changed but not declared (4) |
|---|---|
| `OWNER_QUEUE_2026_09_07/Q_P09_01_L4_AUTHORITY_RESOLUTION.md` | `OWNER_QUEUE_2026_09_07/P09_AUTO_RESUME_STATE.md` |
| `OWNER_QUEUE_2026_09_07/Q_P09_02_CHALLENGE_SCOPE_PREPARED_NOT_RUN.md` | `L1_L8_BOUNDED_CORRECTION_2026_09_06/P09_AUTO_RESUME_STATE.md` |
| `OWNER_QUEUE_2026_09_07/LAYER2_AUDIT_QUARANTINE/q1.py` | `L1_L8_BOUNDED_CORRECTION_2026_09_06/P09_CHECKPOINT_REGISTER.md` |
| `OWNER_QUEUE_2026_09_07/LAYER2_AUDIT_QUARANTINE/q1_results.json` | `ACCOUNT_P09_PLAN_TO_ANALYZE/PACKAGE_MANIFEST_SHA256.md` |

**declared ∩ changed = 4 · changed \ declared = 4 · declared \ changed = 0.** The declared set is a
strict subset — better than `RC-03`, where two declared files were not even touched.

**Why it is material here specifically:** the undeclared four include `PACKAGE_MANIFEST_SHA256.md`.
A manifest changed by the same commit it is supposed to attest is exactly the surface `P11-E-49`
turned on — a coverage assertion carried forward and false. The matrix does not put it in front of
the challenger. **`RC-01`'s expected-challenge row says nothing about it either.**

**One instance of `IV-R-01`, measured in all five lanes in `07_` §3.** The check **fires in all five**,
including `RC-05`, so it has **no passing control** and is weak as a discriminator; `07_` §3 therefore
ranks the lanes **by magnitude** rather than treating them alike. This session does not call
`RC-05`'s single-file miss material.

## 4. Findings

**None issued.** No `SUPPORTED`, `CONTRADICTED`, `NARROWED` or `ROUTED` disposition is recorded
against this surface by this session. **Absence of findings here is absence of testing, not absence
of defects** — and under §2.10 of the governing prompt it may not be read as a discharge of anything.

## 5. What the appointed verifier must still do

Re-execute `q1.py` from the frozen ref, sourcing `k1_population.json` **in-repo**, not from the peer
clone path. **Establish the deployed generation before relying on an Odoo 18 root** — the handoff row
says so explicitly, and this programme has already read the wrong generation for four rounds. Then
test truth-at-location, superseded lineage, single authoritative disposition, no new contradiction,
and no peer mutation.
