# P01 — THREE-WAY MATCH MATRIX

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

---

## 1. AVAILABILITY

| Root | Present? |
|---|---|
| `R1` — v18 active enterprise addons | **No** |
| `R2` — v18 archive | Yes |
| `R3` — v19 enterprise addons | Yes |
| `R4` — project custom, v18 line | No |
| `R5` — project custom, v19 line | Yes |

`EV-P01-23`. Classification: **FACT VERIFIED, class A within the five declared roots.** This is
not a claim that the capability is unobtainable — only that it is not in the active root of the
generation prior rounds cited as the target. That the project's own v19 custom set carries a
copy is itself evidence the project wanted it.

## 2. WHAT IT ACTUALLY IS

**It is an advisory status, not a control.**

The capability adds a bill-level status — *yes* / *no* / *exception* — computed from a per-line
status, with an explicit **manual override flag** on the bill. `EV-P01-32`.

The module's models contain **no blocking construct at all**: no raised exception and no
constraint. `EV-P01-33` (negative claim class A within the module's models directory; class C
for its views and for other modules). In the later generation the status is referenced only
inside its own module — nothing else consumes it. `EV-P01-34` (class A within that root's
non-test python).

**Consequence:** a bill in *exception* can be posted and paid. The match does not gate posting,
does not gate payment, and does not gate the release of the payable. It populates a filter and
a dashboard.

## 3. THE MATCH RULES

| Input | Source |
|---|---|
| Ordered quantity | order line |
| Received quantity | order line's derived receipt quantity |
| Billed quantity | order line's derived billed quantity |
| Price | bill line price vs order line price |

| Condition | Resulting line status |
|---|---|
| Bill line not linked to any order | **exception** (`EV-P01-36`) |
| Bill price differs from order price | **exception** (`EV-P01-35`) |
| Quantities agree under the applicable billing policy | yes |
| Quantities disagree | no / exception, per policy |

Bill-level roll-up: any line in exception puts the whole bill in exception; lines with
differing statuses also produce exception; an empty bill yields *no*.

## 4. THE DEFECT IN THE PRICE COMPARISON

The price check converts the bill price into the order's currency **at today's date**, not at
the bill date and not at the order date. `EV-P01-35`.

For a foreign-currency purchase this means the match result is **a function of when it is
computed**. The status is stored and recomputed when its dependencies change, so a bill that
matched when it was entered can later be recomputed against a different rate. Two consequences:

- the exception status of a foreign-currency bill is not stable over time;
- the same bill can present differently to two readers on two dates.

Classification: **FACT VERIFIED** for the conversion date, scope `R2`.
**SUPPORTED INTERPRETATION** for the instability consequence — it follows from the stored,
computed nature of the field but was **not** observed at runtime.

## 5. ASSESSMENT AGAINST THE DIRECTIVE

`§3` requires three-way matching to be deeply examined. The result:

| Question | Answer |
|---|---|
| Is there a three-way match? | Yes, as a **status**, and not in the active root of `R1` |
| Does it prevent payment of an unmatched bill? | **No** |
| Can a user override it? | **Yes**, by an explicit flag on the bill |
| Is the price tolerance configurable? | **Not found** — the comparison is exact. Class **B**, scope: the module's models only |
| Is the quantity tolerance configurable? | **Not found** — decimal precision only. Class **B**, same scope |
| Is the result stable over time? | **No** for foreign-currency bills (§4) |
| Does anything downstream consume the status? | **Not in the later generation's non-test python** — class A within that scope |

## 6. DESIGN POSITION CARRIED FORWARD

**DESIGN CANDIDATE, not yet a decision.** If SMEsPlus requires three-way matching as a
*control* rather than a *report*, the reference implementation is not a transfer candidate: it
would have to be rebuilt as a gate with configurable tolerance, an auditable override with a
reason and an approver, and a comparison performed at a fixed date rather than at read time.

Independent examination of the lifecycle and matching semantics around this capability was
assigned to the Functional Design expert; results and any disagreement with the above are in
`P01_AAS03_EXPERT_CHALLENGE.md`.
