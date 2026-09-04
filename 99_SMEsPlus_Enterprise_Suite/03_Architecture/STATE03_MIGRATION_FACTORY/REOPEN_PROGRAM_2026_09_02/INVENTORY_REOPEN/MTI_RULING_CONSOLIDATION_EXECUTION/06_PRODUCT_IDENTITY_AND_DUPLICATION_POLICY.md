# [SMEPLUS-26-09-04-INV-MTI-RULING-CONSOLIDATION-001]
# 06 — Product Identity And Duplication Policy

Control Level: `/L9999.9999`
Status: `POLICY CONSOLIDATED FROM MTI-D-01 — RE-SPECIFICATION REQUIRED — MAPPING LAYER UNSPECIFIED`

---

## 1. The Policy, Stated Once

**A product is a company-owned business object.** Its definitional identity is anchored to `company` within `tenant`. Two records in two companies that share a code, a name, a barcode, a unit of measure, a category, a route or a description are **two different business objects**, and treating them as one is prohibited.

**Duplication is not a defect.** It is the expected and correct consequence of operational and legal separation per company, and no design output, register, report, control or remediation may describe it as a defect, an anomaly, a data-quality issue, or something to be cleaned up.

---

## 2. Why The Policy Is What It Is — `L1`

Boss's stated reason governs interpretation, and is recorded here because a downstream reader who has only the rule will eventually apply it wrongly.

Two companies may perform what is described by the same words and mean two different things. Boss's worked example: Company A does transport business subject to a 1% withholding condition; Company B states it is hired transport service with no such condition. **The service description is nearly identical and the tax treatment is not.**

AAS+ enumerates the dimensions that may differ behind identical-looking names: tax treatment, withholding practice, product/service meaning, accounting mapping, approval path, route/rule policy, reporting requirement, and migration provenance.

**The operative principle: similarity of label is not evidence of identity of object.** Any rule in this file that could be read as collapsing two objects because they look alike is being read wrongly.

---

## 3. The Six Binding Identity Rules

| # | Rule | Source |
|---:|---|---|
| **P-01** | Product definitional identity is anchored to `company` within `tenant` | `D-01` §1, rule 1 |
| **P-02** | Code, name, barcode, UoM, category, route or description similarity **never** creates shared identity across tenants or companies | `D-01` rule 2; AAS+ `25` §3.4 |
| **P-03** | Cross-tenant deduplication is **not a requirement**. Cross-company deduplication is **not a default requirement** | `D-01` rules 3, 4 |
| **P-04** | Cross-company or group-level comparison requires an **explicit controlled mapping / provenance layer** | `D-01` rule 5 |
| **P-05** | Every consuming module resolves product identity **through** tenant/company context, never by inference | `D-01` rule 6 |
| **P-06** | Migration **may preserve** duplicate products where that reflects source business reality; reporting aggregates **only after** an authorized mapping exists | `D-01` rules 7, 8 |

---

## 4. What This Changes In The Published Design — `L6`

The invariant set took the opposite option. The delta is exact and is repeated here because `06` is the file a re-specification pass will work from.

| Artifact | As Published | Required Under `MTI-D-01` |
|---|---|---|
| `MTI-11` anchor | Definitional identity anchored to **`tenant`** | Definitional identity anchored to **`company`** |
| `MTI-11` enablement clause | *"A company may transact a product only where an explicit company enablement exists"* | **Void as written.** Ownership is the enablement. Retaining the clause implies a shared master that does not exist |
| `MTI-11` status | `SPECIFIED — CONDITIONAL (MTI-D-01)` | Conditionality **resolved**; content rewritten |
| `XCR-03` — tenant-level definitional master reference | One of four cross-context register entries, `SPECIFIED — CONDITIONAL` | **ELIMINATED.** Register falls to **3** entries |
| `04` §4.1 — *"tenant-level definitional data is a shared surface, and shared surfaces must be proven too"* | A live proof obligation | **Void for product and variant.** No shared surface exists to prove |
| `04` matrix rows 5, 6, 7 | `SPECIFIED — CONDITIONAL` | Conditionality resolved; anchors rewritten to `company` |
| `L10-04`, `MTA-17` | Conditional on `MTI-D-01` | Conditionality resolved; re-scored against a company-anchored master |
| `MTI-16` costing/valuation attachment | Company-scoped | **Unchanged.** Already correct under either option |
| Element 8 `WHICH Product / Lot / Serial` | Resolved tuple, not bare value | **Simplified.** The product half is company-resolved by construction |

