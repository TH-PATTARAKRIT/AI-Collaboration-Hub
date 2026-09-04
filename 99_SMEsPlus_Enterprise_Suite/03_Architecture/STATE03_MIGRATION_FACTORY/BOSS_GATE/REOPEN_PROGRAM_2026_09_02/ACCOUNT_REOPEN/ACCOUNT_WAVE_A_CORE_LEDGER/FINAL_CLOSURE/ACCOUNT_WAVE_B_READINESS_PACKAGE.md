# ACCOUNT WAVE B — READINESS PACKAGE (`AR / REVENUE`)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Prepared, **not executed**. Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001`.

> # `WAVE B STATUS: NOT STARTED`
> **Wave B must not open until Boss passes the Wave A Final Research Gate.**
> Nothing in this file authorises execution.

---

## 1. Scope boundary

### In scope
| Area | Detail |
|---|---|
| **AR documents** | `out_invoice` (Customer Invoice), `out_refund` (Customer Credit Note), `out_receipt` (Sales Receipt) — **3 of the 7 `move_type` values** |
| **Customer master** | partner as customer; receivable account assignment; payment terms; credit data |
| **Revenue recognition** | invoice → revenue account → GL; deferred/accrued revenue if present |
| **Cash application** | customer payment, partial and full reconciliation, over/under payment, write-off |
| **Follow-up / dunning** | `account_followup` |
| **Aged AR** | ageing buckets, reporting currency, as-at date semantics |
| **AR reconciliation** | AR sub-ledger ↔ GL control account |

### Out of scope (explicit)
| Area | Why | Where it belongs |
|---|---|---|
| AP / vendor bills (`in_invoice`, `in_refund`, `in_receipt`) | Different wave | Wave C |
| Tax computation internals | Localisation wave | separate |
| Sales order → invoice **upstream** flow | Sales module, not Accounting | Sales wave |
| Bank statement import | Treasury | Wave D |
| **Any Wave A blocker** | **Routing a Wave A blocker into Wave B to clear the Wave A Gate is prohibited and is re-tested for** | stays in Wave A |

---

## 2. Inherited semantic baseline — what Wave B may rely on

| Element | Status | Reliance |
|---|---|---|
| Journal entry / entry line as the ledger fact | `VERIFIED` | **RELIABLE** |
| Entry ↔ line company consistency | `VERIFIED` with defects (`T0-09`) | **RELIABLE AS FACT, NOT AS CONTROL** |
| Debit = credit assertion | **`T0-12` — SUPPRESSIBLE** | **NOT RELIABLE.** Wave B may not assume a posted entry is balanced |
| FX conversion semantics | **`GB-08` / `MCU-21` OPEN** | **NOT RELIABLE** |
| Period lock / close | `VERIFIED` with `T0-10` | **CONDITIONALLY RELIABLE** |
| Reconciliation model (`partial` / `full`) | `VERIFIED` | **RELIABLE** as structure; `T0-05` over-reconciliation open |
| Company / tenant boundary | **`GB-01` OPEN — Boss decision** | **NOT RELIABLE** |
| Report definitions | **`MCU-04` `VERIFIED DEFECT`** | **NOT RELIABLE** — no company dimension |
| Accounting date derivation | `VERIFIED` — system-derived | **RELIABLE AS FACT** |
| Entry identity / numbering | **`T0-08` — 6+ weakening mechanisms** | **NOT RELIABLE** |

> **Six of ten baseline elements are not reliable for design purposes.** Wave B is executable as
> **research** on all ten; it is **not** executable as **design** on six.

---

## 3. Carry-forward evidence list

| From | Artefact |
|---|---|
| Wave A core | `01`–`26` (L1–L12 registers) |
| `CORR1` | `C01`–`C14`, esp. **`C04` negative-claim scope register (`NC-01`…`NC-24`)** — *the AAS+ panel's `V-SYS-2` found this is the register most often not consumed* |
| `GAPCLOSE` | `G01`–`G11` |
| `MC` | `01`–`12` |
| `MCC` | `MCC_00` (**governing, but see `FC-F1`**), `MCC_A`–`MCC_L` — esp. **`MCC_G §8`** correction notice |
| **`FC`** | this package; **`MCU-04` disposition**, **`GB-08` decision package**, root-set finding |
| Sibling | `AAS_PLUS_REDESIGN` `00`–`21` — **`NOT CANONICAL`**, carries `AASR-VETO-01` |

