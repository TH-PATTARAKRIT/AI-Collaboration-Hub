# P09_SOURCE_LINK_REGISTER

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. **This register deliberately contains no reference-product file path, model name or method name.** Those live in the Layer 2 quarantine and are cited from Layer 1 only by evidence identifier.

---

## 1. WHAT THIS REGISTER IS FOR

It records **where each Layer 1 claim's evidence lives**, so that any claim can be traced to a source read without Layer 1 carrying vendor identifiers.

## 2. EVIDENCE SOURCES USED BY THIS SESSION

| ID | Source class | Description | Layer | Read by |
|---|---|---|---|---|
| **SRC-01** | primary source | reference-pattern enterprise build, principal addons root — 790 module manifests | 2 | research team + all four experts |
| **SRC-02** | primary source | reference-pattern archive addons root — 959 manifests, of which 448 are timestamp-suffixed duplicates | 2 | research team + three experts |
| **SRC-03** | primary source | platform core (object-relational layer, field layer, model-definition model, cache, registry, system-parameter model) | 2 | X2, X4 |
| **SRC-04** | primary source | tenant custom addon set, copy A — 65 modules | 2 | research team, X3 |
| **SRC-05** | primary source | tenant custom addon set, copy B — 57 modules | 2 | research team, X3 |
| **SRC-06** | primary source | tenant custom addon set, copy C — 47 modules | 2 | research team, X3 |
| **SRC-07** | primary source | the module upgrade script for the analytic surface | 2 | X2 |
| **SRC-08** | primary source | the reference pattern's own automated tests, used as corroboration for one behavioural claim | 2 | X3 |
| **SRC-09** | primary source | client-side allocation component and its template | 2 | X4 |
| **SRC-10** | project standard | the negative-claim standard (classes A–E, declared boundaries) | 1 | all |
| **SRC-11** | project standard | the denominator rule (population, pattern, path set, unit, independence) | 1 | all |
| **SRC-12** | governing instruction | the P09 process directive | 1 | all |
| **SRC-13** | governing instruction | the scope-aware constitution correction | 1 | research team |

**Not used, and declared:** no running database, no runtime dump, no user-interface session, no deployment environment. **Every operational consequence in this package is therefore stated as a code-path conclusion and explicitly hedged as unexecuted.** Where a claim would require execution, it is marked so and routed in `P09_DEPENDENCY_REGISTER` §C.

## 3. LAYER 1 CLAIM → EVIDENCE MAP

| Layer 1 document | Principal evidence identifiers | Sources |
|---|---|---|
| `01` Management Accounting Model | EV-P09-010…015, 021…024, 027…036, 060, 065, 070; COR-P09-03 | SRC-01, SRC-03 |
| `02` Analytic Semantic Model | EV-P09-025, 026, 031, 100…106, 110…113; COR-P09-02, COR-P09-05 | SRC-01 |
| `03` Analytic Distribution Matrix | EV-P09-016…024, 115; COR-P09-01, COR-P09-02 | SRC-01, SRC-02 |
| `04` Cost Object Model | EV-P09-013, 111, 117…119; COR-P09-04, COR-P09-06 | SRC-01, SRC-04…06 |
| `05` Budget Control Model | EV-P09-060…070 | SRC-01 |
| `06` Actual vs Budget Trace | EV-P09-061…064, 100…103; X1-05, X1-06, X1-07 | SRC-01 |
| `07` Financial vs Management Boundary | EV-P09-016, 025, 026, 031, 040…053, 100…113 | SRC-01 |
| `08` Event-to-Analytic Matrix | EV-P09-047, 103…113; COR-P09-01, COR-P09-02, COR-P09-05 | SRC-01, SRC-02 |
| `09` Cross-Process Ownership | X3-01…X3-05, EV-P09-107 | SRC-01, SRC-04…06, SRC-08 |
| `10` Edge Case Matrix | the full evidence base plus all four challenge verdicts | SRC-01…SRC-09 |
| `11` Contradiction Register | all of the above | all |
| `19` Scope Ownership Matrix | EV-P09-010, 013, 021, 027…031, 070, 114…116; COR-P09-03 | SRC-01, SRC-03, SRC-13 |

## 4. GITHUB EVIDENCE

| Item | Value |
|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical branch | `SMEsPlus` — **not touched by this session** |
| Working branch | `research/account-p09-plan-to-analyze-2026-09-04-001` |
| Base commit | `88f52cd` — *governance: approve canonical evidence acquisition flow* |
| Package path | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_P09_PLAN_TO_ANALYZE/` |
| Merge status | **not merged, not requested.** Boss decides. |
| Session commit | **`16f884f`** |

## 5. JIRA EVIDENCE

**No Jira issue was created or transitioned by this session.**

The connectors required to do so are not authorised in this execution environment: the Atlassian and related servers require an interactive authorisation flow that a non-interactive session cannot complete. This is recorded as a **factual limitation of the environment**, not as a decision, and not as evidence that no Jira control applies.

**Class B** — no Jira evidence was retrievable within this session's authorised capability. To publish Jira evidence for P09, the Atlassian connector must be authorised from an interactive session or via the claude.ai connector settings; the capability is unavailable until then. Routed as `DEP-P09-11`.

## 6. CROSS-SESSION REFERENCES

| Reference | Relationship to P09 |
|---|---|
| Account Wave A Core Ledger study | P09 **inherits** its finding that no accounting-event identity and no provenance carrier exist; this becomes `DEP-P09-01`, P09's blocking dependency and the ground for `AAS+-VETO-01` |
| Asset deep research | P09 hands over the equipment↔asset bridge finding (PD-02); it does **not** adjudicate against that track's conclusions |
| Inventory multi-tenant invariant work | P09's scope-ownership determinations are P09's own; reconciliation with that track's invariants is a P11 matter |

**P09 does not adjudicate between parallel evidence tracks.** Where another branch's evidence overlaps, it is cited as a pointer only.

## 7. TERMINAL STATE

**REGISTER ISSUED. 13 SOURCES DECLARED. ONE EVIDENCE CHANNEL (JIRA) UNAVAILABLE AND RECORDED AS CLASS B WITH ITS CAUSE. NO GATE MOVED.**
