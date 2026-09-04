# ACCOUNT WAVE A — FINAL RESEARCH GATE REPORT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` (`aad8a1e`) · Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001`
Date `2026-09-04`

> **Recommendation only. Boss is the sole Final Approver. No AI may declare Final Approval.**

> ## Amended `2026-09-04` by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GB08-001`
>
> Three sections are amended and one is added. **The gate recommendation is unchanged.**
> - **§1, §3** — GitHub publication is now **VERIFIED**; the branch is on `origin` and was re-read from it.
> - **§1, §4** — Jira publication is now **VERIFIED**; one evidence comment is posted on `ERPPLUS-138`.
> - **§5** — the published denominator is corrected: it overlaps (`GB08-F3`).
> - **§9 (new)** — `GB-08` status, and six corrections to the `GB-08` package.

---

## 1. Wave A status

| Dimension | Status |
|---|---|
| **Research status** | **COMPLETE AS AN EXERCISE.** Every task in the round instruction executed to its end. Six parent findings re-verified from primary source; five reproduced exactly, one corrected |
| **Method convergence** | **`NOT CONVERGED`.** `MC-01`…`MC-10` = **7 not met · 2 partially met · 1 met** (parent 8/2/0). **`MC-04` Repeatability reaches `MET` — the first `MET` in the programme's history.** Fixed point `NOT REACHED` |
| **Evidence status** | **VERIFIED AND MANIFESTED.** 13 documents + 1 re-runnable scan script; per-file SHA-256 and roll-up digest; clean working tree; parent commits `33cdc6f` and `aad8a1e` both proven ancestors |
| **GitHub publication** | **`GITHUB EVIDENCE PUBLICATION VERIFIED`** — §3, amended |
| **Jira publication** | **`JIRA EVIDENCE PUBLICATION VERIFIED`** — §4, amended |
| **Remaining unknowns** | **17 standing** (corrected membership) + 2 opened by this round |
| **Remaining gating unknowns** | **8 ledger-gating · 2 gate-gating method controls.** `MCU-21` is both and is the parent of three others |
| **Tolerance-zero status** | **12 boundaries · `0` resolved · `0` opened by this round** |
| **`MCU-04` disposition** | **`VERIFIED DEFECT`** |
| **`GB-08` decision requirement** | **`BOSS DECISION REQUIRED — GB-08`** — decision package complete, §9 |

---

## 2. Panel completion

**Tested mechanically, not assumed.** The sibling **AAS+ Redesign** panel (`…-AASR-001`) was **actively
writing when this session began** — 20 files in 4 minutes at 13:44, with an independent veto report
appearing mid-session. It reached terminal state at **13:56** (24 files, evidence manifest written, zero
writes thereafter).

Its declared terminal state, quoted as data:

> `ACCOUNT WAVE A — PROVISIONAL PARALLEL SYNTHESIS · AAS+ OUTPUT IS NOT CANONICAL`
> `AWAITING PARENT CONVERGENCE, REGISTER CLOSURE AND DELTA REVALIDATION`

`AASR-VETO-01` **upheld**. **All Wave A panels are now finished. The criterion was not met when this
session opened.**

---

## 3. GitHub publication — declared, not assumed

> # `GITHUB EVIDENCE PUBLICATION NOT VERIFIED`
>
> ## **AMENDED `2026-09-04` — now `GITHUB EVIDENCE PUBLICATION VERIFIED`.** See §3a.

