# SA_CORR4_02 — `XMC-C-D1` TENANT + COMPANY EMITTING HANDOFF CONTRACT

## CP-SA-C4-20 — `XMC-C-D1` CONTRACT CLOSED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR4-PREGATE-CLOSURE-001]`
Branch: `architecture/phase-sa-corr4-pregate-closure-2026-09-09-001`
Condition closed: **`C4-02`**
Authority: `BD-ACC-01`'s express grant — *"Phase SA may design the technical representation
independently"*. **Business-semantic clauses only.** No schema, no data type, no identifier format.
Boss: **SOLE FINAL APPROVER**

---

## 1. What CORR3 left, and what re-measurement changes

CORR3's condition 2: *"Add tenant and company to the emitting handoff payload (`XMC-C-D1`). This
closes the **interface half** of element 10."* Its ground was `XMC-F-02`:

> *"Element 10 … is absent from the emitting party's own published payload."*

**The measurement reproduces exactly. The sentence's scope does not** — `SA_CORR4_00` §4.4, finding
`C4-B-04`. Re-measured over the whole producer package rather than one file:

| Producer artefact | `tenant` | `Tenant` | `company` | Element 10 carried? |
|---|---:|---:|---:|---|
| `V1_0/07_…ACCOUNTING_CONTROL_IMPACT_V1.md` §1.1 *(CORR3's file)* | 1 | 0 | 4 | **No** |
| `V1_0/10_…CROSS_MODULE_HANDOFF_V1.md` — the 31-row `HX-` register | 1 | 0 | 2 | **No** — and neither of the two `company` lines is a payload element; both are **route descriptions** (`HX-21`, `HX-22`) |
| `V2_0/05_INVENTORY_V2_FUNCTIONAL_DELTA_DESIGN.md` | 2 | 1 | 2 | **No** |
| `V2_0/03_INVENTORY_V1_TO_V2_DELTA_MAP.md` | 0 | 0 | 0 | **No** |

Two instruments (`ugrep`, `ripgrep`), case-sensitive, negative control 0 on all four.

> **The finding survives on all 30 artefacts of the `FINAL_SOLUTION` package, in both versions.**

### 1.1 `C4-02-F-01` — a second emitting-side contract exists, and it carries element 10

`.../REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/MULTI_TENANT_INVARIANT_SET_EXECUTION/`
`06_CROSS_MODULE_HANDOFF_CONTRACT_FIELDS.md` specifies a context field group for exactly this
boundary, extended to **eleven** fields by `MTI_RULING_CONFORMANCE_EXECUTION/07_CONSUMING_MODULE_
OBLIGATION_MATRIX_R2.md`:

| Field | Content | Mandatory |
|---|---|---|
| **`HF-CTX-01`** | **Tenant identity** | **Always** |
| **`HF-CTX-02`** | **Company identity** | **Always** |
| `HF-CTX-03` / `-04` | Warehouse; location, source and destination | where situated / where goods move |
| **`HF-CTX-05`** | **Context anchor path** — the object chain company was derived from | **Always** |
| **`HF-CTX-06`** | **Context conformance attestation** — the `MTI-19` run identifier, timestamp, result | **Always** |
| `HF-CTX-07` | `MTI-22` cross-context relationship identity | where applicable; `N/A` **with reason** |
| **`HF-CTX-08`** | **Authority reference** — actor and authority, including any `MTI-18` grant | **Always** |
| `HF-CTX-09` | Owner dimension, stated separately from company | where an owner other than the company applies |
| `HF-CTX-10` | Operation-type identity + platform class (`CF-I-05`) | where the fact arose through an operation type |
| **`HF-CTX-11`** | **Authorization attestation** — the `CF-I-03` run identifier, timestamp, result | **Always** |

> **`C4-02-F-01`. Tenant and company are already specified as unconditionally mandatory emitting-side
> handoff fields, with a derivation path and an attestation, in a package Boss-ruling-conformed on
> 2026-09-05. `XMC-F-02` is true of the `FINAL_SOLUTION` package and false as a statement about the
> programme.** CORR3 cites `HF-CTX-11` and `MTI-43` and therefore reached the package; **the bound of
> a read is not the bound of a package**, which is the defect CORR3 itself named at `XMC-F-01`,
> executing one level along.

**What this changes for `C4-02`.** CORR3's condition was *"add tenant and company."* That is an
**authoring** act on somebody else's design. **The corrected condition is to consolidate two
independently-authored halves into one contract and prove it across domains** — which is Phase SA's
own work, and is what §3–§5 do.

### 1.2 `C4-02-F-02` — the two handoff registers do not reference each other

| Test | Result | Control |
|---|---:|---|
| `HX-` cited in `06_CROSS_MODULE_HANDOFF_CONTRACT_FIELDS.md` | **0** | `HO-` fires **6** in the same file |
| `HX-` branch-wide, unit `U2` | **18 text paths** (case-sensitive). A case-insensitive run returns **20**; the two extra are `.zip` archives, **outside `U2` by the frame's own extension rule** | negative control **0** |
| `HO-` or `HF-CTX` cited in `10_…CROSS_MODULE_HANDOFF_V1.md` | **0** | `HX-` fires **35** in the same file |

**Two SMEsPlus-owned registers describe the same Inventory→Accounting boundary and neither cites the
other.** Exactly one file in the corpus cites both, and it is the R2 obligation matrix.

> **`C4-02-F-02` is CORRECTED by independent challenge, and the corrected form is worse.** This
> finding first called `HX-` and `HO-` *"two disjoint identifier families."* **They are not disjoint —
> they are the same row numbers under two prefixes.** File 06 §6 cites `HO-01`, `-02`, `-04`, `-05`,
> `-06`, `-07`, `-09`…`-27`, and each aliases its `HX-` twin **content-for-content**: `HO-22` is
> *"Inter-company transfer"* and so is `HX-22`; `HO-04`/`-05`/`-06` are the expected-receipt,
> over-receipt and replenishment rows and so are `HX-04`/`-05`/`-06`; `HO-18`/`-19`/`-20` are the
> Manufacturing rows and so are `HX-18`/`-19`/`-20`.
>
> **My own count missed it**: `grep 'HO-[0-9]{2}'` returns **6**, because the file writes the rest in
> the elided form `` `HO-01`, `-02` `` — **the same elision defect, in the opposite direction, that the
> challenger's own recount exhibited.** Two parties, one pattern, two wrong counts.
>
> **The corrected finding: two registers use one row numbering under two prefixes, and neither states
> that they are the same rows.** An undeclared alias is a worse defect than two disjoint families,
> because a reader of either register has no way to learn that the other one exists — and it makes
> §5's join **an alias, not an inference**. §7 residual 5 is corrected accordingly.

**Consequence, and it is the operative one for the Pre-Test Matrix:** a Pre-Test case written against
`HX-07` has **no stated field list**, and a case written against `HF-CTX-*` has **no stated trigger or
receiver obligation**. Neither register alone can generate an executable test. §5 supplies the join.

### 1.3 `C4-02-F-03` — the Boss-mandated canonical joint artifact has never been created

`03_BOSS_APPROVAL_…MINIMUM_HANDOFF_DATA_CONTRACT_2026_09_02.md` §5, verbatim:

> *"A dedicated `ACCOUNTING_INVENTORY_INTERFACE_CONTRACT_AND_CROSS_PROOF.md` (or equivalently
> controlled canonical artifact) is **mandatory before final integrated freeze**."*

