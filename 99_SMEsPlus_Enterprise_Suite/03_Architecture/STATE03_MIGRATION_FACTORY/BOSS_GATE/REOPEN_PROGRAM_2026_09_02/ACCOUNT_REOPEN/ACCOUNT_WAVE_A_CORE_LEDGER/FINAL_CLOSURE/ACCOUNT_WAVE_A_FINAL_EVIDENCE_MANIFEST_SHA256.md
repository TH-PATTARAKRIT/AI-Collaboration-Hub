# ACCOUNT WAVE A — FINAL CLOSURE EVIDENCE MANIFEST (SHA-256)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` (`aad8a1e25dfd08473c8fefbc90158f82d643e942`)
Generated `2026-09-04T14:13:35+0700`

> **Recommendation only. Boss is the sole Final Approver.**
>
> **`ER-CORE-8` — hash the package BEFORE review.** Any reviewer verdict on this package must name
> the roll-up digest below. The parent round shipped a package that changed while it was under
> review (`MCC_J` `J-17`); this manifest exists so that cannot happen silently here.

## 1. Roll-up

| Measure | Value |
|---|---|
| Files manifested | **14** |
| Markdown lines | **2387** |
| **Roll-up digest (SHA-256 of the per-file digest list)** | `f6d168fdc95cad5114c6ab9ce3de21e230b9bba607b0ef436533b11491ff3781` |
| Citable identity | **the roll-up digest above** — content-addressed, no commit-SHA regress |
| Branch | `research/account-wave-a-mcc-2026-09-04-001` |
| Published on `origin` | **NO** — see Gate Report §3 |

## 1a. Amendment `2026-09-04` — `GB-08` round

| Measure | Value |
|---|---|
| **Roll-up digest, `FINAL_CLOSURE/` as published at `ba0b747`** | `f6d168fdc95cad5114c6ab9ce3de21e230b9bba607b0ef436533b11491ff3781` |
| **Verified from `origin`** | **YES** — recomputed from content extracted with `git archive origin/research/account-wave-a-mcc-2026-09-04-001` into a scratch directory, then `mkmanifest.sh \| shasum -a 256`. **Match.** |
| **Roll-up digest, `FINAL_CLOSURE/` after this amendment** | `d1430f43d6807ba2ea32662bef9086e598788fa9419e5eea31efdbed9466254b` |
| Files changed by the amendment | **2** |
| `ACCOUNT_WAVE_A_FINAL_RESEARCH_GATE_REPORT.md` | `1e18eb32ade647b0013cba53a8c211257a8c291f8a8804b0003ada9aa829d6df` → `a6185191f251ffb86259a8a7daf2773c71a2fb0f420f3a3b3a4a70259fe0b1da` — publication status, the §5 denominator correction, and a new §9 `GB-08` status section |
| `ACCOUNT_WAVE_A_GB08_BOSS_DECISION_PACKAGE.md` | `04d67227ae3a44931c9b2a653e9ca4cf48d93fda1b43e10e7d8dd907f0e978ff` → `4d226f24205717b78826612d211ad9083abf8ae29728a6da64c0ea3fa10357b2` — **supersession banner only.** The original body is left unaltered so the six corrections stay auditable against what was published |
| Files unchanged | **12 of 14** — every digest in §2 other than the two above still verifies |
| **Companion package** | `../GB08_DECISION/`, roll-up `9a51f4aaed8e63e94c41a153951dd8d5a62689463bf913854aaa658c0f4c0a72` |
| Published on `origin` | **YES** — branch `research/account-wave-a-mcc-2026-09-04-001`, re-read from `origin`. Gate Report §3a |

> **§2 below is the manifest as published at `ba0b747` and is deliberately not rewritten.** A manifest
> whose history is overwritten cannot show that a package changed under review — which is the defect
> `ER-CORE-8` exists to prevent. The two changed digests are named above; regenerate with
> `mkmanifest.sh` to confirm the other twelve.