| Item | Value | Verified how |
|---|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` | `git remote get-url origin` |
| Branch | `research/account-wave-a-mcc-2026-09-04-001` | `git branch --show-current` |
| **First closure commit** | `0a101b95c4f375e9d743dfa52ea3e6a9b050f69c` | `git rev-parse` |
| **Branch HEAD at publication** | assigned by the final commit; **recorded in the Jira comment at posting time** | see note below |
| **Content identity — cite this** | **manifest roll-up digest**, `ACCOUNT_WAVE_A_FINAL_EVIDENCE_MANIFEST_SHA256.md` §1 | `mkmanifest.sh \| shasum -a 256` |
| Parent `MCC` commit | `aad8a1e25dfd08473c8fefbc90158f82d643e942` | `git merge-base --is-ancestor` → **yes** |
| Grandparent `MC` commit | `33cdc6fa009c4eafcca543c253ccad19e97fd0dc` | `git merge-base --is-ancestor` → **yes** |
| Working tree | **clean, 0 uncommitted** | `git status --porcelain` |
| Scope | **only `FINAL_CLOSURE/`** — 0 files touched elsewhere | `git diff --cached --name-only` |
| **Branch present on `origin`** | **NO** | `git ls-remote --heads origin \| grep -c mcc` → **`0`** |

> **Why the content digest and not a commit SHA.** A commit cannot contain its own SHA, so a package
> that cites its own commit is always one commit stale. **The manifest roll-up digest is
> content-addressed and has no such regress** — it is stable, independently recomputable by
> `mkmanifest.sh | shasum -a 256`, and it is what a reviewer should name under `ER-CORE-8`. The branch
> HEAD SHA is resolved and published **at posting time**, which is the only moment it is knowable and
> the moment the Jira comment is written.

### What changed from the parent round, and what did not

| | Parent (`MCC`) | **This session** |
|---|---|---|
| `git push --dry-run` | not attempted | **SUCCEEDED** — remote reachable, credentials valid, `[new branch]` reported |
| `git push` (real) | **refused by the harness permission classifier** | **REFUSED by the harness permission classifier** |

> **The blocker is isolated and named.** It is **not** credentials, **not** the remote, and **not** the
> repository — the dry-run negotiated with `origin` successfully and reported the branch it would
> create. **It is the executing harness's write-permission control.** No workaround was attempted; that
> control is deliberate and this session does not route around it.

**Remedy — one command, once push permission is granted:**

```
git -C "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MCC_2026_09_04_EXECUTION" \
    push -u origin research/account-wave-a-mcc-2026-09-04-001
```

**The address the branch will occupy — NOT asserted as live:**
`https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/tree/research/account-wave-a-mcc-2026-09-04-001`

### §3a — Publication, executed and verified from `origin`

| Item | Value | Verified how |
|---|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` | `git remote -v` |
| Branch | `research/account-wave-a-mcc-2026-09-04-001` | pushed `[new branch]` |
| **Branch present on `origin`** | **YES** | `git ls-remote origin refs/heads/research/account-wave-a-mcc-2026-09-04-001` returns a SHA |
| **Local HEAD == origin HEAD** | **YES** | `git rev-parse HEAD` == `git rev-parse origin/research/…` |
| Package readable **from `origin`, not the working tree** | **YES** | `git archive origin/research/… <package path> \| tar -x` into a scratch directory |
| **Manifest roll-up recomputed from the extracted `origin` content** | `f6d168fdc95cad5114c6ab9ce3de21e230b9bba607b0ef436533b11491ff3781` | `mkmanifest.sh \| shasum -a 256` — **matches the digest published in `ACCOUNT_WAVE_A_FINAL_EVIDENCE_MANIFEST_SHA256.md §1`** |
| Branch URL | `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/tree/research/account-wave-a-mcc-2026-09-04-001` | live |

> **The blocker named in §3 was correctly diagnosed.** It was the harness write-permission control, not
> credentials and not the remote. Once Boss granted the push permission path the recorded remedy command
> executed unchanged and the branch landed. **No workaround was used at any point.**
>
> **Note on the digest.** `f6d168fd…` identifies the `FINAL_CLOSURE/` package **as published at
> `ba0b747`**. The `GB-08` amendment adds a new directory, `GB08_DECISION/`, with its **own** manifest
> and roll-up digest, and it edits this report — so `FINAL_CLOSURE/`'s digest is **regenerated** in the
> same commit and both values are recorded in `ACCOUNT_WAVE_A_FINAL_EVIDENCE_MANIFEST_SHA256.md`.

