# SA_CORR4_01 — PRIVILEGED-BYPASS PATH ENUMERATION

## CP-SA-C4-10 — PRIVILEGED BYPASS ENUMERATED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR4-PREGATE-CLOSURE-001]`
Branch: `architecture/phase-sa-corr4-pregate-closure-2026-09-09-001`
Condition closed: **`C4-01`** · Discharges the dependency `MTI-18` has carried since `L9-01`
Boss: **SOLE FINAL APPROVER**

---

## 1. What was actually inherited

CORR3, `SA_CORR3_07` §5.1 and §7.1: *"The privileged/system/background/administrative/migration path set
is **not enumerated**; the audit was **started and never finished**, with the Gate blocked."*

**Traced to primary text, the inheritance is thinner than the phrase suggests.**

`10_L9_SAAS_MULTI_TENANT_MULTI_COMPANY_REGISTER.md` (11 branches), row `L9-01`, verbatim:

> *"**What exists** — Prior evidence records company scoping enforced at the application layer across
> the core stock concepts, with **no database-layer backstop**, and **an audit of privileged bypass
> paths that was started and never completed.**
> **What is missing** — The invariant set itself (`RISK-U03`); the completed bypass-path audit; any
> database-layer enforcement."* R4 status: **`NOT PROVEN`**.

`03_MTI_INVARIANT_SET_R2_CONFORMED.md` §5.1, verbatim: *"`L9-01` records an audit … that was started
and never finished. `MTI-18` states the target property. **It does not supply the audit** … `MTI-18` is
unverifiable until that audit is completed, **because the set of privileged paths is not enumerated.**"*

> ### `C4-01-F-01` — the started audit left **no output at all**
>
> **Measured:** every downstream citation of `L9-01` — `SA11_STANDARDS_AUDIT_CONTROL_MAP.md` row 67,
> `SA_CORR3_07` §5.1, `07_L9_ISOLATION_PROOF_MATRIX.md` `MTP-03`,
> `05_FUNCTION_ENFORCEMENT_POINT_MATRIX.md` §4 — **references the same fact, that it was started and
> never finished, and never any of its content.** No partial path list, no interim register, no partial
> findings exist anywhere in `U2`.
>
> **The audit's stopping point is zero.** *"Started and never finished"* has been carried for rounds as
> if a partial result were somewhere waiting to be completed. **There is nothing to complete.** This
> file is the first enumeration, not a continuation — which is why it is scoped as a full pass over
> a declared population rather than a delta.

---

## 2. Method, population and controls

**POPULATION** the 185 branch heads, `U2` = 3,604 text paths (`CORR4-FRAME`).
**PATTERN** twenty-one vocabulary tokens, case-insensitive, plus a structural pass over every document
that specifies an actor, an entry point, or a write path.
**UNIT** **one execution path class**, not one document and not one token occurrence.

| Control | Result |
|---|---|
| Positive — `MTI-18` | **17 paths.** Fires |
| Positive — `privileged` | **89 paths** · `superuser` **34** · `break-glass` **4**. Two reference-estate elevation tokens also fire in the **Layer 2 audit quarantine only**, as expected, and are **not transcribed here** |
| Negative — `zqw94713_corr4_no_such_token` | **0** |
| **Coverage** | 21 tokens requested / 21 executed / **0 skipped** |

### 2.1 `C4-I-01`, restated because it decided this file's result

