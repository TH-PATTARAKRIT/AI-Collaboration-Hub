# P11 — AAS-03 CORR3 CHALLENGE

`[SMEPLUS-26-09-06-ACC-P11-CORR3-ACCOUNTING-INTAKE-INTEGRITY-001]` · `CP-P11C3-09` · **PHASE S**

> Package frozen at **`9356557`** before commissioning; **no edit to the reviewed surface until all
> four returned.** Four experts, bounded to P11 + the frozen peer artefacts, read-only, no contact.
> **Every material finding below was re-verified by P11 at source before acceptance.**

---

## 1. Verdict

> ## `CONTRADICTED — THE INSTRUMENT IS NOT CERTIFIABLE, AND THE ROUND CERTIFIED IT`
>
> CORR3 was ordered to repair intake integrity **first**. It built a better instrument, **certified it
> on controls that could not fail, and did not publish it.** The numbers were right; the certification
> was not.

**Findings: 52. Accepted: 48. Disputed in part: 4.**

## 2. The finding that subsumes the round — `S06`

> **`S06_P09_NEGATIVE_CLAIM_CONTROL_STANDARD.md` is returned by none of `D1`, `D2`, `D3`. Union hit: 0.**
>
> **P11's own error log, line 955, names it:** *"it lost `D26`, `D27`, **`S06`**, `S22`, `D24` of P09"*.
> The certification premise at §3.4 was *"every artefact CORR2 was shown to have missed must return"*.
> **P11 listed twelve and tested ten, and the two it dropped include the one that fails.**
> Re-run on the full twelve: **11 pass, `S06` fails.**
>
> **And `S06` contains the rule the instrument breaks.** Line 21, issued *"for adoption across all
> SMEsPlus Deep Research processes"*:
>
> > **`NC-8` — "No `head`, `tail`, sampling, `limit`, or first-N command may bound a population."**
>
> **`D3` is a `tail`, and it bounds P11's denominator.** The artefact the instrument cannot see
> carries the standard the instrument violates. `P11-E-42`.

## 3. `CRITICAL` — verified at source

| # | Finding | Verified |
|---|---|---|
| `X1-1`/`X3-C3` | **`P11-C-15`'s independence is FALSE — `P11-C-09` repeated in the round that corrected it.** `P10_G02_SOURCE_LINK_REGISTER` L14: *"**P02 authoritative closure `7cb1c27`** … **Consumed as controlled input**"*; L24 files the invariant finding as **admitted P02 evidence**; `P10_TO_P11_HANDOFF` L55 **credits the correction/reversal location to P02**. P11 relayed P10's word *"independently"* without testing it, and **did not open P10 this round** | ✔ verbatim |
| `X1-1b` | **The inversion.** P10 marks `G02-E-C` (design candidates) *"reached independently"* and attaches **no** independence claim to `G02-E-D` (the invariant). **P11 demoted the independent item and promoted the relayed one** | ✔ |
| `X2-C7`/`X4-C3` | **`D3`'s "last 5" is LEXICAL — the semantic warrant is unestablished.** `git ls-tree` carries no timestamps. P01's `P`-series returns `S,V,V,V,W,W` — the alphabet — labelled `CURRENT-CRITICAL`. **The defect that got attempt 1 rejected survives into attempt 4: P11 changed the partition and never the order** | ✔ executed |
| `X2-C15` | **The `PEER\|basename` key discards generations.** `P09_CHECKPOINT_REGISTER.md` exists at **5** paths, `P09_AUTO_RESUME_STATE.md` at **5**; the **directory is the only generation discriminator** (`…_2026_09_05` vs `…_2026_09_06`). **10 paths → 2 keys** — the exact supersession failure `P11-G-07` exists to prevent | ✔ (worse than reported: 5, not 4/3) |
| `X2-C1`/`X4-C2` | **The instrument was unreproducible.** *"Series"* was never defined; four experts tried eight readings and none returned 155. **Now published and re-executed: `D1=55 · D2=48 · D3=155 · UNION=212 · 19/36/29` reproduce exactly.** The numbers were right; **for a round whose thesis is *prove the instrument could have failed*, the instrument was the one thing not in evidence** | ✔ published, reproduces |
| `X4-C4` | **`B-33` receives the absolute it was written to prevent.** `IC-01`'s accrual control (*0 of 15,522*) is sourced **from a deployed series-18 database**, while `B-33` registers `CRITICAL` that *"no deployed database runs 18.0"*. Both in one commit | ✔ |
| `X4-C5` | **`B-33` registered, not applied.** The 18.0 qualifier reaches **2** rows (`T0-15`, `P11-C-12`); **nine** P08-sourced rows are published unqualified, including `T0-16`, `B-34` and `B-21`'s *"all three deployed databases"* | ✔ |
| `X3-C2` | **The artefact that falsifies `B-31` is outside the union.** `23_P10_PEER_INTAKE_REGISTER.md` is in **none** of D1/D2/D3 — and misses for exactly the reason P11 diagnosed for `D26` | ✔ union=0 |

