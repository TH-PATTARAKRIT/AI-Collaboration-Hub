# 24 — P02 THE EIGHT PREVIOUSLY UNCOVERED BUSINESS SCENARIOS

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-TARGETED-FORENSIC-CLOSURE-001`

Closes the eight gaps the first independent challenge identified (`16` CH-21…CH-24). Researched across
**both** source generations, because the mechanism changes between them.

## 0. Denominator

- **POPULATION** — both addon roots taken whole: v18 **797** module directories; v19 **1,427**.
- **PATTERN** — every negative in §10 is bounded by a literal command executed **separately against each
  root**. Module-existence questions were answered by directory tests, never inferred from imports.
- **UNIT** — the source construct (field, method, call site, data record). Never "a module", never "a
  finding".
- **Declared boundary** — source-tree facts. Deployed-data questions are marked as such and were answered
  separately in `22`.

**A tooling note that is itself a finding.** An unquoted include-glob in this shell silently returns
"no matches" rather than searching. One early sweep produced exactly that false zero. Every subsequent
search was re-issued quoted. **A negative from an unquoted glob is not a negative.**

## 1. Results

| # | Scenario | v18 | v19 | P02 disposition |
|---|---|---|---|---|
| **1** | **Drop-shipping** | Purpose-built entry, gated on the company boolean; two offsetting valuation layers; the invoice **also** adds a cost line, and the two net through the interim account | **No cost entry anywhere in the O2C leg** — excluded on three independent paths | **PEER — P01.** Cost recognition displaces entirely to the vendor bill, unlinked to the sale |
| **2** | **Credit control** | **Advisory only** — one comparison inside a message builder; no raise, no constraint, nothing in order confirmation or posting | **Identical (none).** Cosmetic refactor only | **P02 RETAINS** as a design gap |
| **3** | **Unrealised FX revaluation** | **Present**, Enterprise-licensed | **Present**, essentially identical | **PEER — P08** (close calendar), **P06** (realised half) |
| **4** | **Bill-and-hold** | No hold concept; representable only as invoice-on-order; cost falls back to standard price and credits the **interim** account | Same, but credits the **inventory account directly** | **PEER — P10** (cut-off) |
| **5** | **Outbound consignment** | **Not representable** — owner restriction models *inbound* third-party stock only | Same, plus one tightening | **P02 RETAINS** — it is a revenue-trigger question |
| **6** | **Warranty / return provision** | **Not found** | **Not found** | **PEER — P08.** Nothing automated exists to route |
| **7** | **Freight charges** | Revenue line; tax taken from the carrier's delivery product only | Same tax source; **income-account resolution changed** | **PEER — P07** (tax), **P08** (account) |
| **8** | **Lot/serial cost** | Layer-backed; stock and invoice read one source | **Divergence introduced** for `lot_valuated + standard` | **P02 RETAINS** as a v19 defect |

## 2. The Three Findings That Matter Most

**`FACT VERIFIED` — S-01 (DROP-SHIPPING, v19).** A dropshipped sale produces **no cost entry anywhere in
Order-to-Cash**. Three independent exclusions: the delivery gate requires the move to be inbound or
outbound and a dropship move is neither; the cost generator excludes any line whose moves are dropshipped;
and **the same predicate also suppresses the vendor-bill account redirect**. v18 had a purpose-built entry
for exactly this case. Detail and evidence in `22` §15.3.

**`FACT VERIFIED` — S-02 (CREDIT CONTROL, BOTH).** The entire enforcement surface is **one comparison
inside a string builder** that returns a translated message or an empty string. **It never raises.**
Searches for a blocking constraint were run separately against each full root under five distinct forms —
constraint decorators near the credit fields, raises near credit tokens, "credit limit" in raise text,
the order-confirmation body, and the posting bodies — and returned **zero** relevant rows in both
generations.

Worse, the warning is guarded on draft/sent status, so **it self-erases at the moment of confirmation or
posting** — absent precisely at the transition a gate would have to intercept.

**A defect inside the advisory itself, present in both generations, at four sites:** each compute opens
with a company-context call **whose return value is discarded**. Because the credit limit is a
company-dependent field, the limit actually read is the one resolved against the acting company, not the
document's. In a multi-company tenant the warning can be computed against the wrong company's limit.
Deployed consequence: `UNRESOLVED — EVIDENCE REQUIRED`.

**`FACT VERIFIED` — S-03 (OUTBOUND CONSIGNMENT, BOTH).** Not representable, and the reason is structural:
**valuation follows location, not ownership.** The owner-restriction machinery models *third-party stock in
your warehouse* — the inbound case. There is no way to keep your own stock valued while it sits somewhere
you do not control. The two available workarounds each break one half:

| Workaround | Valuation | Revenue trigger |
|---|---|---|
| Ship to a customer-usage location | **lost** — stock leaves valuation | fires on shipment, not on consumption |
| Model the customer's site as internal | **kept** — correct | **never fires** — consumption is invisible |

There is no third state in which goods are simultaneously on the seller's balance sheet and at the
customer's site with a consumption-triggered revenue event.

## 3. What P02 Hands Over

| To | Item |
|---|---|
| **P01** | Drop-shipped cost recognition on the v19 line — it is now entirely on the vendor bill. Determine the account, the date, and whether anything links it to the originating sale. |
| **P07** | Freight tax mechanics only: the tax on a freight line is whatever sits on the carrier's delivery product, company-filtered and fiscal-position-mapped; **the shipped data record leaves it unset**, so it inherits the company default sales tax; and the real-cost re-price writes price and description only and **does not re-run tax determination**. **No statutory conclusion drawn.** Note the standing P07 finding that zero/exempt VAT settles to a withholding group — that interaction is **unexamined for freight lines**. |
| **P08** | Unrealised-FX close calendar; the warranty/return provision absence, since nothing automated exists; and the v19 freight income-account resolution change. |
| **P10** | Bill-and-hold cut-off, plus a v19-only accrual override with no v18 counterpart. |
| **P06** | The realised-FX counterpart, which is never reversed. |
| **P03** | Confirm whether lot-valuated finished goods exist, for scenario 8. |

## 4. Negative Claims

Each is a statement about **what a stated search returned**, run separately against each full root.
`NO EVIDENCE FOUND != FUNCTION DOES NOT EXIST.`

| # | Claim | Scope |
|---|---|---|
| N-1 | No credit-limit hard block | Both full roots, five search forms: constraint decorators within 8 lines of the credit fields; raises within 6 lines of credit tokens; "credit limit" in raise text; onchange handlers; and the extracted order-confirmation and posting bodies. Zero relevant rows. |
| N-2 | No module named `*credit*` | Directory listing, both roots |
| N-3 | No sales-return or warranty provision | Both roots: the four sales/stock modules under `provision` → zero. Widened to the full root, the only accounting-logic occurrence is the FX revaluation provision. Plus four further token forms and a `warrant` directory test. |
| N-4 | No bill-and-hold representation | Both full roots under the phrase; both roots' sales/stock modules under four hold-token forms; and the picking status enumeration **read in full** in both — six values, none a hold |
| N-5 | No outbound-consignment mechanism | Directory listing plus a full-root content sweep; the returned hits were **read** and are a settings label, a visibility check, and test fixtures |
| N-6 | No freight cost account in the delivery modules | Both roots, delivery modules, nine account/valuation tokens → **exactly one hit per root**, and it is a customs-declaration value read from the *goods'* cost, not a posting |
| N-7 | The shipped delivery product record sets no tax | The data file **read in full** in both generations, not grepped |
| N-8 | No cron or period-close trigger for FX revaluation | Both roots' report data files; the only crons are report-send and, in v19, account-return generation |

**Explicitly left open rather than asserted:** the deployed population of lot-valuated standard-cost
real-time products (scenario 8), and whether any tenant sets differing per-company credit limits that
would expose the company-context defect (scenario 2). Both are `UNRESOLVED — EVIDENCE REQUIRED`.

## 5. Status

**Six of eight scenarios are answered and routed. Two are retained by P02 as design gaps** (credit control,
outbound consignment). **None is closed** — each is now analysed where before it had no analysis at all,
which moves `EC-01` but not `EC-04`.

The track's own recommendation is recorded unchanged: **three of the eight turn on negative claims whose
search boundaries are stated but have not been re-run in a second form by a party other than the author.**
