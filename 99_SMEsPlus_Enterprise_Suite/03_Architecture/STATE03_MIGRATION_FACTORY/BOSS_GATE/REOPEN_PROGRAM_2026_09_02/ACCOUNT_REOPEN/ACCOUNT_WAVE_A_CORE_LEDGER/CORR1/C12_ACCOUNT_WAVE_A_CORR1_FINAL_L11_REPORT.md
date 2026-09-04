# C12 — ACCOUNT_WAVE_A_CORR1_FINAL_L11_REPORT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · **supersedes `C08`, which superseded file `18`**

Final Level 11 proof, re-run after the fresh L12 review and all verified corrections.

Status: `HOLDS` · `HOLDS WITH QUALIFICATION` · `DOES NOT HOLD AS STATED` · `NOT PROVABLE`.

---

## Part 1 — The seven equations, final

| # | Equation | Status | Change from `C08` |
|---|---|---|---|
| `P-01` | `Debit = Credit` | **`DOES NOT HOLD AS STATED`** | **worse** — the suppression flag is now established as externally reachable (`C09`) |
| `P-02` | `GL → Trial Balance` | `HOLDS WITH QUALIFICATION` | unchanged |
| `P-03` | `Opening + Movements = Closing` | `HOLDS WITH QUALIFICATION` | **narrowed** — the re-dating population is smaller than `C08` assumed (`A2-03`), but still needs no lock |
| `P-04` | `Subledger ↔ Control Account` | **`NOT PROVABLE`** | unchanged in substance; the package's own inconsistency corrected (`B-07`) |
| `P-05` | `Journal Entries ↔ Journal Items` | `HOLDS WITH QUALIFICATION` | unchanged |
| `P-06` | `Reconciled + Residual = Original` | **`DOES NOT HOLD AS STATED`** | unchanged |
| `P-07` | `Company ↔ Transaction Currency` | sign `HOLDS`; magnitude **`DOES NOT HOLD`** | **worse** — trigger condition widened (`A1-04`); detection signal withdrawn (`A1-01`) |

### `P-01` — final basis

The balanced-entry assertion is a suppressible application check with no database constraint, while
four lesser per-item rules are genuine constraints. `C09` establishes from the dispatch layer that
the suppression key is applied from a **client-supplied context with no filtering**, gated only by
the called method not being private. `write` and `create` are public.

**The invariant is therefore addressable by any authenticated user who may write an entry.**

### `P-03` — final basis, narrowed

`C08` stated that period membership is unstable "by default, in every tenant". `A2-03` narrows the
population: the unconditional re-dating path applies to **non-sale invoices and refunds whose journal
numbering resets by period**. Journals with non-resetting numbering return the document date
unchanged, and documents dated today or later are not moved.

**The qualification survives**, because the narrowed population — vendor bills in a monthly-numbered
purchase journal, entered after their month — is a default configuration and an ordinary workflow.
The word "every" is withdrawn; the finding is not.

### `P-07` — final basis, worse

Three changes, all adverse:

1. **Trigger widened.** Par conversion occurs when no rate row **with a non-empty value** exists —
   not merely when no row exists. The rate field carries no `required` (`A1-04`).
2. **Detection removed.** For invoices and bills the displayed rate is read from the **stored**
   document rate, so par valuation and par display remain mutually consistent indefinitely. The
   single detection signal `C08` relied on **does not exist for the affected population** (`A1-01`).
3. **Compensating control possibly contaminated.** A revaluation mechanism exists (`NC-19`) but may
   resolve rates through the same fallback (`FX-07`, open).

---

## Part 2 — `BALANCED BUT WRONG` register, final

`C08` identified twelve cases. The fresh review confirmed the register's construction, corrected two
entries, and added three.

| # | Case | Status after review | Detectable? |
|---|---|---|---|
| `BW-01` | Wrong FX — par valuation | **worse** — trigger widened; **no detection at all for invoices and bills** | **No** |
| `BW-02` | Wrong period — derived date | **narrowed population**, still needs no lock | No |
| `BW-03` | Wrong period — generated consequence relocated | unchanged | Partially |
| `BW-04` | Wrong account — retroactive merge | unchanged | No |
| `BW-05` | Wrong classification — retroactive type change | unchanged | Partially |
| `BW-06` | Duplicate event — machine-generated | **corrected**: a detector exists but covers only sale and purchase documents, warns rather than blocks, and (reported, `NOT YET SEARCHED`) may be year-scoped | Partially, for a narrow population |
| `BW-07` | Over-settlement | unchanged | Partially |
| `BW-08` | Broken source linkage | **corrected**: typed origin links exist for specific generated entries; no general carrier | No, generally |
| `BW-09` | Silent tamper on a secured entry | **narrowed**: tax fields and due date **are** field-tracked; evidence-free set is `amount_currency`, `currency_id`, `analytic_distribution`, reconciliation fields | No, for that set |
| `BW-10` | Hash collision on rounding precision | unchanged | No |
| `BW-11` | Unbalanced entry stored | **worse** — externally reachable | Yes, by a proof over stored data |
| `BW-12` | Cross-tenant control state | unchanged | No |
| `BW-13` | **NEW** — duplicate **manual journal entry**: the duplicate detector never runs on `entry`-type moves | `VERIFIED` | **No** |
| `BW-14` | **NEW** — a **null-company rate re-measures another tenant's postings** | `PARTIALLY VERIFIED` — the resolver accepts null-company rows; whether they arise is open (`SB-05`) | **No** |
| `BW-15` | **NEW** — same bank transaction ingested by two routes with disjoint keys | `NOT PROVEN` (`NOT YET SEARCHED`) | Unknown |

**Fifteen cases. Thirteen are undetectable by the equation set.** Only `BW-11` is caught by a proof
over stored data, and `BW-06` partially by an existing warning.

---

## Part 3 — Final readiness assessment

| Measure | Parent file 18 | `C08` | **Final** |
|---|---|---|---|
| Equations holding unconditionally | 0 of 7 | 0 of 7 | **0 of 7** |
| Holding with qualification | 3 | 3 | 3 |
| Failing as stated | 3 | 3 | 3 |
| Not provable | 1 | 1 | 1 |
| Balanced-but-wrong cases | not assessed | 12 | **15** |
| Undetectable by the equation set | — | 11 | **13** |

The conclusion is unchanged in direction and firmer in evidence:

> The seven equations test **internal consistency**. Every material failure found in Wave A is a
> failure of **external correspondence** — to a real measurement, a real period, a real account, a
> real distinct event, a real source document, a real tenant boundary. A ledger can satisfy all seven
> equations and be wrong in thirteen identified ways.

### Proposed readiness criterion — final form

1. **Every equation provable from stored data alone**, independently of the code that wrote it.
2. **Every fact traceable to an external correspondent** — a measurement the business agreed, a
   period it asserted, a distinct source event, a classification that existed at the time.
3. **No accounting invariant expressible as a request parameter** — added on the strength of `C09`.

Criterion 1 addresses `BW-11`. Criterion 2 addresses eleven of the remaining fourteen. Criterion 3
addresses the mechanism by which criterion 1 can be defeated at the point of writing.

`RECOMMENDATION:` this three-part criterion should be the standard the eventual readiness gate
applies. It is offered for Boss decision and is not adopted by this session.