**Two of these are reductions in work — `XCR-03` and `04` §4.1. Option B removes a shared surface that would otherwise have needed its own isolation proof.** That is a genuine and under-appreciated benefit of the ruling and is recorded as `RC-F-02`.

---

## 5. The Control That Must Replace Deduplication — `L8`

### 5.1 The problem the ruling knowingly accepts

The invariant set's own statement of Option B's cost is exact and is not softened here:

> *"the same physical item exists as several unrelated identities within one tenant; inter-company transfer loses its natural correlation; Thai SME groups that operate several companies over one catalogue would maintain duplicate masters, **which the L8 evidence names as a live source of identity failure**."*

Boss has ruled with that cost visible, and the ruling is authoritative. **This session does not re-argue it.** What this session must record is a control consequence that follows and that no document yet addresses:

**Deduplication is no longer available as a control against identity failure, because deduplication is now prohibited as a default. The identity-failure mode the L8 evidence names does not disappear because the remedy was ruled out. It now requires a different control, and no published design supplies one.**

### 5.2 What the ruling puts in its place

`D-01` rules 5 and 8 name the replacement: an **explicit controlled mapping / provenance layer**. Aggregation happens only after an authorized mapping exists.

**That object does not exist in any published design.** Not in R4, not in the review, not in the invariant set. The nearest construct — `XCR-03`, the tenant-level definitional master reference — is the very thing the ruling eliminates, and it served a different purpose: it let a company-scoped record *reference* a shared definition. A mapping layer does the opposite: it asserts a *correspondence* between records that remain separate.

Recorded as `RC-F-03`, **BLOCKING** for any group-level reporting.

### 5.3 The properties the mapping layer must have

Derived from the rulings and the standing invariants. **This is a requirement statement, not a design.**

| # | Required Property | Source |
|---:|---|---|
| M-01 | It **asserts correspondence; it never merges identity.** Both sides remain separate business objects after mapping | `D-01` rules 1, 2 |
| M-02 | It is **explicit and authorized.** A mapping is created by a named authority, never derived from similarity | `D-01` rules 2, 5 |
| M-03 | It is **evidenced** — who mapped, when, on what basis, under what authority | `MTI-38`, `MTI-50` |
| M-04 | It **never crosses a tenant boundary** | `MTI-25`; `D-01` rule 1 |
| M-05 | It is **versioned and non-retroactive.** A mapping created today does not re-interpret a report produced yesterday | `MTI-36`, `MTI-06` |
| M-06 | It carries **no quantity, no value, no policy attachment and no history** of its own. It is a correspondence, not a record of business | `XCR-03`'s eliminated constraint, carried forward as the correct shape for the replacement |
| M-07 | Any report produced across a mapping **states the mapping version it used** as part of the report's identity | `MTI-28` |
| M-08 | It **carries no valuation content while the COGS Gap stands** | `AAS-V-03` |
| M-09 | Its use is **scoped, time-bounded and logged**, exactly as a cross-context read is | `MTI-25`, `XCR-02` |
| M-10 | It must not become the **de facto shared master** it replaced. A mapping that everything is routed through is a shared master with extra steps | `D-01` §1; AAS+ `25` §3.5 |

### 5.4 The dependency this creates — `RC-F-04`

Properties M-04, M-08 and M-09 are the properties of `XCR-02`, the Cross-Context Report Grant, whose status is `SPECIFIED — CONDITIONAL (MTI-D-04)`. **`MTI-D-04` — whether a sanctioned cross-company read exists at all — is unruled.**

`D-01` rules 5 and 8 therefore presuppose a mechanism whose existence is itself an open Boss decision. The ruling is not thereby defective; it is not fully operable until `MTI-D-04` is ruled.

The invariant-set package's warning applies with more force now than when it was written: *"Not deciding is not neutral. The need gets met by export, which is the worst outcome."* Under Option B a Thai SME group has **more** need for a group view, not less, because it now maintains several catalogues rather than one.

---

## 6. Migration And Historical Continuity Under Option B — `L10`

| Requirement | Consequence |
|---|---|
| `D-01` rule 7 — migration **may preserve** duplicate products where that reflects source business reality | Migration must be able to produce duplicates **deliberately**, and must be able to **evidence** that the duplication was deliberate rather than a fault. That evidence is provenance, and provenance is `GAP-FS-08`, which does not exist |
| `MTI-42` — context may never be **inferred** at migration | A migration that assigns company by name-matching a product across source systems would violate both `MTI-42` and `P-02`. `R4-F-24` records exactly this failure mode for location kinds |
| `R4-F-23` — migrating legacy batch identities without company scope imports the collision surface in bulk | **Narrowed.** `MTI-12` plus `P-01` make the target state unambiguous. Still open; only implementation and verification close it |
| Handoff element 14 `WHICH Migration / Replay Batch` | **Obligation widened.** The provenance reference must now evidence deliberate duplication, not only batch membership |

