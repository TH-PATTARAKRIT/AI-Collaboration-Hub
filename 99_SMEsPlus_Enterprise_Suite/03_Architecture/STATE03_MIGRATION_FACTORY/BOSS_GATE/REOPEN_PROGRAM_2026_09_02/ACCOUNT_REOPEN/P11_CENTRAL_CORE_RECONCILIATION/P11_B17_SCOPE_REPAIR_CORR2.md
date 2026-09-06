# P11 — `B-17` SCOPE REPAIR (R1)

`[SMEPLUS-26-09-06-…-CORR2-PHASES-001]` · `CP-P11C2-02` · **PHASE S** · Layer 1 clean-room

> **The defect being repaired.** P11's subledger re-run failed criterion `S3` — *"detail is immutable
> once posted"* — for five of seven structures on **one** statement, and attributed it to *"`P08` over
> the declared 22-root set"*. That statement is a **source-line 18.0** finding. `P08` `52_…_V2`
> forbids the crossing in terms: *"Every `P08` source statement is 18.0; every deployed count is 16.0
> or 19.0. **No deployed database matches the source line.** Any peer combining the two as one fact
> must re-read it as two facts with two scopes."*
>
> **Nothing below is deleted. The prior B-17 history is preserved verbatim in
> `P11_SUBLEDGER_RERUN_B17.md` and `P11_BLOCKER_REGISTER_CORR1.md`.**

---

## 1. The one fact, split into two

| | **`S3-SRC`** | **`S3-DEP`** |
|---|---|---|
| **Statement** | The reference source, series 18.0, permits mutation of posted journal-item detail | Posted journal-item detail **is** mutable in the deployed estate |
| **Scope** | `SOURCE LINE — 18.0` | `DEPLOYED ESTATE — 16.0 / 18.0 / 19.0` |
| **Who may assert it** | `P08` (source reader) | any peer with deployed evidence |
| **What it can support** | a claim about what the product **permits** | a claim about what the estate **is** |
| **What it may NOT support** | any statement about a deployed database | any statement about product design intent |

**The cross-scope inference P11 made and now removes:** `S3-SRC` was used to conclude `S3-DEP`.
**Deleted, not softened.** No P11 register row may reach a deployed-estate conclusion from `S3-SRC`.

## 2. `S3-SRC` — evidence, restated inside its own scope

| Item | Status |
|---|---|
| Nine header attributes protected; protection **waived by a caller-supplied parameter** | `FACT VERIFIED — SOURCE LINE 18.0` (`P08`) |
| A posted item's account, counterparty, label, reference and allocation **editable in place** | `FACT VERIFIED — SOURCE LINE 18.0` (`P08`) |
| Entry substance while posted guarded at application level, **seven production bypass sites** | `FACT VERIFIED — SOURCE LINE 18.0` (P11 `X2-F07`) |

> **`S3-SRC` stands, unchanged, and now says only what it can say.** It fails `S3` **for the 18.0
> source line**. It does not reach any deployed database, including the series-18 deployment `P01`
> discovered after this was written.

## 3. `S3-DEP` — and it is now independently established, by two peers, without `P08`'s source line

This evidence **did not exist at CORR1**. It arrives with the CORR2 frozen snapshot.