## 2. Per-file SHA-256

| SHA-256 | File |
|---|---|
| `c723cd09b0b4c5af26ce87cdb7e371fd149598a84e78ddbde9305317a14acdd4` | `ACCOUNT_WAVE_A_FINAL_BALANCED_BUT_WRONG_REGISTER.md` |
| `bbc18122ddbfbd56b9ceebd21ba2e59929eb69d1d2ba5022ace6a6b0b1110584` | `ACCOUNT_WAVE_A_FINAL_CLOSURE_MASTER.md` |
| `9560ce5bc1a9a3df0744f8aa76a7c3cc881c61e307ebfdb9b57b989a98fcbc83` | `ACCOUNT_WAVE_A_FINAL_GATING_UNKNOWN_REGISTER.md` |
| `fc61cd3b1450fce4dd77e3c045768e80d639bfd0f5259bb01e18c86e737667c3` | `ACCOUNT_WAVE_A_FINAL_METHOD_CONVERGENCE_REPORT.md` |
| `23392ac72ec96504a8813d928decdc3fc5de2f15fad9c3c1c29678084421c0ba` | `ACCOUNT_WAVE_A_FINAL_NEGATIVE_CLAIM_COMPLIANCE.md` |
| `1e18eb32ade647b0013cba53a8c211257a8c291f8a8804b0003ada9aa829d6df` | `ACCOUNT_WAVE_A_FINAL_RESEARCH_GATE_REPORT.md` |
| `62e0d825659213727aba62f10272fcda54ee52c35d731b2612485c6a0fcd942b` | `ACCOUNT_WAVE_A_FINAL_TOLERANCE_ZERO_REGISTER.md` |
| `04d67227ae3a44931c9b2a653e9ca4cf48d93fda1b43e10e7d8dd907f0e978ff` | `ACCOUNT_WAVE_A_GB08_BOSS_DECISION_PACKAGE.md` |
| `2b53afff3eed6a6317a4599dec053fab6629fbf0d3d679e8663186cb5aac0514` | `ACCOUNT_WAVE_A_MCU04_FINAL_DISPOSITION.md` |
| `c9292de0b754ac7f4331f998376fb31c577be13b4f2a40ad57958095516b4307` | `ACCOUNT_WAVE_B_NEW_SESSION_PROMPT_DRAFT.md` |
| `8d86b918ce9f6b8db221026f2bd405317b3523aabbe3e38c9997fc4040cf3ec9` | `ACCOUNT_WAVE_B_READINESS_PACKAGE.md` |
| `3bbb6d201f9fb8f92e69ae92f056baf532969fc4120b34c16efb8275ad24cf61` | `LAYER2_FC_EVIDENCE/fcscan.sh` |
| `21985838853402636050e1b0041bed35feba134db892fa281070b16af3661a38` | `LAYER2_FC_EVIDENCE/mkmanifest.sh` |
| `5e2049fe8744935a694f77adceb49bf59746e0eba4b6c251d85673f9001a99e5` | `SMEPLUS_VERY_DEEP_RESEARCH_STANDARD_CANDIDATE_L99999_99999.md` |

## 3. Reproduce

From `ACCOUNT_WAVE_A_CORE_LEDGER/`:

```
./FINAL_CLOSURE/LAYER2_FC_EVIDENCE/mkmanifest.sh | shasum -a 256
```

Compare against the roll-up digest in §1. The compliance scan is re-runnable the same way:

```
./FINAL_CLOSURE/LAYER2_FC_EVIDENCE/fcscan.sh
```

## 4. Parent package integrity

| Check | Result |
|---|---|
| Tracked files modified outside `FINAL_CLOSURE/` | **0** |
| Parent `MCC` package altered | **NO** — `DR-NC-06`: superseded parent text stands unedited |
| Source / product code modified | **NO** |
