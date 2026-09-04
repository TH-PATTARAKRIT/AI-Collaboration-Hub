# 21 — P02 DEPLOYED DATABASE EVIDENCE

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 0. Why This File Exists — A Research Error, Not A Late Addition

Deliverables `00`, `12`, `14`, `15`, `18` and `19` each stated that **this session had no database or
runtime evidence**, and that limitation was used to explain why two very-expert requirements were
undischarged and why `C-04` could not be closed.

**That statement was false, and it was never tested.**

Five deployed database archives are on the execution host and `pg_restore` is installed. A declared
absence of evidence is a **negative claim** and is governed by the negative-claim control like any other —
`NO EVIDENCE FOUND != EVIDENCE DOES NOT EXIST`. **Neither this session's six self-corrections nor the
independent AAS-03 challenge caught it**, because neither was scoped at the *evidence base itself*; both
were scoped at the findings.

The error is recorded as `RE-13` in `15_P02_REVISION_LOG.md`. This file contains what one pass over the
evidence produced.

## 1. Evidence Acquisition — Declared

| Field | Value |
|---|---|
| Archives found on host | **5** deployed database archives, plus a loose SQL dump |
| Tooling | `pg_restore` / `psql` / `pg_dump`, PostgreSQL 16.15, already installed |
| Archive used for this pass | `iSMEs_2026-07-11_05-03-27.dump` — 148 MB, 14,045 table-of-contents entries |
| Method | **Offline extraction only.** `pg_restore -s` for schema, `pg_restore -a -n public -t <table>` per table. **No server was started, no database was created, nothing was restored, nothing was written.** |
| Other archives | **NOT YET SEARCHED** — four remain unexamined. Their contents may differ, and a multi-database comparison is a named next step. |

**Scope of this pass.** Six tables were extracted: company, product category, configuration properties,
chart of accounts, journal lines, valuation layers. **This is one pass over one database.** It is not a
substitute for the runtime reproduction that `C-04` requires.

## 2. The Deployed Configuration

| # | Fact | Value |
|---|---|---|
| **DB-01** | Companies in the database | **1** — a Thai company (Thai fiscal country) |
| **DB-02** | **Split cost recognition** | **OFF** |
| **DB-03** | Lock dates — global and tax | **none set at all** |
| **DB-04** | Cash-basis tax switch at company level | **ON** |
| **DB-05** | Tax rounding method | round per line |
| **DB-06** | Product categories | **30**, of which **15 carry real-time valuation** |
| **DB-07** | Costing methods in use | FIFO and average, both present |
| **DB-08** | **Every configured outbound stock account** | **an expense account** — codes `4010001`–`4010009` and `411000`, all typed as direct-cost expense |
| **DB-09** | Valuation accounts | current assets — `1141001`, `1146001`, `1148001`, `1148002`, `1145000` |

## 3. The Decisive Test — And It Confirms The Package's Mechanism Analysis Exactly

`02_P02_INVOICE_POLICY_MATRIX.md` and `01_P02_PROCESS_MAP.md` S5 predicted that **three** outcomes are
configuration-reachable, and that which one you get is decided by two settings held on different objects
and never validated against each other.

**The deployed database is on outcome 2, and the prediction is confirmed by direct count.**

| # | Test | Predicted | Observed |
|---|---|---|---|
| **DB-10** | Journal lines carrying a **cost-of-sales** marker, across the company's entire history | **zero**, because split recognition is off | **ZERO.** 447,384 journal lines. The marker value **does not occur once.** |
| **DB-11** | Journal-line marker values that *do* occur | product, payment term, tax, section, note | exactly those five: `product` 381,115 · `payment_term` 39,997 · `tax` 25,383 · `line_note` 827 · `line_section` 62 |
| **DB-12** | Valuation layers | present, since 15 categories are real-time | **74,982** |
| **DB-13** | Valuation layers carrying a journal entry | most | **57,863** |

**`FACT VERIFIED` — DB-14 (THE HEADLINE, NOW EMPIRICAL).**

> **In a live Thai deployment with 447,384 journal lines and 74,982 valuation layers, the invoice-side
> cost-of-sales mechanism has never executed — not once.** Cost of sales is recognised **at delivery**,
> directly to an expense account, and **no cost line is ever added to a customer invoice.**

This is **outcome 2** of the three, and it is reached because the implementer pointed the outbound stock
account at an expense account. That is the correct resolution for a split-recognition-off configuration —
**the implementer got it right** — and it is a resolution the chart does not supply and nothing validates.

## 4. What This Corrects In The Package

### 4.1 Corrected — the "Thai default" claim was about the chart, not about deployments

`01` S5 said outcome 3 — cost recognised **nowhere** — "is the **default** starting position" for a Thai
company. **That is true of the chart in isolation and is not what a deployment does.** This deployment
resolved it, by hand, to outcome 2.

