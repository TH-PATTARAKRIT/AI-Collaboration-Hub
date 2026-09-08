# SA16 — TARGETED VERY DEEP RESEARCH REGISTER

Status: **6 triggers raised, 0 executed in this session.**
Protocol: Very Deep Research Re-entry Protocol `54dd32f2`; master prompt §23.

---

## 1. Re-entry discipline

Targeted Very Deep Research reopens **only the affected function**. It does not reset Phase S,
does not restart Account L1 learning, and does not reopen unrelated verified evidence. Every
trigger below names the exact function, the exact reason under master prompt §23, and the
exact question that closes it.

A trigger is not a finding. It is a statement that a named function cannot be assured on
current evidence and that the affected work is frozen until it is.

---

## 2. Triggers raised

### TVDR-01 — Supply Routing resolution (SA-D05)

| Field | Value |
|---|---|
| Function frozen | Supply Nature resolution and the routes depending on it |
| Trigger reason (§23) | insufficiently evidenced; missing downstream semantics; missing Inventory impact |
| Evidence position | 81 blobs, 3.0% of corpus — lowest of 22 domains (`SA00` §6) |
| Blocks | BN-04, BN-05, BN-06, BN-07 in `SA05`; E2E-04, E2E-05, E2E-06, E2E-07 in `SA15` |
| Question that closes it | Which inputs resolve a line's Supply Nature, in what precedence, at what moment, and is the resolution immutable once made? For dropship specifically: does title passage without own-warehouse movement require a recorded inventory event? |
| Status | `TARGETED VERY DEEP RESEARCH REQUIRED — SUPPLY ROUTING` |

### TVDR-02 — Service delivery and completion evidence (SA-D17)

| Field | Value |
|---|---|
| Function frozen | Service order → completion evidence → revenue recognition |
| Trigger reason (§23) | unclear; missing downstream semantics; Boss has ruled the boundary without a process study |
| Evidence position | 16 blobs |
| Blocks | BN-08; E2E-08 |
| Question that closes it | What constitutes completion evidence for a service, who owns it, and at what point does it become an accounting recognition event under BD-ACC-01? |
| Status | `TARGETED VERY DEEP RESEARCH REQUIRED — SERVICE DELIVERY` |

### TVDR-03 — Project ↔ Analytic boundary in operation (SA-D18)

| Field | Value |
|---|---|
| Function frozen | Project operational progress → analytic dimension → derived financial view |
| Trigger reason (§23) | insufficiently evidenced (4 blobs — lowest single figure in the register) |
| Blocks | BN-10 |
| Governing decision | `fa57d10f` — Project manages work; Analytic Accounting manages financial dimensions; Project dashboards must not create duplicate financial truth |
| Question that closes it | By what mechanism does a Project dashboard derive financial values from source facts without holding its own copy, and what happens to the derived view when a source fact is reversed? |
| Status | `TARGETED VERY DEEP RESEARCH REQUIRED — PROJECT / ANALYTIC` |

### TVDR-04 — Quality hold on the accounting path (SA-D19)

| Field | Value |
|---|---|
| Function frozen | Inspection outcome → stock availability → cost recognition timing |
| Trigger reason (§23) | missing Inventory impact; missing Accounting impact |
| Evidence position | 20 blobs |
| Blocks | BN-17 |
| Question that closes it | Does a quality hold change when stock becomes available and when cost is recognised, and is a rejected receipt an inventory event, a return, or neither? |
| Status | `TARGETED VERY DEEP RESEARCH REQUIRED — QUALITY HOLD` |

### TVDR-05 — Equipment and Maintenance interaction with production cost (SA-D20)

| Field | Value |
|---|---|
| Function frozen | Equipment breakdown → maintenance order → production resumption; maintenance cost destination |
| Trigger reason (§23) | missing Accounting impact; missing downstream semantics |
| Evidence position | Equipment 13 blobs; Maintenance 34 blobs |
| Blocks | BN-18 |
| Governing decisions | `36c62ab3` Equipment vs Fixed Asset; `a11c9e7b` Work Order vs Maintenance Order (route stated verbatim in its §3) |
| Question that closes it | Does maintenance cost reach production cost, period expense, or asset carrying amount, and what happens to a Work Order's cost while its Work Center is down? |
| Status | `TARGETED VERY DEEP RESEARCH REQUIRED — EQUIPMENT / MAINTENANCE` |

### TVDR-06 — Commercial policy: pricing, discount, credit control (SA-D21)

| Field | Value |
|---|---|
| Function frozen | Price and credit determination at order entry |
| Trigger reason (§23) | insufficiently evidenced (pricing 18 blobs, credit control 16 blobs) |
| Blocks | the input side of BN-01, BN-02, BN-03, BN-06 — every sale begins here |
| Note | `02_BOSS_DECISION_CORE_EXTENSION_BOUNDARY` names pricing and discount strategy as *more extensible* areas. An extension point over an unspecified core is not yet a design. |
| Question that closes it | What is the core price and credit determination that extensions extend, and what may an extension not change? |
| Status | `TARGETED VERY DEEP RESEARCH REQUIRED — COMMERCIAL POLICY` |

---

## 3. Consolidation — one programme, not six sessions

`SA05-F-01` established that the seven `HOLD` business natures share a single root cause. The
six triggers above are the same root cause seen from six domains. They are therefore
registered as **one targeted research programme with six bounded work items**, not six
independent re-entries.

Consolidated scope: *the demand-and-supply front end of SMEsPlus* — how commercial demand is
taken, how supply is decided, and how non-goods delivery (service, project, quality outcome,
equipment availability) reaches the ledger.

**Explicitly out of scope for this re-entry:** every domain classified
`EVIDENCED — OPERATIONAL + ACCOUNTING` in `SA01` (D00, D03, D06, D07, D08, D09, D14). These are
not reopened. Their evidence stands.

---

## 4. Items NOT routed to targeted research, and why

Not every open item is a research trigger. The following are open but are **not** evidence
gaps, and routing them to research would be a category error:

| Item | Why not research |
|---|---|
| Group A **A1** cancellation-gate symmetry | It is a *decision*, and it is already formally addressed to Accounting/AR-AP authority. Research cannot answer an authority question. Routed to `SA19`. |
| Group A **A2** legacy approval evidence | Its own register records `EVIDENCE MISSING / BOSS DECISION REQUIRED` — Boss may commission acquisition or accept the vendor-neutral shape. That is a Boss election, not a research task. |
| `SA05-F-02` Supply Nature resolution precedence | Research bounds the alternatives; **selecting** among them is a Boss material-alternative decision (§26). Research first, then `SA19`. |
| Group A **N12** reservation-claim tie-break, **N13** dead-event inclusion rule | Recorded `CONTROLLED CARRY-FORWARD` by an independent verifier. Their status field is not "unknown"; it is "deliberately open". Re-opening them would overwrite a disposition this session has no authority to overwrite. |

---

## 5. Execution status

**No targeted Very Deep Research was executed in this session.** Six triggers are raised and
bounded. Executing them requires a research session with access to the primary evidence
estate; this session's authority is Phase SA assurance, not research execution.

Recording a trigger as raised is not the same as closing it, and this register does not treat
it as such.

---

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
