# [SMEPLUS-26-09-04-INV-MTI-RULING-CONSOLIDATION-001]
# 09 — Remaining Blocker Register After Rulings

Control Level: `/L9999.9999`
Status: `15 NEW ITEMS RAISED — 3 DECISION BLOCKERS RULED BY BOSS — 0 FINDINGS CLOSED — ALL CARRIED IDENTIFIERS PRESERVED UNCHANGED`

---

## 1. Lane Vocabulary In Force

This register uses **the authorization's lane vocabulary**, which is the vocabulary the AAS+ / PMO review and the invariant-set package both used.

| Letter | Meaning here |
|---|---|
| **A** | Inventory-owned architecture / control / data identity |
| **B** | Accounting COGS / valuation / period-close dependency |
| **C** | Business SME / Thai user / statutory validation |
| **D** | Clean-room / governance / audit veto / Boss ruling |
| **E** | Cross-module joint decision |
| **F** | Duplicate / superseded / no-action |

`REV-F-03` — the lane-letter collision with R4's own registers — **remains open**. R4's Lane C means *COGS-gated*; here Lane C means *Business SME / Thai*. Until Boss ratifies one vocabulary programme-wide, every cross-document lane reference stays ambiguous. **This session adds a third document using the authorization's vocabulary; it does not resolve the collision.**

---

## 2. Status Classification In Force

The authorization at §9.4 mandates seven status values. Every item in this register carries exactly one.

