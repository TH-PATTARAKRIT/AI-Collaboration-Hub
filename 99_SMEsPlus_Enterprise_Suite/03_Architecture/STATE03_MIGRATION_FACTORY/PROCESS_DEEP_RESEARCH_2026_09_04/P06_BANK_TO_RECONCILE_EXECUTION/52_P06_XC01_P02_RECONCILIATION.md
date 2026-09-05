# P06_XC01_P02_RECONCILIATION.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S14)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Constraint observed:** *"P06 must not decide P02 architecture."*

---

## 1. The authoritative contradiction, retrieved not inferred

`P06-XC-01`, as recorded in `11_P06_CONTRADICTION_REGISTER.md` Appendix B.3:
> **P02 `P02-F-43` (`FACT VERIFIED`): the four states *are* kept separate "and does it well". P06 headline (i): they are not independent.**

---

## 2. The two positions, verbatim

**P02** — `09_P02_PAYMENT_RECONCILIATION_MATRIX.md` §1:
> **`FACT VERIFIED` — P02-F-43.** The reference process **does** keep these separate, and does it well. Registering a payment executes three separable steps — create, post, then match — and the matching step is the one that changes the receivable's residual (T2 §1). **This separation must be preserved in SMEsPlus.** Collapsing "the customer paid" into "the bank balance changed" destroys bank reconciliation and is the most common SME-ERP failure.

**P06** — headline (i): the four states are not independent, and no field means "the bank confirmed this".

---

## 3. The decisive fact: P02 publishes the qualification itself, in the next section

`09_P02_PAYMENT_RECONCILIATION_MATRIX.md` **§2, titled "The Configuration That Breaks It"**:
> **`FACT VERIFIED` — P02-F-44 (SURPRISE, T2-S3).** **A payment may post no journal entry at all.** Entry generation is filtered to payments that have an outstanding account, and an outstanding account is force-assigned **only when the full-accounting module is absent**.
> So the canonical "outstanding receipts then bank" narrative describes the **invoicing-only** configuration. In the full-accounting configuration a payment may be booked **directly against the bank account**, in which case:
> - the intermediate state disappears entirely — the payment is declared matched at creation;
> - the "money received but not yet cleared" position **does not exist**;
> - bank reconciliation has nothing to reconcile.

And `T2_PAYMENT_RECONCILIATION_EVIDENCE.md` §5, `SUPPORTED INTERPRETATION`:
> **In-payment is specifically the outstanding-account configuration's intermediate state.**

**XC-F-01 — There is no evidentiary disagreement. There is a headline that omits its own qualification.**
P02 states the separation works **and** that a configuration removes it. P06 states the separation does not hold **because** of that configuration. **Both packages describe the same mechanism and reached the same understanding.** What differs is which half each promoted to a headline.

---

## 4. Evidence-base comparison

| | P02 | P06 |
|---|---|---|
| Cited range | `account/models/account_payment.py:428-456`, markers `:437 :440 :443 :446-449 :451` | `:436-455` (round 3), **`:433-455` re-executed at round 4** |
| Branch count published | **four** | **three** (`25_`) / four (`35_`) — **inconsistent** |
| **Re-executed at this round** | — | **four top-level branches, five assignment sites** |
| Additional evidence | `:1002` entry generation filtered on outstanding account; `chart_template.py:842` | dispatch and state-machine trace |

**XC-F-02 — P06's own package was internally inconsistent, and P02 was right about the count.**
`25_` said three; `35_` said four; P02 said four. Source re-execution at this round gives **four top-level branches (`:436`, `:439`, `:442`, `:445`) and five assignment sites**. `25_` had silently omitted `:439-441`.
**Corrected in both files. Recorded as REV-E-11.** The comparison that exposed it was a peer's citation against this package's own — **P06 did not catch this by re-reading itself.**

**The correction strengthens P06's finding.** Of five assignment sites: two set `is_matched = True` **unconditionally with no statement** (`:444` zero-amount, `:450` journal-default configuration), one sets it **circularly** from the payment's own state (`:438`), one always False, and **only `:452` tests anything resembling a bank match.**

---

## 5. The reconciliation P06 proposes

> **The separation of payment / posting / bank-confirmation / settlement is REAL and WORKS in the outstanding-account configuration. It COLLAPSES AT CREATION in the direct-to-bank configuration, where the payment is declared matched before any bank event exists.**
> **It is therefore a configuration-dependent property, not a system property. A design may not rely on it without mandating the configuration — which is precisely what P02's own `DC-09-01` requires:** *"In SMEsPlus the outstanding/undeposited position must be **structural and non-optional**."*

**XC-F-03 — P02's design candidate already concedes P06's point.** `DC-09-01` says the position must be *non-optional* — which is only necessary if it is currently optional. **The two packages agree on the remedy and disagree only on how the present state was headlined.**

---

## 6. Classification

**`P06-XC-01`: `BOTH PARTIAL` — and, more precisely, `CONFIGURATION-DEPENDENT`.**

- **P02 CONFIRMED** for the outstanding-account configuration.
- **P06 CONFIRMED** for the direct-to-bank configuration and for the absence of a bank-confirmation *field* in either.
- **Neither headline is correct unconditionally**, and each package contains the evidence that qualifies its own.

**This is not a defect in either package's research.** It is a defect in two headlines, and it is exactly the class of thing a cross-process reconciliation exists to catch.

**P06 does not decide P02's architecture and does not ask P02 to withdraw `P02-F-43`.** What P06 asks is that the finding travel with its qualification, because `P02-F-43` currently reads as an unqualified `FACT VERIFIED` and **P11 will consume it that way.**

---

## 7. Routed to P11

**`P11 DECISION REQUIRED`** — and the routing note matters:

`P11_CONTRADICTION_REGISTER.md` runs `P11-C-01` … `P11-C-07` with **no row for this**, because P11 ingested P02 and P06 in separate deltas and did not cross-read them. An independent sweep of all nine peer branches at this round confirms **no peer package carries a row for it either**.

**P06 raises it as candidate `P11-C-08`** with:
1. both positions verbatim;
2. the shared source range and the corrected branch count;
3. the proposed reconciliation in §5;
4. the observation that **both packages' design candidates already converge** (P02 `DC-09-01`, P06 `PSM-R-03`).

**Estimated reconciliation cost: LOW.** No new evidence is required. It is a wording decision on two headlines.

---

## 8. Open items

| ID | Item | Class |
|---|---|---|
| `P06-OQ-107` | Whether P02 will qualify `P02-F-43` in its own package, or whether P11 records the qualification centrally. **P02's decision, not P06's.** | — |
| `P06-OQ-108` | P02 cites `account_payment.py:1002` and `chart_template.py:842` for the force-assignment condition; P06 has not independently verified those two lines. | C |
