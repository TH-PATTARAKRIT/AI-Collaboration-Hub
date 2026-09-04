# C02 — ACCOUNT_WAVE_A_ACCEPTED_CORRECTIONS_REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · reconciles all 20 accepted corrections into the canonical Wave A artefacts

**Lineage rule.** No prior finding is overwritten. The original claim, the reviewer finding, the
evidence and the corrected conclusion all remain visible. Where a correction supersedes a parent
claim, the parent claim is marked superseded, not deleted.

Disposition values: `CONFIRMED` · `CORRECTED` · `RESCOPED` · `RETRACTED` · `UNKNOWN` · `HOLD`.

---

## Part 1 — The twenty corrections

| # | Original claim | Reviewer finding | Corrected conclusion | Affected registers | Levels | Downstream semantic impact | Disposition |
|---|---|---|---|---|---|---|---|
| `COR-01` | No fiscal-year model exists in the tree | A fiscal-year model exists in the advanced accounting module | It exists, but as an optional, mutable, deletable **calendar override** with no state, close, posting or entry link | 01, 12, 21, 26; `NC-01` | L1, L9, L11 | **Strengthens** the close model: the reference has a year object and still attaches no close to it | `RESCOPED` |
| `COR-02` | Lock re-dates to lock+1 on create | Wrong code path; three mechanisms exist; one needs no lock | The accounting date is **system-derived**; for non-sale documents the derivation is unconditional | 01, 03, 04, 09, 10, 12, 19, 20, 26; `C07` | L2, L3, L5, L6, L11 | **Escalates.** Period attribution is altered even with no lock configured. Drives `DT-01`–`DT-06` | `CORRECTED` |
| `COR-03` | Whether deprecation blocks posting is unknown | It is blocked at three points, one without a bypass | Deprecation **is** a posting block; the residual gap is that an account holding a balance may still be deprecated | 02, 03, 04, 19 | L2, L3, L6 | Narrows a gap; strengthens `ST-11` | `CORRECTED` |
| `COR-04` | Lock exceptions are append-only | A revoke action escalates privilege past the read-only rule | Grant **and** revoke are held by one role; no segregation of duties | 04, 14, 20; `CONTRA-11` | L3, L7 | Moves the override control from "under-justified" to "structurally unsound" | `CORRECTED` |
| `COR-05` | Account code uniqueness has no DB constraint | The storage form makes a conventional constraint **inexpressible**; the duplicate search is unlocked | Not a hardening task — a modelling decision upstream of the constraint | 02, 14, 15, 19 | L2, L7, L8 | Changes the remedy, not the finding | `CONFIRMED` + extended |
| `COR-06` | The hash omits the transaction-currency amount | The write guard also fails open on the canonical amount field | Split into `CONTRA-01a` (guard fails, detector catches) and `CONTRA-01b` (neither) | 03, 15, 18, 20 | L2, L8, L11 | Sharpens severity; `01b` remains the true integrity hole | `CONFIRMED` + extended |
| `COR-07` | — (not in the parent) | The entry balance invariant is a suppressible application check with no DB constraint, while four lesser item rules are real constraints | **Control tiering is inverted** | 14, 18, 19, 20, 26 | L7, L11 | **New severe finding.** Proposed `T0-01` | `CONFIRMED` |
| `COR-08` | Merge is a provenance trade-off | It deletes by direct statement past the ORM's own guards and logs nothing | A **control bypass**, not a trade-off | 04, 10, 14, 20 | L3, L7 | Escalates to `T0-03`; reinforces `ST-26` `REJECT` | `CORRECTED` |
| `COR-09` | Over-reconciliation is a multi-currency risk | The reconciliation model has zero constraints; it applies in any configuration | Over-reconciliation is structurally reachable universally | 11, 18, 19, 20 | L6, L11 | Widens `P-06` failure; proposed `T0-05` | `CORRECTED` |
| `COR-10` | No rate-type dimension exists | Four rate types are derived at query time in the same module | Storage holds one measurement per date; **valuation bases are derived** | 02, 13, 21; `NC-02` | L2, L5 | **Improves** the model — becomes the positive position `ST-05` | `RESCOPED` |
| `COR-11` | — | The hash serialises company-currency amounts at the **foreign** currency's precision | A hash collision vector in multi-currency | 13, 15, 20 | L8 | Compounds `CONTRA-01b`; drives `ST-13` | `CONFIRMED` |
| `COR-12` | — | The hash chain keys on database row identifiers | Tamper-evidence **cannot survive migration** | 15, 16, 17, 20 | L8, L9, L10 | Drives `MG-10`, `ST-13`, `SB-03` | `CONFIRMED` |
| `COR-13` | (source registry omitted Thai localization) | Two localization modules are present in the verified build | Availability corrected; **content not adopted** | `EV-000`; `NC-03` | all | Statutory positions **unchanged — all remain `HOLD`** | `RESCOPED` |
| `COR-14` | — | A missing rate converts at 1:1, silently | **Reachable from the product's shipped initial state** (see `C06`) | 13, 18, 19, 20, 26; `C06` | L6, L11 | **Most severe finding in the Wave.** Proposed `T0-02`; `ST-27` `REJECT` | `CONFIRMED` + escalated by `C06` |
| `COR-15` | The posted freeze has a documented bypass | The bypass is used at seven production sites, one unconditionally | The posted invariant is **owned by the calling module** | 03, 10, 14, 20 | L2, L7 | Escalates `CONTRA-13`; drives `ST-28` `REJECT` | `CORRECTED` |
| `COR-16` | The numbering control parameter is tenant-writable and tenant-wide | Requires system administrator; the store has **no company dimension** | Wrong actor, wider blast radius: **every tenant in a shared database** | 03, 14, 16, 20 | L7, L9 | Re-filed from control matrix to SaaS boundary; `ST-29` `REJECT` | `CORRECTED` |
| `COR-17` | Cash-basis tax entries relocate to today when locked | Date selection ignores the tax lock, but the write is then refused | A **third outcome**: the reconciliation hard-fails | 11, 12, 19 | L3, L6 | Adds `RC-04`; routed to `WAVE-D TAX` | `CORRECTED` |
| `COR-18` | The identifier ceiling triggers at 10,000 companies | It triggers at company **identifier** ≥ 10,000, reached by cumulative creation | More likely, and sooner | 16, 20 | L9 | Raises likelihood of `SB-02` | `CORRECTED` |
| `COR-19` | Both immutability switches are runtime configuration | They are one-way ratchets defaulting off | Risk is fixed at **provisioning and first posting**, not at runtime | 03, 14, 15 | L7, L8 | Improves risk profile; sharpens `ST-12` | `CORRECTED` |
| `COR-20` | — | Thai statutory extracts are driven by the system-derived accounting date | Implementation fact recorded; **statutory consequence `HOLD`** | 05, 21; `C07` | L4 | Connects `COR-02` to statutory exposure; first item for the Accounting-Tax track | `HOLD` |

