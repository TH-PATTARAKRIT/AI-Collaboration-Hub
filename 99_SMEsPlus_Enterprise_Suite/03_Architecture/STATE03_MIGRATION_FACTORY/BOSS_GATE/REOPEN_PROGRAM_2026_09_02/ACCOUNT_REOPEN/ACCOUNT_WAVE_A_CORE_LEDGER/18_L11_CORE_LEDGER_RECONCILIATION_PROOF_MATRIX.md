> **SUPERSEDED BY CORR1.** This file is retained for lineage and is no longer the governing text.
> Governing text: `CORR1/C08_ACCOUNT_WAVE_A_L11_RECONCILIATION_RERUN.md` (session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`).
> Nothing below has been deleted or edited; read it as the state before correction.

# 18 — LEVEL 11: CORE LEDGER RECONCILIATION PROOF MATRIX

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

Each equation is stated, then tested against the Wave A evidence. **Every one of the seven required
equations needs additional semantic qualification** — none holds unconditionally as written.

Status: `HOLDS` · `HOLDS WITH QUALIFICATION` · `DOES NOT HOLD AS STATED` · `NOT PROVABLE`.

---

## P-01 — `Debit = Credit`

**Status: `DOES NOT HOLD AS STATED`.**

The equation is asserted by an application check that is **suppressible by a named context flag**,
and the entry carries **no database constraint** enforcing it (`COR-07`). Four *lesser* per-item
rules are genuine storage-level constraints, so the control tiering is inverted.

**Qualification required.** The equation holds for every entry created through a path that did not
suppress the check. It cannot be asserted of the stored data as a property.

**What SMEsPlus must add.** Storage-level enforcement, and a periodic proof over stored data rather
than trust in the write path. `T0-01`.

---

## P-02 — `GL → Trial Balance`

**Status: `HOLDS WITH QUALIFICATION`.**

The trial balance is an aggregation of items by account. It is arithmetically sound.

**Qualifications, all material:**
1. **Account merge** retargets posted items to a surviving account and deletes the original
   (`COR-08`). The trial balance re-foots correctly, but a prior-period trial balance is **not
   reproducible** after a merge — the account it named no longer exists.
2. **No temporal validity on accounts** (`GAP-A03`) means a type change restates prior-period
   classification retroactively.
3. **Off-balance accounts** must be excluded; exclusion semantics were not traced (Wave G).

---

## P-03 — `Opening + Movements = Closing`

**Status: `HOLDS WITH QUALIFICATION`.**

Arithmetically sound within a period.

**Qualifications:**
1. "Opening" is not a stored fact for any period except the first. It is a **re-aggregation from
   the beginning of time** for accounts whose type carries balances forward, and a **reset to zero**
   for those whose type does not (`EV-016`). The equation is therefore a restatement of the
   aggregation, not an independent check.
2. There is **no closing posting**, so "closing" is likewise derived (`EV-016`).
3. **Period membership is unstable.** An entry's accounting date can be moved by two independent
   mechanisms, one of which operates with no lock configured (`COR-02`). An entry can therefore leave
   the period a prior report attributed it to.
4. Generated entries — cash-basis tax, exchange reversals — can be dated into the current period
   although they arise from a prior one (`EV-015`).

**The equation holds; the periods it is stated over are not stable.** That is the finding.

---

## P-04 — `Subledger ↔ Control Account`

**Status: `NOT PROVABLE AS STATED` — the terms are not both defined.**

There is **no explicit control-account concept** in the reference model (`GAP-A01`). What exists is
an account *type* (receivable, payable) that forces reconcilability, and items on those accounts
carrying counterparties. The "subledger" is therefore a **view over the same items**, not a separate
ledger.

**Consequence — and this is a genuinely favourable one.** Because there is only one set of items,
subledger and control cannot disagree: they are the same data aggregated two ways. The classic
subledger-to-control break is **structurally impossible** here.

**But the qualification is real.** The equation as usually understood tests two independent records
against each other. Here there is one record, so the equation is a tautology rather than a proof, and
it provides no assurance. Assurance must come from elsewhere — from `P-06` and from provenance.

**What SMEsPlus must decide.** Whether to keep the single-record model (`ADAPT` — it eliminates a
whole class of failure) and accept that this check yields no information, or to introduce genuine
control accounts and with them the reconciliation burden. `RECOMMENDATION:` keep the single-record
model; do not manufacture a break in order to be able to check for it.

---

## P-05 — `Journal Entries ↔ Journal Items`

**Status: `HOLDS WITH QUALIFICATION`.**

Items belong to exactly one entry and are deleted with it.

**Qualifications:**
1. An entry may exist with **no substantive items** while draft; posting refuses it.
2. **Analytic lines are not items** — they are a derived subledger, destroyed on un-post and
   regenerated on repost (`EV-012`). Any equation that treats them as ledger records will not hold
   across a correction.
3. Item-level identity is positional; there is no stable business key (file 15).

---

## P-06 — `Reconciled + Residual = Original Open Item`

**Status: `DOES NOT HOLD AS STATED`.**

Nothing bounds the matched amount against the item's residual. The reconciliation record carries
**no database constraints at all** (`COR-09`), so the sum of matches against an item can exceed the
item. Over-reconciliation is structurally reachable **in any currency configuration** — not only in
multi-currency, which is how `EV-014` originally framed it.

Compounding qualifications:
1. Residual and the reconciled flag are **stored computed** values. If recomputation is missed they
   drift from the matching records, and **no reconstruction path was identified** (`GAP-E03`).
2. Matching records are **deleted silently** when an entry is reset to draft (`EV-012`), so the left
   side of the equation can vanish without the right side changing.

**This is the weakest equation in the set** and the one most in need of SMEsPlus enforcement.
`T0-05`.

---

## P-07 — `Company Currency ↔ Transaction Currency`

**Status: `HOLDS WITH QUALIFICATION` on sign; `DOES NOT HOLD` on magnitude.**

**What holds — and it is a genuine storage-level guarantee.** A database check requires the item's
balance and its transaction-currency amount to **share a sign** (`COR-06`). The transaction-currency
amount cannot be sign-flipped independently.

**What does not hold:**
1. **Magnitude is unconstrained.** No check ties the transaction-currency amount to the balance
   through a rate. On a secured entry the magnitude is neither write-guarded nor hash-detected
   (`CONTRA-01b`).
2. **A missing rate resolves to 1.0**, silently (`CONTRA-08`). The resulting entry satisfies the sign
   check, balances, and passes every other control — while asserting a measurement the business never
   agreed to. **This is the single most serious proof failure in Wave A**, because the corrupted
   entry is indistinguishable from a correct one.
3. The integrity hash serialises company-currency amounts at the **transaction** currency's decimal
   places (`CONTRA-06`), so the protection that does exist is weakened in exactly the multi-currency
   case.

---

## Summary

| # | Equation | Status |
|---|---|---|
| `P-01` | Debit = Credit | **`DOES NOT HOLD AS STATED`** — suppressible, no storage constraint |
| `P-02` | GL → Trial Balance | `HOLDS WITH QUALIFICATION` — not reproducible after a merge |
| `P-03` | Opening + Movements = Closing | `HOLDS WITH QUALIFICATION` — periods are not stable |
| `P-04` | Subledger ↔ Control | **`NOT PROVABLE`** — one record, so the check is a tautology |
| `P-05` | Entries ↔ Items | `HOLDS WITH QUALIFICATION` — analytic lines are not items |
| `P-06` | Reconciled + Residual = Original | **`DOES NOT HOLD AS STATED`** — unbounded |
| `P-07` | Company ↔ Transaction currency | sign `HOLDS`; magnitude **`DOES NOT HOLD`** |

## Core ledger readiness — Wave A assessment

The Boss instruction for this Level is to prove **core ledger readiness**. The honest result:

> Three of seven equations do not hold as stated, one is not provable, and the three that hold
> require qualifications that are themselves material findings. The reference core ledger is
> **arithmetically consistent** but **not self-proving**: its correctness depends on write paths
> having behaved, not on properties of the stored data.

`RECOMMENDATION:` SMEsPlus should require every one of these seven equations to be **provable from
stored data alone**, independently of the code that wrote it. That is the concrete definition of
"auditable ledger" for this programme, and it is the criterion Wave A proposes for the eventual
readiness gate.

## CHECKPOINT L11

| Item | Record |
|---|---|
| Scope completed | All seven required equations tested; readiness assessed |
| Verified findings | Three fail as stated; one is a tautology; three hold only with material qualification |
| Contradictions | `CONTRA-05`, `CONTRA-08`, `CONTRA-09` all surface here as proof failures |
| Unknowns | Reconstruction path for stored derived settlement values (`GAP-E03`) |
| Risks | The ledger's correctness is a property of its write paths, not of its data |
| Next research target | Level 12 — adversarial challenge consolidation |

`CHECKPOINT L11 RECORDED — CONTINUING AUTOMATICALLY.` Not Boss approval.