> **Mandatory reading rule for Wave B, learned at cost:** *design input comes from a source's
> **adversarial and correction** sections, never its summary.* `MCC_G §8` and `CORR1/C04` are the two
> most-missed.

---

## 4. Unresolved Wave A dependencies — the gate list

| # | Dependency | Blocks in Wave B | Hard? |
|---|---|---|---|
| `D1` | **`MCU-21`** — which reference root does SMEsPlus target? | **Everything behavioural** | **HARD** |
| `D2` | **`GB-08`** — rate-resolution semantic / build freeze | FX invoice, FX payment, realised FX, aged AR in presentation currency | **HARD** |
| `D3` | **`T0-12`** — balance assertion suppressible | Any claim that an AR entry is balanced | **HARD** |
| `D4` | **`GB-01`** — tenant/company measurement crossing | Customer scoping, AR ageing per company | **HARD** |
| `D5` | `T0-08` — entry identity | Invoice numbering, duplicate detection | **HARD** |
| `D6` | `GB-02` — cross-company rewrite of a posted fact | AR immutability | **MEDIUM** |
| `D7` | `T0-05` — over-reconciliation | Cash application | **HARD for cash application only** |
| `D8` | `GB-04` / `MCU-16` — exposure surface not traversed | Tenant claims about AR | **MEDIUM** |
| `D9` | `GB-06` / `MCU-17` — correction backlog | Evidence integrity of the whole package | **MEDIUM** |
| `D10` | `MCU-04` — report definitions | AR reporting | **CLOSED as a defect; the design decision is `GB-01`** |

**Wave B research may proceed on all of these. Wave B *design* may not proceed on `D1`–`D5`, `D7`.**

---

## 5. AR / Revenue inventory — seed, declared

**Pattern:** `<menuitem` declarations in `views/` per addon, ODOO19 primary tree.
**This is a seed, not a denominator** — `MCU-21` must be closed before it becomes one.

| Addon | `<menuitem>` in `views/` |
|---|---|
| `account` | **52** |
| `sale` | **37** |
| `account_reports` | 2 |
| `account_followup` | 1 |
| `sale_management` | 1 |
| **Seed total** | **93** |

**Addon surface seed:** **114** addons matching `^(account|sale)(_|$)` in the ODOO19 primary tree.
Thai localisation: `l10n_th` present.

**Core AR models:** `account.move` (`out_*` types), `account.move.line`, `account.payment`,
`account.payment.term`, `account.payment.term.line`, `account.partial.reconcile`,
`account.full.reconcile`, `res.partner` (receivable), `account.account` (receivable type).

---

## 6. Chain to be traced

```
source document (SO / manual)
  → AR event (invoice · credit note · receipt · payment · write-off · follow-up)
    → journal entry + entry lines
      → GL posting (revenue · receivable · tax · FX)
        → reconciliation (partial → full)
          → AR sub-ledger ↔ GL control reconciliation
            → reporting (aged AR · revenue by period · statement)
```

**Each arrow must carry:** company scope · currency + rate resolution · date semantics (document /
accounting / due / as-at) · identity + immutability · control (record rule, ACL, constraint) ·
failure mode · tolerance-zero exposure.

---

## 7. Coverage matrix to be completed

| Element | Required output |
|---|---|
| Customer master | field semantics; receivable derivation; company scope |
| Invoice | `out_invoice` full lifecycle; state machine; numbering |
| Credit note | `out_refund`; reversal lineage — **`BW-35` applies: no constraint on the link** |
| Payment | `account.payment`; method lines; over/under payment |
| Follow-up | levels, triggers, company scope |
| Aged AR | bucket definition; **as-at semantics**; currency — **`BW-31` applies** |
| Write-off | authorisation; account derivation |
| Statement | content; company filter — **`J-10` class applies: check for a missing company term** |

---

## 8. Tenant / company boundaries to test

Every one of these is a **known Wave A failure shape** to be re-tested on the AR surface:

