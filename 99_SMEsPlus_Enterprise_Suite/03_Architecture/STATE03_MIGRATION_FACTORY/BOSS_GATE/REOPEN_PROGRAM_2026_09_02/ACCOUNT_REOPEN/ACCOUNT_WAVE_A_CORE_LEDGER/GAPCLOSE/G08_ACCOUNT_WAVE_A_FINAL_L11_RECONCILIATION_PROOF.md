# G08 — FINAL L11 RECONCILIATION PROOF (DELTA)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · **supersedes `C12`, which superseded `C08` and file `18`**

Delta re-run: only the equations and cases the four closures touched.

---

## 1. Equations — final

| # | Equation | `C12` | **Final** | Change |
|---|---|---|---|---|
| `P-01` | `Debit = Credit` | fails as stated | **fails as stated** | unchanged |
| `P-02` | `GL → Trial Balance` | holds with qualification | **holds with qualification** | unchanged |
| `P-03` | `Opening + Movements = Closing` | holds with qualification | **holds with qualification** | unchanged |
| `P-04` | `Subledger ↔ Control` | not provable | **not provable** | wording corrected per `RS`/`B-07`; substance unchanged |
| `P-05` | `Entries ↔ Items` | holds with qualification | **holds with qualification** | unchanged |
| `P-06` | `Reconciled + Residual = Original` | fails as stated | **fails as stated** | unchanged |
| `P-07` | `Company ↔ Transaction Currency` | sign holds; magnitude fails | **sign holds; magnitude fails — and now for three distinct reasons** | **worse** |

### `P-07` — final basis

The magnitude relationship between an item's transaction-currency amount and its company-currency
balance can be wrong through **three independently verified paths**:

1. **No usable rate** → resolver returns `1.0` (`C06`, widened by `A1-04` to "no rate row with a
   non-empty value").
2. **Rate written at branch level** → resolver reads the root, does not match it, falls through to an
   unrelated rate or par (`G03`).
3. **Rate scoped to no company** → another company's rate is used (`G02`).

And the control that should detect all three — periodic revaluation — **resolves through the same
path and guards only against zero** (`G04`), so it reports no adjustment required.

> `P-07` is the only equation in the set whose failure is now shown to be **both undetectable and
> uncorrectable without reversal**.

## 2. `BALANCED BUT WRONG` — final register

`C12` held 15 cases. This round adds two and re-rates one.

| # | Case | Status | Detectable? |
|---|---|---|---|
| `BW-01` | Wrong FX — par valuation, no rate | **worse** — trigger widened; no detection for invoices and bills; **revaluation control confirmed contaminated** | **No** |
| `BW-02` … `BW-15` | as recorded in `C12` | unchanged | as recorded |
| `BW-16` | **NEW** — **wrong FX from a branch-scoped rate.** A rate exists and was deliberately maintained, but is invisible to the resolver | `VERIFIED` (`G03`) | **No — and the rate table shows rates are loaded, which actively misleads** |
| `BW-17` | **NEW** — **wrong FX from another company's global rate.** A null-company rate measures a company that has none of its own | `VERIFIED` (`G02`) | **No — indistinguishable at the point of use from the company's own rate** |

**Seventeen cases. Fifteen are undetectable by the equation set.**

`BW-16` is the most insidious in the register: every other case arises from something absent;
`BW-16` arises from something **present and correct that the system does not read.**

## 3. Readiness criterion — final form

Unchanged from `C12` in structure; the third clause is reinforced by `G05`, and a fourth is added by
this round.

1. **Every equation provable from stored data alone**, independently of the code that wrote it.
2. **Every fact traceable to an external correspondent** — a measurement the business agreed, a
   period it asserted, a distinct source event, a classification that existed at the time.
3. **No accounting invariant expressible as a request parameter**, and no authorisation attached to a
   UI action rather than to the fact (`C09`, `G05`).
4. **NEW — every fact scoped by exactly one owning boundary, applied identically by every writer and
   every reader** (`TI-07`, from `G02` and `G03`).

Clause 4 is the one this round earned. Two of the three verified boundary crossings, and the entire
`BW-16` case, exist because a single fact is scoped one way when written and another when read.

## 4. Position

> **0 of 7 equations hold unconditionally.** Three fail as stated, one is not provable, three hold
> only with material qualification, and **17 balanced-but-wrong cases satisfy the full equation set,
> 15 of them undetectably.**

The core ledger is arithmetically consistent and **not self-proving**. That conclusion has now
survived three adversarial rounds and has strengthened at each one.
