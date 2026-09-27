# G01 PLATFORM_BASE — RED TEAM Reconciliation Addendum R1 (A3 remediation, batch 2) — `bus`, `digest`, `resource`, `resource_mail`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RECONCILIATION (REC)**. This is an addendum only. All parent REC files are immutable and were not edited |
| Group / Modules | G01 PLATFORM_BASE / `bus`, `digest`, `resource`, `resource_mail` |
| Date | 2026-09-27 |
| Parent REC artifacts (sha256, unchanged since A3 intake; re-verified 2026-09-27T15:25Z) | `G01_RECONCILIATION/G01_BUS_REC_20260927.md` `251c8a2ad06918477e4c9b9c8c52093fa95f0484ffa0db1cc5f558fe5f20e4bc`; `G01_RECONCILIATION/G01_DIGEST_REC_20260927.md` `6744994d045efe9306665256b9d437f73ed0e7720d8e88302d6032c4c4192ee5`; `G01_RECONCILIATION/G01_RESOURCE_REC_20260927.md` `e2adc10a1f346bb5dc1fe73100d3187c485a1208c12af6bc3a4732475a0fe259`; `G01_RECONCILIATION/G01_RESOURCE_MAIL_REC_20260927.md` `1ec90af273af437692663390db5e4d182cf4490204385dbf67d25fefed8cb26f` |
| Additional input (immutable, written earlier in this remediation) | A2 addendum `G01_A2_REVIEWS/G01_BATCH2_A2_ADDENDUM_R1_20260927.md` sha256 `9664c13e01c777e4731381966a412b4a9eea675168ec5ad4f848c56d0a6a037c`. Parent A2 reviews as listed in that addendum's section 0.1 (unchanged) |
| A3 reports (sha256) | `G01_A3_CHALLENGES/G01_BUS_A3_STATIC_20260927.md` `4f9c2676bfe15588479686392e4ec9520e26ab6b56ea90b9920ef613ef3209b6`; `G01_A3_CHALLENGES/G01_DIGEST_A3_STATIC_20260927.md` `2eae23cddf02d14bb5ad47fd19890be5150733088ed332271e7daab8f31360a4`; `G01_A3_CHALLENGES/G01_RESOURCE_A3_STATIC_20260927.md` `50894e31e50ad78ad88bbec72a0d0bb218bcdd38b30832f7e5dedd79675dab52`; `G01_A3_CHALLENGES/G01_RESOURCE_MAIL_A3_STATIC_20260927.md` `1c570f56bb35bab9375be2c1cc287c4c3eb90bd5137e05181a0b9a49231d7a4a`; `G01_A3_CHALLENGES/G01_RESOURCE_RMAIL_A3_SUPPLEMENT_S2_20260927.md` `25c154b36361ba549f8ac4f8edd34dc6f0f70d7f7723b290499c2ccad908edb1` (MASTER-registered; the stricter result governs) |
| Question lineage inputs | bus bank W1-B02 `G01_BUS_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `cfa2be28db573021c4a842db7a7cfb6e9e71e62e89f948a1898177cc30a8860d`; digest bank W1-B03 `G01_DIGEST_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `1ba4226db5739143130e0afc1757e3aaa3c0cf1f934ccf3349a907d0c64d74ec`; Standard 55 `QUESTION_BANK_STANDARD_55_V2.00.md` sha256 `f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d`. All three were re-hashed 2026-09-27T15:25Z and equal the parent intake values |
| Challenge IDs addressed (REC parts) | **bus:** D-BUS-02, D-BUS-03, D-BUS-04, D-BUS-05, plus the A3 1.2 REC-BUS-24 finding and the REC side of D-BUS-06. **digest:** D-DGST-01, D-DGST-02, D-DGST-03, plus the REC side of D-DGST-04. **resource:** A3-RSRC-D01 (REC primary), S-A (routing), S-B, S-C, N1–N7, and the lineage side of S-E. **resource_mail:** M-A, M-B, and N-1 precision |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Clean-room note: neutral paraphrase only. Identifiers are used only as pointers, and no code is reproduced. No percentages. No Formal Coverage claim. **No QID is answered**, since QID mapping is lineage only. No git operations. No existing artifact was edited.

Owner-stage re-derivation: before writing each REC correction, the owner stage re-checked the point against source at the anchor. The evidence is in the A2 addendum sections cited in each row, and every point was AGREED unless the row says DISPUTE.

---

## 1. `bus`

### 1.1 D-BUS-03: Lane B label restoration

