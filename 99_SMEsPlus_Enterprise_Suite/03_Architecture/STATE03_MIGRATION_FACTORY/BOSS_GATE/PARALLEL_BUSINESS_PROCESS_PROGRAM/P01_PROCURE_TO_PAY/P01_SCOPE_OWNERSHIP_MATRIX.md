# P01 — SCOPE OWNERSHIP MATRIX

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Governing correction: `SMEPLUS-26-09-04-ACC-REV2-CORR1` — **SCOPE-AWARE EVERYWHERE**.
Layer: **1 — Clean-room business learning.**

This register was created **in response to the correction**, mid-session, as a delta. It does
not restate or replace any earlier finding; it re-frames the ones that were expressed under the
superseded "Tenant + Company context everywhere" reading, and adds the scope analysis the
correction requires.

Scopes: `PLATFORM` · `TENANT` · `COMPANY`.
`MISSING REQUIRED SCOPE = DENY`. `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`.

---

## 1. METHOD AND ITS BOUNDS

Two mechanical probes were run over `R1`:

**Probe 1 — model declarations.**
POPULATION: model declarations. UNIT: one source line that is exactly a model-name assignment
at class-body indentation. PATTERN: `^\s+_name\s*=\s*['"]<model>['"]\s*$`.
PATH SET: all of `R1`, excluding test directories.
FALSE-NEGATIVE MODES: a model declared on one line together with other assignments is missed;
a model created dynamically is missed; models declared only in the roots not searched are
missed (class C).

**Probe 2 — company scoping on the canonical declaring file.**
UNIT: the presence of a company field declaration, and the count of company-dependent field
declarations, in that file. FALSE-NEGATIVE MODE: a company field added by a *different* module
extending the same model is not counted by this probe. **This probe therefore proves presence,
never absence.** Every "no company field" cell below is class **B**, not class A.

**Self-caught defect.** The first version of Probe 1 used `_name\s*=` without a line anchor and
therefore also matched `model_name = '...'`, returning implausible declaration counts (25 for
one model). It was corrected before any finding was drawn from it. Recorded in
`P01_RESEARCH_ERROR_AND_REVISION_LOG.md` as `ERR-P01-02`.

---

## 2. OBJECT SCOPE CLASSIFICATION

`Own co. field` = the canonical declaring file declares a company field (Probe 2).
`Co.-dep. values` = that file declares company-dependent field values.

| Object | Own co. field | Co.-dep. values | OWNS | MUTATES | FINANCIAL EFFECT | Company owning the effect |
|---|---|---|---|---|---|---|
| Unit of measure | no | no | **PLATFORM** candidate | PLATFORM | no | n/a |
| Currency | no | no | **PLATFORM** candidate | PLATFORM | no | n/a |
| Currency rate | yes (optional) | no | **PLATFORM or TENANT** — unresolved | see note | indirect | **HOLD — owned by the Account track ruling** |
| Vendor / partner | **no** | yes (1) | **TENANT** | TENANT | no directly | n/a — but see §4 |
| Item (template) | yes (optional) | no | **TENANT**, optionally company-restricted | TENANT | no | n/a |
| Item (variant) | **no** | yes (1) | **TENANT** | TENANT | no | n/a |
| Item category | **no** | no on the file itself | **TENANT** | TENANT | **no — but it carries the account map** | see §3 |
| Vendor price list entry | yes, required | no | **COMPANY** | COMPANY | no | n/a |
| Storage location | yes (optional) | no | **TENANT or COMPANY** — unresolved | — | **yes** (it can override the clearing account, `EV-P01-07`) | **HOLD — SCOPE EVIDENCE REQUIRED** |
| Warehouse | yes, required | no | **COMPANY** | COMPANY | indirect | owning company |
| Purchase order | yes, required | no | **COMPANY** | COMPANY | no at confirmation (`EV-P01-01`); **yes via the accrual routine** (`EV-P01-16`) | owning company |
| Purchase agreement / requisition | yes, required | no | **COMPANY** | COMPANY | no | n/a — **see §5, this may be wrong for the business** |
| Goods receipt | yes | no | **COMPANY** | COMPANY | conditional | owning company |
| Stock movement | yes, required | no | **COMPANY** | COMPANY | conditional | owning company |
| Valuation layer | yes, required | no | **COMPANY** | COMPANY | **yes** | owning company |
| Landed cost | yes, required | no | **COMPANY** | COMPANY | yes | owning company |
| Vendor bill / journal entry | yes | no | **COMPANY** | COMPANY | **yes** | owning company |
| Journal item | yes | no | **COMPANY** | COMPANY | **yes** | owning company |
| Payment | yes, required | no | **COMPANY** | COMPANY | **yes** | owning company |
| Ledger account | yes, required | no | **COMPANY** | COMPANY | **yes** | owning company |
| Journal | yes | no | **COMPANY** | COMPANY | **yes** | owning company |
| Tax | yes, required | no | **COMPANY** | COMPANY | **yes** | owning company |
| Fiscal position | yes | yes (13) | **COMPANY** | COMPANY | yes | owning company |
| Fiscal year | yes, required | no | **COMPANY** | COMPANY | yes | owning company |
| Partial reconciliation | yes | no | **COMPANY** | COMPANY | yes | owning company |
| Full reconciliation | **no** | no | **COMPANY** by semantics; **not company-scoped on the object** | — | yes | **HOLD — SCOPE EVIDENCE REQUIRED** |
| Company | n/a | n/a | **TENANT** owns the set of companies | TENANT | no | n/a |