`02_BOSS_APPROVAL_JOINT_22_SCENARIO_CROSS_PROOF_BASELINE_2026_09_02.md` §— requires it to define
*"ownership, event semantics, required context, timing, reconciliation, correction/reversal,
provenance, tenancy/company isolation, idempotency and replay controls."*

**Measured: `0` of `3,604` paths.** Positive control — the Boss file's own name string returns **4**
paths; negative control **0**.

**Recorded as outstanding — twice, and both times by the Inventory side**: `16_PROCESS_HANDOFF_MAP.md`
(*"is mandatory before integrated final freeze and does not yet exist … R4 records that requirement as
outstanding and does not attempt to author it, since it is a joint artifact"*) and
`09_JOINT_DECISION_READINESS_MATRIX.md` (*"does not yet exist … This review likewise does not author
it and records it as outstanding"*).

> **`C4-02-F-03`. The mandate is recorded twice by the producing domain and by no Phase SA artefact —
> `SA00`–`SA20`, `SA_CORR2_*` and `SA_CORR3_*` cite it 0 times.** And `SA_CORR3_08` §3 published a
> thirty-clause cross-domain contract that answers **nine of the ten subjects** the mandate lists,
> **without citing the mandate it was answering.** Two parties each did half of a Boss instruction
> neither knew it was executing.

**This file cites it, and states what it is and is not**: §3–§5 below are a **contract specification**
that could become the mandated artifact's context, ownership and isolation sections. **It is not that
artifact.** That artifact is joint, and this session is not the joint workstream. **Escalated as
`C4-D-01` — an appointment, not a decision.**

---

## 2. Scope, and the two authorities

| | |
|---|---|
| **What this contract is** | A **business-semantic** interface specification for the tenant/company context of every cross-module business handoff |
| **What it is not** | A schema, a data model, a field type, an identifier format, an API, an event technology, or an implementation |
| **Authority to write it** | `BD-ACC-01` — *"Phase SA may design the technical representation independently"* — read **narrower than granted**: semantics only |
| **Authority it does not claim** | Ruling any Joint decision; ruling `CF-D-02`; ruling `RC-D-01`; authoring the mandated joint artifact; amending `HF-CTX-*` or `XMC-C-*`, both of which govern where this file and they disagree |
| **Scope rule that binds every clause** | **`SCOPE-AWARE EVERYWHERE`** (`SMEPLUS-26-09-04-ACC-REV2-CORR1`): `PLATFORM` requires neither context; `TENANT` requires tenant; `COMPANY` requires both. `MISSING REQUIRED SCOPE = DENY` |
| **Topology** | `SHARED SaaS POOL` only — `CF-I-08` |

### 2.1 The invariant that governs the whole file

Boss decision `00`/`01`, carried at `SA10` §8.2, verbatim in substance:

> **Tenant is the security/customer boundary; Company is the legal/accounting boundary inside it.
> Unrelated independent companies are separate tenants. Multi-tenant membership is not a multi-tenant
> execution context. A lower-level relationship can never weaken an upper-level security boundary.**

**No clause below may be read as creating an exception to it, and none does.** The one cross-**company**
path is the enumerated `MTI-22` register. **There is no cross-tenant path in this contract, and this
file does not create one.**

---

## 3. `XMC-C-D1` — the emitting handoff contract

### 3.1 The thirteen required elements, and where each already stands

`✔` = specified in a cited primary source · `◐` = partially specified · `✎` = specified **first** here.

| # | Element | Semantics | State | Source / this file |
|---:|---|---|:---:|---|
| 1 | **Tenant context identifier** | The tenant the fact arose in. **Mandatory on every cross-module business handoff without exception** — including `PLATFORM`-scoped facts, where it names the platform context explicitly rather than being absent | ✔ | `HF-CTX-01`; `SI-01` |
| 2 | **Company context identifier** | Mandatory where the business fact is company-scoped; `N/A` **with reason** where the fact is `TENANT`- or `PLATFORM`-scoped. **Never blank** | ✔ | `HF-CTX-02`; `SI-02`; `MTI-04` |
| 3 | **Source module / domain** | The owning domain, as the owner names itself. **A receiver never infers the owner from payload shape** | ✔ | `HX-` register col. 2; `BD-ACC-01` ownership boundary |
| 4 | **Source business-fact identity** | The occurrence **as its owner identifies it** — not a document number, not a sequence | ✔ | `XMC-C-A3` part 4 |
| 5 | **Accounting-event / downstream correlation identity** | Where the fact has a financial consequence. Assigned by the **Accounting Core**, never by the source module or the posting engine. Basis = tenant · company · owning domain · occurrence · **recognition role** · policy version | ✔ | `XMC-C-A2`, `A3`, `A4` |
| 6 | **Origin reference** | The originating business document or trigger | ✔ | element 11; `HX-` col. 4 |
| 7 | **Event / transaction timestamp** | **Two distinct values, never one**: the physical event date and the entry date | ✔ | `MTI-38`; elements 3 and 4 |
| 8 | **Actor / service principal** | Who or what performed the act. **A rule is a principal only with its identity *and version*; *"the system" is not an asserter*** | ✔ | `HF-CTX-08`; `XMC-C-C3` |
| 9 | **Authorization context reference** | The `AUTH` under which the act occurred, **plus** the attestation naming the `CF-I-03` run that last asserted it | ◐ | `HF-CTX-08` + `HF-CTX-11`; control now specified at `SA_CORR4_03` |
| 10 | **Payload version / schema semantic version** | The **semantic** version of the contract the payload conforms to, and the policy version in force at recognition. **A contract change that alters meaning is a new version; one that does not, is not** | ✎ | `XMC-C-A3` part 6 supplies policy version. **The contract-version element is specified first here** |
| 11 | **Idempotency / correlation key responsibility** | **A responsibility statement, not a key.** The **Accounting Core** owns recognition of a repeat presentation: *"a second presentation of the same basis **is** the same event … the source module is not required to know it is retrying"* | ◐ | `XMC-C-A6`. **The key itself is element 15 and does not exist — `RISK-C02`** |
| 12 | **Reversal / correction reference** | A reversal is a **new** event whose basis includes the identity of the event it reverses, in the reversal role. Never mutation, never deletion; each discoverable from the other | ✔ | `XMC-C-A8`, `A9`; `MTI-39`, `MTI-40` |
| 13 | **Audit trace reference** | The inspectable evidence reference — for context, the `HF-CTX-06` run; for authority, the `HF-CTX-11` run; **never a boolean** | ✔ | element 16; `MTI-50` |

**Tally: 13 of 13 addressed — `10 ✔` · `2 ◐` · `1 ✎`.** Each element appears exactly once, and the
tally is **re-derived from the rows above rather than asserted**.

> **`C4-02-F-06`, self-caught.** This line first read *"9 `✔` · 3 `◐` · 1 `✎`"*. **It summed to 13 and
> its distribution was wrong** — the total was right, which is precisely why a casual read passes it.
> Found by re-deriving the tally mechanically from the table's own state column. **Recorded because the
> programme's rule is that a total is an unverified claim about the rows beneath it, and this package's
> own §5 tally, §3.1's, and every count in `SA_CORR4_06` were re-derived the same way after it.**

**The two `◐` are honest and each names its blocker:** element **9** is specified and its control is
**unbuilt**; element **11** is a responsibility with **no carrier** (`RISK-C02`).
**The single `✎`** — element **10**, the contract semantic version — **is new here and reviewed by
nobody outside this session**, and is named again at §7 as the first thing a challenger should attack.

### 3.2 What this contract deliberately does not specify

Field types · identifier formats (UUID/ULID/sequence — expressly forbidden to this round by
`BD-ACC-01`) · transport · serialisation · ordering guarantees · retry mechanics · storage.
**`XMC-C-A12` binds a consumer regardless: it may not rely on arrival order and must reconcile rather
than infer.**

---

## 4. The nine contract rules

Each is stated, then **classified by what supports it**: `RULED` = follows from a standing Boss ruling ·
`SPECIFIED` = follows from a published invariant or contract clause · `DETERMINED HERE` = this file's
own determination, with independent rationale.

| # | Rule | Basis | Class |
|---:|---|---|---|
| **R1** | **Tenant is mandatory for every cross-module business handoff.** Not conditional on the fact's scope class: a `PLATFORM`-scoped fact names the platform context explicitly | element 10 *"mandatory company **and** tenant context"*, no qualifier; `MTI-01`, `MTI-02`. **`SI-01` cited *by analogy only* — see below** | **RULED** |
| **R2** | **Company is mandatory where the business fact is company-scoped**, and `N/A` **with a stated reason** otherwise. Blank is never permitted | `SCOPE-AWARE EVERYWHERE`; `MTI-04`; Boss contract §3 *"If a field is not applicable, record `N/A` plus reason"*. **`SI-02` by analogy only** | **RULED** |
| **R3** | **A receiver must not infer tenant from any payload content.** Not from a document number, a code, a name, a warehouse, a product, a partner, or a range | `MTI-20` *"never inferred from a name or code"*; `MTI-45` *"mandatory, non-inferable"*; Boss `00`/`01` | **RULED** |
| **R4** | **A receiver must not infer company from user or session defaults where the handoff carries authoritative context.** Where the handoff does **not** carry it, the receiver **rejects the fact** — it does not fall back | `MTI-20` *"never inherited from a session fallback"*; `MTI-45`; `SA10-F-03`, the evidenced defect of resolving accounts in the **user's** company rather than the transaction's | **RULED** |
| **R5** | **A tenant or company mismatch is rejectable and auditable.** The receiver rejects; the rejection is an event with the fact reference, the two contexts and the deny condition. **A mismatch never degrades to a filter, an empty result or a silent no-op** | `EP-P`; `CF-I-03` `D2`/`D3`; `N-01`, `N-03` | **SPECIFIED** |
| **R6** | **Replay and retry preserve the original tenant and company.** A replayed fact keeps the identity of the fact it replays; context is **never re-resolved from current configuration** | `XMC-C-A7`; `MTI-41`; `MTI-42` | **SPECIFIED** |
| **R7** | **Reversal and correction preserve lineage to the original scoped event.** The reversal's basis includes the original identity; **a correction may not change context**; re-dating is not a correction | `XMC-C-A8`, `A9`; `MTI-39`, `MTI-40`; `06` §4 *"corrections may not change context"* | **SPECIFIED** |
| **R8** | **No cross-tenant aggregation is permitted inside statutory posting flows** — and, under `BD-ACC-02`, **no cross-company statutory posting, offsetting or filing either**. The only cross-**company** read is `XCR-02`, within one tenant, read-only, no valuation content while the COGS Gap stands. **There is no cross-tenant analogue** | `BD-ACC-02`; `MTI-25`, `MTI-22`; `GB-08`; `AAS-V-03` | **RULED** |
| **R9** | **Source ownership and downstream execution ownership remain distinct.** The source owns the fact; the Accounting Core owns the event identity; the Posting Engine owns the posting. **A source module may present a fact repeatedly; it may not present an identity** | `BD-ACC-01`; `XMC-C-A2` | **RULED** |

**6 `RULED` · 3 `SPECIFIED` · 0 `DETERMINED HERE`.**

> **`C4-02-F-08`, found by independent challenge.** `R1` and `R2` first cited `SI-01` and `SI-02` as
> though those rulings governed cross-module handoffs. **They do not.** The ruling's own decision line
> reads **`APPROVED — CROSS-GATE SAAS INVARIANTS SHALL APPLY TO EVERY COA CLOSURE GATE`**, and §2
> scopes them *"mandatory across **COA-G01, G02, G03, G04, G04S, G05, G06, G07 and G08**"* — the
> Thailand Chart-of-Accounts closure gates, **not the Sales, Purchase or Manufacturing boundaries
> `R1` and `R2` are addressed to.**
>
> **`R1` and `R2` survive as `RULED`** on element 10's own unqualified text, `MTI-01`/`-02`/`-04` and
> the `SCOPE-AWARE EVERYWHERE` correction — **all of which do govern this subject.** `SI-01`/`SI-02`
> are retained **as analogy, labelled as such**. **The classification is unchanged and the citation
> was over-extended, which is the programme's *exclusion-needs-authority* defect inverted: an
> authority claimed wider than its own grant.**

> **That distribution is the finding, and it is the strongest single result in this file.** All nine
> rules the master prompt asks Phase SA to *"prove or specify"* were **already settled** — six by
> standing Boss rulings and three by published invariants. **Not one required a new determination.**
> What was missing was never the rules. **It was that they had never been assembled into one contract,
> and were therefore invisible to any party holding only one half.** `C4-02-F-01`, `C4-02-F-02` and
> `C4-02-F-03` are three independent instances of the same shape.

### 4.1 Two rules that read as reciprocal and are not

**R3 and R4 are asymmetric on purpose.** R3 forbids inference **always** — tenant is the security
boundary, and no payload content is ever evidence of it. R4 forbids inference **where the handoff
carries authoritative context**, and requires **rejection** where it does not.

The asymmetry is `SCOPE-AWARE EVERYWHERE`: company is legitimately absent on `PLATFORM`- and
`TENANT`-scoped facts, so "company is absent" is not by itself an error — but **taking it from the
session is always one.** Stated because the natural simplification — *"never infer either"* —
**over-constrains in exactly the direction `CORR1` corrected**, and would make every platform-scoped
handoff non-compliant.

---

## 5. Cross-domain proof

**Method.** For each flow: does an emitting artefact exist; does it carry elements 1 and 2; do R1–R9
hold; and what is the exact gap. Classified `CONTRACT-SUFFICIENT` / `CONTRACT-GAP` /
`NOT APPLICABLE` / `RESEARCH REQUIRED`.

**`CONTRACT-SUFFICIENT` means:** the contract is specified for the flow to the point where a Pre-Test
case can be written. **It does not mean built, proven, verified or compliant.** `0 of 10` material
handoffs are contract-compliant and that figure is unchanged by this file.

| # | Flow | Emitting artefact | El. 1 · 2 | R1–R9 | Class |
|---:|---|---|---|---|---|
| 1 | **Sales → Inventory** | **none authored by the emitter.** `HX-01`/`-03` are *Inventory's* register of facts it **receives** | Absent / supplied | hold | **`CONTRACT-GAP`** — §5.0 |
| 2 | **Sales → Manufacturing** | **none** — no `HX-` row; `HX-18` is Manufacturing→Inventory | — | — | **`CONTRACT-GAP`** — **no emitting artefact exists for this boundary at all** |
| 3 | **Sales → Purchase / dropship** | **none.** `XMC-H-03` records the boundary as *"a control breach, not a data gap"* — the write **bypasses the demand-approval gate every human-raised purchase must pass** | — | **R9 holds; `XMC-C-D3` binds** — a route inherits its destination's entry conditions | **`CONTRACT-GAP`** — and the gap is a **control-floor** gap, not a context gap |
| 4 | **Purchase → Inventory** | **none authored by the emitter.** `HX-04` is *Inventory's* receiving-side row | Absent / supplied | hold | **`CONTRACT-GAP`** — §5.0 |
| 5 | **Inventory → Accounting** | `HX-07`, `-09`, `-10`, `-11`, `-12`, `-14`, `-17`, `-20` + `HF-CTX-01`…`-11` | **Specified `Always`** | hold | **`CONTRACT-SUFFICIENT`** — the only flow with both halves published. **Elements 4, 7, 14, 15 remain absent for non-context reasons** |
| 6 | **Manufacturing → Inventory → Accounting** | **first leg: none authored by the emitter** (`HX-18` is Inventory's receiving-side row). **Second leg Inventory→Accounting is covered** | Absent / supplied | hold | **`CONTRACT-GAP` on the first leg** — §5.0. `R-22` `GAP`; fixed-overhead elements have no injection path |
| 7 | **AR/AP → Payment/Bank → Accounting** | **none** | — | **R8 binds**; `H-07` records matching as `NOT DURABLE` and *"freely destructible across a closed period"* | **`CONTRACT-GAP`** — **no emitting artefact; and the receiving side's own durability is `NOT DURABLE`, so a context guarantee would attach to a destructible record** |
| 8 | **Asset → Accounting** | **none.** Routing found **one missing consumer — Asset → Equipment** | — | — | **`CONTRACT-GAP`** |
| 9 | **Expense → Accounting** | **none** | — | — | **`CONTRACT-GAP`** |
| 10 | **Tax-related handoffs** | `HX-27`, `-28`, `-31` — all `TAX-HOLD` | Absent / supplied | **R2 and R8 bind hardest**: `BD-ACC-02` makes statutory tax company-scoped, so a fact spanning companies **has no statutory owner and cannot be filed** | **`CONTRACT-SUFFICIENT` for context · `HOLD / EVIDENCE REQUIRED` on every statutory element.** **No statutory Thai claim is made here** |

**Tally: `2 CONTRACT-SUFFICIENT` · `8 CONTRACT-GAP` · `0 NOT APPLICABLE` · `0 RESEARCH REQUIRED`.**
Ten rows, each classified once. ✓ `SUFFICIENT` = flows **5** and **10**, the two where **Inventory is
the emitting party.**

### 5.0 `C4-02-F-09` — the classification was wrong on three flows, and the error was mine

> **Found by independent challenge, and it is the single largest correction in this package.**

This table first classified flows **1, 4 and 6** `CONTRACT-SUFFICIENT` on the strength of `HX-01`,
`HX-04` and `HX-18`. **Those rows are in `10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md`, whose own header
reads `SMEsPlus-OWNED HANDOFF DESIGN` — and its owner is Inventory.** On flows 1, 4 and 6 the emitting
parties are **Sales, Purchase and Manufacturing**, and `HX-01`/`-04`/`-18` are **Inventory's record of
what it expects to receive from them** — not a commitment by any of the three to attach `HF-CTX-01`
and `HF-CTX-02`.

**And `SA_CORR4_00` §5 reproduces the fact that settles it:** `FINAL_SOLUTION` holds **30 paths, `0`
outside `INVENTORY`**. **Sales, Purchase and Manufacturing have no producing-side design package** —
**which is the exact condition this file used to fail flows 2, 7, 8 and 9.**

> **The test I stated was *"a producer has published."* The test I actually applied to flows 1, 4 and 6
> was *"Inventory has documented this boundary from its own side."* Those are different tests, and
> applying the weaker one to three rows while failing four other rows on the stronger one is not a
> classification — it is an inconsistency that flattered the result.**

**Corrected: `5 / 5` becomes `2 / 8`.** Only flows **5** (Inventory → Accounting) and **10**
(Inventory → Audit/Tax) have an artefact authored by the party that emits.

**§5.1's core finding is not weakened by this — it is enlarged.** The gap was already *"the absence of
a producing-side design"*; **it is now eight flows rather than five, and the one-to-one correspondence
with the missing `FINAL_SOLUTION` packages is exact rather than approximate.** The correction makes the
result worse and the reasoning sounder, which is the right direction for a correction to run.

### 5.1 `C4-02-F-04` — the gap is one shape, in eight places

**Every one of the eight `CONTRACT-GAP` rows fails for the same reason, and it is not tenant or
company.** Flows **1, 2, 4, 6, 7, 8 and 9** have **no artefact authored by the emitting party** — no
register, no payload definition, no field list. Flow **3** has a boundary described only as a control
breach.

> **The eight gaps are not element-10 gaps. They are the absence of a producing-side design on seven
> domain boundaries, plus one control-floor breach.** Applying `XMC-C-D2` — *"a rule addressed to a
> receiver with no element capable of satisfying it is not a rule"* — **R1 and R2 are presently rules
> addressed to nobody on flows 1, 2, 4, 6, 7, 8 and 9.** They bind the moment a producer publishes, and until
> then they are unenforceable **not because they are weak but because the addressee does not exist.**

**Structural corroboration, reproduced:** `FINAL_SOLUTION` holds **30 paths, `0` of them outside
`INVENTORY`** — there is no `FINAL_SOLUTION/ACCOUNT`, `/SALES`, `/PURCHASE`, `/ASSET` or `/EXPENSE`.
**Every flow whose emitting party has no `FINAL_SOLUTION` package is a `CONTRACT-GAP`, and the two
`CONTRACT-SUFFICIENT` flows are exactly the two Inventory emits.** The correspondence is one-to-one
and is not a coincidence: **the contract is sufficient wherever the emitting party has published and
gapped wherever it has not.**

### 5.2 `C4-02-F-05` — element 10 and element 15 remain one object with two names

`SA_CORR3_06` `JCP3-F-05b`, carried and **not weakened by this contract**: the only idempotency carrier
anywhere in the estate is *"table-global rather than tenant-scoped"*, so **the sole mechanism that could
satisfy element 15 is by its own scoping incapable of satisfying element 10.**

**This contract does not repair that and must not be read as doing so.** Element 11 of §3.1 is a
**responsibility statement** — it says who must recognise a repeat presentation. **It does not supply
the key, and `RISK-C02` is unchanged.** A reader taking §3.1 row 11 as element 15 supplied would be
making precisely the error `CF-V-01` exists to prevent, one element along.

### 5.3 `C4-02-F-07` — a stranded event architecture states positions on elements 10 **and** 15, and no register cites it

**`ARC-WP-010 INTEGRATION_EVENT_ARCHITECTURE`**, on the same unmerged branch as the 19 deliverables of
`SA_CORR4_01` `C4-01-F-07`, states verbatim:

| § | Text | Bears on |
|---|---|---|
| 12.4 | *"Domain events … are append-only, versioned, **tenant-scoped** and never mutated/deleted. Each event has an **owning source**."* | element 10; `R9` |
| 12.3 | *"validation, entitlement and **tenant resolution at the gateway**"* | `R3`, `R4` |
| **12.7** | *"**Every consumer uses an idempotency key (event ID / business key) to prevent duplicate side effects** (critical for Posting Engine)."* | **element 15** |
| 12.5 | *"**At-least-once** delivery with **idempotent consumers**; ordering preserved per aggregate where required."* | element 15; `XMC-C-A12` |
| 16 | *"**Every event carries tenant context; consumers reject events outside their tenant scope**; external webhooks are tenant-scoped."* | element 10; `R5` |
| 12.8 | *"external tokens are least-privilege and **scoped per tenant**"* | `SA_CORR4_01` class 6 |
| 13 | `ADR-ARC-002` immutable event store · `ADR-ARC-017` at-least-once + idempotent consumers · `ADR-ARC-018` gateway-only external integration — **all `PROPOSED`** | — |

**Citation measurement.** `ARC-WP-010` returns **14 paths**; `INTEGRATION_EVENT_ARCHITECTURE` returns
**15**; **`ADR-ARC-017` returns 4, every one of them inside the stranded package itself.**
**Outside that package the only citers are a STEP0301 document inventory and this CORR4 file.**
**No `MTI-*` register, no element-15 register, no Phase SA artefact cites any of them.**

> **`C4-02-F-07`. The programme's standing statement about element 15 is that the object *"does not
> exist"* and *"none has been designed."* That is **true of the corpus every consumer reads and false
> of the repository.** An architectural position on idempotency — a named key source, a delivery
> guarantee, a consumer obligation and a proposed ADR — was written on 2026-07-14 and has been
> invisible ever since.

**What this does NOT do, stated firmly because the temptation is real.** §12.7 places an obligation on
*consumers* and names a **key source** (*"event ID / business key"*). **It does not define a
deterministic identity basis**, which is what element 15 requires and what `XMC-C-A3` specifies six
parts of. **It is `Version 0.1 · DRAFT · NOT VERIFIED · Gate Status: HOLD`, its ADRs are `PROPOSED`,
and its named review never occurred.**

> **Element 15's status does not move. `RISK-C02` stands. `0 of 10` handoffs compliant stands.
> `JCP3-F-05b` stands** — the only *implemented* carrier in the estate remains table-global and
> therefore incapable of satisfying element 10.
>
> **What changes is the act.** CORR3 classified element 15's remedy as *"a design act — origination."*
> **On this evidence it is an adjudication act**: read a draft that exists, reconcile it with
> `XMC-C-A3`'s identity basis and with `MTI-31`'s run-scoping, and have it independently reviewed.
> **Cheaper, and more honest, than commissioning the origination of something already written.**

**Folded into `C4-D-01`**, which already carries the joint-artifact appointment, rather than raised as
a third escalation for one governance cause.

---

## 6. What this file changes, and what it does not

| | |
|---|---|
| Element 10's status | **Unchanged** — `specified, not built, not verified`. `AAS-V-01` in force |
| Handoffs contract-compliant | **`0 of 10`. Unchanged** |
| Element 15 | **Unchanged** — `RISK-C02` open |
| Elements 4, 7 | **Unchanged** — `HOLD / ACCOUNTING COGS GAP` |
| Element 14 | **Unchanged** — provenance reference does not exist; `GAP-FS-08` |
| Vetoes | **6 in force, 0 discharged** |
| Anything proven | **Nothing. `0` remains `0`** |
| **What does change** | The interface half of element 10 is **stated as one contract** — 13 elements, 9 rules, 10 flows — instead of two disjoint half-specifications neither party could execute alone. **A Pre-Test case can now be written against it.** It cannot yet be executed |

---

## 7. Residual, stated exactly

1. **Five of ten flows have no producing-side design.** Naming that is not closing it, and this session
   does not author another domain's design. **`C4-D-01`** — the mandated joint artifact's
   commissioning — is an **appointment**, not a decision.
2. **`XMC-C-D1` is one clause of a thirty-clause contract published by CORR3 and reviewed by nobody.**
   CORR3 says so in terms: *"The `BD-ACC-01` contract published here has been reviewed by nobody. It
   was written by the same model that assessed it."* **This file inherits that exposure and adds to it.**
3. **Element 10 of §3.1 — the contract semantic version — is new here** and has no prior source. It is
   the one `✎` and the first thing a challenger should attack.
4. **The `N/A` with reason mechanism is load-bearing and untested.** R2 permits company to be `N/A` on
   `PLATFORM`- and `TENANT`-scoped facts. **If the scope class of a fact is itself wrong, R2 licenses
   the omission and `CF-I-03` `D5` is the only thing that catches it.** The scope-class assignment is
   therefore a single point of failure this contract does not itself protect. **Recorded; not solved.**
5. **The `HX-`/`HF-CTX-` join in §5 was tested by independent challenge and is stronger than I
   claimed.** I recorded it as *"an inference from subject matter."* It is not — `HO-nn` and `HX-nn`
   are **the same rows**, content-for-content (`C4-02-F-02` as corrected). **The residual that remains
   is the opposite one: neither register declares the alias**, so a future reader of either can still
   miss the other, and nothing in the corpus fixes that.

---

## 8. Checkpoint

> ## `CP-SA-C4-20 — XMC-C-D1 CONTRACT CLOSED`
> **13 of 13 elements addressed · 9 of 9 rules stated, `6 RULED` + `3 SPECIFIED` + `0` newly
> determined · 10 flows proved: `2 CONTRACT-SUFFICIENT` / `8 CONTRACT-GAP`** — corrected from `5 / 5`
> by independent challenge (`C4-02-F-09`).
> **9 findings** — `C4-02-F-01` … `C4-02-F-09`. **1 escalation** — `C4-D-01`, an appointment.
> **Element 10 does not move. `0 of 10` handoffs compliant. 0 vetoes discharged.**

**Next autonomous action:** `CP-SA-C4-10`, on the returning privileged-path evidence.

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