The parent REC section 3 note "shown as UNCORROBORATED with the proof link" is **withdrawn**. A2's label is restored in the Lane B column:

| REC ID | A1 claim | Parent Lane B column | **R1 Lane B column** |
|---|---|---|---|
| REC-BUS-03 | C03 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-BUS-05 | C05 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-BUS-07 | C07 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-BUS-09 | C09 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-BUS-13 | C13 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-BUS-14 | C14 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-BUS-17 | C17 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-BUS-18 | C18 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |

Lane B column after R1: NOT_APPLICABLE 6, UNCORROBORATED 14, MISSING_REQUIRED_RUNTIME_PROOF 8. FAIL 0, and nothing is failed for absence. The Lane B label rule (R1) is now: A2's class is carried unchanged. For A2 omissions that A2 did not class, REC uses UNCORROBORATED when the item is runtime-observable and NOT_APPLICABLE when it is a static declaration.

### 1.2 Basis and proof-link corrections (the class is unchanged in every row)

| REC ID | Challenge | Parent basis text (defect) | **R1 basis** | Class | R1 proof link |
|---|---|---|---|---|---|
| REC-BUS-21 | D-BUS-02 | "tenant separation rests on DB name in channel key" (A2 OM-B01 said "solely") | Per A2 OM-B01-R1: wake-up **routing** is keyed by the DB name. **Payload** separation also rests on per-DB storage and the socket's own-DB cursor. The residual exposure is clear-text channel identifiers on the shared NOTIFY, including client string channels that serve as capability tokens (C05/C06), visible to any principal able to LISTEN on the cluster maintenance DB. **Linked to REC-BUS-05 and REC-BUS-06** | GAP | PR-BUS-09R1 → PC-BUS-17R1 (static), PC-BUS-18R1 (runtime) |
| REC-BUS-24 | A3 1.2 | "publisher obligation to publish near commit" | Per A2 OM-B04-R1: the loss window runs from the bus pre-commit insert to commit visibility. The module's own deferral mostly meets the "publish near commit" advice. The residual obligation covers work that runs after the bus pre-commit step inside the same commit (framework ordering, not read) | GAP | PR-BUS-06R1 → PC-BUS-11R1, PC-BUS-12R1 |
| REC-BUS-18 | D-BUS-01 | (class upheld; proof design defective) | The CONTRADICTION stands on source. The loss condition is restated per A2 addendum 2.1: the pre-commit id allocation, the dispatch-time history, and trimming only on a non-empty dispatch. A delivery observed at runtime does **not** establish at-least-once | **CONTRADICTION** | PR-BUS-06R1 → PC-BUS-11R1 (static), PC-BUS-12R1 (runtime, declared injection) |
| REC-BUS-25 | D-BUS-05 | no proof link | Unchanged fact. **Now has a proof requirement** | GAP | **PR-BUS-10 → PC-BUS-19 (static), PC-BUS-20 (runtime)** |
| REC-BUS-28 | D-BUS-05 | "cluster notify failure silences all tenants on that process" | Per A2 OM-B08-R1: a dispatcher error pauses wake-ups for every database's sockets on that process for at least the 50 s retry sleep. Rows stay stored. Rows whose NOTIFY fell in the pause are delivered at each socket's **next trigger**. The delay has **no module bound** and can exceed 50 s. It becomes loss only if no trigger arrives before GC retention ends. **DISPUTE (partial) of A3's "up to about 50 s":** dispatch is trigger-only and nothing re-polls periodically (A2 addendum 2.4) | GAP | **PR-BUS-11 → PC-BUS-21 (static), PC-BUS-22 (runtime, declared injection)** |
| REC-BUS-14 | D-BUS-06 | "effective control is Origin check" | Per A1 C14 RISK-R1 and A2 SF-B04-R1: the Origin handling is module-level only. The framework sets the session cookie with HttpOnly and **no explicit SameSite** at the anchor, so browser cross-site exploitability depends on browser and proxy behaviour and is runtime | UNKNOWN_PENDING_PROOF | PR-BUS-04R1 → PC-BUS-07, **PC-BUS-23** (static), PC-BUS-08R1 (runtime, adds a browser-originated variant) |
| REC-BUS-09, REC-BUS-22 | A3 §3 note | — | Unchanged. The runtime pack adds an anonymous caller naming an arbitrary string channel | GAP | PR-BUS-05R1 → PC-BUS-09, PC-BUS-10R1 |
| REC-BUS-17 | A3 1.2 | — | Unchanged. Note: its only runtime case is a **MEASUREMENT** (PR-BUS-08). It cannot close REC-BUS-17 in either direction, and the item stays UNKNOWN_PENDING_PROOF until an outcome is recorded and judged | UNKNOWN_PENDING_PROOF | PR-BUS-08 → PC-BUS-15, PC-BUS-16 (MEASUREMENT) |

