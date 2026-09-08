# SA11 — STANDARDS AND AUDIT CONTROL MAP

Status: **HOLD**
Governing law: master prompt §16 — the Audit and Standards function participates *during*
Phase SA, not after design.

**No certification or compliance is claimed anywhere in this map.** The objective is to
determine which standards apply, what SMEsPlus must support, what evidence is required, and
where the gaps are.

---

## 1. Status vocabulary (master prompt §16)

`SUPPORTED BY EVIDENCE` · `CONTROL GAP` · `STANDARD GAP` · `EVIDENCE GAP` ·
`NOT APPLICABLE` · `RESEARCH REQUIRED`

---

## 2. Accounting standards identified in the baseline

| Standard | Where it binds | Requirement established | SMEsPlus control | Status |
|---|---|---|---|---|
| **TAS 2 ¶12** (inventories — conversion cost) | Manufacturing → Inventory valuation | Fixed production overhead — **expressly including depreciation and maintenance of factory buildings, factory equipment and right-of-use assets used in production** — forms part of conversion cost. The asset lineage records the finding *"exceeds the question: absorption is required, not merely permitted"*, closed as `BLK-03 — CLOSED — EVIDENCE VERIFIED` | none yet | **`STANDARD GAP`** — see `SA11-F-01` |
| **TAS 2 ¶13** (normal capacity) | Overhead absorption denominator | Absorption requires a normal-capacity denominator | none | **`RESEARCH REQUIRED`** — open blocker `BLK-07`, `HOLD — DESIGN DECISION REQUIRED`, **Boss-owned**; the asset lineage records an explicit veto that no costing implementation may begin before it |
| **TAS 2** (net realisable value / write-down) | Inventory valuation | NRV write-down is an authoritative requirement with **no reference pattern to learn from** — recorded as *"original design work for SMEsPlus, not adaptation work"* | none | **`STANDARD GAP`** |
| **TAS 16** (property, plant and equipment) | Depreciation method and convention | Gazetted text **unretrieved** | — | **`EVIDENCE GAP`** — open blocker on the asset side |
| **Thai VAT / withholding statute** | SA-D07 | Statutory registers, form codes, filing | Company-scoped per `BD-ACC-02` | **`EVIDENCE GAP`** — `0 of 78` Thai validations; no authoritative government source consulted for form codes |

### SA11-F-01 — a requirement-versus-mechanism gap, corroborated three ways

TAS 2 ¶12 **requires** fixed production overhead to be absorbed into inventory value.

The measured position across four deployed databases is that **fixed production overhead has
no path into inventory value**: seven of eight overhead elements have no source path at all,
and the eighth — machine cost via a work-centre rate — has a path that is *not enabled*
(1 of 60 work centres rated).

The one structurally plausible route is closed by construction. The depreciation entry writes
its analytic distribution onto **both** legs; the legs are equal and opposite; therefore
**the analytic dimension nets to zero on a depreciation entry and can never accumulate a
depreciation cost pool.** This was reached independently by three separate packages —
manufacturing, asset and analytic — and is recorded as structural, configuration-independent
and version-independent.

**This is not a configuration gap and not a defect to fix in place. It is a requirement with no
mechanism.** For SMEsPlus it is original design work, and it is gated behind the normal-capacity
decision (`BLK-07`) that only Boss can take.

**Negative-claim discipline applied:** the permitted wording is *"no path verified in the
examined deployments"*, never *"no path exists"*. The source-side half of the claim is bounded
to the generations actually read; the measured half is version-independent and is the
load-bearing one.

---

## 3. Internal control and audit requirements

| Control domain | Requirement | Evidence expected | Status |
|---|---|---|---|
| Segregation of duties | Identity-based self-approval exclusion; requester and approver distinguishable | approval record naming actor and time | **`CONTROL GAP`** — `XD-03`, the occurrence half populated on 0 of 27,874 rows |
| Approval authority | Amount threshold or configured N-level | approval record with mandatory rejection reason | `SUPPORTED BY EVIDENCE` on the buy side; **`CONTROL GAP`** on the sell side (`XD-02`) and on cross-module auto-created documents (`SA03-F-02`) |
| Audit trail immutability | Events immutable; a correction is a new linked event, never an edit or delete | event store | **`CONTROL GAP`** — specified (`MTI-38`/`MTI-39`), `0` proven |
| Event date vs entry date | Two distinct values | both recorded | `SUPPORTED BY EVIDENCE` as a specification (`MTI-38`) |
| Period lock integrity | A locked period cannot be written | control assertion | **`CONTROL GAP`** — locked-period entries recorded as silently re-dated; and a lock enforced by *refusing* one operation while *silently declining half* of another, telling the user nothing |
| Derecognition completeness | A disposal produces a posted, non-deletable entry | posted entry | **`CONTROL GAP`** — the derecognition entry is recorded as left in draft and silently deletable, and a blank account link drops the corresponding leg |
| Privileged bypass | No unaudited elevation; named grant with grantor, grantee, reason, scope, expiry | permanent record | **`EVIDENCE GAP`** — `MTI-18` specified; unverifiable until the bypass audit completes |
| Master-data control integrity | Values determining every future accounting entry are enforced below the interface | non-interface write path testing | **`CONTROL GAP`** — three of the four values determining every future depreciation entry are enforced **only at the user interface**, so every import, migration, integration and scripted correction bypasses all three |
| Evidence retention | The evidence that each invariant held is itself retained and inspectable | retained attestation | **`CONTROL GAP`** — `MTI-50` specified, `0` proven |

