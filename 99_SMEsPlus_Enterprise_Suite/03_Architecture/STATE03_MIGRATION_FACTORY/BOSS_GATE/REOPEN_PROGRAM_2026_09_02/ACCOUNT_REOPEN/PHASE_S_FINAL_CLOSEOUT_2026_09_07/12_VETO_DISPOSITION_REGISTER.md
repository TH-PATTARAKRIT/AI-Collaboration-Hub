# 12_VETO_DISPOSITION_REGISTER

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-FINAL-CLOSEOUT-001]`
**Authoritative source population** `06_VETO_AND_BOSS_DECISION_DEPENDENCY_REGISTER.md` @
`audit/account-xrecon-2026-09-06-001` `3291210` — **17 named, 0 discharged**

> **`CLOSED` is not used as a synonym for `DISCHARGED`.** Allowed dispositions only:
> `DISCHARGED BY VERIFIED EVIDENCE` · `PARTIALLY SATISFIED — REMAINS OPEN` · `UPHELD` ·
> `SUPERSEDED WITH LINEAGE` · `ROUTED` · `BOSS DECISION REQUIRED`.

## 1. Result: **0 of 17 discharged. 17 remain standing.**

**No veto was discharged by this session, and none could have been.** Every veto whose lifting condition
requires independent proof is blocked behind an RC that no eligible party has run — and this session is
disqualified from every RC lane by `PHASE-S/Q-BOSS-02` (`10_` §1).

## 2. Disposition, one row per veto

| Veto | Owner | Original lifting condition | Corrected evidence | Independent RC evidence | Cross-package dependency | **Disposition** | May be discharged by |
|---|---|---|---|---|---|---|---|
| `AASP-VETO-07` | P06 | *"an independent verifier that completes this prompt"* — expressly **not** the P06 IEV actor; 3 independent sufficient grounds | `Q-P06-01` @ `692ea27`; `Q-P06-03`/`-04` @ `b5f5a21` | **NONE** — `RC-03`/`RC-04` not run | `XRD-009` | **UPHELD** | independent verifier, not the P06 IEV actor, not this session |
| `AASP-VETO-06` | P06 | owner + independent evidence; engaged by `XRD-006` | partial via `Q-P06-03` | **NONE** | — | **PARTIALLY SATISFIED — REMAINS OPEN** | owner + independent verifier |
| `AASP-VETO-04` | P06 | carried into CORR4 by P11 §6 | none this round | **NONE** | P11 §6 | **UPHELD** | owner + independent verifier |
| `AAS+-VETO-01` (inherited) | P08 | **0 of 2** conditions met | none this round | **NONE** | blocks P11 `B-29` via `C-1` | **UPHELD** | P08 owner + independent evidence |
| `AAS+-PS-VETO-01` | P08 | **0 of 6**; **`C-6` open on two independent grounds** | `Q-P08-01`/`-02` @ `c7cfd8a` | **NONE** — `RC-05` on HOLD | `XRD-009` — partly reserved to Boss | **UPHELD; `C-6` is BOSS DECISION REQUIRED** | Boss for `C-6`; independent verifier for the rest |
| 4 vetoes from the audited round | P08 | **0 of 25 evidenced** | none this round | **NONE** | — | **UPHELD** | P08 owner + independent evidence |
| 4 vetoes from the verification | P08 | 41 conditions | none this round | **NONE** | — | **UPHELD** | independent verifier |
| `AAS+-VETO-04` | P09 | `K-2` surface complete **and re-tested** | `Q-P09-01` resolves `M-1` @ `2079a25`; `Q-P09-02` scope published, correctly not self-run | **NONE** — `RC-01` ready, not run | blocked by `M-1` + `M-2`; consumed by P11 `B-38` | **PARTIALLY SATISFIED — REMAINS OPEN** (`M-1` resolved, `M-2` open) | independent verifier via `RC-01` |
| `AAS+-VETO-01` | P09 | — | none | **NONE** | — | **UPHELD, unchanged** | — |
| `AAS+-VETO-02` | P09 | — | none | **NONE** | — | **UPHELD, unchanged** | — |
| `AAS+-VETO-03` | P09 | — | none | **NONE** | — | **UPHELD, unchanged** | — |
| `AASP-P11-C3-VETO-01` | P11 | **6 lift conditions** | none this round | **NONE** | — | **UPHELD** | independent verifier |
| `AASP-P11-C3-VETO-02` | P11 | implementation | — | **NONE** | Phase SA+ | **UPHELD** | not reachable in Phase S |
| `AASP-P11-C3-VETO-03` | P11 | *no count without `E6`* | — | **NONE** | **engaged by `CO-F-01`** — the CORR3 denominator is non-deterministic | **UPHELD, AND NEWLY REINFORCED** | independent verifier |
| `AASP-P11-C3-VETO-04` | P11 | *no control set drawn by the party it controls* | — | **NONE** | **binds all six fresh challenges** | **UPHELD** | independent verifier only; **P11 may not self-discharge** |
| `P10 AASP-VETO-01` r3 | P10 | inherited by P11 §6 | — | **NONE** | P10 not opened | **UPHELD** | P10 owner; out of Phase S scope |
| `AAS+-PS-VETO-01 C-6` *(tracked separately per `03_`)* | P08 | structural independence of the verification | — | **NONE** | `XRD-009` = **NOT SATISFIED** | **BOSS DECISION REQUIRED** | **Boss only** |

## 3. Vetoes on which this session produced *new* material

| Veto | What changed | Effect on disposition |
|---|---|---|
| `AASP-P11-C3-VETO-03` — *no count without `E6`* | `CO-F-01` establishes that P11's CORR3 intake denominator is computed against **floating branch heads**, returns a different value on every run (212 / 214 / **216**), and that its published `D1`/`D2`/`D1∩D2` are each wrong by one | **The veto is reinforced, not weakened.** A count that changes when an unrelated peer commits is exactly what this veto exists to prevent. **No discharge; the standing case is stronger** |
| `AAS+-VETO-04` (P09) | `M-1` is resolved on the frozen surface; `M-2` remains, and `RC-01` is now **evidence-unblocked** (inputs confirmed present, `10_` §4) | Moves from *fully blocked* to **PARTIALLY SATISFIED — REMAINS OPEN.** **This is not a partial discharge**; the lifting condition is conjunctive and `M-2` is unmet |
| `AASP-VETO-07` (P06) | The IV's stated blockers for `RC-03`/`RC-04` are cleared — 25-vs-26 adjudicated at **26**, and the `RC-04` surface **exists** contrary to the IV report | **Disposition unchanged: UPHELD.** Only the *path* to a challenge is unblocked. **Clearing an obstacle to a challenge is not the challenge** |

## 4. The rule this register enforces against itself

**No owner may self-discharge a veto whose lifting condition requires independent proof.**
`AASP-VETO-07`, `AAS+-PS-VETO-01` `C-6`, `AAS+-VETO-04` and `AASP-P11-C3-VETO-04` all carry that property,
and **this session — being the same model that authored the repairs — is an owner for this purpose, not
an independent party.** Its findings in `09_`–`11_` are offered to the verifier as leads and are **not
evidence toward any discharge.**
