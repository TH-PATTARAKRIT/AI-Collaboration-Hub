# G02 — SB-05 TARGETED CLOSURE — CROSS-TENANT FX RATE INTEGRITY

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · Layer 2 / audit quarantine
Prior classification: `PARTIALLY VERIFIED` · **Tolerance = 0 applies (tenant isolation)**

---

## 1. The question

Can an exchange rate with null or insufficient company scoping affect a posting belonging to another
tenant or company?

## 2. Evidence

### 2.1 Rate ownership and its default

`base/models/res_currency.py:365-366` — the rate carries
`company_id = fields.Many2one('res.company', default=lambda self: self.env.company.root_id)`.
The field is **nullable**, and its default is the acting company's **root**, not null.

### 2.2 Lookup and filter logic

`base/models/res_currency.py:128-131` — `_get_rates` filters
`('company_id', 'in', (False, company.root_id.id))`.

> **`VERIFIED FACT`:** a rate row whose company is null is matched for **every company in the
> database**, without exception.

### 2.3 Record-level security — the decisive control

`base/security/base_security.xml:62-66` — record rule `res_currency_rate_rule`:

```
['|', ('company_id', 'parent_of', company_ids), ('company_id', '=', False)]
```

> **`VERIFIED FACT`:** the rule **explicitly permits** `company_id = False` rows for every user.
> Record-level security therefore does **not** scope null-company rates. This is a deliberate
> "global reference data plus company override" design, not an oversight.

`_get_rates` uses `_search` (`:128`, `:133`) and does **not** elevate privilege, so record rules do
apply — but the rule permits the global rows, so they are returned.

### 2.4 Priority and matching order

`base/models/res_currency.py:131` — `order='company_id.id, name DESC'`, ascending on company with
**no explicit nulls clause**. `models.py:2234-2244` shows Odoo emits `NULLS FIRST`/`NULLS LAST` only
when the order string states it. PostgreSQL's default for `ASC` is `NULLS LAST`.

> **`VERIFIED FACT` (SQL generation) / `INFERENCE` (resulting precedence):** a company-specific rate
> sorts before a null-company rate, so **a company's own rate takes precedence**. A null-company rate
> applies only where the company has no rate of its own for that currency on or before the date.

### 2.5 Write access control

`base/security/ir.model.access.csv:60-64` — public, portal and internal-user groups are
**read-only** (`1,0,0,0`). Only `group_system` holds create, write and unlink (`1,1,1,1`).

> **`VERIFIED FACT`:** only a system administrator can create any rate row, including a null-company
> one, and doing so requires deliberately clearing a field that defaults to the acting company's root.

### 2.6 Database-level boundary

`base/models/res_currency.py:368-371` — `unique (name, currency_id, company_id)`.

> **`VERIFIED FACT`:** there is **no** database-level company or tenant boundary on rate
> *consumption* — the constraint governs uniqueness only.
> **`INFERENCE` (standard PostgreSQL `NULLS DISTINCT` semantics, not separately tested here):** because
> NULLs compare as distinct, the constraint does **not** prevent multiple null-company rows for the
> same currency and date.

### 2.7 Effect on already-posted transactions

`account_move_line.py:113-147` — `balance` and `amount_currency` are **stored**.

> **`VERIFIED FACT`:** an existing posted entry is **not** re-measured by a later rate. Its amounts
> are frozen. Re-measurement affects **future postings** and **report-time derivations** — including
> the consolidation currency table (`account/models/res_currency.py:105-160`), which resolves through
> the same path.

### 2.8 Cached or shared state

`_get_rates` executes a query per call; `_compute_current_rate` is non-stored and context-dependent
(`:148-158`). No cross-request rate cache was found in `base/models/res_currency.py` or
`account/models/res_currency.py`.
Classification: **`B — NOT FOUND IN SEARCHED SCOPE`**. ORM-level and deployment-level caching were
not examined — `C — NOT YET SEARCHED`.

## 3. What is and is not possible

