# P07 — CHECKPOINT AND AUTO_RESUME_STATE

Round `SMEPLUS-26-09-06-P07-TH-TAX-SHARED-DOMAIN-PURE-CLOSURE-002`.
`LAYER 2 — AUDIT QUARANTINE`. **This file is an instruction to the next session, not a summary.**

## 1. CHECKPOINT

| | |
|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Branch | `research/account-p07-th-tax-compliance-2026-09-04-001` |
| Baseline entering this round | `3548b343c3baa70817905661a264b457a78635e8` |
| Prompt commit fast-forwarded to | `aef26ed60aeb8616407df1f52ae51d20037e17a9` |
| Package | `…/ACCOUNT_REOPEN/P07_TH_TAX_TO_COMPLIANCE_EXECUTION/` — 23 root files **+ `S02_DOMAIN_PURE_CLOSURE_2026_09_06/`** |
| Terminal state | **`P07 BOUNDED-DEEP CLOSURE COMPLETE — READY FOR PHASE S SHARED-HANDOFF EVIDENCE — OPEN HOLDS NAMED`** |
| Verdict | `RECOMMEND HOLD` · **0 of 8** exit criteria · **0** blockers closed · no merge · no freeze |
| `AASR-P07-VETO-01` | **not discharged** — rests on `P07-U-03` |
| Findings | `P07-F-01` … **`P07-F-112`** |
| Revisions | `REV-E-01` … **`REV-E-95`** · `REV-M-01` … **`REV-M-99`** |
| Contradictions | `P07-C-01` … **`P07-C-29`** |
| Open items | **33** — 2 opened (`P07-U-34`, `P07-U-35`), 1 opened and closed (`P07-U-36`) |
| **Background tasks** | **ZERO RUNNING.** Verified at round close by process scan. The one historical task (`btrz49256`) is dispositioned at `22 §48.1` as `TERMINATED — REDUNDANT CORROBORATIVE ROUTE / BLOCKED_ON_IO`. |
| Mutation | **none.** Read-only throughout: no database, runtime, source or configuration was modified. |

### 1.1 Peer inputs consumed, at their commits

| peer | commit | artefact | status |
|---|---|---|---|
| P10 | `1fea562` | `P10_TO_P07_HANDOFF.md` | **consumed and answered**; reply published |
| P06 | `9e5d729` | `54_P06_P07_BLOCKING_DEPENDENCY_MATRIX.md` | **consumed**; four requirements accepted as the counterparty half |
| Program | `48ee264` | `COMMON_CLOSURE_EXECUTION_CONSTITUTION_V1` | governance applied |

### 1.2 Handoffs published this round

| to | file | contains |
|---|---|---|
| **P10** | `P07_TO_P10_HANDOFF.md` | `Q07-1`…`Q07-3` answered negative and bounded; **`Q07-4` CONTRADICTED with evidence**; `Q07-5` refused as a statutory unknown; the 9-vs-10 count resolved as two denominators; the 18-field interaction surface; one interface fact observed and deliberately not interpreted |
| **P06** | `…HANDOFF_PACK.md §CH-06` | acceptance only. **Nothing is asked of P06 that P06 has not already committed.** |

## 2. AUTO_RESUME_STATE

### 2.1 If this session is resumed with no new prompt — **STOP.**

The round is terminal. Every declared Closure Question has one terminal disposition; no
background task is running; the commit is pushed and the remote verified. **Do not open a new
research round. `No Material Delta = No Additional Research Round.`**

### 2.2 NEXT EXACT ACTION, if and only if a named trigger fires

**Read this table before doing anything else. Do not re-derive it, and do not start elsewhere.**

| trigger | the exact next action | do **not** |
|---|---|---|
| **P10 publishes a correction to its `Q07-4` `FACT VERIFIED`** | Record it in `P07_CONTRADICTION_AND_REVISION_SUPPLEMENT.md §3` against `P07-C-26` and close that row. **One edit.** | re-run `EP-3`/`EP-4a`; they already agree by two routes |
| **P10 disputes the `Q07-1`…`Q07-3` answer** | Re-read `CH-C`'s scope note first. The claim is bounded to **modules named `l10n_th*`**, not to Thai tax code. If P10's dispute is about that boundary, **it is right and the answer is to widen the population by capability, extending `P07-F-83`'s route** — not to re-run the token scan. | re-run `EP-2` with more tokens |
| **P05 publishes** | Read its register and status fields — **never a summary**. Route only same-scope material deltas to the affected P07 question. Expect overlap on `TX-03`, `TX-04`, `TX-05`, which P06 already cited. | open a P05 review; read P05 internals |
| **The new P06 continuation publishes** | Check only whether `P07-R-01`…`P07-R-04` survived. If any was withdrawn, the affected row of `X-07`/`X-08`/`X-09` loses its counterparty half and reverts. | re-assess P06's mechanism |
| **P01 publishes** | `DUP-01` becomes reconcilable for the first time — *the withholding fact is created in P06 and reported from a P01 artefact*. That is the only P01-dependent item. | anything else in P01 |
| **P11 rules on tenant containment** | Close `P07-U-14` / `H-07` against the ruling. | infer a scope rule before the ruling |
| **A controlled execution is authorised** | **Run all four together in one sitting: `P07-U-20`, `P07-U-29`, `P07-U-35`, and P04's `P04-B-47`.** Two moves with withholding posted in one batch, recomputed, both stored values read — this settles `P07-U-35` and `CH-D`'s frequency question at once; then the chart-template load under an active Thai language, run twice in opposite orders. | run them separately; they are one ask |
| **PHASE B opens with AI EOS active** | The candidate pack becomes the input. **Read `CH-A`'s challenge first**: the pack has no candidate for *the tax fact itself* as a first-class object, and PHASE B will not find one in it. | treat any `DESIGN CANDIDATE — PHASE S ONLY` row as a specification |

### 2.3 Standing prohibitions carried into any resumption

- **Do not reopen `P07-N-25`.** Settled at `22 §30`/`§31` by the `ir_model` registry route.
- **Do not rerun the `P07-N-25` filesystem sweep.** Terminated `BLOCKED_ON_IO`; cloud-backed
  storage will block it again.
- **Do not widen the census** to key `P07-U-32`'s 20 artefacts without a Closure Question
  denominated over them. It is Class E today.
- **Do not write "localisation does not affect recognition."** The permitted sentence is in
  `P07_TO_P10_HANDOFF.md §2`, and its bound is part of it.
- **Do not read `P07-F-78` as a general discharge of copy identity.** `REV-M-96`: it tested four
  claims; `P07-F-108` is a fifth and it turns on the answer.
- **Do not treat `P07-R-01`…`P07-R-04` as P07 findings.** They are P06's commitments in P06's
  chosen numbering.

### 2.4 The three things a reader of this package most easily gets wrong

Written down because each has already happened at least once.

1. **A field that exists is not a field that is used.** `tax_period` and `tax_period_date` exist
   at both levels in 3 of 7 identities and are read for selection at neither (`REV-E-93`).
2. **A module in the source tree is not a module in the deployment.** The only consumer of the
   stored `wht_amount` is uninstalled in 6 of 7 identities (`REV-E-94`); and
   `smesplus_tax_period_date`, cited throughout this package, is installed in **none**
   (`REV-E-92`).
3. **A count is not wrong because two documents disagree.** Nine and ten Thai localisation
   modules were both right — for different databases (`REV-M-97`).