**Related lineage correction (`FC-F5`).** `MCC_L` recorded the `MCC` prompt as *"NOT COMMITTED"*. It
**is** committed — as `c32a924` on `origin/research/account-wave-a-mc-2026-09-04-001`, together with
the AAS+ prompt (`c6aa32b`) and **this round's own prompt** (`b6cc260`). The parent searched **its own
branch** and reported an **unbounded** absence. **The negative-claim defect, appearing in a governance
claim.**

---

## 4. Jira publication — withheld by rule, not failed

> # `JIRA EVIDENCE PUBLICATION NOT VERIFIED`
>
> ## **AMENDED `2026-09-04` — now `JIRA EVIDENCE PUBLICATION VERIFIED`.** See §4a.

**Reachability tested this session, not inherited:**

| Check | Result |
|---|---|
| Atlassian identity | **Authenticated** — `SCG LEGACY`, `scgl.thailand@gmail.com` |
| Site / cloud id | `https://scgl.atlassian.net` · `67b5858f-f930-4950-af26-aa7662000e77` |
| Governing issue | **`ERPPLUS-138`** — *[STATE03][ACCOUNT-REOPEN] Accounting Core Full Reopen & 9-Council Deep Revalidation / L999.999* |
| Project | `ERPPLUS` — SMEsPlus ERP SYSTEMS |
| Issue status | **`To Do`** · last updated `2026-09-04T11:12:55+07:00` |
| Issue link | `https://scgl.atlassian.net/browse/ERPPLUS-138` |
| **Comment posted** | **NO** |
| **Status transitioned** | **NO** |

**Reason — a decision, not a failure.** The round instruction §2 forbids representing this package in
Jira with a dead branch link, and §3 permits the comment **only after** live GitHub verification.
**The package is not published. A comment citing a branch absent from `origin` is the fabricated
evidence trail the instruction forbids.**

**The comment is drafted and ready. It will carry the live branch link, the branch HEAD SHA resolved
at posting time, and the manifest roll-up digest, and it will be posted by
the next session immediately after the push lands and is re-read from `origin`.**

### §4a — Posted, after `origin` verification and not before

| Check | Result |
|---|---|
| Atlassian identity | **Authenticated** — site `https://scgl.atlassian.net`, cloud id `67b5858f-f930-4950-af26-aa7662000e77` |
| Governing issue | **`ERPPLUS-138`** — *[STATE03][ACCOUNT-REOPEN] Accounting Core Full Reopen & 9-Council Deep Revalidation / L999.999* · project `ERPPLUS` |
| Issue status at posting | **`To Do`** — **not transitioned.** No AI may move a Boss gate |
| **Comment posted** | **YES** — one comment, after the branch was verified on `origin` and re-read from it |
| Comment content | live branch link · HEAD SHA resolved at posting time · both manifest roll-up digests · gate recommendation · `GB-08` status |
| **Status transitioned** | **NO** — deliberately |

> **The order of operations was the rule, not a convenience.** The branch was pushed, re-read from
> `origin`, and the manifest roll-up recomputed from the extracted `origin` content **before** any Jira
> text was written. The exact comment identifier and URL are recorded in
> `GB08_DECISION/ACCOUNT_WAVE_A_GB08_PUBLICATION_RECORD.md`, which is committed **after** the comment
> exists — a document cannot contain its own posting receipt any more than a commit can contain its own
> SHA.

---

## 5. Progress

> # `NOT CALCULABLE FROM VERIFIED BASELINE`

**`% Board`, `% STATE` and `% STEP` are not reported, and the reason is now precise rather than
cautious:**

A percentage needs a denominator. **This round established that the programme's denominator is
undeclared at its root:** 1 reference core root of **22** was searched; **1,753** manifested modules of
**23,530** raw were in scope; and no artefact states which root, or that a choice was made.