### SA11-F-02 — the recurring control shape is "enforced by the screen"

Three independent findings share one mechanism: values that determine accounting outcomes are
constrained only at the presentation layer — the asset master-data case above, the sell-side
credit and availability advisories (`XD-02`), and a display-only value that differs from the
value actually posted in the machine-cost case.

**SMEsPlus determination (Nature DNA, ND-06): a control that exists only in the user interface
is not a control.** Every constraint that determines an accounting outcome must hold on every
write path — import, migration, integration, scheduled job and API included. Independent
rationale: `MTI-30` already requires deferred executions to carry their authority; a
screen-only constraint is the exact complement of that rule and would defeat it.

---

## 4. SaaS and data-governance control domains

| Domain | Requirement | Status |
|---|---|---|
| Tenant isolation | No cross-tenant read, write, reference, aggregation or influence | **`CONTROL GAP`** — 58 invariants specified, `0` proven, `0 of 13` enforcement surfaces verified, `0 of 52` negative access tests executable |
| Company boundary | Closed; cross-company only through an enumerated register | **`CONTROL GAP`** — register empty, `0 of 3` entries proven |
| Existence non-disclosure | Absence must not leak existence through uniqueness or collision feedback | **`CONTROL GAP`** — `MTI-27` specified, unproven |
| Deny-by-default read scoping | Scoped before evaluation, not filtered after | **`CONTROL GAP`** — `MTI-21` specified, unproven |
| Offboarding / erasure | Bounded to exactly one tenant's data | **`RESEARCH REQUIRED`** — conditional |
| Change control | No customer fork of core, schema, posting, authorization, event logic or isolation rules | `SUPPORTED BY EVIDENCE` as a ruling (`MTI-D-03`) |

---

## 5. SA11-F-03 — the audit function has no consolidated standards map to inherit

Searched across the corpus for a consolidated mapping of SMEsPlus to control or accounting
standards. What exists is **standards cited inside individual findings** — TAS 2 in the asset
lineage, statutory tax in P07, control expectations distributed across the invariant sets.

**This map is the first consolidation.** It is therefore incomplete by construction: it can only
consolidate standards the baseline happened to name. Standards that no package has yet
encountered are absent from it, and this map must not be read as an applicability assessment.

Determining the applicable standard set — rather than collecting the ones already mentioned —
is a scoped piece of work that has not been done. Recorded as an open obligation for the
Audit/Standards function rather than silently presented as complete.

---

## 6. What this map does not claim

- No certification is claimed.
- No compliance conclusion is drawn for any standard.
- Thai statutory items remain `HOLD / EVIDENCE REQUIRED` and are routed to the tax track.
- TAS 2 ¶12's requirement is quoted from the package that established it; the gazetted primary
  text for TAS 16 remains unretrieved and is recorded as an evidence gap rather than assumed.

---

`CP-SA-70` (standards/audit half) — **HOLD**. Two standard gaps, one of them a requirement with
no mechanism corroborated three ways; nine control gaps; and no consolidated applicability
assessment exists.

Boss remains the sole Final Approver.

---

## 7. Addendum — the standards architecture that is approved but not built

### 7.1 The applicability register does exist, at Boss-decision level

`SA11-F-03` above stated that no consolidated standards map exists. That remains correct for a
*mapping artefact*. It requires one qualification: **the applicability register exists as a Boss
decision.** `05_BOSS_DECISION_STANDARDS_FIRST_AND_INTERNAL_AI_KNOWLEDGE_OF_TRUTH` (`fa57d10f`,
`APPROVED`) names the frameworks in scope:

| Layer | Frameworks named |
|---|---|
| Universal baseline | ISO 9001, ISO/IEC 27001, ISO/IEC 27701, ISO 22301, ISO 37301, **COSO Internal Control Framework** |
| SaaS baseline | ISO/IEC 20000-1, ISO/IEC 27017, ISO/IEC 42001, SOC 1, SOC 2 |
| Thailand baseline | **TFRS / TFRS for NPAEs**, Revenue Department e-Tax / e-Receipt, **PDPA**, accounting, tax, electronic-transaction and retention requirements |
| Industry packs | ISO 22000 / HACCP, IATF 16949, ISO 13485, ISO 45001, ISO 14001, ISO 50001 |

