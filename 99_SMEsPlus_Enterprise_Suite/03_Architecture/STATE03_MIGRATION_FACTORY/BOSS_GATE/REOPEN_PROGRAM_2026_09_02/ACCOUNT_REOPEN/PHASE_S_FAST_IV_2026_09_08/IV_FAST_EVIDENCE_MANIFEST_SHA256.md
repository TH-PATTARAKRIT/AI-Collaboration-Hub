# IV FAST — EVIDENCE MANIFEST (SHA-256)

**POPULATION** every file under `PHASE_S_FAST_IV_2026_09_08/` except this manifest.
**PATTERN** `find . -type f -name '*.md' ! -name 'IV_FAST_EVIDENCE_MANIFEST_SHA256.md'` — **executed, output below**, not merely declared (`[[smeplus-declared-pattern-not-run-defect]]`).
**PATH SET** the single directory above, on branch `audit/account-phase-s-fast-iv-2026-09-08-001`.
**UNIT** one file.

| Files returned by `find` | Files processed by the manifest | Roll-up SHA-256 |
|---|---|---|
| **14** | **14** | `f28130babc6119ec9adf75b1cbeaaf5ee058c9fb5a8bd2f270a6801c78ad4eaf` |

> **Coverage assertion:** `find` returned **14**, the manifest processed **14**. Both figures
> are printed, not asserted — `[[smeplus-coverage-assertion-rule]]` records a loop that silently
> processed 10 of 16 files while reporting success. **Returned and processed are separate numbers and
> both appear here.**

```
6f92a484ce934c2297d2a1344f45af9307f9a7e8a4f991898baae341eff8eee9  00_IV_FAST_PRECONDITION_AND_FROZEN_AUTHORITY.md
efa1cecb2f19ddee4112864f440c158af23821b7472c887215b1f65603f27190  01_RC01_P09_CHALLENGE.md
2f5b667766f1bd35c3b73f6c856c6d408fa7451892bb31ebdb46f6104dbbb890  02_RC02_P11_CHALLENGE.md
77537bd2214b2fbfc8b74ab3d3cc003b55f920a569e0bd388069862c9f0a0d9b  03_RC03_P06_IEV_CHALLENGE.md
6141587344d10a76f1ed89d615a6b2f0cd2ed29ccc64ad00e610a0cd4383a765  04_RC04_P06_SOURCE_CHALLENGE.md
dbb32c7a3c1b1ba115527e0c87b89ba76f4b490841a856a7b95991546e5ed843  05_RC05_P08_CHALLENGE.md
3fcce4f132f61f0e94ff46d2f018acdaa91415347ececf875f4b4565807caed6  06_RC06_P11_CHALLENGE.md
e95e22bef571c97e82a9e94956a30f6abc032ae632de591f8b72404a75e535bc  07_RC_RESULT_REGISTER.md
092bc0496ca583a988e79906155952a4ae8833194ea07386775c6ea4828208bd  08_POST_RC_CROSS_PACKAGE_VERIFICATION.md
57a7b3ee27444597dc99f334d0e2c2230b909353ae5d33aa026b862ecb21db3b  09_VETO_DISPOSITION_RECOMMENDATION.md
f7c2059fd2a6f5aaa9f93eb3600ee9572ea7612e919e3058348a955b133eeba2  10_PHASE_S_CLOSURE_CRITERIA_INDEPENDENT_TEST.md
24fbd2d391a56a7d2a82f12d3a75fc9f004b8ebf5decfd109f6a216bc3a49cf0  11_PHASE_S_FINAL_BOSS_DECISION_EVIDENCE_PACK.md
d9eaebb0df53a2010f606f1fda485be2ff5b36a3e37350ef0ef39502ff0a5084  IV_FAST_AUTO_RESUME_STATE.md
40c298f97b1b10dabfb5c7ee78779bb11e9a96ff4ba5a01f0131877625379fd4  IV_FAST_CHECKPOINT_REGISTER.md
```

## Pre-commit sweeps — four disjoint units, each with its control

| Sweep | Unit | Result | Control |
|---|---|---|---|
| Prohibited PASS / closure wording | one line | **0 matches** | **fired** — a synthetic file containing `RC-PASS — BOUNDED SURFACE SURVIVES` and `PHASE S = CLOSED` returned **2** matches, so the pattern can detect what it looks for |
| Clean-room declared token list (`stock.`, `product.`, `ir.`, `quant`, `orderpoint`, `picking`, `_action_`, `sudo`) | one token occurrence | **0 matches** | pattern is a literal alternation, verified by inspection |
| Orphan identifier — `IV2-F-*` | one identifier | **4 cited, 4 defined, 0 orphans** | set difference both directions |
| Orphan identifier — `CP-F-*` | one identifier | **12 cited, 12 defined, 0 orphans** | set difference both directions |

### Declared-versus-derived, stated rather than assumed

The clean-room sweep above ran the **declared** token list only. Per
`[[smeplus-clean-room-rules]]`, `tok = declared ∪ derived`, and the two halves are **not**
supersets of one another. The derived half was **not** run here.

**Stated plainly so it is not read as absence:** this package does contain Layer 2 citations —
`account_move`, `account_move_line`, `ir_module_module`, `pg_restore`, `.py`,
`parent_state`, `amount_currency`. **None is matched by the declared list** (`ir_module_module`
carries an underscore, not the `ir.` dot form). They are permitted here: this package sits under
`BOSS_GATE/` and is **Layer 2 audit quarantine, Boss / PMO / AI-Audit only**.

> **These tokens must not be transcribed into any Layer 1 reference package.**

## Branch and remote read-back

Recorded on push; see the session report. Every material claim in this package carries
Branch + Commit SHA + Artifact Path + verifier status.