**Publishing a percentage against that baseline would be the exact defect this round exists to report.**

**What *is* calculable, and is reported instead:**

| Measure | Value | Denominator status |
|---|---|---|
| Gating unknowns dispositioned | **17 of 17** | verified — the register is the population |
| Gating unknowns closed by `MCC`+`FC` | **10 of 17 (58.8%)** | verified; **`MCC_00` publishes 9 — see `FC-F1`** |
| Tolerance-zero boundaries resolved | **0 of 12** | verified |
| `MC-01`…`MC-10` met | **1 of 10** | verified |
| Blockers open | **8 of 8** (`GB-01`…`GB-08`) | verified |
| Parent findings re-verified this round | **6**; 5 exact, 1 corrected | verified |
| Reference core roots searched | **1 of 22** (parent) · **6 of 22** (this round, for `MCU-04`) · **22 of 22** (`GB-08` round, for the rate chain) | **verified for the first time** |

> ### Amendment `2026-09-04` — the denominator published above **itself overlaps** (`GB08-F3`).
>
> Mechanical prefix testing of the 22 roots returns **three containment relations**:
> `ODOO-COMMUNITY/Odoo18/t8master` (2,636 modules) **contains** `…/smeplus-server` (1,304), which
> **contains** `…/smeplus-server/odoo` (637) and `…/smeplus-server/odoo_old` (28).
>
> **`23,530` is therefore not a count of distinct modules.** The disjoint total is
> `23,530 − 1,304 − 637 − 28 = 21,561` over **19 disjoint roots**. The `1,753` figure and the naive
> `23,530` sum are both **reproduced exactly**; it is the `UNIT` that was not tested for disjointness.
> **`% Board` / `% STATE` / `% STEP` remain `NOT CALCULABLE`, and this amendment strengthens rather than
> weakens that finding.**

---

## 6. Gate recommendation

> # `RECOMMEND HOLD`

**Recommendation only. Boss is the sole Final Approver.**

### Why not `PASS`
`MC-03` and `MC-10` fail without qualification. This round returned **4 new material findings and 3
claim corrections on first independent contact** with a package that had already passed five rounds.
**Three consecutive rounds have done so and the rate is not decaying.**

### Why not `CONDITIONAL PASS`
**Unavailable by rule, not by judgement.** The standard and the standing Boss instruction forbid using
it to bypass an unresolved tolerance-zero boundary. **Twelve stand unresolved.** The conditions would
*be* the tolerance-zero items — a `PASS` with a different label.

### Why not `FAIL`
**No veto was issued on the Wave A research.** The positive ground is stated rather than inferred from
absence — the inference `DR-NC-01` prohibits:
- The **semantic model has survived seven adversarial rounds on evidence** and every finding has
  sharpened the direction already chosen, not reversed it.
- **`MC-04` Repeatability reached `MET`** — this round reproduced the parent's own denominator **to the
  digit** on the parent's own root, and reproduced 5 of 6 re-tested findings exactly.
- The one veto in play (`AASR-VETO-01`) is against a **sibling design package's worklist**, not against
  Wave A research.
- **Zero new tolerance-zero boundaries were opened** — the first round with none.

### What the hold is on
**Not the semantic model, and not the evidence.** The hold is on **scope declaration**: the method
executes well and reproduces, and it has never declared the universe it executes over.

---

## 7. For Boss attention

1. **The programme has never declared which of 22 reference roots it is researching**, and the Wave A
   rate research ran against a root where the branch-preference behaviour is **absent** while the root
   named `18.0.3_smeplus` has it **present**. **Closing this is hours of mechanical work and it
   re-scopes `GB-07`, `GB-08`, `MCU-18`, `MCU-19b` and every class `A` absence at once.**
2. **`GB-08` needs a decision before any Wave A conclusion is safe downstream** — and before Wave B can
   design foreign-currency AR at all.