### 1.3 D-BUS-04: QID lineage corrections (lineage only; not answers)

Bank text is paraphrased. Q007: event payloads carry only the minimum needed. Q013: a slow or disconnected consumer cannot cause unbounded growth that harms others. Q037: burst coalescing does not merge data across customers or records. Q002: authorization is checked when a subscription is created. Q040: equivalent realtime paths enforce the same rules.

| QID | R1 mapped REC items | Evidence pointers (topical relevance only) |
|---|---|---|
| bus+Q007 | REC-BUS-03, REC-BUS-21 | A2 C03 refinement: NOTIFY carries channel identifiers only, and the payload is re-read from the table. OM-B01-R1: stored payloads are whatever publishers send, and the module does not minimize them |
| bus+Q013 | REC-BUS-12 | C12 and Lane A #15: keep-alive and frame-response timeouts close dead consumers. The in-memory history per socket is time-trimmed |
| bus+Q037 | REC-BUS-03, REC-BUS-21 | Lane A #9: NOTIFY batches channel identifiers per transaction and splits them when too large. Recipient payloads come only from per-socket polls restricted to that socket's own channels |
| bus+Q002, bus+Q040 | **REC-BUS-14** (previously "no clear fit") | Q002: the handshake Origin handling decides the socket identity at creation. Q040: the socket and the polling fallback are equivalent delivery paths with different CORS and last-id handling |

**R1 lineage summary (41 QIDs):** Mapped **35**: the parent 32 plus Q007, Q013 and Q037. No evidence yet **6**: Q021, Q022, Q028, Q031, Q032, Q033. REC items with no clear fit: REC-BUS-01, 17, 19, 20, 26. Mapped ∪ no-evidence = Q001–Q041, with no overlap. The weak fit REC-BUS-02 → Q038 (fit by absence) is kept and flagged weak, as A3 noted.

### 1.4 `bus` counts after R1

MATCH 11 · GAP 11 · CONTRADICTION 1 · UNKNOWN_PENDING_PROOF 5 · **Total 28** (unchanged). Items with a proof link after R1: all parent items plus **REC-BUS-25 and REC-BUS-28**. REC-BUS-20, 26 and 27 remain without a proof requirement, as A3 upheld.

---

## 2. `digest`

### 2.1 D-DGST-02: Lane B label restoration

| REC ID | A1 claim | Parent | **R1 Lane B column** |
|---|---|---|---|
| REC-DGST-03 | C03 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-DGST-04 | C04 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-DGST-06 | C06 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-DGST-07 | C07 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-DGST-09 | C09 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-DGST-11 | C11 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-DGST-12 | C12 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |

Lane B column after R1: NOT_APPLICABLE 3, UNCORROBORATED 17, MISSING_REQUIRED_RUNTIME_PROOF 7. FAIL 0.

### 2.2 Basis and proof-link corrections (class unchanged)

| REC ID | Challenge | **R1 basis / note** | Class | R1 proof link |
|---|---|---|---|---|
| REC-DGST-27 | D-DGST-01 | Unchanged fact. **Now has a proof requirement.** The send loop has no share or active filter in module code, and the recipient restriction is a UI domain only | GAP | **PR-DGST-11 → PC-DGST-22 (static), PC-DGST-23 (runtime)** |
| REC-DGST-09 | D-DGST-04 | Adds A2 C09 finding R1: the cron's catch covers an exception type that the module's queue-only send path does not raise, so the catch is **effectively unreachable** on the module's own path. The partial-queue repeat can only be shown by **declared fault injection** | GAP | PR-DGST-05R1 → PC-DGST-09, **PC-DGST-21** (static), PC-DGST-10R1 (runtime, declared injection) |
| REC-DGST-23 | D-DGST-04 | Same as REC-DGST-09 | GAP | PR-DGST-05R1 → PC-DGST-10R1 |
| REC-DGST-20 | D-DGST-04 | Unchanged fact. The runtime expectation is now **disjunctive**: labels and currency show B, and the KPI value is either computed for A or zero or restricted by record rule under B's narrowing (consistent with A2 SF-D02/OM-D02 and REC-DGST-21) | GAP | PR-DGST-08R1 → PC-DGST-15, PC-DGST-16R1 |
| REC-DGST-07, REC-DGST-26 | A3 §3 note | Unchanged. The runtime case also records the serialized window strings | GAP | PR-DGST-04R1 → PC-DGST-07, PC-DGST-08R1 |
| REC-DGST-04 | A3 1.2 | Unchanged. Its runtime case is a **MEASUREMENT** only (PR-DGST-02). The item stays UNKNOWN_PENDING_PROOF until an outcome is recorded and judged | UNKNOWN_PENDING_PROOF | PR-DGST-02 → PC-DGST-03, PC-DGST-04 (MEASUREMENT) |

