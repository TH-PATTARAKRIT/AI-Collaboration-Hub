# IV CHECKPOINT REGISTER

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]`
**Branch** `audit/account-phase-s-iv-rc-verify-2026-09-07-001` · base `origin/SMEsPlus` @ `b8666f1`

| # | Checkpoint | Result |
|---|---|---|
| `CP-IV-01` | Fresh clone, new branch from `origin/SMEsPlus` | `b8666f14fab9a13dc1a986fdd5446ec55c6eb9db` |
| `CP-IV-02` | §1 precondition — `REMEDIATION-A` published | **SATISFIED** — `0941161824f4d447d9e0816e492a90b99bcfaecc`, read back from remote |
| `CP-IV-03` | Handoff matrix present and complete for 6 RCs | **SATISFIED** — all 8 required columns per row |
| `CP-IV-04` | Prior `IV-PRECONDITION-HOLD` @ `9d8ad70` re-assessed | **SUPERSEDED WITH LINEAGE** — correct when written |
| `CP-IV-05` | Governing rulings read from **primary text**, not from the handoff summary | `Q-BOSS-01`, `Q-BOSS-02`, `Q-BOSS-03` read in full at `0941161` / `6cb9946` |
| `CP-IV-06` | Executor eligibility determined per repair/challenge pair | **NOT ELIGIBLE, 6 of 6** — `Co-Authored-By` trailer checked on every SHA individually |
| `CP-IV-07` | `IV-INSTR-01` frozen-ref instrument defect found and re-run | 6 false `MATCH` on empty comparison → re-run in a second shape → **6 of 6 genuine MATCH** |
| `CP-IV-08` | `IV-INSTR-02` input-sweep defect found and re-run | zsh glob abort produced a false negative → re-run by exact filename → **4 of 4 present** |
| `CP-IV-09` | `RC-05` frozen inputs hash-verified | **4 of 4 SHA-256 and byte-size match**; `pg_restore` 16.15 **and** 18.6 present |
| `CP-IV-10` | `RC-01` source root and population reproduced | **13,515 `.py`**, matches the asserted figure |
| `CP-IV-11` | `k1_population.json` provenance verified | **4 copies, all `54edc214…bbbdc569`** — matrix claim `SUPPORTED` |
| `CP-IV-12` | `IV-R-01` surface-set check, all 5 lanes | fires **5 of 5** — no passing control; ranked by magnitude, 4 called material |
| `CP-IV-13` | `IV-INSTR-03` found — RC-05 size read from the manifest, not measured | corrected in place with the error preserved; **it is what hid `IV-R-04`** |
| `CP-IV-14` | `IV-R-04` manifest coverage sweep (`P11-E-49` lead) | **2 live false assertions** (P11 91-vs-92, RC-05 7-vs-8); **P09 is the passing control** |
| `CP-IV-15` | `IV-R-05` veto population reproduction attempted | **17 not reproducible; rows give 19–22.** The 51 Boss decisions **do** reproduce (19+19+10+3) |
| `CP-IV-16` | Six `RC` results issued | **0 PASS · 0 FAIL · 6 HOLD** |
| `CP-IV-17` | Cross-package sweeps | 3 executed · 2 partial · 4 not reachable · 1 added |
| `CP-IV-18` | Veto dispositions | **0 dischargeable**; 0 discharged; 0 self-discharged |
| `CP-IV-19` | Closure criteria independently tested | **4 TRUE · 5 FALSE · 1 RE-OPENED** |
| `CP-IV-20` | Peer-owner mutation check | **0 peer refs written; 0 peer files edited** |
| `CP-IV-21` | Prohibited-wording sweep | 0 `PASS` verdicts, 0 Phase S closure, 0 Team B/C, 0 implementation authorization |
| `CP-IV-22` | Publication | branch + commit SHA recorded on push; remote read-back |

**Terminal:** `IV-CLOSEOUT-C — REQUIRED EVIDENCE UNAVAILABLE` (an eligible `RC` executor).