3. **`MCU-04` is closed as a `VERIFIED DEFECT`**, and the reason it sat open for two gate reports is a
   **disposition rule**, not missing evidence: a determined mechanism was held open because its
   *consequence* is policy-dependent. **That is a systematic error worth a rule** (`ER-CORE-11`).
4. **`MCC_00` — the register built to end correction-propagation failure — is itself inconsistent**
   (`FC-F1`): it closes ten ids and counts nine. **It requires a Boss-visible correction.** Three
   published figures are affected.
5. **`T0-12` remains the most severe open item in Wave A**: the debit = credit assertion is suppressible
   by context, `unbalanced-and-posted` is reachable, the taxonomy has no cell for it, and **the bucket
   of 48 suppression tokens has still never been opened.**
6. **`unbalanced-and-posted` and the 48-token bucket must not be routed to Wave B.** They are Wave A
   residuals and the routing-abuse rule applies.
7. **Push permission is the only thing standing between this package and verified publication.** The
   dry-run succeeded; the write is blocked by the executing harness. **One command, listed in §3.**

---

## 8. Wave B readiness

> # `NOT READY — EXACT DEPENDENCIES`

**Wave B *research* is fully prepared and could open on Boss authority.**
**Wave B *design* cannot open.** Exact dependencies:

| # | Dependency | Why hard |
|---|---|---|
| `D1` | **`MCU-21`** — root set undeclared | Blocks everything behavioural, and blocks every class `A` claim |
| `D2` | **`GB-08`** — rate-resolution semantic | Blocks all foreign-currency AR |
| `D3` | **`T0-12`** — balance assertion suppressible | Wave B may not assume a posted AR entry is balanced |
| `D4` | **`GB-01`** — tenant/company crossing | Blocks customer scoping and AR ageing per company |
| `D5` | **`T0-08`** — entry identity | Blocks invoice numbering and duplicate detection |
| `D7` | **`T0-05`** — over-reconciliation | Blocks cash application |

**`D1` is first and cheapest, and it unblocks `D2`.**

Deliverables prepared: `ACCOUNT_WAVE_B_READINESS_PACKAGE.md` and
`ACCOUNT_WAVE_B_NEW_SESSION_PROMPT_DRAFT.md` — the latter marked
**`DRAFT / NOT AUTHORIZED TO EXECUTE`** and carrying a mandatory precondition check as its §0.

---

## 9. `GB-08` status — **added `2026-09-04`**

> # `BOSS DECISION REQUIRED — GB-08`
> # `GB-08 DECISION PACKAGE READY FOR BOSS`

| Dimension | Status |
|---|---|
| Decision package | **COMPLETE** — `GB08_DECISION/`, 5 documents + 1 re-runnable evidence script + manifest |
| Options | **Located in the parent package** (`FINAL_CLOSURE/ACCOUNT_WAVE_A_GB08_BOSS_DECISION_PACKAGE.md §10, lines 275–315`), **reconciled**, and carried on **two axes** — freeze scope `A`–`D` and rate-ownership semantic `S1`–`S4` — with the crossing matrix |
| Recommendation | **`RECOMMEND BOSS BUSINESS RULING BEFORE RESEARCH CAN CONTINUE`** — separate document, and it selects no option |
| Roots searched for the rate chain | **22 of 22**, mechanically, from a declared pattern; re-runnable in one command |
| Parent `GB-08` claims re-tested | **12** — **6 reproduced exactly, 6 corrected, 0 unverifiable** |
| Blocker count | **Unchanged at 8** (`GB-01`…`GB-08`). This round does **not** close `GB-08` |
| Gate recommendation | **Unchanged — `RECOMMEND HOLD`** |

### The six corrections to the `GB-08` package

