# 02 — ACCOUNT WAVE A · VERIFIED SEMANTIC BASELINE

**`PROVISIONAL / NON-AUTHORITATIVE / EVIDENCE-CONSUMER MODE`** · governed by `01` dependency register

> This file states **what is currently held true**, separated strictly by evidence class. It is a
> reconstruction of the parent evidence, not an addition to it. Nothing here is a design.

---

## 1. Reconciliation of the evidence base

| Round | Branch / state | Artefacts | Consumed |
|---|---|---|---|
| Core `L1–L12` | `research/account-wave-a-core-2026-09-04-001` | files `01`–`26` | yes |
| Challenge | same | `CHALLENGE/C1` | yes |
| Expert review | same | `EXPERT_REVIEW/X1`–`X4` | yes |
| `CORR1` | `research/account-wave-a-corr1-2026-09-04-001` | `C01`–`C14` + 2 fresh adversarial reviews | yes |
| `GAPCLOSE` | `research/account-wave-a-gapclose-2026-09-04-001` | `G01`–`G11` + 2 final reviews | yes |
| Method Convergence | `research/account-wave-a-mc-2026-09-04-001` @ `33cdc6f` | `01`–`12` + `LAYER2_MC_EVIDENCE` | yes |
| Method Convergence **Closure** | **uncommitted working tree** | `MCC_A`–`MCC_I`, `MCC_K`, master, `LAYER2_MCC_EVIDENCE` | yes — **`DEP-00`** |
| Parent expert/audit challenge | — | **`MCC_J` does not exist** | **no — never produced** |

**93 files reconciled + 20 rescued.** Correction lineage is preserved: every core file carries its
`CORR1` correction notice, and this baseline reads the **governing** text where they conflict.

---

## 2. `VERIFIED FACT` — structural findings that no round has contradicted

