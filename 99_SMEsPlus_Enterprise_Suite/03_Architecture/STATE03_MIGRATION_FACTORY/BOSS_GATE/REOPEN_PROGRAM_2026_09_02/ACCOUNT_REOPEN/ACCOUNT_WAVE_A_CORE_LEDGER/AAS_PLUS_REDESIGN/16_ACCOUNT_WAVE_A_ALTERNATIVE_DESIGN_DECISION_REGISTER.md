# 16 — ALTERNATIVE DESIGN DECISION REGISTER

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

> The mandate requires **at least two viable clean-room alternatives per high-impact area**, compared
> on: semantic correctness · auditability · tenant safety · accounting integrity · migration
> continuity · operational simplicity · extensibility · reporting consistency · testability · failure
> containment. **Alternatives are not prematurely collapsed.** A recommendation is offered where the
> evidence supports one; where it does not, the choice is left open and said to be open.

---

## `ADR-01` — Accounting event identity

| | **A1 — Separate event object** | **A2 — Entry carries event attributes** |
|---|---|---|
| Shape | A durable accounting event with its own identity, provenance, idempotency key; the entry presents it | The entry gains identity, provenance and idempotency fields; no second object |
| Semantic correctness | **high** — matches `BS-01` `F2` exactly | medium — conflates recognition with presentation, the very fusion `BS-03` identifies |
| Auditability | **high** — "what did we recognise" is answerable separately from "how we wrote it down" | medium |
| Migration continuity | **high** — provenance survives re-presentation | low — provenance dies with the entry |
| Operational simplicity | **lower** — two objects | higher |
| Extensibility | **high** — one event may later present differently per reporting framework | low |
| Testability | high | medium |
| Failure containment | **high** — duplicate detection at the event, not the entry | medium |
| Cost | real: every producer, every report, every migration touches it | low |

**Recommendation `A1`.** `PROVISIONAL` `D-01`. The parent's own `L5` reached the same position
independently and stated the reason as five problems resolved by one separation. **`A2` is retained,
not dismissed** — it is the pragmatic path if Boss judges the cost of `A1` too high, and it degrades
gracefully: `A2` can become `A1` later, whereas the reference model's current state can become
neither without a migration.

---

## `ADR-02` — Where immutability is enforced

| | **B1 — Storage-level** | **B2 — Application-level with audit** |
|---|---|---|
| Shape | Database constraints and append-only structures | Guards in code plus a tamper-evidence chain |
| Evidence bearing | `VF-02`: exactly **two** things are unconditionally immutable today, and the entry's substance is guarded by an **application guard with seven production bypass sites** | — |
| Accounting integrity | **high** | low — *"if it can be switched off, it is not immutability"* |
| Failure containment | **high** | low — `MCU-01`, `MCU-56` |
| Operational simplicity | lower — corrections must be genuinely additive | higher |
| Testability | **high** — the constraint either exists or does not | low — requires proving no bypass exists, over 192 sites of which 9 are assessed |

**Recommendation `B1`.** `PROVISIONAL` `D-02`. The decisive argument is testability, not purity:
`B2`'s correctness is a negative claim over a surface the programme has proven it cannot yet bound.

---

## `ADR-03` — Measurement (rate) scope

| | **C1 — Tenant + company** | **C2 — Tenant-level shared series** | **C3 — Group root (reference behaviour)** |
|---|---|---|---|
| Semantic correctness | high | medium — assumes one tenant, one measurement policy | **low** — `VF-15` |
| Tenant safety | **high** | medium | **fails** — `BW-14`, `BW-17` |
| Operational simplicity | lower — N series to maintain | **high** | high |
| Reporting consistency | high | high | medium |
| Migration continuity | medium — `MCU-19` applies to all three | medium | medium |

**No recommendation.** `EVIDENCE-DEPENDENT` `D-10`. `C1` and `C2` differ only where a tenant runs
companies with genuinely different measurement policies — which is a **business** question, not a
research one. And **all three are unsafe until `GB-03`'s null-company axis closes**: a company-less row
is admitted by 6 resolvers and refused by 6, under every one of these shapes.

**`C3` is recorded as rejected**, with its rejection resting on `VF-15` and not on `FX-08` — see
`D-10a`, the invalidated framing.

---

## `ADR-04` — Period and close

| | **D1 — Period object with state** | **D2 — Lock dates plus a close artefact** |
|---|---|---|
| Shape | A period is a record: boundaries, state, close artefact, facts linked to it | Keep date-range locking; add a durable close artefact recording who/when/basis |
| Semantic correctness | **high** | medium — `VF-08`: what is locked remains a date range, not a period |
| Auditability | high | **high** — the artefact is where auditability actually comes from |
| Operational simplicity | lower | **high** — much smaller change |
| Migration continuity | lower — historical data must be bucketed into periods | **high** |
| Extensibility | **high** — period-scoped controls, per-period state | low |

