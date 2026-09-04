# GR1 — FINAL INDEPENDENT GATE REVIEW — CLOSURE VALIDITY

**Reviewer:** Final Independent Gate Reviewer 1
**Session:** `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · Layer 2 / audit quarantine
**Date:** 2026-09-04
**Independence:** I authored none of this package and took part in no prior review round. I treated
`G02`–`G05`, `C10`, `C12` and every prior reviewer as **claims**, not as evidence.

**Method.** Every citation below marked *personally read* was opened directly in the read-only
reference tree at
`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/`
with `sed -n` / `grep -n`. Nothing under that path was modified. Where I could not verify, I wrote
`UNKNOWN` rather than padding. No implementation is proposed and nothing is approved — the Boss is
the sole Final Approver.

**Reference-tree line numbers cited in this document are my own reads, not the package's.**

---

## PART 1 — PER-BLOCKER VERDICTS

| Blocker | Claimed disposition | My verdict | Citation I personally read | Note |
|---|---|---|---|---|
| `SB-05` — cross-tenant FX rate integrity | `VERIFIED DEFECT` — scoped | **`CONFIRMED WITH CAVEAT`** | `base/models/res_currency.py:130` (`('company_id','in',(False, company.root_id.id))`); `base/security/base_security.xml:62-66`; `base/security/ir.model.access.csv:60-64`; `base/models/res_currency.py:365-366`, `:368-371`; **`account/security/ir.model.access.csv:7`** | The defect itself is **confirmed at full strength**. One load-bearing limiting `VERIFIED FACT` — §2.5, "only a system administrator can create any rate row" — is **`CONTRADICTED`** by `account/security/ir.model.access.csv:7`. See `GR1-F-01`. The error makes the blocker **worse**, not better. |
| `FX-08` — branch-company rate context | `VERIFIED DEFECT` | **`CONFIRMED WITH CAVEAT`** | `currency_rate_live/models/res_config_settings.py:1374-1376`, `:205`, `:269`, `:289`; `base/models/res_currency.py:130`, `:389-397`, `:399-406` | Writer and resolver sides both verified exactly as cited. Two caveats: §7 says **two** divergent scoping helpers — I count **four** (`GR1-F-03`); and §5's "net detectability: none" is **over-scoped** — it holds for invoices/bills but not for non-invoice journal entries (`GR1-F-04`). |
| `FX-07` — revaluation control contamination | `VERIFIED DEFECT` | **`CONFIRMED`** | `account_reports/models/account_multicurrency_revaluation_report.py:41`, `:43-45`, `:58-60`, `:63-66`; `account_reports/wizard/multicurrency_revaluation.py:169-178`; `base/models/res_currency.py:140` | Every citation is exact and every quoted fragment is verbatim. The strongest-evidenced of the four. If anything the closure is **under**-stated (`GR1-F-05`). |
| `B-05` — Studio approval engine | `VERIFIED` — parent finding rescoped | **`CONFIRMED WITH CAVEAT`** | `web_studio/models/studio_approval.py:381-393` (patch + `create`/`write`/`unlink` exclusion at `:385-386`), `:267-268`, `:398-404`, `:459` | All three particulars verified verbatim, including the self-documenting comment. Caveat: residual `B05-R3` is classified `C — NOT YET SEARCHED`; I searched it and **found a reachable elevation path in ordinary operation** (`GR1-F-06`). `B05-R2` is partly closable on a code fact. |

**No blocker is `CONTRADICTED` at the level of its central defect.** All four defects are real and I
reproduced each from source. The caveats concern **the boundaries the closures drew around those
defects**, which is precisely where this package's documented failure mode lives.

---

## PART 2 — ANSWERS TO QUESTIONS A–H

### A. Are `SB-05` and `FX-08` genuinely closed?

**`SB-05` — the defect is closed; one of its stated limits is not.**

`VERIFIED FACT` (personally read): `base/models/res_currency.py:130` filters
`('company_id', 'in', (False, company.root_id.id))`. A null-company rate row is matched for every
company in the database. `base/security/base_security.xml:62-66` carries
`['|', ('company_id','parent_of',company_ids), ('company_id','=',False)]` — the record rule
**explicitly admits** the null-company row for every user. Both G02 claims are exact.

`VERIFIED FACT`: `base/models/res_currency.py:365-366` — `company_id` is a plain nullable
`Many2one` defaulting to `self.env.company.root_id`. `:368-371` — the only SQL constraints are a
uniqueness triple and `CHECK (rate>0)`; there is no company or tenant boundary on consumption. G02
§2.1 and §2.6 are exact.

**The over-statement.** G02 §2.5 states as `VERIFIED FACT`: *"only a system administrator can create
any rate row, including a null-company one."* That is true of `base/security/ir.model.access.csv`
alone. It is **`CONTRADICTED`** at domain scope by
`account/security/ir.model.access.csv:7`:

```
access_res_currency_rate_account_manager,res.currency.rate account manager,base.model_res_currency_rate,group_account_manager,1,1,1,1
```

`group_account_manager` — an ordinary accounting manager — holds **create, write and unlink**. And
`base/views/res_currency_views.xml:20`, `:44`, `:169` expose `company_id` as an **editable,
non-readonly** field in an `editable="bottom"` / `editable="top"` list and in the rate form, gated
only by `base.group_multi_company`. The record rule at `base_security.xml:64` admits
`company_id = False` for write as well as read.

So the row in G02 §3 reading *"An ordinary user creates a cross-tenant rate | **No** | §2.5 — system
administrator only"* is **not supported**. This matters because G02 itself designates that limit
"load-bearing", and because `C12` left open exactly the question it purports to answer ("whether they
arise is open"). Under `Tolerance = 0` this is the single most consequential defect in the package.

**Is the disposition over- or under-stated?** The **defect** is stated at the right scope and G02
deserves credit for two honest *narrowings* against its own parent: it correctly refutes `C10`'s
"re-measure another tenant's postings" using `account/models/account_move_line.py:123-128` and
`:139-142` (`balance` and `amount_currency` both `store=True` — I read them), and it correctly
declines to claim precedence override. Those are disciplined. The **limits** are over-stated on one
axis.

**`FX-08` — closed, and understated.**

`VERIFIED FACT` (personally read): `currency_rate_live/models/res_config_settings.py:1374-1376` is
verbatim as quoted. `:205` `update_currency_rates` iterates `self` grouped by provider and calls
`companies._generate_currency_rates(...)` at `:230`; `:269` is `for company in self:`; `:289` is
`CurrencyRate.create({... 'company_id': company.id})`. There is **no** `root_id` normalisation
anywhere on that path. `base_setup/models/res_config_settings.py:12-13` — `company_id` defaults to
`self.env.company`, which may be a branch. The writer/resolver disjunction is exactly as claimed.

I additionally closed residual `FX08-R1`, which G03 classified `C — NOT YET SEARCHED`. See
`GR1-F-02`: the settings UI does **not** restrict rate maintenance to a root company, whereas the
cron **does**. This confirms and sharpens `FX-08` rather than weakening it.

### B. Can any financial fact cross a tenant or company boundary?

**Yes — and by more paths than the package has found.** Tested independently.

**Path 1 — the rate record rule (verified, and the package has it).**
`base/security/base_security.xml:62-66`. The `('company_id','=',False)` disjunct is unconditional. It
is not perm-scoped, so it governs read, write, create and unlink alike. `_get_rates` uses `_search`
(`base/models/res_currency.py:128`, `:133`) with no elevation, so record rules apply — and permit the
crossing. `VERIFIED FACT`.

**Path 2 — `_get_rates` (verified, and the package has it).**
`base/models/res_currency.py:130`. No tenant dimension exists in the filter, and none exists in the
model. `VERIFIED FACT`.

**Path 3 — the rate writer (verified, and the package has it).**
`currency_rate_live/models/res_config_settings.py:289`. Writes `company.id`, unnormalised.
`VERIFIED FACT`.

**Path 4 — `NOT IN THE PACKAGE`: the consolidation currency table bypasses the ORM entirely.**
This is `GR1-F-07` in Part 3 and is the most serious thing I found. In
`account/models/res_currency.py`, `_create_currency_table` (`:75`) executes raw SQL through
`self._cr.execute` at `:125`. Five join predicates —`:183`, `:211`, `:258`, `:300`, `:316`, `:320` —
select the translation rate with `rate.company_id = %(main_company_id)s`, where
`main_company_id = main_company.root_id.id` and `main_company = self.env.company` (`:102`). The
rows so selected are used to translate **`other_companies`** — every selected company whose currency
differs from the acting company's (`:103-104`). Because this is raw SQL, **no record rule executes on
this path at all**. `VERIFIED FACT`.

**Path 5 — `NOT IN THE PACKAGE`: write access is broader than the package states.**
`account/security/ir.model.access.csv:7`. See `GR1-F-01`. `VERIFIED FACT`.

**Negative I tested and refuted against myself.** I hypothesised that the multicurrency revaluation
report aggregates across `env.companies` spanning different roots while resolving rates from one
root. **Refuted.** `account_reports/models/account_report.py:1276-1288` shows
`filter_multi_company` defaulting to `'disabled'`
(`account/models/account_report.py:91-95`), so the else-branch applies:
`companies = self.env.company._accessible_branches()` — the active company and its branches, which
share a root. Rate scope is therefore consistent for that report. I record the refutation because a
reviewer's discarded hypotheses are part of the evidence.
`NEGATIVE CLASS: A — VERIFIED ABSENCE`, boundary
`addons/account_reports/models/account_report.py` `_init_options_companies` and
`addons/account/models/account_report.py` field definition.

### C. Are `FX-07` and `B-05` evidence-backed?

**`FX-07` — yes, fully. This is the best-evidenced document in the package.**

Personally read in `account_reports/models/account_multicurrency_revaluation_report.py`:
- `:41` — `rates = active_currencies._get_rates(self.env.company, options.get('date').get('date_to'))`. The resolver is the same one. **Verbatim as quoted.**
- `:43-45` — `company_rate = rates[self.env.company.currency_id.id]` then `rates[key] /= company_rate`. **Verbatim.**
- `:58-60` — the sole rate guard, `if currency_rates['rate'] == 0: raise UserError(...)`. **Verbatim.**
- `:63-66` — `options['custom_rate']` computed by `float_is_zero(cr['rate'] - rates[...], 20)`.
- `base/models/res_currency.py:140` — `SQL("COALESCE((%s), (%s), 1.0)", ...)`. The `1.0` terminal fallback is exactly where G04 says it is.
- `account_reports/wizard/multicurrency_revaluation.py:169-178` — `create_entries` creates the move, `action_post()`s it, `_reverse_moves`, sets `reversal_date`, `action_post()`s the reversal. **Verbatim.**

`1.0` does not equal `0`, so the guard does not fire. G04's central chain is a direct reading, and its
stated confidence ("high") is warranted. `CONFIRMED`.

Two additions that G04 did **not** claim and that make its case stronger, not weaker — see
`GR1-F-05`.

**`B-05` — yes, on all three particulars, with one residual that is no longer open.**

Personally read in `web_studio/models/studio_approval.py`:
- `:381-393` — `_patch` replaces a method via `setattr`, preserving the original as `studio_approval_rule_origin`; `:382-384` refuses private methods; **`:385-386` refuses `create`, `write` and `unlink`** (`if method_name in ["create", "write", "unlink"]: raise ValidationError(...)`). **Verbatim.**
- `:459` — `_patch(Model, approval.method, approval_method)` inside the loop over `self.search([])`. **Verbatim.**
- `:267-268` — `if model_name == "account.move": state_field = self.env["ir.model.fields"]._get("account.move", "state")`. **Verbatim**, and the neighbouring `sale.order` / `purchase.order` cases confirm it is a by-name special case in a series.
- `:398-404` — `if self.env.su:` … the three-line comment naming *"invoice posting because online payment succeeeded"* (misspelling in the original) … `_logger.info("Skipping approval checks in a sudoed environment: ...")` … `return method.studio_approval_rule_origin(...)`. **Verbatim, including the comment.**

The skip is written with `_logger.info` — application log only. G05's claim that no accounting record
is produced is `VERIFIED FACT`. G05's `INFERENCE` that such a control "constrains the button, not the
fact" follows directly from `:385-386` and is correctly labelled as an inference.

`B05-R3` — "whether other elevation paths reach `action_post` in normal operation" — is classified
`C — NOT YET SEARCHED`. I searched it. See `GR1-F-06`: a path exists on the ordinary online-payment
flow. That reclassifies the residual and strengthens the disposition.

`B05-R2` — "whether `web_studio` is present in the intended SMEsPlus reference baseline" — is
partly closable on a code fact: the module **is present** in this reference tree
(`web_studio/models/studio_approval.py`, 1303 lines, read directly). Whether it belongs in the
*intended* SMEsPlus baseline is an SMEsPlus scoping decision, not a code fact, and remains
`UNKNOWN — EVIDENCE REQUIRED`.

### D. Are any remaining negative claims still over-scoped?

**One is, and it is on the `Tolerance = 0` blocker.**

| Claim | As written | Correct class | Assessment |
|---|---|---|---|
| G02 §2.5 — "only a system administrator can create any rate row" | Presented as `VERIFIED FACT`, unqualified, with **no declared search boundary** | Was `B — NOT FOUND IN SEARCHED SCOPE` (boundary: `base/security/ir.model.access.csv`); is now **`E — CONTRADICTED`** by `account/security/ir.model.access.csv:7` | **A Class-B negative presented as Class A**, then relied on as a load-bearing limit in the §3 table and in §4. This is the exact prohibited promotion. |
| G02 §2.8 — no cross-request rate cache | `B — NOT FOUND IN SEARCHED SCOPE`, ORM/deployment caching `C` | Correct as classified | Correctly scoped. Boundary declared. |
| G02 `SB05-R3` — shipped/localization null-company rate rows | `C — NOT YET SEARCHED` | Correct as classified | Correctly scoped. The parenthetical "shipped currency master data contains no rate rows at all" is an unboundaried assertion inside a `C` residual; I did not verify it and record it as `UNKNOWN`. |
| G03 §6 — no restatement tool | `B — NOT FOUND IN SEARCHED SCOPE`, boundary `addons/account`, `addons/currency_rate_live` | Correct as classified | Correctly scoped. |
| G03 §7 — "**two** rate-resolution helpers … apply different company scoping rules" | Presented as `VERIFIED FACT` | The two cited are verified; the count is **understated** | Not an over-claim. An **under**-claim. Four rules exist (`GR1-F-03`). |
| G03 §5 — "Net detectability: **none** through any accounting control" | Presented as a bolded conclusion, unboundaried | `A — VERIFIED ABSENCE` for invoices/bills; **not established** for non-invoice journal entries | **Over-scoped.** See `GR1-F-04`. Modest — the divergence is a screen artefact, not a control — but the word "none" is unbounded and the evidence is not. |
| G04 `FX07-R1` / `FX07-R2` | `B` and `C` respectively, boundaries declared | Correct as classified | Correctly scoped. G04 §2 declares its search boundary explicitly and §5 records three tested refutations. **This is the model the rest of the package should follow.** |
| G05 §3.1 — no reference to the journal-entry model in `approvals` | `B`, boundary "its models or data" | Correct as classified | Correctly scoped. |
| G05 §6 — "`E — CONTRADICTED` at domain scope, `A — VERIFIED ABSENCE` within `addons/account`" | Dual-classed | Correct, and correctly split | **Exemplary.** This is how a rescoped negative should read. |

**Summary.** Eight of ten negatives are correctly classed with declared boundaries — a materially
better record than this package's history. One is over-scoped (G03 §5). One is `CONTRADICTED` and was
never boundaried at all (G02 §2.5), and it sits on the tenant-isolation blocker.

### E. Does any finding remain mathematically correct but economically wrong?

**Yes — three cases the package has not registered.** All are `BALANCED BUT WRONG` in the package's
own sense: internally consistent, externally false, undetectable by arithmetic control.

1. **`GR1-F-08` — company precedence outranks recency.** `base/models/res_currency.py:132` orders
   `company_id.id, name DESC` with **company as the primary key**. Within the two-value domain at
   `:130`, this means the root company's rate is chosen **before** any null-company rate regardless of
   date. A root rate from years ago therefore beats a null-company rate from yesterday. G02 §2.4
   states this outcome correctly, but records it only as *"a company's own rate takes precedence"* — a
   framing that reads as a **safeguard**. It is also a staleness mechanism.
2. **`GR1-F-09` — the fallback branch has no date bound and can apply a future rate to a past
   posting.** `base/models/res_currency.py:133-136`: `rate_fallback` carries **no `('name','<=',date)`
   predicate** and orders `name ASC` — the earliest rate ever recorded. It is reached only when no
   rate exists on or before `date`, which means the rate it returns is **necessarily dated after the
   posting**. G03 §3 names this branch but describes it neutrally as "earliest rate ever"; it does not
   state that the branch is an **anachronism by construction**.
3. **`GR1-F-07` — the consolidation table's own silent par fallback**, in raw SQL, at five sites, with
   no guard at all. See Part 3.

### F. Does any unresolved finding violate `Tolerance = 0`?

**Yes. Two, on my own evidence.**

1. **`GR1-F-01`** (tenant isolation). `Tolerance = 0` was already declared for `SB-05`. The finding
   that an ordinary accounting manager — not a system administrator — can create the null-company row
   through the standard UI **materially enlarges the population who can cause the crossing**, and it
   contradicts the closure's own bounding statement. A `Tolerance = 0` item cannot cross a gate with a
   contradicted load-bearing `VERIFIED FACT` in its closure.
2. **`GR1-F-07`** (tenant isolation **and** financial integrity). A raw-SQL path that selects another
   company's translation rate from the acting company's root scope, **outside the ORM and therefore
   outside every record rule**, and silently substitutes `1` when no row matches, is a
   `Tolerance = 0` candidate on both limbs. It is not in the package.

`GR1-F-06` (the reachable elevation bypass) does not by itself violate `Tolerance = 0`, because the
approval engine is not an accounting control in the first place — G05's own rescoping is what makes
that true. It is a `HOLD` item for the control-design track, not a gate-stopper.

### G. Is the evidence lineage complete?

**Substantially, with one break and one gap.**

- **Complete.** Every file-and-line citation in all four documents that I checked resolves to real
  source, and every fragment presented as a quotation is verbatim. I found **no fabricated citation
  and no misquotation** across `G02`–`G05`. For a package with this history, that is the most
  important lineage result in this review, and I state it plainly.
- **Break.** `G02` §2.5's conclusion has no boundary and its source does not support the scope
  claimed. The lineage stops at `base/` and the conclusion is written at domain scope. That is a
  lineage break, not merely a scoping slip.
- **Gap.** `G02` §2.7 cites `account/models/res_currency.py:105-160` as "the consolidation currency
  currency table, which resolves through the same path." Having read `:75-336`, that citation is
  **directionally right but materially incomplete**: the table does **not** resolve through the same
  path. It uses raw SQL with a **different** company predicate and **excludes** null-company rows
  (`GR1-F-07`). The citation points at the right code and draws the wrong conclusion from it. The
  lineage exists; the reading is thin.
- **Line-number drift.** `G02` §2.2 and `G03` §2 cite `:128-131` for a predicate I read at `:130`, and
  `:365-366`/`:368-371` for content I read at `:365-366`/`:368-371`. Ranges are right, individual
  lines are occasionally off by one or two. Immaterial, but a `RECOMMENDATION`: cite the predicate
  line, not the call block, so a reviewer can check a claim without reconstructing it.

### H. Has any conclusion been strengthened beyond its evidence?

**This is the decisive question, and the answer is: once, materially — and it is not where the
package's history would predict.**

The pattern in this package's record is over-claiming the **severity** of a defect. That did **not**
happen here. On the contrary, three of the four documents *narrowed* their parent claims against
their own interest:

- `G02` refuted `C10`'s "re-measures another tenant's postings" using the stored-field evidence at
  `account_move_line.py:123-128`/`:139-142`, and said so in bold.
- `G02` refused to claim precedence override and stated the three limits "as firmly as the defect".
- `G05` rescoped a finding it could have left as a clean contradiction, and dual-classed the negative
  (`E` at domain scope, `A` within `addons/account`) instead of taking the stronger single class.
- `G04` recorded three refutations it tested against itself, one of which ("the user override makes
  the resolved rate advisory") it marked *"partially true and insufficient"* rather than dismissing.

That is disciplined work and I record it as such.

**The one material over-claim runs the other way: a *limiting* statement was strengthened beyond its
evidence.** `G02` §2.5 asserts, unboundaried and as `VERIFIED FACT`, that only a system administrator
can create a rate row. The evidence supports that only within `base/security/ir.model.access.csv`.
`account/security/ir.model.access.csv:7` contradicts it. Because `G02` then leans on that statement
twice — in the §3 possibility table and in §4's "It is not an arbitrary-user cross-tenant write" —
the package **understates the reachability of a `Tolerance = 0` tenant-isolation defect**. An
over-claimed limit is as damaging as an over-claimed severity, and it is harder to catch because it
reads as caution.

**One secondary over-claim.** `G03` §5's "Net detectability: **none** through any accounting control"
is unbounded. It is `A — VERIFIED ABSENCE` for invoices and bills — `account_move_line.py:661-664`
reads the **stored** `invoice_currency_rate` (`account_move.py:475-481`, `store=True`), exactly as
`A1-01` says. It is **not** established for non-invoice journal entries, where
`account_move_line.py:665-671` computes `currency_rate` live and **unstored**. See `GR1-F-04`.

**Two under-claims**, recorded for symmetry: `G03` §7 (four scoping rules, not two) and `G04`
(two unstated amplifiers, `GR1-F-05`).

**Net answer to H:** the four closures do **not** claim more severity than their citations support.
One claims more **certainty about a boundary** than its citations support, on the tenant-isolation
blocker, and that single defect is sufficient to withhold a gate under `Tolerance = 0`.

---

## PART 3 — INDEPENDENT FINDINGS NOT IN THE PACKAGE

### `GR1-F-01` — An accounting manager, not only a system administrator, can create a null-company rate

**FINDING.** `G02` §2.5's load-bearing limit is contradicted at domain scope. The population able to
create the cross-tenant rate row is `group_account_manager`, through the standard rate list, not
`group_system` alone.

**EVIDENCE** (`VERIFIED FACT`, all personally read):
- `account/security/ir.model.access.csv:7` —
  `access_res_currency_rate_account_manager,...,base.model_res_currency_rate,group_account_manager,1,1,1,1`
  (`perm_read,perm_write,perm_create,perm_unlink` all `1`). Line `:6` grants the same on
  `res.currency` itself.
- `base/views/res_currency_views.xml:20` (rate list, `editable="bottom"`), `:44` (rate form), `:169`
  (rate list embedded in the currency form, `editable="top"`) — `company_id` is rendered as a plain
  editable field, `groups="base.group_multi_company"`, with **no `readonly`**.
- `base/models/res_currency.py:365-366` — `company_id` is a nullable `Many2one`; the default is
  overridable and the field is not `required`.
- `base/security/base_security.xml:62-66` — the record rule's `('company_id','=',False)` disjunct
  carries no `perm_` restriction, so it admits create and write, not only read.

**INFERENCE** (labelled, not promoted): a user holding `group_account_manager` **and**
`group_multi_company` can therefore clear the company on a rate row through the shipped UI. I did not
execute this; I read the four artefacts that compose it.

**NEGATIVE CLASS.** `E — CONTRADICTED`. Boundary of my search: `addons/**/security/*.csv` and
`addons/**/*.xml` for `model_res_currency_rate`, executed across the whole `addons/` tree — the two
ACL files and the one `ir.rule` above are the **complete** set in that tree.
`A — VERIFIED ABSENCE` of any further ACL or record rule on `res.currency.rate` within `addons/`.

**CLASSIFICATION.** `Tolerance = 0` — tenant isolation. Raises `SB-05`'s reachability.

**REQUIRED RESOLUTION.** `G02` §2.5, its §3 table row, and its §4 limiting paragraph must be
rewritten to the evidence, with the boundary declared. `SB05-R3` should be re-opened to ask not only
whether shipped data creates such rows but **who in a live tenant can**. Routed to the Boss as a
correction to a `Tolerance = 0` closure, not as a new finding.

---

### `GR1-F-02` — The rate-maintenance UI is not root-scoped, while the cron is — closing `FX08-R1`

**FINDING.** `G03` residual `FX08-R1` ("whether the settings UI prevents selecting a branch company
for rate maintenance") is classified `C — NOT YET SEARCHED`. I searched it. The UI does **not**
prevent it — and the automated path **does**, which is what makes the divergence live.

**EVIDENCE** (`VERIFIED FACT`, personally read):
- `currency_rate_live/models/res_config_settings.py:1326-1331` — the cron entry point
  `run_update_currency` searches `[('currency_next_execution_date','<=',...), ('parent_id','=',False)]`.
  **`parent_id = False` restricts the cron to root companies.**
- `currency_rate_live/models/res_config_settings.py:1374-1376` — the manual button
  `update_currency_rates_manually` calls `self.company_id.update_currency_rates()` with **no such
  filter**.
- `currency_rate_live/views/res_config_settings_views.xml:22` — the button is rendered with no
  `invisible` or `readonly` guard on `is_root_company`.
- `account/views/res_config_settings_views.xml:103-106` — the enclosing
  `<setting id="update_exchange_rates">` is gated only on `invisible="not group_multi_currency"`.
- `base_setup/models/res_config_settings.py:12-13` — `company_id` defaults to `self.env.company`;
  `:14`, `:123-125` — `is_root_company` **exists** as a computed field but is not referenced by
  either view.

**NEGATIVE CLASS.** `A — VERIFIED ABSENCE`. Boundary: `addons/currency_rate_live/views/` (both files,
read in full) and `addons/account/views/res_config_settings_views.xml` (the `update_exchange_rates`
setting block). No root-company gate exists on the rate-maintenance control in that boundary. I did
not search localization modules — `C — NOT YET SEARCHED` for those.

**CLASSIFICATION.** Confirms and sharpens `FX-08`. The reference **has** the concept of root-scoped
rate maintenance and applies it to the cron; the manual path simply does not use it. This makes
`FX-08` an inconsistency inside the reference's own design, not an unconsidered omission —
strengthening the `REJECT` position in `G03` §9.

**REQUIRED RESOLUTION.** Reclassify `FX08-R1` from `C` to `A` within the stated boundary.
`RECOMMENDATION`: extend the search to localization modules before the residual is closed outright.

---

### `GR1-F-03` — Four company-scoping rules govern one rate table, not two

**FINDING.** `G03` §7 reports two divergent rate-resolution helpers in `base/models/res_currency.py`.
There are **four** distinct company-scoping rules over `res.currency.rate` across `base` and
`account`, and the fourth is outside the ORM.

**EVIDENCE** (`VERIFIED FACT`, all personally read):

| # | Site | Rule | Null-company rows |
|---|---|---|---|
| a | `base/models/res_currency.py:130` (`_get_rates`) | `company_id IN (False, company.root_id.id)` | **included** |
| b | `base/models/res_currency.py:403` (`_get_last_rates_for_companies`) | `x.company_id == company or not x.company_id` — **exact** company | **included** |
| c | `base/models/res_currency.py:396` (`_get_latest_rate`) | `x.company_id == (self.company_id or self.env.company.root_id)` — exact company | **excluded** |
| d | `account/models/res_currency.py:183`, `:211`, `:258`, `:300`, `:316`, `:320` | `rate.company_id = main_company.root_id.id`, raw SQL | **excluded** |

Rules (b) and (c) feed `company_rate` and `inverse_company_rate` at
`base/models/res_currency.py:416`, `:419`, `:423` — and those are precisely the two fields the user
**types and reads** in the rate list (`base/views/res_currency_views.xml:21-22`, `:169-173`). Rule (a)
measures the posting. Rule (d) consolidates.

> **`VERIFIED FACT`:** the rate a user enters and sees, the rate that measures a posting, and the rate
> that consolidates the result are resolved by **three different company-scoping rules** over the same
> table.

**Additional defect at site (b), not in the package.** `base/models/res_currency.py:401-403`:

```
company.sudo().currency_id.rate_ids.filtered(lambda x: (
    x.rate
    and x.company_id == company or not x.company_id
))
```

Python binds `and` tighter than `or`, so this evaluates as
`(x.rate and x.company_id == company) or (not x.company_id)`. **The `x.rate` truthiness guard does not
apply to the null-company branch.** A null-company row with an unset rate is admitted. `:404` then
applies `.rate or 1` — another silent par substitution. The method also carries **no date bound**, so
a future-dated rate is eligible. `VERIFIED FACT` for the parse; `INFERENCE` for the reachability,
since `CHECK (rate>0)` (`:369`) constrains non-null values but does not exclude `NULL`.

**NEGATIVE CLASS.** `A — VERIFIED ABSENCE` of any shared scoping helper. Boundary:
`addons/base/models/res_currency.py` (read in full for all `company_id` predicates) and
`addons/account/models/res_currency.py` (read `:43-336`). Other modules not searched —
`C — NOT YET SEARCHED`.

**CLASSIFICATION.** `HOLD`. Reinforces `FX-08` and `SB-05`. `G03` §9's requirement — "one scoping
rule, applied identically by every writer and every reader" — is correct and now has twice the
evidence behind it.

**REQUIRED RESOLUTION.** `G03` §7 to be restated at four rules with the table above. The operator-
precedence defect at `:403` to be registered separately; it is a distinct class of error from the
scoping divergence and should not be folded into it.

---

### `GR1-F-04` — "Net detectability: none" is over-scoped to non-invoice journal entries

**FINDING.** `G03` §5 concludes, unbounded, that there is no detectability through any accounting
control. That holds for invoices and bills. For **non-invoice journal entries** a display-versus-stored
divergence does arise, because the displayed rate is not stored on that branch.

**EVIDENCE** (`VERIFIED FACT`, personally read) —
`account/models/account_move_line.py:661-673`, `_compute_currency_rate`:
- `:663-664` — if the move `is_invoice(include_receipts=True)`, `currency_rate` is taken from
  `move_id.invoice_currency_rate`, which **is** stored (`account/models/account_move.py:475-481`,
  `store=True`, `@api.depends('currency_id','company_currency_id','company_id','invoice_date')`).
  **`G03` §5 and `A1-01` are correct here.**
- `:665-671` — **otherwise** `currency_rate` is computed live via `_get_conversion_rate(...)`.
- `:134-138` — `currency_rate` on the line is declared `compute='_compute_currency_rate'` with **no
  `store=True`**, whereas `balance` (`:123-128`) and `amount_currency` (`:139-142`) are both stored.

`INFERENCE` (labelled): once the missing rate is later entered, a posted miscellaneous journal entry
will display a corrected `currency_rate` alongside a frozen par `balance`. That is a visible
inconsistency on the same screen.

**I do not overstate its value.** It is a **screen artefact, not a control**: nothing raises it,
nothing reconciles it, nothing reports on it, and it requires a human to look at a specific field on a
specific posted line after the rate table has been repaired. `G03`'s substantive conclusion — that no
*accounting control* detects this — survives. Only the word "none", applied without a boundary, does
not.

**NEGATIVE CLASS.** `A — VERIFIED ABSENCE` of a stored document rate on non-invoice lines. Boundary:
`addons/account/models/account_move_line.py` field declarations and `_compute_currency_rate`;
`addons/account/models/account_move.py` `invoice_currency_rate` declaration and compute.

**CLASSIFICATION.** `CONFIRMED WITH CAVEAT` on `FX-08`. Not gate-stopping.

**REQUIRED RESOLUTION.** `G03` §5 to be boundaried: "no detectability through any accounting control,
within `addons/account`; for non-invoice entries a display-versus-stored divergence exists and is not
surfaced as a control."

---

### `GR1-F-05` — `FX-07` is understated: the par default is indistinguishable from a genuine unit rate, and raises no warning

**FINDING.** Two amplifiers that `G04` does not claim and that its own cited lines support.

**EVIDENCE** (`VERIFIED FACT`, personally read) —
`account_reports/models/account_multicurrency_revaluation_report.py`:
1. `:63-66` — `options['custom_rate']` is true only when a supplied rate **differs** from the resolved
   one. A fabricated `1.0` that the user accepts yields `custom_rate = False`, so `:74-75` raises
   **no warning at all**. The report's only user-facing signal about rates is therefore silent in
   exactly the failure case `G04` describes.
2. `:41-45` — the fabricated `1.0` is normalised by `company_rate` and stored into
   `options['currency_rates']` as an ordinary rate. Nothing downstream — including
   `account_reports/wizard/multicurrency_revaluation.py:136-140`, which **prints the rate into the
   journal-entry line label** — can distinguish "no rate row exists" from "the rate is genuinely 1".
   The posted entry's own narrative asserts a rate that was never measured.

**NEGATIVE CLASS.** `A — VERIFIED ABSENCE` of any provenance flag on a resolved rate. Boundary:
`account_multicurrency_revaluation_report.py` `_custom_options_initializer` and `_customize_warnings`;
`wizard/multicurrency_revaluation.py` `_get_move_vals` and `create_entries`; `base/models/res_currency.py:121-141`.

**CLASSIFICATION.** Strengthens `FX-07`. Feeds directly into the Wave's `no event identity` /
provenance theme.

**REQUIRED RESOLUTION.** Record as an extension to `G04` §6's narrow claim. `G04`'s disposition and
confidence need no change.

---

### `GR1-F-06` — The `env.su` approval bypass is reachable on the ordinary online-payment path — closing `B05-R3`

**FINDING.** `G05` residual `B05-R3` ("whether other elevation paths reach `action_post` in normal
operation") is classified `C — NOT YET SEARCHED`. I searched it. A path exists, and it is the very one
the reference's own bypass comment names.

**EVIDENCE** (`VERIFIED FACT`, personally read):
- `payment/controllers/post_processing.py:88-90` — the monitored transaction is obtained as
  `request.env['payment.transaction'].sudo().browse(...)`.
- `account_payment/models/payment_transaction.py:107-109` — inside `_post_process`,
  `self.invoice_ids.filtered(lambda inv: inv.state == 'draft').action_post()`.
- `account_payment/models/payment_transaction.py:196-197`, `:208` — `payment.action_post()` and a
  second `invoices...action_post()` on the capture path.
- `web_studio/models/studio_approval.py:398-404` — the wrapper returns the unguarded original when
  `self.env.su` is true.

**REFERENCE BEHAVIOUR:** an Odoo environment propagates through relational field traversal, so
`tx.invoice_ids` inherits `env.su` from a sudoed `tx`.

**INFERENCE** (labelled, **not** promoted): `env.su` is therefore true at the point `action_post` is
invoked on that path, so every configured Studio approval rule is skipped, with only an
`_logger.info` line. I read both ends of this chain and the propagation rule; I did not execute it.
Runtime confirmation is a cheap test and is **required** before this is stated as fact.

**NEGATIVE CLASS.** `B — NOT FOUND IN SEARCHED SCOPE` for any *further* elevation path. Boundary:
`grep` across `addons/**/*.py` for `sudo().action_post`, `sudo()._post`, `with_user(SUPERUSER`, plus
targeted reads of `addons/payment/controllers/` and `addons/account_payment/models/`. Subscription,
POS, e-commerce and localization posting paths **not** searched — `C — NOT YET SEARCHED`.

**CLASSIFICATION.** `HOLD` for the control-design track. It does **not** escalate `B-05` to
`Tolerance = 0`, because `G05`'s own rescoping establishes that the engine is a customisation facility
and not an accounting control — a bypass of a non-control is a design observation, not an integrity
breach. It does confirm that `G05` §7's requirement (2) — "must not be suppressible by execution
context… a **named automated actor with its own authority**" — addresses a live path rather than a
hypothetical one.

**REQUIRED RESOLUTION.** Reclassify `B05-R3` from `C — NOT YET SEARCHED` to
`B — NOT FOUND IN SEARCHED SCOPE` for further paths, with this path recorded as found and its final
step marked `INFERENCE — RUNTIME CONFIRMATION REQUIRED`.

---

### `GR1-F-07` — The consolidation currency table resolves another company's rate from the acting company's root scope, in raw SQL, outside every record rule, with a silent par fallback

**FINDING.** The most serious item I found that the package does not contain. `G02` §2.7 cites this
code and characterises it as resolving "through the same path". It does not. It uses a **different**
company predicate, **excludes** null-company rows, **bypasses the ORM entirely**, and carries **its own
undeclared par fallback**.

**EVIDENCE** (`VERIFIED FACT`, all personally read in `account/models/res_currency.py`):
- `:75` `_create_currency_table(self, companies, date_periods, use_cta_rates=False)`.
- `:102` — `main_company = self.env.company`.
- `:103-104` — `other_companies = companies - domestic_currency_companies`, i.e. every selected
  company whose currency differs from the acting company's.
- `:112` — `main_company_unit_factor = main_company.currency_id._get_rates(main_company, date_to)[...]`
  — resolved in the **acting** company's scope and then applied to **other** companies.
- `:125` — the whole table is materialised by **`self._cr.execute(SQL(...))`**. This is raw SQL. The
  `res_currency_rate_rule` at `base/security/base_security.xml:62-66` **never executes on this path**.
- `:183`, `:211`, `:258`, `:300`, `:316`, `:320` — every rate join predicate is
  `AND rate.company_id = %(main_company_id)s` with `main_company_id=main_company.root_id.id`
  (`:189`, `:220`, and the corresponding builder arguments).
  In SQL, `company_id = X` is false for `NULL`, so **null-company rates are silently excluded here
  while being included by `_get_rates`.**
- `:178`, `:206` (and the historical/average builders) —
  `CASE WHEN rate.id IS NOT NULL THEN %(main_company_unit_factor)s / rate.rate ELSE 1 END`. **A fourth
  and entirely separate silent par fallback**, in SQL, with no guard, no warning and no
  `UserError` anywhere on the path.

**Three distinct consequences**, each `VERIFIED FACT` for the code and `INFERENCE` for the effect:
1. **Boundary.** Company B's balances are translated with a rate row owned by Company A's root. Where
   `companies` spans more than one root — a shared-database SaaS deployment, or any principal with
   multi-root access — this is a financial fact crossing a company boundary. No record rule can stop
   it, because none runs.
2. **Internal inconsistency.** A null-company rate **is** used to measure a posting (`_get_rates`,
   `:130`) but **is not** used to consolidate it (`:183`). The same company, currency and date can be
   measured one way and reported another.
3. **Undeclared par.** `ELSE 1` produces the same fabricated unit measurement as `SF-01`, at a site the
   package has not registered, on the consolidation path specifically.

**NEGATIVE CLASS.** `A — VERIFIED ABSENCE` of any record-rule enforcement or rate-availability guard
on this path. Boundary: `addons/account/models/res_currency.py:43-336`, read in full, with every `def`,
`_cr.execute`, `rate.company_id` and `ELSE 1` occurrence enumerated by `grep -n`.
`C — NOT YET SEARCHED`: the callers of `_create_currency_table`, and whether any caller constrains
`companies` to a single root.

**CLASSIFICATION.** **`Tolerance = 0` candidate on both limbs — tenant isolation and financial
integrity.** Not in `SB-05`, not in `FX-07`, not in `FX-08`, not in `C05`.

**REQUIRED RESOLUTION.** A targeted closure of its own, on the model of `G04`, before this Wave's gate
is reconsidered. It must establish: which callers reach `_create_currency_table` and with what
`companies` set; whether any caller can span two roots; and whether the `ELSE 1` branch is reachable
in a configuration the tenant can create. Until then the crossing is `UNKNOWN — EVIDENCE REQUIRED` in
its *reachability* and `VERIFIED FACT` in its *mechanism*. **I do not assert that the crossing occurs
in a shipped configuration. I assert that nothing in the searched scope prevents it.**

---

### `GR1-F-08` — Company precedence outranks recency, so a stale own-rate silently beats a current global rate

**FINDING.** `G02` §2.4 presents company precedence as a **safeguard**. It is simultaneously a
staleness mechanism, and the closure does not say so.

**EVIDENCE** (`VERIFIED FACT`, personally read): `base/models/res_currency.py:132` —
`order='company_id.id, name DESC'`, `limit=1`. **Company is the primary sort key; date is secondary.**
Within the two-value domain at `:130`, the root company's most recent rate on or before `date` is
selected whenever one exists at all — of any age — in preference to a null-company rate of any
recency.

`G02` §2.4's own wording ("A null-company rate applies only where the company has no rate of its own
for that currency on or before the date") is **accurate**. My objection is to its framing, not its
content: presented under the heading "a company's own rate takes precedence", it reads as
containment. A root rate from 2010 outranking a global rate from yesterday is not containment.

**NEGATIVE CLASS.** `A — VERIFIED ABSENCE` of any recency bound or staleness guard on the primary
branch. Boundary: `base/models/res_currency.py:121-141`, read in full.
`SB05-R2` (runtime confirmation of `NULLS LAST`) remains an open `INFERENCE` and I did not test it;
my finding does **not** depend on it, since it concerns the company-before-date key order, which is
explicit in the `order` string.

**CLASSIFICATION.** `BALANCED BUT WRONG` — a new case. Register alongside `BW-01` / `BW-16`.

**REQUIRED RESOLUTION.** Record as a distinct `BW` case. `RECOMMENDATION`: the SMEsPlus position
already implied by `G02` §5 and `G03` §9 — one owning boundary, no crossing — should be extended with
an explicit **staleness bound**, since boundary correctness alone does not prevent this.

---

### `GR1-F-09` — The fallback branch has no date bound and applies a future rate to a past posting

**FINDING.** `G03` §3 names the second `COALESCE` branch as "earliest rate ever for that currency in
`(NULL, root)` scope". It does not state that this branch is, by construction, **an anachronism**.

**EVIDENCE** (`VERIFIED FACT`, personally read): `base/models/res_currency.py:133-136` —

```
rate_fallback = self.env['res.currency.rate']._search([
    ('company_id', 'in', (False, company.root_id.id)),
    ('currency_id', '=', currency_id),
], order='company_id.id, name ASC', limit=1)
```

There is **no `('name','<=',date)` predicate** — compare `:129` on the primary branch, which has one.
`:138-141` — `COALESCE(rate_query, rate_fallback, 1.0)`, so this branch is reached **only** when the
primary branch returned nothing, i.e. only when **no rate exists on or before `date`**. The row it
then returns is therefore **necessarily dated after the posting**.

`INFERENCE` (labelled): any backdated posting earlier than the first rate row ever recorded is
measured at a rate that did not exist on the posting date. The entry balances; the measurement is
anachronistic; no control fires.

**NEGATIVE CLASS.** `A — VERIFIED ABSENCE` of a date bound on the fallback branch. Boundary:
`base/models/res_currency.py:121-141`, read in full.

**CLASSIFICATION.** `BALANCED BUT WRONG` — a new case, and a **third** distinct failure mode of the
same `COALESCE`, alongside `BW-01` (par, no rate at all) and `BW-16` (branch rate invisible). It is
also directly relevant to migration: an opening-balance or historical load posted before the first
rate row is exactly the trigger.

**REQUIRED RESOLUTION.** Register as a distinct `BW` case and route to the migration track, where
backdated loads are routine.

---

**Thai statutory matters.** None of my findings turns on Thai law. No Thai statutory claim is asserted
anywhere in this review. Should any downstream party wish to argue that a par or anachronistic
measurement is or is not permissible under Thai requirements, that is
**`HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track.**

---

## PART 4 — REVIEWER 1 POSITION

### What the package got right, stated plainly

I checked every file-and-line citation in `G02`–`G05` that carries weight. **Not one is fabricated and
not one quotation is inaccurate.** For a package whose failure history is over-claiming, that is the
most significant result of this review and it should be recorded as such. `G04` in particular — with
its declared search boundary, its three self-tested refutations, and its refusal to dismiss the
user-override counter-argument — is the standard the rest of the programme should be held to. `G05`'s
dual-classed negative (`E` at domain scope, `A` within `addons/account`) is the correct way to rescope
a contradicted claim and should be adopted as the pattern.

All four defects are real. I reproduced each independently from source. **The gate is not being
withheld because the findings are wrong.**

### Why I cannot recommend the gate open

Three things stand between this package and a gate, and two of them sit on `Tolerance = 0`.

**First — a contradicted `VERIFIED FACT` on the tenant-isolation blocker.** `G02` §2.5 asserts,
without a declared boundary, that only a system administrator can create a rate row.
`account/security/ir.model.access.csv:7` grants `group_account_manager` create, write and unlink;
`base/views/res_currency_views.xml:20`, `:44`, `:169` expose `company_id` as editable. `G02` then
relies on that assertion twice as a limit on a `Tolerance = 0` finding. A closure whose bounding fact
is contradicted has not closed the thing it claims to have bounded. This is a Rule-D violation — a
Class-B negative promoted to Class A — and it is on the one blocker where the project has declared
zero tolerance.

**Second — an unfound `Tolerance = 0` crossing.** `GR1-F-07`. The consolidation currency table selects
another company's translation rate from the acting company's root scope, in raw SQL executed via
`self._cr.execute`, where **no record rule runs at all**, excluding the very null-company rows that
`_get_rates` includes, and silently substituting `1` when nothing matches. Question B asked me to look
for company-scoping gaps the package has not found. This is one, it is on both `Tolerance = 0` limbs,
and `G02` §2.7 cites the exact file while drawing the opposite conclusion from it. Its *mechanism* is
`VERIFIED FACT`; its *reachability in a shipped configuration* is `UNKNOWN — EVIDENCE REQUIRED`, and I
decline to assert more than that. But an unresolved `Tolerance = 0` candidate cannot be discovered by
the final reviewer and then set aside in the same round.

**Third — the package's own residual set is materially out of date.** Of the residuals I tested,
`FX08-R1` and `B05-R3` were both classified `C — NOT YET SEARCHED` and both yielded findings on a
single afternoon's search — one confirming the reference has a root-scoping concept it declines to
apply to the manual path, the other locating the elevation bypass on the ordinary online-payment
flow. A residual set that gives up two findings this cheaply has not been worked to the point where a
gate should rest on it.

### What would change my position

None of this requires new research at Wave scale. Specifically: correct `G02` §2.5 and its two
dependent statements to the evidence, with a declared boundary; boundary `G03` §5's "none" and restate
§7 at four scoping rules; reclassify `FX08-R1` and `B05-R3`; register `GR1-F-08` and `GR1-F-09` as
distinct `BW` cases; and run one targeted closure on `GR1-F-07` in the manner of `G04` — establishing
its callers, whether any can span two roots, and whether `ELSE 1` is tenant-reachable. With
`GR1-F-01` corrected and `GR1-F-07` either bounded or escalated, I would expect to arrive at a
different recommendation.

### Position

> **`REVIEWER 1 POSITION`**
>
> The four blockers' **central defects** are `CONFIRMED` and correctly evidenced: `FX-07` without
> qualification, `SB-05`, `FX-08` and `B-05` `CONFIRMED WITH CAVEAT`. The package's citation
> discipline is sound and its severity claims are, for once, not inflated.
>
> But one load-bearing `VERIFIED FACT` bounding the tenant-isolation blocker is `CONTRADICTED` by
> primary source; a second `Tolerance = 0` company-scoping crossing exists that the package has not
> found and that its own citation points directly at; and two residuals marked "not yet searched"
> gave up findings immediately on being searched.
>
> Under `Tolerance = 0` for tenant isolation and financial integrity, the gate cannot open on this
> evidence.

### Gate recommendation

> ## `RECOMMEND HOLD`

**Reasons, in order of weight:**

1. `GR1-F-01` — a `Tolerance = 0` closure's load-bearing limit is `CONTRADICTED` by
   `account/security/ir.model.access.csv:7`; the crossing is reachable by an accounting manager, not
   only a system administrator.
2. `GR1-F-07` — an unregistered `Tolerance = 0` candidate: cross-company rate resolution in raw SQL,
   outside every record rule, with an undeclared par fallback, at the exact file `G02` §2.7 cites.
3. `GR1-F-03` — four company-scoping rules govern one rate table, including an operator-precedence
   defect at `base/models/res_currency.py:403`; the package documents two.
4. `GR1-F-08`, `GR1-F-09` — two new `BALANCED BUT WRONG` cases (stale-own-rate precedence;
   anachronistic fallback with no date bound), neither registered.
5. `GR1-F-02`, `GR1-F-06` — two residuals classified `C — NOT YET SEARCHED` yielded findings on
   first search, indicating the residual set is not gate-ready.
6. `GR1-F-04` — `G03` §5's unbounded "none" is over-scoped; minor, but it is the same category of
   error as (1) and shows the pattern is not isolated.

**Nothing in this review is an approval.** The Boss is the sole Final Approver. No implementation is
proposed, no reference code, schema or architecture is proposed for copying, and no source under the
reference tree was modified.