### 2.3 D-DGST-03: QID lineage corrections (lineage only)

Bank text is paraphrased. Q015: a summary does not include protected detail that the recipient would be denied in-app. Q007: cached summary values never broaden visibility after access loss. Q032: a change in reporting membership re-evaluates recipients at a defined point.

| QID | R1 mapped REC items | Evidence pointers (topical relevance only) |
|---|---|---|
| digest+Q015 | REC-DGST-04, REC-DGST-06 | C06: KPIs are evaluated with the recipient's rights, and an access error silently drops the KPI. C04: the messages KPI has no company term, and its effective boundary is framework message visibility |
| digest+Q007 | REC-DGST-06 | Lane A #4: KPI values are non-stored computes. The source invalidates the per-window cache after each read (`models/digest.py`@3eea1c39 L284–289), so no persisted summary cache is evident |
| digest+Q032 (partial) | REC-DGST-18, REC-DGST-27 | C18: auto-subscribe happens only at user creation. The recipient list is static, with no re-evaluation when a user's type or membership changes (OM-D08) |

**R1 lineage summary (40 QIDs):** Mapped **30**: the parent 27 plus Q007, Q015 and Q032 (partial). No evidence yet **10**: Q014, Q017, Q018, Q023, Q024, Q025, Q026, Q034, Q037, Q039. REC items with no clear fit: REC-DGST-01. Mapped ∪ no-evidence = Q001–Q040, with no overlap. The weak fit REC-DGST-12 → Q019 is kept and flagged weak, as A3 noted.

### 2.4 `digest` counts after R1

MATCH 12 · GAP 10 · CONTRADICTION 0 · UNKNOWN_PENDING_PROOF 5 · **Total 27** (unchanged). **REC-DGST-27** now has a proof link. REC-DGST-25 remains without one, as A3 upheld.

---

## 3. `resource`

### 3.1 A3-RSRC-D01: REC-RSRC-24 wording restored to the conditional form

Parent basis (defect): "shared (company-less) calendars get no computed reference, so the rate falls back to 100".

**REC-RSRC-24 basis R1:** "The full-time reference hours are recomputed from the company default calendar whenever a company calendar's own weekly hours change, and a manual value is overwritten. For company-less (shared) calendars the compute **skips** the record without zeroing it. On creation, the reference is **seeded from the default (session) company's calendar**, unless a company or value is supplied, and it stays **user-editable**. The rate therefore falls back to 100 **only when the reference is empty or zero**. Otherwise it follows weekly hours ÷ reference with no clamp. The rate is a **non-stored** compute." (A2 F-04 caveat restored; A2 addendum 4.2.) Class GAP (unchanged). Proof link: **PR-06R1 → PC-RSRC-08R1 (static), PC-RSRC-R06R1 (runtime)**, replacing PC-RSRC-08 and R06 for REC-24.

### 3.2 S-A: runtime proof links for GAP/CONTRADICTION items that had static links only

| REC ID | Class | Parent proof link | **R1 proof link** |
|---|---|---|---|
| REC-RSRC-06 | CONTRADICTION | PC-RSRC-06 | PC-RSRC-06 + **PR-11 → PC-RSRC-R11** |
| REC-RSRC-19 | GAP | PC-RSRC-06 | PC-RSRC-06 + **PR-11, PR-12 → PC-RSRC-R11, R12** |
| REC-RSRC-11 | GAP | PC-RSRC-12 | PC-RSRC-12 + **PR-13 → PC-RSRC-R13** |
| REC-RSRC-20 | GAP | PC-RSRC-12 | PC-RSRC-12 + **PR-13 → PC-RSRC-R13** |
| REC-RSRC-27 | GAP | PC-RSRC-17, 21 | PC-RSRC-17, 21 + **PR-14 → PC-RSRC-R14** (destructive toggles; isolated instance only) |
| REC-RSRC-28 | GAP | PC-RSRC-03, 07 | PC-RSRC-03, 07 + **PR-15 → PC-RSRC-R15** (includes recording the framework admin → ERP-manager implication) |