| # | Fact | Evidence | Negative class | Rounds surviving |
|---|---|---|---|---|
| `VF-01` | **Four identities a ledger needs have no carrier found in the searched scope**: accounting event, source event, tenant, period | `15 §1`, `EV-020` | `B` | all |
| `VF-02` | Within the **fourteen invariants the parent enumerated**, two were found unconditional: a hashed entry, and the hard lock date's forward-only movement | `P-15 §2`, **`NC-14`** | **`D — UNKNOWN`** · *"the enumeration is the package's own and is not proven exhaustive"* | contradicted at `CORR1` — the parent's own `L3` says **one**, not two |
| `VF-03` | **No temporal validity model was found in the searched scope.** No effective dating, no versioning, no period entity carrying state | `L5 §4`, `15 §3` | `B` | all |
| `VF-04` | **The accounting date is system-derived, not user input**, and is moved by a lock rule *and* by a numbering-convenience rule | `COR-02`, `C07` | — | `CORR1` onward |
| `VF-05` | **Restated after `NC-20`/`NC-21` (both class `E — CONTRADICTED` in part).** No **general** recognition-date carrier was found, but **purpose-specific carriers exist** (deferral start/end on the item; an asset depreciation start date). No **stored** tax-point field was found, but a **derived** tax point exists for cash-basis taxes via the reconciliation's maximum matched date. The posting timestamp has no accounting carrier. The tax lock and statutory extracts operate on the accounting date | `P-C07 §1`, **`NC-20`, `NC-21`** | `E` in part | **restated** |
| `VF-06` | **WITHDRAWN — `NC-22` class `E — CONTRADICTED`, four counterexamples verified**: the path is gated on an invoice test; non-period-resetting numbering returns the document date unchanged; `max(document date, today)` returns the document date when the document is dated today or later; and **the posting-time call IS lock-gated**. What survives: for *some* non-sale configurations the accounting date is derived rather than asserted | `P-C07 §2` **superseded by `NC-22`** | `E` | **contradicted** |
| `VF-07` | **Period attribution is derived from a numbering format**, which is itself deduced from the highest existing number in the journal | `C07 §2` consequence **C** | — | `CORR1` onward |
| `VF-08` | **What is locked is a range of accounting dates**, per company, per lock kind. There is no period, document or entry lock. Being locked does **not** mean refused — it means **re-dated** | `12 §1`, `COR-02` | — | all |
| `VF-09` | **Soft locks move backward freely**, with no distinct authority and no artefact | `12 §3` | — | all |
| `VF-10` | **No year-end result-transfer entry was found** within the core accounting and reporting modules — **class `B`** (`NC-04`); the only closing entry found is a tax-return posting, and **localization and third-party modules were not searched**; the year's result is computed at report time and never posted | `EV-016`, re-verified under `COR-01` | — | all |
| `VF-11` | **A missing rate converts at par, silently**, producing a valid-looking entry — and the resolver has **four** distinct fallback semantics across three modules | `CONTRA-08`, `COR-14`, `T0-07` | — | strengthened twice |
| `VF-12` | **Nothing bounds a match against the residual it discharges**, in any currency configuration | `COR-09`, `RC-01` | — | all |
| `VF-13` | **Matching records and analytic lines are destroyed silently** by an ordinary un-post | `EV-012`, `RC-02` | — | all |
| `VF-14` | **Account merge** retargets posted items, deletes accounts past the ORM's own guards, and **writes no record of any kind** | `EV-004`, `COR-08`, `AE-20` | — | all |
| `VF-15` | **No tenant concept exists.** The outermost boundary is the company group; account codes, currency rates and fiscal years are keyed to the group **root** | `EV-020`, `EV-001`, `EV-018`, `COR-01` | — | all |
| `VF-16` | **One configuration store has no company dimension at all** — one write disables a control for every tenant in the database | `SB-01`, `COR-16` | — | all |
| `VF-17` | **Tamper-evidence is keyed on storage row identifiers** and cannot survive a split, merge, restore or migration | `SB-03`, `COR-12`, `CONTRA-07` | — | all |
| `VF-18` | **Deletion evidence leaves the tenant** — it is written to the application log | `SB-04`, `EV-011` | — | all |
| `VF-19` | **Seven accounting events are emitted without an operator asking; four are invisible at the moment they occur** | `07` | — | all |
| `VF-20` | **16 company-consistency declarations on the company model do not execute at write** — they generate a client-side field domain, so the control is **present in the view layer and absent at write** (`G-C7`) | `T0-09`, `MCU-21` | — | MCC |
| `VF-21` | **The company-consistency enforcement surface is 9 of 22 models and 36 of 139 relational fields** | `MCU-21` | — | MCC |
| `VF-22` | **The reversal lineage pointer carries no constraint of any kind** — not unique, severable, server-written | `BW-35` | — | MCC |

---

## 3. `VERIFIED BUSINESS SEMANTIC` — meanings, not mechanisms

| # | Semantic | Evidence |
|---|---|---|
| `BS-01` | Everything in Wave A reduces to **seven facts**: classification identity, accounting event, financial fact, settlement fact, measurement fact, finality declaration, provenance. `F2 F3 F4 F7` are immutable; `F1 F5 F6` are governed | `L5 §1` |
| `BS-02` | The reference implements **four of the seven** as durable objects; implements finality as a bare date; and does **not implement provenance at all** | `L5 §1` |
| `BS-03` | The journal entry is the **accounting representation** of an accounting event — and in the reference it is also the event's **only durable record** | `L5 §2` |
| `BS-04` | **Realisation is caused by an event (settlement); revaluation is caused by a date.** Only the first belongs to the settlement mechanism | `13 §3` |
| `BS-05` | Reconciliation is **three separable things**: an immutable matching record, a derived settlement state, and an emitted accounting event. Unreconciling is **not an undo** — it is a further accounting event | `11 §1` |
| `BS-06` | **Measurement is stored once per date; valuation bases are derived per reporting purpose.** Closing, historical, average and current are *selection rules*, not second measurements | `COR-10`, `ST-05` |
| `BS-07` | An account is a **classification identity** that survives every renaming and renumbering; codes and names are labels resolved in a context | `EV-001`, `ST-01` |
| `BS-08` | A close is a **state the data must earn**, not a date someone types — the precondition pattern is the single best control found in Wave A | `ST-07`, `12 §4` |
| `BS-09` | **Month 12 is procedurally an ordinary month close** — independently corroborating the Boss baseline | `EV-016`, `ST-10` |
| `BS-10` | A **liquidity account belongs to exactly one legal entity** and is never shared | `EV-019`, `ST-06` |

