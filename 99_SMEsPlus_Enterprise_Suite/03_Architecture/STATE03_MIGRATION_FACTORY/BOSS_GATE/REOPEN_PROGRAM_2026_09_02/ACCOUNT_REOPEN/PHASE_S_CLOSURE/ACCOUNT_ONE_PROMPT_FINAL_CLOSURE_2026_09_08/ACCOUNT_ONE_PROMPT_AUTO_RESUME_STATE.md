# ACCOUNT_ONE_PROMPT_AUTO_RESUME_STATE.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` · deliverable **12 of 12**
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. STATE

```
TERMINAL A — ACCOUNT PHASE S OWNER CLOSURE COMPLETE —
READY FOR ONE FINAL INDEPENDENT GATE + PHASE SA HANDOFF

EVENT-DRIVEN. NOT WAITING IDLE. NOT STOPPED FOR A ROUTINE QUESTION.
```

**This prompt is complete. It is the ONE and ONLY Account execution prompt, and it did not create another.**

## 2. FINAL OWNER SHAs — resolve against these, not against anything earlier

| Owner | Branch | **SHA** |
|---|---|---|
| P06 | `corr/p06-one-prompt-final-2026-09-08-001` | `a533fe92d6f6855e0b362179403476520cc9aafa` |
| P08 | `corr/p08-one-prompt-final-2026-09-08-001` | `ca577be42e6ba9535e1911dc0bad1dfab74a8aa8` |
| P09 | `corr/p09-one-prompt-final-2026-09-08-001` | `ab8c0131c46e8154ad7efae18de2a54af2f17362` |
| P11 | `corr/p11-one-prompt-final-2026-09-08-001` | `79e1369156ca052ad77c8f589842f5e99b25f800` |
| P07 | `research/account-p07-th-tax-compliance-2026-09-04-001` | `ee2be30ebf155e241510b3c7133c69419eb060a0` **READ-ONLY** |
| Account deliverables | `audit/account-one-prompt-final-closure-2026-09-08-001` | this branch |

**Superseded — do NOT resolve against:** `P06 1b018c1 · 5212756 · b5f5a21 · 692ea27` · `P08 00ccd66 · e368d11 · 4bdf8a2 · c7cfd8a · f0cf287 · 82df5f3` · `P09 4778792 · 5441f8d · 2079a25 · ec4d3d2` · `P11 9d4ecdc · 002748d · dc4cc4a · ed7ec37 · 3cee38f`.
**`92de8a1` is a PROMPT commit — non-substantive under `P11-G-10`.**

## 3. NEXT EXACT ACTION — and it is NOT an Account owner action

> ### **ONE final external independent gate.** Nothing else.

| # | The gate's exact scope | Owner |
|---|---|---|
| 1 | fresh `RC-04` delta — P06's changed validation surface | external |
| 2 | fresh `RC-01` delta — P09's four corrected surfaces | external |
| 3 | fresh `RC-05` delta — P08's changed population/namespace/provenance surfaces **and independent re-execution of the newly published run** | external |
| 4 | fresh `RC-06` delta — P11's propagation | external |
| 5 | **`B-35` certification on the full twelve-control set including `S06`** | external — **the certifier must not be the author** |
| 6 | whether `B-37`'s repair closes it | external |
| 7 | whether `AASP-VETO-06`'s delivery limb is satisfied now that P11 recorded receipt | external |

**`RC-02` and `RC-03` are NOT reopened** — no correction in this prompt changed their validated surfaces.

**Then:** Boss decides `BD-ACC-01`…`BD-ACC-04`. **`BD-ACC-03` needs no gate — it is a policy decision and can be taken at any time.**

## 4. WHAT A SUCCESSOR MUST NOT DO

- **Do not create another Account execution prompt.** Boss authorised **one** and it has run.
- **Do not re-run the owner corrections.** They are published at immutable SHAs.
- **Do not treat this session's internal adversarial QA as independent.** It is not, and it is nowhere labelled as such.
- **Do not discharge a Veto.** Zero are discharged; **12 are recommended PRESERVE**; one is `NOT MATERIAL TO PHASE SA HANDOFF`.
- **Do not resolve peer trees against superseded heads.** §2 above is the current table.
- **Do not mutate P07.**
- **Do not read `AAS+-VETO-01` unqualified.** It has **two meanings** — `P08/AAS+-VETO-01` and `P09/AAS+-VETO-01`. See `BD-ACC-04`.

## 5. OPEN — carried, with owner

| Item | State | Owner |
|---|---|---|
| `B-35` intake instrument certification | **CRITICAL — OPEN.** Rebuilt and internally QA'd; **not certified** | external gate |
| `B-27` | OPEN — gated on a certified `B-35` | external gate |
| `B-37` | OPEN — **defect repaired and evidenced**; closure reserved | external gate |
| `B-38` / `AAS+-VETO-04` | OPEN — **`M-1` resolved, `M-2` not** | external gate |
| `BD-ACC-01` event identity | OPEN | **Boss** |
| `BD-ACC-02` cross-company tax grouping | OPEN | **Boss** |
| `BD-ACC-03` valuation method | OPEN | **Boss** |
| `BD-ACC-04` veto identifier collision | OPEN — **interim: producer-qualified citation** | **Boss** |
| `P08-F-NEW-01` custom access-rights module installed in one extract only | OPEN — **received, not adjudicated** | **Boss** |
| P11 terminal state | **`TERMINAL B` — intake integrity NOT established** | unchanged |

## 6. NOT BLOCKING — the point of this session

**Nine of eleven Account interfaces are `ACCOUNT-HANDOFF-READY-WITH-DELTA` and usable now.** Two are `EXTERNAL-DECISION-PENDING`, on `BD-ACC-02` and `BD-ACC-03` — **decisions, not research.**

> **No other module should wait for Account.** Account's remaining work is a gate and four Boss decisions. **The interface semantics the rest of the programme needs are published, classified, and each unresolved attribute is named with an owner and a smallest next action.**

## 7. ENVIRONMENT — for the record

Everything ran on the existing authorised environment: the local host, the repository, and already-installed tooling. **No paid API, no PAYG, no API key, no purchased service, no additional credits.** Where one tool failed — a regex engine rejecting a pattern, an older restore client refusing an archive — **another already-authorised mechanism was used and the failure was published**, never converted into a reason to stop.