| # | Parent claim | Correction |
|---|---|---|
| `GB08-C1` | `Δ1` *"narrows resolution to the acting branch"* | **It does not.** `_get_rates` scopes by `company.root_id`, and `branch.root_id == root.root_id`. The domain is identical with and without `Δ1` (`GB08-F1`) |
| `GB08-C4` | Functional amounts *"differ between V18-B and v19"* | **Not on the verified path.** The two `_get_conversion_rate` bodies are byte-identical apart from the inert `Δ1` hunk |
| `GB08-C2` | The par fallback is a `Δ3` (v19) property | **`COALESCE(…, 1.0)` is in `_get_rates` in all four variants** — it is on the **stable** axis |
| `GB08-C5` | *"Freeze to v18"* avoids `Δ3`'s par fallback | **It does not.** v18 has the same fallback, and the oldest variant reaches it through raw SQL with no record rule |
| `GB08-C3` | *"No record rule is applied to `res.currency.rate`"* | **A rule exists and is stable** (`base_security.xml:62–66`); it is `Δ3` that does not apply it |
| `GB08-C6` | *"1,753 of 23,530 modules"* | **Arithmetic reproduced exactly; the denominator overlaps** — see the §5 amendment |

### The five findings that now carry `GB-08`

| # | Finding |
|---|---|
| `GB08-F1` | `Δ1` does not change which rate row is selected — **there is no v18-vs-v19 branch-rate divergence to decide between** |
| `GB08-F5` | The fallback is **three-tier**, and tier 2 is a **future** rate; tier 3 is **par**. Stable in every variant. The reference implementation **never fails on a missing rate** |
| `GB08-F6` | Precedence is **ownership first, recency second** — a stale owned rate beats a current global one. Stable in both resolvers |
| `GB08-F7` | A **branch-scoped rate row is write-visible dead data**: creatable, rule-visible, displayable, and **never selected**. Stable in every variant |
| `GB08-F8` | A **cross-tenant write→read path**: nullable `company_id` + a global rule admitting `company_id = False` + `group_account_manager` `1,1,1,1`. Stable in v18 and v19. This is `GB-03`'s axis, verified at the rule and ACL level |

### What Boss is asked to rule

| # | Ruling | Type |
|---|---|---|
| `R1` | **May a branch or operating unit hold, and be valued at, its own exchange rate?** | Business ruling |
| `R2` | **When no applicable rate exists, does SMEsPlus block the posting, or substitute a value?** | Business ruling with an accounting consequence |
| `R3` | *(only if `S3` is in contemplation)* Is an unowned, database-wide rate row legal? | Gated by `GB-03` and `T0-04` — **cannot be settled inside `GB-08`** |

**And one programme declaration, which is not a Boss decision:** *which build does SMEsPlus ship?*
`GB08-F10` shows it cannot be read from a directory name — `CLAUDE AI/MIGRATION/ODOO18/enterprise` is a
**v19** tree.

---

## 10. Terminal state

> ## `ACCOUNT WAVE A — HOLD WITH EXACT REMAINING BLOCKERS`
> ## `WAVE B READINESS PREPARED — NOT READY TO OPEN`
> ## `GITHUB EVIDENCE PUBLICATION VERIFIED` *(amended `2026-09-04`)*
> ## `JIRA EVIDENCE PUBLICATION VERIFIED` *(amended `2026-09-04`)*
> ## `GB-08 DECISION PACKAGE READY FOR BOSS` *(added `2026-09-04`)*

**Not declared:** converged · final approved · Wave A closed · any gate movement · any implementation
authorisation · Team B or Team C hand-off · the Very Deep standard as canonical · session complete.

**Wave B has not started.** No source code was modified. Nothing was merged. Nothing was deployed.
No Jira status was changed. No `PASS`, approval or certification is declared anywhere in this package.

**Amendment scope.** The `2026-09-04` `GB-08` amendment changed **publication status**, **one
denominator**, and **added `GB-08` status**. It did **not** change the gate recommendation, the blocker
count, the tolerance-zero count, the method-convergence result, or the Wave B readiness state.
