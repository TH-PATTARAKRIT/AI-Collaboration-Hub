# SA_CORR5_02 — `G1` EXECUTION-CONTEXT CLOSURE

## CP-SA-C5-20 — G1 EXECUTION CONTEXT CLOSED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Workstream: **B** · Closes: **`G1`** (`SA_CORR4_01` §9) — five path classes with no stated execution
context: platform operator (class 1), service account (6), internal service-to-service (11),
wallet/prepaid financial background process (13), approval execution (14).
Boss: **SOLE FINAL APPROVER**

---

## 1. The invariant that governs every row, and the rule it forbids

Boss decision `00`/`01` (carried at `SA10` §8.2), `MTI-D-02` §4 rules 1, 6 and 8, `CF-I-01`:

> **Tenant is the security/customer boundary; Company the legal/accounting boundary inside it.
> Multi-tenant membership is not a multi-tenant execution context. A lower-level relationship can never
> weaken an upper-level security boundary.** Background jobs and system automation carry explicit
> tenant / company / warehouse / operation-type context. No axis substitutes for a wider one.

The scope rule is `SCOPE-AWARE EVERYWHERE`: a `PLATFORM`-scoped act requires neither tenant nor company
**as data context**, but it always has an **execution context** — the platform context — and an
authority. **"No tenant" is a scope class, never an absence.** Every row below states, for its
class, the execution context as a scope class plus the authority it runs under; **no row derives
cross-tenant execution from membership, and no row creates a cross-tenant path.**

### 1.1 Existing work consumed (`AUTO-C5-02`)

`SA_CORR4_01` §4 (the enumeration and per-class evidence), §5 (`C4-01-F-05`, the `BR-TEN-001` /
`Platform Operator` contradiction), §5.2 (`ARC-WP-002`, `-004`, `-009`); `SA_CORR4_03` (`CF-I-03`,
especially §3.14 *service account* and *break-glass* rows and `D4`/`D6`); `SA_CORR5_05` (`CF-I-03R`);
`SA_CORR5_01` (`E15-A1`, `XMC-C-A14`); `MTI-18`, `MTI-29`/`-30` R2, `CF-I-02`, `CF-I-04`;
`06_CROSS_MODULE_HANDOFF_CONTRACT_FIELDS` §6.1 (*the context boundary wins over segregation of
duties*, `MTI-F-05`); `FDS_TENANT` §8/§10, `FDS_MODULE` §8, `FDS_SUBSCRIPTION` §8,
`FDS_SUBSCRIPTION_MODULE` `FR-SM-005`, `FDS_REPORTING` `REP-004`/`BR-REP-001`, `FDS_INTEGRATION`
`FR-INT-001`…`-006`, `FDS_APPROVAL` `FR-APR-001`…`-007`/`BR-APR-003`, `FDS_IAM` `BR-IAM-003`;
`SAAS_CELL/22`, `/24`–`/27`, **`/29` `TRG-01`…`-18`** (new to this frame, `C5-B-05`); `ARC-WP-009`
§12.4–12.8; `ARC-WP-004` §12.0–12.6. **Nothing in the eleven attributes below is originated where a
source states it; every originated cell is marked `✎`.**

---

## 2. The eleven attributes, per class

Legend: `✔` carried from a cited source · `✎` specified first here · `M` mandatory · `n/a` not applicable
**with reason**.

### Class 1 — Platform operator / administrator

