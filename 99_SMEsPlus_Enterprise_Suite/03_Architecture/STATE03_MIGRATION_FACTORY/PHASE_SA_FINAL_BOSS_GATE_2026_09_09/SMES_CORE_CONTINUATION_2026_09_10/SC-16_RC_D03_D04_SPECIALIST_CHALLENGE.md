# SC-16 — SMEs CORE SPECIALIST CHALLENGE — `RC-D-03` / `RC-D-04`

## `CP-SA-SC-130 — SMEs CORE GAP RE-CHALLENGED`

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Head consumed `ce987553`
Subjects: `SC-14` (`RC-D-03`) · `SC-15` (`RC-D-04`)
**This is SMEs Core specialist challenge — internal. It is NOT structurally independent assurance.**

**14 challenges raised · 6 accepted and corrected before publication · 5 sustained-in-part · 3 rejected
with reasons. Accepted findings are corrected in `SC-14`/`SC-15` above, not merely listed here.**

---

## 1. `RC-D-03` — challenges

| # | Lens | Challenge | Outcome |
|---:|---|---|---|
| `SC-CH-01` | **Clean Room / Nature DNA** | *"Do the four trigger classes come from a vendor's hosting tiers?"* | **Rejected.** No reference topology, packaging or deployment artefact was read. Each class traces to a SMEsPlus ruling: `BD-ACC-02`, `MTI-D-03`, `MTI-D-04`, `CF-I-08`. **`SC-14` §11 states the derivation explicitly** |
| `SC-CH-02` | **Security / Authorization** | *"`CF-I-08` forbids authoring for the Private Company topology. Does `SC-14` breach it?"* | **ACCEPTED — corrected.** The pool-exit vs topology-behaviour distinction is now stated as the load-bearing control at **`SC-14` §3.1**, and §7 carries an explicit out-of-scope list. **Without that correction the recommendation would itself have breached `CF-I-08`** |
| `SC-CH-03` | **SaaS / Multi-tenant** | *"Escalation is an exit from the pool. Who decides — platform or account management?"* | **ACCEPTED — corrected.** `SC-14` §7 now fixes it as a **platform** decision with a recorded trigger class, external attribution and deciding authority |
| `SC-CH-04` | **Accounting / Thai boundary** | *"Could escalation be used to obtain cross-company statutory treatment?"* | **ACCEPTED — corrected.** It is now **`NEVER` trigger #1** at `SC-14` §5, on the ground that **`BD-ACC-02` binds in every topology**. This was the highest-risk hole in the first draft |
| `SC-CH-05` | **Internal Control** | *"A closed trigger set with no exception path will be bypassed informally."* | **Sustained in part.** `SC-14` §6 retains **(c) as an exception path under (a)**, requiring the same authority and a recorded basis — rather than pretending exceptions will not occur |
| `SC-CH-06` | **Audit / Evidence** | *"§9 says threshold values are unavailable. Is that a research gap in disguise?"* | **Sustained in part.** Each of the four is attributed to a **named non-research owner** (Thai statutory/legal, legal/commercial, operations, security/compliance), and one is **structurally unobtainable now** — the pool's measured SLA ceiling needs a built pool, and **`RC-V-01` bars implementation start.** **A business input is not a research gap**, so no targeted Very Deep Research is opened |
| `SC-CH-07` | **Operations / Deployment** | *"Migration mechanics into the topology are undefined — is the recommendation usable?"* | **Rejected as an objection to `RC-D-03`.** Migration mechanics are **`CF-I-08` territory** and authoring them here is prohibited. Recorded as a **known downstream gap**, `SC-14` §10, not as a defect in this decision |

## 2. `RC-D-04` — challenges

