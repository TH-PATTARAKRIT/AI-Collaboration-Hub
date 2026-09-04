# P01 — AAS+ CONSOLIDATION

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

Per `§2.10`, this consolidates agreements, disagreements, contradictions, missing evidence,
cross-process impact, and architecture / SaaS / accounting / business-fit risk.
**Minority challenge is preserved, not averaged away.**

---

## 1. THE SINGLE MOST IMPORTANT STATEMENT

> **The receipt-to-bill accounting bridge that this package traced in the v18 source has no
> physical structure to run on in two of the three readable deployed databases.**

The deployed v19 databases have no goods-received clearing account on the item category and no
inventory valuation-layer table at all. `P01_DEPLOYED_SCHEMA_EVIDENCE.md` §3, class A within
those two databases.

Everything else in this package is subordinate to that, because it determines **which of these
findings are about the system the project is actually building on.**

---

## 2. AGREEMENTS — WHAT ALL EVIDENCE LAYERS SUPPORT

1. **A purchase order creates no payable and no journal entry on confirmation.** Source-verified;
   the directive's instruction not to assume otherwise is borne out.
2. **The vendor bill is the only universal accounting event in procure-to-pay** — *within the
   journal-entry creation-site population declared in the evidence base, which is a floor and
   not a total, so this is class **B**, not a verified absence of other paths.* Every purchase
   shape reaches it; every upstream effect found is conditional.
3. **Item and company configuration, not the business event, selects the accounting pattern.**
   Five ledger patterns behind one document set; of fourteen switches that decide the shape,
   effectively one is a per-transaction business decision.
4. **The receipt's accounting date is not the receipt's date.**
5. **Three-way matching, where present, is a report and not a control.**
6. **Several failure paths are silent** — no error, no warning, no suspense posting.

---

## 3. DISAGREEMENTS AND MINORITY POSITIONS — PRESERVED

| # | Position | Counter-position | AAS+ resolution |
|---|---|---|---|
| 1 | This session: the receipt entry's date has three branches | Code & UI Architect: three in the older generation, **two** in the newer, and the first is unreachable in procure-to-pay | **Expert governs**, re-derived and confirmed. The session's original statement was over-general |
| 2 | Localization expert: lock dates are **not** bypassed in the custom roots (class A) | Code & UI Architect: the same custom module escapes the lock via direct SQL | **Both stand.** Not a contradiction: one is about the accounting lock, the other about a path outside it. **Neither was suppressed to produce agreement** |
| 3 | Functional Design expert: access exposure is write on order lines | This session: write on the order, its lines and the matching object, in both generations | **The wider reading governs**, after this session first got its own cross-version comparison wrong (`ERR-P01-03`) |
| 4 | This session: the down-payment wizard converts bill lines | Functional Design expert: it also creates and self-confirms an order from the bill | **Both true.** The session's account was incomplete |
| 5 | Database Design expert: the top-ranked custom risks are **not installed** in any readable database, so they are latent | The same modules are severe where installed | **Both retained.** Severity and reachability are separate axes and this package keeps them separate |

---

## 4. CONSOLIDATED RISK

### 4.1 Accounting risk

| Risk | Evidence | Severity |
|---|---|---|
| A soft period lock **relocates** a posting instead of refusing it; cut-off testing on entry dates is self-confirming | `CONTRA-P01-08` | **Critical** |
| Correction by **deletion** of derived journal items on reset-to-draft or cancel | `CONTRA-P01-01` | **Critical** |
| Price difference silently **not posted** where the item has no expense account | `EV-P01-14` | High |
| The clearing bridge silently **never closes** where the account is not flagged reconcilable | `EV-P01-10` | High |
| A payment produces **no entry at all** without an outstanding-payments account | `EV-P01-20` | High |
| Withholding on partial vendor payments **compounds instead of netting** | `CONTRA-P01-09` | **Critical**, custom layer |
| Two shipped copies map the same fact to **opposite statutory forms** | `CONTRA-P01-10` | **Critical**, unresolvable here |
| A missing exchange rate resolves silently to a fallback with no date filter, then to 1.0 | `EV-P01-50` | High |

### 4.2 Architecture risk

