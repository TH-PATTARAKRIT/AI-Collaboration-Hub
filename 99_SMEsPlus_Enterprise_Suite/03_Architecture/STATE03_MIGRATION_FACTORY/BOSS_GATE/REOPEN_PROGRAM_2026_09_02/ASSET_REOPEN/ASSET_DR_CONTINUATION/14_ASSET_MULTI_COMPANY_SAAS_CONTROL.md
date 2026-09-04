# 14 — MULTI-COMPANY / SaaS CONTROL (LEVEL 16)

**LAYER 2 — AUDIT QUARANTINE.**

Requirement: no cross-tenant access, no cross-company cost leakage. This report
establishes what the reference product actually enforces, finds the leakage vectors,
and separates the eight scoping concepts the prompt requires to be kept apart.

---

## 1. The scoping ladder — eight concepts, and where each exists

| Concept | Exists in the reference product | Notes |
|---|---|---|
| **Tenant** | **No** | There is no tenant concept. Multi-tenancy is achieved by database separation, not by a model |
| **Company** | Yes — the accounting and legal entity | The only enforced boundary |
| **Site / Plant** | **No** | Not modelled |
| **Warehouse** | Yes | Stock only; not connected to assets or work centres |
| **Work centre** | Yes | Company **optional** |
| **Equipment** | Yes | Company **optional** |
| **Asset** | Yes | Company **required** |
| **GL company** | Yes — the company of the journal entry | |

**Two of the eight do not exist and must be built** if the design needs them: site/plant,
and any tenant concept above company. `19` §8 takes a position on both.

## 2. Record-level visibility rules, as verified from source

| Model | Visibility domain | Character |
|---|---|---|
| **Asset** | company is a **parent of** an allowed company | **Unusual — see §3** |
| Asset group | parent-of, same | Same |
| **Equipment** | company in allowed set **or empty** | **Permissive** |
| Maintenance request | company in allowed set **or empty** | Permissive |
| Maintenance team | company in allowed set **or empty** | Permissive |
| **Work centre** | company in allowed set **or empty** | **Permissive** |
| Bill of materials, operations | company in allowed set **or empty** | Permissive |
| **Work order** | company in allowed set | **Strict** |
| **Time log** | company in allowed set | **Strict** |

## 3. The asset rule deserves attention

The asset visibility rule is not the ordinary "company in the allowed set". It grants
sight of assets whose company is a **parent of** an allowed company.

Read plainly: **a user active only in a subsidiary can see the parent company's assets.**
The direction is upward, which is the opposite of the usual containment intuition and is
easy to misread as a typo when reviewing a security file quickly.

For a group structure this may be intentional. **For a SaaS deployment where companies
are unrelated customers sharing one database, it is a cross-customer disclosure.** It
does not permit *writing*, and it does not by itself move cost — but it is a
confidentiality exposure and it is the kind of default that survives into production
because nobody reads the rule.

**Ruling:** SMEsPlus scopes assets strictly to the owning company, with no parent
traversal. Group visibility, if ever needed, is an explicit grant, not a default.

## 4. The leakage vectors

### `LK-01` — Company-less equipment — **the primary vector**

Equipment's company is **optional**, and the rule explicitly admits an empty company.
An equipment record with no company is visible to, and usable by, **every** company.

The chain that makes it a costing problem:

1. Company A's asset (company mandatory) links to a company-less machine.
2. Company B's asset links to the **same** machine — nothing prevents it (`BLK-02`).
3. Company B's work centre references the same machine.
4. The machine's cost pool now contains depreciation from **two legal entities**.
5. Company B's products absorb part of company A's depreciation.

Steps 1–3 are `FACT VERIFIED` as *possible*. Steps 4–5 are the consequence for the
proposed design, and are `SOURCE-SUPPORTED INTERPRETATION` — they describe what would
happen if a machine-grain cost pool were built on this foundation without a company
constraint.

