# P06_SCOPE_OWNERSHIP_MATRIX.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Created under:** `[SMEPLUS-26-09-04-ACC-REV2-CORR1]` — Scope-Aware Constitution Correction
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. Why this file exists and what it supersedes

The opening P06 directive carried the wording *"Tenant/Company boundary mandatory."* Correction CORR1 supersedes any reading of that as blanket enforcement. The canonical rule is **SCOPE-AWARE EVERYWHERE**: every material object and operation must first determine its applicable scope from **PLATFORM · TENANT · COMPANY**, and context requirements follow the proven scope — they are not assumed.

Applied definitions:
- **TENANT** = security / customer boundary.
- **COMPANY** = legal / accounting / business boundary.
- **OWNERSHIP ≠ AVAILABILITY.** Ownership scope ≠ operational scope ≠ financial scope ≠ reference scope.
- **Unrelated independent companies are separate tenants by default.**
- Missing required scope, or unprovable ownership, = **DENY**.

**This session was NOT reset.** All evidence, source links, findings and blockers raised before the correction stand. What follows is (a) a scope determination for every material P06 object, and (b) a named revalidation of the findings the earlier wording materially affected.

---

## 2. Scope determination method

For each object the eight CORR1 questions are answered where applicable: what scope **owns** it, **executes** on it, may **access**, **mutate** and **reference** it; whether it creates a **financial effect**; and if so which **company** owns that effect.

Determination is made from business/legal/accounting semantics first, corroborated by source evidence. Where source evidence and semantics disagree, that disagreement is itself the finding. Where neither settles it, the row reads **HOLD — SCOPE EVIDENCE REQUIRED** and unaffected work continues.

---

## 3. The matrix

Legend: **OWN** = owning scope · **EXEC** = executing scope · **FIN** = creates a financial effect · **Ref-impl** = what the reference implementation's own field structure implies.

