# G01 PLATFORM_BASE — RED TEAM Reconciliation Addendum, Remediation Cycle R2, Batch C — `web`, `mail`

**[ADDENDUM — RECONCILIATION (REC) STAGE]**

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RECONCILIATION (REC)** addendum only. No existing REC or REC-delta file is edited |
| Group / Modules | G01 PLATFORM_BASE / `web`, `mail` |
| Date | 2026-09-27 |
| Cycle | Remediation **R2**, Batch **C** — RES-W1, RES-M1, RES-M2 (routes to PROOF R2C), RES-M3, RES-M4 |
| Upstream addendum consumed (pinned) | `G01_A2_REVIEWS/G01_R2C_A2_ADDENDUM_20260927.md` sha256 **`05eb2519a9606c043913114900639a5e24cb0797ee79ae8c65808c16d039d11c`** |
| D1-level mail REC re-frozen (RES-M3; see §3) | `G01_RECONCILIATION/G01_MAIL_REC_DELTA_D1_20260927.md` sha256 **`bb5de020246be21a802880bfa3d0b411a6c430c84237cf57ae6e14bc59b8812f`**, re-hashed and pinned at **2026-09-27T16:35:40Z**, before this addendum closes and before any R2C Proof step is treated as settled |
| D1-level web REC (reference; unaffected by RES-W1, which is a scan-table addition only) | `G01_RECONCILIATION/G01_WEB_REC_DELTA_D1_20260927.md` sha256 `b89931533a23ace1fc25d9cecd5febd2e305b84cf83e4e94aa0a2f40f2c00985` |
| A3 residual source | `G01_A3_CHALLENGES/G01_B3B_A3_RECHECK_R1_20260927.md` §7 (RES-W1..RES-M4) sha256 `13e06b8c8ae6d387c7ad763f4f36525e457660b5ec7d860c49cbdcccd8bac316`; underlying mail A3 D1 items A3-MD-13/14/16/19 in `G01_A3_CHALLENGES/G01_MAIL_A3_DELTA_D1_20260927.md` sha256 `004d3df2fa30cd8c741cd3bd526bf302301ef849aac478959bbab55bfbfef1c7` |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

### 0.1 Rule-compliance table

| Rule | Compliance in this REC addendum |
|---|---|
| C1-B rule 1 | Not applicable — no Lane B cell is reassigned here; the mail D1 Lane B column stands as REC D1 recorded it |
| C1-B rule 2 | Not applicable to REC — no Proof case text is written here |
| C1-B rule 3 (scan all A1 item classes) | **Complied — this is RES-W1's fix.** §1 names BR-2'/BR-3' explicitly in the web D1 scan |
| C1-B rule 4 (A2 → REC sha → Proof predeclare → Proof execute) | **Complied.** This addendum consumes A2 R2C by sha256 (above) and is frozen (sha computed on close, §5) before PROOF R2C's predeclaration. §3 additionally cures the *substance* of the earlier D1-level ordering defect for the three items A2 R2C independently re-derived |
| C1-B rule 5 | Not applicable to REC |
| MD-07 (anchor-only evidence) | This addendum invents no new source facts; it re-derives counting and scan-table corrections from artifacts already anchor-verified by A2 R2C and by the D1-level REC/A3 files themselves |
| MD-08 (bounded enumeration) | §2's recount states exactly which rows were re-classified and why; it does not claim a new completeness bound beyond the two rows named |

Clean-room note: neutral paraphrase only. No vendor code. No percentages. No Formal Coverage claim. **No QID is answered** — QID references below are lineage only. No git operations. No existing artifact edited.

---

## 1. RES-W1 — `web` D1 item-class scan: BR-2'/BR-3' named