The same decision **specifies the traceability chain** —
`Framework → Version → Requirement/Clause → Control Objective → SMEsPlus Control → Process/Function → Test → Evidence → Conformance Result`
— with mandatory fields, and `04_BOSS_DECISION_SMT_GRC_ASSURANCE_STRUCTURE` assigns the
resulting five artefacts (control matrix, compliance requirement register, framework mapping
registry, control ownership matrix, audit-readiness gap register) to a named assurance office.

**None of those five artefacts was found**, searched by filename pattern across the corpus with
a firing filter. **`SA11-F-04`: the standards architecture is approved and specified in full, and
the artefact that would implement it does not exist.** This is the same *specified-not-built*
shape that `SA10-F-01` records for isolation.

### 7.2 The statutory register that does exist

`.../TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/B01_AUTHORIZED_INPUT_REGISTER.md` (`fa57d10f`) §7 is
the closest thing to a scoped statutory map, and each entry carries its own scope limit:

| ID | Requirement | Declared scope limit |
|---|---|---|
| RG-01 | Thailand Accounting Act B.E. 2543 — statements prepared, retained, independently audited | — |
| RG-02 | accounting records retained 5–7 years | — |
| RG-03 | e-Tax invoice/receipt integrity and authenticity (ETDA) | *"scope limited to e-Tax documents; does not extend to the general ledger without separate proof"* |
| RG-04 | tax invoice serial number (Revenue Code §86) | *"scope limited to tax invoices; gapless-numbering and general-ledger extension remain unproven"* |
| RG-05 | FX remeasurement at each reporting date (IAS 21) | — |

RG-03 and RG-04 are models of correct scoping: each states what it does **not** cover. Any
SMEsPlus design that extends gapless numbering from tax invoices to the general ledger is making
a new claim, not applying this one.

### 7.3 The internal-control objective set that does exist

`B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md`, status `B9 = COMPLETE.`, carries CO-01…CO-16 — the most
complete control-objective set in the baseline. Three are directly load-bearing for Phase SA:

- **CO-02 Segregation of duties** — must *support* maker-checker **without mandating it**,
  because *"an SME with two accounting staff cannot always achieve the segregation a larger
  enterprise can"*; and it is explicitly *"not evidenced as a specific Thai statutory
  requirement … stated as a design objective, not a regulatory claim"*.
- **CO-11 Evidence retention floor** — the longest applicable statutory minimum, enforced as a
  floor that **cannot be configured below**.
- **CO-16 Materiality is a policy input, never computed** — citing IAS 8 ¶5 and ¶41, verified
  from primary-source text.

Its own **residual scope boundary** is a limit Phase SA must carry: none of CO-01…CO-13 can
prevent a sufficiently privileged infrastructure-level actor from altering committed data or
audit evidence outside the domain's reach.

### 7.4 The two-person SME constraint is a design requirement, not a concession

The inventory control register records the reference pattern for inventory segregation of duties
as `None evidenced`, with the associated finding stating that *"a Thai micro-SME may have two
staff in total. A segregation model that cannot degrade gracefully to a two-person business will
be bypassed rather than followed"*, and recommending an explicit recorded compensating-control
path.

**SMEsPlus determination (Nature DNA, ND-08): segregation of duties degrades to a recorded
compensating control, never to a silent exception.** Where the organisation cannot separate two
duties, the system records that it could not, who accepted it, and against which control —
rather than either blocking the SME or pretending the segregation held. Independent rationale:
`CO-02` requires support without mandate, and `XD-03` shows what an unrecorded control produces —
nothing.

### 7.5 Correction to §5 of this map

`SA11-F-03` said the audit function has *no consolidated standards map to inherit*. Corrected by
population: **an applicability register and a traceability specification exist at Boss-decision
level; the five mapping artefacts they mandate do not.** The revised statement is `SA11-F-04`.
The original sentence overstated the absence, and the correction narrows it.

---

## 8. SA11-F-05 — an unqualified standards-compliance claim is live on every branch, including this one

**The claim.** `99_SMEsPlus_Enterprise_Suite/16_Learning_Analysis/01_SYSTEM_OVERVIEW.md`, under a
heading *"Standards Compliance"*, asserts without qualification:

> - ISO 27001 (Information Security)
> - ISO 9001 (Quality Management)
> - SOC 2 (Security & Availability)
> - GDPR (Data Protection)
> - Local regulations (Thailand)