The **first** run of this scan returned **0 for all sixteen tokens then in the list, including
`MTI-18`.** Cause: zsh does not word-split an unquoted `$VAR`, so 185 refs were passed as one argument.
**The output was a coherent, plausible, wholly false answer — "the corpus contains no privileged-path
vocabulary" — and had it been believed, this file would have reported `ENUMERATION COMPLETE — NO
MATERIAL UNKNOWN` over an empty set.** Detected only because a positive control had been run minutes
earlier in a different command form.

### 2.2 `C4-I-05` — a second false zero, in the opposite direction

`grep -c 'tenant_id'` over `FDS_AUDIT.md` returns **0**. The file's §12 lists `tenant\_id` — **markdown
escapes the underscore.** The escape-tolerant pattern `tenant\\?_id` returns **1**, on both `ugrep` and
`ripgrep`.

**Caught by reading §12, not by a second instrument** — both instruments shared the pattern, which is
`C4-I-02`'s shape again. Every field-level count in §5 below uses the escape-tolerant pattern, and the
naive figure is published beside it wherever they differ.

---

## 3. `C4-01-F-02` — the enumeration's principal finding

> **The only documents in the corpus that specify a privileged execution path concretely are the
> `01_SaaS_Foundation/FDS/Domains/` family — 17 files, present on 185 of 185 branches — and no Phase SA
> artefact has ever cited one of them.**

**Measured.** `FDS_IAM`, `FDS_INTEGRATION`, `FDS_AUDIT`, `FDS_TENANT` are cited by name in **3, 6, 6 and
9 paths** respectively. **Not one is an `SA00`–`SA20`, `SA_CORR2_*` or `SA_CORR3_*` artefact.** Every
citer is a Foundation-internal file, a capability map, a rule catalog, a consolidation report or a patch.
Positive control: `MODULE_SPEC_AUTHORIZATION` returns 6 paths, so the instrument locates spec-name
citations.

**Why it was missed, exactly.** Phase SA worked from `MODULE_SPEC_AUTHORIZATION.md`,
`MODULE_SPEC_USER_ROLE_MANAGEMENT.md`, `MODULE_SPEC_API_GATEWAY.md`, `MODULE_SPEC_TENANT_MANAGEMENT.md`
and their `FR_DETAIL_*` decompositions — which are **also** on 185 of 185 branches, are also SMEsPlus-
owned, and read as the authoritative functional baseline. **They contain no privileged-path content
whatever**: no platform operator, no service account, no background job, no break-glass, no escalation.
`MODULE_SPEC_AUTHORIZATION`'s entire workflow is a **seven-step interactive login**, and step 4 —
*"System resolves tenant and organization scope"* — **is the only context-resolution step specified
anywhere in that family.**

> **A party reading only the `MODULE_SPEC_*` family would correctly conclude that SMEsPlus has no
> non-interactive execution paths at all.** The two families are the same size, on the same branches,
> in the same repository, and describe different systems. **That is the `PATH SET` defect, not a
> reading defect** — and it is the reason `MTI-18`'s enumeration looked impossible.

---

## 4. The enumeration

**Legend.** `SPEC` = specified concretely, with an entry point or actor · `PROP` = specified only as a
required property, no mechanism · `NAME` = the term appears, no design · `NONE` = no specification.
Context columns: `M` mandatory · `—` not stated · `n/a` not applicable.

| # | Path class | State | Best source (branch coverage) | Tenant ctx | Company ctx | Audit event | Time-bound |
|---:|---|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Platform administrator / operator** | **`SPEC`** | `FDS_TENANT` §8, `FDS_MODULE` §8, `FDS_SUBSCRIPTION` §8, `FDS_REPORTING` REP-004, `FDS_AUDIT` §3 — **185/185** | **—** | **—** | partial — §5.1 | **—** |
| **2** | Support / admin escalation | **`PROP`** | `MTI-18` (17 paths); `MTP-03`; `SA11` row 67 | M by design | M by design | required by design | **required — expiry named** |
| **3** | **Break-glass** | **`NAME`** | `SAAS_CELL/03` §7, `/04` §3.2; `IDENTITY_ACCESS_ARCHITECTURE` §17 — **1/185** | — | — | *"is audited"* | — |
| **4** | Background worker / queued job | **`SPEC`** | `MTI-29`, `MTI-30`, `CF-I-02`; `MTA-05`, `MTA-13` | **M** | **M** | **yes, incl. non-execution** | **yes — revalidated at release** |
| **5** | Scheduled job / cron | **`SPEC`** | `MTI-29`, `MTI-31`; `MTA-12` | **M** | **M** | partial | yes |
| **6** | **Integration / service account** | **`SPEC` (entry) + `NONE` (context)** | `FDS_INTEGRATION` FR-INT-001/002/006 — **185/185** | **`NONE`** | **`NONE`** | yes | **`NONE`** |
| **7** | Batch / import | **`PROP`** | `SA11-F-02`; `INV-F-19`; `MTA-21` | M by design | M by design | not specified | n/a |
| **8** | System migration utility | **`PROP`** | `MTI-06`, `MTI-42`; `INV-F-41`; `MTA-04`, `MTA-21` | M by design | M by design | **required, undefined** | n/a |
| **9** | Cross-company administrative function | **`PROP`** | `MTI-22` register — **4 entries, 1 incomplete, 3 conditional**; `SA10-F-05` | **M** | **M** | yes by design | per grant |
| **10** | Audit / support tooling | **`SPEC`** | `FDS_AUDIT` — **185/185** | **M** (`BR-AUD-003`, field `tenant_id`) | **`NONE`** | self-referential | — |
| **11** | API / internal service-to-service | **`SPEC` (external) + `NONE` (internal)** | `FDS_INTEGRATION`; `MTI-17` | **`NONE`** | **`NONE`** | yes | — |
| **12** | **Usage-metering / capacity pipeline** | **`SPEC`** | `SAAS_CELL/22`, `/23` — Boss-approved **2026-09-09** | **M** (per-tenant evidence) | **`NONE`** | required — *"reproducible and auditable per Tenant"* | — |
| **13** | **Wallet / prepaid financial background process** | **`SPEC` (business) + `NONE` (context)** | `SAAS_CELL/24`, `/25`, `/26`, `/27` — Boss-approved **2026-09-09** | **`NONE`** | **`NONE`** | — | — |

**13 path classes. 11 from the master prompt's list, 2 found in evidence (`12`, `13`).**
**`5 SPEC` · `4 PROP` · `1 NAME` · `3 mixed`.** Each class appears once.

### 4.1 Per-class detail, for the classes where the finding is in the detail

**Class 1 — the four concrete acts, verbatim, all on 185/185 branches**

| Act | Source | Audit event | Reason captured? |
|---|---|---|---|
| Suspend / terminate a tenant — *"Only Platform Operator (internal)"* | `FDS_TENANT` §8 | `tenant.status_changed (actor, old_status, new_status, reason)` | **Yes — the only one** |
| Enable / disable a module | `FDS_MODULE` §8 | `module.enabled/disabled (actor, module_code)` | **No** |
| View / adjust a subscription *"for support cases"* | `FDS_SUBSCRIPTION` §8 | `subscription.plan_changed (actor, old_plan, new_plan)` | **No — so the stated justification is not itself auditable** |
| **Cross-tenant** health dashboard | `FDS_REPORTING` REP-004, status `GAP — NEW` | none stated | n/a |

**Class 6 — the service credential carries no context, and it is not a template artefact**

`FDS_INTEGRATION` §9 *Database Mapping* names four tables — `api_clients`, `api_keys`, `webhooks`,
`integration_logs` — **and no columns for any of them.** §10 *Security* is five words: *OAuth2 Ready ·
JWT · HTTPS · API Key Rotation · Audit.* **`tenant_id` and `company_id` each return `0` under the
escape-tolerant pattern, on both instruments.**

**This is not simply the long-form template.** `FDS_COMPANY` uses the same template and returns
`company_id` **6** times; `FDS_AUDIT` uses it and returns `tenant_id` **1**. **The absence in
`FDS_INTEGRATION` is specific to it, and it is the file that defines how a non-human principal
authenticates.**

**Class 10 — the audit record carries one of the four axes**

`FDS_AUDIT` §12 *Audit Fields*: `audit_id · tenant_id · user_id · action · resource · resource_id ·
before_value · after_value · request_id · ip_address · user_agent · created_at` — **12 fields, and
`company_id` is not among them** (0 on both instruments, escape-tolerant).

`MTI-D-02` §4 requires the audit trail to answer *who performed what action under which **tenant,
company, warehouse and operation type***. **The canonical audit record carries 1 of the 4 axes.**

Two further defects in the same file: §14 *Risks* names **"Unauthorized Audit Access"** and lists **no
mitigation for it or for either other risk** — the section is three bare lines. And `FDS_REPORTING`
`BR-REP-002` sends the reader to *"`FDS_AUDIT.md` section 8"* for access scoping; **§8 is "Screen
Mapping."** The security content is §11 (*Read Only · RBAC · Tenant Isolation · Immutable*).
**The access-scoping rule the reporting domain relies on is not where its own corpus says it is.**

**Classes 12 and 13 — Boss-approved on the morning of 2026-09-09, outside CORR3's frame**

Measured over all seven new decisions, case-insensitive, both instruments agreeing:

| File | `tenant` | `company` | `context` | `scope` |
|---|---:|---:|---:|---:|
| `22` usage-based capacity and transparent billing | **4** | 2 | **0** | **0** |
| `23` customer usage visibility | **4** | **0** | **0** | **0** |
| `24` wallet protection and advance notification | **0** | **0** | **0** | **0** |
| `25` 30-day advance wallet depletion notice | **0** | **0** | **0** | **0** |
| `26` prepaid before usage / notice is not credit | **0** | **0** | **0** | **0** |
| `27` low base subscription with prepaid usage services | **0** | **0** | **0** | **0** |
| `28` package and organization size | **2** | 1 | **0** | **0** |

> **`C4-01-F-03`.** File `22` approves an architecture chain — Resource Governor → **Capacity Meter** →
> Entitlement Engine → Usage Statement — measuring CPU, RAM, DB load, I/O, queue, storage, API volume
> and job consumption. **That is a continuously-running, cross-tenant, non-interactive measurement path
> — a class-4/5 execution path by any reading — and it is cross-referenced to `MTI-29`, `MTI-30` or
> `CF-I-02` in exactly `0` places.** It carries its own per-tenant evidence requirement (`UCE-03`) and
> **no company axis at all.**
>
> **`C4-01-F-04`.** Files `24`–`27` specify **per-customer financial background processes** — wallet
> depletion, advance notice, prepaid deduction — and contain **zero occurrences of `tenant`, `company`,
> `context` or `scope`.** Positive control: `tenant` fires **4** times in file `22` of the same set, so
> the instrument reads this corpus. **These are financial mechanisms with no stated execution context
> whatever**, approved after every isolation register in the programme was written.
>
> **The word `context` and the word `scope` appear `0` times across all seven.**

---

## 5. `C4-01-F-05` — the contradiction at the centre of the canonical baseline

**All four statements below are on 185 of 185 branches. They are not reconciled anywhere in `U2`.**

| # | Statement | Source |
|---:|---|---|
| **A** | *"A user belongs to **exactly one tenant**; **cross-tenant accounts are not permitted in v1**."* | `FDS_TENANT` `BR-TEN-001` |
| **B** | *"User ต้องอยู่ภายใต้ Tenant เดียว"* — a user must be under exactly one tenant | `FDS_IAM` `BR-IAM-003` — **the same rule, second file, second language** |
| **C** | *"**Only Platform Operator (internal)** can Suspend/Terminate a tenant"* · *"Platform Operator shall have a **cross-tenant** health dashboard"* · Platform Admin is an actor in `FDS_IAM` and `FDS_AUDIT` | `FDS_TENANT` §8 · `FDS_REPORTING` REP-004 · `FDS_IAM` §3 · `FDS_AUDIT` §3 |
| **D** | `Role` entity key attributes: `id, tenant_id, name, is_template` — **tenant-scoped by its own schema** | `FDS_ROLE` §6 |

> **The canonical baseline specifies a cross-tenant privileged actor in four files and prohibits
> cross-tenant accounts in two — and the entity that would carry that actor's authority is
> tenant-scoped by its own key attributes.**
>
> **There is no reconciliation, no exception clause, and no separate platform-identity model.**
> `FDS_IAM`'s ten functional requirements — `FR-IAM-001` Login through `FR-IAM-010` Session Management —
> are **all ordinary tenant-user flows.** *There is no authentication path in the corpus by which a
> Platform Operator signs in*, no session model for it, no MFA obligation on it, and nothing that
> revokes or expires it.

**This is the exact failure the mandatory invariant exists to prevent** — Boss decision `00`/`01`:
*"multi-tenant membership is not a multi-tenant execution context; a lower-level relationship can never
weaken an upper-level security boundary."* **Class 1 is a path whose execution context is unstated, on
an actor whose account model contradicts the rule, exercisable against any tenant.**

**Severity.** `CRITICAL — TOLERANCE ZERO` in the target architecture. **Reachability today: nil — no
implementation exists.** `SA10-F-03`'s rule binds and is applied: *"A defect that cannot fire today is
not thereby safe: it is a defect whose trigger is becoming multi-company"* — here, **multi-tenant** —
*"which is precisely what SMEsPlus is. Severity ranking must use the target architecture, not the
reference deployment's accident."*

### 5.1 The mandatory invariant, tested against all thirteen classes

> **No lower-level role, process or business relation may weaken the upper Tenant security boundary.
> Multi-tenant membership must never become multi-tenant execution context implicitly.**

| Verdict | Classes |
|---|---|
| **Invariant stated and honoured in the specification** | **4, 5, 9** — `MTI-29`/`MTI-30`/`CF-I-02` carry `CTX` **and** the authority, and revalidate at release; `MTI-22` is a closed enumerated door |
| **Invariant not addressed — the path has no stated execution context** | **1, 6, 11, 13** |
| **Invariant addressed on the tenant axis only** | **10, 12** |
| **Invariant stated as a property with no mechanism** | **2, 7, 8** |
| **Invariant not reachable — the path is a name** | **3** |

**`3 honoured · 4 unaddressed · 2 partial · 3 property-only · 1 name` = 13.** ✓

---

## 6. Residual attack surface carried from the existing registers

Reproduced, not re-derived: `08_FAILURE_EDGE_CASE_AND_LEAKAGE_ATTACK_REGISTER.md` holds **24** `MTA-*`
attacks; `07_L9_ISOLATION_PROOF_MATRIX.md` holds **30** `MTP-*` scenarios. **`5` carry
`RESIDUAL: BLOCKING`** — `MTA-12`, `-18`, `-21`, `-22`, `-24`.

The four that bear directly on this enumeration, verbatim:

| ID | Attack | Residual |
|---|---|---|
| `MTA-05` | *"A background or import path finds no company and falls back to 'the first' or 'the default' company"* | **`MATERIAL`** — *"Unverifiable until the privileged-path audit is completed"* |
| `MTA-13` | *"A job is scheduled, the scheduling user's access to that company is revoked, the job fires later"* | `NONE IN DESIGN` — defeated by `MTI-30` |
| `MTA-21` | *"A legacy warehouse or location list is imported and company is inferred from a name, code or text pattern"* | **`BLOCKING`** — `MTI-42` *"prohibits the bad act but cannot evidence the good one"* |
| `MTA-04` | Warehouse company reassigned after movements exist | **`MATERIAL`** — *"A real business need currently has no compliant path"* |

> **`C4-01-F-06`. `MTA-05`'s residual is discharged as to its stated blocker by this file.** Its residual
> reads *"unverifiable until the privileged-path audit is completed."* **The audit is now performed, and
> the answer is worse than unverifiable: classes 1, 6, 11 and 13 have no stated execution context at
> all, so on those paths there is no specification to fall back *from*.** The attack is not defeated;
> **its status changes from `unverifiable` to `unmitigated on four named path classes`, which is a
> testable statement and was not one before.**

---

## 7. What this enumeration is, and what it is not

| | |
|---|---|
| A specification-level enumeration over a declared corpus | **Yes** |
| A runtime enumeration of paths in a running system | **No — none exists** |
| Proof of `MTI-18` | **No.** `MTI-18` requires that no *unaudited* bypass exists; that is a property of a **built** system |
| Does it discharge `MTI-18`'s **dependency**? | **Yes.** `MTI-18` was *"unverifiable … because the set of privileged paths is not enumerated."* **The set is now enumerated.** `MTI-18` moves from *unverifiable in principle* to *unproven pending implementation* — which is where the other 56 invariants already are |
| Does it unblock `MTI-02`, `MTI-17`, part of `MTI-38`? | **The dependency, yes. The proofs, no** — `SA_CORR4_06` |
| Vetoes discharged | **0** |

---

## 8. Residual, stated exactly

1. **The population is documentary.** A path can exist in a built system and in no document. **This
   enumeration is a floor on the path set, never a ceiling**, and no reader may treat it as
   exhaustive of a future implementation. **`CF-I-03` §3.8 is written to fail closed on exactly that
   residual**: an unknown privileged path is `D4`, never a pass.
2. **Classes 12 and 13 were found only because the frame was re-measured.** They were approved on the
   morning of 2026-09-09 and are outside CORR3's population. **Any path class approved after this file
   is outside mine, by the same mechanism** — which is an argument for re-measuring the frame at
   publication, not at commencement.
3. **The `FDS` family is on 185 of 185 branches and Phase SA had never read it.** I have read the 12
   domain files bearing on access; **there are 17, plus `FDS_REQUIREMENT_CATALOG.md` and
   `FDS_TEMPLATE.md`.** The five I did not open — `FDS_APPROVAL`, `FDS_DIVISION`, `FDS_NOTIFICATION`,
   `FDS_ROLE_PERMISSION`, `FDS_SUBSCRIPTION_MODULE` — **are a declared, bounded residual and the first
   thing a challenger should sweep.**
4. **`IDENTITY_ACCESS_ARCHITECTURE.md` (ARC-WP-009) is the only consolidated IAM design in existence
   and it sits on 1 of 185 branches**, at version `0.1`, `DRAFT`, `NOT VERIFIED`, `Gate Status: HOLD`,
   never independently reviewed. Its §12.6 (*privileged access time-bound, MFA-enforced, fully
   audited*), §12.4 (six standard roles including Platform Operator) and §17 (break-glass audited)
   **are the only statements in the corpus that would resolve `C4-01-F-05`** — and **nothing on
   mainline, and no Phase SA artefact, cites it.** Whether it is adopted is not my act; **that it is
   invisible where it is needed is the finding.**
5. **My unit is the path class, and a class is a judgement.** Splitting class 4 from class 5, or
   merging 6 with 11, would change the counts without changing the evidence. **The counts are
   therefore not the result; the per-class context columns are.**

---

## 9. Verdict

> # `ENUMERATION COMPLETE — EXACT BOUNDED GAPS LISTED`

**Complete** in the sense the classification permits: **13 path classes enumerated over a declared
185-branch, 3,604-path population, with a positive control, a negative control, a coverage assertion,
and two false zeros found and corrected.** Every class carries its state, its best source with branch
coverage, its context columns and its exact gap.

**The bounded gaps are named and are these five:**

| # | Gap | Class |
|---:|---|---|
| **G1** | **Four path classes have no stated execution context at all** — platform operator, service account, internal service-to-service, wallet/prepaid | 1, 6, 11, 13 |
| **G2** | **The canonical baseline contradicts itself** on whether a cross-tenant actor may exist, and provides no authentication path for the one it specifies | 1 |
| **G3** | **The canonical audit record carries 1 of `MTI-D-02`'s 4 axes** — no `company_id` | 10 |
| **G4** | **Break-glass is a name with no design**, assigned as a future responsibility of an unstaffed role | 3 |
| **G5** | **A Boss-approved cross-tenant metering pipeline and four financial background processes are unintegrated** with the execution-boundary invariant family | 12, 13 |

**No `TARGETED VERY DEEP RESEARCH` is required.** Every gap above is a **specification** gap over
evidence that is present and has been read — not an evidence-acquisition problem. **`G1`, `G3` and `G5`
are closable by SMEs Core design acts. `G2` is a contradiction inside a Boss-owned canonical baseline
and is escalated as `C4-D-02`. `G4` has a named future owner and is a PMO staffing item.**

## 10. Checkpoint

> ## `CP-SA-C4-10 — PRIVILEGED BYPASS ENUMERATED`
> **13 path classes · 5 bounded gaps · 6 findings (`C4-01-F-01` … `-F-06`) · 2 instrument findings
> (`C4-I-01`, `C4-I-05`) · 1 escalation (`C4-D-02`).**
> **`MTI-18`'s enumeration dependency is discharged. `MTI-18` is not proven and cannot be at Phase SA.**
> **0 vetoes discharged. 0 invariants proven.**

**Next autonomous action:** `CP-SA-C4-40`, compliance retraction propagation.

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
