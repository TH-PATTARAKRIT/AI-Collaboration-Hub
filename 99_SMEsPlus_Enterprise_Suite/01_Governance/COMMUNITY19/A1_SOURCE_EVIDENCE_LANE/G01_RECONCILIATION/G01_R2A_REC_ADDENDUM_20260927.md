# G01 PLATFORM_BASE — RED TEAM Reconciliation Addendum (Remediation Cycle R2, batch R2A) — `auth_signup`, `base_automation`, `bus`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RECONCILIATION (REC)**. This is an addendum only. No parent REC, parent REC addendum, A2, or Proof artifact is edited. Append-only lineage |
| Group / Modules | G01 PLATFORM_BASE / `auth_signup`, `base_automation`, `bus` |
| Cycle | Remediation Cycle R2, batch R2A |
| Date | 2026-09-27 (written after the A2 addendum froze at 16:33:22 UTC; before any R2A Proof predeclaration) |
| Stage order position | **Second** artifact. Consumes the A2 addendum below. This addendum's own sha256 is recorded below at freeze and must be quoted in the Proof addendum header **before** Proof predeclares (MASTER C1-B rule 4). This addendum cites **no** Proof result of this batch; none existed when it was written |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

### 0.1 Parent / input artifacts (sha256)

Paths relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Artifact | sha256 |
|---|---|
| **A2 input (this batch)** `G01_A2_REVIEWS/G01_R2A_A2_ADDENDUM_20260927.md` (frozen 16:33:22 UTC) | `1a51ec1f84e995aea5a1c06f1b513d109b9d691ed4cec37adef7c2d5c25e2313` |
| A3 report `G01_A3_CHALLENGES/G01_B3A_A3_RECHECK_R1_20260927.md` | `a63547079815bab5d682aab52ca4974ff79ffa24ea9b840eac0d400d543c7699` |
| A3 report `G01_A3_CHALLENGES/G01_BATCH2_A3_RECHECK_R1_20260927.md` | `52a0e7f1b9b98f46a962025b38b1cf518851653aeb11a613e7e7d5d9a5043261` |
| Parent REC `G01_RECONCILIATION/G01_B3A_REC_ADDENDUM_R1_20260927.md` | `44deb36d461c391c7f10d5602e5f26d3727cec7397ae7ee981f6dec341810fdd` |
| Parent REC `G01_RECONCILIATION/G01_BATCH2_REC_ADDENDUM_R1_20260927.md` | `18292fd3418f26152330446fc20080f4fd453a04c3555c1932807652e56c5331` |
| Parent Proof (for lineage only, not consulted for classification) `G01_PROOF/G01_B3A_PROOF_ADDENDUM_R1_20260927.md` | `d64cdefeb70da1e89216a8007d537bef3f3f16961e0ee744122f6f52845583ce` |
| Parent Proof (for lineage only) `G01_PROOF/G01_BATCH2_PROOF_ADDENDUM_R1_20260927.md` | `141fb8558c59303a9e6395d4bd6fd2b26bf5fb865d6d094988153108fd0854f9` |
| A1 package `G01_A1_PACKAGES/G01_AUTH_SIGNUP_A1_PACKAGE_20260927.md` | `da32ca50…fe69e` (as recorded upstream) |
| A1 package (bus, for the Q021 rescan) `G01_A1_PACKAGES/G01_BUS_A1_PACKAGE_20260927.md` — item C18, and its Lane A source `G01_LANE_A_PASS1/G01_BUS_LANE_A_PASS1_20260927.md` item #12 | `6c3e5a44267b28835f26c1859c5637432ebe791f4030f3e0f13f0f0054f1d875` (A1 package, as recorded upstream) |
| Parent REC (bus), for the corrected Q021 row | `G01_RECONCILIATION/G01_BUS_REC_20260927.md` `251c8a2ad06918477e4c9b9c8c52093fa95f0484ffa0db1cc5f558fe5f20e4bc` |

### 0.2 Residual IDs addressed here