| # | Object | OWN | EXEC | ACCESS | MUTATE | REFERENCE | FIN | Ref-impl says | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| S-01 | Currency | PLATFORM | PLATFORM | all | PLATFORM | all | no | global | agreed |
| S-02 | **Currency rate** | **TENANT** | TENANT | tenant | TENANT | tenant | indirectly | global, with a company-scoped reporting overlay | **see SCOPE-F-01** |
| S-03 | Chart of accounts / GL account | COMPANY | COMPANY | company | COMPANY | company | yes | `company_id` present | agreed |
| S-04 | Bank journal | COMPANY | COMPANY | company | COMPANY | company | yes | `company_id` required; `_check_company_domain_parent_of` | **see SCOPE-F-02** |
| S-05 | **Physical bank account (`res.partner.bank`)** | **COMPANY** | COMPANY | company | COMPANY | company | yes | `company_id` is an **optional, derived** related field, and `False` is admitted everywhere | **CONTRADICTION — SCOPE-F-03** |
| S-06 | Bank statement | COMPANY | COMPANY | company | COMPANY | company | yes | via journal | agreed |
| S-07 | Bank statement line / bank event | COMPANY | COMPANY | company | COMPANY | company | yes | `company_id`, `check_company=True` | agreed |
| S-08 | Journal entry (`account.move`) | COMPANY | COMPANY | company | COMPANY | company | yes | `company_id` | agreed |
| S-09 | Payment | COMPANY | COMPANY | company | COMPANY | company | yes | `company_id`, `_check_company_auto` | agreed |
| S-10 | **Reconciliation (partial / full)** | **COMPANY** | COMPANY | company | COMPANY | company | yes | guarded at **`root_id`**, not `company_id` | **CONTRADICTION — SCOPE-F-04** |
| S-11 | Reconcile model (matching rule) | COMPANY | COMPANY | company | COMPANY | company | yes (via write-off) | `company_id` present | agreed — but see SCOPE-F-05 |
| S-12 | Payment method (definition) | PLATFORM | — | all | PLATFORM | all | no | global reference | agreed |
| S-13 | Payment method **line** (account binding) | COMPANY | COMPANY | company | COMPANY | company | yes | journal-bound | agreed |
| S-14 | Payment provider configuration | **TENANT or COMPANY** | COMPANY | — | — | — | yes | `company_id` required, immutable once transactions exist | **HOLD — SCOPE-F-06** |
| S-15 | Payment token | COMPANY (derived) | COMPANY | see below | — | — | no directly | `related='provider_id.company_id'`; record rule uses **`parent_of`** | **CONTRADICTION — SCOPE-F-07** |
| S-16 | Payment transaction | COMPANY | COMPANY | company | COMPANY | company | yes | `related='provider_id.company_id'` | agreed |
| S-17 | Online bank connection (`account.online.link`) | TENANT or COMPANY | COMPANY | — | — | — | yes | journal-bound | **HOLD — SCOPE-F-08** |
| S-18 | Bank transaction identity (`unique_import_id`) | COMPANY | COMPANY | company | none | company | no | **database-global UNIQUE**, value-namespaced only | **CONTRADICTION — SCOPE-F-09** |
| S-19 | Lock dates / period close | COMPANY | COMPANY | company | COMPANY | company | yes | company fields, with parent inheritance for soft locks | agreed |
| S-20 | Suspense account | COMPANY | COMPANY | company | COMPANY | company | yes | journal/company | agreed |
| S-21 | Inter-bank transfer account | COMPANY | COMPANY | company | COMPANY | company | yes | `company_id` | agreed |
| S-22 | FX gain/loss accounts and journal | COMPANY | COMPANY | company | COMPANY | company | yes | `company_id` | agreed |
| S-23 | Payment tolerance parameter | COMPANY | COMPANY | company | COMPANY | company | **yes — it decides whether an invoice closes** | reconcile-model field, `tracking` only | agreed on scope; **control gap stands** (RM-F-19) |
| S-24 | Bank statement import format parser | PLATFORM | — | all | PLATFORM | all | no | module code | agreed |
| S-25 | Cheque number sequence | COMPANY | COMPANY | company | COMPANY | company | no | journal-bound | agreed |
| S-26 | Batch payment | COMPANY | COMPANY | company | COMPANY | company | yes | single-journal constraint | agreed |
| S-27 | Thai withholding-tax rule set | **PLATFORM reference + COMPANY application** | COMPANY | — | — | — | yes | custom modules, company-bound | **HOLD — statutory, routed to Accounting-Tax** |
| S-28 | Employee advance request (custom) | COMPANY | COMPANY | company | COMPANY | company | yes | company-bound | agreed |
| S-29 | Bank reconciliation report | COMPANY | COMPANY | company | — | company | no | company-scoped | agreed |
| S-30 | Cross-company (intercompany) settlement | **two COMPANY scopes, one TENANT** | COMPANY ×2 | tenant | COMPANY | tenant | yes ×2 | no payment support at all | **see SCOPE-F-10** |

**Rows: 30.** **DENOMINATOR:** POPULATION: material objects appearing in the P06 semantic trace (Module→Model→Field→Function→Payment Event→Bank Event→Accounting Event→Journal→Settlement→Reconciliation→Report) as evidenced in this package. UNIT: object. **This is the P06 object set, not a census of every object in the system** — Class B for anything outside it.

---

## 4. Scope findings

**SCOPE-F-01 — Currency rate is TENANT-scoped, and the reference treats it as global.**
A rate table is a shared reference the customer maintains; it is not a legal-entity fact, and two unrelated customers must not share one. Under the corrected model that is **TENANT**, not PLATFORM and not COMPANY. The reference implementation holds rates globally with a company-scoped *reporting* overlay (`$V18E/account/models/res_currency.py:178,206,307`).
**Consequence:** rate governance is a tenant-level control the target must supply. The four parity fallbacks (FX-F-06, FX-F-07) are therefore **tenant-scope failures**, not company-scope ones — one missing rate degrades every company in the tenant simultaneously. This *raises* the severity of FX-R-02.

