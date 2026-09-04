# C05 — ACCOUNT_WAVE_A_SEVERE_FINDINGS_REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`

The five most severe findings, reconciled independently.

> **Severity rule applied.** Four of these five originated with independent reviewers rather than
> with the primary research team. **Severity has not been reduced on that account.** A finding's
> weight is a property of the evidence, not of who found it. Where this round *raised* a severity, it
> is because new evidence warranted it — `SF-01` and `SF-02` are both escalated below.

Assessment dimensions per the Boss instruction: accounting · data integrity · statutory · SaaS ·
migration · control · exploit or failure path · detectability · correction possibility · downstream Wave.

---

## `SF-01` — A missing exchange rate converts at 1:1, silently

**Origin:** Expert 3. **Parent ref:** `COR-14` / `CONTRA-08`. **Forensic:** `C06`.
**Severity this round: ESCALATED.**

| Dimension | Assessment |
|---|---|
| **Accounting** | Every foreign-currency amount is valued at par. Revenue, expense, assets and liabilities are misstated by the whole rate factor |
| **Data integrity** | The stored `balance` and `amount_currency` are permanently wrong; the non-stored rate is recomputed and will later disagree with them |
| **Statutory** | `HOLD / EVIDENCE REQUIRED` → `WAVE-D TAX`. The ledger implication is that filed figures derive from par valuations |
| **SaaS** | Per-tenant, arising at onboarding — i.e. it recurs for **every new tenant** rather than once |
| **Migration** | **Highest.** Opening balances loaded before rates are valued at par and then hard-locked by `MG-13` |
| **Control** | Defeats every control in the matrix; `IC-14` has no owner |
| **Failure path** | Activate a currency → post before entering a rate. No special privilege, no misconfiguration, no unusual sequence |
| **Detectability** | **Effectively none forward.** Retrospective only, via a displayed rate that no longer agrees with stored amounts |
| **Correction** | Amounts are frozen at posting. Correction requires reversal and re-entry of every affected document, after rates exist |
| **Downstream Wave** | Wave A owns the control; `WAVE-G` for restatement; `WAVE-D` for statutory consequence |

**Why escalated.** The parent treated this as a missing-configuration risk. `C06` establishes that
**shipped currency data contains zero rate records**, and rates ship only in demonstration data. Zero
rates is therefore the **production default state of every currency**, so the 1:1 path is reached by
following the product's own onboarding sequence. This moves the finding from "a misconfiguration can
cause it" to "the default state causes it".

**Position:** `REJECT` (`ST-27`). Proposed `Tolerance = 0` candidate `T0-02`.

---

## `SF-02` — The double-entry invariant is suppressible and has no storage constraint

**Origin:** Expert 2, independently Expert 4. **Parent ref:** `COR-07` / `CONTRA-05`.
**Severity this round: CONFIRMED, with the tiering argument strengthened.**

| Dimension | Assessment |
|---|---|
| **Accounting** | Debits need not equal credits. The defining rule of double entry is advisory |
| **Data integrity** | An unbalanced entry can be stored. The trial balance can fail to foot |
| **Statutory** | Any filing derived from an unbalanced ledger is unsupportable — `HOLD` for the statutory framing |
| **SaaS** | Per-tenant |
| **Migration** | High — bulk loads are exactly where multi-step construction suppresses the check |
| **Control** | `IC-01`. **Inverted tiering**: four lesser per-item rules are genuine database constraints while this one is not |
| **Failure path** | Any code path that sets the suppression flag. Whether that is reachable externally is `GAP-C04`, **still open** |
| **Detectability** | Detectable by an independent proof over stored data — which `C08` recommends and the reference does not perform |
| **Correction** | Correctable if detected; undetected, it propagates into every report |
| **Downstream Wave** | Wave A; `WAVE-G` for the proof |

**Position:** `EXTEND` (`ST-17`). Proposed `Tolerance = 0` candidate `T0-01`.
**`GAP-C04` remains the single most valuable open test in the programme** — it decides whether this
is an internal engineering risk or an externally reachable bypass.

---

## `SF-03` — The accounting date is system-derived, including with no lock configured

**Origin:** Expert 1, Expert 3, Expert 4 and the challenge unit, **independently**.
**Parent ref:** `COR-02` / `CONTRA-12`. **Forensic:** `C07`. **Severity this round: ESCALATED.**

| Dimension | Assessment |
|---|---|
| **Accounting** | Period attribution is derived, not asserted. Entries land in periods the user did not choose |
| **Data integrity** | The intended date is never stored, so relocation is undetectable afterwards |
| **Statutory** | **Highest exposure in the Wave.** The Thai extracts select and print by this field — `COR-20`. Consequence `HOLD` → `WAVE-D TAX` |
| **SaaS** | Per-tenant; universal, since it needs no configuration |
| **Migration** | High — migrated documents are re-dated on load |
| **Control** | No guard; the warning is hidden once posted |
| **Failure path** | Enter a vendor bill. That is the whole path |
| **Detectability** | **None after posting.** No trace is retained |
| **Correction** | Reversal and re-entry, which is itself re-dated |
| **Downstream Wave** | Wave A owns the carrier; `WAVE-D TAX` owns the statutory consequence; `WAVE-C AP` the process |

