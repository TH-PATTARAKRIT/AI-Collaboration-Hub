# P09_ACTUAL_VS_BUDGET_TRACE

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. Evidence identifiers resolve in the Layer 2 quarantine.

---

## 1. THE THREE FIGURES AND THEIR THREE TIME BASES

The reference pattern reports budget consumption as three numbers. They do not share a source, a time basis, or a definition of "when".

| Figure | Source | Date basis | Stored? | Evidence |
|---|---|---|---|---|
| **Achieved** | management records (analytic lines) | the **management record's own date** | no — recomputed on every read | EV-P09-062 |
| **Committed** | open purchase commitments, not-yet-invoiced quantity, on confirmed or completed orders | the **order date** | no — recomputed on every read | EV-P09-063 |
| **Theoretical** | the budget amount itself | **elapsed calendar days** in the budget window | no — computed in application code | EV-P09-064 |

**AB-01 — Three time bases cannot be compared.** A cost committed in one period, delivered in a second and recorded against a management record dated in a third contributes to two of the three figures on two different dates. The reference pattern presents the three side by side with no reconciliation and no warning.

**AB-02 — SMEsPlus shall declare one time basis per budget** — commitment date, event date, or accounting date — and shall present every figure on that basis, converting explicitly and visibly where a source uses another.

## 2. THE ACHIEVED FIGURE IS NOT THE LEDGER

This is the trace's most important property.

**Achieved is computed from management records, not from posted ledger rows** (EV-P09-062). Because the management record population includes records with no ledger counterpart at all — timesheets, work-order durations, inventory estimations (EV-P09-110, EV-P09-111) — a budget can be consumed by amounts that were **never posted**.

The account dimension enters only as a *type* filter on the general account named by the management record, and the sign is flipped for expense budgets (EV-P09-062).

**Consequence chain:**

1. an operational time entry writes a costed management record with no journal entry (EV-P09-110);
2. that record names a general account and falls inside a budget line's window;
3. the budget's achieved figure rises;
4. no ledger balance changed;
5. the budget report and the trial balance now disagree, by design, with no marker.

**AB-03.** SMEsPlus's actual-versus-budget shall state, per figure, which truth it is measuring: Financial Ledger Truth (T1), Management Dimension Truth (T2), or Operational Measurement Truth (T3). A figure that mixes them shall be prohibited, or shall be decomposed on the face of the report.

## 3. THE MATCH CONDITION

A budget line is matched to actuals on three conditions (EV-P09-061):

| Condition | Behaviour | Assessment |
|---|---|---|
| dimension equality | the actual's axis value equals the budget line's axis value, per axis column | exact match only; no hierarchy roll-up evidenced at this join |
| date window | the actual's date falls inside the budget line's window | free-form window, no fiscal period object (EV-P09-069) |
| company | matches when the budget's company is **empty** or equal | an empty company on the budget consumes actuals from **every** company |

The third condition is the scope-critical one. Under the corrected constitution it is not automatically a defect — a TENANT-scoped budget legitimately spans companies — but it is **undeclared**: the same empty field is used for "this is a tenant budget" and for "I forgot to set the company". Ownership and availability are conflated into one nullable field.

**AB-04.** The match condition shall be derived from the budget's **declared scope**, not from the emptiness of a field. A TENANT-scoped budget consuming COMPANY-scoped actuals is an explicit, authorised cross-company aggregation (`P09_BUDGET_CONTROL_MODEL` BC-09).

## 4. THE FULL TRACE, END TO END

The constitutional trace, instantiated for budget consumption:

```
Business Source          operational act or commercial document
        ↓                [identity: non-uniform in the reference pattern]
Financial Event          posted accounting event
        ↓                [NO IDENTITY EXISTS — inherited gap]
Management Dimension     axis + value
        ↓                [axis is physical schema, not data]
Allocation               percentage payload
        ↓                [not integral, not complete, not audited]
Cost Object              — NO OBJECT —
        ↓
Budget                   header + line, no position object
        ↓
Actual                   recomputed at read time from management records
        ↓                [three time bases; includes ledger-less records]
Management Report        presented over a shadowed ledger table
```

**Four of eight links are broken or absent.** The trace is not traversable in the reference pattern in either direction: from a budget variance one cannot reach the causing business act, and from a business act one cannot prove which budget it consumed.

**AB-05 — Bidirectional traversability is the acceptance criterion.** SMEsPlus's actual-versus-budget shall satisfy: from any variance figure, every contributing record is enumerable; and from any contributing record, every figure it affected is enumerable. Neither is achievable without the Financial Event identity and the Cost Object.

## 5. STABILITY OF THE COMPARISON

| Property | Reference pattern | Evidence |
|---|---|---|
| is the achieved figure reproducible on a later date? | **no** — it is recomputed, and its inputs are mutable: an allocation on a posted entry can be changed at any time with no audit trace | EV-P09-100..103 |
| is it reproducible for a different user? | **no** for any figure derived from a dimension balance — conversion uses the reader's active company currency, at today's rate | EV-P09-031 |
| is a prior-period comparison stable? | **no** — re-parenting an axis rewrites historical management records by direct statement | EV-P09-014 |
| is the figure retained when the control fires? | there is no control to fire | EV-P09-065 |

**AB-06 — A budget comparison shall be reproducible.** The figures presented for a closed period shall be storable, dated, and re-derivable to the same values. The reference pattern cannot satisfy this for any of its three figures.

## 6. WHAT HAPPENS AFTER PERIOD CLOSE

The directive asks explicitly. The answer, from the evidence:

| Behaviour after close | Finding | Class |
|---|---|---|
| can a management record be written into a closed period? | the ledger's lock-date guards are consulted only when a **protected** field changes, and the allocation field is in none of the three protection lists | **A** (EV-P09-100) |
| can an allocation on a posted, locked, hash-chained entry be changed? | yes; it is absent from the lock-date lists, from every integrity-hash field list, and from the tracked-field set | **A** on three independent lists (EV-P09-100/101/102) |
| does the change leave a trace? | **no chatter entry, no tracking value, no hash break** | **A** (EV-P09-102) |
| does it change the ledger? | no — balance, debit and credit are untouched | **A** (EV-P09-100) |
| what happens to the prior management records? | they are **destroyed and re-created** | **A** (EV-P09-103) |
| does the budget figure change retrospectively? | yes, because achieved is recomputed on read | **A** (EV-P09-062) |

**This is the composite finding of P09.** Stated as one sentence: *after a period is closed and its entries are hashed, the management allocation of every posted amount in that period remains freely editable by any holder of the analytic group, without audit, and every budget figure over that period changes silently as a result.*

**AB-07.** Period close shall bind Management Dimension Truth exactly as it binds Financial Ledger Truth. A closed period's allocations shall be immutable; correction shall be by a dated reallocation event in an open period, carrying a reference to the closed record it corrects.

## 7. TERMINAL STATE

**AB-01 … AB-07 ISSUED AS PROPOSALS. THE TRACE IS DETERMINED NOT TRAVERSABLE IN THE REFERENCE PATTERN. NO GATE MOVED.**
