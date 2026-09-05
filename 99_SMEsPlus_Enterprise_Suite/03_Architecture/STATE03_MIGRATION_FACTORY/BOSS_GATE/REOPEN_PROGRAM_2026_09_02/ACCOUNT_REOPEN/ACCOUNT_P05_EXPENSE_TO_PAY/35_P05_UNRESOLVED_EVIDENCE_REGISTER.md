# 35 — P05 UNRESOLVED EVIDENCE REGISTER (CONTINUATION)

`LAYER 2 — AUDIT QUARANTINE`
Supersedes `20`. Every unknown carries a permitted disposition. **No unclassified gating unknown
remains.** Dispositions used: `CLOSED` · `PARTIALLY RESOLVED` · `NON-GATING` · `ROUTED TO PEER` ·
`HOLD — <evidence class> REQUIRED` · `DESIGN DECISION REQUIRED AT FINAL GATE`.

| ID | Unknown | Disposition | Gating | Exact evidence that closes it |
|---|---|---|---|---|
| `U-01` | Module install state | **PARTIALLY RESOLVED.** Closed **for the six registries named** — class **A** within those files only; class **B** for any wider population, since they are a convenience sample and no deployment population was ever enumerated (`24 §4` correction). Open for the **v18 target**, class **D**. | **YES** (residue) | A dump or `ir_module_module` export of `smesplus_th`, or of any Odoo 18 database carrying the P05 custom modules. Caveat: the six registries are a convenience sample, not an enumerated population of deployments. |
| `U-02a` | Database evidence for the P05 chains | **CLOSED.** Production scale obtained: 183,590 entries, 5,201 certificates, 6,159 lines (`25`). For the claim, petty-cash and advance chains, **closed as unobtainable** — the modules are installed nowhere evidenced and the tables do not exist. | NO | — |
| `U-02b` | Runtime **execution** evidence | **HOLD — RUNTIME EVIDENCE REQUIRED.** Standing up an instance is a write/deploy action prohibited by the directive; `HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED` recorded rather than assumed. | **YES** | Authorisation to restore a dump into a disposable database and run read-only ORM queries, or an Odoo 18 instance carrying the P05 modules. |
| `U-03` | Exact `payment_state`/residual outcome of a force-cancelled bill, and of a cross-currency clearing reconciliation | **HOLD — RUNTIME EVIDENCE REQUIRED.** Class **D**; a reviewer declined to infer it and that refusal is upheld. | **YES**, for `TZ-07`/`TZ-08` closure only | Depends on `U-02b`. |
| `U-04` | `account_disallowed_expenses` mechanism and linkage | **CLOSED.** Report-only, no GL write path (class **A**); no connection to the expense path (class **A**); installed in no registry. | NO | — |
| `U-05` | `sale_expense` re-invoicing accounting effect | **ROUTED TO PEER — P02.** Class **C**. `sale_expense` is installed in 5 of 6 registries, so the route is live and worth P02's attention. | NO | P02's trace. |
| `U-06` | `multi_level_approval` linkage to P05 documents | **NON-GATING, partially informed.** No dependency links it to the expense or advance documents (class **B**); it is installed in 2 of 5 real databases, so approval chains exist in the estate but not wired to P05's surface. | NO | — |
| `U-07` | Optional core module install status | **CLOSED** — subsumed into `U-01` and now answered: `hr_expense_extract` and `hr_payroll_expense` are installed in the two `iTEST02` registries and in none of the others. `TZ-10` and the payroll leg of `TZ-11` are therefore live in 2 of 6. | NO | — |
| `U-08` | Scope determinations `SO-01`..`SO-04` | **HOLD — SCOPE EVIDENCE REQUIRED.** `SO-03` partially informed: the registries are separate databases with different owners, consistent with the default that unrelated companies are separate tenants — but that evidences the *reference estate's* topology, not the SaaS target's (class **C**). | `SO-01`, `SO-03` **YES** | A multi-company deployment to observe, plus the SMEsPlus tenancy model. |
| `U-09` | Thai statutory basis for WHT rates, forms, certificate content, add-back | **HOLD — STATUTORY EVIDENCE REQUIRED. ROUTED TO PEER — P07** (`30 §3`, eleven items). | **YES**, for statutory claims only | An authoritative Revenue Department source. P05 asserts none. |
| `U-10` | Whether view-only `is_editable` gating has a model-level equivalent outside the six modules searched | **ROUTED** — class **B** beyond that boundary. | NO | One further enumeration pass. |
| `U-11` | `addons_archive` not swept for compensating guards | **ROUTED** — eight negative claims are class **C** as whole-installation statements. Materially bounded: the deployment config's own header states `addons_archive` must not be on the `addons_path`, so it is not deployed. | NO | A sweep, if ever needed. |
| **`U-12`** | **Cause of the 1,031 certificates (27.2%) whose declared payee disagrees with the payment's counterparty** — including 940 singleton payments, so batch payments do not explain it | **HOLD — SOURCE EVIDENCE REQUIRED.** Class **D**. Raised by independent review; not investigated. | NO, but material to P07 | Read the certificate creation wizard's partner resolution against the payment's. |
| **`U-13`** | **Whether the v19 statutory-column regression** (`date`, `income_tax_form`, `supplier_partner_id` becoming nullable) **is intentional** | **HOLD — SOURCE EVIDENCE REQUIRED.** Class **D**. | NO, but material to P07 | The v19 module source, which is not in this session's declared roots. |
| **`U-14`** | **Whether the three re-dispatched AAS-03 challenges complete**, and what they find | **OPEN AT PUBLICATION.** One of four completed on first attempt; three terminated on a session rate limit and were re-dispatched. | **YES**, for `EC-07` | Their completion. Reported as a coverage shortfall in `36 §1`, not absorbed. |

## Gating Summary

| Gating unknown | Blocks |
|---|---|
| `U-01` residue | `EC-01`, `EC-03` |
| `U-02b` | `EC-03`, and closure of `U-03` |
| `U-03` | `EC-04` closure of `TZ-07`, `TZ-08` |
| `U-08` (`SO-01`, `SO-03`) | `EC-03` |
| `U-09` | `EC-03` for statutory rows only |
| `U-14` | `EC-07` |

**Six gating unknowns.** Prior package: five. The count rose because `U-14` is new and honest — the
independent-review coverage this continuation was directed to obtain was not fully obtained on the
first attempt. Every other gating unknown narrowed.

## Movement Since `20`

| ID | Was | Now |
|---|---|---|
| `U-01` | blanket unknown, `BOSS DECISION REQUIRED` | **partially resolved**, residue named precisely |
| `U-02` | blanket unknown, "no evidence exists" — **which was false** (`39 RE-07`) | **split**: `U-02a` closed at production scale, `U-02b` held |
| `U-04` | conditional | **closed** |
| `U-07` | subsumed | **closed with an answer** |
| `U-12`, `U-13`, `U-14` | — | **new**, all raised by or arising from independent review |