**Recommendation `D1`,** `PROVISIONAL` `D-06` — but **`D2` is a genuinely viable reduced-scope
path** and is recorded as such. `D2` alone closes `GAP-G01` (no close artefact of any kind), which is
the single largest close-model gap, at a fraction of the cost. If Boss constrains scope, `D2` is the
recommendation, not a compromise.

---

## `ADR-05` — Missing measurement at posting

| | **E1 — Refuse the posting** | **E2 — Post to a quarantine state** |
|---|---|---|
| Semantic correctness | **high** — no fact is asserted at an unknown measurement | high |
| Accounting integrity | **high** | high, if quarantine is genuinely outside the ledger |
| Operational simplicity | lower — business stops when a feed stops | **higher** |
| Failure containment | **high** | medium — a quarantine that reports is a second ledger |
| Testability | **high** | low |

**Recommendation `E1`.** `PROVISIONAL` `D-09`. `E2` is retained because `E1`'s operational cost is
real and will be felt. But the evidence is one-directional: `BW-01` par, `BW-29` undated earliest-ever,
`BW-30` opening at a 2010 rate, `BW-31` v19 today-rate aggregation — **four distinct fallback
semantics, each producing a plausible wrong number.** A fallback is the design that created every one
of them.

---

## `ADR-06` — Tenant boundary

| | **F1 — Tenant above company group** | **F2 — Company group *is* the tenant** |
|---|---|---|
| Shape | A new identity above the group; group-root-keyed structures re-key to tenant | Accept the reference boundary; enforce one group per tenant, one database per tenant |
| Tenant safety | **high**, if `CR-01`…`CR-05` hold | **high by deployment**, not by design |
| Operational simplicity | lower | **high** |
| Cost | high — every group-root-keyed structure changes | **low** |
| Weakness | must prove isolation over 192 sites, **9 assessed** | database-per-tenant economics; `SB-01` still disables a control **for that whole database** |

**No recommendation. `GB-01` is a Boss decision and this register does not pre-empt it.**

The one fact worth putting in front of Boss: **`F2` does not make `SB-01` safe.** A configuration
store with no company dimension is database-wide, so under `F2` it is tenant-wide — which is
acceptable — **but only if every tenant genuinely has its own database.** `F2` is a deployment
commitment, not merely an architectural simplification.

---

## `ADR-07` — Analytic / dimensional attribution

| | **G1 — Attribution is part of the fact** | **G2 — Attribution is restatable** |
|---|---|---|
| Semantic correctness | high, if management reporting must not restate | high, if it must |
| Auditability | **high** | medium — needs its own versioning |
| Operational simplicity | lower — a wrong dimension needs a correcting event | **high** |

**No recommendation. `D-28` is `UNKNOWN`, decider Boss.** The reference never makes the distinction
explicit, *"which is why analytic attribution can be silently destroyed while the account cannot"* —
so there is no evidence to adapt, only a decision to take. What the design **does** require either
way: the destruction path (`AE-05` un-post) is removed.

---

## `ADR-08` — Correction linkage

| | **H1 — Constrained bidirectional relation** | **H2 — Correction as a first-class event type** |
|---|---|---|
| Shape | Reversal and re-entry each name the other, uniqueness and delete behaviour enforced | A `correction` event carries both the retraction and the restatement as one recognised act |
| Semantic correctness | high | **high** — "we corrected X to Y" is one business act |
| Auditability | high | **high** |
| Operational simplicity | **high** — small change | lower |
| Failure containment | medium — two events can still be severed | **high** — atomic |

**Recommendation `H1` now, `H2` as the target.** `PROVISIONAL` `D-03`. `H1` is the minimum that
closes `BW-35` (`VF-22`: the pointer is not unique, is severable, has no declared delete behaviour).
`H2` is the better model and is the natural shape **once `D-01`'s event object exists** — recorded so
the sequencing is deliberate rather than accidental.

---

## Summary

| ADR | Area | Recommendation | Status |
|---|---|---|---|
| `ADR-01` | event identity | `A1` separate event object | `PROVISIONAL` |
| `ADR-02` | immutability enforcement | `B1` storage-level | `PROVISIONAL` |
| `ADR-03` | measurement scope | **none — open** | `EVIDENCE-DEPENDENT` |
| `ADR-04` | period and close | `D1`, with `D2` as the viable reduced path | `PROVISIONAL` |
| `ADR-05` | missing measurement | `E1` refuse | `PROVISIONAL` |
| `ADR-06` | tenant boundary | **none — Boss decision** | `UNKNOWN` |
| `ADR-07` | attribution class | **none — Boss decision** | `UNKNOWN` |
| `ADR-08` | correction linkage | `H1` now, `H2` as target | `PROVISIONAL` |

**Five recommendations, three deliberate non-recommendations.** The three are not gaps in the work —
two are business decisions the evidence cannot settle, and one waits on `GB-03`.
