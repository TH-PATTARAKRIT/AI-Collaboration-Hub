# P06_55_BLOCKER_SEVERITY_REGISTER.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S02)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Standing defect closed by this file:** AAS+ raised the absence of a severity model at round 2 (`AASP-F-04`), PMO elevated it at round 3 (`PMO-TF-05`), and it has been open across two rounds. **It required no new evidence and should have been built earlier.**

---

## 1. Denominator, executed not declared

```
grep -oh 'P06-B-[0-9]\+' *.md | sort -u | wc -l   →  55
```
**POPULATION:** distinct `P06-B-*` identifiers across all package files at baseline `ebf24a0`. **UNIT:** blocker. **RESULT: 55**, ids `B-01` … `B-55`, contiguous.

The prompt's figure of 55 is **CONFIRMED against the register**, not assumed. Separately: 44 `P06-OQ-*` open items and 1 `P06-XC-*`, which are **different units and are not ranked here**.

---

## 2. Severity criteria — stated before any assignment

A blocker is **CRITICAL** if it satisfies **at least one**:
- **C1** destruction of financial truth (posted history can be removed, not reversed)
- **C2** unauthorised financial mutation (a financial effect reachable without an authorisation check)
- **C3** cross-tenant financial access or effect
- **C4** irrecoverable audit-lineage loss (provenance cannot be reconstructed)
- **C5** systemic duplicate financial effect (a routine act produces double accounting)
- **C6** ability to bypass a fundamental accounting control (period close, immutability, matching integrity)

**HIGH** — a material financial misstatement or control failure, but bounded: it needs an uncommon configuration, a specific privilege, or it misstates without destroying.
**MEDIUM** — a real defect with a workaround, a reporting or visibility gap, or a bounded-value error.
**LOW** — correctness or hygiene issue with no direct financial effect.
**INFORMATIONAL** — governance, process or documentation.
**UNRANKED — EVIDENCE INSUFFICIENT** — severity genuinely cannot be assigned without evidence the session does not hold.

**Two dimensions are recorded separately and must not be merged:** *impact* (the criteria above) and **reachability** (how hard the precondition is). AAS+ asked for ranking by *precondition reachability*; that is the heatmap axis in `47_`, not this file's severity letter.

**Evidence confidence** is a third, independent axis: `FACT VERIFIED` · `SUPPORTED INTERPRETATION` · `PLAUSIBLE` · `UNRESOLVED`.

---

## 3. CRITICAL — 6

| ID | Title | Criteria | Reachability | Confidence |
|---|---|---|---|---|
| **B-50** | `om_data_remove` deletes bank statements, payments, moves, partial reconciles and chatter by unfiltered SQL, commits per table, swallows errors, rewinds sequences; **no server-side authorisation on the dispatch chain**; present in 4 of 4 custom roots and locally customised in one | **C1, C2, C4, C6** | SOURCE-REACHABLE / RUNTIME UNVERIFIED; requires the module installed | FACT VERIFIED (source) |
| **B-06** | No field in the system means "the bank confirmed this"; the nearest proxy is true by configuration in 2 of 3 branches | **C6** — the fundamental control of a treasury process does not exist | always present | FACT VERIFIED |
| **A6 / B-46 group** | Reconciling and un-reconciling are outside the entire period-close regime; the one indirect block fires on the wrong move | **C6, C4** | any user with unreconcile rights + a closed period | FACT VERIFIED |
| **B-10** | 4 of 7 bank-event ingestion doors attach no identity; the identity system fails open at all three enforcement points | **C5** — re-importing a CSV or QIF duplicates every line and its posted entries, silently | *"import a file twice"* — the lowest precondition in the package | FACT VERIFIED |
| **B-26** | Bank accounts may exist with no owning company and are admitted into every company by three independent guards | **C3** | a partner with no company | FACT VERIFIED |
| **B-13** | Bank-event identity fields are mutable with no journal-entry trace; only 6 fields synchronise | **C4** | write access to a statement line | FACT VERIFIED |

**Note on `A6`:** it is a finding, not a `P06-B-*` id. Its blocker carriers are `B-46` and, for the wrong-move scoping, the item tracked in `28_` PC-F-07. Recorded here because omitting the package's strongest control failure from a CRITICAL list would be a severity model that hides the worst finding.

---

## 4. HIGH — 17

| ID | Title | Why not CRITICAL | Confidence |
|---|---|---|---|
| B-27 *(CLOSED)* | `root_id` is a fiscal hierarchy; the company guard cannot enforce the boundary it names | closed; retained for lineage | FACT VERIFIED |
| B-04 | Payment intent has four entry points and no single author | misstatement risk, not destruction | FACT VERIFIED |
| B-07 | Invoice payment status has two writers | bounded | FACT VERIFIED |
| B-11 | `is_complete` compares a derived figure against a default copy of itself | a control that reports green without testing | FACT VERIFIED |
| B-12 | Deletability of bank evidence is a company toggle, not an invariant | configuration-dependent | FACT VERIFIED |
| B-14 | Six silent-drop behaviours remove bank events with no record | bounded to ingestion | FACT VERIFIED |
| B-17 | No owner for bank fees, interest or provider commission | omission, not destruction | FACT VERIFIED (bounded, see `50_`) |
| B-22 | No approval or amount control on settlement write-offs | needs an operator to act | FACT VERIFIED |
| B-25 | Net-vs-gross provider settlement unhandled | bounded to provider use | FACT VERIFIED |
| B-29 | Bank-event identity enforced database-globally, filtered with no company domain | collision, not destruction | FACT VERIFIED |
| B-30 | Accounting created outside the webhook transaction; the cron ships disabled | window bounded by 4 days | FACT VERIFIED |
| B-37 | `cr_effective_date_entries` unposts, resequences and re-dates posted entries; raw SQL on valuation rows | needs a hidden group | FACT VERIFIED |
| B-38 | Two auto-posting modules post invoices on non-accounting triggers with no idempotency guard | upstream of P06 | FACT VERIFIED |
| B-44 | **Generation gap** — only deployment evidence is Odoo 19; research target is v18 | evidence risk, not a system defect | FACT VERIFIED |
| B-45 | Lock dates inherit up the hierarchy, strictest wins, elevated privilege, including archived companies; members may be legally distinct | needs a hierarchy | FACT VERIFIED (P04 + P06) |
| B-52 | Custom write-off producer grants full CRUD to any Invoicing user, no ceiling | bounded by amount | FACT VERIFIED |
| B-55 | Evidence base is a filtered distribution; every tree-scope negative inherits that boundary | evidence risk | FACT VERIFIED |