REC-19 reachability note, added to the basis: the form onchange rejects a two-week edit that lacks exactly one section per week, so the no-section state is reachable only through non-form writes (RPC, import, or code).

### 3.3 S-B: Lane B label corrections

Rule R1: **NOT_APPLICABLE** is reserved for pure static declarations, such as ACL rows or field declaration flags. Behaviour that can be observed at runtime is **UNCORROBORATED** when there is no observation.

| REC ID | Item | Parent | **R1** | Reason |
|---|---|---|---|---|
| REC-RSRC-06 | Section/overlap constraint | NOT_APPLICABLE | **UNCORROBORATED** | Constraint behaviour can be observed on save |
| REC-RSRC-12 | Leave date validation; company compute | NOT_APPLICABLE | **UNCORROBORATED** | Validation error and computed company can be observed |
| REC-RSRC-13 | Efficiency DB check; flexible without calendar | NOT_APPLICABLE | **UNCORROBORATED** | DB rejection can be observed |
| REC-RSRC-16 | Default-calendar provisioning; restrict delete | NOT_APPLICABLE | **UNCORROBORATED** | Provisioning and delete refusal can be observed |
| REC-RSRC-18 | Timezone default chain | NOT_APPLICABLE | **UNCORROBORATED** | Defaults can be observed on create |
| REC-RSRC-19 | Two-week no-section / untyped rows | NOT_APPLICABLE | **UNCORROBORATED** | Save outcome can be observed (PC-RSRC-R11/R12) |
| REC-RSRC-14 | Week parity | NOT_APPLICABLE | **UNCORROBORATED** | *Added by the owner stage beyond S-A's list:* the computed week type of a date can be observed at runtime |

Kept as NOT_APPLICABLE: REC-RSRC-03 (ACL rows) and REC-RSRC-15 (mixin field declaration flags). Lane B column after R1: NOT_APPLICABLE 2, UNCORROBORATED 33 (including the new items in 3.5). FAIL 0.

### 3.4 S-C: conditional materiality of naive-as-UTC

The parent section 7 bullet "The naive-as-UTC rule is material (7-hour shift)" is **replaced** by: "Conditionally material. The rule matches the framework convention (stored datetimes are naive UTC, and the planning helpers return naive UTC for naive input). Harm arises only when a consumer passes naive **local** wall-clock values. For Asia/Bangkok that means a 7 h shift that can cross a day boundary. No such caller is identified in `resource`. Consumers in other modules remain open." (A2 addendum 4.1.) REC-RSRC-09 stays UNKNOWN_PENDING_PROOF. PC-RSRC-10 is re-labelled ILLUSTRATION by PROOF (S-D) and no longer counts as proof for REC-09. Its static basis is PC-RSRC-09.

### 3.5 N1–N7: new REC items (UNKNOWN_PENDING_PROOF)

These are A3 source-visible candidates, verified by A2 (addendum 4.4) and promoted here. Each is a statically predicted effect that depends on runtime or framework behaviour.

| REC ID | Source item | A1 | A2 (addendum R1) | REC class | Lane B | Proof link | MODULE+STD-QID lineage |
|---|---|---|---|---|---|---|---|
| REC-RSRC-29 | N1 | (not stated) | Clearing or changing a calendar's company rebuilds its global leaves from the new company's default calendar. Clearing it empties them. Whether they are deleted or left calendar-less is framework behaviour. If left calendar-less, they would apply to all calendars (REC-20 chain) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-16 → PC-RSRC-22, R16 | resource+STD-Q04, Q27, Q49 |
| REC-RSRC-30 | N2 | (not stated) | Calendar-level computations (no resource) subtract calendar-less leaves of **any** company visible to the caller, because the company guard applies only when a resource is set | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-17 → PC-RSRC-23, R17 | resource+STD-Q27, Q28, Q38 |
| REC-RSRC-31 | N3 | (not stated) | The cached weekday lookup counts section and break rows as worked and is keyed on calendar id only. **Precision (DISPUTE, partial):** it is called in the module by the works-on-date helper, which itself has no caller in the module files | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-18 → PC-RSRC-24a, 24b, R18 | — (no clear fit) |
| REC-RSRC-32 | N4 | (not stated) | The leave end-date fallback reads the company on the whole recordset, so a batch with more than one leave and no user or context tz may raise a singleton-type error | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-19 → PC-RSRC-25, R19 | resource+STD-Q54 |
| REC-RSRC-33 | N5 | (not stated; A2 F-09 omission) | Leaving two-week mode also switches duration-based mode off with no notice | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-20 → PC-RSRC-26, R20 | resource+STD-Q04 |
| REC-RSRC-34 | N6 | (Proof R1, superseded) | The tz is frozen at the first **matching** (leave, resource) pair. Instants stay correct. The likely effect is on output tzinfo and whole-day widening of flexible leaves | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-21 → PC-RSRC-27, R21 | resource+STD-Q50 |
| REC-RSRC-35 | N7 | (not stated) | Overlap is checked on one weekly timeline, so out-of-range hours (REC-05/23) can collide across adjacent days. "Per weekday" is an approximation | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-22 → PC-RSRC-28, R22 | resource+STD-Q08, Q54 |