| # | Lens | Challenge | Outcome |
|---:|---|---|---|
| `SC-CH-08` | **Cross-Module Integration** | *"Which mapping layer is in scope? Does this collide with the 12-boundary contract just ruled at `SC-BD-02`?"* | **ACCEPTED — corrected.** `SC-15` §1 now answers scope **first**, names `CF-XCR-GAP-01` at primary text, and **explicitly excludes** the handoff element contract and migration mapping. Widening would have re-opened a ruled decision |
| `SC-CH-09` | **Internal Control** | *"`MTI-D-04` declined the grant, so the layer has no subject. Why is this not dissolved like `F3`?"* | **ACCEPTED — corrected, and it changed the recommendation.** `SC-15` §2.1 now grounds non-dissolution in `CF-V-02`'s release path at `SA_CORR5_09` L37 — **three conditions, and a dissolved `RC-D-04` leaves limb 1 permanently unliftable.** The v1 status became **`SPECIFIED — DORMANT — NO SUBJECT`** as a direct result |
| `SC-CH-10` | **Audit / Evidence** | *"Does specifying the layer force `CF-XCR-GAP-01` to be numbered, breaking the isolation-completeness claim?"* | **ACCEPTED — corrected.** `SC-15` §8 now states that the class stays **un-numbered** because it is **specified and dormant** rather than **unspecified and absent** — the register's completeness claim survives either way. This was a real trap: the obvious fix would have broken the isolation claim |
| `SC-CH-11` | **Accounting / Thai boundary** | *"Semantic ownership to Accounting Core — is that authority it actually holds?"* | **Sustained.** Grounded in **`BD-ACC-01`** — Accounting Core owns canonical Accounting Event Identity. **No new authority is originated**; the recommendation places semantics with the body that already owns identity |
| `SC-CH-12` | **Security / Authorization** | *"What stops a mapping from silently changing a posted figure?"* | **ACCEPTED — corrected.** `SC-15` §4 now carries the prohibition as a ruled line — **a mapping layer may never become a source of truth** — plus append-only versioning and **activation/retirement as events, not edits**, mirroring `M-1`/`M-6` |
| `SC-CH-13` | **SaaS / Multi-tenant** | *"Is the scope Tenant, Company, or both?"* | **Sustained.** `SC-15` §6: **Tenant-scoped and Company-qualified**; none may span tenants at all; none may span companies for a statutory purpose (`BD-ACC-02`) |
| `SC-CH-14` | **Clean Room** | *"Is split ownership inherited from a reference integration module?"* | **Rejected.** No reference mapping table, matching routine, ORM relation or integration module was read. Derivation is `BD-ACC-01` plus SMEsPlus's own Approval/Execute/Post separation — `SC-15` §9 |

## 3. What the challenge changed

**Six accepted findings, all corrected in the recommendations before publication:**

1. **`SC-CH-02`** — added the `CF-I-08` pool-exit distinction. **Without it `SC-14` would have breached an
   active prohibition.**
2. **`SC-CH-04`** — added the `BD-ACC-02` `NEVER` trigger. **Without it escalation would have been a route
   to buy a closed ruling.**
3. **`SC-CH-09`** — reversed the drafting instinct to dissolve `RC-D-04`, and produced the
   `SPECIFIED — DORMANT — NO SUBJECT` status. **This is the finding that changed a recommendation, not
   merely sharpened one.**
4. **`SC-CH-10`** — kept `CF-XCR-GAP-01` un-numbered, preserving the isolation-completeness claim.
5. **`SC-CH-08`** — bounded the mapping-layer scope, preventing re-entry into a ruled decision.
6. **`SC-CH-12`** — added the never-a-source-of-truth prohibition and append-only versioning.

**Declared bias check.** Two of the three rejections (`SC-CH-01`, `SC-CH-14`) rejected Clean Room
objections **against SMEs Core's own work**, which is the self-interested direction. Both were answered by
**naming the derivation chain per element** rather than by asserting cleanliness — the derivations are in
`SC-14` §11 and `SC-15` §9 and are checkable against the cited rulings. **`SC-CH-07`'s rejection is the
only one resting on a prohibition rather than on evidence**, and it is recorded as a downstream gap so it
is not lost.

## 4. Dispositions

| Recommendation | Disposition |
|---|---|
| **`SC-14` — `RC-D-03`** | **`PASS TO BOSS DECISION`** — on the model, the authority and the `NEVER` list. **Threshold values are a declared business input, not a research gap** |
| **`SC-15` — `RC-D-04`** | **`PASS TO BOSS DECISION`** — on split ownership, the lifecycle authority, Tenant/Company scope, the immutability rules and the `SPECIFIED — DORMANT — NO SUBJECT` v1 status |

**Neither is `RETURN TO SMEs CORE`. Neither requires `TARGETED VERY DEEP RESEARCH`.**
**Both carry `OTHER AUTHORITY REQUIRED` residues that are named, not hidden:** `RC-D-03`'s threshold values
(Thai statutory/legal, legal/commercial, operations, security) and, for both, **AAS+** as the body that
discharges `CF-V-02` once Boss rules and the specifications stand.

## 5. Checkpoint

> ## `CP-SA-SC-130 — CLOSED`
> **14 challenges · 6 accepted and corrected in the source documents · 5 sustained in part · 3 rejected with
> stated grounds · both recommendations `PASS TO BOSS DECISION` · 0 returns open · no targeted research
> required · this is internal challenge and is not claimed as independent assurance.**