**SCOPE-F-02 — Journal is COMPANY-scoped, and the reference deliberately admits parent-company journals.**
`$V18E/account/models/account_journal.py:43` opts into `_check_company_domain = models.check_company_domain_parent_of`, whose contract (ORM core, `odoo/models.py:188-194`) admits a record whose `company_id` is a **parent** of the given companies, **or whose `company_id` is `False`**.
**Scope verdict:** admitting a parent company's journal into a child company's operation is a COMPANY-boundary crossing for any *financial* effect. Admitting `company_id = False` is worse — it is an unowned object, and CORR1 is explicit that **unprovable ownership = DENY**.

**SCOPE-F-03 — A physical bank account is COMPANY-owned, and the reference makes its ownership optional and derived. CONTRADICTION.**
`$V18E/base/models/res_bank.py:86` — `company_id` is `related='partner_id.company_id', store=True, readonly=True`. It is **not required**, and a partner with no company yields a bank account with no company. Three separate guards then explicitly admit that case:
- `check_company_domain_parent_of` admits `company_id = False` by contract;
- `$V18E/account/models/account_journal.py:469` — `if journal.bank_account_id.company_id and ...` — a `False` company skips the check entirely;
- `$V18E/account/models/account_bank_statement_line.py:514` — `return bank_account.filtered(lambda x: x.company_id.id in (False, self.company_id.id))`.
And the uniqueness constraint is partner-scoped, not company-scoped (`$V18E/base/models/res_bank.py:89-93` — `unique(sanitized_acc_number, partner_id)`).
**Verdict: a real bank account — the most company-specific object in the entire treasury domain — can exist unowned and be used by every company in the database.** Under CORR1 this is a DENY condition that the reference does not enforce. Raised as `P06-B-26`.

**SCOPE-F-04 — Reconciliation is COMPANY-scoped, and the reference guards it at ROOT. CONTRADICTION, with a caveat.**
`$V18E/account/models/account_move_line.py:2336-2340`:
```
if len(self.company_id.root_id) > 1:
    raise UserError(_("Entries don't belong to the same company: %s",
```
The guard raises only when the lines span two different **roots**. Sibling companies under one root reconcile freely. The bank-rec matching domain is widened to match: `$V18E/account/models/account_bank_statement_line.py:518` uses `child_of self.company_id.root_id.id`, and `:525` carries an in-code comment saying the widening is deliberate.
**The caveat, stated honestly:** whether a set of companies sharing a `root_id` represents *one legal entity with branches* or *several distinct legal entities* is a **configuration and legal question this session cannot settle from source**. If they are branches of one legal entity, root-scoped reconciliation is correct at COMPANY scope. If they are distinct legal entities, it is a COMPANY-boundary breach.
**What the runtime evidence does and does not show (added by AAS3-C-02):** extract S-04 shows companies C1 and C2 with **disjoint bank journals and different legacy chart-of-account code ranges** — suggestive of distinct accounting entities. It is **silent on their `parent_id`/`root_id` relationship**, which is the actual question. Resolving it needs one query this session could not run (NC-01).
**Verdict: HOLD — SCOPE EVIDENCE REQUIRED.** The target design must decide which meaning `root_id` carries and enforce accordingly; it may not inherit the ambiguity. Raised as `P06-B-27`.
**This supersedes the unqualified wording of requirement RM-R-10** ("never at `root_id`") — see §5.

**SCOPE-F-05 — A reconcile model is COMPANY-scoped, but its effect is a financial one and its parameter has no control.**
Scope is agreed; the finding is unchanged. What CORR1 adds is that the **financial effect is owned by the company** while the parameter is changeable by anyone with accounting rights in that company, with tracking only (RM-F-19). Under "which COMPANY owns that financial effect" the answer is unambiguous, which makes the absence of an approval control a company-level governance gap, not a technical detail.

**SCOPE-F-06 — Payment provider scope is genuinely ambiguous. HOLD.**
A provider *contract* (the merchant agreement) is plausibly TENANT — one customer, one merchant relationship. The *settlement* is unambiguously COMPANY, because the money lands in one company's bank account. The reference forces the whole object to COMPANY (`$V18E/payment/models/payment_provider.py:43-45`, immutable once transactions exist at `:288-293`).
**Verdict: HOLD — SCOPE EVIDENCE REQUIRED.** The likely correct shape is a TENANT-scoped provider relationship with COMPANY-scoped settlement bindings, but that is a design decision, not a research finding. Continuing unaffected work.