**Net effect on `GAP-FS-08`: unchanged in status, larger in scope.** It was `BLOCKING`; it remains `BLOCKING` and now has more to evidence.

---

## 7. Inter-Company Transfer Under Option B — `L4` / `L5`

`XCR-01` — inter-company transfer — was already `INCOMPLETE` on `JT-10` (open) and `GAP-FS-07` (path never traced end to end). Option B adds a structural difficulty that must be recorded.

Under Option A, the two sides of an inter-company transfer would have shared a tenant-level definitional identity, giving the pairing a natural correlation. **Under Option B they are two unrelated product identities.** The correlation must therefore be carried **entirely by the relationship** — the `MTI-22` register entry and the correlation identity in `HF-CTX-07` — and may **never** be reconstructed by matching product attributes, because `P-02` prohibits exactly that.

This does not make inter-company transfer impossible. It makes the relationship identity load-bearing where it was previously corroborated. `JT-10` is unchanged in status and harder in content.

**No valuation consequence of inter-company transfer is stated here.** `JT-01` is **NOT DECIDABLE**, `JT-10` is open, `GAP-FS-07` records the path as never traced. `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`.

---

## 8. The Disclosure Channel Widens — `MTI-F-03`

`MTI-27` requires that **absence must not leak existence**: a caller outside a record's `CTX` receives the same response as for a record that does not exist.

`MTI-F-03` raised this because `MTI-12` made traceable-identity uniqueness per-company. **`MTI-D-01` extends the same condition to products.** Under Option B, per-company product uniqueness is the ruled norm, so a user in Company A entering a product code already used in Company B must receive a response that discloses nothing.

The channels are: uniqueness feedback · autocomplete and suggestion · barcode resolution · error text · identifier-collision messages · import validation responses · export scoping.

**`MTI-F-03`'s scope is larger than when it was raised, and it was raised as `MATERIAL`.** It is not upgraded here — severity classification of another session's finding is not this session's act — but the widening is recorded so that whoever re-scores it does so with this in hand.

---

## 9. What Must Not Be Done, Stated As Prohibitions

Because the most likely failure mode of this policy is a well-intentioned optimisation.

| # | Prohibited | Why |
|---:|---|---|
| 1 | Merging, linking or correlating products by code, name, barcode, UoM, category or description similarity | `P-02`. This is the ruling's central prohibition |
| 2 | Reporting duplicate products across companies as a data-quality defect, anomaly or cleanup candidate | `D-01` §1, rule 3; the required carry-forward wording |
| 3 | Building a de facto shared master under a different name — a "golden record", a "canonical product", a "master mapping table" everything routes through | M-10; `D-01` §1 |
| 4 | Aggregating across companies before an authorized mapping exists | `D-01` rule 8 |
| 5 | Carrying valuation content across a mapping while the COGS Gap stands | `AAS-V-03` |
| 6 | Inferring company from product at any point in any module | `P-05`, `MTI-42` |
| 7 | Recording `MTI-11` as satisfied, or the product isolation property as proven, on the basis of this file | `AAS-V-01`'s principle; nothing here is built or verified |
| 8 | Treating the mapping layer as designed because its properties are enumerated at §5.3 | `RC-F-03`. Requirements are not a design |

---

## 10. Policy Status

| Dimension | Status |
|---|---|
| Ruled by Boss | **Yes** — `MTI-D-01`, Option B |
| Policy stated | **Yes** — six rules, ten mapping-layer properties, eight prohibitions |
| Published design conforms to it | **No** — `RC-F-01`, `MTI-11` inverted |
| Replacement control designed | **No** — `RC-F-03`, mapping layer unspecified |
| Replacement control operable once designed | **Not yet** — `RC-F-04`, depends on `MTI-D-04`, unruled |
| Migration able to evidence deliberate duplication | **No** — `GAP-FS-08` |
| Any product isolation property proven | **No** — `L9-02` `DEFINABLE`, not proven |
| Thai-validated | **No** — `0 of 78` |
| Valuation consequences stated | **No** — `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |

`DECIDED BY BOSS — SPECIFIED, NOT BUILT, NOT VERIFIED — REPLACEMENT CONTROL UNSPECIFIED`

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