Every "no" in the first column is class **B** per §1.

---

## 3. THE CENTRAL SCOPE FINDING: COMPANY TRUTH ON TENANT OBJECTS

Verified (`R1`): **every general-ledger account that P01 posts to is a company-dependent value
hung on an object whose own scope is TENANT.**

| Account role | Stored on | Object scope | Value scope |
|---|---|---|---|
| Inventory valuation account | Item category | **TENANT** | company-dependent |
| Goods-received clearing account | Item category | **TENANT** | company-dependent |
| Valuation journal | Item category | **TENANT** | company-dependent |
| Item expense account | Item / item category | **TENANT** | company-dependent |
| Vendor payable account | Vendor | **TENANT** | company-dependent |

Classification: **FACT VERIFIED**, scope `R1`, read from the field declarations themselves.

**This is not, in itself, a defect.** It is a correct implementation of
`OWNERSHIP SCOPE ≠ FINANCIAL SCOPE`: one tenant-scoped object, many company-scoped values. Under
the superseded reading it would have been reported as an isolation failure. Under the corrected
model it is reported accurately as a legitimate scope split.

**The defect is the mutation asymmetry that follows from it:**

> The scope that may **mutate** the object is TENANT.
> The scope that **owns the financial effect** of the value is COMPANY.
> Nothing observed requires COMPANY-scope authority to change a COMPANY-scope accounting value.

A tenant-scope actor editing a tenant-scope catalogue object can therefore change which
accounts a *particular company's* purchases post to. The value-level guard that constrains the
chosen account to the right company is declared on the category account fields; **whether that
guard executes** was assigned to the Database Design expert and is **not** established here.

Classification: **SUPPORTED INTERPRETATION**, with the authority question class **B**
(scope searched: the field declarations, not the access rules).
Recorded as `CONTRA-P01-05`.

---

## 4. RE-FRAMED: THE CROSS-COMPANY TRIGGER

Restated under the corrected model. Full text in `P01_CROSS_PROCESS_OWNERSHIP.md` §4.1.

| Question | Answer |
|---|---|
| Scope of the object used to resolve the target company | the vendor/partner — **TENANT scope, no company field** (§2) |
| Scope of the resulting document | **COMPANY** (target company) |
| Scope executing the operation | **COMPANY** (source company) |
| Is ownership of the target-company financial effect proven? | **No** — inferred from an ancestor match in the shared contacts hierarchy, resolved with elevated privilege, first match wins (`EV-P01-26`) |
| Is the tenant boundary tested? | **Not found in the files searched — class B** (`EV-P01-31`) |

Correct statement of the finding under the corrected constitution:

> A **COMPANY-scoped financial effect** is created in a company whose ownership of that effect
> is derived from a **TENANT-scoped reference object**, with elevated privilege, and without a
> tenant test. `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`; the observed behaviour is to
> proceed, as superuser by default, and optionally to post.

Since unrelated independent companies are separate tenants by default, an untested company pair
is also an untested **tenant** pair. This is why the item carries tolerance-zero weight, and it
is the item that keeps P01 from an unconditional outcome.

Status: **HOLD — SCOPE EVIDENCE REQUIRED**, pending the Database Design expert's independent
check of record rules and access paths.

---

## 5. SCOPE QUESTIONS P01 CANNOT RESOLVE FROM SOURCE

Each is `HOLD — SCOPE EVIDENCE REQUIRED`. None blocks unaffected work.

| ID | Question | Why source cannot settle it |
|---|---|---|
| `SC-01` | Is a purchase agreement / framework contract TENANT-scope or COMPANY-scope? | The reference makes it COMPANY-scope and required. Commercially, a group negotiates once and several companies draw down. Which is right is a **business decision**, not a source fact. |
| `SC-02` | Is a vendor price list TENANT-scope or COMPANY-scope? | Same shape as `SC-01`; the reference makes it COMPANY-required. |
| `SC-03` | Is a storage location TENANT-scope or COMPANY-scope? | Its company field is optional, and a location can override a clearing account — so an under-scoped location can redirect a company's postings. |
| `SC-04` | Is currency-rate data PLATFORM or TENANT? | Rate ownership is already the subject of a standing ruling on the Account track. P01 inherits and does not decide. |
| `SC-05` | Is a tax definition TENANT or COMPANY? | The reference makes it COMPANY-required. A national rate table is arguably PLATFORM reference data with COMPANY-scope application. **Statutory question — no authoritative source consulted.** |
| `SC-06` | Is the item category TENANT or PLATFORM? | It carries no company field and holds the account map. If categories were platform-standard, the account map could not live on them. |
| `SC-07` | Does the reconciliation grouping object need company scope? | It carries no company field on its canonical file, yet it groups company-scoped journal items. Class B; may be scoped by its members. |

---

## 6. WHAT THE CORRECTION CHANGED IN THIS SESSION

| Finding | Before | After |
|---|---|---|
| Cross-company auto-generation | framed as "cross-company financial effect without explicit transaction" — a blanket prohibition reading | re-framed as **unproven ownership of a COMPANY-scoped effect derived from a TENANT-scoped object**, with the tenant test class B |
| Accounts on catalogue objects | would have been reported as a company-isolation gap | reported as a **legitimate scope split** with a real **mutation-authority** defect underneath it |
| Models lacking a company field | would have been reported as defects | now each is first assigned its correct scope; only mismatches are defects, and three are recorded as `HOLD — SCOPE EVIDENCE REQUIRED` rather than asserted |

No evidence was discarded. No checkpoint was re-run. No completed enumeration was repeated.