**SCOPE-F-07 — Payment token access is wider than its ownership. CONTRADICTION.**
Ownership is COMPANY (derived: `$V18E/payment/models/payment_token.py:17-19`, `related='provider_id.company_id', store=True`). But the record rule is `parent_of`:
`$V18E/payment/security/payment_security.xml:31-35` — `[('company_id', 'parent_of', company_ids)]`
while the transaction rule immediately above it is the narrower `[('company_id', 'in', company_ids)]` (`:14-18`).
**A stored payment instrument is visible to a wider scope than the transactions made with it.** OWNERSHIP ≠ AVAILABILITY is exactly the CORR1 distinction, and here availability exceeds ownership for a credential-bearing object. Raised as `P06-B-28`.
Note also `$V18E/payment/models/payment_token.py:137-143` — for *validation* operations the token search **widens to the commercial partner** and ignores provider availability, with an in-code comment saying so.

**SCOPE-F-08 — Online bank connection scope is undetermined. HOLD.**
The connection is journal-bound and therefore behaves as COMPANY. Whether the *credential* to the bank aggregator is a tenant-level or company-level asset was not determined; the aggregator contract is not in the searched scope (NC-03). **HOLD — SCOPE EVIDENCE REQUIRED.**

**SCOPE-F-09 — Bank transaction identity is enforced at a scope wider than its owner. CONTRADICTION.**
The identity of a bank event belongs to **one company's** bank account. The reference enforces `unique (unique_import_id)` **globally across the database** (`$V18E/account_bank_statement_import/models/account_bank_statement.py:14-19`) and achieves separation only by string-prefixing the value with the sanitised account number and journal id (`.../account_journal.py:223-226`).
**Two consequences, in opposite directions, and both are real:**
1. **Too wide:** because the constraint is global, a collision between two companies is a hard database error, not a graceful per-company skip. In a multi-company tenant this is a cross-company failure mode.
2. **Too narrow:** because the account-number prefix collapses to empty when the file supplies none, the effective key degrades to `journal_id-raw_id`, and the deduplication filter (`:261-267`) is a **global `sudo()` search with no company domain at all**.
**Verdict: the identity is neither company-owned nor reliably unique.** Raised as `P06-B-29`. The residual question of whether two companies can actually collide depends on `sanitize_account_number`, which was not read — `P06-OQ-01`, Class D.

**SCOPE-F-10 — Intercompany settlement is two COMPANY effects inside one TENANT, and the reference supports neither the pairing nor the payment.**
Under CORR1 the correct shape is explicit: **two financial effects, each owned by a different company, linked by a TENANT-scoped object that owns neither.** `account_inter_company_rules` covers invoices and credit notes only (EGL-F-09), so no such linking object exists. This sharpens `P06-B-20`: the missing thing is not a feature, it is **a tenant-scoped carrier for a fact that no single company may own.**

---

## 5. Revalidation of findings affected by the superseded wording

Per CORR1 §6, each affected finding is recorded with its original form, the scope assumption used, why it was over- or under-constrained, and its updated classification. **Findings not listed here were not materially affected and are preserved unchanged.**

### R-01 — CPO-F-04, journal-code uniqueness
- **Original finding:** *"Two companies reuse the same journal codes (`BKK1`, `KAS1` appear in both C1 and C2). Journal code is therefore not a unique key across the tenant."*
- **Scope assumption used:** that a journal code must be unique at TENANT scope.
- **Why it is over-constrained:** a journal is **COMPANY**-scoped (S-04). Two companies legitimately using the same journal code is **correct behaviour**, not a defect. Requiring tenant-wide uniqueness would impose a security-boundary constraint on an accounting-boundary object.
- **Correct scope analysis:** journal code must be unique **within a company**. The real defect is not the repetition — it is that **any matching rule, import mapping, provider binding or report filter keyed on journal code without a company qualifier is ambiguous**, and the reference contains at least one such path (FFI-F-09, an unordered `limit=1` bank-journal search).
- **Updated classification:** the *observation* stands as evidence; the *implied requirement* is withdrawn and replaced. **Reclassified from "defect" to "correct-at-scope, with a downstream keying defect."**
- **Architecture impact:** every key that references a journal must carry company. Restated as `SCOPE-R-04` below.
- **Cross-process impact:** P01, P02, P05 — any process referencing a journal by code.

