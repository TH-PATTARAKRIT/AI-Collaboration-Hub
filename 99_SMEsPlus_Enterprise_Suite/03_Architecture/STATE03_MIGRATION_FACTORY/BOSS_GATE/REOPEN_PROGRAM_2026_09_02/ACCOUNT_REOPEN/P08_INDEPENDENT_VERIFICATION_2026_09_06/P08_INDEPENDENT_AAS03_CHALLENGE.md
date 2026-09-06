# P08_INDEPENDENT_AAS03_CHALLENGE

Prompt `[SMEPLUS-26-09-06-P08-R2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-003]` · frozen surface `00ccd66`

Four experts challenged the **corrected** surface. Each reported before seeing any other. **Every material finding below was re-checked by the verifier against source or data before adoption**, and where a challenger was wrong or imprecise the verifier says so.

| Expert | Lane | Verdict | Veto |
|---|---|---|---|
| **E1** Leader Functional Design | R2R semantics, finality, correction and handoff meaning | `RECOMMEND HOLD` | `AAS03-E1-IV-VETO-01`, 10 conditions |
| **E2** Leadership Database Design | every number re-derived **from the original dumps** | `RECOMMEND HOLD` | `AAS03-E2DB-V-02`, 12 conditions |
| **E3** Lead Integration & Localization | outbound propagation, scope, peer-facing qualifiers | `RECOMMEND HOLD` | `AAS03-E3-IV-VETO-01`, 12 conditions |
| **E4** Lead Code & UI Architect | instrument reproducibility, source/runtime/version | `RECOMMEND HOLD` | `AAS03-E4-REPRO-VETO-01`, 7 conditions |

---

## 1. The one thing that discharges an audit warning

**E2 re-extracted all 21 tables from the original database dumps and compared them byte-for-byte against the extracts produced by the party under audit.**

> **Identical, 21 of 21**, once a per-session restore nonce emitted by the newer restore tool is excluded. **No selective extraction, no truncation, no row filtering.**

**The audited party's intermediate evidence is a faithful projection of the primary source.** The verification register's provisional caveat is discharged for those tables — and E2 states the bound precisely: **class B, scope the seven table families both parties extracted**, and its own sharpest finding turns on an eighth that **neither** extracted.

E2 also resolved why a fourth database was never read: **its archive format is newer than the restore tool available on this host.** That converts an open evidence gap into a **specific, cheap, liftable blocker** rather than an unbounded search.

## 2. Findings the verifier re-derived and adopted

### 2.1 The period repair is false inside the set it retreated to — **E1**

Verified directly: a **persisted fiscal-year model** (name, start, end, company, all required, plus an overlap constraint) sits **inside the declared root set**, and a **period resolver** with required, defaulted company-level boundaries sits in **core accounting**. On the deployment, **89 of 89 companies carry a populated fiscal-year boundary**. See `IVR-F-09`.

**And E1 found the regression**: the package **already held the correct qualified wording**, installed by an earlier independent review, which the Phase-S round dropped. See `IVR-F-10`.

### 2.2 The capability denominator reads the wrong column, and its predicate is falsified — **E2**

**Re-derived by the verifier from the original dump.** The published `7 / 75` rests on a **per-company code-override map**; company scoping of accounts lives in a **separate relation table that neither party extracted**. Under the correct relation, one 19.0 database alone shows **11 companies holding accounts, not 3**.

**And the predicate fails its own natural control.** A posted entry exists whose company appears in **no** charted set **under either instrument** — so the *capability* set does not contain the *history* set. **A one-line control (`history ⊆ capability`) was never run.**

> `IVR-F-15`. **`P08-CONTRA-65` — the correction of a correction — fixed an eligibility defect and introduced a population-instrument defect**, which is the class the programme's own standing rule names.

**E2's method finding is as important as the defect:** across **six** defensible denominators the numerator is **0 in every one**. Two rounds of denominator correction **could not have changed any conclusion** — and the denominator is not robust: one added posting precondition swings the journal count from 75 to 34, with no sensitivity note published.

### 2.3 A figure with no referent, shipped to P11 — **E2**