| Attribute | Specification | Basis |
|---|---|---|
| Actor identity | A **platform principal** — a human identity in the **platform identity domain**, distinct from any tenant user record. **It is not a tenant user and has no tenant membership.** `BR-TEN-001`/`BR-IAM-003` (*a user belongs to exactly one tenant*) are statements about **tenant users** and are honoured: a platform principal is not a user of any tenant | `✎` — this is the reconciliation `G2`/`C4-D-02` lacked: the contradiction dissolves once the actor is placed outside the tenant user model rather than inside it with an exception |
| Execution context | **`PLATFORM` scope**. Data context: the **tenant being acted on, named explicitly as the object of the act**, never resolved from the operator's own session | `SCOPE-AWARE EVERYWHERE`; `MTI-20` |
| Tenant context | `n/a` as *own* context — a platform principal has none; **the target tenant is a parameter of the act and is mandatory** for every act that touches a tenant (suspend/terminate, module enable, subscription assign/adjust) | `FDS_TENANT` §8; `FR-SM-005` |
| Company context | `n/a` — the five evidenced platform acts are tenant-level; **a platform principal may not act on a company-scoped business fact at all** | `FDS_*` §8 census (`SA_CORR4_01` §4.1); `MTI-D-02` rule 1 |
| Authority source | A **platform grant**, `MTI-18`-class: grantor (platform governance), grantee, reason, **scope = an enumerated act class** (suspend/terminate · module enable/disable · plan assign/adjust · health-dashboard read), **expiry mandatory**, permanent record. **MFA mandatory** | `MTI-18`; `ARC-WP-009` §12.6 |
| Allowed boundary crossing | **None into tenant business data.** The health dashboard is *"scoped to operational data only"* and *"must never surface tenant business data content"* — carried as a hard rule | `REP-004`, `BR-REP-001` |
| Prohibited crossing | Reading, selecting, searching, reporting, inferring or writing any tenant business record; acting on more than one tenant in one act; holding a tenant role | `MTI-D-02` §4 rule 1; `MTI-29` |
| Audit | Every act a `MTI-38` event in **platform** context with **target tenant as object**, actor, grant, **reason captured on every act** (today only `tenant.status_changed` captures reason — `C4-01` §4.1; extended to all five) | `FDS_TENANT` §10, widened `✎` |
| Break-glass / privileged | **Every platform act is privileged by definition** and evaluated by `CF-I-03` as a grant like any other (`D4` six fields). No suppression of any deny condition. Break-glass beyond this remains `G4` — a name, PMO staffing | `CF-I-03` §3.8, §3.14 |
| Revocation | `CF-I-03R` full lifecycle; leaver → immediate; platform grants are the first population for `FOR CAUSE` sweeps because their reach is every tenant | `SA_CORR5_05` |
| Downstream data contract | A platform act emits **no cross-module business handoff**. It emits a platform event consumed by tenant lifecycle, entitlement and audit only; `HF-CTX-*` do not apply (no business fact); a `PLATFORM` handoff to the platform's *own* accounting is `SA_CORR5_04` §5 | `SCOPE-AWARE EVERYWHERE` |

> **`C5-02-F-01` — `G2` re-scoped from *contradiction* to *model omission*.** The four canonical
> statements (`C4-01-F-05` A–D) do not contradict once the platform principal is a **separate identity
> domain**: `BR-TEN-001`/`BR-IAM-003` constrain tenant users; `FDS_TENANT` §8 names an actor that is
> **not** a tenant user; `FDS_ROLE`'s tenant-scoped `Role` entity carries tenant roles and **does not
> carry platform grants**. What the corpus lacks is the platform identity domain's own model — an
> authentication path, a session model, an MFA obligation, a grant store — which `ARC-WP-009` §12.2/12.6
> drafts and which no `FDS_*` file states. **That is an omission in `FDS_IAM`, a document-owner
> correction with a mechanically stated patch (§4), not a Boss contradiction.** `C4-D-02` is carried as
> the *review* of `ARC-WP-009` (PMO appointment), no longer as an unresolved design question.

### Class 6 — Integration / service account (external non-human principal)

