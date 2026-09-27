# G01 PLATFORM_BASE — RECONCILIATION Addendum, Remediation Cycle R2 batch D — `phone_validation`, `onboarding`, `web_unsplash`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RECONCILIATION (REC)**. This is an addendum only. Every parent artifact (parent RECs, the B3C REC R1 addendum, and all upstream stages) is immutable and none was edited |
| Group / Modules | G01 PLATFORM_BASE / `phone_validation`, `onboarding`, `web_unsplash` |
| Cycle | Remediation Cycle **R2**, batch **D** |
| Date | 2026-09-27 (written after 16:31:45Z; frozen before the Proof R2D predeclaration) |
| Governing rules | `MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` sha256 `d3966ad058ca11e82ef20ec777818486a726996f8d04f6a59da4315cf6e84e42`; `MASTER_DECISION_LOG_G01_20260927.md` sha256 `20c10c3efe3dddf321d888aba88b1f69e2e8455ee162274e934947d8c65a8981` (MD-07/MD-08) |
| Input — A3 re-check (immutable) | `G01_A3_CHALLENGES/G01_B3C_A3_RECHECK_R1_20260927.md` sha256 `a30062c25bf3a2f8f41284b473863b3a97e12de8ae99d42c9d8733cf12a823a2` |
| Input — A2 addendum R2D (immutable; frozen before this REC addendum) | `G01_A2_REVIEWS/G01_R2D_A2_ADDENDUM_20260927.md` sha256 **`3a4d1bdc8972e2cec1640c85d47e9f0cd23ea48ec8f071b71439c97ca1d0757e`** |
| Input — B3C addenda (immutable; unchanged) | A2 `a364fa30d6007c06dc34f79747a8bc6fc60afea71a4bacf131940a0720581750`; REC `c77ed8a00d6a6d88c6f34c3356ee3b64c645ee8e9950296d6e88ab8492709f6b`; Proof `c8fdd5a2c82cb442c52f6a98051efe0c99c5f505f33e9ad0dacd8cd551c18c82` |
| Parent REC artifacts (sha256; unchanged since B3C freeze) | `G01_RECONCILIATION/G01_PHONE_VALIDATION_REC_20260927.md` `87a34f17b618b902a8933413c706c76cdaeccc9cfec6d6fd3626160c7187a717`; `G01_RECONCILIATION/G01_ONBOARDING_REC_20260927.md` `fdd2d41b3b3cfdc7d5612820ff46c6c226da92d95d27012adbbd384308b91889`; `G01_RECONCILIATION/G01_WEB_UNSPLASH_REC_20260927.md` `66eb15218a853ab0f43589e5558b4622586080aa3d8c1a8a2f6eb2a5de1f3ffd` |
| Question lineage | phone: W1-B10 ELIGIBLE (bank `c70aae333f7a25b558383945b2cca58a66816413eb079c6225161075a50b8a80`, re-verified below). onboarding: W1-B09 HOLD, Standard 55 only. web_unsplash: no bank, Standard 55 only. **No QID is answered** |
| Residuals addressed here | **R-PHON-1** (REC item), **R-PHON-2** (QID lineage correction), **R-UNSP-1** (PROVIDER-CLAIM sub-tag) |
| Residuals not addressed here | R-ONBD-1, R-ONBD-2 — both PROOF-only (tally tag, wording); see the Proof R2D addendum |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Clean room: neutral paraphrase only. Identifiers and line numbers are pointers only, and no code is reproduced. No percentages. No Formal Coverage claim. No git write operations. No existing artifact was edited.

---

## 1. `phone_validation`

### 1.1 R-PHON-1: new REC item for the audit-duplication observation

**New REC-PHON-31.**