| # | Deployed-estate evidence | Owner | Class |
|---|---|---|---|
| 1 | **`stock_valuation_layer_account_move_id_fkey FOREIGN KEY (account_move_id) REFERENCES public.account_move(id) ON DELETE SET NULL`** — schema-verified, with controls in the same schema (584 `ON DELETE CASCADE`, 1,741 `ON DELETE SET NULL`) | `P01` `S16-B-05` @ `b820b29` | `FACT VERIFIED — DEPLOYED SCHEMA` |
| 2 | **`om_data_remove 16.0.1.0.1` is INSTALLED** and performs raw `DELETE FROM <table>` + `commit()` — *"no ORM, no lock-date check, no company filter, no log"*; **10 of 20 destructive buttons carry no confirmation** | `P01` `S16-B-05` | `FACT VERIFIED — DEPLOYED` |
| 3 | The same module, independently: **`DESTRUCTIVE PATH VERIFIED` · `NO SERVER-SIDE AUTHORIZATION VERIFIED` · `REACHABLE — DEPLOYMENT VERIFIED`** on an Odoo 19 database in this estate; **17 copies**, three rebranded | `P06` `70_` @ `249b7c2` | `FACT VERIFIED — DEPLOYED` |
| 4 | **No lock date is set on any of the archive's three locking surfaces**, over **169,143 posted entries** — `res_company` (3 fields NULL) + `account_change_lock_date` (**0 rows**) + `account_fiscal_year` (4 rows, boundaries not locks) | `P01` @ `b820b29` | `FACT VERIFIED — DEPLOYED` |
| 5 | **0 of 6 transacting companies** set a close; close is a date comparison, not an object | `P08` `58_` @ `194efcb` | `FACT VERIFIED — DEPLOYED` |

> ### `S3-DEP` = **FAILED**, on deployed evidence alone, from two independent peers, with a schema
> read and an installed-module read — **not one line of it borrowed from the 18.0 source statement.**

**This is a stronger result than the one it replaces**, and it is the correct direction: the repair was
required because the evidence was mis-scoped, and re-scoping it found better evidence, in the right
scope, that P11 already had a route to and had not used.

## 4. The re-run's verdicts, re-derived under the two-scope reading

| Structure | Verdict at CORR1 (mis-scoped) | **Verdict under `S3-DEP`** | Changed? |
|---|---|---|---|
| AR | derived view | **derived view** | no |
| AP | derived view | **derived view** | no |
| Bank | derived view | **derived view** | no |
| Tax | derived view | **derived view** | no |
| Settlement | derived view | **derived view** | no |
| Inventory / valuation | derived view | **derived view — and now with a named mechanism** (§3 item 1) | strengthened |
| Asset | qualified | **qualified** | no |
| Of record, unqualified | **0** | **0** | no |

> **The count does not move. The warrant does.** Every verdict that rested on a source-line statement
> now rests on deployed evidence, and the one structure whose failure was weakest — inventory
> valuation — is now the best-evidenced of the seven, because the deletion path that severs its link
> to the ledger is **schema-verified and installed**.

## 5. What is deliberately **not** claimed

- **Not** that the deletion path has fired in any specific database. `P01`: *"No evidence the module
  ran in the series-16 deployment"*, **with the stated limit** that two target tables are empty and
  *"the module leaves no trace by design"*.
- **Not** that `S3-SRC` and `S3-DEP` corroborate each other. They are two facts in two scopes; each
  stands on its own evidence. **Agreement between them is not additional evidence for either.**
- **Not** that any structure has been re-tested by P11 against a database. P11 performed **no**
  extraction; every deployed fact above is **received from its owner and attributed**.

## 6. Disposition

| Item | Disposition |
|---|---|
| `S3-SRC` | `FACT VERIFIED — CLOSED FOR CURRENT P11 EVIDENCE` — bounded to the 18.0 source line |
| `S3-DEP` | `FACT VERIFIED — CLOSED FOR CURRENT P11 EVIDENCE` — deployed estate, two independent peers |
| The cross-scope inference | **`CONTRADICTED — CORRECTED AND CLOSED`** |
| **`P11-B-17`** | **`CONTRADICTED — CORRECTED AND CLOSED`.** The blocker was *"a stated rule that was not the rule applied"*, compounded by a scope crossing. The rule is now applied as stated, in the correct scope, on evidence that survives the crossing being removed |

> **`B-17` closes for the second time, and this time the input is in the scope its owner permits.**
> The first closure was withdrawn by P11's own commissioned challenge within the hour. **This one is
> submitted to a fresh challenge before it is relied on** (`CP-P11C2-11`), which is the control the
> first closure did not get.

**`CP-P11C2-02` — COMPLETE — EVIDENCE VERIFIED.**
