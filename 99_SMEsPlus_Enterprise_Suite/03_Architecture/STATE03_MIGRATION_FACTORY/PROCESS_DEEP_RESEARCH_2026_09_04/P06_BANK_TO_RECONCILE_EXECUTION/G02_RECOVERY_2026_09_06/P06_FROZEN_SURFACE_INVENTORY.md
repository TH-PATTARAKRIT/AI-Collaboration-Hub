# P06_FROZEN_SURFACE_INVENTORY.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-FROZEN-SURFACE-RECOVERY-005]`
**Session:** P06 — INDEPENDENT FROZEN-SURFACE CORRECTION RECOVERY (CP-P06R01)
**Classification:** LAYER 2 — AUDIT QUARANTINE

> **Published before any correction edit, per prompt §4.** Nothing in this file is taken from a prior register. Every number is measured from the frozen tree.

---

## 1. Freeze, and the mismatch that had to be classified first

| Step | Result |
|---|---|
| §4.1 local HEAD at session start | `9c8e11151f275e74c6f0f9a3dfc2e370ff7667dd` |
| §4.2 authoritative remote SHA — `git ls-remote origin refs/heads/research/account-p06-bank-to-reconcile-2026-09-04-001` | **`52127569863455acc06b82a845ef64e106115900`** |
| **Match?** | **NO. Classified before proceeding, per §4.2** |

