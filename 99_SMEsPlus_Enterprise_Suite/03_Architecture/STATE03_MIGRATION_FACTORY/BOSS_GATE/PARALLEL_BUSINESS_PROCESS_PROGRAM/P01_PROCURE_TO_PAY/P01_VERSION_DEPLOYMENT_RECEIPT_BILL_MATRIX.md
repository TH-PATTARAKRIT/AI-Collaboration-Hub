# P01 — VERSION / DEPLOYMENT RECEIPT-BILL MATRIX

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**

Every difference below is classified as `VERSION` · `MODULE` · `CONFIGURATION` · `DEPLOYMENT` ·
`UNKNOWN`. The distinction is the point of this document: the previous round conflated a
version difference with a configuration one.

---

## 1. THE MATRIX

| Aspect | v18 source | v19 source | `D3` v16 deployed | `D1`/`D2` v19 deployed | Difference class |
|---|---|---|---|---|---|
| Receipt object | movement + separate valuation layer | movement only; value stored **on the movement** | layer table present, 74,982 rows | **no layer table** | **VERSION** |
| Valuation → ledger link | layer carries the journal-entry link | movement carries the journal-entry link | 57,863 of 74,982 layers linked | **0 of 14,441 movements linked** | VERSION (structure) + **CONFIGURATION** (the zero) |
| Counter-account source | **item category**, with a per-location override | **location only** | category properties in the generic property store | location account **unset on 0 of 525** | **VERSION** |
| Goods-received clearing concept | present (`input`/`output` category accounts) | **no runtime use anywhere in the root** | present | absent | **VERSION** |
| Replacement concept | — | valuation account + **stock-variation** account | — | variation account **set on 0 of 544 accounts** | VERSION + CONFIGURATION |
| Valuation account wired | required | required | configured (bridge operates) | **set on 0 of 37 categories** | **CONFIGURATION** |
| Valuation journal wired | required | required | configured | **set on 0 of 37 categories** | **CONFIGURATION** |
| Valuation **policy** declared | per category | per category | operating | **`real_time` on 27–28 of 37** | — |
| Behaviour when accounts are missing | **raises a blocking error at receipt** | **silently creates nothing** | n/a | silent | **VERSION — a regression in failure behaviour** |
| Bill-line account override to the clearing account | present | **absent from the corresponding file** | operating | n/a | **VERSION** |
| Price-difference replay engine | ~358 lines incl. history replay | **absent from the corresponding file (33 lines)** | 1,267 layers carry a bill-line link | n/a | **VERSION** |
| Three-way match module | in archive root only | in core root | **not installed** | **not installed** | MODULE + DEPLOYMENT |
| Intercompany auto-generation | available | available | **not installed** | **installed in both** | **DEPLOYMENT** |
| Landed cost | available | available | **installed** | **installed** | — |
| Subcontracting | available | available | **not installed** | **not installed** | DEPLOYMENT |
| Custom vendor-advance module | available | available | **installed** | **installed** | — |
| Custom purchase-request module | available | available | **installed** | **not installed** | DEPLOYMENT |
| Approvals pair | available | available | **installed** | **not installed** | DEPLOYMENT |
| Base requisition module | available | available | **not installed** | **not installed** | DEPLOYMENT |
| Purchase-side accounting bridge module | does not exist | `purchase_accountant` | n/a | **installed in both** | **VERSION + MODULE** |

---

## 2. THE FINDING THIS MATRIX EXISTS TO ISOLATE

> **The two v19 deployments declare perpetual inventory valuation and wire no accounts to
> receive it.**

- Valuation **policy**: `real_time` on 27 of 37 categories (`D1`) and 28 of 37 (`D2`).
- Valuation **accounts**: category valuation account 0/37 · category valuation journal 0/37 ·
  location valuation account 0/525 · account-level stock-variation account 0/544.

**CORRECTED after independent disproof.** That combination is **not** internally contradictory:
v19's perpetual option means *"Perpetual (at invoicing)"*, so no receipt-time posting is
expected. The correct statement is narrower and worse — **no valuation account resolves at the
bill either**, and the inventory closing period is `manual` on 87 of 88 company rows, so
**inventory value reaches the ledger by no route at all**. See `ERR-P01-10` and
`CONTRA-P01-12R`.

Classification: **FACT VERIFIED**, class **A** within `D1` and `D2`.

This is not a periodic-inventory choice either: under a genuine periodic policy the categories
would carry the periodic mode, and 27–28 of them carry the perpetual one while the periodic
closing route is disabled.

---

## 3. THE REGRESSION IN FAILURE BEHAVIOUR — THE MOST TRANSFERABLE LESSON

| Generation | Missing valuation accounts at a goods receipt |
|---|---|
| **v18** | **Refuses.** A blocking error names the missing account and stops the receipt |
| **v19** | **Proceeds silently.** The entry-creation gate simply evaluates false; goods are received, a value is computed and stored, and nothing reaches the ledger. No error, no warning, no marker |

Classification: **FACT VERIFIED**, symmetric source comparison, scope `R1` vs `R3`.

v18 made misconfiguration impossible to ignore by making it impossible to proceed. v19 made
the same misconfiguration **invisible**. The deployed evidence in §2 is what that invisibility
looks like after the fact: a warehouse with 14,441 movements and a ledger that never heard
about any of them.

**For the clean-room design this is the single clearest "do not inherit" in the package**: a
missing posting destination must never be a silent no-op.

---

## 4. INDEPENDENT CORROBORATION FROM A PEER PROCESS

Peer **P02 (Order-to-Cash)** withdrew its own symmetry premise on the ground that *the inbound
interim account is defined but wired to nothing, so neither direction is chart-supported*
(`EV-P02-081`).

P02 reached that from the **sales** side; P01 reached §2 from the **purchase** side and from
the deployed configuration. **Two processes, opposite directions, same conclusion.**

P01 does not adopt P02's finding as its own evidence — it is recorded as **convergent
independent corroboration**, and P02's item is routed to P11 alongside this one.

---

## 5. WHAT REMAINS UNKNOWN

| Item | Class |
|---|---|
| The fourth database dump — not readable with available tooling | **C** |
| Whether any deployment outside these three wires the accounts | **C** |
| Whether the v19 deployments intend to post inventory value at all, or run inventory operationally with a periodic manual entry | **D — UNKNOWN**, and not answerable from a dump |
| Whether `purchase_accountant` (v19-only, installed in both) supplies any part of the bridge | assigned as a **disproof** task to an independent expert |
