# P08_REVISION_LOG
*(serves as this session's `RESEARCH_ERROR_AND_REVISION_LOG` required by correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` §6)*

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

Corrected text is **not deleted**. Every superseded position stands with its supersession recorded.

## 1. Revisions made by the session on its own findings, before any external review

| ID | Original position | What changed it | Corrected position |
|---|---|---|---|
| `REV-01` | "Persistence-layer invariants do not exist on the core accounting tables; every control is application-level." | Reading the table-initialisation routines rather than only the declared constraint blocks | **Corrected.** Database-level objects **do** exist: a partial unique index on the entry number scoped by (number, book) for posted non-placeholder entries; a per-item check that debit and credit are not both non-zero; a per-item sign-coherence check. What does **not** exist is any database constraint on per-entry balance. The corrected form is narrower and stronger. |
| `REV-02` | The seal's protected attribute set was recorded as fixed. | Reading the version selector in both attribute-set definitions | **Corrected.** The set is selected by a **caller-supplied version value**, and the older version's set omits the entry number. |
| `REV-03` | The lock-bypass sentinel was initially grouped with the other suppression parameters. | Reading the comparison operator | **Corrected.** It is an object-identity comparison and therefore **cannot** be satisfied by a client-supplied context. It is server-side only. Grouping it with the string-keyed parameters would have overstated the attack surface. |

`REV-03` matters: it is a correction that made a finding *less* severe, and it is recorded with the same weight as the ones that made findings worse.

## 2. Revisions required by the scope-aware constitution correction

Correction `SMEPLUS-26-09-04-ACC-REV2-CORR1`, received mid-execution. Columns as mandated: original finding → scope assumption used → why over-constrained → correct scope analysis → updated classification → architecture and cross-process impact.

| ID | Original finding | Scope assumption used | Why over-constrained | Correct scope analysis | Updated classification | Impact |
|---|---|---|---|---|---|---|
| `SC-REV-01` | "No tenant dimension exists on the currency model, the rate model, the journal item or the company — a gap." | Tenant + company mandatory for every operation | A currency unit and a published rate observation are **platform reference data**. Requiring a tenant context on them would make shared reference data unusable and would force every tenant to re-source public information. | Split into four objects: unit (`PLATFORM`), observation (`PLATFORM`), policy (`TENANT`), **rate applied to a posting** (`COMPANY`). | **Not a gap** for the first two. **Gap stands, and sharpens,** for the fourth: a posted financial fact must carry its owning tenant and company and does not. | GB-08 facets `1a` and `4d` re-scored from `SILENT` to `VIOLATES` **for the posted fact only** |
| `SC-REV-02` | "The statement definition models carry no company dimension and no isolation rule — a leak." | Same | A **statutory statement layout** is platform reference data. Adding a company dimension to it would let each tenant edit its own statutory format, which is worse than the defect it fixes. | Statutory layout `PLATFORM` and immutable to tenants; management layout `TENANT`; produced statement `COMPANY`. | Reclassified — **but not "no gap"**. The scope is right and the *protection* is absent: one ordinary accounting role holds full create/update/delete over every statement definition, with no change history. The defect is that **one object serves all three scopes** (class `SV-2`) **and that none of the three is protected**. | `P08-RQ-RP-01` replaces "add a company field" |
| `SC-REV-03` | "Shared master data — counterparties, payment terms, rounding profiles — is not company-isolated; this is the leak surface." *(The draft also listed currencies here; that was an error — a currency unit is `PLATFORM`, not `TENANT`. Corrected after independent review.)* | Same | These are legitimately **tenant-scope** objects. Company-isolating them would forbid a tenant from maintaining one customer list across its own companies. | `TENANT` scope, correct as shared. | **Not a gap.** The defect is the **reach-through** (class `SV-3`): a tenant-scope mutation rewriting company-scope posted facts. | `P08-RQ-SH-01`, and the generalised rule `KRN-INV-05` |
| `SC-REV-04` | "The system configuration parameter store has no company dimension — a leak." | Same | The store is correctly `PLATFORM`. | `PLATFORM`. | **Not a gap in the store.** The defect is that **tenant and company accounting policy is kept in it** (class `SV-5`). | `P08-RQ-SH-02` |
| `SC-REV-05` | Retention / audit-trail policy was recorded as a company setting that is off by default — a weakness. | Same | The correction **tightens** this one. Whether posted facts may ever be erased is not a company's decision about itself: an administrator who can disable retention can erase the evidence of their own erasure. | `PLATFORM`, or `TENANT` with no path to disable once any fact exists. | **Escalated** from a weakness to a tolerance-zero candidate, `P08-T0-05`. | `P08-RQ-CL-01` |
| `SC-REV-06` | The fiscal calendar was recorded as delegated to the company-tree root, without comment. | Same | A fiscal year is a legal attribute of a legal entity, so its scope is `COMPANY`. The benchmark's delegation is an **over-constraint in the benchmark**. | `COMPANY`. | New contradiction `P08-CONTRA-09`; new open question `P08-SC-U-01`. | `P08-RQ-PC-08` |

**CORRECTED after independent review.** The draft of this section closed with a sentence declaring the posting-engine, entry-identity, close-mechanism, report-derivability and settlement sets "not materially affected, and therefore not re-run". **That declaration was false as written**, and four of the five sets it named were re-analysed under the correction — two of them in the table four lines above it. The declaration is withdrawn and replaced by the accurate split below. No finding was quietly withdrawn or softened; what was wrong was the account of what had been done.

| Set | Re-analysed under the correction? | Where | Did a conclusion change? |
|---|---|---|---|
| Close-mechanism set | **yes** | `SC-REV-06` — the fiscal calendar re-scoped to `COMPANY`, opening `P08-CONTRA-09` and `P08-RQ-PC-08` | no conclusion changed; a classification and a rationale did |
| Report-derivability set | **yes** | `SC-REV-02` — statement layouts re-scoped, `P08-RQ-RP-01` replacing "add a company field" | no conclusion changed; the **remedy** changed |
| Entry-identity set | **yes** | `04` §2 — `AID-04`, `AID-07`, `AID-08` re-analysed, producing `AID-SC-01` and `AID-SC-02` | no conclusion changed; two findings gained a violation class |
| Settlement set | **partly** | `01` §2.4 — `REC-06`/`REC-07` re-classified as `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY` | no conclusion changed; severity framing did |
| Posting-engine integrity set | **no** | — | not re-run |
| The attack file | **partly** — `AT-17` and `AT-18` re-diagnosed as scope classes; the other twenty not re-run | `16` | no |

Evidence, citations, checkpoints and commit lineage are preserved unchanged throughout. The distinction the six-column mandate exists to capture — *classification and rationale changed, conclusion did not* — is now recorded, which the withdrawn sentence prevented.

## 3. Method revision made during the session

| ID | What changed | Why |
|---|---|---|
| `REV-M-01` | The session began bound by the programme rule forbidding any class-`A` absence while the root set is undeclared, and would have had to downgrade every absence to class `C`. Instead it **declared and proved the root set** and re-ran three high-impact negatives across all 22 roots. | Downgrading would have been compliant and useless. The prohibition exists because the root set was unknown; the correct response to an unknown that is cheap to close is to close it. Recorded in `01A_P08_ROOT_SET_DECLARATION.md`. |
| `REV-M-02` | A fourth negative was scanned across all 22 roots and **declined promotion**, because its pattern is vocabulary-based rather than structural and its matches were not each opened. | The same discipline that permits the three promotions forbids the fourth. Recorded as `RS-B-01`, class `B`. |

## 4. Independent-review revisions

Recorded in `22_P08_AAS03_CHALLENGE.md`. Every reviewer finding is verified before acceptance; findings reduced or rejected on verification are recorded alongside those accepted, so that the reviewer's own error rate is visible.

## 5. Revisions arising from an inbound peer finding (P04 — Acquire-to-Retire)

Full handling in `09A_P08_PEER_INBOUND_P04_LOCK_REDATE.md`. Every peer claim was verified against primary source before acceptance.

| ID | Original P08 position | What changed it | Corrected position |
|---|---|---|---|
| `REV-P-01` | "Posting silently relocates the accounting date when the requested date falls in a locked period." Which locks participate was left unstated. | P04's finding, verified: the violation lookup used by the posting routine passes the hard-lock flag set | **Corrected and sharpened.** The **irrevocable** lock also relocates rather than refuses on this path. The prior wording would have been read as implying the irrevocable lock refuses, and it does not. |
| `REV-P-02` | "There is no subledger; it is a projection." | P04's finding, accepted: the fixed-asset register and the inventory valuation record are **genuine separate stores** | **Corrected — the original was too broad.** The *partner* subledger is a projection. Where a genuine subsidiary store exists, the kernel imposes **no reconciliation obligation at all**. New requirement `P08-RQ-KRN-01`. The absence of a reconciliation mechanism is class `C` for P08, which did not run that search. |
| `REV-P-03` | The kernel assumed one measurement basis per fact, without saying so. | P04 re-opening the tax-book gap | **Made explicit.** New requirement `P08-RQ-KRN-02` and new decision `P08-BD-11`. The statutory half is `HOLD / EVIDENCE REQUIRED` and no P08 conclusion rests on it. |

`REV-P-02` is the most important revision in this log: it was produced by a peer working in a different domain, and neither this session's own work nor its four commissioned adversarial reviews had surfaced it.

---

# CLOSURE DELTA — targeted forensic closure

**19 corrections. 0 self-caught.** Each was re-run by the author against primary evidence before adoption; each carries a contradiction ID; the withdrawn wording is quoted, not replaced.

| Wave | Corrections | Source |
|---|---|---|
| Author revalidation, phases A–C | 3 first-pass class-A results withdrawn as pattern artefacts; the version premise broken and repaired; the accounting-event class-A claim withdrawn | self |
| **AAS-03 expert challenge** | **19 further, none self-caught** — `P08-CONTRA-22` … `-42` | E1, E2, E3, E4 |
| Author follow-through on the experts' one convergent lifting condition | The package had **searched the wrong custom tree**; a tax-period carrier P08 had told a peer could not exist is populated on 61,157 posted entries | self, prompted |

**Two reviewer claims were rejected on verification** and are recorded as rejected in `48` §5. Reviewer findings are not automatically true.

**The correction of a correction:** the author's own re-run of the orphan population reached 9,754; a third reviewer showed the correct figure is **6,585**. A correction is not exempt from the discipline it applies.