| Attribute | Specification | Basis |
|---|---|---|
| Actor identity | A **service principal**: an API client identity **owned by exactly one tenant** (created by that tenant's owner under `FR-INT-001`), with **identity and version** — *"the system" is not an asserter* | `FDS_INTEGRATION` §3 (*Tenant Owner จัดการ API ขององค์กร*); `XMC-C-C3` |
| Execution context | **`TENANT` or `COMPANY` scope, fixed at credential issuance** — the credential *is* a grant and carries its four-axis scope | `ARC-WP-010` §12.8 *"external tokens … scoped per tenant"*; `CF-I-01` |
| Tenant context | **`M`**, bound to the credential, **never taken from the request payload** (`R3`: a receiver never infers tenant from payload content) | `XMC-C-D1` `R3` |
| Company context | **`M` where the act is company-scoped**, bound to the credential's scope; a credential scoped to several companies is **several `AUTH` entries**, never one broadened entry (`CF-I-01`); the request names **one** | `CF-I-01`; `MTI-29` |
| Authority source | The credential grant: grantor = tenant owner (under `FR-INT-001`), grantee = the client, four-axis scope, reason, **expiry / rotation** (`FR-INT-002`), permanent record. Rotation is `SUPERSEDED`; disable (`FR-INT-006`) is `REVOKED — LIFECYCLE` | `FDS_INTEGRATION`; `CF-I-03R` §3.2 |
| Allowed crossing | None. A service principal acts inside its tenant exactly as a tenant user would | — |
| Prohibited crossing | A credential issued in tenant A presented against tenant B → `CF-I-03` `D3`, tolerance zero; a credential with no company acting on a company-scoped object → `D5`; a credential with no version → `D6` | `CF-I-03` §3.14 |
| Audit | `MTI-38` event per act with the credential identity **and version** as actor; `integration_logs` (`FR-INT-005`) is a **secondary** log and never the audit trail of record | `BR-INT-004`; `SA_CORR5_03` |
| Break-glass | **Never.** A service principal cannot hold an `MTI-18` elevation | `✎` |
| Revocation | `CF-I-03R`; **`CREDENTIAL_COMPROMISED` is the canonical for-cause class for this actor**; secret rotation is not revocation | `SA_CORR5_05` §3.3 |
| Downstream data contract | A fact presented by a service principal is an ordinary emitting handoff: `HF-CTX-01`…`-11` mandatory; **`FR-INT-004` "Retry Supported" is bound by `XMC-C-A14`** — every presentation carries an attempt identity, and `E15-A1` deduplicates at the Accounting Core | `SA_CORR5_01` §7 |

### Class 11 — Internal service-to-service

| Attribute | Specification | Basis |
|---|---|---|
| Actor identity | An **internal service principal** — a platform component (posting engine, workflow engine, notification, entitlement, audit) with **identity and version**. Not a user, not a tenant client | `ARC-WP-004` §12.0; `ARC-WP-002` *"platform services … always resolve and enforce tenant context before returning data"* |
| Execution context | **The context of the request it is serving — propagated, never re-resolved.** An internal call inherits the **resolved `CTX` and four-axis `AUTH` of the originating act as a resolved tuple**; it does not run under a platform identity to do tenant work | `MTI-29` R2 (*resolved at scheduling and again at release; never inferred from the run's own payload*); `04_CTX_AUTH` §7 (stored *as a resolved tuple, not as a reference to the actor*) |
| Tenant context | **`M`**, propagated | `MTI-01` |
| Company context | **`M` where company-scoped**, propagated | `MTI-04` |
| Authority source | **The originating act's grant**, carried with the call; the service's own identity is the *executor*, the originating principal remains the *asserter*. **A service has no standing authority of its own over tenant data** | `CF-I-04` (defining ≠ acting, applied to services); `HF-CTX-08` |
| Allowed crossing | None. **A service that must touch several tenants (metering, audit retention) does so as an enumerated set of single-context executions, each with its own identity and result** | `MTI-29`; `SA_CORR5_04` |
| Prohibited crossing | Any internal call without a propagated `CTX`/`AUTH` → refused (`D6`); any call whose propagated tenant differs from the object's → `D3` | `CF-I-03` |
| Audit | The originating `MTI-38` event names the executing service **and version** in its evidence reference; internal hops that change state emit their own events under the propagated context | `SA_CORR5_03` |
| Break-glass | Never | `✎` |
| Revocation | A service version can be `REVOKED — FOR CAUSE` (`POLICY_VIOLATION` — e.g. a defective release); acts executed by that version become `SUSPECT` under `RFC-03` | `SA_CORR5_05` |
| Downstream data contract | `XMC-C-D1` unchanged; **posting and event delivery are idempotent on the Accounting Event Identity** (`ARC-WP-004` §12.1, `ARC-WP-010` §12.7 under the `SA_CORR5_01` §7 reading) | `SA_CORR5_01` |

### Class 13 — Wallet / prepaid financial background process

| Attribute | Specification | Basis |
|---|---|---|
| Actor identity | **The platform's billing service principal** — a class-11 internal service running **on the platform's own behalf**, identity and version recorded | `SAAS_CELL/24` §*Commercial wording*; `/27` |
| Execution context | **Two contexts, never one.** (a) **`PLATFORM` scope** for the platform's own financial fact (the wallet is a **liability of SMEsPlus to the customer**; its deduction is the platform's revenue recognition, not the tenant's accounting). (b) **`TENANT` scope, one tenant per execution**, for the usage evidence, forecast and notice delivered to that tenant | `✎` on the split; `TRG-01` *"Tenant execution context is mandatory for metered operations"*; `MTI-29` |
| Tenant context | **`M` — exactly one per execution**, selected by **enumeration from the subscription register**, never by scanning data | `MTI-29`; `TRG-02` |
| Company context | `n/a` with reason: a wallet is held by a **tenant** (the customer), not a company inside it; **no company-scoped business fact of the tenant is read or written**. If a tenant later asks for per-company statements, that is a read of *platform* evidence, not a company execution | `SAAS_CELL/27` deduction order (all platform charges) |
| Authority source | A **platform grant to the billing service** with scope = the four charge classes (base rental · measured usage · add-on · optional services) and **no authority over tenant business data** | `MTI-18`-class; `TRG-05` |
| Allowed crossing | **Read of per-tenant metered evidence** (`SAAS_CELL/22` `UCE-07`, `/29` `TRG-07`); **write of the tenant's own wallet ledger and notice**; nothing else | `TRG-01`, `-02` |
| Prohibited crossing | Any read of tenant business content; **any cross-tenant aggregation inside the per-tenant run** — platform-level totals are computed **from the per-tenant results afterwards**, in platform context (`SA_CORR5_04` §4) | `TRG-02`; `MTI-25`/`R8` analogue |
| Audit | Every deduction, forecast, notice and pre-authorisation decision is an **immutable event** (`SAAS_CELL/24` principle 2 *"historical usage and billing evidence remain immutable/auditable"*, `TRG-07`) in **platform** context with the tenant as object, **and** a tenant-visible copy (customer drill-down, `/23`) | `MTI-38` shape |
| Break-glass | Never. A manual wallet adjustment is a **platform operator act** (class 1) with reason, not a background-process capability | `✎` |
| Revocation | The billing service's grant under `CF-I-03R`; a defective release → `SUSPECT` deductions → disposition by **credit/re-deduction as new events** (`XMC-C-A8`), never edits | `SA_CORR5_05` §4.3 |
| Downstream data contract | Handoff **to the platform's own Accounting** (SMEsPlus as a company): an ordinary `BD-ACC-01` emitting handoff with tenant = the platform's tenant, company = SMEsPlus's operating company, owning domain = Billing, occurrence = the deduction event; **tax/accounting treatment of prepaid balances is an open item of `/27` and is `HOLD / EVIDENCE REQUIRED`** — not decided here. **No handoff to the customer tenant's Accounting**: the customer's own books record the prepayment from the statement they receive, outside SMEsPlus's control | `SA_CORR5_04` §5 |

### Class 14 — Approval execution

| Attribute | Specification | Basis |
|---|---|---|
| Actor identity | The **assigned approver** — a tenant user, identity recorded; `BR-APR-003` *only the assigned approver can approve*. **No delegation, proxy or substitute exists in the domain; where one is later added it is a grant (`CF-I-04`: assignment ≠ authority to act) and is out of scope here** | `FDS_APPROVAL` |
| Execution context | **The context of the request being approved — `COMPANY` scope, inherited from the request, never from the approver's session** | `06` §6.1; `R4` |
| Tenant context | **`M`** = the request's tenant. **The approver must be a user of that tenant** (`BR-TEN-001`) | `MTI-01` |
| Company context | **`M`** = the request's company. **The approver must hold a valid `AUTH` in that company** — *the context boundary wins over segregation of duties* | `06` §6.1 rule; `MTI-F-05` |
| Authority source | An **approval grant**: four-axis `AUTH` + operation class *approve* on the request's document class; **distinct from the grant to create the request** (`CF-I-04`) | `CF-I-04`; `ARC-WP-004` §12.3 |
| Allowed crossing | None. A group with one qualified approver in another company **may not** approve across the company; the segregation requirement **degrades to a recorded compensating control** (`ND-08`, `SA17` §4) — the compensating-control *design* needs Thai user input (Lane C) and is recorded, not authored | `06` §6.1; `ND-08` |
| Prohibited crossing | Approver outside the request's tenant → `D3`; outside its company → `D2`; creator = sole approver → `SoD` breach (`ARC-WP-004` §12.3), degraded only by an evented exception record | `CF-I-03`; `ENTERPRISE_CONTROL_LAYER` §12.4 |
| Audit | **The occurrence of approval is mandatory output** (`ND-04`, `XD-03`: populated on 0 of 27,874 rows in the evidenced estate) — a `MTI-38` event carrying request identity, approver, `AUTH`, decision, comment where required (`FR-APR-003`), two dates; `BR-APR-004` history undeletable | `SA17` §3 row 1 |
| Break-glass | An **override** of an approval route is a **restricted action** requiring elevated permission and an exception record | `ENTERPRISE_CONTROL_LAYER` §12.4 |
| Revocation | Revoking an approver's grant **after** an approval leaves the approval standing (`RFC-01` lifecycle) unless `FOR CAUSE`, in which case the approval is `SUSPECT` and the approved document's downstream effects are flagged for disposition | `SA_CORR5_05` §4.3 |
| Downstream data contract | The approval event is **not** a business fact and emits no `HF-CTX` handoff; it is a **precondition** the emitting module's fact carries as evidence (`HF-CTX-08` authority reference names the approval event where a control floor requires one — `XMC-C-D3`) | `XMC-C-D3` |

---

## 3. The invariant, tested against the five closed classes (the `SA_CORR4_01` §5.1 test, re-run)

| Class | `SA_CORR4_01` §5.1 verdict | After this file |
|---|---|---|
| 1 | not addressed — no stated execution context | **Stated and honoured** — platform scope, target tenant as object, no tenant business data, grant-bound |
| 6 | not addressed | **Stated and honoured** — scope fixed at credential issuance, `R3` binds |
| 11 | not addressed | **Stated and honoured** — propagated resolved tuple, no standing authority |
| 13 | not addressed | **Stated and honoured** — two contexts, one tenant per execution, platform totals only afterwards |
| 14 | not addressed | **Stated and honoured** — request's context governs, boundary wins over SoD |

**`5 unaddressed` → `0 unaddressed`.** With classes 4, 5, 9 already honoured, the enumeration reads
**8 honoured · 2 partial (10, 12 — `G3`, `G5`) · 3 property-only (2, 7, 8) · 1 name (3)** = 14. Classes
10 and 12 are closed at `SA_CORR5_03` and `SA_CORR5_04`; classes 2, 7, 8 have mechanisms on the stranded
`ARC-WP-004` (`C4-01-F-07a`) and remain `PROP` until that document is reviewed — a **PMO review act
(`C4-D-01` fold), not a Phase SA gap**; class 3 remains `G4`, PMO staffing.

---

## 4. Document-owner corrections owed, stated as patches

| Artefact | Owner | Patch |
|---|---|---|
| `FDS_IAM.md` | SMEsPlus Product Team | Add §2 *In Scope* item **"Platform Principal identity domain (separate from tenant users)"**; add actor row **Platform Principal — ไม่ใช่ผู้ใช้ของ Tenant ใด (candidate wording, UNVALIDATED)**; add `FR-IAM-011 Platform Principal Login` with acceptance criteria *MFA required · grant required · session platform-scoped · audit recorded*; add `BR-IAM-007` *"Platform Principal มีสิทธิ์เฉพาะตาม platform grant และเข้าถึงข้อมูลธุรกิจของ Tenant ไม่ได้"* (candidate) |
| `FDS_INTEGRATION.md` | same | §9 tables gain conceptual attributes *tenant, company scope, version, effective-from/-to* on `api_clients`/`api_keys` (conceptual, no types); `FR-INT-004` gains *"Attempt identity required on every retried presentation"* |
| `FDS_APPROVAL.md` | same | `BR-APR-005` *"Approver must hold authority in the request's company; the context boundary wins over segregation of duties"*; `FR-APR-002` acceptance gains *"Approval occurrence event recorded"* |
| `FDS_SUBSCRIPTION.md`, `FDS_MODULE.md`, `FDS_SUBSCRIPTION_MODULE.md` | same | Audit events gain `reason` on every platform act |

**Materiality:** with this file as the controlled Phase SA reading, the patches are **conformance
edits to Layer-1 foundation documents**, non-material to any Phase SA conclusion; they are carried at
`SA_CORR5_14` §3 as document-owner items whose absence changes no gate result.

## 5. What this file does not do

Create any cross-tenant execution path · authenticate a platform principal (a design in `ARC-WP-009`,
unreviewed) · design delegation/proxy approval · design the SoD compensating control (Lane C, Thai
user input) · staff `G4` · decide the tax/accounting treatment of prepaid balances · build anything.

## 6. Residual

1. **Class 1's "separate identity domain" is the load-bearing position and it is originated here.**
   The alternative — a platform principal *is* a tenant user of a "platform tenant" — is coherent and
   would make `BR-TEN-001` literally true of it. It was rejected because a platform tenant would be a
   tenant with cross-tenant reach, which is the exact thing the invariant forbids. A challenger should
   test that rejection.
2. **Class 13's platform-vs-tenant split** has no prior statement in the wallet decisions and is the
   first time the wallet is named as the platform's liability. If `SAAS_CELL/27`'s open item
   *"tax/accounting treatment of prepaid balances"* is later ruled otherwise, the handoff row changes.
3. **The compensating control for class 14** is named, not designed — by the corpus's own routing to
   Thai user input. It is an execution-context closure, not a control-design closure.

## 7. Checkpoint

> ## `CP-SA-C5-20 — G1 EXECUTION CONTEXT CLOSED`
> **5 of 5 path classes: 11 of 11 attributes each, `5 unaddressed → 0` · `G2` re-scoped from
> contradiction to model omission (`C5-02-F-01`) · 0 cross-tenant paths created · 4 document-owner
> patches stated · 1 finding.**

**Next autonomous action:** `CP-SA-C5-30` (`SA_CORR5_03`).

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