R-ASGN-1 (carry A2's corrected wording into REC-ASGN-28's basis), R-ASGN-2 (annotate REC-ASGN-18/C18-R1 with the corrected, bounded enumeration method), R-BAUT-1 (carry A2's gate-location correction into REC-BAUT-38/REC-BAUT-11), R-BUS-1 (carry A2's OM-B08-R2 wording into REC-BUS-28), **R-BUS-2 (own-owned correction: re-scan and add Q021 to the mapped list)**, R-BUS-3 (carry the citation correction into REC-BUS-14's proof link note).

Clean-room note: neutral paraphrase only; identifiers are pointers. No vendor code. No percentages. No Formal Coverage claim. No QID is answered; every QID mapping is lineage only. No git operations. No existing artifact was edited. REC did not fetch source in this addendum beyond re-reading the two A1/Lane-A items needed for the Q021 rescan (§3); the source basis for the wording corrections is the A2 addendum's own re-read.

### 0.3 MASTER process-rule compliance (this addendum)

| Rule | Compliance | Evidence |
|---|---|---|
| 1. Preserve A2 `MISSING_REQUIRED_RUNTIME_PROOF` | **MET**. Section 1 restates the A2 label unchanged for every item touched (O4-R1, C18-R1, O14-R2, REC-BUS-28, REC-BUS-14); none is downgraded | §1 |
| 2. Post-declaration tagging | **NOT APPLICABLE** (REC predeclares no Proof cases). REC changes are all labelled "basis addendum" or "lineage correction" | §§2–3 |
| 3. Scan all A1 item classes for "no evidence" QIDs | **MET for this batch's residual** (R-BUS-2). §3 re-scans the bus "no evidence yet" list specifically against A1-G01-BUS-C18 and Lane-A-only item #12, which the batch-2 REC addendum's own rescan had missed for Q021. auth_signup and base_automation "no evidence" lists are unaffected by this batch's residuals and are not re-scanned here (R-ASGN-1/2 and R-BAUT-1 are wording/method corrections, not QID-lineage items) | §3 |
| 4. REC frozen (sha256) before Proof executes; Proof records it | **MET for this addendum** (hash recorded below at freeze, before any R2A Proof predeclaration). Parent RECs' historical ordering is unchanged by this addendum and not re-litigated | Header; §0.1 |
| 5. Cases sha256 + UTC before first Proof fetch | **NOT APPLICABLE** (Proof duty) | — |
| MD-07 (anchor-only admissibility) | **MET**. REC performs no independent source fetch beyond citing the A2 addendum's own anchor-fetched, blob-verified evidence and re-reading the two already-anchored A1/Lane-A text items for §3. No code search or index is used | §0.1, §3 |
| MD-08 (bounded completeness) | **MET**. §2 records the A2 addendum's stated enumeration boundary verbatim in the REC basis cell for REC-ASGN-18/C18-R1, rather than repeating or hardening it into an unqualified completeness claim | §2 |

---

## 1. Rule 1 — A2 labels restored/carried (no change; verification only)

| Item | REC ID | A2 proof label | Carried? |
|---|---|---|---|
| auth_signup O4-R1 (R-ASGN-1) | REC-ASGN-28 | MISSING_REQUIRED_RUNTIME_PROOF | Unchanged — carried |
| auth_signup C18-R1 (R-ASGN-2) | REC-ASGN-18 | MISSING_REQUIRED_RUNTIME_PROOF | Unchanged — carried |
| base_automation O14-R2 (R-BAUT-1) | REC-BAUT-38, REC-BAUT-11 | MISSING_REQUIRED_RUNTIME_PROOF | Unchanged — carried |
| bus OM-B08-R2 (R-BUS-1) | REC-BUS-28 | MISSING_REQUIRED_RUNTIME_PROOF | Unchanged — carried |
| bus SF-B04-R2 citation (R-BUS-3) | REC-BUS-14 | MISSING_REQUIRED_RUNTIME_PROOF (UNKNOWN_PENDING_PROOF class, unchanged) | Unchanged — carried |

No REC class changes in this batch. No item is promoted, demoted, or moved between MATCH/CONTRADICTION/GAP/UNKNOWN_PENDING_PROOF/UNCORROBORATED/NOT_APPLICABLE.

---

## 2. Basis corrections (wording only; class unchanged)

### 2.1 `auth_signup`

| REC ID | Change | Basis addendum (from A2 R2A) | Class | Proof link |
|---|---|---|---|---|
| REC-ASGN-28 | Basis wording correction (R-ASGN-1) | Per A2 O4-R1 wording correction (§1 of the A2 addendum): the local default base URL persists on the regenerating copy only if the source database's `web.base.url.freeze` parameter was set (and therefore copied); if it was unset, the very next system-user login carrying a base location automatically rewrites the URL. The parent phrase "until an administrator changes it" is imprecise and is replaced by this conditional statement | UNKNOWN_PENDING_PROOF (unchanged) | PR-ASGN-13 superseded by PR-ASGN-13R2 (records the freeze-parameter state and exercises one post-copy login) |
| REC-ASGN-18 | Basis addendum (R-ASGN-2, evidence-integrity correction) | Per A2 §2 (R2A): the cross-module caller enumeration is redone by a manifest-`depends`-plus-`__init__`-chain method at the anchor, **not** a default-branch code-search index. Five call sites are confirmed anchored (§2.3 of the A2 addendum): portal share wizard, survey start page, website_slides invite/identify, portal mail-thread notification, portal grant wizard; a sixth, the portal-mixin share-URL builder, is an anchored call site whose own callers remain unenumerated. The enumeration is bounded to the historical G01 23-module roster (exhaustively manifest-checked) plus six named canonical addons already surfaced by the B3a A3 re-check; it is explicitly **not** a claim that no caller exists anywhere else in the Odoo addon universe | CONTRADICTION (A1 vs A2; unchanged) | PC-ASGN-36 superseded by PC-ASGN-36R2 (manifest-and-chain-driven table, with the boundary statement carried as part of the case, not dropped) |

**MD-08 disposition:** REC does **not** convert the A2 addendum's bounded-evidence statement into an unqualified "the only callers are …" claim. The completeness gap named in A2 §2.4 (portal-mixin callers unverified; wider Odoo addon universe not tree-listed) is carried into the REC basis cell above and into the Proof case, not dropped.

### 2.2 `base_automation`

| REC ID | Change | Basis addendum | Class | Proof link |
|---|---|---|---|---|
| REC-BAUT-38 | Basis wording correction (R-BAUT-1) | Per A2 O14-R2 wording correction: for a job user outside the settings group (variant ii-b), the run fails **at the server-action gate (`_can_execute_action_on_records`, invoked by `run()` before `_run()`)**, not "at the first rule search" and not "at rule lookup." No rule search executes in this branch at all. The FAILED/nothing-stamped/last-run-unchanged/counter-incremented outcome is unchanged | UNKNOWN_PENDING_PROOF (unchanged) | PC-BAUT-64R1 superseded by PC-BAUT-64R2 (wording of the (ii-b) expected text only; fail condition unchanged) |
| REC-BAUT-11 | Basis wording correction (R-BAUT-1) | Same correction applied to the REC-BAUT-11 time-path row: "a reassigned ordinary user would apply that user's rights to record selection" is qualified as applying only to a settings-group job user (variant ii-a); a non-settings job user (ii-b) never reaches record selection because the server-action gate denies first | UNKNOWN_PENDING_PROOF (unchanged) | As REC-BAUT-38 |

### 2.3 `bus`

| REC ID | Change | Basis addendum | Class | Proof link |
|---|---|---|---|---|
| REC-BUS-28 | Basis wording correction (R-BUS-1) | Per A2 OM-B08-R2: the delay is bounded **in practice** by the affected socket's remaining keep-alive lifetime when a client reconnects (client reconnect logic itself not read); loss requires that no trigger — a later notification, a resubscribe, or a reconnect — arrives before the 24 h GC retention window closes. Neither the original A3 "~50 s" framing nor the remediation's earlier "silences all tenants" framing is reinstated | GAP (unchanged) | PC-BUS-21 PASS stands (predicate incomplete but verdict correct, per the batch-2 A3 ruling); PC-BUS-22 superseded by PC-BUS-22R1 (records keep-alive open time and remaining lifetime so Case A cannot give a false FAIL from an expired socket) |
| REC-BUS-14 | Citation correction (R-BUS-3) | Per A2 SF-B04-R2: the request-path session-cookie save invokes `FutureResponse.set_cookie`, not `Response.set_cookie`; both share identical defaults, so the finding (HttpOnly; no explicit SameSite; no explicit Secure) is unaffected. The proof-link citation is corrected accordingly | UNKNOWN_PENDING_PROOF (unchanged) | PC-BUS-23 superseded by PC-BUS-23R1 (citation only; verdict unchanged) |

---

## 3. R-BUS-2 — rule-3 rescan: Q021 wrongly left on the "no evidence yet" list

**Re-derivation (REC's own, before applying the fix).** The batch-2 REC addendum's §1.3 rule-3 rescan (D-BUS-04) corrected Q007, Q013, Q037, Q002 and Q040, but left Q021 (duplicate subscription registration does not multiply delivery) on the "no evidence yet" list of 6 (alongside Q022, Q028, Q031, Q032, Q033). Checking Q021 against **all** A1 item classes (as rule 3 requires, not only the previously-checked claims):

- **A1-G01-BUS-C18** (claim class): "per-socket in-memory history of dispatched ids (10 s) de-duplicates and tolerates out-of-order commit visibility."
- **Lane-A-only item #12** (pre-A1 source observation, carried into the A1 package's evidence pointers): "Ordering/duplicate control: per-socket in-memory history of dispatched ids kept 10 s to handle out-of-order commit visibility; last-id advances only past contiguous expired entries."

Both are topically relevant to Q021: the per-socket dispatched-id history is the mechanism that would prevent the same underlying row from being re-delivered to a socket that re-subscribes or otherwise re-triggers a dispatch while that id is still within the 10 s retained window. This is a **topical fit for lineage purposes only** — it does not answer Q021 and does not establish that a duplicate **subscription request** (as opposed to a duplicate **dispatch trigger**) is deduplicated; that distinction is exactly what remains open.

**AGREE with A3.** Q021 should be **mapped**, not left on the no-evidence list, with the fit flagged as topical-only (the same convention already used for other weak/topical fits in this batch's REC addenda).

> **Correction applied:** Q021 moves from "no evidence yet" to **mapped**, linked to **REC-BUS-18** (C18/at-least-once contradiction item) and **REC-BUS-24** (publisher-obligation item, both already touching the same dispatched-id/history mechanism). bus "no evidence yet" list (post batch-2 R1) was **6**: Q021, Q022, Q028, Q031, Q032, Q033. After this correction it is **5**: Q022, Q028, Q031, Q032, Q033. Mapped count rises from 35 to **36**. Mapped ∪ no-evidence remains Q001–Q041 with no overlap (36 + 5 = 41).

| QID (topic) | Added mapping | A1/Lane-A item class and reason |
|---|---|---|
| Q021 (duplicate subscription registration) | REC-BUS-18, REC-BUS-24 | A1-C18 and Lane-A item #12: per-socket in-memory dispatched-id history (10 s) is the module's only de-duplication mechanism; topical to whether a duplicate subscription request could multiply delivery, though the subscription-request-vs-dispatch-trigger distinction is not itself evidenced (no QID answered) |

No other bus QID is moved by this correction. digest, resource and resource_mail "no evidence" lists are untouched (outside this batch's residuals).

---

## 4. Handoff to PROOF

Proof must, **after** recording this addendum's sha256 in its header and **before** its first R2A source fetch, predeclare (file sha256 + UTC) the following, per the A2 addendum §6 requirements table:

| Module | Required |
|---|---|
| auth_signup | PR-ASGN-13R2 (runtime, wording); PC-ASGN-36R2 (static, supersedes PC-ASGN-36 with the manifest-and-chain-driven table and the stated completeness boundary) |
| base_automation | PC-BAUT-64R2 (wording of the (ii-b) expected text only; fail condition unchanged) |
| bus | PC-BUS-22R1 (records keep-alive open time and remaining lifetime); PC-BUS-23R1 (citation only) |

Runtime device is offline per every upstream Proof; runtime cases are expected to be **NOT-EXECUTED** and must not be reported otherwise.

## 5. Limitations

- REC read no new source in this addendum beyond the two A1/Lane-A text items re-checked for §3; all other bases rest on the A2 addendum's own anchor-fetched re-read.
- The Q021 mapping is topical lineage judged by this owner stage; it is not a coverage measure and answers nothing.
- The same controller authored the A2, REC and Proof addenda of this batch. This independence limitation is disclosed; A3 remains the independent re-check stage.
- No Lane B or runtime evidence exists; absence is not failure. No percentages, no Formal Coverage claim, no git operations, no existing file edited.
