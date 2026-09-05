# 37 — SCOPE-02 / P04-B-35 — P11 HANDOFF

**LAYER 2 — AUDIT QUARANTINE.** Disagreement preserved, not harmonised.

---

## 1. The item

| Field | Value |
|---|---|
| P03 identifier | `SCOPE-02` |
| P04 identifier | `P04-B-35` / `P04-PD-01` |
| Statement | The work-centre rate produces a company-scoped financial effect on a record permitted to have no company. Question 7 of CORR1 — *which company owns that financial effect* — is unanswerable. `MISSING REQUIRED SCOPE = DENY` |
| Severity | **High**, both sessions |
| Class | `FACT VERIFIED` (mechanism); **CONTRADICTED** as a design — `CTR-P03-06` |

## 2. Agreed between P03 and P04

| Point | Status |
|---|---|
| The work-centre rate creates a financial effect | **Agreed** |
| A company-optional work centre cannot answer which company owns it | **Agreed** |
| Equipment register is `TENANT`, company-optional correct | **Agreed** — P03 re-derived it independently, `36` §2 |
| Asset is `COMPANY` | **Agreed** |
| Closing evidence is a runtime count of company-less work centres | **Agreed as necessary** |

## 3. Where they differ

| # | Point | P04 | P03 | Evidence |
|---|---|---|---|---|
| **D-1** | Does the tenant narrowing extend from Equipment to Asset? | Does not say; the message narrows equipment only | **Explicitly not.** Depreciation is a company-scoped financial effect | `36` §1 — the two objects are **unlinked in both directions** |
| **D-2** | Is the specified count sufficient to close? | Named as *the* closing evidence | **Necessary but not sufficient** — it returns an empty population | `31` §5 — 0 of 0 across three databases |
| **D-3** | Monetisation count | 7 under its declared unit (9 under posting-artefact) | 2 under the inventory-value-writer unit | `27` §3 — **not a disagreement; different units, both published** |

**D-3 is listed as a difference and immediately resolved**, so that a later reader does not
re-open it as one. D-1 and D-2 are live.

## 4. What P11 must decide

| # | Decision | Why it is P11's |
|---|---|---|
| **P11-D-1** | Whether a scope narrowing established for one object may be read across to a related object | A cross-process scope-semantics rule; neither P03 nor P04 may set it |
| **P11-D-2** | What closes a scope defect whose specified evidence returns an empty population | A programme-wide evidence-sufficiency question — it recurs wherever a defect is latent |
| **P11-D-3** | Whether `MA-11` (P09) is binding on P01–P10 | P09 states it; P03 adopts it; only P11 can make it programme-wide |

## 5. What P11 should **not** be asked

- To adjudicate the monetisation count. Four units are declared and all four counts are
  published — `27` §3. There is nothing left to adjudicate.
- To close `SCOPE-02`. The mechanism is verified; only the incidence is open, and that
  needs a deployment with work centres, which no session currently has.

## 6. Status

**`PEER DEPENDENCY OPEN — P11`.** P03 did not wait, and every unaffected activity in this
round completed.