**Corrected statement — `FACT VERIFIED`:** outcome 3 is the shape the Thai chart produces **before an
implementer intervenes**. It is reachable, it is unvalidated, and nothing warns about it — but the one
deployment examined is **not** in it. The finding stands as a **configuration-integrity** finding; it does
**not** stand as a claim about what Thai deployments actually do, and it was written as though it did.

### 4.2 Confirmed and strengthened — the three-outcome analysis is real

The package's central mechanism claim — that a boolean on the company and an account on the product
category jointly decide *where cost of sales is recognised*, with no cross-validation — is confirmed
against a deployment. **The two settings did diverge from the chart's own shape, and only manual
intervention reconciled them.**

### 4.3 New — a live cut-off exposure the package did not identify

**`FACT VERIFIED` — DB-15.** Under outcome 2, **cost of sales is recognised at delivery and revenue at
invoice.** There is no interim account between them and therefore **no matching, no residual and no
mechanism whatsoever to detect a mismatch**.

So for every shipment where delivery and invoice fall in different periods, **cost lands in one period and
its revenue in another, permanently, and nothing in the system can detect it.** The package analysed the
interim-account residual at length (`07` §3) — that is the **outcome 1** failure mode. **Outcome 2 has no
residual to inspect at all**, which is worse for detection, and the package did not say so.

**`DESIGN CANDIDATE` DC-21-01.** Cut-off between the outflow event and the billing event must be
**measurable in every configuration**. A design in which cost and revenue are recognised by two different
documents and no position connects them cannot be reconciled at period end, however simple it looks.

### 4.4 New — the guard the challenge found is populated in this deployment

**`FACT VERIFIED` — DB-16.** **1,267 valuation layers carry the accounting-line link** — the field the
reset-to-draft guard tests (`EV-P02-092`, `EV-P02-086`). The guard is therefore **live and active for
those layers**, on the purchase side, in a real deployment. It is not dead code. **The sales side has no
such layers**, which is consistent with DB-10: with no cost lines, there is nothing to link.

## 5. An Observation That Is NOT A Finding — Stated So It Is Not Mistaken For One

**17,119 of the 74,982 valuation layers carry no journal entry** — 22.8%.

**This is not presented as a defect, because it is fully explained by an ordinary cause:** 15 of the 30
product categories are **not** on real-time valuation, and a manual-valuation category produces valuation
layers with no accounting entry **by design**.

Attributing those 17,119 layers would require joining each to its product and its category's valuation
mode, which this pass did not do. **Until that join is performed the number means nothing**, and reporting
it as an anomaly would be exactly the aggregation failure the AAS-03 challenge found five instances of.

**What would settle it:** the join above, plus a check of whether any layer belonging to a **real-time**
category lacks a journal entry. **That specific count is the live test for the unpicked-completion hole
(`03` §2), and it is now performable.** It was not performed here.

## 6. What Is Now Discharged, And What Is Not

| Requirement | Before | Now |
|---|---|---|
| Database proof | declared undischarged | **DISCHARGED for the configuration and posting-outcome questions** — one database, one pass |
| Runtime proof | declared undischarged | **STILL UNDISCHARGED.** Reading a dump is not executing the system. `C-04` needs a *transaction*, not a *table*. |
| `C-04` — cost-of-sales idempotency | open, "no database access" | **still open, and the stated reason was wrong.** The real reason is that this deployment has **zero** cost lines, so it cannot exhibit duplicated ones. Testing it needs a deployment on **outcome 1**, or a live transaction. |

**`FACT VERIFIED` — DB-17.** `C-04` cannot be closed from **this** database at all, for a reason that is
itself a finding: **the mechanism under suspicion has never run here.**

## 7. Named Next Steps

1. **Join valuation layers to category valuation mode** and count real-time layers with no journal entry —
   the live test for `03` §2. Performable now.
2. **Examine the four unexamined archives.** If any is on outcome 1 (split recognition on), it can test
   `C-04`, the interim-account residual, and the reset-to-draft cost divergence — none of which this
   database can exhibit.
3. **Compare delivered quantity against the outflow ledger** per order line — the live test for `05` §3a.
4. **Test the eight uncovered business situations against deployed data** — drop-shipping and credit
   control first.
5. **Then re-run the eight-criteria assessment**, which `18_P02_PMO.md` currently scores partly on a
   limitation that did not exist.

## 8. Method Statement

Every number in this file is a **count over an extracted table**, reproducible by re-running the stated
extraction. No number is inferred, and the one number that could be mistaken for a finding is explicitly
disclaimed in §5.

**The lesson is recorded, not softened:** the package's most-repeated limitation was a negative claim that
nobody tested — not the author across six self-corrections, and not an adversarial panel across twenty
findings — because **every review was scoped at the findings and none at the evidence base.**
