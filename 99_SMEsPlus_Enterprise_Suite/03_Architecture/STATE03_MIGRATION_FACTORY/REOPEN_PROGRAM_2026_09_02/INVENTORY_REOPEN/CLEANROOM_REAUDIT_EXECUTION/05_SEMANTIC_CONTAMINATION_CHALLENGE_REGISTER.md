# 05 — Semantic Contamination Challenge Register

Session: `SMEPLUS-26-09-02-INV-CLEANROOM-REAUDIT-001` | Control Level: `/L999.999`

Purpose: CP-03/CP-04 established that the menu package is lexically/syntactically clean (no code, no ORM syntax, no vendor identifiers) with one narrow exception (file `10`'s location-path notation). This checkpoint asks the harder question the mandatory patterns cannot test for: has benchmark **behavior** — as opposed to benchmark **vocabulary** — become SMEsPlus design by stealth, simply because no competing Thai evidence exists to argue otherwise? Method: direct read of the package's own risk self-disclosure (`20_CLEAN_ROOM_PROCESS_TRANSFORMATION_REGISTER.md` §6) plus the highest-risk content maps it points to, cross-checked against this session's own `C-05` and mechanical-scan findings.

---

## 1. Risk 1 — Default-by-Absence (the package's own named risk, self-disclosed in `20` §6)

**Claim under test:** count policy, backdate governance, product-kind classification, and branch/warehouse fields are described in the package as if they were settled business requirements, when in fact no Thai storekeeper, accountant, or auditor has validated any of them — the description is really "what the benchmark does," carried forward for lack of anything to compete with it.

**Evidence:**
- The package itself names this exact risk in `20` §6 ("benchmark behaviour becomes design because no Thai evidence competes") and lists it as the top forward risk — this is a documented self-awareness, not something this re-audit is the first to notice.
- `17_THAI_MENU_AND_REPORT_NAMING_REGISTER.md` marks every Thai label `candidate / UNVALIDATED`, which is the correct hedge at the *naming* level.
- However, the *process content* the Thai names attach to (e.g. `06_INVENTORY_MENU_BY_MENU_PROCESS_MAP.md`'s per-menu purpose/input/process/output narrative) is written in confident, declarative prose ("the process is...", "the control impact is...") rather than "the benchmark does X; Thai fitness unvalidated" framing at the sentence level. The hedge lives in the header/status line of each file, not repeated at each behavioral claim inside it.
- This is a real but structural finding, not a leak: it is the natural consequence of writing a 29-file reference package from benchmark-derived process knowledge before the TBRAC validation session (doc `26` action #3) has happened. The package's own terminal status (`HOLD / EVIDENCE REQUIRED`, "not final solution") is the correct governance response to exactly this condition.

**Classification: `NEEDS_WORDING_REWRITE` (systemic, not file-specific)** — recommend that any future revision of this package (or its Team B/C successor, once authorized) carry the "candidate, Thai-fitness unvalidated" hedge at the level of individual behavioral claims, not only in file headers, so a reader skimming mid-document cannot mistake benchmark-derived process description for validated Thai requirement. Not `FAIL_FROZEN`: the package does not claim these are final designs, and the terminal status already reflects the correct caution.

## 2. Risk 2 — Bundle-by-Inheritance: Product Category as Valuation Policy Owner (`20` §6, carried from memory record `[[smeplus-clean-room-rules]]` context and reopen benchmark facts)

**Claim under test:** the package's `08_CONFIGURATION_FOUNDATION_MAP.md` and `15_LANDED_COST_VALUATION_ACCOUNTING_HANDOFF_MAP.md` (both cited against `CF-09 Product Categories` in `20` §1) describe Product Category as the natural owner of both storage/putaway grouping *and* valuation policy — a coupling that is a benchmark architectural choice, not a demonstrated Thai business requirement. This directly matches this project's own carried-forward benchmark fact ("Product Category as benchmark policy owner", tracked from the prior reopen chain).

**Evidence:** `20`'s own table marks `CF-09`'s "what was deliberately not carried" as "Category model; account fields; dual ownership" — i.e. the authoring session already recognized dual-ownership as a risk to guard against, and the field-level model was not copied. This is the correct clean-room posture at the mechanical level. The open question is whether the *business framing* in `08`/`15` (grouping category as the natural place to also hang valuation policy) still steers a future designer toward the same coupling by default, absent an explicit Boss/Accounting-Tax decision on the point.

**Classification: `BOSS_ONLY_REVIEW`** — this is not a mechanical leak and not something a further clean-room pass can resolve; it is a design-ownership question (does valuation policy belong on Product Category, on a separate valuation-policy object, or jointly with Accounting?) that the package correctly declines to answer and that doc `26` action #5 (Account × Inventory Joint Session) already routes to the right forum. No file requires quarantine; the open question requires a Boss/Joint-Session decision, not a rewrite.

## 3. Risk 3 — Vocabulary Transcription Into Team B Schema (`20` §6)

**Claim under test:** if a future Team B session inherits this package's Thai vocabulary (`17`) alongside the process maps, will state-machine names, document-type names, or model names leak through as literal schema even though the package's Thai labels are meant to name *business concepts*, not *objects*?

**Evidence:** this risk is prospective — it names a failure mode for a session that has not yet run (Team B is explicitly not authorized by this package or by doc `26`). It cannot be tested against content that does not exist yet. The package's own control candidate ("re-apply clean-room checklist to lifecycle documents; this package's Thai templates as the vocabulary source") is a reasonable mitigation, contingent on it actually being applied.

**Classification: `SAFE_CLEAN_ROOM_LEARNING` for this package as it stands (the risk is correctly named, not realized here); carries a `BOSS_ONLY_REVIEW` condition on the *next* session** — Boss should confirm the clean-room checklist re-application is a mandatory gate on any future Team B kickoff prompt, not merely a recommendation on paper.

## 4. Risk 4 — The One Concrete Instance Found: File `10` Location-Path Notation

This is not a hypothetical risk category — it is the one place in the package where §1's "default-by-absence" pattern is already visible as a concrete structural carry-over (see `03_MENU_PACKAGE_MECHANICAL_LEAKAGE_SCAN.md` §4): the specific five-node `WH/Stock, WH/Input, WH/Quality, WH/Output, WH/Packing` location scaffold and its parent/child path notation is benchmark structure, not a re-derivation from Thai warehouse practice. Classification carried forward: **`NEEDS_WORDING_REWRITE`**, consistent with §3 of file `03`.

## 5. Risk 5 — Account Vocabulary Transliteration (`20` §6)

**Claim under test:** whether Thai Chart-of-Accounts—adjacent vocabulary in this package (landed cost, valuation account references in `15`) risks transliterating benchmark accounting vocabulary rather than being independently derived from TFRS-for-NPAEs.

**Evidence:** `15_LANDED_COST_VALUATION_ACCOUNTING_HANDOFF_MAP.md` frames landed cost strictly as an "accounting interface" (a handoff, not an Inventory-owned design decision), consistent with `04`'s handoff classification (12 Inventory-owned / 6 accounting-interface / 4 Account-only / 9 Joint, independently verified in `04_CITATION_PROVENANCE_CLAIM_SAFETY_REGISTER.md` §2). This is the correct posture — the package defers the accounting-vocabulary question to the Account track rather than asserting it.

**Classification: `SAFE_CLEAN_ROOM_LEARNING`** — the package does not itself make an accounting-vocabulary design claim; it correctly routes the question to Accounting-Tax, matching doc `26`'s own recommendation.

---

## 6. Summary Table

| Risk | Source | Classification | Action owner |
|---|---|---|---|
| Default-by-absence (systemic hedging depth) | `20` §6, this session | `NEEDS_WORDING_REWRITE` | Package maintainers, next revision |
| Product Category as valuation-policy owner | `20` §6, benchmark fact | `BOSS_ONLY_REVIEW` | Boss / Account×Inventory Joint Session (doc 26 #5) |
| Vocabulary transcription into future Team B schema | `20` §6 | `SAFE_CLEAN_ROOM_LEARNING` (as-is) + `BOSS_ONLY_REVIEW` (gate condition on next session) | Boss (prompt-writer for any future Team B session) |
| File `10` location-path notation | This session, `03` §4 | `NEEDS_WORDING_REWRITE` | Package maintainers |
| Account vocabulary transliteration | `20` §6 | `SAFE_CLEAN_ROOM_LEARNING` | Accounting-Tax track (already routed) |

**Most conservative unresolved verdict in this set: `BOSS_ONLY_REVIEW`.** No item in this challenge reaches `NEEDS_QUARANTINE` or `FAIL / FROZEN` — nothing found here rises to the severity of the mechanical `C-05` leak audited in `02`. The dominant pattern is a package that correctly *names* its own contamination risks in `20` §6 but has not yet had those risks resolved by the Boss decisions or validation sessions that alone can resolve them (doc `26` actions #1 and #3).

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