---

## 4. `CONTROL REQUIREMENT` — derived, not optional

| # | Requirement | Source |
|---|---|---|
| `CR-01` | Every control-affecting configuration value carries a tenant dimension | `TI-01` |
| `CR-02` | No identity may be encoded by arithmetic over other identities | `TI-02` |
| `CR-03` | Tamper-evidence keys on business identity so it survives migration and tenant reshaping | `TI-03` |
| `CR-04` | All control evidence — including evidence of destructive acts — is stored inside the tenant's own data | `TI-04` |
| `CR-05` | Template-derived and tenant-created configuration remain distinguishable for the life of the tenant | `TI-05` |
| `CR-06` | Tenant isolation of ledger data and controls is a `Tolerance = 0` candidate | constitution principle 13 |
| `CR-07` | **The executor of every declared control must be proven.** A declared guard that cannot execute is not a control | `T0-09`, MCC method delta |
| `CR-08` | An accounting event emitted by the system is still an event: it needs an actor, a reason and a record | `07` |

---

## 5. `UNKNOWN / OPEN DECISION`

Full treatment in file `15`. Summary of the classes:

| Class | Count | Note |
|---|---|---|
| Gating unknowns standing at parent's last count | **17** | membership almost entirely different from the 17 it started with — **oscillating, not converging** |
| Tolerance-zero boundaries | **10 registered · 12 known** | **zero resolved.** Two returned by the parent's challenge are recorded **only in `MCC_J`, which does not exist** |
| Blockers | **8** (`GB-01`…`GB-08`) | `GB-08` new; `GB-02` widened twice; `GB-07` widened on a new axis |
| Orphan / unclassified unknown ids | **5** | `GAP-A03`, `GAP-A04`, `GAP-C01`, `GAP-G01`, `GAP-H03` |
| Boss decision items | at least **3** | retained earnings (`D-22`), tenant boundary (`GB-01`), lock cascade (`CL-05`) |

---

## 6. Negative claims carried into design — with their classes intact

Per the programme's negative-claim standard, these are the load-bearing negatives this package relies
on. **None is class `A` on a whole-system scope.**

| Claim | Class | Declared boundary | Design that rests on it |
|---|---|---|---|
| No accounting-event identity exists | `B` | the primary module tree; **962 manifested modules unsearched** (`GB-07`, `MCU-18`) | `D-01`, `D-24` |
| No **general, mandatory** provenance carrier found | `B`, **partly `E`** (`NC-05`) — **typed origin links DO exist**: payment origin, recurring-entry origin, cash-basis origin, statement-line link, plus a free-text origin field | core accounting models and wizards; 962 modules unsearched | `D-04`, `D-29` |
| No revaluation posting mechanism found | `B` | the scope read at `L1–L12` (`GAP-H01`) | `D-23` |
| No record rule on either reconciliation model | **`A`** | the primary tree, independently re-verified | `D-31` context |
| No raw-SQL write to the rate table | **`A`** | **791 primary directories + 962 manifested modules** (`MCC_E` `E-C3` — the cited *"1,752 module directories"* conflated two populations and was corrected; **3 stray modules were missed entirely**) | retires the `FX-08` hold — see `D-10a`. **Until `MCC_F` `F-01`'s re-test is confirmed to cover the 3 stray modules, this retirement rests on a corrected denominator** |
| No v16/v14 framework core in the searched roots | `C` | project custom modules only | **must never be reported as "the constraint has always existed"** (`MCU-19b`) |

> **The first three are the exposure.** Three `PROVISIONAL` designs rest on class-`B` negatives
> whose boundary the parent has itself proven wrong. They are labelled `PROVISIONAL` because the
> *positive* evidence for them is strong and multi-round — not because the negative is settled.
