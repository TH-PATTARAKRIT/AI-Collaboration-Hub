# G01 PLATFORM_BASE — RED TEAM Proof Addendum (Cycle R2, batch B) — `resource`, `resource_mail`, `google_recaptcha`, `base_sparse_field`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF**. This is an addendum only. All parent Proof files and all R1 Proof addenda are immutable and were not edited. |
| Cycle | **R2 (remediation of A3-sustained residual defects, Cycle R2)**, remediation batch **B** |
| Group / Modules | G01 PLATFORM_BASE / `resource`, `resource_mail`, `google_recaptcha`, `base_sparse_field` |
| Date | 2026-09-27 |
| REC consumed (this cycle) | `G01_RECONCILIATION/G01_R2B_REC_ADDENDUM_20260927.md`, sha256 **`f8784cbd1a61e24cc437b0a8249cdec4f0c6377cc80b53fd60067a4f5ada1260`**, frozen **2026-09-27T16:34:22.423Z** — recorded here **before** any text of this Proof addendum was written, satisfying C1-B rule 4 for this cycle |
| A2 consumed (this cycle) | `G01_A2_REVIEWS/G01_R2B_A2_ADDENDUM_20260927.md`, sha256 `5b1cf760b703326be12663b74aa83cfb50a3ac3df67c9e4f49f85ddc0847174f`, frozen 2026-09-27T16:32:55.456Z |
| This file's own write time | Begun 2026-09-27T16:36Z, i.e. after the REC freeze above — **A2 → REC → PROOF order held for this cycle** |
| Runtime device | Still **OFFLINE**. Every runtime case referenced anywhere in this lineage (R1 and earlier) remains **NOT-EXECUTED**. This addendum executes **no** case, static or runtime, and predeclares none, because R-RSRC-1 and RCAP/SPRS R-2 are label/process corrections that require no new source fact or new proof case |
| Residuals addressed (PROOF part) | RCAP/SPRS **R-2** — records, for this cycle, that REC was frozen before this Proof addendum existed, and that the R1 violation is disposed (not repaired) by the REC addendum's option-(a) independent re-derivation |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Clean-room note: neutral paraphrase only. No code, expression or literal token reproduced. No percentages. No Formal Coverage claim. No QID answered. No git write operations. No existing artifact was edited.

---

## 1. Why no new proof case is declared

Both residuals routed to this batch are process/label corrections, not new source findings:

- **R-RSRC-1** (REC, section 1 of the REC addendum) restores a Lane B label using facts already established and already `PC`-cased in the R1 Proof addendum (`G01_BATCH2_PROOF_ADDENDUM_R1_20260927.md`, PC-RSRC-08R1/22..28, PC-RMAIL-07, etc., "static totals... 17 executed, 16 PASS, 1 FAIL"). No new Expected/Fail predicate is needed because the underlying static facts are unchanged; only the Lane B column of the REC row (not owned by Proof) changes.
- **RCAP/SPRS R-2** is a disposition of an ordering defect in how the R1 REC addendum was written and timed relative to the R1 Proof addendum's execution. It requires no new evidence run — it requires (a) an independent re-derivation, which the A2 addendum (this cycle) performs, and (b) confirmation, which the REC addendum (this cycle) performs and which this Proof addendum now attests to procedurally by recording that its own REC input was frozen first.

Declaring a new predeclared case here, with no new Expected/Fail content, would itself be a rule-2/rule-5 violation (post-hoc case invention without substance). None is declared.

---

## 2. Procedural attestation: REC-before-PROOF held this cycle

| Check | Result |
|---|---|
| Was the REC addendum (this cycle) sha256'd and timestamped before this Proof addendum's text existed? | **Yes** — REC sha256 `f8784cbd…5ada1260` frozen 16:34:22.423Z; this file's first content was written after that, at ≥16:36Z (this session's tool-call ordering: A2 write → A2 hash → REC write → REC hash → this file) |
| Does this Proof addendum cite anything from a later-written file? | **No** — it cites only the REC addendum (frozen before it), the A2 addendum (frozen before the REC addendum), and R1/parent artifacts that predate this cycle entirely |
| Does resolving RCAP/SPRS R-2 require editing the R1 REC or R1 Proof addenda? | **No, and none was edited.** Both remain as originally written, with the ordering defect disclosed in their own text (R1 Proof §7/8, R1 REC §3.7/§5) and now further disposed here |

