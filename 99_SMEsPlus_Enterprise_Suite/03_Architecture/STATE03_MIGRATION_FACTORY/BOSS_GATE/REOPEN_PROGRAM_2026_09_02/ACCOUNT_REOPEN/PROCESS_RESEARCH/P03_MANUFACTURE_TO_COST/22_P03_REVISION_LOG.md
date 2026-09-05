# 22 — P03 REVISION LOG / RESEARCH ERROR REGISTER

**LAYER 2 — AUDIT QUARANTINE.**

Serves as both the revision log and the research-error register required by
`SMEPLUS-26-09-04-ACC-REV2-CORR1` §6.

---

## 1. Session revisions

| Rev | Trigger | Effect |
|---|---|---|
| `R0` | Session start, prompt `SMEPLUS-26-09-04-ACC-P03-M2C-REV2-001` | Governance read, primary source located, `01`–`17` drafted |
| `R1` | Self-challenge, `19_P03_AAS03_CHALLENGE.md` | Ten corrections `C-01` … `C-10`, applied in place |
| `R2` | **`SMEPLUS-26-09-04-ACC-REV2-CORR1` received mid-session** | Scope revalidation; `18_P03_SCOPE_OWNERSHIP_MATRIX.md` created; `06` §5, `14`, `16` revised |
| `R3` | AAS+ audit, `20_P03_AAS_PLUS.md` | `AASP-01` and `AASP-03` applied in place; `AASP-02`, `AASP-04`, `AASP-05` recorded as unrepaired and disclosed |
| `R4` | Closure | Clean-room scan, manifest, push at `812cc5c` |
| `R7` | **Supplemental continuation `…RUNTIME-INVERSION-RISK-RECLASSIFICATION-001`** | Fourth database opened; `DEP-04` and `UNR-P03-07` closed; `DEP-13` executed substantively; the valuation explosion found; **5 of P03's own errors corrected, one of them this round's own draft**. Files `48`–`73` |
| `R6` | **Continuation `SMEPLUS-26-09-05-…-CROSS-PROCESS-EVIDENCE-CLOSURE-001`** | Peer branches read; runtime/database evidence executed for the first time; `DC-14`/`DC-15`/`DEP-13` dispositioned; 2 unresolved items closed; **4 of P03's own errors corrected**. Files `26`–`47` |
| `R5` | **Inbound peer evidence from P04 — Acquire-to-Retire**, after push | Every claim independently re-verified from source. Two new findings `DC-14`/`DC-15`; two sharpened; `CC-07` strengthened; **the `01` §3 denominator corrected**; **one scope downgrade `REV-S-05`**; AAS+ veto second limb widened. Record: `25` |

**No reset occurred. No evidence was discarded. No completed work was repeated.**

## 2. Research errors found by self-challenge — `R1`

Each was a real error in the draft, corrected in place.

| ID | Error | Correction |
|---|---|---|
| `C-01` | `DC-01` framed so as to imply all conversion cost doubles | Scoped to the machine component |
| `C-02` | `10` §4 stated the residue-netting risk unconditionally | Conditioned on a mixed-costing configuration |
| `C-03` | `DC-08` cited without line precision | Weakness recorded rather than hidden |
| `C-04` | **`DC-08`'s mechanism classified `FACT VERIFIED` when `_set_duration` had not been read** | Downgraded to `SUPPORTED INTERPRETATION`; the outcome remains `FACT VERIFIED` |
| `C-05` | `DC-12` described imprecisely | Stated as a rate-squared error |
| `C-06` | `DEP-07`'s negative claim used a conceptual, non-reproducible pattern | Labelled `NO EVIDENCE FOUND — PATTERN NOT MECHANICAL` |
| `C-07` | **`02` §2 miscounted its own register: 11 + 8 ≠ 20** | Corrected to 11 + 8 + 1 |
| `C-08` | `01` §6's denominator excluded the module expansion plan | Plan searched — **no manufacturing reference found** — and the claim bounded |
| `C-09` | Fifteen requirements scattered across three files | Consolidated in `21` §3 with an explicit non-baseline marker |
| `C-10` | Layer separation asserted but not verified | Scan run; result in §5 |

`C-07` is the error this session most wants recorded: it is the same defect
`smeplus-account-wave-a-final-closure-status` names — **a package miscounting its own
register** — reproduced here despite the lesson being on file. Self-review caught it;
nothing structural prevented it.

## 3. `R2` — scope revalidation under CORR1

CORR1 supersedes any wording implying blanket "Tenant + Company mandatory everywhere".
Each affected finding, in the format CORR1 §6 requires.