---

## Part 2 — Reconciliation into the canonical artefacts

Each correction now has a home. Where a parent register states a superseded claim, the correction
reference is the governing text.

| Canonical artefact | Corrections landing in it | Governing text |
|---|---|---|
| `01` L1 Domain Semantic Map | `COR-01`, `COR-02` | close model and date semantics per `COR-01`, `C07` |
| `02` Function Coverage Register | `COR-03`, `COR-05`, `COR-10` | `H-13`/`H-15` move `NC` → `PC`; `A-18` narrowed |
| `03` UI / Field Semantic Register | `COR-02`, `COR-03`, `COR-06`, `COR-15`, `COR-16`, `COR-19` | accounting-date row superseded by `C07` |
| `04` L3 Function Forensic | `COR-02`, `COR-03`, `COR-04`, `COR-08`, `COR-17` | `FN-04`, `FN-05`, `FN-09`, `FN-11` amended |
| `05` Cross-Module Map | `COR-20` | `XM-02` now cites the statutory chain |
| `09` Source of Truth Register | `COR-02` | accounting date confirmed `ACCOUNTING FACT`, system-owned |
| `10` State Transition Register | `COR-08`, `COR-15` | merge row and posted-freeze row amended |
| `11` Reconciliation Matrix | `COR-09`, `COR-14`, `COR-17` | `RC-01`, `RC-03`, `RC-04` |
| `12` Period Close Matrix | `COR-01`, `COR-02` | fiscal-year row rewritten per `NC-01` |
| `13` Currency & FX Matrix | `COR-10`, `COR-11`, `COR-14` | rate-type rows rewritten; `C06` governs the missing-rate row |
| `14` Control Matrix | `COR-04`, `COR-05`, `COR-07`, `COR-08`, `COR-15`, `COR-16`, `COR-19` | `IC-01` restated per `COR-07` |
| `15` Identity & Immutability | `COR-05`, `COR-06`, `COR-11`, `COR-12`, `COR-19` | immutability register amended |
| `16` SaaS Boundary | `COR-12`, `COR-16`, `COR-18` | `SB-01` and `SB-02` restated |
| `17` Migration Requirements | `COR-12` | `MG-10` restated |
| `18` L11 Proof Matrix | `COR-06`, `COR-07`, `COR-09`, `COR-14` | **superseded by `C08` (L11 re-run)** |
| `19` L6 Failure Register | `COR-03`, `COR-09`, `COR-14`, `COR-17` | `FE-06`, `FE-07`, `FE-27`, `FE-34` |
| `20` Contradiction Register | all | `CONTRA-01a`/`01b` split; `CONTRA-05`–`15` added |
| `21` Unknown / Gap Register | `COR-03`, `COR-10`, `COR-13` | `GAP-A04` closed; `GAP-H01` re-scoped; `TX-01`–`TX-07` unchanged |
| `22` Semantic Transfer Register | `COR-14`, `COR-15`, `COR-16` | `ST-05`, `ST-27`, `ST-28`, `ST-29` |
| `26` Final Gate Report | all | **superseded by `C10` (CORR1 gate report)** |

---

## Part 3 — Corrections that changed a decision

Only three corrections changed a **decision**, as opposed to sharpening a finding:

| Correction | Decision changed |
|---|---|
| `COR-10` | `ST-05` was going to be an `EXTEND` (SMEsPlus must design valuation bases). It became an **`ADAPT`** — the reference already implements the right separation |
| `COR-14` | Added `ST-27` **`REJECT`**, which did not exist in the first draft of the transfer register |
| `COR-07` | Reordered the `Tolerance = 0` proposals, placing the entry-balance invariant first |

**Seventeen of twenty corrections sharpened, escalated or rescoped an existing finding without
changing its direction.** That is the honest characterisation: the parent package's *direction* was
largely sound; its *precision*, and its handling of negatives, were not.
