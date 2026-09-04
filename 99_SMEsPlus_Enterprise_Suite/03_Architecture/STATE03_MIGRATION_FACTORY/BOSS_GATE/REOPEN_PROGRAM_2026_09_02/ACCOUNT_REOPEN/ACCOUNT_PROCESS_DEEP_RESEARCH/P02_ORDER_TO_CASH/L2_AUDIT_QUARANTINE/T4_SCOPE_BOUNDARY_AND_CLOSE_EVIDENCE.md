# T4 EVIDENCE EXTRACT — COMPANY BOUNDARY, INTERCOMPANY, AND PERIOD CLOSE

`LAYER 2 — AUDIT QUARANTINE` · Parallel research track T4 · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`
Reference root `R = /Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons`, plus the ORM core.

> **SCOPE NOTE, added by the primary session after correction `SMEPLUS-26-09-04-ACC-REV2-CORR1`.**
> This track was commissioned before the three-scope model (PLATFORM / TENANT / COMPANY) was issued.
> Its **evidence** is scope-neutral and stands unchanged. Its §9 gap analysis is re-expressed against
> the three-scope model in deliverable `20_P02_SCOPE_OWNERSHIP_MATRIX.md`; nothing here asserts that
> tenant and company context are required for every operation.

## §0 DENOMINATOR

**POPULATION** — 9,431 `.py` files under `R`, plus the ORM core module.
**UNIT** — one source line, addressed `path:line`. All counts are counts of lines matching a declared
pattern, never author-chosen lists.

| Path set | Members | count |
|---|---|---|
| **PS-O2C** | the 13 chain model files (order, order line, picking, movement, movement line, quant, valuation layer, valuation movement, accounting document ×3, accounting line) | 13 |
| **PS-MOD** | whole modules: sales 64, sales-inventory 36, inventory 84, inventory-accounting 31, accounting 141, intercompany rules 10, sales-purchase intercompany 12, reporting 77 | 455 |
| **PS-ALL** | every `*.py` / `*.xml` under `R` | 9,431 `.py` |

**PATTERNS** — `company_id`, `check_company=True`, `_check_company_auto`, `_check_company()`,
`_check_company_domain`, `\.sudo\(`, `lock_date`, `bypass_lock_check|BYPASS_LOCK_CHECK`,
`force_period_date`, `unaffected_earnings`, `fiscalyear_last_day`, `_find_company_from_partner`,
`with_company|with_user`.

**SCOPE CAVEAT CARRIED INTO EVERY SECTION** — the reference has **no tenant entity**. The
case-insensitive pattern `tenant` over the five core modules returns **zero files**. Everything below
describes a **company** boundary only.

## §1 Company propagation along the O2C chain

| Hop | Storage | Evidence |
|---|---|---|
| Order | stored, required, defaulted from the environment company; no compute, no relation | `R/sale/models/sale_order.py:76-79` |
| Order line | related to the order, stored, precomputed | `R/sale/models/sale_order_line.py:45-47` |
| Movement (created from the order) | **not** taken from the order — set by the **routing rule**, with the order's company only as a last fallback | `R/stock/models/stock_rule.py:352` |
| Movement (model default) | stored, required, defaulted from the environment company | `R/stock/models/stock_move.py:41-44` |
| Picking | stored, required, defaulted from the environment company | `R/stock/models/stock_picking.py:127-129` |
| Movement line | stored, required, **no default, no compute, no relation** | `R/stock/models/stock_move_line.py:27` |
| Quant | related to the location, stored | `R/stock/models/stock_quant.py:57` |
| Valuation layer | stored, required, **no default, no compute, no relation** | `R/stock_account/models/stock_valuation_layer.py:23` |
| Accounting document | stored, **computed from the journal**, with an inverse, writable | `R/account/models/account_move.py:193-198`, derivation `:831-834` |
| Accounting line | related to the document, stored, read-only | `R/account/models/account_move_line.py:56-58` |

**`FACT VERIFIED` — the chain is NOT a single inherited value.** It breaks into **four independently
sourced segments**: (a) order and order line from the environment company at creation; (b) the movement
from the **routing rule's** company; (c) valuation layer and movement line from whatever the creating
code passes; (d) the accounting document from the **journal's** company.

**`FACT VERIFIED`** — the movement created from a procurement is created **as superuser** under an
explicit company context — `R/stock/models/stock_rule.py:298`.

**`FACT VERIFIED`** — the valuation journal entry's company is **always the movement's own company**,
never the source or destination company — `R/stock_account/models/stock_move.py:686`. See §5.

**`FACT VERIFIED`** — the valuation layer's company on manual cost-change entries is taken from the
**environment**, not from the record — `R/stock_account/models/product.py:297`, `:317`;
`R/stock_account/models/stock_valuation_layer.py:234`, `:265`.

### Writability after confirmation

- The order's write guard blocks only the price list on a confirmed order; **the company is not
  guarded** — `R/sale/models/sale_order.py:1004-1006`. — `FACT VERIFIED`
- The order form exposes the company field with **no read-only attribute**, in contrast to its
  neighbours which carry a state-based read-only — `R/sale/views/sale_order_views.xml:764`, neighbours
  `:765-770`. — `FACT VERIFIED`
- **A multi-company user can therefore rewrite a confirmed order's company through the standard form.**
  The only barriers are the automatic consistency sweep and a product constraint; **neither
  re-companies the already-created pickings or invoices.** — `SUPPORTED INTERPRETATION`
- The unmodifiable-field set for a posted accounting document does **not** include the company —
  `R/account/models/account_move.py:3245-3248`; journal changes after posting **are** blocked
  (`:3215-3227`). A company rewrite on a posted document is stopped only by a **consistency check**
  firing on the journal/account fields, not by a period or state rule. — `FACT VERIFIED` / `SUPPORTED INTERPRETATION`
- The movement and movement-line company fields have **no write guard tied to completion**; the only
  company validation is two explicit checks at confirm and at done —
  `R/stock/models/stock_move.py:1546`, `:2038`. — `FACT VERIFIED`

## §2 Company-consistency constraints

**DENOMINATOR** — PATTERN `check_company=True` and `_check_company_auto` over PS-O2C. UNIT: one field
declaration line.

| File | fields flagged | auto-validation on? |
|---|---|---|
| order | 8 | **yes** (`:54`) |
| order line | 2 | **yes** (`:22`) |
| sales-inventory order | 1 | no |
| sales-inventory order line | 0 | no |
| picking | 11 | **yes** (`:24`) |
| movement | 11 | **no** |
| movement line | 10 | **no** |
| quant | 4 | **no** |
| valuation layer | 6 | **no** |
| inventory-accounting movement | 0 | n/a |
| inventory-accounting document | 0 | n/a |
| accounting document | 11 | **yes** (`:92`) |
| accounting line | 7 | **yes** (`:25`) |
| **TOTAL** | **71** | 5 of 13 |

- **The flag is inert unless the model opts in.** Auto-validation is off by class default and the check
  runs only under that opt-in, on write and on create (ORM core). — `FACT VERIFIED`
- **31 of the 71 flagged fields sit on models that never auto-validate them** — the movement, the
  movement line, the quant and the valuation layer. **This is the entire physical-and-valuation half of
  the O2C chain.** — `FACT VERIFIED`
- The compensating manual calls are **exactly 8 non-definition call sites** across the inventory,
  inventory-accounting, sales and accounting modules. They are **event-time** checks (confirm, done,
  apply-inventory), not transition checks: a write to a movement's destination location or company
  **between** confirm and done is re-validated by none of them. — `FACT VERIFIED` / `SUPPORTED INTERPRETATION`
- **The check is not equality.** The default domain admits **company-less** records, and the branch
  variant admits every **parent** company. — `FACT VERIFIED`
- **The chart of accounts is many-to-many to companies in this version** — one account row is
  legitimately shared by several companies — `R/account/models/account_account.py:106-107`, `:25`. — `FACT VERIFIED`
- **Specific gap on the delivery vector:** on the movement, the **source** location and the **final**
  location carry the consistency flag; **the destination location does not** —
  `R/stock/models/stock_move.py:82`, `:92`, versus `:83-86`. — `FACT VERIFIED`
- **Company-dependent valuation configuration is resolved from the environment, not the record.** The
  valuation mode, costing method, stock journal and the three stock accounts are all company-dependent
  properties on the product category; for such fields the consistency check validates against the
  **environment** company, not the record's. — `FACT VERIFIED`

## §3 Cross-company leakage surfaces

**DENOMINATOR** — PATTERN `\.sudo\(` over `*.py`, tests excluded:
inventory-accounting **43**, sales **37**, sales-inventory **8**.

**Class A — privilege elevation with no company argument, company supplied by the values dictionary.**
Valuation-layer creation and journal-entry creation, 12 sites. These cannot *read* across companies but
they *write* whatever company the caller computed, with the record rule bypassed. Correctness rests
entirely on the caller. — `FACT VERIFIED` / `SUPPORTED INTERPRETATION`

**Class B — elevation paired with an explicit company context (bounded).** 8 sites. — `FACT VERIFIED`

**Class C — elevated *read* through a relation, unbounded by company but bounded by the traversal.**
7 sites including `R/stock_account/models/stock_move.py:50-51` and five in
`R/stock_account/models/account_move.py`. These can surface layers and accounting lines the acting
user's companies exclude, **whenever the traversed relation itself crosses a company** — which §5 shows
is reachable via the shared transit location. — `FACT VERIFIED` / `SUPPORTED INTERPRETATION`

**Class D — elevated search with an explicit company clause (bounded).** 1 site. — `FACT VERIFIED`

**Class E — elevated search with NO company clause.** `R/stock_account/models/res_config_settings.py:21`
— a settings sweep across the whole database on a model that has no company at all. — `FACT VERIFIED`

**Two sales-module elevated searches whose domain contains no company term:**
`R/sale/models/res_partner.py:48-56` (order existence) and `:109-115` — **partner deletion removes that
partner's draft and cancelled orders in every company.** — `FACT VERIFIED`

**A cross-company reporting leak.** `R/sale_stock/report/stock_forecasted.py:36` searches order lines
as superuser with a domain built at `:48-57` from state plus *optional* product and *optional*
warehouse terms — **no company term** — and the result feeds draft-order quantities and **order names**
into the forecast panel (`:44-45`). **The forecast report discloses draft and sent order counts,
quantities and order names from companies the viewer is not in, whenever no warehouse filter is in
context.** — `FACT VERIFIED` / `SUPPORTED INTERPRETATION`

### The valuation elevation at movement completion

- The layer recordset is elevated at `R/stock_account/models/stock_move.py:363`; entries are validated
  and posted at `:371`; **the company check runs at `:378`, seven lines later.** — `FACT VERIFIED`
- **The company consistency of the layer set is therefore verified AFTER its journal entries are already
  posted.** If the check raises, the posted entries are unwound only by transaction rollback; there is
  no compensating unpost path. **The guard is a transaction abort, not a pre-condition.** — `SUPPORTED INTERPRETATION`
- The cross-company **sanity check** *is* called before layer creation, at `:369`, and is the real gate
  (§5). — `FACT VERIFIED`

### The interim-account matching routine

- **It performs no search at all** — it works entirely by relation traversal and filtering
  (`R/stock_account/models/account_move.py:182-247`, `:194`, `:218`, `:219`). **No filter in the method
  tests the company.** — `FACT VERIFIED`
- Its only company scoping is a per-document split-recognition guard at `:192-193`. — `FACT VERIFIED`
- **The interim account is resolved without a company context** — `:207` — in direct contrast to the
  sibling cost-of-sales builder in the same file, which sets the company explicitly at `:109` before
  resolving accounts at `:123`. Because the stock account properties are company-dependent, **the
  interim account selected for matching is the one belonging to the environment company, which is not
  guaranteed to equal the document's company. Where they differ, the account matches no line and the
  matching silently does nothing.** — `FACT VERIFIED` / `SUPPORTED INTERPRETATION`
- **The terminal matching call does not require identical companies, only a shared root** —
  `R/account/models/account_move_line.py:2335-2339`. **Journal items of two different legal entities
  that share one root company are reconcilable with each other.** — `FACT VERIFIED`

## §4 Intercompany sale — receivable in A becomes payable in B

- The mirror fires from the **posting** override, on already-posted sale documents only —
  `R/account_inter_company_rules/models/account_move.py:14-15`. — `FACT VERIFIED`
- Company B is found by **partner lookup with no scoping term of any kind** — `:16`, lookup at
  `R/account_inter_company_rules/models/res_company.py:34`. **The whole company table is candidate.** — `FACT VERIFIED`
- Gated on B's own flag (`:17`); inverse document types are hard-coded (`:33-36`). — `FACT VERIFIED`
- **Acting identity:** the mirror runs as a configured user, **defaulting to the superuser** —
  `R/account_inter_company_rules/models/account_move.py:23`;
  `R/account_inter_company_rules/models/res_company.py:22-28`. — `FACT VERIFIED`
- The mirrored bill is posted only if B's document-state setting says so; **that setting defaults to
  draft** — `:67-68`; `R/account_inter_company_rules/models/res_company.py:8-15`. — `FACT VERIFIED`

**Same amount?**
- Quantity, unit price and discount are copied verbatim — `:121-123`. — `FACT VERIFIED`
- **Taxes are RE-COMPUTED under B's fiscal position, not copied** — `:47-49`, position resolved at
  `:82-84`. — `FACT VERIFIED`
- **There is therefore a guarantee on the untaxed amount and NONE on the total.** Where A's and B's
  fiscal positions map taxes differently the totals legitimately diverge, and **nothing in the module
  compares the two afterwards.** — `SUPPORTED INTERPRETATION`
- **The product may be dropped** from the mirrored line: a company-restricted product yields a
  text-only bill line — `:125-131`. — `FACT VERIFIED`

**Same date?**
- Only the **document** dates are copied; the **accounting date is not in the mirrored values** —
  `:93-94`, value set `:85-100`. — `FACT VERIFIED`
- The accounting date is then computed **asymmetrically by direction**: a sale document takes the
  document date unchanged; a purchase document runs its own lock-aware period resolution —
  `R/account/models/account_move.py:801-810`. — `FACT VERIFIED`
- **The two sides are not guaranteed to share an accounting date, and the divergence is silent.** Both
  are additionally subject to the posting-time reschedule of §6(b). — `SUPPORTED INTERPRETATION`

**Same currency rate?**
- The currency **identifier** is copied; **no rate is carried** — `:89`. — `FACT VERIFIED`
- Rates are stored per **root** company and a rate may only be created for a main company —
  `R/base/models/res_currency.py:365-366`, `:458-461`; resolution at `:129-141` ends in the
  `COALESCE(..., 1.0)` fallback. — `FACT VERIFIED`
- **Where A and B are separate root companies they read independent rate tables. Two different
  company-currency amounts for the same foreign-currency invoice are the expected outcome, and where B
  has no rate row the conversion silently uses 1.0. Neither module reconciles the difference.** — `SUPPORTED INTERPRETATION`

**Order → purchase-order direction**
- Same shape, fired from order confirmation, acting as the configured user under B's company —
  `R/sale_purchase_inter_company_rules/models/sale_order.py:12-22`, `:21`; auto-confirmation gated at
  `:58-59`. — `FACT VERIFIED`
- **Asymmetric currency validation:** the reverse direction **raises** when the price-list currencies
  differ (`R/sale_purchase_inter_company_rules/models/purchase_order.py:46-57`); **the forward direction
  has no equivalent check.** — `FACT VERIFIED`
- **`CONTRADICTED`** — the in-code comment at
  `R/sale_purchase_inter_company_rules/models/sale_order.py:94` claiming the mirrored price is net of
  discount is contradicted by the code beneath it (`:95`, `:103`, `:104`): price and discount are
  carried as two separate fields and the discount is not netted in.
- A unit-of-measure re-expression happens on the mirrored line — `:96-97`. — `FACT VERIFIED`

## §5 Inter-company and inter-warehouse stock

**The sanity check** — `R/stock_account/models/stock_move.py:385-401` — three refusals, all raising, all
evaluated **per movement** and derived from the **locations of the movement lines**, not from the
movement's company:

1. a movement that is simultaneously inbound and outbound (`:388-389`);
2. movement lines whose source or destination companies are not singular (`:390-399`);
3. **source company ≠ destination company** → *"they are doing an intercompany in a single step while
   they should go through the intercompany transit location"* (`:400-401`).

**`FACT VERIFIED` — answer to "what happens when source and destination belong to different companies":
the delivery is REFUSED at validation.** A single-step A→B transfer is impossible for a real-time-valued
product; the flow must be split into two movements through a transit location.

**`SUPPORTED INTERPRETATION`** — the check is scoped to **valued** movements only. It is called from one
site inside the per-valuation-type loop. A non-storable product returns early from the entry builder,
and a manual-valuation product produces no layer, so **neither reaches this gate.**

### The transit location it points at

- **The inter-company transit location is a single, company-less, database-global record** —
  `R/stock/data/stock_data.xml:54-60`. The customer and supplier locations are likewise company-less
  (`:41-52`). — `FACT VERIFIED`
- **Creating any company rewires stock routing on every other company in the database** — **qualified by
  the primary session on re-derivation: the rewiring routine returns early unless the acting user holds
  the multi-company group (`R/stock/models/res_company.py:203-204`). The unarchive of the shared location
  is unconditional; the rewiring is gated.** See `12_P02_CONTRADICTION_REGISTER.md` C-11. — a superuser
  search over all other companies writes the shared transit location onto each of their partner records
  as the customer and supplier stock location, and unarchives the shared location database-wide —
  `R/stock/models/res_company.py:201-215`, invoked at `:195`, unarchive at `:187-189`. — `FACT VERIFIED`
- **This is the single most scope-hostile construct found. In one database it makes every company a
  stock counterparty of every other company by configuration default, and it runs as superuser so no
  record rule constrains the enumeration.** — `SUPPORTED INTERPRETATION`
- The *internal* (same-company, inter-warehouse) transit location is per-company and **deliberately
  non-valuing**, with an in-code comment saying so — `R/stock/models/res_company.py:47-62`, field at
  `:19-20`. — `FACT VERIFIED`

### Which company's accounts are used

- Source and destination companies are derived from the movement-line locations —
  `R/stock_account/models/stock_move.py:722-723`. — `FACT VERIFIED`
- **The accounts are resolved BEFORE either is applied, and under the movement's own company** — `:725`,
  and the resolver opens by setting the movement's own company at `:480`. — `FACT VERIFIED`
- **The journal entry's company is the movement's own company**, not either endpoint — `:686`. — `FACT VERIFIED`
- The endpoint company contexts at `:729`, `:731`, `:736`, `:738` therefore influence **only** what the
  value-preparation reads from the environment — the date branch (`:669-675`) and the partner resolution
  (`:667`) — **not the journal, not the accounts, and not the document's company.** — `FACT VERIFIED`
- **Answer: always the movement's own company's accounts**, resolved through company-dependent category
  properties. In the two-step transit flow this is correct by construction; **it means there is no code
  path in which the destination company's accounts are consulted.** — `SUPPORTED INTERPRETATION`
- The split-recognition dropship entry pins the company explicitly to the movement's own — `:755`, `:758`. — `FACT VERIFIED`

## §6 Period close

**DENOMINATOR** — POPULATION: every file in PS-ALL declaring an inheritance of the company model.
PATTERN: `lock_date.*= fields\.`. UNIT: one field declaration.
**Result: one file; ten declarations; no other addon in the tree extends the lock-date set.**

**Five stored dates** — global, tax-return, sale, purchase, and **hard** —
`R/account/models/company.py:73-98`. **Five computed effective mirrors**, one per stored date (`:105-109`).
The partition into soft and hard is a module constant (`:53-64`).

- **Every lock is inherited down the company tree** — `:540-563`, hard lock at `:396-402`. A parent
  company's lock binds its branches. — `FACT VERIFIED`
- **Journal-type selectivity** — the effective fiscal lock is the greater of the global and hard locks,
  then folded with the sale lock for sale journals and the purchase lock for purchase journals (`:565-577`). — `FACT VERIFIED`
- **The comparison is inclusive** (`:594`, `:629`). — `FACT VERIFIED`

### (a) What a lock date actually BLOCKS

**DENOMINATOR** — PATTERN for the two check methods over PS-ALL excluding tests: **exactly two
definitions and nine call sites.**

**`FACT VERIFIED` — every one of those guards is conditioned on the document already being posted**
(`R/account/models/account_move.py:3230-3236`, `:3238-3241`, `:3280-3283`;
`R/account/models/account_move_line.py:1275-1276`, `:1703`).

**`FACT VERIFIED` — document creation performs no lock check whatsoever** —
`R/account/models/account_move.py:3181-3199`; its only refusal is against creating a document already in
the posted state (`:3182-3183`).

**`SUPPORTED INTERPRETATION`** — a lock date blocks: (i) changing the name or date of an already-posted
document; (ii) un-posting one; (iii) writing a date into the locked period on a document that is or
becomes posted; (iv) tax-affecting line edits on a posted document. **It does not block creating a draft
entry dated inside the locked period.**

**`FACT VERIFIED`** — the tax lock is narrower still: it raises only for lines that actually affect the
tax report, and queries with only the tax and hard locks enabled
(`R/account/models/account_move_line.py:1286`, `:1278-1285`).

**`FACT VERIFIED`** — the hard lock has two extra set-time pre-conditions, both raising: it cannot be
removed or decreased (`R/account/models/company.py:492-499`), and it refuses to engage while draft
entries exist in the period (`:501-517`).

### (b) What a lock date SILENTLY RESCHEDULES instead of blocking — the load-bearing finding

**`FACT VERIFIED`** — posting silently moves the date rather than refusing —
`R/account/models/account_move.py:4932-4936`. **No exception is raised on this path.** The subsequent
state write then re-enters the check, which now passes because the date has already been moved.

**`FACT VERIFIED`** — the reschedule target is the day after the last violated lock, snapped to a period
end by the journal's sequence-reset shape, capped at today for sale documents — `:5673-5690`.

**`FACT VERIFIED` — the same silent shift on three further paths:** document duplication (`:3127-3129`),
cash-basis tax entries (`R/account/models/account_partial_reconcile.py:512-514`), and the computed
accounting date on purchase documents (`R/account/models/account_move.py:808-810`).

**`FACT VERIFIED`** — the user is warned, not stopped (`:5713-5717`, surfaced at `:676`, `:1681-1685`).

**`SUPPORTED INTERPRETATION` — the reference's lock date is NOT a period-close bar; it is a
period-REDIRECT.** Postings dated into a closed period land in a later open period with a changed
accounting date and no error. Only the four transitions in (a) actually refuse.

### (c) Who can override

**Mechanism 1 — a lock exception record.** Dated, optionally user-scoped, optionally expiring —
`R/account/models/account_lock_exception.py:12-70`, consulted at `R/account/models/company.py:545-556`.
**An exception without a user applies to everyone, and one without an end date is permanent** — the
in-code comments say so at `R/account/models/account_lock_exception.py:37`, `:46`. — `FACT VERIFIED`
Create is granted to the accounting-manager group (`R/account/security/ir.model.access.csv:18-19`);
revocation requires the same group (`R/account/models/account_lock_exception.py:260-261`). — `FACT VERIFIED`
**Exceptions cannot reach the hard lock** — it is absent from the soft set and from the exception's field
selection, and the hard-lock mirror takes no exception argument. — `FACT VERIFIED`

**Mechanism 2 — a context sentinel that skips the check entirely.**
`R/account/models/account_move.py:83` and `:2378-2379` (first statement of the check).
**DENOMINATOR for the sentinel:** PATTERN over PS-ALL — **5 lines, 3 files, exactly 2 use sites**, both
in **partner merge** — `R/account/models/partner.py:804-805`. — `FACT VERIFIED`
**`SUPPORTED INTERPRETATION` — a contacts-role operation rewrites fields on posted journal items inside a
period protected by EVERY lock date including the hard lock, with the check disabled by construction
rather than by permission.**

**Mechanism 3 — writing the lock date itself.** Company write validation raises only on hard-lock
removal or decrease and on unreconciled statement lines / draft entries
(`R/account/models/company.py:663-665`, `:474-528`). **Soft lock dates can be moved backwards freely.**
On any soft-lock change, active exceptions on that field are revoked and re-created against the new
value (`:687-693`). — `FACT VERIFIED`

## §7 Year-end closing entry

**SCOPE OF FINDING** — patterns searched over PS-ALL (`*.py` + `*.xml`, excluding translations and
tests): `unaffected_earnings`, `fiscalyear_last_day`, case-insensitive `retained earning`,
`year_end_clos|yearly_clos|year_closing|closing_entry|_close_fiscalyear|fiscal_year_clos|fiscalyear_clos`,
the fiscal-year model name, and a filename glob.

- **The closing is computed on the fly at report time** — a dedicated aggregate query keyed on the
  account's initial-balance flag over all dates up to the fiscal-year start —
  `R/account_reports/models/account_general_ledger.py:314-339`, period built at `:343-360`. — `FACT VERIFIED`
- **The result is grafted onto a real account for display only, not posted** — in-code comment and
  application at `:203`, `:206-223`. — `FACT VERIFIED`
- **Profit-and-loss versus balance-sheet membership is a computed property of the account**, not a posted
  transfer — `R/account/models/account_account.py:666-668`. — `FACT VERIFIED`
- The balance sheet renders current-year and prior-year retained earnings as **report lines** —
  `R/account_reports/data/balance_sheet.xml:159`, `:218`, `:225`, `:240`. — `FACT VERIFIED`
- The fiscal-year object is a **date-range definition only** — no entry generation —
  `R/account_accountant/models/account_fiscal_year.py:10-40`. — `FACT VERIFIED`
- The current-year-earnings account is a **singleton per company set**, enforced by constraint —
  `R/account/models/account_account.py:33-42`; created on demand at `R/account/models/company.py:740-766`. — `FACT VERIFIED`
- **The only posted entry touching it is the one-off go-live opening entry**, where it is the balancing
  line — `R/account/models/company.py:813-829`, `:846-853`. — `FACT VERIFIED`
- A real recurring closing-entry generator **does** exist — **but only for VAT**, not for
  profit-and-loss to equity — `R/account_reports/models/account_generic_tax_report.py:216`, `:256`. — `FACT VERIFIED`
- **The reference never posts a profit-and-loss to retained-earnings journal entry.** Income and expense
  accounts accumulate across fiscal years in the ledger; every statement that needs a year boundary
  re-derives it at query time. — `SUPPORTED INTERPRETATION`

## §8 What is unlocked at close, for O2C specifically

- **The stock side contains no reference to any lock date.** PATTERN `lock_date` over the inventory,
  inventory-accounting, sales and sales-inventory modules, all file types: **zero matches.** — `FACT VERIFIED`
- The valuation posting path creates the entries as superuser and **posts them through the SAME posting
  routine as a manual entry** — `R/stock_account/models/stock_valuation_layer.py:96-100`, second site
  `:286-288` — including the reschedule and the on-post lock check. — `FACT VERIFIED`

### Answer: can a valuation entry land in a period locked for accounting?

**`FACT VERIFIED` — no, but not because it is refused: because its date is silently moved.** There is no
error on the valuation path; the reschedule runs first and the check then passes.

- **The date the valuation entry proposes** — forced-period date if in context, else the layer's own
  accounting line date, else **today** — `R/stock_account/models/stock_move.py:669-675`. — `FACT VERIFIED`
- **The standard delivery case is TODAY, not the movement's own date.** The movement's date field is
  never consulted by the value preparation. — `FACT VERIFIED`
- The cost-change entry supplies **no date at all**, so it falls to today. — `FACT VERIFIED`
- **The one path that CAN aim at a past, possibly locked, period is user-supplied and unvalidated** — an
  accounting-date field on the quant with **no constraint and no lock comparison**
  (`R/stock_account/models/stock_quant.py:15-19`), routed into the entry as the forced-period date
  (`:67-74`) and **exposed as a user-writable inventory field** (`:85-88`); the same field exists on the
  count-request wizard. — `FACT VERIFIED`
- **DENOMINATOR for the forced-period date:** PATTERN over PS-ALL excluding tests — **8 lines, 3 files.
  Not one of them tests a lock date.** — `FACT VERIFIED`

**`SUPPORTED INTERPRETATION` — the material consequence.** The valuation layer and its journal entry are
decoupled in time and the decoupling is silent: the layer is created unconditionally with **no date field
of its own** (its only temporal key is the creation timestamp, which is also its ordering key), stock
valuation reporting is keyed on that creation timestamp, and the general ledger is keyed on the
accounting date that posting may have moved. **Where a lock date shifts a valuation entry, the inventory
valuation report and the general ledger will disagree for the affected period, and nothing detects or
reports that divergence.**

**`FACT VERIFIED` — a second ordering issue on the same path.** Entry creation and posting run seven
lines before the company-consistency check on the same layer set. The company consistency is verified
after its journal entries are already posted.

## §9 What the reference provides at company level

1. A company column on each O2C model, populated by **four independent mechanisms**. **There is no single
   propagation invariant to inherit.**
2. **Record-rule isolation, not model isolation.** The boundary is a set of rule rows evaluated against
   the user's **activated** companies — the company switcher — and those rows are runtime-editable data.
3. Field-level consistency that is **opt-in per model and off on four of the chain models**, that admits
   company-less and parent-company records rather than requiring equality, and that on the chart of
   accounts is a many-to-many by design.
4. A **hard refusal** for single-step cross-company movement of valued goods — the strongest single
   boundary found — reachable **only for valued movements**.
5. **Lock dates that redirect rather than bar**, with an all-users, no-expiry exception model and one
   context sentinel that skips the check outright.
6. **No year-end closing entry** — the fiscal-year boundary is a report-time derivation.
7. Intercompany mirroring that runs **as superuser by default** and locates the counterparty with an
   **unscoped** elevated search over the whole company table.
8. A **shared, company-less inter-company transit location** that a company-creation hook wires onto
   **every other company in the database**.

The re-expression of this against the SMEsPlus three-scope model is in
`20_P02_SCOPE_OWNERSHIP_MATRIX.md`.

## §10 Negative claims, with search scope

1. **No tenant entity found** in the five core modules under case-insensitive `tenant` over `*.py` —
   zero matching files.
2. **No lock-date reference found** in the inventory, inventory-accounting, sales and sales-inventory
   modules under `lock_date`, all file types — zero matches.
3. **No auto-validation opt-in found** on the movement, movement line, quant or valuation layer.
4. **No profit-and-loss to retained-earnings closing-entry generator found** in PS-ALL under the six
   declared patterns. The only closing-entry generator returned by that scope is the VAT one.
5. **No lock-date validation found on the quant's accounting-date field** under `lock_date`,
   constraint decorators, or the violated-lock helper.
6. **No company-domain term found** in the forecast report's order-line domain builder.
7. **No company term found in any filter** of the interim-account matching routine; the only company
   reference in the method body is the per-document split-recognition guard.
8. **No company-context call found** in the interim-account matching routine, in contrast to the same
   file's cost-of-sales builder.
9. **No scoping term found** in the intercompany counterparty lookup's search domain — a single clause.
10. **No amount, date or exchange-rate equivalence assertion found** between the two sides of an
    intercompany invoice pair, across all 160 lines of that model, under five patterns.
11. **No currency-consistency check found** in the order→purchase-order direction, in contrast to the
    reverse direction.
12. **No consistency flag found on the movement's destination location**, present on its source and final
    locations.
13. **No use of the lock-bypass sentinel found outside partner merge** — 5 lines, 3 files, 2 use sites.
14. **No lock check found in accounting-document creation.**

**`UNRESOLVED — EVIDENCE REQUIRED`**

- Whether the environment company at the moment the valuation entries are validated can, in a scheduler
  or cross-company delivery-validation context, differ from the movement's company — and therefore
  whether the missing company context in the interim-account matching routine produces a real
  mis-resolution or only a latent one. Settling this requires runtime tracing through picking validation;
  static reading does not settle it.
- Whether any localisation module in PS-ALL supplies a jurisdiction-specific year-end closing entry. The
  §7 patterns were run over PS-ALL, but the localisation module list was **not separately enumerated as
  its own denominator**; negative claim 4 is bounded by the stated patterns, not by a localisation census.
- Whether the company-dependent category account properties are read anywhere else on the O2C path
  without a covering company context. A full call-graph enumeration of the account resolver's callers was
  not performed.
