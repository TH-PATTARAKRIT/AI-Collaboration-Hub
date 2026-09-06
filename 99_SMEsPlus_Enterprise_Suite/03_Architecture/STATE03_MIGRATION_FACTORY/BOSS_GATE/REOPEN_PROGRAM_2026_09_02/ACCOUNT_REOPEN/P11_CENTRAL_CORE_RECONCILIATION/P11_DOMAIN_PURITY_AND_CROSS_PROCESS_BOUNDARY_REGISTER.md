# P11 — DOMAIN PURITY AND CROSS-PROCESS BOUNDARY REGISTER

`[SMEPLUS-26-09-06-…-CORR2-PHASES-001]` · `CP-P11C2-10` · **PHASE S — DOMAIN PURITY FIRST**

> **The governing rule:** *P11 combines Accounting Truth from all Pxx, but P11 must not re-learn the
> internal operation of another Pxx.*
> **Test applied to every evidence path in CORR2:** *does this step read a peer's lifecycle, module
> internal, model internal, or runtime implementation?* If yes → **STOP THAT PATH**.

---

## 1. Contamination events — detected, stopped, routed

| # | The path P11 was about to take | Why it was contamination | Action | Minimum fact retained |
|---|---|---|---|---|
| `DC-01` | Open the `om_data_remove` module source to establish which tables it deletes and whether authorisation exists | **`P06`'s domain.** `P06` has already classified it: `DESTRUCTIVE PATH VERIFIED` / `NO SERVER-SIDE AUTHORIZATION VERIFIED` / `REACHABLE — DEPLOYMENT VERIFIED` | **STOPPED.** Routed to `P06` | *that the path exists, is installed, and is unauthorised* — attributed to `P06` and `P01`, never re-derived |
| `DC-02` | Read `stock_valuation_layer._validate_accounting_entries` to confirm the gate `manual_periodic` closes | **`P01`/inventory internals.** `P01` published the gate and its five consequences | **STOPPED.** Routed to `P01` | *that one setting closes the gate and five P11 items collapse to one* |
| `DC-03` | Re-derive `P09`'s depreciation pairing to check the 17,405 → 17,465 population correction | **`P09`'s analytic internals**, and `P09` has already re-measured it under independent challenge (`D25`) | **STOPPED.** Received as published | *the corrected figures and the gross/net ratio* |
| `DC-04` | Enumerate the 31 core trees to adjudicate `P04-B-51` against `ERR-P01-41` | **Estate-wide search**, forbidden by §14; and the dispute is **`P01`/`P04`'s to settle** | **STOPPED.** Published as `OC-06`, routed to all three | *that the two statements are mutually exclusive* |
| `DC-05` | Open `P05`'s petty-cash workflow to understand why 634 of 993 expenses use it | **`P05`'s workflow internals.** Incidence is the accounting-relevant half and is published | **STOPPED** | *the incidence, and the inversion rule `P11-G-05`* |
| `DC-06` | Read `P10`'s recognition grid/convention engine to evaluate the six restored options | **`P10`'s engine internals**, and the options are Boss-reserved | **STOPPED** | *that the option set is six and `OPT-A` is restored* |

> **6 contamination events. 6 stopped at detection. 0 pursued. 0 peer lifecycles opened in CORR2.**

## 2. Reads P11 **did** perform, and why each is inside the boundary

| Read | Justification |
|---|---|
| 12 P11-addressed peer artefacts at frozen SHAs | These are the peers' **published interfaces to P11**. Reading a handoff addressed to you is the opposite of contamination |
| `git ls-tree` over peer trees (filename level only) | Establishes the **artefact population**. No file content read outside the 12 |
| `P09` `D23`/`D25`, `P01` `ERR-*` supplements | **Supersession resolution** — required by `P11-G-04` v3 and by the prompt's §5.3 |
| P11's own package | P11's domain |

**No database was opened. No source tree was opened. No module was read. No mutation of any kind.**

## 3. Boundaries P11 asserts against **itself**

| Boundary | Held? |
|---|---|
| P11 does not decide Boss items | **held** — 0 of 18 decided |
| P11 does not design an event schema (`D-5`) | **held** |
| P11 does not design idempotency (`CQ-11`) | **held** — routed to Phase B |
| P11 does not design isolation (`CQ-13`) | **held** |
| P11 does not adjudicate `P03`'s monetisation count | **held** — declined, as `P03` asked |
| P11 does not rank `P06`'s two severity axes into one | **held** — both carried |
| P11 does not adjudicate `OC-06` | **held** — routed |
| P11 does not fill the 30 producer debit/credit cells | **held** — fifth challenge survived |

## 4. Phase-boundary attestation

| Not started / not activated | Verified |
|---|---|
| PHASE SA · PHASE B · PHASE C | not started |
| **AI EOS** | **NOT ACTIVE** — not invoked, not simulated |
| Whole-ERP Event Continuity validation | not performed |
| Final Producer/Consumer contracts | not established |
| Functional Design · schema · API · queue · saga · outbox · workflow engine | **no technology chosen, none evaluated** |
| Forbidden labels `FINAL CONTRACT` / `FINAL ERP TRUTH` / `FINAL ARCHITECTURE` / `DESIGN FROZEN` | **0 occurrences** |

**`CP-P11C2-10` — COMPLETE — EVIDENCE VERIFIED.**