## 4. `HIGH` — accepted

| # | Finding | Verified |
|---|---|---|
| `X1-3`/`X3-C1`/`X4-C6` | **`B-31` is falsified.** `23_P10_PEER_INTAKE_REGISTER` records receipt of **four P11-origin items** with a verification column and a **reasoned refusal** (`RF-02`); `P06_AUTO_RESUME_STATE` L16-17 is a working receipt record. **And `AASP-VETO-06` — *"a handoff is not delivered by being written"* — is a standing P06 veto absent from P11's tree.** P11 cited the weaker `REV-E-23` because the stronger is in its blind zone | ✔ |
| — | **`B-31` breaks P11's own §5 rule** — a universal absence claim resting on the denominator P11 certified as *not certified for absence*, three files earlier | ✔ |
| `X1-2` | **`P06` answered the `exercised` question two rows below the line P11 quoted.** `70_` L27: *"Execution having occurred \| **`SUPPORTED INTERPRETATION`** — first-party remediation module, not a log."* P11 wrote *"exercised NOT ESTABLISHED"* three times, **routed the answered question to P06 as an open ask, then counted its non-delivery as evidence for `B-31`** | ✔ |
| `X2-C2`/`X4-R3` | **Substring contamination.** `P04` ⊂ `STEP0401`; **26 files** under P04 alone. State-02 migration artefacts from 2026-07 entered the *"owner's current accounting statement"* register | ✔ |
| `X2-C6` | **§3.2, titled *"executed, not declared"*, is `UNION − |Di|` in all three rows — a tautology that cannot fail** | ✔ |
| `X2-C8`/`X4-R1` | **`TAIL=5` is fitted.** `D26` sits at **−2**, so `TAIL=2` would pass. The 10-member control returns **10/10 at TAIL 2,3,4,5** while D3 moves **117→207** | ✔ |
| `X3-R2`/`X4-R3` | **The failure control is vacuous** — its subject is not in the scanned population. **The identical defect CORR2 condemned as `X2-R1`, restated and certified on** | ✔ |
| `X2-C3` | **`ADDRESSED` is 84, not 77** — contradicted by §3.1's own three cells (55+48−19) | ✔ executed |
| `X2-C4` | **`191` carries two mutually exclusive definitions**; §5's single exclusion reason (*"not P11-addressed"*) is **false for 63 artefacts by P11's own instrument** | ✔ |
| `X2-C5` | **`OPENED = 21` is cited to a file naming 9** | ✔ |
| `X3-C4` | **`19_P07_CORE_RECON_HANDOFF_PACK.md` is inside the union and inside `ADDRESSED`, never opened.** Title: *"CORE ACCOUNTING RECONCILIATION HANDOFF PACK"*. **P11 has never opened P07 at any SHA across three rounds** | ✔ |
| `X4-C8` | **`P11_AUTO_RESUME_STATE.md` at the frozen SHA still says *"DO NOT RE-RESOLVE"* over the CORR2 heads** (`P06 1b018c1 · P08 00ccd66 · P09 4778792`) and reports 40 errors against 41. **A successor obeying P11's own control artefact rebuilds on superseded heads** | ✔ |
| `X4-M-8` | **`P09_..._L1_L8_FINAL_BOUNDED_CORRECTION_NEXT_PROMPT` is inside `D1`, unopened** — and at that head **P09 declares its own package internally contradictory and under open correction** (*"P09 carried a fact and its negation in the same package"*), with `AAS+-VETO-04` **NOT DISCHARGED**. P11 dispositioned P09 as `CONSUMED` without it | accepted |
| `X3-C5` | **`P08-HO-14` and `P07-F-02`/`F-03` are mutually contradictory** at two SHAs P11 declared, with **no contradiction registered** — and they may be true of **different generations** | accepted |
| `X1-4`/`X2-C10` | **The falsification pass was published; the registers it falsifies were not touched.** `9356557` = 7 files, **0 deletions**. The matrix still asserts the withdrawn chronology, the un-noted `447,384`, and *"the largest unrecognised position"* — as `FACT VERIFIED` | ✔ |
| `X2-C11`/`X4-C9` | **The falsification tally covers 7 of 10** (`5+1+1`), and **undercounts P11's own self-correction by 2** | ✔ |