This satisfies, for the present batch, the requirement the RCAP/SPRS A3 re-check attached to R-2 ("future R-rounds freeze REC before Proof executes").

---

## 3. RCAP item 12 — cross-reference only (not owned by Proof)

The Lane A erratum for item 12 is issued as a standalone Lane A-owner note in the A2 addendum (this cycle), section 2, per the task's routing (the Lane A packet itself is not edited, and Proof does not issue Lane A notes). This Proof addendum records only the pointer: A3 residual **R-5** ("the item 12 erratum exists only as a pointer recorded by Proof") is now superseded — the pointer previously recorded in the R1 Proof addendum (§7, table row for A3-RCAP-D1) is followed by an actual Lane A-owner erratum note, issued this cycle. **R-5 is CLOSED.**

---

## 4. Effect on the case ledger

No case is added, superseded, relabelled, executed or predeclared by this addendum. The R1 Proof addendum's effective case ledger (§6 of `G01_BATCH2_PROOF_ADDENDUM_R1_20260927.md`, and the corresponding table in `G01_RCAP_SPRS_PROOF_ADDENDUM_R1_20260927.md`) stands unchanged. MASTER consolidation for all four modules remains **BLOCKED on runtime**; nothing in this batch lifts that block.

## 5. Limitations

- No runtime execution occurs in this addendum. No runtime result is claimed or fabricated.
- No percentages, no Formal Coverage claim, no QID answered. No git operations were run. The parents and all R1 addenda are untouched.
- This addendum's scope is deliberately narrow: it closes R-RSRC-1 (via the REC addendum) and RCAP/SPRS R-2 and R-5 (via the A2 and REC addenda, with this file's role limited to the procedural attestation in section 2 and the cross-reference in section 3).

## 6. Rule-compliance table

| Rule | Compliance | Evidence |
|---|---|---|
| C1-B rule 1 (preserve A2 MRRP label) | **N/A for PROOF** (REC owns the Lane B label; see REC addendum §1) | — |
| C1-B rule 2 (tag post-declaration Expected text) | **N/A** — no case, and so no Expected text, is declared in this addendum | — |
| C1-B rule 3 (REC scans all A1 item classes) | **N/A for PROOF** | — |
| C1-B rule 4 (REC frozen, sha256 recorded, before PROOF executes; PROOF records the REC sha256 consumed) | **MET** — section 0 records the REC addendum's sha256 and freeze time, recorded before this file's text; section 2 attests to the ordering explicitly | Header; section 2 |
| C1-B rule 5 (cases sha256 + UTC timestamp before first source fetch) | **N/A** — no case is predeclared and no new source fetch is performed by this addendum (it reuses already-hash-verified fetches recorded in the A2 addendum, this cycle) | — |
| MD-04/MD-09 (different-author runtime execution) | **N/A** — no runtime executes; device remains offline | — |
| MD-05 (rule-compliance table in every addendum) | **MET** (this table) | — |
| MD-06 (commit subject/body) | Applies at commit time (Integration Control / MASTER) | — |
| MD-07 (anchor-fetched, `git hash-object`-verified evidence; no code search/index/training recall for completeness) | **MET** — this addendum introduces no new evidence claim; it relies solely on the A2 addendum's section 0.2/1 anchor-verified trace | A2 addendum (this cycle) §0.2, §1 |
| MD-08 (enumeration claims state method / are bounded) | **MET** — section 1 explicitly bounds this addendum's scope ("no new proof case") rather than asserting completeness of any enumeration | Section 1 |
| RCAP/SPRS A3 residual R-2 | **CLOSED** (disposed under option (a) in the REC addendum, this cycle; procedurally attested here) | REC addendum §2; this file §2 |
| RCAP/SPRS A3 residual R-5 | **CLOSED** (Lane A erratum issued; see A2 addendum §2) | A2 addendum (this cycle) §2; this file §3 |
