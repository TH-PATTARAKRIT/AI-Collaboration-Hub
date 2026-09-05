# P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md

# ⚠ SUPPLEMENT TO THE PRIOR P06 HANDOFF — **NOT A REPLACEMENT**

**The prior handoff (`18_P06_CORE_RECON_HANDOFF_PACK.md`, incl. its Appendix B) stands in full.** This file carries **material delta only**, produced by `[SMEPLUS-26-09-05-ACC-P06-B2R-CRITICAL-RISK-SUPPLEMENT-001]` on baseline `ebf24a0`.

**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. The one thing to read first

> **A third-party database-cleanup module, `om_data_remove`, is INSTALLED on a real Odoo 19 database in this programme's estate. It deletes bank statements, payments, journal entries, journal items, reconciliations and the audit trail by unfiltered `DELETE FROM`, committing per table, swallowing errors. No server-side authorisation exists anywhere on its RPC dispatch chain. It exists in 17 copies, three rebranded `SMEsPlus Remove Data`, one locally extended for this project's Thai withholding-tax certificates. And a remediation module written inside this programme states the destructive path has already been run and produced user-visible breakage.**

**P08 found it independently** (`EV-CUST-04`, `AT-21`) and raised it as tolerance-zero `P08-T0-08`. **P08 left one question open — *"whether the underlying methods are reachable by a lower-privileged direct call is `D UNKNOWN`"*. P06 has answered it: `NO SERVER-SIDE AUTHORIZATION VERIFIED`.**

---

## 2. Classifications delivered

| Item | Classification |
|---|---|
| `om_data_remove` destructive path | **DESTRUCTIVE PATH VERIFIED** |
| Server-side authorization | **NO SERVER-SIDE AUTHORIZATION VERIFIED** |
| Reachability | **REACHABLE — DEPLOYMENT VERIFIED** on a v19 database not confirmed to be the SMEsPlus target *(v18 source chain: SOURCE-REACHABLE / RUNTIME UNVERIFIED)* |
| Financial history | **DELETION OF FINANCIAL HISTORY VERIFIED** |
| Execution having occurred | **SUPPORTED INTERPRETATION** — first-party remediation module, not a log |
| Version evidence | **CROSS-VERSION INVARIANT VERIFIED** for six core findings; **VERSION-DEPENDENT** for native WHT and the localisation surface; target generation **UNRESOLVED** |
| Custom root population | **17 copies**, four Odoo generations |
| Filtered tree | **CORRECTED** — relocated, not filtered; loadable 791, full v18 1752 |

---

## 3. Severity model — delivered, and it disagrees with itself usefully

**6 CRITICAL · 17 HIGH · 20 MEDIUM · 3 LOW · 7 INFORMATIONAL · 2 UNRANKED = 55** (baseline population; now 58).

| CRITICAL | Why |
|---|---|
| `B-50` | unauthorised deletion of financial history — **installed** |
| `B-06` | no bank-confirmation fact exists at all |
| `A6`/`B-46` | reconcile and un-reconcile are outside the close regime |
| `B-10` | 4 of 7 ingestion doors attach no identity — **precondition: import a file twice** |
| `B-26` | bank accounts admitted into every company with no owner |
| `B-13` | bank-event identity mutable with no trace *(weakest of the six)* |

**Ranked by impact, `B-50` leads. Ranked by reachability, `B-10` leads.** Two different first actions. `47_` carries both axes; **P11 should not collapse them.**

---

## 4. Highest-leverage actions, for P11 to sequence

| # | Action | Closes / bounds |
|---|---|---|
| **1** | **`ir.module.module` export from the SMEsPlus target** | `B-44`, bounds `B-50`, plus `B-31`, `B-19` |
| **2** | **Query the `iEVING` dump for the predicted orphan signature** — `account_full_reconcile` rows with zero surviving parts, `account_move_line.full_reconcile_id` pointing at them, `matching_number` violating the ORM constraint | **converts "installed" into "fired, and here is the damage"** — `OQ-112` |
| 3 | `SELECT id, parent_id, vat, company_registry FROM res_company` | `B-45` exposure |
| 4 | Five second-pass greps on single-pass negatives | lifts part of `AASP-VETO-01` |
| 5 | P01 publication | `F-02`, part of `B-04` |

---

## 5. Cross-process delta

**`P06-XC-01` — reconciled and routed.** Classification **`BOTH PARTIAL` / `CONFIGURATION-DEPENDENT`**: the four-state separation is real in the outstanding-account configuration and collapses at creation in the direct-to-bank configuration. **Neither P02's nor P06's headline is correct unconditionally, and each package contains the evidence qualifying its own.** P02's own `DC-09-01` already concedes the remedy. **Candidate `P11-C-08`. P06 does not adjudicate P02's architecture.**

**P07's three BLOCKING dependencies** — `X-07`, `X-08`, `X-09` — **all accepted, all reported defective, all with committed requirements** (`54_` `P07-R-01…04`).

**P08 — 8 of 9 peers now read.** `F-06` and `F-17` resolved to P08; `F-15` disclaimed back to P06 and now **genuinely unowned by any process**; `B-46` still open with P08 supplying both mechanism and remedy. **New inbound accepted: `XP-05` → `P06-B-57`, the settlement event has no date of its own.**

**P10 `X-08` — answered and closable.**

**P05 settlement door — denominator CORRECTED.** P05 counts **7 settlement paths** and had already counted `SR-04` as path 5. **"Eighth door" withdrawn.** `B-53` marked inherited, LOW to P06, flagged for deduplication.

**PH-DELTA-01 — Three peers independently require the same three things of a settlement event: an identity, a date, and a reversal link.** P06 `P07-R-01/03`, P07 `X-07`/`X-09`, P08 `XP-05`/`KRN-INV-01`. **That is the clearest actionable design signal the peer round produced, and P11 should carry it as one requirement, not three.**

---

## 6. Veto delta

| Veto | Status |
|---|---|
| **VETO-01** reliance | **REMAINS, narrowed** — two lift conditions unmet |
| **VETO-02** implementation | **STRENGTHENED** — `B-50` is installed |
| **VETO-03** evidence boundary | **SUPERSEDED** — premise wrong |
| **VETO-04** *(new)* | **VETO on P11 aggregating negatives across processes until each declares its addons-path population** — P06 searched 791; the full v18 distribution is 1752 |
| **VETO-05** *(new)* | **VETO on treating P06 as "well-verified" absent an independent audit** — 16 author errors, 12 caught externally |

**`AASP-VETO-04` is raised by P06 against its own contribution to P11's registers.**

---

## 7. What P11 must NOT infer

- **NOT** that the critical risk is closed. It is better evidenced and **worse** than it looked.
- **NOT** that `om_data_remove` is on the SMEsPlus target. `iEVING` is a BHPRO database.
- **NOT** that the v18 findings transfer wholesale to v19. **Six were re-tested; the FK, sequence and numbering analyses were not.**
- **NOT** that P06's negatives share a population with peers' negatives (**VETO-04**).
- **NOT** that "eighth settlement door" was ever valid — it is withdrawn.
- **NOT** that the bytecode evidence stands — it is withdrawn.

---

## 8. Terminal

> **P06 SUPPLEMENTAL CRITICAL-RISK CLOSURE — MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR SPECIFIC VERSION / DEPLOYMENT / PEER / BOSS DECISION**

Handed to P11 as **material delta supplementing the prior handoff**, under **four active vetoes**, with **58 blockers** (7 closed, severity-ranked), **16 recorded author errors**, and **16 preserved dissents**.

**Not a PASS. Not approved. Not frozen. Not merged. No implementation authorisation.**