## 5. Disputed — in part

| # | Expert position | P11's position |
|---|---|---|
| `X2-C1` *(wrong)* | `D3=155` / `UNION=212` are **wrong**; executed 212/268 | **Disputed.** The published code reproduces **155/212/19/36/29 exactly**. The expert reconstructed from prose because the regex was unpublished. **The defect is unreproducibility, not error** — and it was P11's defect to create |
| `X1-5` | `IC-01` is an **over-correction**; P11 is now under-claiming | **Accepted in substance, disputed in framing.** The owner routes judgement to `P08` and the decision to Boss — it does **not** remove the position from P11's carriage. **`B-28` is re-instated as a carried candidate at `฿27,490,865.80` / 1,411 receipted lines**, with `฿1,538,601.86` carved out. **Carrying is not promoting and is not deciding** |
| `X3-C6` | `F-01` over-corrects — P08 did not withdraw the settlement graph | **Accepted.** P08 uses *"WITHDRAWN"* precisely elsewhere and does not here. `F-01` re-stated: **a consequence stated against the claim, not an owner withdrawal** |
| `X1-9`/`X3-C7` | `F-07` missed the strongest counterexample to `P11-C-12` — P03's **25 of 25** subsidiary-vs-GL divergence, already in P11's own matrix | **Accepted.** A measured divergence on a genuinely separate store, immune to the *"true by construction"* defence. `F-07` under-corrected **by omitting evidence P11 already held** |

## 6. What survives

| Survives | Basis |
|---|---|
| **The peer snapshot** — 10/10 file counts exact, all SHAs terminal | verified by 3 experts independently |
| **`D1`=55, `D2`=48, and the union/intersection test 19/36/29** | reproduced exactly by **three** experts working separately |
| **The `D26` diagnosis and `P11-G-07`** | *"sound"* (E4-S5); terminal-member-only genuinely loses `D26` |
| **The five P08 corrections, carried faithfully and against P11's own interest** | verified verbatim by E2 and E3 |
| **The falsification pass's substance** | 6 of P11's own claims disproved from owners' current statements |
| **No statutory determination anywhere** | E3 checked explicitly: *"No smuggling found"* |
| **Domain purity** | no peer internal, database, module or source tree opened |

**`CP-P11C3-09` — COMPLETE — `CONTRADICTED`.**