`58` §1 publishes *"at 1e-7 the answer is 3, all float artefacts on eight-figure sums."* **Re-derived by the verifier in exact Decimal: 0 unbalanced at 0.005, at 1e-4, at 1e-7 and at exact equality**, on both the computed and the stored balance.

> `IVR-F-16`. **The "3" has no referent in the data.** The package names the cause — its own float instrument — in the same sentence, and ships the number into the outbound handoff as a property of the ledger.

### 2.4 The corrections did not reach the wording that leaves the process — **E3 and E4, converging**

Both experts, working independently in different lanes, reached the same conclusion. The verifier re-derived the two sharpest instances:

- **`P08-CONTRA-26` claims *"Corrected to 0 of 109 wherever it appears."*** Enumerated: the superseded form survives in **six files**; the correction **named a file that never carried it** and **missed three that did**. `IVR-F-14`.
- **`P08-CONTRA-50`'s withdrawn wording** — *"every non-sale document"* — survives in **six further locations**, including the outbound handoff to three peers and the previously published handoff pack.

### 2.5 A token count published as an existence status — **E4**

`56` §2 states the audit-retention control has **"ZERO occurrences in the declared 18.0 source tree"** and is **UNREACHABLE** there. **Verified: the control exists in 18.0 under a different name, in 52 files — and the package's own Layer-2 quarantine cites it at two line numbers.** An earlier round had already recorded it as present. The Phase-S round searched the **newer name against the older tree** and published the zero as an existence status.

> `IVR-F-17`. **This is the package's own *population-instrument ≠ claim-instrument* defect, committed inside the correction raised to fix that very axis** — and it contradicts the package's own earlier round and its own quarantine.

### 2.6 The verifier's own new finding

`IVR-F-13` — **the handoff identifier namespace is collided.** `HO-01`…`HO-06` are defined in **two live artefacts** with different content and different consumers. **Raised by no challenger.**

## 3. Where a challenger was wrong or imprecise — recorded, not suppressed

| Claim | Verifier's check |
|---|---|
| **E3**: the version-marker count is 266 rows / 51 marked | **The verifier and E4 both measure 307 / 52.** Three parties, three row definitions, three numbers — which is itself the finding: **the metric is unreproducible because its unit is undeclared.** The package's own 299/47 is a fourth |
| **E3**: `58` carries no version marker | **False, and E4 caught it too.** `58` carries exactly one. The package's own sub-claim is wrong in the same direction |
| **E1**: *"97 files"* for the 19.0 period object | **Not reproducible.** E1 measured 853 tree-wide; E4 reproduced 97 only under an undeclared narrower path. **The substance holds; the count does not** |
| **E4**: a hard-coded flag in a product-named module defeats the audit constraint | **WITHDRAWN BY E4'S OWN CONTROL** — byte-identical to stock. Recorded because a challenger running its own discriminating case and retracting is the behaviour the programme wants |
| **E2**: the deletion module has left no execution residue | **Adopted with E2's own bound.** Three negative probes, class **B** — *no evidence found ≠ did not happen*. It correctly reframes the outbound row from *event* to **capability** |

## 4. Convergence

**All four experts, in four lanes, reached one conclusion:**

> **The arithmetic held and the instruments did not.** Between them the experts re-derived the great majority of the package's figures — E2 alone confirmed **33 of 46** exactly, several to five decimal places, from the original dumps. **Every material defect is an undeclared unit, an undeclared path set, a wrong column, a search token standing in for an existence claim, or a correction recorded and never applied to the text.**

**And the defect the verification exists to catch is the dominant one:** corrections were audited by **disposition** rather than by **population**. In every propagation failure the edit landed on the row naming the identifier and nowhere else.

## 5. Vetoes

**Four new vetoes, 41 lifting conditions.** They stand **in addition to** `AAS+-VETO-01` (2 conditions) and `AAS+-PS-VETO-01` (6 conditions), and to the four vetoes from the audited round.

**No condition of `AAS+-PS-VETO-01` is discharged by this verification.** Three of its conditions — the purity re-run, the 19.0 root naming, and the correction-count resolution — are themselves audits of the party that made the errors and **cannot be discharged by P08**.