---

## 5. MEDIUM — 20

`B-05` posting-state authorship · `B-15` statement↔entry 1:1 by convention only · `B-16` internal transfer unpaired, transit unaged · `B-18` no ageing on suspense or transit · `B-19` voided cheque numbers return to the pool · `B-20` no intercompany settlement carrier · `B-21` vendor advance defaults to a P&L expense account *(statutory HOLD)* · `B-23` two account-determination chains fail silently to `False` · `B-24` chart-of-accounts mutated as a side effect of configuration and of an import path · `B-28` *(CLOSED)* token availability exceeds ownership · `B-31` unverified-input order cancel in the v14 provider copy · `B-32` tolerance control is inverted — switching it off widens acceptance · `B-33` no cash session, custodian or blind count · `B-34` post-dated cheque not migrated · `B-35` returned-payment handling not migrated · `B-36` duplicated divergent unimported override · `B-43` payment-register wizard root-scoped, second instance of the A4a shape · `B-47` derived ownership is the common root of two guard failures · `B-48` outbound UETR has no inbound counterpart · `B-49` no import-batch object

---

## 6. LOW — 3

`B-39` module version-stamped v18 with an unchanged v14 body · `B-51` approval framework's execution path sets the flag that disables its own gate *(PLAUSIBLE, no executed path traced)* · `B-53` eighth settlement door *(inherited from P05; LOW **to P06** because the owning process is P05 — its severity in P05's register is P05's to set)*

---

## 7. INFORMATIONAL — 7

`B-01` no receiving process specification in the canonical repo · `B-02` no Jira work item · `B-03` *(CLOSED)* peers unread · `B-40` *(CLOSED)* Class-A negatives unverified · `B-41` no severity model **— closed by this file** · `B-42` deliverable-list gap · `B-54` P01 unpublished *(P08 now published — see `52_`)*

---

## 8. UNRANKED — EVIDENCE INSUFFICIENT — 2

| ID | Why it cannot be ranked |
|---|---|
| `B-08` | FX rate source and missing-rate policy at settlement. P11 holds it as `BOSS DECISION REQUIRED, packaged not decided`. Severity depends on a policy that does not yet exist. |
| `B-09` | 12 physical bank accounts on 2 GL accounts. Whether this is a defect or accepted Thai practice is **HOLD — STATUTORY EVIDENCE REQUIRED**. |

---

## 9. Distribution

| Severity | Count | Share |
|---|---|---|
| **CRITICAL** | **6** | 11% |
| **HIGH** | **17** | 31% |
| **MEDIUM** | **20** | 36% |
| **LOW** | **3** | 5% |
| **INFORMATIONAL** | **7** | 13% |
| **UNRANKED** | **2** | 4% |
| **Total** | **55** | 100% |

Arithmetic checked: 6 + 17 + 20 + 3 + 7 + 2 = **55**. Matches the executed denominator.

> **SUPPLEMENTAL NOTE.** Three blockers were raised after this register was built — `B-56` (MEDIUM), `B-57` (**HIGH**), `B-58` (INFORMATIONAL) — and are severity-assigned in `40_` Appendix A. **The distribution above is the 55-blocker baseline population and is deliberately not retro-fitted**, so the arithmetic remains checkable against the denominator it declares.

**Of the 55, 7 are CLOSED** (`B-03`, `B-27`, `B-28`, `B-40`, `B-50`, `B-51`, `B-52`) and are retained in the population with their severity, because closure of a *finding* does not remove the *risk* it documents. `B-41` becomes the eighth closure on publication of this file.

---

## 10. Three observations the ranking makes visible

**SEV-F-01 — Five of six CRITICAL blockers are in the reference implementation, not the custom estate.**
Only `B-50` is custom. **The bank half of P06 runs on unmodified reference behaviour** — the round-2 headline — and this ranking shows that is where the critical risk concentrates. Customisation is not the problem; the absence of customisation over a weak foundation is.

**SEV-F-02 — The lowest-precondition CRITICAL is also the most mundane.**
`B-10` requires only that someone imports a bank file twice. It needs no privilege, no unusual configuration and no hostile intent. **Ranking by impact alone would have placed `B-50` first; ranking by reachability places `B-10` first.** Both orderings are in `47_`, and they disagree — which is the argument for keeping the axes separate.

**SEV-F-03 — The two UNRANKED items are unranked for opposite reasons, and neither is an evidence failure by this session.**
`B-08` awaits a *decision that does not exist yet*; `B-09` awaits *statutory evidence outside any research session's reach*. Marking them UNRANKED is the honest outcome; assigning them a letter would have manufactured precision.
