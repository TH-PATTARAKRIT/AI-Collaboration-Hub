# ACCOUNT WAVE A — `GB-08` PUBLICATION RECORD

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GB08-001` · Date `2026-09-04`

> **This is a receipt, not evidence.** It is excluded from the `GB08_DECISION/` manifest by design — it
> cites the roll-up, so it cannot be inside it. See `LAYER2_GB08_EVIDENCE/mkmanifest.sh`.

---

## 1. GitHub — `GITHUB EVIDENCE PUBLICATION VERIFIED` for the parent package

| Item | Value |
|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Branch | `research/account-wave-a-mcc-2026-09-04-001` |
| Branch URL | `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/tree/research/account-wave-a-mcc-2026-09-04-001` |
| **HEAD on `origin` at the time of the Jira comment** | `ba0b747bc4e39e6116013e967d4228aa6a2455e3` |
| `FINAL_CLOSURE/` roll-up, **recomputed from `origin` content** | `f6d168fdc95cad5114c6ab9ce3de21e230b9bba607b0ef436533b11491ff3781` — **match** |

**How it was verified — executed, not asserted:**

```
git push origin research/account-wave-a-mcc-2026-09-04-001        # [new branch]
git ls-remote origin refs/heads/research/account-wave-a-mcc-2026-09-04-001
git rev-parse HEAD ; git rev-parse origin/research/account-wave-a-mcc-2026-09-04-001
git archive origin/research/account-wave-a-mcc-2026-09-04-001 <package path> | tar -x -C <scratch>
cd <scratch>/…/ACCOUNT_WAVE_A_CORE_LEDGER && bash FINAL_CLOSURE/LAYER2_FC_EVIDENCE/mkmanifest.sh | shasum -a 256
```

The roll-up was recomputed from content **extracted from `origin`**, not from the working tree.

## 2. GitHub — `GB-08 EVIDENCE PACKAGE NOT PUBLISHED`

> # `GB-08 HOLD — EVIDENCE PACKAGE NOT PUBLISHED`

| Item | Value |
|---|---|
| Commit holding the `GB-08` package | **cited by content, not by SHA** — roll-up `9a51f4aa…` (`GB08_DECISION/`) and `d1430f43…` (amended `FINAL_CLOSURE/`). A document cannot name the commit that will contain it |
| **Present on `origin`** | **NO** |
| Blocker | The **second** `git push` was refused by the executing harness permission classifier |
| Not the cause | Credentials, the remote, or the repository — **the first push of this same session, same command form, succeeded** and created the branch |
| Workaround attempted | **None.** The control is deliberate and this session does not route around it |

**Remedy — one command, once push permission is re-granted:**

```
git -C "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MCC_2026_09_04_EXECUTION" \
    push origin research/account-wave-a-mcc-2026-09-04-001
```

**Then:** re-read from `origin`, recompute both roll-ups from the extracted content, and **update Jira
comment `10996` in place** with the new HEAD SHA. The comment already states that the `GB-08` package is
not yet on `origin`, so nothing published is inaccurate — it is incomplete, and it says so.

## 3. Jira — `JIRA EVIDENCE PUBLICATION VERIFIED`

| Item | Value |
|---|---|
| Site | `https://scgl.atlassian.net` · cloud id `67b5858f-f930-4950-af26-aa7662000e77` |
| Issue | **`ERPPLUS-138`** — *[STATE03][ACCOUNT-REOPEN] Accounting Core Full Reopen & 9-Council Deep Revalidation / L999.999* · project `ERPPLUS` |
| Issue URL | `https://scgl.atlassian.net/browse/ERPPLUS-138` |
| **Comment id** | **`10996`** |
| **Comment URL** | `https://scgl.atlassian.net/browse/ERPPLUS-138?focusedCommentId=10996` |
| Posted | `2026-09-04T21:14:27+07:00` by `SCG LEGACY` |
| Comments posted | **One** |
| **Issue status** | **`To Do` — NOT transitioned.** No AI may move a Boss gate |

**Order of operations, which was the rule and not a convenience:** the branch was pushed, re-read from
`origin`, and the roll-up recomputed from extracted `origin` content **before** any Jira text was
written. The comment states exactly what is on `origin` and exactly what is not.

## 4. Digests recorded

| Package | Roll-up |
|---|---|
| `FINAL_CLOSURE/` **as published at `ba0b747`** | `f6d168fdc95cad5114c6ab9ce3de21e230b9bba607b0ef436533b11491ff3781` |
| `FINAL_CLOSURE/` **after the `GB-08` amendment** | `d1430f43d6807ba2ea32662bef9086e598788fa9419e5eea31efdbed9466254b` |
| `GB08_DECISION/` | `9a51f4aaed8e63e94c41a153951dd8d5a62689463bf913854aaa658c0f4c0a72` |

All three recompute with `mkmanifest.sh | shasum -a 256` from the respective package directory.

## 5. What is **not** claimed here

- **Not claimed:** that the `GB-08` package is on `origin`. It is not, and §2 says so.
- **Not claimed:** any gate movement, approval, certification, or convergence.
- **Not claimed:** that `ERPPLUS-138` was transitioned. It was not.
- **Not done:** Wave B, implementation, source-code modification, merge, deploy.
