> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 6 — Fact Ownership / Handoff / Dependency Matrix

# 10 — FACT OWNERSHIP, HANDOFF AND DEPENDENCY MATRIX

## 00 — Governing Rule

`Document state changed ≠ Physical stock changed ≠ Financial posting occurred.` Every row below is independently
justified from the canonical designs in files 04–09, not restated from evidence without re-derivation.

## 01 — Master Ownership Table

| Fact | Owner | Changing event | Who else may write | Who reads |
|---|---|---|---|---|
| Party identity | Shared Master | Explicit registration action | No transaction domain | Sales, Purchase, Inventory |
| Product/Service identity | Shared Master | Explicit definition action | Inventory (trackability-derived state only) | All three |
| Vendor Price Reference | Shared Master | Explicit maintenance, or opportunistic extension | Purchase, at commitment time (narrow exception) | Purchase |
| Sales Price Rule | Shared Master | Explicit maintenance | No transaction domain | Sales |
| Commercial Commitment (header + line) | Sales | Confirm / lock / cancel / line edit | No other domain | Inventory (fulfillment-relevant fields only), Financial Handoff (Billable-Now) |
| Supply Commitment (header + line) | Purchase | Confirm / approve / cancel / line edit | No other domain (except the scoped subcontract/dropship auto-creation, which is still a Purchase-owned write once created) | Inventory, Financial Handoff |
| Internal Demand Request | Purchase (demand-capture sub-capability) | Create / approve / reject / convert | No other domain | Supply Commitment (read-only, gate) |
| Movement Instruction / Execution | Inventory | Confirm / reserve / execute / cancel / reverse | No other domain — **hard rule** | Sales (Delivered), Purchase (Received) |
| Stock Position | Inventory | Only as a consequence of Movement Execution | No other domain | Sales, Purchase (derived views only) |
| Reservation | Inventory | Movement Instruction confirm/cancel | No other domain | Not directly read by Sales/Purchase |
| Fulfillment Continuation link | Inventory | Transfer Operation closes with a remainder | No other domain | Not directly read by Sales/Purchase |
| Reversal | Inventory | Explicit reversal action against a fully-executed operation | No other domain | Sales/Purchase (traceability linkage only) |
| Billable-Now quantity | Sales / Purchase (each its own) | Recomputed on Delivered/Received or Invoiced change | No other domain | Financial Handoff (write target) |
| Invoiced quantity | Sales / Purchase (each its own), but **backward-derived** | Financial Handoff posts a record | Financial Handoff is the actual source of truth; Sales/Purchase only mirror it | Sales/Purchase billing-status computation |
| Approval state (amount-threshold) | Purchase | Confirm action evaluated against threshold/role | No other domain | Supply Commitment lifecycle |
| Approval state (sequential level-based) | Sales / Purchase / Internal Demand Request (shared Approval Control concept) | Level approve/reject action | No other domain | Owning document's lifecycle (internal trigger logic HOLD — see [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md)) |

## 02 — Handoff Points (Cross-Domain, With Hard/Advisory Classification)

| Handoff | From → To | Mechanism | Hard or advisory? |
|---|---|---|---|
| Commercial commitment → physical fulfillment request | Sales → Inventory | Event-driven, indirect (Inventory resolves routing) | Hard — the only way a confirmed commercial line produces a Movement Instruction |
| Supply commitment → physical receipt expectation | Purchase → Inventory | Direct, synchronous | Hard |
| Physical execution → commercial/supply derived quantity | Inventory → Sales/Purchase | Read-only compute | Advisory in that neither domain blocks on it directly — but the resulting quantity becomes an input to the next hard gate (billing) |
| Fulfillment quantity → billing eligibility | Sales/Purchase → Financial Handoff | Billable-Now written verbatim | Hard |
| Financial posting → re-derived invoiced quantity | Financial Handoff → Sales/Purchase | Backward read of a posted record | Hard (drives whether more may be billed) |
| Internal demand → supply commitment | Internal Demand Request → Purchase | Hard-gated on Approved | Hard |
| Stock shortage → supply need | Inventory → (registered fulfiller, typically Purchase) | Reflective/pluggable dispatch | Hard trigger, soft binding (Inventory does not know who will respond) |
| Commercial line (scoped product config) → draft supply commitment | Sales → Purchase | Direct write, narrowly scoped | Hard, but scope-limited — not the general case |
| Physical reversal → traceability | Inventory → Sales/Purchase | Read-only linkage | Advisory (informational only; neither domain gates on it) |

## 03 — Never-Assume-Equivalence Reminders (Adopted, Restated for This Matrix)

1. A committed Commercial Commitment does not mean a Movement Instruction exists yet — only that one has been
   requested (and only for physically-fulfilled lines).
2. A committed Supply Commitment does not mean stock has arrived — Received stays at zero until a Movement
   Execution occurs, regardless of commitment state.
3. A fully-executed Movement does not mean a Financial Handoff has occurred — Billable-Now is a separate compute
   that may fire immediately (commitment-based policy) or only after fulfillment (fulfillment-based policy); the
   two are never conflated in this design.
4. An "Approved" Internal Demand Request does not, by itself, prove which control mechanism performed the
   approval — see [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) for why this remains a Controlled
   Carry-Forward Unknown at the internal-logic level even though the fact of approval is real and evidenced.

## 04 — Independent Addition: Ownership of the Financial Handoff Contract Itself

TEAM B adds one ownership fact not explicit in evidence but required for design completeness: **the shape of the
Billable-Now payload (what fields Sales/Purchase must supply to Accounting) is jointly negotiated, not unilaterally
owned by either side.** Sales/Purchase own *producing* the value; Accounting owns *what it requires to accept it*.
This is recorded here because [15](15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md) treats the contract
as an interface both sides must honor, not a Sales/Purchase-unilateral decision.