### `REV-S-01` — `06` §5, multi-tenant/multi-company section

| Field | Content |
|---|---|
| **Original finding** | "Every event carries a company … tenant/company context mandatory", with two exceptions |
| **Scope assumption used** | Tenant + company required for every event |
| **Why over-constrained** | `BE-01` … `BE-04` include master-data selection (BOM, routing) that is not a legal-entity fact and needs no company context to be correct |
| **Correct scope analysis** | Master-data events are `TENANT`; every event with a financial effect is `COMPANY`; cited reference taxonomies are `PLATFORM` candidates |
| **Updated classification** | `FACT VERIFIED`, restated by scope class |
| **Architecture impact** | Introduces the tenant/company split of `18` §4 and requirement `R-15` |
| **Cross-process impact** | Offered to P11 as a candidate, not binding — `DEP-11` |
| **Evidence required** | None for this row |

### `REV-S-02` — `DC-11`, wrong-company account resolution

| Field | Content |
|---|---|
| **Original finding** | Company-dependent accounts resolved in the acting user's company. Critical, tenant-isolation class |
| **Scope assumption used** | Company context mandatory for all operations |
| **Why over-constrained** | The blanket premise was wrong, but this operation is a journal entry |
| **Correct scope analysis** | A journal entry is the canonical `COMPANY`-scoped financial event. Company context is **mandatory for this operation specifically**; missing = DENY |
| **Updated classification** | **`FACT VERIFIED`, unchanged, and now resting on a stated scope rule rather than a blanket one — strengthened** |
| **Architecture impact** | None new |
| **Cross-process impact** | Still routed to the Inventory MTI conformance track — `DEP-05` |
| **Evidence required** | None |

### `REV-S-03` — the WIP wizard's company handling, `06` §4 and §5

| Field | Content |
|---|---|
| **Original finding** | Reads the active company, never an order's company, while accepting a multi-company selection |
| **Scope assumption used** | Blanket |
| **Why over-constrained** | The premise was; the conclusion was not |
| **Correct scope analysis** | The WIP accrual is a `COMPANY`-scoped financial event. Accepting orders from several companies into one such entry is a scope breach under the corrected model, not merely under a blanket rule |
| **Updated classification** | `FACT VERIFIED`, **severity raised** from an observation to a scope breach |
| **Architecture impact** | Reinforces `R-11` |
| **Cross-process impact** | `DEP-05` |
| **Evidence required** | None |

### `REV-S-04` — **new finding produced by the correction**

`SCOPE-01` / `CTR-P03-06` / `P03-GAP-07`: master data may be owned by **no** scope via an
empty company, and a cost rate producing a `COMPANY`-scoped financial effect sits on such a
record. **This was not visible under the blanket assumption**, because a rule requiring
company context everywhere cannot express "this record legitimately has no company, and
that is exactly the problem". Ownership ≠ availability was the instrument that surfaced it.

**The correction produced a finding, not merely a relaxation.** Recorded because that is
the strongest evidence available that CORR1 was applied substantively rather than
cosmetically.

### `REV-S-05` — P03's first **downgrade** under CORR1

| Field | Content |
|---|---|
| **Original finding** | `18` §3 gave one row, *"Machine / equipment — `COMPANY`"* |
| **Scope assumption used** | That anything touching an asset is company-scoped |
| **Why over-constrained** | It conflates the **equipment register** with the **asset**. The register creates no financial effect of its own, so requiring company context on it is over-constrained, and company-optional is correct |
| **Correct scope analysis** | Register = `TENANT`, company-optional correct. Asset = `COMPANY`, unchanged. Work-centre **rate** = `COMPANY`, reinforced as `SCOPE-02` |
| **Updated classification** | **DOWNGRADED** for the register; unchanged for the asset and the rate |
| **Architecture impact** | Narrows `SCOPE-01`'s blast radius; `R-15` unaffected |
| **Cross-process impact** | Raised by P04; P03 **dissents** from extending the tenant reading to assets — preserved for P11 |
| **Evidence required** | None for the downgrade; `DEP-13` for `SCOPE-02` |

**This is the correction operating in both directions.** Before `R5`, `22` §3 recorded two
findings strengthened, one new, and **zero downgrades** — a pattern that is evidence of a
correction being applied selectively. A scope correction that only ever makes findings
worse is not being applied honestly.

### Findings checked and **not** materially affected

`DC-01` … `DC-10`, `DC-12`, `DC-13`, all of `02`, `03`, `04`, `05` §2–§3 and §5–§9, `07`,
`08`, `09`, `10`, `11`, `13`, `15`, and the Asset/COGS/Inventory boundary discipline.
**None used the tenant+company-everywhere assumption**, so none was re-run — CORR1 §6.