**Why escalated.** This session found a case none of the four reviewers reported: for a **current-month**
non-sale document the derivation returns **today**, not the document date (`C07` §2, consequence B).
The behaviour is therefore not confined to late entry — it applies to ordinary same-month processing.

**Position:** `REJECT` the numbering-driven rule (`ST-22`); `REJECT` silent relocation (`ST-23`);
require an explicit tax point and retained intent (`DT-01`, `DT-03`). Boss decision `CL-04`.

---

## `SF-04` — Account merge rewrites posted history past the ledger's own guards

**Origin:** Expert 1 and Expert 2. **Parent ref:** `COR-08` / `CONTRA-03`.
**Severity this round: CONFIRMED.**

| Dimension | Assessment |
|---|---|
| **Accounting** | Posted items are retargeted to a different account. Prior-period reports are not reproducible |
| **Data integrity** | The predecessor row is deleted by direct statement, so the model's own deletion guards — including the one forbidding deletion of an account holding journal items — do not run |
| **Statutory** | Audit trail broken for any period spanning the merge — `HOLD` for the statutory framing |
| **SaaS** | Per-tenant |
| **Migration** | High — chart consolidation during migration is exactly when merges occur |
| **Control** | **None.** No approval, no log, no tracking, no inverse |
| **Failure path** | One accounting manager, one action |
| **Detectability** | **None.** The wizard writes no record of any kind |
| **Correction** | **None within the application** |
| **Downstream Wave** | Wave A |

**Position:** `REJECT` (`ST-26`). Replacement must be a forward-dated succession relationship.
Proposed `Tolerance = 0` candidate `T0-03`.

---

## `SF-05` — Integrity hashing is partial, precision-blind, and cannot survive migration

**Origin:** the challenge unit (`COR-11`, `COR-12`), Expert 2 (`COR-06`).
**Parent ref:** `CONTRA-01a`/`01b`, `CONTRA-06`, `CONTRA-07`. **Severity this round: CONFIRMED.**

Three defects that compound:

| Defect | Effect |
|---|---|
| Coverage | The transaction-currency amount, the currency, tax fields, the analytic distribution and the due date are **neither write-guarded nor detected** |
| Precision | Company-currency amounts are serialised at the **foreign** currency's decimal places — a collision on materially different amounts |
| Keying | The chain keys on **database row identifiers**, so it cannot survive migration, restore, or tenant split or merge |

| Dimension | Assessment |
|---|---|
| **Accounting** | "Secured" asserts an integrity guarantee the mechanism does not provide in multi-currency |
| **Data integrity** | Undetectable post-hoc modification of monetary and dimensional fields |
| **Statutory** | Where hashing is relied on as tamper-evidence for filing purposes — `HOLD` → `WAVE-D TAX` |
| **SaaS** | `SB-03`: assurance cannot cross a tenancy boundary |
| **Migration** | **Highest for this finding** — assurance is lost precisely when most needed |
| **Control** | `IC-09`, `IC-10`; and the mechanism is opt-in, defaulting off, fixed at first posting |
| **Failure path** | Edit an unhashed field on a secured entry |
| **Detectability** | Coverage defect: none. Precision defect: none. Keying defect: visible as a wholesale chain failure after migration |
| **Correction** | Re-hashing after correction is possible but attests only the corrected state |
| **Downstream Wave** | Wave A |

**Position:** `EXTEND` (`ST-13`) — full-field coverage, correct precision, keyed on business identity.

---

## Cross-cutting observation

Four of the five share one property: **the failure produces a record that satisfies every control.**
`SF-01`, `SF-03`, `SF-04` and `SF-05` are all silent. Only `SF-02` produces an artefact that a proof
over stored data would catch.

`INFERENCE:` this is the defining risk characteristic of the domain and should shape the SMEsPlus
control strategy — the priority is not more guards on the write path, but **independent proofs over
stored data** that do not trust the write path at all. That principle governs the Level 11 re-run
(`C08`).

## Severity ranking for the gate

| Rank | Finding | Basis |
|---|---|---|
| 1 | `SF-01` | reachable from the shipped default state; silent; irreversible once posted |
| 2 | `SF-03` | universal, needs no configuration, silent, statutory exposure |
| 3 | `SF-02` | defeats the defining accounting invariant; reachability still open (`GAP-C04`) |
| 4 | `SF-04` | total absence of control, but requires a deliberate act |
| 5 | `SF-05` | severe where relied upon; the mechanism is off by default |