**This is the strongest single reason `BLK-02` must be closed before the costing design
is built, and the reason a uniqueness constraint alone is insufficient — it must be
uniqueness *and* company alignment.**

### `LK-02` — Company-less work centres

Same shape. A work centre with no company is visible to every company, and operations
on it are visible too. Work orders and time logs are strictly scoped, so *execution*
data does not leak — but *configuration*, including **the hourly rate**, does. Under the
proposed design the rate is derived from a company's depreciation, so a shared work
centre with a derived rate is a direct leak.

### `LK-03` — The parent-traversal asset rule

§3. Read leakage, upward.

### `LK-04` — Shared physical equipment between related companies

A real business case: one machine, legally owned by one company, used by another under
an intercompany arrangement.

**The reference product supports it by accident**, through `LK-01` — leaving the machine
company-less. That is the wrong mechanism: it achieves sharing by abolishing ownership.

**Correct treatment — DESIGN CANDIDATE:** ownership and use are **separate facts**.

| Fact | Owner |
|---|---|
| Legal and accounting ownership | The asset's company. Singular, mandatory, never empty |
| Operational use | A **dated usage-rights record**: machine, using company, period, basis of charge |
| Cost consequence | The using company's production absorbs a charge; the owning company recognises corresponding intercompany income. **Two entities, two ledgers, an intercompany transaction — not a shared pool** |

This keeps the accounting truth intact and makes the sharing explicit and auditable
rather than a side-effect of an empty field. It is also the only treatment that survives
a tax authority asking why one company's products carry another company's depreciation.

## 5. Required controls for SMEsPlus

| # | Control | Rationale |
|---|---|---|
| 1 | **Every** costing-relevant record has a mandatory, non-empty company | Closes `LK-01` and `LK-02` at the root |
| 2 | Asset → machine link constrained to the **same company**, and unique | Closes `BLK-02` and the cross-company half of `LK-01` |
| 3 | Machine → work centre constrained to the same company | Closes `LK-02` |
| 4 | Asset visibility scoped strictly, **no parent traversal** | Closes `LK-03` |
| 5 | Cross-company machine use expressed as a **dated usage-rights record with an intercompany charge** | Replaces `LK-04`'s accidental mechanism |
| 6 | Normal capacity, rates and cost pools are all company-scoped | The rate derives from one company's depreciation and must not be visible to, or usable by, another |
| 7 | Tenant isolation is **not** modelled as a company field | See §6 |
| 8 | Every cross-company posting is an explicit intercompany transaction | No implicit cost transfer anywhere |

## 6. Tenant versus company — the distinction that must not be collapsed

The reference product has no tenant concept, so there is a standing temptation to make
"company" carry both meanings. It must not.

| | Tenant | Company |
|---|---|---|
| Means | A customer of the SaaS | A legal entity |
| Cardinality | One tenant has one or many companies | |
| Isolation required | **Absolute.** No record, no report, no aggregate, ever crosses | **Relative.** Intercompany transactions are legitimate and expected |
| Correct mechanism | Enforced **above** the application — separate database or an enforced tenant predicate that no query can omit | Record rules and check-company constraints inside the application |

**Collapsing them means implementing absolute isolation with a mechanism designed for
relative isolation.** Every vector in §4 is an example of what that produces: rules that
are correct for a group of related companies and wrong for unrelated customers. The
company-or-empty pattern is convenient in a group and is a disclosure in a SaaS.

**Ruling:** tenant isolation is a deployment-architecture property, not a field. No
tenant-crossing query may be *expressible*, rather than merely being refused.

## 7. Site and plant

Not modelled at all. Where a company operates several plants, the design needs a level
between company and work centre for:

- normal capacity, which is a plant-level fact as much as a machine-level one,
- statutory reporting where a plant is a separate registered establishment,
- and equipment transfers between sites, which `15` `EC-07` shows are today a single
  untraced field write.

**Candidate:** a site/plant entity, mandatory on the work centre, company-scoped. Not
blocking; deferrable, but cheaper to introduce before the costing model than after.
