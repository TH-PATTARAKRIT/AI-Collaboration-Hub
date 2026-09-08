# ACCOUNT_FINAL_OWNER_SHA_REGISTER.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` · deliverable **2 of 12**
**Prompt commit:** `a06f5d9c69e020bf8e7749108b892b73c6b31e62` on `control/account-one-prompt-final-closure-2026-09-08-001`
**Boss non-degradation ruling:** `63c76e4b0c9e8331a365ddb922667b269960c10e`
**Repository:** `TH-PATTARAKRIT/AI-Collaboration-Hub`
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. The four final Account owner SHAs

| Owner | Branch | **FINAL IMMUTABLE SHA** | Baseline it started from | Commits |
|---|---|---|---|---|
| **P06** Bank-to-Reconcile | `corr/p06-one-prompt-final-2026-09-08-001` | **`a533fe92d6f6855e0b362179403476520cc9aafa`** | `b5f5a211763568a4212d08954c835412f7728a0a` | 1 |
| **P08** Record-to-Report | `corr/p08-one-prompt-final-2026-09-08-001` | **`ca577be42e6ba9535e1911dc0bad1dfab74a8aa8`** | `e368d11da6f7e4973469ff5608d676ec2d13811c` | 4 |
| **P09** Plan-to-Analyze | `corr/p09-one-prompt-final-2026-09-08-001` | **`ab8c0131c46e8154ad7efae18de2a54af2f17362`** | `2079a2594a6a76eb91bdb528f22eaf928d42c0d6` | 1 |
| **P11** Core Reconciliation | `corr/p11-one-prompt-final-2026-09-08-001` | **`490ccdd81a4fed79d36b7b9d3bbc25deedd597b4`** | `9d4ecdc744fbbb0e502a0b907f59c301bdf7812c` | 4 |
| **P07** Thailand Tax | `research/account-p07-th-tax-compliance-2026-09-04-001` | `ee2be30ebf155e241510b3c7133c69419eb060a0` | — | **0 — READ-ONLY, NOT MUTATED** |

**Every branch is created from the exact baseline the prompt declares. No branch was merged. Boss decides.**

## 2. P08's commit chain — the prediction-before-result lineage `RC05-F3` demanded

| # | SHA | Time | Contents |
|---|---|---|---|
| 1 | `78f537876852ea6f20047524555fd89e90ee4c78` | `2026-09-08T17:04:08+07:00` | **prediction + two instruments only. Zero run output.** |
| 2 | `f0cf287ac9f4ad37b0c19145df4a0e396af84c13` | `2026-09-08T17:16:03+07:00` | run results, scored against the prediction |
| 3 | `82df5f3df8faec484a27146eb1f1d8b652424293` | — | cross-package delta: `54_`/`43_`, four-input install-state refresh, clean-room scrub |
| 4 | **`ca577be42e6ba9535e1911dc0bad1dfab74a8aa8`** | — | third `P08-CONTRA-55` carrier; three-extract boundary declared |

**Checkable without trusting this file:**
```
git show --stat 78f5378                                  # prediction only, no results
git merge-base --is-ancestor 78f5378 ca577be             # exit 0
git log --format='%H %cI' 78f5378..ca577be               # results strictly later
```

## 3. Peer pin currency — what each package points at, at its own final SHA

| Consumer | Pins P06 | Pins P07 | Pins P08 | Pins P09 |
|---|---|---|---|---|
| **P11** | `a533fe9` **current** | `ee2be30` **current, read-only** | `ca577be` **current** | `ab8c013` **current** |

**P08 moved three times after P11's first consumption.** Every move was re-pinned and the delta measured, **not swapped silently**:

| P11 re-pin | Intake UNION | Claim consumed by P11 that moved |
|---|---|---|
| CORR3 pins | 817 | — |
| first final pins | 825 (+8, −0) | balance premise; deletion-path install state |
| P08 `ca577be` | **825 (unchanged)** | **none** — a third carrier of an already-consumed claim, plus a declared boundary |

**The re-pin at `ca577be` moved no claim, and was applied anyway.** A pin that happens to be right is not a control.

## 3.1 The closing sweep moved two SHAs after the deliverables were first drafted

**A mechanical vendor-token count delta against each baseline — run as the last act, not the first — found a clean-room leak in P08 and another in P11**, each made by this prompt's own corrections, each a Layer 2 measurement transcribed into a Layer 1 handoff surface. **P11's sweep also found a compiled `.pyc` that the instrument's own execution had committed into the evidence package.**

| Package | Before the sweep | **After** |
|---|---|---|
| P08 | `f0cf287` → `82df5f3` | **`ca577be`** |
| P11 | `ed7ec37` → `3cee38f` → `79e1369` | **`490ccdd`** |

**Both leaks were found by counting, and by nothing else.** No challenge had run, and neither would have been visible to a reader: the leaked text is *correct* — it names the right tool and the right version — **on the wrong surface.**

## 4. Superseded heads — retained as lineage, must NOT be resolved against

`P06 1b018c1 · 5212756 · b5f5a21 · 692ea27` · `P08 00ccd66 · e368d11 · 4bdf8a2 · c7cfd8a · 3ea9195 · d685176` · `P09 4778792 · 5441f8d · 2079a25 · ec4d3d2` · `P11 9d4ecdc · 002748d · dc4cc4a`

**`92de8a1` is a PROMPT commit and is non-substantive under `P11-G-10`.** P11's rebuilt instrument fails closed on it, and that is one of its four controls.

## 5. What this register does NOT assert

- **No branch is merged, approved, frozen or released.** These are audit branches; `SMEsPlus` is stale by design.
- **No SHA here constitutes a PASS.** Each is the immutable address of an owner's work, nothing more.
- **P07 was not touched at any SHA on any branch.**