| Scenario | Possible? | Basis |
|---|---|---|
| A null-company rate is used to measure Company B's **new** postings | **Yes** | §2.2, §2.3 |
| …even when Company B belongs to a different tenant sharing the database | **Yes** | §2.2 — the filter has no tenant dimension, and none exists (`NC-06`) |
| A null-company rate **overrides** a company's own rate | **No** | §2.4 — company-specific takes precedence |
| Company B's **already-posted** entries are re-measured | **No** | §2.7 — amounts are stored |
| Company B's **historical reporting** shifts | **Yes** | §2.7 — report-time derivation re-resolves |
| An ordinary user creates a cross-tenant rate | **No** | §2.5 — system administrator only |
| A database constraint prevents any of this | **No** | §2.6 |
| Application-level filtering is sufficient | **No** | §2.3 — the rule permits the global row by design |

## 4. Disposition

> ## `VERIFIED DEFECT` — scoped

**The defect, stated at exactly the supported scope:**

> In the reference implementation, an exchange rate may be created with a null company. Such a rate
> is matched by the rate resolver for **every company in the database**, is **explicitly permitted**
> by the record rule, and is bounded by **no database-level company or tenant constraint**. A company
> — including one belonging to a different tenant in a shared database — that has no rate of its own
> for a currency on a given date will therefore be measured using a rate it did not create, cannot
> distinguish from its own, and has no provenance for.

**It is not** an arbitrary-user cross-tenant write, and it does **not** re-measure posted history or
override a company's own rates. Those three limits are load-bearing and are stated as firmly as the
defect.

### Why this is still a `Tolerance = 0` matter

Three properties, each verified:

1. **No boundary exists at the database level** — the isolation depends entirely on nobody creating
   a null-company row.
2. **The record rule permits the crossing by design** — this is not a gap that can be closed by
   configuration; it is the intended behaviour of the reference model.
3. **The crossing is undetectable from within the consuming company** — a null-company rate is
   indistinguishable, at the point of use, from the company's own.

For a single-tenant deployment this design is defensible and arguably convenient. **For a
multi-tenant SaaS sharing a database it is a tenant-isolation failure**, and the reference model was
not built for that deployment.

### Interaction with `SF-01`

A null-company rate **prevents** the par-conversion bug for other tenants — by substituting a
measurement they never agreed to. Both outcomes are wrong; this one is merely less visible.

## 5. SMEsPlus position

**`REJECT` the global-scope rate row.** Every measurement must carry an owning boundary, and rate
resolution must never match across it. Where shared reference rates are genuinely wanted, they must
be **explicitly adopted** by a tenant, creating a tenant-scoped row with recorded provenance, rather
than silently inherited.

Reinforces `TI-01`, `TI-06` and proposed `Tolerance = 0` candidate `T0-04`.

## 6. Residual

| # | Item | Class |
|---|---|---|
| `SB05-R1` | Whether ORM or deployment caching shares resolved rates across company contexts | `C — NOT YET SEARCHED` |
| `SB05-R2` | Runtime confirmation of `NULLS LAST` precedence on the target database | `INFERENCE` — recommended cheap test |
| `SB05-R3` | Whether any shipped or localization data creates null-company rate rows | `C — NOT YET SEARCHED`; shipped currency master data contains no rate rows at all |

---

# ADDENDUM B1 — CORRECTIONS FROM THE FINAL INDEPENDENT GATE REVIEW

Raised by Final Gate Reviewer 1. **Both re-verified against primary source by the research team.**
Body retained unedited; **this addendum governs.**

## B1-01 — §2.5 is CONTRADICTED. An accounting manager can create rates, not only a system administrator.

**Verification: `CONTRADICTED` — the research team's claim was wrong.**

§2.5 asserted, as a `VERIFIED FACT`, that "only a system administrator can create any rate row". It
cited `base/security/ir.model.access.csv:60-64` — the framework's access rows — and **did not search
the accounting module's own access file**.

`account/security/ir.model.access.csv:7`:
```
access_res_currency_rate_account_manager,res.currency.rate account manager,
base.model_res_currency_rate,group_account_manager,1,1,1,1
```

> **`VERIFIED FACT`:** the **accounting-manager** group holds full read, write, create and unlink on
> the currency-rate model.

`base/views/res_currency_views.xml:20,44,169` — `company_id` is rendered as an editable field for the
multi-company group on the rate list, the rate form and the embedded rate view.

> **`VERIFIED FACT`:** the company on a rate is user-editable, so it can be cleared to null through
> the ordinary interface.

### Consequence — SB-05 is materially worse