### R-02 — CPO-F-04, the 12-banks-to-2-GL-accounts finding
- **Scope assumption used:** none material — the finding is COMPANY-internal.
- **Revalidation:** unaffected. Both the GL accounts and the journals are COMPANY-scoped, and the finding is that within one company the GL cannot distinguish six bank accounts. **Preserved unchanged.** Its severity is if anything increased, because the correct control (journal-scoped reconciliation) must now also be proven company-scoped.

### R-03 — RM-R-10, "company isolation must be tested at `company_id`, never at `root_id`"
- **Original finding:** an unqualified requirement.
- **Why it is over-constrained:** it presumes that `root_id` never legitimately equals the COMPANY boundary. If a root and its children are branches of a single legal entity, root-scoped reconciliation is correct.
- **Correct scope analysis:** the requirement is conditional on what `root_id` means in the deployed configuration — SCOPE-F-04.
- **Updated classification:** **RM-R-10 is restated** as `SCOPE-R-02` below. The underlying evidence (`account_move_line.py:2336-2340`) is unchanged and remains a CONFIRMED observation; only the requirement derived from it is re-scoped.
- **Architecture impact:** the target must declare whether branch companies are one legal entity or several, and enforce the matching scope. It may not leave this to configuration.

### R-04 — Attack A4, cross-company bank misuse
- **Original classification:** CONFIRMED DEFECT for sibling-branch companies.
- **Revalidation:** **downgraded to HOLD — SCOPE EVIDENCE REQUIRED** for the sibling-branch vector specifically, pending SCOPE-F-04. **Retained as CONFIRMED DEFECT for the `company_id = False` bank-account vector**, which is unowned and therefore a DENY condition under CORR1 regardless of how `root_id` is interpreted.
- This is the single most consequential revalidation in this package, and it is a **downgrade** — recorded as such rather than quietly retained.

### R-05 — Payment token cross-company use
- **Original finding:** reported as adequately bound to one company.
- **Revalidation:** the binding is real, but the **record rule is wider than the ownership** (SCOPE-F-07). **Reclassified from "adequately bound" to CONTRADICTION.** This is an *upgrade* produced by applying the corrected model, and it was not visible under the earlier blanket wording — which is the strongest argument that the correction was worth applying mid-session.

### R-06 — `unique_import_id` scope
- **Original finding:** reported as "global, value-namespaced," severity framed around collision risk.
- **Revalidation:** reframed under SCOPE-F-09 as **enforcement at a scope wider than the owner, and a dedup filter with no company domain at all** (`$V18E/account_bank_statement_import/models/account_journal.py:261-267`). **Severity increased**; the finding now names the correct owner.

### R-07 — BER-F-20, deletability of bank evidence
- **Original finding:** *"whether a bank event can be erased is configuration, not invariant. For P06 this must become a **tenant-level locked setting**, not a company preference."* (`02_P06_BANK_EVENT_REGISTER.md:126`)
- **Scope assumption used:** that the audit-trail guarantee must be enforced at TENANT scope.
- **Why it is over-constrained:** the records being protected are journal entries and bank statement lines, both **COMPANY**-scoped (S-07, S-08), and deletability of accounting evidence is a legal/accounting question — a COMPANY matter, not a security-boundary matter. Forcing it to TENANT would impose one customer-wide policy on legally distinct entities that may have different retention obligations.
- **Correct scope analysis:** the setting is correctly **COMPANY**-scoped. The defect is not its scope but its **mutability**: `check_account_audit_trail` is an ordinary company toggle, whereas the equivalent guarantee elsewhere in the same system (`hard_lock_date`) is explicitly one-way — it cannot be removed and cannot be decreased (`$V18E/account/models/company.py:496-499`). The audit-trail guarantee has no such ratchet.
- **Updated classification:** the *evidence* stands unchanged (`$V18E/account/models/account_bank_statement_line.py:445-452`); the *requirement* is restated — **a COMPANY-scoped, one-way, non-decreasable policy**, modelled on the hard lock date, not a tenant-level override.
- **Architecture impact:** restated as `SCOPE-R-10` below.
- **Cross-process impact:** all processes producing accounting records.