1. Bare `search` with no company term (`J-10` shape — found in the Thai VAT export)
2. Root-level guard that admits a whole tree (`J-13` shape, ≥7 members)
3. Elevated (`sudo`) read outside every record rule
4. Caller-supplied company id with no access check (`MCU-11` shape)
5. Model with **no company field and no record rule** (`MCU-04` shape)
6. Report/menu artefact with no company dimension (`FC-A1` shape)

---

## 9. Currency / FX dependencies

**All blocked on `D1`/`D2`.** Specifically: invoice-date rate; payment-date rate; realised FX on
settlement; unrealised revaluation of open AR; aged AR in presentation currency (**`BW-31` — converts
at today's rate, no record rule, par fallback**); credit note must reproduce the original rate or the
reversal will not net to zero.

---

## 10. Tax / localisation handoff

Thai VAT output tax on customer invoices; **`J-10` is a live verified defect in this exact area**
(a Thai statutory VAT filing artefact can contain another legal entity's invoices). Withholding tax at
customer receipt. Tax invoice / receipt numbering under Thai rules. **Statutory claims remain `HOLD`
per the clean-room rule** — Wave B may record the mechanism, not the legal conclusion.

---

## 11. Negative-claim search universe

**Declared before Wave B starts, not after:**

| Element | Value |
|---|---|
| `POPULATION` | to be declared per question |
| `PATTERN` | to be declared per question |
| **`PATH SET`** | **BLOCKED on `MCU-21`.** Wave B may not declare class `A` until the root set is declared |
| `UNIT` | to be declared per question |

> **Wave B may make no class `A — VERIFIED ABSENCE` claim until `MCU-21` is closed.** Until then every
> absence is class `C` with a stated boundary. **This is a hard rule and is the single most important
> thing carried out of Wave A.**

---

## 12. Balanced-but-wrong taxonomy seed for AR

| Candidate class | Searched? |
|---|---|
| Revenue in the wrong period | **NO** |
| Revenue to the wrong account | **NO** |
| AR to the wrong customer | **NO** |
| Payment applied to the wrong invoice | **NO** |
| Over-application creating a phantom credit | **NO** — related to `T0-05` |
| Credit note not netting its invoice | **NO** — `BW-35` |
| Aged AR bucket mis-dated | **NO** |
| FX-revalued AR double-counted | **NO** |
| Statement omitting a company | **NO** — `J-10` shape |

**9 candidate classes, 0 searched.** Per `ER-CORE-4`, **an empty class means UNSEARCHED, never
ABSENT** — and that rule has a **2-of-2 record** of empty classes containing a verified defect on first
search.

---

## 13. Plans

**L1–L12:** L1 domain map · L2 function coverage · L3 forensic · L4 cross-module · L5 semantic model ·
L6 failure/edge · L7 control matrix · L8 identity/immutability · L9 SaaS boundary · L10 migration ·
L11 reconciliation proof · L12 independent review.

**Very Deep / L99999.99999 extension:** denominator-first enumeration over a **declared root set** ·
cross-version divergence review across the declared roots · tolerance-zero boundary discovery ·
balanced-but-wrong search of all 9 seed classes · adversarial challenge by non-authors · fixed-point
convergence test.

**Independent review:** ≥2 reviewers, neither an author; reviewers verify **claims**, not prose;
**hash the package before review** (`ER-CORE-8`) and name the digest reviewed.

**Method convergence:** `MC-01`…`MC-10` re-run; fixed point requires two consecutive independent passes
with no material delta.

**Boss Gate dependencies:** `D1`–`D5`, `D7` must be dispositioned before any Wave B **design** output.

---

## 14. Readiness verdict

> # `NOT READY — EXACT DEPENDENCIES`
>
> **Wave B research is prepared and could open immediately on Boss authority.**
> **Wave B design cannot open.** Exact dependencies: **`D1` (`MCU-21`), `D2` (`GB-08`), `D3` (`T0-12`),
> `D4` (`GB-01`), `D5` (`T0-08`), `D7` (`T0-05`).**
>
> **`D1` is first and cheapest.** It is a programme declaration, not research, and closing it unblocks
> `D2` and every class `A` claim Wave B would otherwise be unable to make.
