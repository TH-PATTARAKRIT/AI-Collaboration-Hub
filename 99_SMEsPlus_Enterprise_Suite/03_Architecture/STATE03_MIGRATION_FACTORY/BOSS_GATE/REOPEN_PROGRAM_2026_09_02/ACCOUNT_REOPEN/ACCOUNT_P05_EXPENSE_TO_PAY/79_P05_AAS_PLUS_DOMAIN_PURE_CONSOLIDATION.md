# 79 — P05 AAS+ DOMAIN-PURE CONSOLIDATION

`LAYER 2 — AUDIT QUARANTINE` · PHASE S · **consolidation without forced consensus**
Inputs: `78` (four bounded challenges), `81` (path-set self-test), `83` (error log), `77` (integrity audit).

**AAS+ does not vote and does not average.** Where the four experts disagree or where an expert's
finding cuts against the author's, both positions are carried. Where the author's follow-through
changed a finding's severity in either direction, the change is stated with its direction.

## 1. The Round's Actual Shape

| | |
|---|---|
| Findings raised by independent challenge | **18** |
| Findings raised by the author before review opened | **0** |
| Findings rejected on re-verification | **0** |
| Claims withdrawn entirely | **0** |
| Claims **narrowed** | 4 (`RE-41`, `RE-42`, `RE-45`, `MD-01` framing) |
| Closure questions **re-opened** | **1** (`CQ-P05-13`) |
| Net closed questions | **11**, down from 12 |

> **`AAS+-01` — This round removed more certainty than it added, and that is its result.**
> PHASE S was asked to produce candidate Input / Process / Output / Handoff models. It produced them.
> It also discovered that the evidence base under them was **47.1% smaller than declared**. Both are
> true, and the second does not cancel the first — but it does determine how the first may be used.

## 2. What Survives Unchanged

Recorded first, because a round that only lists damage misrepresents its own package.

| Finding | Why it survives |
|---|---|
| **The funding partition** — 2 / 357 / 634 = 993, disjoint and exhaustive on the typed field | Reproduced independently by Expert 2 from a fresh extraction, then a third time by the author. `RE-39` qualifies a **second** field, not these counts. |
| **`TX-01`** — 100.00%, 358 of 358 at v18 | Structurally overdetermined, not statistical. **Challenged by no expert this round** — recorded as unchallenged rather than as endorsed. |
| **The version basis (`MD-02`)** | Reproduced cell by cell by two experts against both the registry and the manifests. `RE-47` weakens **one** row's basis; four rows compare identical strings. |
| **The state model and its controls** | Expert 4 verified the derived-state compute, the self-approval gate, the single-funding-route constraint and the four-step account fallback **directly in source**, and confirmed each as a real server-side control rather than a view attribute. |
| **`PC-01`** — 267 claims with no accounting entry, **222 of them marked settled and paid** | Reproduced by the author; `PS-04` eliminated one candidate cause without touching the finding. |
| **Zero statutory determinations · zero domain-boundary violations in the package** | Confirmed by Expert 3 explicitly, and by Expert 4's independent boundary check. |

## 3. Where the Consolidation Refuses to Round Off

### `AAS+-02` — `RE-48` is not one finding among eighteen

The other seventeen are corrections **within** a package. `RE-48` is a correction **to the package's
foundation**: it establishes that the set of code this package read was never compared to the set of
code the deployment runs, and that the gap is 47.1%.

It does **not** follow that the P05 findings are wrong. The overwhelming majority are positive claims
about code that **was** read and data that **was** extracted, and those are unaffected. What follows
is narrower and harder:

> **Every P05 negative of the form *"the reference does not do X"* is bounded to 52.9% of the
> installed deployment, and until `AR-04` is authorised it must be read that way.**

That includes `CO-06` (no correction event published), `ORPH-01a` (no correction mechanism at all),
and the *"no live posting exists"* family. None is withdrawn. Each is **narrower than it reads**, and
`69` and `21` now say so on the page rather than in a reviewer's memory.

### `AAS+-03` — the author's follow-through is credited and bounded

Expert 4 stopped at *"the boundary was not tested."* The author ran the test, and the test produced
the round's largest finding. That is the correct behaviour and is recorded as such.

**It is also the behaviour that must not become a habit in this phase.** The follow-through was
legitimate because it was an intersection of two already-declared sets plus three named module reads.
Reading the remaining 167 would be a widening, it was **not** done, and it is routed to `AR-04` for
authorization rather than taken.

### `AAS+-04` — one finding was weakened by its own author, and that is reported

`PS-03` (a lifecycle reaching *paid* with no accounting entry, in installed code) is real. `PS-04`
measured whether it fires and found **0 of 993** qualifying rows. The author looked for the
disconfirming population and published it. **Latent, not live** — stated in the author's own
disfavour, as the latent/live rule requires and as this programme has previously failed to do.

### `AAS+-05` — where the experts did not converge, and no consensus is forced

| Question | Expert 2 | Expert 4 | AAS+ |
|---|---|---|---|
| Is code identity resolvable? | class **D** — *no available search resolves it from this evidence base* | implicitly resolvable — locate the running server's addons path | **Both stand.** Expert 2 is right about *this* evidence base; Expert 4 is right that a path exists. It requires `AR-02`, which is unauthorised. `U-16` stays **D** and the disagreement is recorded rather than settled. |
| Severity of the 23 duplicate-candidate rows | a gap, explicitly not a finding | not examined | **`C — NOT DECIDABLE`**, as Expert 2 proposed. The author does not upgrade it. |

## 4. Veto Position

> **`AAS+-VETO-01` — UPHELD AND EXTENDED.**
> No P05 output may be treated as a **final contract**, and — added this round — **no P05 negative
> claim may be relied upon as a design input** until `AR-04` is dispositioned. Positive findings,
> counts, the funding partition, the version basis and the state model are usable as PHASE S
> candidates now.
>
> This is not a HOLD on P05's work. It is a HOLD on **one class of P05's conclusions**, and it names
> exactly which class and exactly what would lift it.

## 5. What AAS+ Does Not Assert

- That the 167 unread modules contain anything relevant. **They were not examined.** `C — NOT SEARCHED`.
- That the package is now complete. `EC-01` remains **NOT SATISFIED**, for a measured reason.
- That zero rejections among 18 challenges indicates expert accuracy. It indicates the author found
  no overreach on re-verification. **Independent review has committed bounded-enumeration false
  negatives in this programme before**, and four experts missing something in the same way remains
  possible — `78 §7` records what none of them challenged, for exactly this reason.
