# 48 — P05 VENDOR-BILL `sudo()` AUTHORIZATION FORENSIC

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E09`

## 1. The Path

| Stage | Evidence |
|---|---|
| Actor | any user holding `base.group_user` (every internal user) |
| Model | `purchase.advance.payment.bill` (transient wizard) |
| ACL | `security/ir.model.access.csv:2` — full CRUD (`1,1,1,1`) to `base.group_user` |
| Record rule | **none found** in the module — class **A** within it |
| Function | `_create_bill` (`wizard/purchase_advance.py:203`) |
| Elevation | `self.env['account.move'].sudo().create(...)` |
| Journal effect | a vendor bill (`in_invoice`) |

## 2. Classification — `PARTIAL AUTHORIZATION`, not a full bypass

Round 2 stated *"any internal user can create a vendor bill."* That is **too strong as written**, and
the narrowing matters because P01 will act on it.

| Control | Bypassed by `sudo()`? |
|---|---|
| `ir.model.access` on `account.move` (normally `account.group_account_invoice`) | **YES** — `sudo()` skips ACL and record rules |
| `_check_company` / `_check_company_auto` | **NO** — these run inside `create()`/`write()`, not as ACL. A cross-company vendor still raises. |
| Journal entry balance check | **NO** |
| Fiscal lock date at post | **NO** — `_create_bill` creates the bill; posting is a separate act |
| Wizard **reachability** | **Not established.** The ACL grants model access; whether a menu, button or action exposes the wizard to a non-purchasing user was **not** traced. Class **C**. |

**Verdict: `PARTIAL AUTHORIZATION`.** The accounting-rights gate on `account.move` is genuinely
bypassed for any user who can reach the wizard. Whether an ordinary employee can *reach* it is
`NOT YET SEARCHED`. Structural controls (company, balance, lock) remain in force.

## 3. Scope-Aware Reading

`purchase.advance.payment.bill` creates a **COMPANY-scoped financial effect** (a vendor bill).
Under `MISSING REQUIRED SCOPE = DENY`, an operation with a company-owned financial effect must prove
company-scoped authority. Here it proves **tenant-level** authority (`base.group_user`) and elevates.
Recorded as `SC-02` in `31`; **the scope defect is confirmed even though the blast radius is narrower
than Round 2 stated.**

## 4. Reach

Installed in `iSMEs` v16, `iEVING`, `BK12MAY26`, `iTEST02` — **not** on the v18 target.
Exercised: 21 times, in `iSMEs` only.

## 5. Questions Routed to P01

Not P05's to answer: whether advance billing *should* be available to non-accounting users at all;
whether the elevation is intentional delegation or an oversight; and what the correct authorisation
scope for vendor-advance billing is in P01's model.