## 6. Research errors found in round 3

| ID | Error | Correction |
|---|---|---|
| `RE-P03-11` | **P03 recorded P04's count as nine.** P04's *message* said nine; P04's *pushed branch* said **seven**, and had said so before P03 wrote `25`. P03 cited the summary, not the source | `27` §2, `42` §3. The governing rule — *a peer's message is a summary; a peer's pushed branch is the source* — was already on file and was not applied |
| `RE-P03-12` | *"P03 rates this higher than P04 does"* on `DC-14` conflated a **denominator** question with a **ledger** question. On the denominator P04 was right | Framing **withdrawn** — `29` §6 |
| `RE-P03-13` | An `awk` row-counter returned a uniform `9` for every table, including empty ones. **Near-miss** — detected pre-publication because the figure was implausibly identical | Replaced with a parser validated against a positive control — `31` §4 |
| `RE-P03-14` | **`28` §3's headline said "One is live" while its own table marked three further mechanisms reachable.** Measured: four are live | Corrected by measurement — `28` §3. Third instance of a headline not reconciling with its own table in this package |
| `RE-P03-15` | `UNR-P03-09` was written as *"P03, next round"* when it was executable in one command | Executed the same session — `47` §2 |

**Five errors, four of them P03's own arithmetic or citation discipline.** The pattern is
consistent across all three rounds and is stated plainly rather than distributed: **this
package's recurring failure is not its searches — it is the totals and citations that
describe them.** `smeplus-totals-are-unverified-claims` names it exactly; the standing
correction is `42` §7.

## 7. Research errors found in round 4

| ID | Error | Correction |
|---|---|---|
| `RE-P03-16` | **"Material cost present" was an inference published as a measurement.** Round 3 counted valuation rows and inferred value reached the orders | Measured: **49** completed finished moves unvalued, **280** valued zero, **1,386** consumptions unvalued — `51` §4 |
| `RE-P03-17` | `53` §2 counted `DC-14` in two exposure classes and asserted a total that does not equal 15 | **Caught pre-publication by the `60` control** — the first instance of this class caught mechanically |
| **`RE-P03-18`** | **Round 3 reported containerised tooling as unavailable. It never checked.** Docker and Colima were already running and `postgres:17` was already cached | Checked and used read-only; `UNR-P03-07` closed. **This single unchecked assumption cost the package an entire database for a full round** — `62` §6 |
| **`RE-P03-19`** | **This round's own draft classified 5 defects as live**, having measured work-centre configuration and skipped the two posting gates | Measured the gates; live count is **1**. Round 3's figure was right after all — `53` §0 |

**Four errors. Three are the same failure**: a claim asserted where measurement was
available and cheap. `RE-P03-18` is the most costly the package has produced, and it is the
negative-claim standard applied to the session's **own capabilities** — the same error as
the 2026-09-03 Asset session declaring "no code access" from a working-tree search.

**Cumulative across four rounds: 9 research errors, 5 of them arithmetic or citation.** The
package's searches have been consistently sound; its summaries and totals have not.

## 4. Peer and prior-evidence position — unchanged by any revision

| Item | Position |
|---|---|
| Asset `BLK-01`, `BLK-02`, `BLK-07`, `BLK-08` | Quoted, unchanged, **not closed** |
| Asset `UNR-C-03`, `CTR-C-06` | Evidence supplied; **not closed** |
| COGS `JT-01/04/05` | Terminal HOLD, untouched |
| Inventory MTI rulings | Untouched; two items routed **to** them |
| P01, P02 | No output read; `DEP-06` raised as a question, not an answer |
| P11 | `DEP-11` raised as **PEER DEPENDENCY OPEN**; session did not wait |

## 5. Closure controls — `C-10`

Mechanical scans run over this directory at closure. Results are recorded in
`23_P03_EVIDENCE_MANIFEST.md` §3 and §4, which is generated after this file and therefore
carries the authoritative output.

Two controls were run:

1. **Prohibited-verdict scan** — for `PASS`, Team B / Team C authorisation, development
   authorisation, final freeze and merge wording. Required by
   `smeplus-subagent-pass-wording-defect`, which records that verdict wording drifts and
   must be checked before a session is called done.
2. **Layer-1 clean-room scan** — vendor model, field, path and file-extension tokens over
   `24_P03_CORE_RECON_HANDOFF_PACK.md`, the only Layer 1 file. Required by
   `smeplus-clean-room-rules`.