| Status | Meaning As Applied Here |
|---|---|
| `DECIDED BY BOSS` | A ruling has settled the question. Nothing is thereby built, proven or closed |
| `SPECIFIED BUT NOT PROVED` | A statement and acceptance criteria exist. No implementation, no verification |
| `PROOF REQUIRED` | The proposition is definable and the proof is writable, but cannot execute |
| `BLOCKED BY ACCOUNTING COGS GAP` | `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| `BLOCKED BY CLEAN-ROOM RELIANCE` | `C-05` containment or `RISK-CR-02` residual scope |
| `BLOCKED BY PRIVATE COMPANY CLASSIFICATION` | Cannot be classified pool-safe or Private-Company-required; AAS+ advice `29` §7 |
| `HOLD` | Blocked for a reason none of the above captures |

---

## 3. `DECIDED BY BOSS`

| ID | Item | Lane | Decision | What Is **Not** Thereby Closed |
|---|---|---|---|---|
| `MTI-D-01` | Product master scope | D → A | **Option B — company-owned product master** | `RC-F-01` re-specification; `RC-F-03` mapping layer; `RC-F-04` `MTI-D-04` dependency. **No finding, proof, gap or capability** |
| `MTI-D-02` | Authorization granularity | D → A | **Company + Warehouse + Operation-Type** | `RC-D-01` location axis; `RC-F-05` execution-family axis. Build half of `U-01` |
| `MTI-D-03` | Tenant-changeable boundary | D → A | **Platform-owned Core + Tenant Config Overlay**, Private Company through Gate | `RC-F-06` open-ended list; `RC-F-07` Private Company undefined; `GAP-MD-14` regeneration and switch-off halves |
| `RISK-U01` / `U-01` | Warehouse- and operation-level authorization scope | D → A | **Discharged as a decision by `MTI-D-02`** | The **build half**. `L9-03` is now `DEFINABLE`, not proven |

**4 items. 0 findings closed. 0 proofs achieved. 0 capabilities built.**

---

## 4. New Items Raised By This Session

### 4.1 Findings — `RC-F-01` .. `RC-F-09`

| ID | Finding | Lane | Severity | Owner | Status | Next Action |
|---|---|---|---|---|---|---|
| `RC-F-01` | **`MTI-11` contradicts `MTI-D-01`.** The canonical invariant set anchors product definitional identity to `tenant`; Boss ruled `company`. `XCR-03`, `04` §4.1 and matrix rows 5-7 follow it | **A** | **BLOCKING for reliance on `03_INVENTORY_MULTI_TENANT_INVARIANT_SET.md`** | Inventory | `PROOF REQUIRED` after re-specification | Re-specify `MTI-11` and dependents to a company anchor. **No design may be built against file `03` as published** |
| `RC-F-02` | **`XCR-03` is eliminated** and `04` §4.1's shared-surface proof obligation for product is void. The `MTI-22` register falls from 4 entries to 3 | **A** | MATERIAL — **favourable** | Inventory | `SPECIFIED BUT NOT PROVED` | Correct the register. A completeness claim over a register must be corrected when an entry ceases to exist |
| `RC-F-03` | **The controlled mapping / provenance layer does not exist.** `D-01` rules 5 and 8 require it; no published design specifies it. Deduplication is now prohibited as the control, and nothing replaces it | **A** design / **D** authorization | **BLOCKING** for group-level reporting | Inventory + Boss | `HOLD` | Commission the specification. Ten required properties enumerated at `06` §5.3. **Requirements are not a design** |
| `RC-F-04` | **`D-01` is not fully operable until `MTI-D-04` is ruled.** Rules 5 and 8 presuppose an authorized aggregation mechanism, which is exactly `MTI-D-04`'s subject | **D** | MATERIAL | **Boss** | `HOLD` | Rule `MTI-D-04`. Under Option B the group-view need is **larger**, not smaller |
| `RC-F-05` | **The execution family carries no operation-type axis.** `CTX = (tenant, company, warehouse?, location?)`; `AUTH` adds operation type. `D-02` rule 8 requires background jobs to carry it, and no invariant states that they do | **A** | MATERIAL | Inventory + SaaS Foundation | `SPECIFIED BUT NOT PROVED` — the gap is in the specification | Extend `MTI-29` / `MTI-30` or state the `CTX`-to-`AUTH` relationship explicitly |
| `RC-F-06` | **The tenant-configurable enumeration is open-ended.** `D-03` §3 ends with *"other approved Inventory configuration/master records"*; `L9-04`'s boundary half requires the enumeration to be *"published and complete"* | **D** then **A** | MATERIAL | Boss / product scope | `HOLD` | `RC-D-02`. `L9-04` stays `PARTIALLY DEFINABLE` until the list closes |
| `RC-F-07` | **Private Company is a second isolation topology with no invariants, no matrix rows, no proofs and no scenarios.** All 50 invariants, 8 L9 proofs and 30 `MTP-*` scenarios are written for the shared pool | **D** then **A** | MATERIAL, trending BLOCKING | Boss + Inventory | `BLOCKED BY PRIVATE COMPANY CLASSIFICATION` | `RC-D-03`. Six specifications enumerated at `05` §5 |
| `RC-F-08` | **Product Category is tenant-configurable and COGS-blocked at once.** `D-03` names it configurable; `R4-F-10` records it owns reporting, put-away **and costing**; the costing split is `GAP-FS-02`, precondition-blocked on `JT-01`, **NOT DECIDABLE** | **A** config / **B** costing | MATERIAL | Inventory + Joint | `BLOCKED BY ACCOUNTING COGS GAP` | Do not permit configuration of the costing facet until `GAP-FS-02` resolves. The reporting and put-away facets are separable |
| `RC-F-09` | **Payment has no published context obligation.** Named in this authorization's theme 13; absent from the invariant set's seven-module obligation table | **A** | WATCH | Inventory | `SPECIFIED BUT NOT PROVED` — by omission | The successor prompt must either state Payment's obligation or record why it has none |

### 4.2 Decision items — `RC-D-01` .. `RC-D-04`

Each requires a decision this session is not empowered to take. **None is an investigation.**

| ID | Decision Required | Lane | Owner | Why It Cannot Be Taken Here | Consequence If Deferred |
|---|---|---|---|---|---|
| `RC-D-01` | **Location axis disposition.** `MTI-D-02` names three dimensions and not `location`. The invariant set's option 3 bundled *"location- or operation-class-level"*. Is location excluded as an authorization axis, or simply not required? | **D** | **Boss** | It is a scope clarification of a Boss ruling. Only Boss may say what a Boss ruling covers | Five matrix rows (`04` rows 4, 14, 19, 22, 23) that the invariant set assigned to the finest filter stay unsettled. **Design proceeds on the three axes ruled**; the residual is registered, not assumed |
| `RC-D-02` | **Closure of the configurable-record enumeration.** What closes *"other approved Inventory configuration/master records"*, and who approves an addition? | **D** then **A** | **Boss / product scope** | A product-scope decision with an authorization consequence | `RC-F-06`; `L9-04` boundary half stays incomplete; `RC-P-35`, `RC-P-36`, `RC-P-37` stay `DEFINABLE — CONDITIONAL` |
| `RC-D-03` | **Private Company escalation criteria**, and the disposition of pool prohibitions **4** (authorization-engine divergence) and **5** (immutable-event-logic divergence) — Private-Company-eligible, or prohibited outright everywhere? | **D** | **Boss** | `D-03` rule 6 reserves Private Company separation to an explicit Gate record and Boss ruling. AAS+ advice `29` §6 addresses prohibitions 1, 2, 3 and 6 only | `RC-F-07`; `RC-P-45`, `-46`, `-48` stay `NOT DEFINABLE`; **4 of 7 live requirement classes stay unclassifiable** and therefore `HOLD` |
| `RC-D-04` | **Ownership and commissioning of the controlled mapping / provenance layer.** Who owns it, and is it commissioned now or after `MTI-D-04`? | **D** then **A** | **Boss** | It is a commissioning decision, and it is entangled with `MTI-D-04` | `RC-F-03`; `RC-P-20` and `RC-P-21` stay `NOT DEFINABLE`; the group-view need is met by export, which `MTA-09` names as the worst outcome |

### 4.3 Evidence notes

| ID | Note | Lane | Severity | Owner | Action |
|---|---|---|---|---|---|
| `RC-EVIDENCE-NOTE-01` | The authorization's mandatory list omits the three AAS+ advice records (`25`, `27`, `29`) that accompany the rulings and are materially load-bearing | **D** | WATCH | PMO | Name them in any successor prompt. **No evidence was unavailable** |
| `RC-EVIDENCE-NOTE-02` | This authorization has **no** non-existent-filename defect, unlike the invariant-set authorization's `EVIDENCE-NOTE-01`. Recorded because the improvement is worth registering | **D** | Observation | PMO | None |

---

## 5. `BLOCKED BY ACCOUNTING COGS GAP`

`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` applies to every item below. **The dependency is not lifted by any ruling, and no ruling touches it.** The R4 review independently confirmed **10 of 10** dependency areas correctly locked.

| ID | Item | Lane | Status After Rulings |
|---|---|---|---|
| `JT-01` | Which concept owns valuation policy — **NOT DECIDABLE** | E | Unchanged. **BLOCKING** |
| `JT-02` | Standard / average / FIFO | E | Unchanged |
| `JT-03` | Periodic versus perpetual — **no stable reference pattern exists to imitate** | E | Unchanged |
| `JT-04` | COGS at delivery — **NOT DECIDABLE** | E | Unchanged |
| `JT-05` | Return cost basis — **NOT DECIDABLE** | E | Unchanged |
| `JT-06`, `JT-07` | Period close and late movement | E | Unchanged |
| `JT-08` | Landed cost allocation and posting — **Audit VETO retained** | E | Unchanged |
| `JT-10` | Inter-company transfer treatment | E | **Complicated by `D-01`** — the two sides are now unrelated product identities; correlation must be carried by the relationship and never inferred from product |
| `GAP-FS-07` | Cross-company transfer path **never traced end to end** | B | Unchanged. **BLOCKING** |
| `GAP-MD-09` | Consignment and ownership policy | B | Unchanged |
| `GAP-FS-02` | Product category costing facet split | B | **Complicated by `RC-F-08`** — the object is now tenant-configurable |
| `R4-F-20` | Retroactive compensation sequenced by creation order | B | Unchanged — `L13-01` |
| Handoff elements **4** and **7** | Financial recognition timing; valuation / cost basis | B | Unchanged — **not suppliable** on eight of ten material handoffs |
| `L9-06` value half | No cross-company cost leakage | B | Unchanged — `PARTIALLY DEFINABLE` |
| `RC-P-22`; `RC-P-34` value half; `RC-P-39` costing facet | New proof requirements carrying the lock | B | `HELD` |
| `AAS-V-03` | Veto on cross-company valuation content | D | **In force. Unchanged** |

**16 entries. 10 of 10 COGS dependency areas remain locked. Nothing here is upgraded by any ruling, and no ruling was expected to touch it.**

---

## 6. `BLOCKED BY CLEAN-ROOM RELIANCE`

| ID | Item | Lane | Status |
|---|---|---|---|
| `C-05` / `RISK-C05` | Clean-room containment. Both pre-remediation commits **confirmed reachable in a fresh clone by the R4 review**. Only the interim warning label has been executed; options (a) accept in writing, (b) restrict access, (c) rewrite history are **Boss-only and outstanding** | D | **BLOCKING for downstream reliance. This package inherits the lock** |
| `RISK-CR-02` | Residual independent clean-room re-audit — Layer 2 findings, quarantine citations, Thai content | D | **Not further discharged by this session.** This session performed no first-hand reference-system inspection and accessed no quarantine |
| `U-07` / `RISK-U07` | Two competing 9 Veto Council charters, both claiming Boss approval | D | **BLOCKING for challenge finality.** This session's `11` verdict inherits the same conditionality |

**This package is subject to the same reliance lock as every package it consolidates.** A consolidation of locked evidence is itself locked.

---

## 7. `BLOCKED BY PRIVATE COMPANY CLASSIFICATION`

| ID | Item | Lane | Why |
|---|---|---|---|
| `RC-F-07` | Private Company topology has no invariants, proofs or scenarios | D → A | No criteria; no delta; no transition semantics |
| `RC-P-45`, `RC-P-46`, `RC-P-48` | Escalation classification; control-rule delta; pool-to-Private transition | A | `NOT DEFINABLE` |
| Requirement class — different posting treatment | A / B | Pool prohibition 3; escalation route indicated but criteria absent; **and the posting treatment is itself COGS-held** |
| Requirement class — different authorization shape | A | Pool prohibition 4; **`29` §6 does not address prohibition 4** — `RC-D-03` |
| Requirement class — different isolation rule | A | Pool prohibition 6; escalation indicated, but `RC-F-07` point 1 means the L9 proofs may not transfer |
| Requirement class — schema-level divergence | A | Pool prohibition 2; escalation indicated; criteria absent |

**4 of 7 live requirement classes cannot be classified today** (`05` §4). The `HOLD` condition in AAS+ advice `29` §7 is **live and general**, not exceptional.

---

## 8. `SPECIFIED BUT NOT PROVED`

Items with a complete statement and acceptance criteria, no implementation, and no verification.

| ID | Item | Lane | Note |
|---|---|---|---|
| Handoff element **10** | `WHICH Company / Tenant` | A | **`specified, not built, not verified`.** `AAS-V-01` in force; **no other wording may be substituted.** Unchanged by any ruling |
| `MTI-01` .. `MTI-50` | The 50 invariants | A | Specified. **`MTI-11` additionally out of conformance — `RC-F-01`** |
| `HF-CTX-01` .. `HF-CTX-09` | The nine context handoff fields | A | Specified; obligations **widened** by `D-02` |
| `XCR-01`, `XCR-02`, `XCR-04` | The cross-context register, after `XCR-03`'s elimination | A | `XCR-01` **INCOMPLETE**; `XCR-02` conditional on `MTI-D-04`; `XCR-04` conditionality resolved by `D-03`, content still bounded by `RC-F-06` |
| `MTI-F-01` .. `MTI-F-06` | The six invariant-set findings | A | **0 closed.** 2 narrowed, 3 widened, 1 unchanged |
| `RC-F-02`, `RC-F-05`, `RC-F-09` | Three of this session's findings | A | Specification-level items |
| The twelve control rules at `04` §4 | The consolidated control model | A | Derived from rulings; nothing conforms to it yet |

---

## 9. `PROOF REQUIRED`

The 48 proof requirements at `07` and `08`. **`0 of 48` executable today**, because no implementation exists.

| Group | Count | State Summary |
|---|---:|---|
| `RC-P-01` .. `RC-P-08` — product isolation, non-colliding duplication | 8 | 7 `DEFINABLE`; `RC-P-08` **`NOT DEFINABLE`** — needs the privileged-bypass path enumeration |
| `RC-P-09` .. `RC-P-16` — warehouse and operation-type authorization | 8 | 7 `DEFINABLE`; `RC-P-16` conditional on Thai input |
| `RC-P-17` .. `RC-P-22` — report prevention and mapping | 6 | 3 `DEFINABLE`; 2 **`NOT DEFINABLE`** (`RC-F-03`); 1 `HELD` |
| `RC-P-23` .. `RC-P-28` — scheduler, background, API, import, export | 6 | 3 `DEFINABLE`; `RC-P-23` conditional (`RC-F-05`); `RC-P-25` partial (`RISK-C02`); `RC-P-28` conditional (`MTI-D-04`) |
| `RC-P-29` .. `RC-P-31` — immutable audit trail | 3 | 2 `DEFINABLE`; `RC-P-31` definable but **would pass on a broken system** without `RISK-C02` |
| `RC-P-32` .. `RC-P-34` — cross-module handoff | 3 | 2 `DEFINABLE`; `RC-P-34` value half `HELD` |
| `RC-P-35` .. `RC-P-48` — configuration overlay and Private Company | 14 | 7 `DEFINABLE`; 4 conditional; 4 **`NOT DEFINABLE`**; 1 `HELD` |

**48 requirements. 0 proofs. 0 executable.**

---

## 10. `HOLD` — Everything Else Carried Unchanged

Nothing in this table is affected by any of the three rulings. Each is carried because the programme cannot complete while it stands.

| ID | Item | Lane | Severity | Owner |
|---|---|---|---|---|
| `RISK-U03` / `GAP-FS-10` | The multi-tenant invariant **capability** | A | **BLOCKING** | Inventory + SaaS Foundation |
| `RISK-C02` / `IV-06` | Deterministic movement attempt identity — severity ruling outstanding | A build / D severity | **BLOCKING** | **Boss** |
| `GAP-FS-08` / `CN-36` | Migration and replay provenance reference — **scope widened by `D-01` rule 7** | A | **BLOCKING** | Migration + Inventory |
| Privileged-bypass path audit | Started once, never completed | A | **BLOCKING for `L9-01`** | Inventory + SaaS Foundation |
| `GAP-MD-14` / `SAAS-04` | Regeneration, switch-off guards, versioning — **boundary half narrowed by `D-03`; these three unchanged** | A | MATERIAL | Boss / product |
| `GAP-MD-29` | PDPA scope for Inventory documents — **zero coverage anywhere** | D | MATERIAL, trending BLOCKING | Boss + Legal |
| `MTI-D-04` | Cross-company visibility policy — **promoted by `RC-F-04`** | D | **BLOCKING for `RC-F-03`** | **Boss** |
| `MTI-D-05` | PDPA and tenant erasure scope | D then Legal | MATERIAL | Boss + Legal |
| `MTI-D-06` | Physical consolidation across companies — handling unit carrying two companies' goods | C then A | MATERIAL | Thai panel then Inventory |
| `GAP-FS-11` / `GAP-MD-30` | Thai user validation — **`0 of 78`**, unremedied since 2026-08-30. **Surface widened**: every record class in `D-03` §3 and every operation type in `D-02` §5 is a further unvalidated label | C | **BLOCKING for user-facing design** | **Boss to commission** |
| `TH-HOLD-01` .. `TH-HOLD-09` | Thai statutory holds, including `TH-HOLD-06` branch-versus-warehouse | C statutory | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `GAP-FS-19` | Manufacturing scope ruling | D | Open | Boss |
| `SME-Q-02`, `SME-Q-03` | Routed business-SME questions — **no AI may answer either** | C | Open | Business SME |
| `R4-F-01` .. `R4-F-25` | The 25 R4 findings — **0 closed**, 6 narrowed, 1 complicated, 18 unchanged | A / B / C | Various | Inventory |
| `R4-F-16` | Three handoff elements unsuppliable, none for COGS reasons | A | **BLOCKING — stands in full** | Inventory |
| `REV-F-01` | Depth shortfall — two reachable leads unfollowed | A / D | MATERIAL | Team A / Track 07 |
| `REV-F-02` | Element 14 contractually conditional, not universal | D | MATERIAL | PMO |
| `REV-F-03` | Lane vocabulary collision | D | MATERIAL | Boss / PMO |
| `REV-F-04` | 92 open-item roll-up not reconstructable; no crosswalk exists | D | MATERIAL | Boss / PMO |
| `C-04` / `N-CONC-01`, `N-A13-01` | Two reachable leads. **Not read by this session either** | A | CONFLICTING | Team A |
| `MTI-CH-01` | Whether `STORE` enforcement is achievable in a chosen technology | A | Open — **a Team B question, not approached** | Team B, when authorized |
| `MTI-CH-02` | The invariant set has not been minimised | A | WATCH | Inventory |
| `MTI-CH-03` | `MTP-28`, `-29`, `-30` cannot be run even after implementation | A | Open | Inventory |
| `L13-MT-01` .. `L13-MT-03` | Deferred execution context; tenant lifecycle; authorized cross-company traversal | A / D | Open | Inventory + Boss |
| `AAS-V-01` | Veto on recording element 10 as supplied | D | **IN FORCE** | AAS+ |
| `AAS-V-02` | Veto on implementation start before the three shape decisions are ruled | D | **Stated precondition satisfied; not discharged.** See `11` §5 | AAS+ / Boss |
| `AAS-V-03` | Veto on cross-company valuation content while the COGS Gap stands | D | **IN FORCE** | AAS+ |
| `EVIDENCE-NOTE-01`, `-02` | Invariant-set evidence notes | D | WATCH | PMO |

---

## 11. Roll-Up

| Measure | Result |
|---|---:|
| Decision blockers ruled by Boss | **3** (`MTI-D-01`, `-02`, `-03`) |
| Upstream decisions discharged | **1** (`U-01`, decision half) |
| New findings raised | **9** — `RC-F-01` .. `RC-F-09` |
| New decision items raised | **4** — `RC-D-01` .. `RC-D-04` |
| New evidence notes | **2** |
| **Total new items** | **15** |
| New items by lane | A 5 · A/B 1 · A/D 1 · D 6 · D-then-A 2 |
| New proof requirements specified | **48** — `RC-P-01` .. `RC-P-48` |
| Proof requirements executable today | **0** |
| Findings closed | **0** |
| Proofs achieved | **0 of 8** |
| Cross-proof scenarios verified | **0 of 22** |
| Handoffs contract-compliant | **0 of 10** |
| Joint decisions ready | **0 of 12** |
| Thai validations | **0 of 78** |
| Inherited dependencies discharged | **0** |
| Vetoes discharged | **0** |
| Carried identifiers renumbered or retired | **0** |

**No open-item roll-up total is asserted by this session.** `REV-F-04` records that the 92 figure is not independently reconstructable and that no open-item crosswalk exists. The invariant-set session declined to assert a total on those grounds; this session declines on the same grounds. Adding fifteen items to a total that cannot be reconstructed would produce a number that looks precise and is not. **The fifteen new items are enumerated exactly; the roll-up awaits the crosswalk PMO has been asked to publish.**

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