Per A2 R2C §1, the following two rows are added to the web D1 item-class scan record (extending, not replacing, `G01_B3B_REC_ADDENDUM_R1_20260927.md` §7's `web` row, which covered base A1 classes but not these D1 items):

| REC ID | D1 item | Class | Basis | Lane B | Proof link | QID lineage |
|---|---|---|---|---|---|---|
| REC-WEB-D17 | BR-2' (supersedes parent BR-2: export permission applies to all record-based export formats; coupled to Access Rights; does not restrict read APIs) | **MATCH** (unchanged from D1 REC) | PC-WEB-10, PC-WEB-12 (shared with REC-WEB-D20/D21) | UNCORROBORATED | PC-WEB-10, 12 | **Q030, Q050** |
| REC-WEB-D18 | BR-3' (refines parent BR-3: DB lifecycle requires `list_db` enabled plus the master secret; first caller sets the secret on a default configuration) | **MATCH** (unchanged from D1 REC) | PC-WEB-15, PC-WEB-16 (shared with REC-WEB-D23/D24/D25/D26) | UNCORROBORATED | PC-WEB-15, 16 | **Q036, Q037** |

No class changes; nothing is re-opened. This closes RES-W1: both D1 business-rule items now have a named row in the scan record, with the QID lineage each shares with its underlying claim-level items stated explicitly rather than left implicit.

---

## 2. RES-M1 — `mail` D1 REC recount (A3-MD-13)

**Finding applied:** `G01_MAIL_REC_DELTA_D1_20260927.md` §2.4 counts two A2-`OUT_OF_SCOPE` "unchanged" rows as classified delta items — D1-07 (G1, G6, G7, G10, G11) as **GAP**, and D1-22 (CRQ-MAIL-02, 03, 04, 06, 08, 10, 12) as **UPP** — while `G01_WEB_REC_DELTA_D1_20260927.md` §3.4 carries its equivalent rows (CRQ-WEB-08; the G-1/G-A1-3/G-A1-4/G-5 row) as **"Carried, no delta: 2"**, kept out of its "Total classified: 46". REC's own rule R-b ("an A2 OUT_OF_SCOPE row takes the base REC class of its underlying items") governs what class such a row *reads as*, not whether it is counted a second time as a new delta item — the underlying items are already counted once in the base REC (56 items for `mail`).

### 2.1 Before (as `G01_MAIL_REC_DELTA_D1_20260927.md` §2.4 states)

| Class | Count |
|---|---|
| MATCH | 19 |
| CONTRADICTION | 9 |
| UNKNOWN_PENDING_PROOF | 18 (includes D1-22) |
| GAP | 4 (includes D1-07) |
| **Counted total** | **50** |
| Merged duplicate (not counted) | 1 (D1-37) |

### 2.2 After (R2C correction — web convention applied)

| Class | Count | Change |
|---|---|---|
| MATCH | 19 | unchanged |
| CONTRADICTION | 9 | unchanged |
| UNKNOWN_PENDING_PROOF | **17** | −1 (D1-22 moved to carried) |
| GAP | **3** | −1 (D1-07 moved to carried) |
| **Counted total** | **48** | −2 |
| **Carried, no delta (not counted)** | **2** | D1-07 (takes base REC-50/55/56 class, GAP), D1-22 (takes base class, as its mapped base items) |
| Merged duplicate (not counted) | 1 | D1-37, unchanged |

Cross-check: 48 + 2 + 1 = 51, equal to the header's original "51 delta rows" statement — no row is lost or invented, only recategorised as counted vs. carried, consistently with the web D1 REC's own convention.

### 2.3 Second remediation limb (A3-MD-13's alternative wording)

Independent of the recount above: **the mail D1 delta total (48, corrected) and the mail base REC total (56) must not be summed.** They overlap on exactly the items D1-07 and D1-22 name (G1/G6/G7/G10/G11 and the seven unchanged CRQ-MAIL rows), which are single items counted once in the base file and only *referenced*, not re-counted, by the delta. A reader who adds 48 + 56 double-counts those items. This is now stated explicitly for any downstream consumer (A3, MASTER).

---

## 3. RES-M3 — D1-level `mail` REC re-freeze and ordering-defect disposition (A3-MD-19)

The D1-level mail REC (`G01_MAIL_REC_DELTA_D1_20260927.md`, sha256 `bb5de020246be21a802880bfa3d0b411a6c430c84237cf57ae6e14bc59b8812f`) is **re-frozen** at this addendum's header timestamp (2026-09-27T16:35:40Z), before any R2C Proof step is treated as settled. Per A2 R2C §3, its disputed items are disposed as follows, and this REC addendum carries that disposition forward without alteration:

| D1 item | R2 disposition |
|---|---|
| CF-1 / K3 (four company-context emptying sites) | **RE-DERIVED INDEPENDENTLY IN R2** (A2 R2C §3.1) — the ordering defect is cured for this item; REC-MAIL-31/33/34's net class is unaffected, now resting on a fresh, REC-R2C-frozen independent read rather than solely on the pre-freeze Proof D1 execution |
| CF-2 / C28 (zip route has no guest-context decorator) | **RE-DERIVED INDEPENDENTLY IN R2** — cured. REC-MAIL-28 stays CONTRADICTION; the resolution-for-base-A2 is now independently supported |
| D1-34 / D11 (composer template-equality elevation: `sudo()`, not a bypass marker; wizard makes body unconditionally editable outside mass-mail) | **RE-DERIVED INDEPENDENTLY IN R2** — cured. REC-MAIL-18's delta CONTRADICTION on the D1 amendment is unaffected in class, now independently supported |
| CF-3 / D03 (link-preview image-response nuance) | **ORDERING VIOLATION, NOT INDEPENDENTLY RE-DERIVED.** Downstream must read REC-MAIL-D1-26's CONTRADICTION class as resting on the pre-freeze Proof D1 execution only, per A3-MD-12/19, until a future cycle re-derives it |
| D1-23 / K1 (document-operation → *write* mapping) | **ORDERING VIOLATION, NOT INDEPENDENTLY RE-DERIVED.** Same caveat applies to REC-MAIL-31 |
| K4 (controller kwarg allowlisting) | **ORDERING VIOLATION, NOT INDEPENDENTLY RE-DERIVED** (carried unchanged from A3 itself, which also did not re-read it) |
| K5 (parameter-comment ambiguity) | **ORDERING VIOLATION, NOT INDEPENDENTLY RE-DERIVED** — interpretive, no behavioural effect (A3-MD-10); both readings stay open |

No REC class is changed by this section. Its effect is purely evidentiary: three of the seven items A3-MD-19 flagged now rest on a REC-R2C-frozen, independently reproduced source read; the other four are explicitly labelled as still resting on the original ordering defect, so no downstream reader can mistake them for cured.

---

## 4. RES-M2 — routed to PROOF (mail: RD3, N5, G12)

Per the A3 B3B re-check routing table, RES-M2 is **PROOF-owned**. REC's role here is limited to recording the proof links so `G01_PROOF/G01_R2C_PROOF_ADDENDUM_20260927.md`'s new cases are traceable:

| REC ID (existing) | Item | R2C proof link |
|---|---|---|
| REC-MAIL-D1-47 (N5) | All-employees channel definition | PC-MAIL-R2-01 |
| REC-MAIL-D1-49 (G12) | Composer `res_domain_user_id` field unused | PC-MAIL-R2-02 |
| A3-MD-05 / A3-MD-16 (RD3; no prior REC ID — this addendum assigns one) | **REC-MAIL-D1-52 (new)**: publisher remote-message escaping | PC-MAIL-R2-03 |

REC-MAIL-D1-52 is added as **UNKNOWN_PENDING_PROOF at declaration** (a source/config case now exists where none did before); PROOF R2C's result determines its net class in the same run, consistent with rule 4 (REC is frozen before PROOF R2C predeclares — see §5).

---

## 5. RES-M4 — `mail` Q047 disposition

Per A2 R2C §5's independent source re-derivation: `mail` ships `data/neutralize.sql`, which deletes `mail_push_device` rows and both web-push VAPID config parameters, but the service-layer and web-controller neutralisation flag defaults to `False` on both duplicate and restore. **Q047 is resolved at source for `mail`'s own push-device state** (not merely bounded): by default, device/endpoint state survives a clone/restore, and is removed only on an operator's explicit opt-in.

Q047 is **removed from the mail "no evidence" list** (previously 14/16, depending on which D1 recount is read; see §2). REC class assigned: **REC-MAIL-D1-53 (new): MATCH** — A1's silence and A2's fresh verdict agree, and the fact is a static, configuration-default one, not runtime-dependent, so no `UNKNOWN_PENDING_PROOF` label applies. Lane B: NOT_APPLICABLE. Proof link: PC-MAIL-R2-04 (PROOF R2C, tagged POST-DECLARATION per A2 R2C §0.2 and PROOF R2C §1).

---

## 6. Recomputed "no evidence" list for `mail` (lineage only; no QID answered)

Starting from the D1 REC's 16-item "no evidence" list (`G01_MAIL_REC_DELTA_D1_20260927.md` §5): remove **Q047** (§5 above). No other QID changes in this batch (Q039 stays unmapped per the D1 REC's own reasoning, unaffected by this addendum).

**Mail "no evidence" after R2C: 15** of the D1 REC's list: Q012, Q013, Q015, Q016, Q019, Q020, Q026, Q028, Q029, Q034, Q039, Q040, Q042, Q046, Q049.

---

## 7. Handoff and freeze

- To: `G01_PROOF/G01_R2C_PROOF_ADDENDUM_20260927.md`. Proof link IDs named in §4–§5 above (PC-MAIL-R2-01..04) are links only; their text and results are declared and executed by PROOF R2C.
- This file is frozen at close; its sha256 is computed after close and recorded in the PROOF R2C predeclaration record and header, per rule 4.

## 8. Limitations

- §1 and §4–§5 rest on A1, A2 (base and R2C), and the D1-level Proof/REC files already frozen. No new runtime evidence exists anywhere in this addendum.
- §3's cure is bounded to the three items A2 R2C actually re-derived; the four listed items remain an open ordering defect from the original D1 cycle and are not represented as cured.
- QID mapping is controller-judged topical lineage, not coverage. No Formal Coverage, no percentages, no git operations, no existing artifact edited.