### 3.6 `resource` counts after R1

MATCH 7 · GAP 11 · CONTRADICTION 1 · UNKNOWN_PENDING_PROOF **16** (the parent 9 plus REC-RSRC-29..35) · **Total 35**. Lane B: NOT_APPLICABLE 2, UNCORROBORATED 33, FAIL 0.
R1 STD-QID lineage: mapped **16** distinct, the same set as the parent. The new items map only to STD-QIDs already in the parent set (Q04, Q08, Q27, Q28, Q38, Q49, Q50, Q54), so no STD-QID is added. REC items with no clear fit: REC-RSRC-07, 08, 14, 17, 31. MVQ lineage is still unavailable (GMVQ backlog).

### 3.7 S-E lineage (REC side)

This REC addendum records the REC sha256 values that the PROOF addendum R1 must consume and cite: resource REC `e2adc10a1f346bb5dc1fe73100d3187c485a1208c12af6bc3a4732475a0fe259` and resource_mail REC `1ec90af273af437692663390db5e4d182cf4490204385dbf67d25fefed8cb26f`, plus this addendum (hash recorded by PROOF at intake). The parent's order problem (REC finalized after the parent Proof's static execution) cannot be repaired retroactively and remains **INCONCLUSIVE** for the parent. New cases are keyed to REC ids.

---

## 4. `resource_mail`

### 4.1 M-A: REC-RMAIL-06 exposure list

**REC-RMAIL-06 basis R1:** "The avatar card can expose the linked user's **email, phone, share flag, presence, avatar image, and the linked-user reference** (id and display name) to any internal user who can read the resource, meaning resources in **the session's active companies or with no company** (A3 N-1 precision). The avatar is a plain non-stored compute copying the user's avatar, not a related field. Whether it and the related fields are evaluated with elevated rights or with the caller's rights is framework behaviour and is not proven." Class GAP (unchanged). Proof link: **PR-03R1 → PC-RMAIL-04, PC-RMAIL-07 (static), PC-RMAIL-R03R1 (runtime)**.

### 4.2 M-B: labels and REC hash lineage

| REC ID | Parent Lane B | **R1** | Reason |
|---|---|---|---|
| REC-RMAIL-02 | NOT_APPLICABLE | **UNCORROBORATED** | The random colour default can be observed on create |

Kept NOT_APPLICABLE: REC-RMAIL-05 (declared absence of models, ACLs and similar). Lane B after R1: NOT_APPLICABLE 1, UNCORROBORATED 6, FAIL 0. REC hash lineage: see 3.7. Counts are unchanged: MATCH 2 · GAP 2 · CONTRADICTION 0 · UNKNOWN_PENDING_PROOF 3 · Total 7.

---

## 5. Handoff to PROOF (R1)

New or replacement proof requirements passed to PROOF: bus PR-BUS-04R1, 05R1, 06R1, 09R1, 10, 11 (and PR-BUS-08 as MEASUREMENT); digest PR-DGST-04R1, 05R1, 08R1, 11 (and PR-DGST-02 as MEASUREMENT); resource PR-06R1, PR-11..PR-22; resource_mail PR-03R1. PROOF must predeclare every new or replacement case with a timestamp and sha256 **before** executing anything, cite the REC sha256 values it consumes (S-E), and keep all runtime cases NOT-EXECUTED while the device is offline.

## 6. Limitations

- REC reconciles documents. The owner stage's source re-checks are recorded in the A2 addendum, and this addendum only references them.
- No Lane B evidence exists, so nothing here is runtime-corroborated.
- No percentages, no Formal Coverage claim, and no QID answered. The banks were not edited. No git operations were run.