| | §2.5 as written | Corrected |
|---|---|---|
| Who can create a null-company rate | a system administrator | **any accounting manager**, a routine business role |
| Nature of the act | a deliberate administrative action | **an ordinary configuration action in a normal business role** |
| Mitigation strength | strong | **weak** |

The corrected mitigation set for SB-05 is therefore only two items, not three: the **root-company
default** on creation, and **company-specific precedence** in resolution. The access-control
mitigation is withdrawn.

**This is exactly the failure mode this programme keeps repeating**: a claim asserted at wide scope
(`only a system administrator can…`) from a **narrow search** (one of two access files), and this
time it was a *limiting* statement on the `Tolerance = 0` blocker — understating who can cause the
crossing. Recorded as `NC-25`.

## B1-02 — §2.7 is CONTRADICTED on the consolidation path. A fourth, raw-SQL resolution rule exists.

**Verification: `CONTRADICTED`.**

§2.7 stated that report-time derivation "resolves through the same path". It cited the currency-table
builder but did not read it.

`account/models/res_currency.py` — the currency-table builders execute **raw SQL** via
`self._cr.execute(SQL(...))`, joining the rate table directly:
```
LEFT JOIN res_currency_rate rate
    ON rate.currency_id = other_company.currency_id
    AND rate.name <= %(date_to)s
    AND rate.company_id = %(main_company_id)s
...
CASE WHEN rate.id IS NOT NULL THEN %(main_company_unit_factor)s / rate.rate ELSE 1 END
```
with `main_company_id = main_company.root_id.id`.

Three `VERIFIED FACT`s follow:

1. **It is raw SQL, so no record rule runs.** The record-rule analysis in §2.3 does not apply to this
   path at all.
2. **`rate.company_id = <main root>` excludes null-company rows** — SQL equality never matches NULL.
   So this path has the **opposite** null behaviour to `_get_rates`.
3. **It defaults to `1`** when no rate matches (`ELSE 1`), a **fourth** par fallback, in a different
   code path from the three already recorded.

Additionally it resolves **another company's** currency using a rate owned by the **main company's
root** — a deliberate consolidation semantic, but a fourth distinct scoping rule.

### Consequence

There are now **four different company-scoping rules over one rate table**:

| Path | Scoping rule | Null rows | Record rules |
|---|---|---|---|
| `_get_rates` | `company_id IN (NULL, root)` | **included** | apply |
| `_get_last_rates_for_companies` | `company_id == company` or null | included | apply |
| live-rate writer | writes `company_id = acting company` | n/a | apply |
| **currency table (consolidation)** | `rate.company_id = main root` | **excluded** | **bypassed** |

> **This is the single most important structural result of the gap-closure round.** Both verified
> boundary crossings, the branch-rate failure, and this consolidation path all reduce to one cause:
> **the same fact is scoped differently by different code paths, and one of them bypasses the
> security layer entirely.**

Reinforces `TI-07`. Recorded as `SB-08`.

## B1-03 — Two residuals closed by the reviewer

| Residual | Prior | Closed as |
|---|---|---|
| `FX08-R1` (does the UI prevent branch-level rate maintenance?) | `C — NOT YET SEARCHED` | **Closed** — the scheduled job is root-scoped; the **manual button is not**. So the branch-scoped write is reachable through the ordinary interface |
| `B05-R3` (is the elevation bypass reachable in normal operation?) | `C — NOT YET SEARCHED` | **Closed** — reachable through the online-payment post-processing path, which is exactly the flow the bypass comment names |

Both were left `NOT YET SEARCHED` by the research team and yielded findings on first search.
`INFERENCE:` a residual that is cheap to close should be closed before a gate, not carried to it.

## Addendum summary

| # | Effect | Verification |
|---|---|---|
| `B1-01` | Actor widened from system administrator to **accounting manager**; a mitigation withdrawn; **SB-05 worse** | `CONTRADICTED` — confirmed |
| `B1-02` | A **fourth** scoping rule exists, in raw SQL, bypassing record rules, with its own par default | `CONTRADICTED` — confirmed |
| `B1-03` | Two residuals closed, both adversely | confirmed |

**Disposition of SB-05 is unchanged — `VERIFIED DEFECT` — and its severity is raised.** The defect is
reachable by a routine business role, and the boundary is inconsistent across four code paths, one of
which bypasses record-level security.