**`FSI-F-01` — The mismatch is benign and is classified, not waved through.**
```
git log --oneline 9c8e111..5212756
  → 5212756  prompt(P06): add independent frozen-surface recovery continuation
git diff --name-only 9c8e111 5212756 -- <P06 package root> | wc -l
  → 0
git merge-base --is-ancestor 9c8e111 5212756
  → YES (remote strictly ahead; no divergence)
```
**The remote had advanced by exactly one commit, which adds this prompt file and touches ZERO files in the P06 evidence package.** The surface under review is **byte-identical** at `9c8e111` (the prompt's stated baseline) and at `5212756`. Fast-forwarded; re-verified equal to the authoritative remote.

| §4.3 working-tree status | **clean — 0 dirty entries, 0 unpushed commits** |
|---|---|
| **FROZEN SHA** | **`52127569863455acc06b82a845ef64e106115900`** |

## 2. Frozen file list

| Root | Files |
|---|---|
| `…/P06_BANK_TO_RECONCILE_EXECUTION/*.md` | **70** |
| `…/G02_CLOSURE_2026_09_06/*.md` | **12** |
| `…/G02_VERIFICATION_2026_09_06/*.md` | **2** |
| **TOTAL** | **84** |

**Package manifest digest** — SHA-256 over the sorted per-file SHA-256 list, so a single value fixes the whole surface:
```
sort <per-file sha256 list> | shasum -a 256
  → 77638ffed38134af25ac7c44ddf5e18fae61ec377f45cda35b0576066c08f4d4
```
Per-file SHA-256 for all 84 files is recorded in §5.

## 3. §4.5 — the correction surface, enumerated from the files

**Measured over ALL THREE roots. UNIT: marker occurrence.** *(A marker occurrence is not the same unit as a correction — see `FSI-F-02`.)*

```
grep -ohE "REV-E-(18|19|20|21), 2026-09-06" *.md G02_CLOSURE_2026_09_06/*.md G02_VERIFICATION_2026_09_06/*.md | wc -l
grep -lE  "REV-E-(18|19|20|21), 2026-09-06" *.md G02_CLOSURE_2026_09_06/*.md G02_VERIFICATION_2026_09_06/*.md | wc -l
  → 30 occurrences in 15 files        [round 5 — UNCHANGED, as round 6 claimed]

grep -ohE "REV-E-22, 2026-09-06" *.md G02_CLOSURE_2026_09_06/*.md G02_VERIFICATION_2026_09_06/*.md | wc -l
grep -lE  "REV-E-22, 2026-09-06" *.md G02_CLOSURE_2026_09_06/*.md G02_VERIFICATION_2026_09_06/*.md | wc -l
  → 47 occurrences in 24 files        [round 6]
```

**`FSI-F-02` — The published figure "40 repairs across 20 files" REPRODUCES — but only after the unit is fixed, and the first attempt at this measurement said it did not.**

**The raw marker population is 47 occurrences in 24 files. The published figure is 40 in 20.** The 7-occurrence gap resolves entirely, and it resolves in favour of the published figure:

| Occurrence | Kind |
|---|---|
| `P06_CORRECTION_INTEGRITY_VERIFICATION_REGISTER.md`:123 | prose naming the marker |
| `…VERIFICATION_REGISTER.md`:126, :127 | **the printed text of the counting command itself** |
| `P06_AUTO_RESUME_STATE.md`:88 | prose restating the figure |
| `P06_AUTO_RESUME_STATE.md`:94 | **the printed text of the counting command itself** |
| `P06_CHECKPOINT_REGISTER.md`:70 | prose |
| `P06_EVIDENCE_MANIFEST_G02.md`:73 | **the printed text of the counting command itself** |

**47 − 7 narrative references = 40 repairs, in exactly 20 files.** Verified per file.

> **This entry was written twice.** Its first form asserted that the published figure *"does NOT reproduce"* and attributed the gap to an excluded directory and a stale count. **That was wrong, and it is left on the record rather than deleted.** The gap is neither: it is a **unit** difference. A *marker occurrence* and a *repair* are different things, and **four of the seven extra occurrences are the counting command's own printed form** — a grep for a literal marker will always match the documentation of that grep. Recorded as **`VER-E-03`** in `P06_VERIFICATION_TOOL_DEFECT_REGISTER.md`.
>
> **The published count was right. The instrument that first checked it was wrong, and it was wrong in the direction of accusing the package.** *An audit instrument that produces false positives is not safer than one that produces false negatives; it is differently unsafe, and it is more persuasive.*

**`FSI-F-03` — Unit definitions fixed for this round, before any adjudication.**

> **REPAIR** — a marker occurrence attached to a statement whose wording was changed.
> **REFERENCE** — a marker occurrence inside prose or a command string describing the repair programme.
> **CURRENT STATEMENT** — the package asserts this as true now.
> **HISTORICAL RECORD** — a quotation of a past statement, a revision-log row, a before/after table, a challenge quote, a supersession note. **Correct to leave uncorrected.**

**Prompt §7: *"A marker count is not a completeness proof."* Confirmed from the opposite direction as well — a marker count is not even a repair count.**

## 4. §6 — verification surface, declared before Stage 1

| Band | Content | Size at freeze |
|---|---|---|
| **A** | `REV-E-22` occurrences | **47 in 24 files** *(not 40 in 20)* |
| **B** | Every current statement in the same corrected claim classes, marker or no marker | measured in Stage 1 by claim class |
| **C** | Outbound handoff / ownership / dependency / contradiction / checkpoint / auto-resume / manifest records | `18_`, `34_`, `35_`, `36_`, `38_`, `40_`, `53_`, `54_`, `70_`, `G02_CLOSURE/*`, `G02_VERIFICATION/*` |
| **D** | P11-facing propagation — **truth of P06's outbound wording only.** No P11 internals | as above |
| **E** | Session-local residual claims to reproduce or refute: **15** material stale statements · **9** P11-facing false statements · tool defects `VER-E-01`, `VER-E-02` | Stage 1 |

**Nine claim classes carried into Stage 1** — derived from what rounds 5 and 6 corrected, stated as *semantic assertions* rather than as phrases, because scoping by phrase is the defect both prior rounds committed:
1. `X-08`/`D-08`/`PD-08` — answered vs closable vs closed.
2. Peer publication status (P01, P08).
3. Evidence base — "filtered" vs "relocated".
4. `is_matched` — branch/site count and the unconditional-vs-configuration qualifier.
5. "Eighth settlement door".
6. `res.config.settings` ACL breadth.
7. `ir.sequence` reset ⇒ numbers "re-issuable".
8. Generation gap — "only deployment evidence is Odoo 19".
9. Stated `P06-B-*` population totals.

## 5. Per-file SHA-256 at the frozen SHA

| File | Lines | Bytes | SHA-256 |
|---|---|---|---|
| `01_P06_PAYMENT_STATE_MODEL.md` | 280 | 25622 | `d6172f569fc7d3457dbce43e739329c37cee113c963f95fe51d8bda3367f5ffd` |
| `02_P06_BANK_EVENT_REGISTER.md` | 210 | 21174 | `8aaa296751bd0f861dad306c569c6545916980963588539b14709724868f69e3` |
| `03_P06_SETTLEMENT_STATE_MATRIX.md` | 155 | 13809 | `e7ab942b9bd98e80a592b4c9119e5a00b4c53a753451106e3973907061751639` |
| `04_P06_RECONCILIATION_MODEL.md` | 248 | 21869 | `8984b0f9476e8a1598aa288215f61002673561688a9b07cc121660840bf2340f` |
| `05_P06_EVENT_TO_GL_MATRIX.md` | 179 | 17460 | `ce059dccee5a56743b5fd889c65de0c8ae0f32a4ac14dbe1716b2fae473ee881` |
| `06_P06_FX_FEE_INTEREST_MATRIX.md` | 204 | 16260 | `2c9da2c199aacc0830e77e30a342b23c34f87b7d36999a43ad4675722d627cdf` |
| `07_P06_DUPLICATE_MATCH_ATTACK.md` | 252 | 22749 | `de59a506f668f4af22fd982c726c5eb6120d0c225724ca84232960d1f683b546` |
| `08_P06_PAYMENT_PROVIDER_TRACE.md` | 226 | 19669 | `004f5653a50e9b9ee2ff59e763e2611e62deab5e78c48a6b4b34b7f8b82b47eb` |
| `09_P06_CROSS_PROCESS_OWNERSHIP.md` | 125 | 13749 | `89929f9850e87382400a348e8dd36693987588494559fc14e9df18e52e69821a` |
| `10_P06_EDGE_CASE_MATRIX.md` | 210 | 21813 | `e498b0e79cddaf5f11082448e5c7be36957d12b764c0259e346cfff81bb6db5a` |
| `11_P06_CONTRADICTION_REGISTER.md` | 210 | 24045 | `432405bdcc2d77796755cb9bfe08216c31657dfa72305c99eafc65dbf2f59905` |
| `12_P06_SOURCE_LINK_REGISTER.md` | 216 | 19484 | `61af605ec3f1c9a8303982cd562ace4d10300d64cc4c1d3eb98622b2aae2ca25` |
| `13_P06_EVIDENCE_MANIFEST.md` | 154 | 12247 | `6cc7293e5939ea41e5986ee0642633fe8b76edcd2c38c177e9fc3c3744c1b5e8` |
| `14_P06_REVISION_LOG.md` | 115 | 10448 | `850338891d8d6e042df4a94bd3c832a8038e79447357140f8cd3ab3c91173e9b` |
| `15_P06_AAS03_CHALLENGE.md` | 116 | 12564 | `b2d8a7daf39fe744cd28736cf27842ac0d6c7328de881106474639abd4578f03` |
| `16_P06_AAS_PLUS.md` | 143 | 14214 | `84cd452476941cdeba3f3846192050c8f50f270a64c04b044921a4bfdf53aecc` |
| `17_P06_PMO.md` | 164 | 12248 | `84dededd9719d482e2319fff5557178bcbd534c2dcd1bfd5e5022d135e1bc4a2` |
| `18_P06_CORE_RECON_HANDOFF_PACK.md` | 214 | 17546 | `b5910a2f6a4810d7accced1a65ec455ececfda69da954747d5149f3f6c2d07ca` |
| `19_P06_SCOPE_OWNERSHIP_MATRIX.md` | 214 | 25930 | `67fd7d2023c7bbd93f2538c761a633618ccb89f92a8145bc95fad3e8ecc068e0` |
| `20_P06_CUSTOM_MODULE_DELTA.md` | 315 | 31411 | `6083f83255d5fb4593492a0c4326887e2cde05279044af333b7447721430c83d` |
| `21_P06_CURRENT_STATE_RECONCILIATION.md` | 109 | 6495 | `3172ba7f03c69f7da20f11977825ce554c7cdd59bfeb7923aca2c6567db5c275` |
| `22_P06_B27_ROOT_ID_FORENSIC.md` | 162 | 9899 | `c9862dc6a0655f7e806a56fee63419ea2eb795f45f7d237c9ea96ba4f2c4ea21` |
| `23_P06_B27_DEPENDENCY_CLOSURE_GRAPH.md` | 100 | 8580 | `a31ecf5237f46b161c395d4260ec780fa14e3def80f5508fb85f410bb4c13853` |
| `24_P06_DEPLOYED_MODULE_EVIDENCE.md` | 109 | 7952 | `4a3eba9945894a6e71e04b44bd35c98d15cebc99f78971e6fe61289d18895276` |
| `25_P06_PAYMENT_BANK_RECONCILIATION_STATE_MODEL.md` | 141 | 9770 | `0915b86818f3ce14b6472f0fb6366842cf5aafa4368e3799a8e2c59ef5acfdfd` |
| `26_P06_BANK_INGESTION_IDENTITY_MATRIX.md` | 116 | 8263 | `4b8953564a43fd433a3a244c5573a9a2734dc62e35575eaadec18ca2c8ad0edc` |
| `27_P06_DUPLICATE_INGESTION_THREAT_MATRIX.md` | 88 | 7377 | `86c5b2824e9c34493df9e76b7c5f8c0ac8a0e0eadc57979f2eea7589f98cd26c` |
| `28_P06_PERIOD_CLOSE_RECONCILIATION_MATRIX.md` | 111 | 8970 | `3df5a5001f2d6f4b071a545cce2006f1f643ed8655ee3eb0bd8d1c966a2435d7` |
| `29_P06_BANK_ADJUSTMENT_EVENT_MATRIX.md` | 115 | 7881 | `c193cd355a75a057afc67ed4c969ee55e03891a17cbf8459e7368ced6ac2027a` |
| `30_P06_RETURNED_PAYMENT_LIFECYCLE.md` | 97 | 7218 | `a1d41e53777a903b43665f5bcb3baed4b53b40132ae034c09aca363aab6885d4` |
| `31_P06_PAYMENT_TOKEN_SCOPE_REVALIDATION.md` | 109 | 8652 | `53c0092d6f30ff9228e91da32fe85ce4274fd706c200c77cb8de62a153681abb` |
| `32_P06_BUSINESS_EVENT_REGISTER.md` | 63 | 5295 | `e058b4584285c50b67e27ebc42e01e805a074d64bc19b18abf8090443015784e` |
| `33_P06_ACCOUNTING_EVENT_REGISTER.md` | 63 | 4144 | `bdd832bb7116c3e7fbb879be721797898367739c1d674524b5539f2b018233c3` |
| `34_P06_CROSS_PROCESS_OWNERSHIP_REGISTER.md` | 103 | 11529 | `112796f040d3303428c2dfaf384fb98e26b3cf6efcf5b2dfb8eda7008c0e914d` |
| `35_P06_PEER_HANDOFF_MATRIX.md` | 163 | 16890 | `a66169b9a6f76fb9644f825fe497eca387774f1ab4c31d1681267a7f5ff40e66` |
| `36_P06_DEPENDENCY_REGISTER.md` | 68 | 7781 | `95b7eea1c18290aff1aa80d9a10620267b1bc89041890dc3446c6797ab8a091c` |
| `37_P06_SCOPE_REGISTER.md` | 118 | 8197 | `0cb8570bb530b3f93fdafd471db5fa3912e5387d07d6c1c1f2620096d22c56be` |
| `38_P06_UNRESOLVED_EVIDENCE_REGISTER.md` | 134 | 11027 | `da8ab75d796f8aa6b38f8749b1c058f91dbadb042f701e5f949f9e3695163919` |
| `39_P06_RESEARCH_ERROR_AND_REVISION_LOG.md` | 123 | 12083 | `9f535f5e1ed379320ad41694dd4b04bc9ec5ec4397b70c0a5a29fb38d61d28b4` |
| `40_P06_TARGETED_BLOCKER_REGISTER.md` | 256 | 25551 | `a86a3a572d2a29b028f0607ed19b575215e60cd7b244a9081d87d0827f85d165` |
| `41_P06_AAS03_TARGETED_CLOSURE_CHALLENGE.md` | 133 | 13595 | `75656a1d297d8ed563a060fd53264836839f1eb3880d8d8882944cb253404c4a` |
| `42_P06_AAS_PLUS_VETO_RECHECK.md` | 99 | 9317 | `c260c698f94e47baf8ce4f5c3d39f01983b38ff1f9e0371377b17cdf3ca120af` |
| `43_P06_PMO_TARGETED_EXIT_REVIEW.md` | 140 | 9813 | `cb1e91ac86ad4fa19a7fffa1fcb808ddf2caf31d499d891cd876148d094d29a0` |
| `44_P06_OM_DATA_REMOVE_FORENSIC.md` | 216 | 12112 | `445c22e018c431530c56a0c9987c93a1ed4e72881a0813757b840aa57cd30ea6` |
| `45_P06_OM_DATA_REMOVE_AUTHORIZATION_FORENSIC.md` | 156 | 9639 | `1ce1c9236736371d00a7567056f677734239b584f36f68b1ca29e2217e6a2680` |
| `46_P06_55_BLOCKER_SEVERITY_REGISTER.md` | 139 | 13634 | `d86f56fcbcb21551bb2aeaa6b67ee4e0541b1f1517b959158429b43ef7003f9d` |
| `47_P06_BLOCKER_RISK_HEATMAP.md` | 88 | 6417 | `a05b066da1ed0ca058f5d48a66bfd50ba7704911c0f5f69d3aa66196497ec3d3` |
| `48_P06_BLOCKER_LEVERAGE_GRAPH.md` | 113 | 8818 | `8a6ff514e3902c499f4b617aeb739a7405ea179a2cdbcb0ae52ead2d7df86520` |
| `49_P06_OM_DATA_REMOVE_REACHABILITY.md` | 109 | 8272 | `b0fe054fdbdcdabc65d9632375158e7c90a371fd53734168656492cc1a156659` |
| `50_P06_OM_DATA_REMOVE_SCOPE_MATRIX.md` | 92 | 7167 | `fae2f3d414b5543fd3c22a8556d9cb2826686972fe6cf40281af13793cb25790` |
| `51_P06_VERSION_DEPLOYMENT_EVIDENCE_BOUNDARY.md` | 105 | 9403 | `01b6a6c79b3ac3675469e4431b52d1af9fee48a0698352e3d6c770cc4a26c57d` |
| `52_P06_XC01_P02_RECONCILIATION.md` | 103 | 6955 | `e9d016d44852e7687c186e3157872e8e7bcf561c39ab2d37748f9b46c10ed357` |
| `53_P06_P08_INTAKE_AND_DEPENDENCY_REFRESH.md` | 126 | 10614 | `f1dd5ac4d866a9a743fcc480fb90b9267b29c39f1e7b8f8e70b4147e3300f0ba` |
| `54_P06_P07_BLOCKING_DEPENDENCY_MATRIX.md` | 99 | 9417 | `f26b499680bb0488580e617afaa550930017262a193e926702074021748f1f6c` |
| `55_P06_SETTLEMENT_DOOR_DENOMINATOR_REVISION.md` | 95 | 6217 | `f0866d233d0c13ece2d1193c108a14e9fb8dc356d9748283fc9ff86fcd3230eb` |
| `56_P06_FILTERED_TREE_EVIDENCE_BOUNDARY.md` | 107 | 7607 | `2f4bcb92363a34bdefa69241b0f5cdc0a6266148c27a13986a7feaf87bbe2453` |
| `57_P06_BANK_ADJUSTMENT_NEGATIVE_CLAIM_RECHECK.md` | 59 | 4025 | `4cfa6f28449cb33c2ba0c3bd3561cf00024b8340b8987580309d883e7b4d0703` |
| `58_P06_DEPLOYED_MODULE_REGISTRY_PROOF.md` | 137 | 9133 | `593fa547993125bd0ff42e57b3306aa3765322f1a05fdec6df5c05cb67caeb76` |
| `59_P06_DESTRUCTIVE_DATA_PATH_GRAPH.md` | 150 | 10050 | `8dbd6d7b1d3217013d99bcccd52ac1ed0a2d1035fa7cb135b439da5050913e21` |
| `60_P06_DESTRUCTIVE_FINANCIAL_INTEGRITY_MATRIX.md` | 79 | 6304 | `fd1b9c9b347a13a8ecb1412f45224fc667e800a6a5253befe05c1538392685db` |
| `61_P06_SEQUENCE_REWIND_FORENSIC.md` | 110 | 8040 | `338e65455aed121ba776cadd026f12889a870c145da7450b678c1a2dd2e84a8d` |
| `62_P06_TARGETED_CLOSURE_AUTHOR_ERROR_REVISION.md` | 134 | 11603 | `8e9b8521fa5e5492c5ef08771248ec9cf0143f2ab208d792c7858d32a511bca2` |
| `63_P06_FAILED_PAYMENT_SEMANTIC_HARDENING.md` | 68 | 4060 | `5e173d93c25bb573ae0ff8d9dc05d19c2d6b54f259828d26cd192ff12c3b572d` |
| `64_P06_PERIOD_CLOSE_WRONG_MOVE_RECONCILIATION.md` | 89 | 6766 | `1e2ffd5ebdcb22f4a0b45c397228be04068c4a08e820c81e7cd22cb9351bf308` |
| `65_P06_AAS03_SUPPLEMENTAL_CHALLENGE.md` | 126 | 15731 | `96e2895f9a222accb097df3b6699e4096db0e134722c1341096cd42bbed44fb2` |
| `66_P06_AAS_PLUS_VETO_SUPPLEMENTAL_RECHECK.md` | 85 | 6179 | `261e6e0385f2c0b016a93383f402113214d41dc8b6b80f50aaccaf8c10caa8ee` |
| `67_P06_AAS_PLUS_SUPPLEMENTAL_CONSOLIDATION.md` | 51 | 4461 | `cd5380955501eac56f99b0eb8d66d6052157d712344ddfab20e8397f13d5d070` |
| `68_P06_CURRENT_STATE_SUPPLEMENTAL_RECONCILIATION.md` | 67 | 3804 | `d473a176f048e54142d860c36b28b5680ee015976965cf839f17c5d009cd4036` |
| `69_P06_PMO_SUPPLEMENTAL_REVIEW.md` | 88 | 7331 | `aa1a4c6934dcfe0fe343981f98ec7af84e3a30369866b46ad0e7a3764d4cbf33` |
| `70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md` | 110 | 7384 | `1c465adb2544aed85ccb0cf4404bf4ca89ee65485e64204e16338cb807c6ca66` |
| `G02_CLOSURE_2026_09_06/P06_AAS03_BOUNDED_CHALLENGE.md` | 114 | 14293 | `b3a94ab1e0b028ffe2ba0c219983609b14801c0aa77bce6c251abf4fdaf28d29` |
| `G02_CLOSURE_2026_09_06/P06_AAS_PLUS_CONSOLIDATION.md` | 90 | 11809 | `d35366c58af57f5e3fcb2e5cfea1b9820c2242c99205304fb677764b9c16bb01` |
| `G02_CLOSURE_2026_09_06/P06_AUTO_RESUME_STATE.md` | 132 | 9219 | `4fbe414c4d101d8d799df89bfa390a7690abebd2f2b7c1ba4ccefda192927a3c` |
| `G02_CLOSURE_2026_09_06/P06_CANDIDATE_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` | 209 | 22287 | `6d3c27e8ba418e9beedfaa8b3c53f17fa394486f5ca9a570524d209a019ba4e4` |
| `G02_CLOSURE_2026_09_06/P06_CHECKPOINT_REGISTER.md` | 87 | 8761 | `01391d9f60d28635016392d5ea408843913f17422fa8ca0b53957a0683b54859` |
| `G02_CLOSURE_2026_09_06/P06_CONTRADICTION_AND_REVISION_SUPPLEMENT.md` | 203 | 19963 | `6d2d8af979c84e6fc2502b4692a5cdf4b2db00d3adbbc2fd64fe816e9b8e303f` |
| `G02_CLOSURE_2026_09_06/P06_DOMAIN_PURITY_AND_BOUNDARY_REGISTER.md` | 64 | 7341 | `f1cc988db8a3ddb286799475bc43ca41d61166cae8a711041289fc1116ce6dc1` |
| `G02_CLOSURE_2026_09_06/P06_EVIDENCE_MANIFEST_G02.md` | 114 | 10834 | `6a02c094cf8ba0b04227df36fc1c345c185bf12888594b3001b40d81f1b3fbf3` |
| `G02_CLOSURE_2026_09_06/P06_IEVING_LEDGER_STATE_FORENSIC.md` | 153 | 11432 | `b18d51b2172136151da13a2c43e31576fc3556373c2da108a01e23f845d94104` |
| `G02_CLOSURE_2026_09_06/P06_P10_MATERIAL_DELTA_REGISTER.md` | 289 | 29618 | `e1fa3cf89ecfb8cc3f8b342bcfeface4d91d748eeaddc7a4fbb7a7a602054566` |
| `G02_CLOSURE_2026_09_06/P06_PMO_TERMINAL_REVIEW.md` | 106 | 11087 | `85dbeef19af7e8c5d5f66c2a9e06e32ea5a799feaa98801e2d8b66b9f61db6da` |
| `G02_CLOSURE_2026_09_06/P06_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md` | 173 | 17484 | `108ebe9d8549e4a5c55d0362e65fd760e04565f952bdbcf8e9a347e2fcf8cbf8` |
| `G02_VERIFICATION_2026_09_06/P06_CORRECTION_INTEGRITY_VERIFICATION_REGISTER.md` | 173 | 20204 | `15b3730f2a607e2c8223557361b16d4531c9d9285a0f83aa8fd20237c49abe27` |
| `G02_VERIFICATION_2026_09_06/P06_CORRECTION_PROPAGATION_MATRIX.md` | 72 | 7658 | `ffa1acc615f97778d8ce7259c443b92dbbaa4c80f73da1992c89de2a33880bf3` |

**This inventory was written before any correction edit of this round, per §4.**