| Field | Value |
|---|---|
| A1 item | None directly (a cross-cutting effect of BR-2/BR-6 and the SF-PHON-01-R1 mechanism); folded under the same umbrella as REC-PHON-21 |
| Basis | A2 B3C addendum §1.1 item 8 (original observation); **A2 R2D addendum §1.1** (independent re-derivation confirming the mechanism end to end at the pinned anchor: the nested `create()` call inside `_remove()` re-discovers the just-archived entry through its own existence search and returns it, so both `_track_set_log_message` and `message_post` fire on the same record for one `_remove` call) |
| REC class | **UPP** (source mechanism confirmed; runtime confirmation of the actual chatter/message sequence is pending, consistent with how REC-PHON-21 itself stays UPP despite PC-PHON-30's source PASS) |
| Lane B | UNCORROBORATED |
| Proof link | **PR-PHON-12** (runtime, newly declared by A2 R2D §1.2); static basis case **PC-PHON-31** (source) reserved for the Proof R2D addendum |
| Linked to | REC-PHON-21 (same SF-PHON-01-R1 wrong-subject mechanism; this item is the audit-trail consequence rather than the blacklist-state consequence) |
| Text | "One `_remove` call with a no-value or unformattable submitted number, on a subject whose own entry already exists, writes two separate audit entries — a tracking-log message and a posted chatter note — onto that one subject's entry, because the nested `create()` call re-discovers and returns the entry `_remove` just archived. This is a source-confirmed, cross-cutting consequence of the wrong-subject mechanism REC-PHON-21 already covers, tracked here as its own item because it is a distinct auditability defect (a false or doubled audit trail), not an additional access-control defect." |

This closes the "no REC item and no proof-requirement link" half of R-PHON-1 exactly as A3 R1 requested: a governed REC row now exists, linked to REC-PHON-21 by name, with its own Lane B class and its own proof link (both a runtime PR and a reserved static PC).

Phone REC totals after R2D: parent B3C total was 49 (19 MATCH, 6 CONTRADICTION, 19 UPP, 5 GAP). Adding REC-PHON-31 (UPP): **50** rows (19 MATCH, 6 CONTRADICTION, 20 UPP, 5 GAP).

### 1.2 R-PHON-2: Q036 dropped from REC-PHON-30's QID lineage

**Re-derivation (A2 R2D §2.1, adopted here):** Q023 ("blacklist actions from a business record operate on the record's canonical phone identity, not a raw display string") is a direct topical fit for GAP-PHON-10/REC-PHON-30 — the gap is exactly whether an unread consumer passes a record with no sanitized number, causing a write against the wrong (acting-user-fallback) identity instead of the record's own canonical identity. Q036 ("downstream flows honor the active blacklist before sending") concerns enforcement at send time, a materially different question (whether a send is blocked, not whether the wrong identity was written). No QID among the frozen bank's other 39 entries is a closer fit than Q023 (the nearest alternative, Q024, concerns symmetric reversal of the *same* identity, not consumer-supplied mistargeting). The bank is frozen (W1-B10 ELIGIBLE; no new QID may be authored or the bank edited under this remediation's clean-room and no-invention rules).

**Correction to REC-PHON-30 (row edited by this addendum only; parent REC row text is superseded for consumption, not edited in place):**

| REC ID | Field | Was (B3C R1) | **Now (R2D)** |
|---|---|---|---|
| REC-PHON-30 | QID lineage | Q023, Q036 | **Q023 only.** Q036 is dropped as an adjacent-not-direct fit per A3 R1 §5 item 5. No substitute QID exists in the frozen bank for the send-time-enforcement question Q036 raises; that question is out of scope for GAP-PHON-10, which is about write-targeting, not send-time enforcement. If a future GMVQ revision adds a QID for "downstream consumer passes an unsanitized record" specifically, it would be the more precise fit; none exists today |

QID map after R2D (phone): 39 QIDs mapped directly (was 40 with the adjacent Q036 mapping now dropped and not replaced), one (Q039) partial lineage per B3C R1 §1.3. This is not a coverage measure.

---

## 2. `onboarding`

No REC action required. R-ONBD-1 (tally tagging) and R-ONBD-2 (wording) are both Proof-addendum-only corrections; the underlying REC rows (REC-ONBD-15, REC-ONBD-BR7, REC-ONBD-H3/G1) are unaffected in class, Lane B label or proof link. REC independently confirms (A2 R2D §2.2, §2.3, adopted here) that the facts behind both residuals are stable: 5 elevation constructs, all in `tests/`, none in runtime code; and the account/payment controller scan is a deeper (not wider) re-check of a narrower module set than the original A3 probe. Onboarding REC totals are unchanged from B3C R1 (54 rows).

---

## 3. `web_unsplash` — R-UNSP-1: PROVIDER-CLAIM sub-tag

**Adjudication adopted verbatim from A3 R1 §4.1:** the disposition `GAP — PROVIDER CLAIM, NOT SOURCE-PROVABLE` is correct as a qualifier on the GAP class and is **not** changed. A sub-tag is added to distinguish the two situations the single label previously conflated:

| Sub-tag | Meaning | Applies to |
|---|---|---|
| **`[BR-5(b): NO-EVIDENCE-TYPE]`** | No evidence type available to this programme — source, static, or authorized runtime/mock — can ever settle the claim. It is an assertion about a third party's contractual terms, establishable only by an out-of-band, non-technical artifact (the provider's own terms document) that this programme has no route to obtain or verify | REC-UNSP-BR5, part (b) |
| **`[G5: OUT-OF-SCOPE-EVIDENCE]`** | The claim is an ordinary empirical fact about a running third-party service (whether its hosts actually redirect). It is not source-provable and is outside the **authorized** observation scope of this remediation, but it is not unknowable in principle: an authorized provider-side observation, if ever commissioned, would settle it and the item would then become UPP | REC-UNSP-G5 |

**Corrections to existing REC rows (row text superseded for consumption; parent/B3C rows not edited in place):**

| REC ID | Field | Was (B3C R1) | **Now (R2D)** |
|---|---|---|---|
| REC-UNSP-BR5 | Part (b) class | `GAP — PROVIDER CLAIM, NOT SOURCE-PROVABLE` | `GAP — PROVIDER CLAIM, NOT SOURCE-PROVABLE ` **`[BR-5(b): NO-EVIDENCE-TYPE]`**. No class change. Consumption rule unchanged: MASTER must not consume part (b) as fact under any evidence type, present or future, within this programme |
| REC-UNSP-G5 | Class | `GAP — PROVIDER CLAIM, NOT SOURCE-PROVABLE` | `GAP — PROVIDER CLAIM, NOT SOURCE-PROVABLE` **`[G5: OUT-OF-SCOPE-EVIDENCE]`**. No class change. Consumption rule: MASTER must not consume as fact **now**; the item is eligible to become UPP (and only then to be closed) if and when an authorized provider-side observation is commissioned — this remediation authorizes no such observation and none was attempted |

**Re-derivation basis (A2 R2D §2.4, adopted here):** the only source basis for "as its API terms require" is the in-code docstring/comment at `main.py`@00cf725f L26 and L125 (re-fetched and hash-verified, no drift); it names no evidence route this programme has. G5 is a live-HTTP-behaviour question about hosts this remediation is barred from contacting (governing rule: "no request to Unsplash, its CDN, or any other external service"), which is a scope bar, not an evidentiary impossibility.

web_unsplash REC totals: unchanged at 53 rows (the two sub-tagged rows are edits to existing rows, not new rows).

---

## 4. Process-rule compliance (C1B rules 1–5, and MD-07/MD-08)

| # | Rule | Status | Evidence |
|---|---|---|---|
| 1 | Preserve A2 `MISSING_REQUIRED_RUNTIME_PROOF` labels | **MET / N-A**. No Lane B label of any existing row is changed. REC-PHON-31 (new) is UNCORROBORATED per A2's classing rule for a runtime-observable, unclassed item | Section 1.1 |
| 2 | Tag post-predeclaration text `POST-DECLARATION` | **MET / N-A**. This addendum is written before the Proof R2D predeclaration; nothing here is post-declaration text. No parent Proof text is touched by this REC addendum | — |
| 3 | REC scans all A1 item classes | **MET (for the new item)**. REC-PHON-31 is explicitly linked to the A1 business-rule/exception cluster REC-PHON-21 already covers (BR-6, EX1), rather than left as free-standing prose | Section 1.1 |
| 4 | REC frozen (sha256) before Proof; Proof records it | **MET.** This addendum's sha256 (recorded below at file-write time) will be written to scratch and consumed by the Proof R2D addendum header, before Proof R2D predeclares or fetches | Proof R2D addendum header |
| 5 | Predeclared cases hashed and UTC-stamped before the first Proof source fetch | **N-A for REC.** REC fetched no new source in this addendum; it reused the A2 R2D re-derivation and the frozen B3C blob logs | — |
| MD-07 | Anchor-only evidence, `git hash-object`-verified | **MET.** REC cites no new fetch beyond the A2 R2D re-derivation (section 0.1 of that addendum), all hash-verified with no drift | A2 R2D addendum §0.1 |
| MD-08 | Enumeration claims stated as bounded, not completeness | **MET.** The QID-bank scan for R-PHON-2 (section 1.2) is stated as a scan of the frozen 40-entry bank at its recorded sha256, not as a claim that no better QID could ever exist outside that bank | Section 1.2 |

## 5. Limitations

- No runtime evidence exists for REC-PHON-31; it stays UPP until PR-PHON-12 runs.
- The G5 sub-tag records that authorized provider-side observation *would* settle the claim; this remediation does not authorize or attempt any such observation, and none was made.
- QID lineage for phone_validation (W1-B10) permits an eligibility read; the onboarding and web_unsplash MVQ/bank state (HOLD / no bank) is unchanged and is not affected by this addendum.
- No percentages. No Formal Coverage claim. No QID answered. No git write operations. No existing artifact was edited.