### R-08 — Mechanical scan of the pre-correction files
- A case-insensitive scan for the token `tenant` was run over the eight deliverables written before the correction arrived (`01`, `02`, `03`, `04`, `05`, `06`, `09`, `12`).
- **Result: 2 occurrences**, both substantive, both revalidated above — `02_P06_BANK_EVENT_REGISTER.md:126` (R-07) and `09_P06_CROSS_PROCESS_OWNERSHIP.md:81` (R-01). No other finding in those files rests on a tenant-scope assumption.
- **DENOMINATOR:** POPULATION: the eight pre-correction deliverable files. PATTERN: case-insensitive `tenant`. PATH SET: this directory. UNIT: matching line. **Class A within that declared scope.**
- **Correction of record:** an earlier draft of this section asserted one occurrence before the scan was executed. The scan returned two. The count is corrected here rather than silently amended, per the adversarial-section discipline this programme applies to its own output.

---

## 6. Scope requirements for the target design

| ID | Requirement |
|---|---|
| SCOPE-R-01 | Every P06 object carries an explicit scope declaration. An object whose scope cannot be proven is denied, not defaulted. |
| SCOPE-R-02 | The COMPANY boundary must be declared once — branch companies are either one legal entity or several — and every financial guard must test that declared boundary. No guard may test a different boundary from the one declared. |
| SCOPE-R-03 | A physical bank account must be COMPANY-owned and may not exist unowned. `company_id = False` is a DENY. |
| SCOPE-R-04 | No key referencing a journal, account or bank may omit the company qualifier. Journal code is unique within a company only. |
| SCOPE-R-05 | Availability may never exceed ownership. A record rule wider than the owning scope is a defect, notably for credential-bearing objects. |
| SCOPE-R-06 | Bank transaction identity is COMPANY-scoped and must be enforced as such — not globally, and not by string prefix. |
| SCOPE-R-07 | Currency rates are TENANT-scoped shared reference data with tenant-level governance; a missing rate denies rather than defaults. |
| SCOPE-R-08 | Intercompany settlement requires a TENANT-scoped carrier object that owns neither company's financial effect but proves both. |
| SCOPE-R-09 | Provider relationships and bank connections must separate the TENANT-scoped contract from the COMPANY-scoped settlement binding. |
| SCOPE-R-10 | The audit-trail guarantee over bank and accounting evidence is COMPANY-scoped and must be a one-way, non-decreasable policy on the model of the hard lock date — never an ordinary toggle. |

## 7. Open scope items

| ID | Item | Status |
|---|---|---|
| P06-B-27 | Does `root_id` denote one legal entity or several? | **HOLD — SCOPE EVIDENCE REQUIRED** |
| SCOPE-F-06 | Payment provider: TENANT contract vs COMPANY settlement | **HOLD — SCOPE EVIDENCE REQUIRED** |
| SCOPE-F-08 | Bank aggregator credential scope | **HOLD — SCOPE EVIDENCE REQUIRED** |
| S-27 | Thai WHT rule set: PLATFORM reference vs COMPANY application | **HOLD** — statutory, routed to Accounting-Tax |
| PEER DEPENDENCY OPEN | P01–P05 and P07–P11 scope determinations are unpublished (CPO-F-03). P06's scope assignments for shared objects (currency rate, payment method, bank account) must be reconciled by P11. This session does **not** stop for it. | **PEER DEPENDENCY OPEN** |

---

# End