| Risk | Evidence |
|---|---|
| The bill-to-receipt match depends on **audit-log tracking rows**, not on accounting records — and migrated documents have none | `CONTRA-P01-06` |
| Deleting one order line erases the bill's origin **and** the receipt's purpose in one operation | `CONTRA-P01-11` |
| Two representations of the received-not-billed obligation, neither aware of the other, one leaving no trace on its source document | `CONTRA-P01-02`, `EV-P01-17` |
| Asset classification and inventory clearing **compete for the same field** on the same bill line | `CONTRA-P01-04` |
| Order reset-to-draft has **no guard at all**, while cancel is guarded | `EV-P01-43` |

### 4.3 SaaS and scope risk

| Risk | Evidence |
|---|---|
| A **company-scoped financial effect** is raised in a company whose ownership of that effect is inferred from a **tenant-scoped** contacts hierarchy, resolved with elevated privilege, first match winning, superuser by default, optionally auto-posted | `P01_SCOPE_OWNERSHIP_MATRIX.md` §4 |
| **No tenant test found** on that path — class B, three files searched | `EV-P01-31` |
| Mutation authority follows the tenant-scoped object while the financial effect is company-scoped | `CONTRA-P01-05` |

**The first of these is the tolerance-zero item.** Under `EC-04` a conditional outcome may not
bypass a tolerance-zero risk.

### 4.4 Business-fit risk

| Observation | What it implies |
|---|---|
| Vendor advances are **bill-first** in the base and the project added its own advance-payment modules in both custom sets | The base shape did not fit the business |
| Three requisition mechanisms coexist (base agreements, an approvals capability, the project's own purchase request) | No single owner for "a need to buy has been raised" |
| The **service-received** business fact has no document of its own | A whole purchase class has no operational event |
| Nine independent withholding formulas, two of them in vendor-facing documents that never net prior payments | The document handed to the vendor and the ledger disagree by construction |

### 4.5 Segregation-of-duties risk

Individually verified, and material only in composition:
order reset-to-draft is unguarded (`EV-P01-43`) → a reset order's quantity and price become
editable → the accounting-invoicing group holds write on exactly those fields (`EV-P01-44`) →
bill-to-order matching does not test the vendor on the reference branches (`EV-P01-39`) → on
match, the vendor's own bill lines are **replaced** by the order's (`EV-P01-41`).

**Composite: the party that receives the invoice can make the commitment agree with it, and
the matching step can then erase what the vendor actually billed.**
Each component FACT VERIFIED; the composition **SUPPORTED INTERPRETATION**, runtime
confirmation required.

---

## 5. MISSING EVIDENCE, RANKED BY HOW MUCH IT WOULD OVERTURN

1. **Which generation and which copy is deployed** (`DEP-P01-01`). Gates `CONTRA-P01-07`,
   `CONTRA-P01-10`, most of the localization findings and six functional findings.
2. **Runtime behaviour.** Nothing in this package was executed. Seven cases are ranked for
   first execution in `P01_EDGE_CASE_TEST_MATRIX.md`.
3. **Authoritative Thai statutory sources** (`DEP-P01-04`). Twenty statutory entries, all held.
4. **The tenant test on the cross-company path** (`DEP-P01-02`). Tolerance-zero.
5. **A pass briefed under the corrected scope constitution** (`DEP-P01-06`).

---

## 6. CROSS-PROCESS IMPACT

`P01_CROSS_PROCESS_OWNERSHIP.md` carries the detail. The three that most constrain peers:

- **`HO-05`** — the received-not-billed obligation needs one owner across P01, Inventory and
  Account.
- **`HO-06`** — what *proves* ownership of a company-scoped financial effect is a platform
  question, and every peer process that can trigger an effect in another company inherits it.
- **P11** — this package's scope matrix is the first input to cross-process scope
  reconciliation, and it carries seven unresolved scope questions rather than assertions.

---

## 7. WHAT THIS CONSOLIDATION REFUSES TO DO

- It does not convert any class B, C or D negative into a class A absence.
- It does not resolve a contradiction by preferring the more convenient side.
- It does not treat expert agreement as verification: **every admitted expert finding was
  re-derived from source or schema by this session**, and those not re-derived are labelled.
- It does not claim convergence. Eleven contradictions stand and **the count rose during the
  session**.
- It does not present this package as implementation input. Per `§9` of the exit constitution,
  design work on this basis can only be `PROVISIONAL / NON-CANONICAL`.