**The repudiation, in the same corpus.**
`.../07_Output_From_AI/Phase_2.5_Knowledge_Consolidation/KNOWLEDGE_CONSOLIDATION_REPORT.md`
carries a *"Critical Confidence Flag"* recording that the file describes a generic greenfield
system that does not reconcile with the evidence base, and that its compliance claims and its
multi-role sign-off chain *"[do] not appear anywhere else in the repository's governance model"*.

**The governing rule it violates.** Boss decision `05` states:

> SMEsPlus does NOT claim that the customer is certified merely because SMEsPlus implements
> standards-aligned controls.

and its applicability register adds: *"No blanket compliance claim is created by this register."*
Boss decision `03` extends the same prohibition to ISO / SOC / PDPA / GDPR collectively, and
`AUD-10` forbids self-declaring customer certification.

**Verified independently for this register.** Both files were read at `origin/SMEsPlus`
`fa57d10f`, and the claim was confirmed present on **this session's own branch** at `HEAD`.
Both blobs are reported byte-identical across the corpus, so neither the claim nor its
repudiation is resolved on any branch.

**`SA11-F-05`.** A document asserting ISO 27001, ISO 9001, SOC 2 and GDPR compliance is live in
the repository, contradicted by another document in the same repository, and prohibited by two
standing Boss decisions. It is the exact claim class the programme forbids, and it has
propagated to every branch including the Phase SA branch.

**Class.** Not a research gap and not a design defect — a **live overclaim in published
material**. Its remedy is retraction or explicit quarantine, which is a governance act this
session has no authority to perform.

**Disposition.** Carried to `SA19` as a Boss governance item. **SMEs Core is the first detector.**

---

## 9. Framework applicability — measured, with the traps that were avoided

Frameworks **named** in the corpus, by declared search across all non-ignore remote branches:
TAS 1/2/8/16/18/21/23/36, TFRS 13/15/16, TFRS for NPAEs, IAS 1/8/16/21, IFRS 16, TFAC and its
promulgating announcement, the Thai commercial-registration prescribed statement forms, Revenue
Code s.65 bis (2) and the associated Royal Decree, the Thai Accounting Act, ETDA e-Tax, PDPA,
GDPR, COSO, SOC 1, SOC 2, ISO 9001, ISO/IEC 27001, ISO/IEC 27701, ISO 22301, ISO 37301,
ISO/IEC 20000-1, ISO/IEC 27017, ISO/IEC 42001, ISO 22000/HACCP, IATF 16949, ISO 13485,
ISO 45001, ISO 14001, ISO 50001.

Frameworks **searched for and not found**, each with the pattern declared and run across the
same population: US GAAP, COBIT, ITGC, SOX / Sarbanes-Oxley, ISAE, SSAE, ISQC, ISQM, PCAOB,
the internal-audit institute, ITIL, IFRS for SMEs, the interpretations committees, and the
Conceptual Framework.

### 9.1 Two false-positive traps, reproduced and corrected

| Trap | Unbounded result | Word-bounded result | Cause |
|---|---|---|---|
| `NIST` | 5 files | **0** | every hit is the substring inside *admi**nist**ration* |
| `SOX` | 175 hits | **0** in text | every hit is raw bytes inside one binary document |

Reproduced independently for this register on `origin/SMEsPlus`: unbounded 5, word-bounded 0.

**Why this is recorded in a standards map.** Either trap, left uncorrected, would have put a
control framework on the applicability list that the corpus has never cited. A standards map is
exactly the artefact where an unbounded token match becomes a false compliance scope.

### 9.2 SA11-F-06 — the accounting-standard work and the control-framework work occupy disjoint branch sets

The control-framework citations (COSO, SOC, the ISO family) live in two files of one directory,
carried on a minority of branches. **COSO is cited exactly once in the entire corpus.** The
accounting-standard work (TAS / TFRS / IFRS / IAS) lives on the research branches, which carry
no control-framework citation at all. One branch holds both.

For Phase SA this means the two halves of "standards" have never been read against each other:
the people establishing TAS 2 absorption were not working beside the people establishing the
control framework that would evidence it.

### 9.3 The statutory boundary, as the corpus itself draws it

The corpus admits only two sources as `THAI STATUTORY REQUIREMENT` for depreciation — a Revenue
Code section and its Royal Decree — and records that their rate tables are **maximums**, and
that using the **day** as the apportionment unit is `COMMON ERP PRACTICE`, on `HOLD`, because the
primary text says *period*. TAS 2 ¶12/¶13 are classed `ACCOUNTING STANDARD REQUIREMENT (TFRS)`,
explicitly **not** statutory.

Provenance discipline is likewise recorded: one standard was read at primary-source level while
its Thai counterpart was confirmed only through secondary sources and **was never silently
upgraded** to primary. `SA11` adopts that discipline: no statutory claim in this map rests on a
secondary source, and none is made.
