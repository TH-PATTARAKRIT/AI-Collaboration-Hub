# 71 — AAS+ RUNTIME-INVERSION CONSOLIDATION

**LAYER 2 — AUDIT QUARANTINE.** Dissent preserved.

---

## 1. Consolidated risk

| Risk | Status | Severity | Evidence |
|---|---|---|---|
| **Live cost loss** | **CONFIRMED** — conversion cost never reaches inventory in any examined deployment, by two different routes | **Critical** | `54`, `P03R-F-09` |
| **Live inventory cost corruption** | **CONFIRMED** — 30 rows to ±10²¹, −48.7 % of valuation | **Critical** | `55` |
| **Subsidiary ↔ general ledger divergence** | **CONFIRMED** — 25 of 25 mismatched | **Critical** | `55` §2, routed **P08** |
| **Latent double counting** | 7 defects, **no mutual exclusion anywhere** | **High**, latent | `56` |
| **WIP risk** | two unreconciled representations; one absent in the manufacturing database | High | `03` §3, `68` |
| **Asset interaction** | no path; analytic route structurally incapable | High | `58`, P04, P09 |
| **Analytic interaction** | cannot fire — 0 distributions in 4 databases | Medium | `65` |
| **Scope risk** | `SCOPE-02` mechanism stands; incidence **0 of 60** | **High → Medium** | `64` |
| **Evidence-population risk** | **materially reduced** — 4 of 4 databases; `DEP-04` closed | Medium | `61` |
| **Future configuration risk** | **the dominant residual risk** | **Critical** | §2 |

## 2. The consolidated judgement

> **The system is not safe; it is unconfigured.** Eleven of fifteen defects are latent
> because rates, expense accounts, analytic distributions and automated valuation are all
> switched off. Each is a field an administrator is expected to fill.

**A costing model whose safety property is "nobody has finished configuring it" has no
safety property.**

## 3. What the two live failures have in common

`55` (explosion) and `54` (zeroing) look opposite and share one cause:

> **`_cal_price` computes what it is handed and asks nothing.** Handed nothing, it produces
> zero. Handed 10¹² per unit against a ten-month history of 30, it produces 10²¹. There is
> **no plausibility test, no bound, no reconciliation** on either side.

`R-17` — magnitude validation — is therefore the single most important design implication of
the whole P03 package, and it addresses both failures at once.

## 4. Design implications — `DESIGN CANDIDATE` only

| ID | Requirement | From |
|---|---|---|
| `R-16` | Every entry from a business event carries an identity **written and read** as the duplication guard | `DC-15` |
| `R-17` | **A cost-injection path validates the magnitude of its inputs and refuses what it cannot justify** | `55` |
| `R-18` | Mutual exclusion between competing attribution mechanisms is **structural**, not an unset field | `56` |
| `R-19` | The subsidiary valuation ledger and the general ledger must be **continuously reconcilable**, with divergence detected | `55` §2 |
| `R-20` | Absorption accounts are **mandatory**, never defaulting to a cost-of-sales account | `DC-07`, 60 of 60 |

**No architecture is frozen. `AASP-VETO-01` stands.** `21` §3 and `39` §5 carry the same
prohibition and E4's unresolved dissent about numbered requirements becoming a de facto
baseline applies here with equal force.

## 5. The inference the directive forbids, restated

§25: the deployed reference running material-only costing **does not** license SMEsPlus to
omit labour, machine cost, depreciation or overhead.

**P03 explicitly does not draw it.** The measured facts are about one vendor's product as
configured by particular operators. They are evidence about **what goes wrong**, not about
**what is required**. TAS 2 ¶12's requirement is unaffected by any of it, and remains routed
to the Asset and Accounting-Tax registers.

## 6. Preserved dissent

| Source | Position |
|---|---|
| `E1` (`69` §4, `70` §7) | Material-only costing may be deliberate; "zeroing" may be the wrong frame. Unanswerable on current evidence |
| `E4` (`69` §3, `70` §7) | The valuation fallback was inferred from absence, not read from `ir_default` — `UNR-P03-18` |
| `E4` (round 1, `20` §1 `D-03`) | Numbered requirements become a de facto baseline regardless of labelling. **Unresolved** |
| P03 vs P04 (`37` `D-1`) | Tenant narrowing must not extend from Equipment to Asset. **Preserved for P11** |
