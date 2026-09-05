# P10 ↔ P09 — ANALYTIC / RECOGNITION ECONOMIC-EFFECT RECONCILIATION

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1
Peer: `P09` Plan-to-Analyze, package `16f884f`, amendment `9a3bded`, terminal `READY FOR CORE ACCOUNTING RECONCILIATION` qualified by PMO `RECOMMEND HOLD` and two AAS+ vetoes.

---

## 1. Why This Reconciliation Matters to P10

A recognition event has an **economic effect** as well as an accounting effect. The accounting effect lands in the ledger; the economic effect lands on a cost object. P10's recognition entries carry an attribution payload, so P10 is a producer of management-accounting data whether or not it intended to be.

## 2. The Reconciliation's Product — `P10-F-38`

`P09` published a root cause: the management dimension is expressed as physical database schema plus a schemaless allocation payload, and **eleven independently-found defects all follow from that one choice.** `P04` then supplied `P09` with a specific instance: depreciation writes the allocation onto both rows of the entry, with no account-type filter and opposite signs, so the two management records are mirror images that net to zero.

P10 re-derived the same mechanism in its own domain, from its own primary source. **The deferral engine has the identical shape** — see `24` §3. So the instance count is now two, in two unrelated mechanisms, and the defect is confirmed as a property of programmatic recognition posts generally rather than of the asset engine.

`P09`'s eleven-defect root cause gains a second confirming instance, returned as `OUT-02`.

## 3. What P10 Adopts From P09

| # | Item | Effect on P10 |
|---|------|---------------|
| `AD-1` | An analytic plan has **no company field at all** — plans are database-global | P10's recognition attribution is therefore carried on a structure with no company scope, while the recognition itself is COMPANY-scoped. See `33` |
| `AD-2` | The allocation payload is absent from every lock-date list, every integrity-hash list and the tracked-field set | The attribution of a **posted, hashed, locked** recognition entry is freely editable and untracked. P10's period-close controls do not reach it |
| `AD-3` | ~~Mandatory-plan validation is restricted to product-type rows, so programmatic posts skip it~~ — **CAUSE CONTRADICTED, class `E`, `34` `W-05`.** Deferral lines *are* product-type rows and pass that filter. The gate is inert because it requires a context key supplied only by user-interface buttons | The conclusion stands — no mandatory-attribution rule binds P10's entries — but **the mechanism P10 adopted from the peer was wrong**, and P10 propagated it as firm without deriving it |
| `AD-4` | `MA-11` — *a company-scoped attribution requirement shall never be enforced through a tenant-scoped structure* | **Adopted as a P10 design constraint.** See `33` |
| `AD-5` | The **cost object** does not exist as a first-class object; ten de facto ones share one record type with no discriminator | P10 cannot specify what a recognition event is attributed *to* until this is authored. `PEER DEPENDENCY OPEN` |

`AD-1`, `AD-2` and `AD-3` are carried as **peer-supplied, class `B`** — P10 did not re-derive them. `AD-4` is a position. Only the mechanism in §2 was independently verified.

## 4. Scope Consequence

`P09`'s structure and P10's requirement point in opposite directions, and the conflict is real:

- A recognition event's economic effect is **COMPANY-scoped** — it is a financial effect in a company's books.
- The structure carrying its attribution is **database-global**, with no company field at all.

Under `MA-11` this is exactly the prohibited arrangement. Under `SCP-08` — *"unset" may never mean "all"* — a plan with no company is not a plan for every company; its scope is **undefined**, and `MISSING REQUIRED SCOPE = DENY` applies.

P10 therefore records, in `33`: **recognition attribution may not be enforced, relied upon, or reported as company truth through the present structure.** That is a constraint on P10's own design, not a demand on P09.

## 5. Open Between P09 and P10

| # | Item | Status |
|---|------|--------|
| `PR-09-01` | What is a recognition event attributed *to*, once a cost object exists? | `PEER DEPENDENCY OPEN` — blocked on `AD-5` |
| `PR-09-02` | Should a recognition event carry attribution at all, or should attribution be derived from the source document it recognises? | **P10 position: derived.** A mirror-image pair that nets to zero is evidence that carrying it on the entry does not work. Offered to P09, not asserted over it |
| `PR-09-03` | P09 holds an AAS+ veto blocking implementation while the accounting-event identity is undefined | **P10 concurs** and notes it is the same object as `IN-05` and Boss `D-5`. Three processes are now blocked on one undefined object |
