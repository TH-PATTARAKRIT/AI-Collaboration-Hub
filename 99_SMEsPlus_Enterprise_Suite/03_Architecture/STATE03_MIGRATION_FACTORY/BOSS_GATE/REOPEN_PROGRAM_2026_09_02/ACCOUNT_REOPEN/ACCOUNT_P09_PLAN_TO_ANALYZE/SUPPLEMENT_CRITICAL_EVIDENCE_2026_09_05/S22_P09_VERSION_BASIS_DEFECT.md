# S22 — P09_VERSION_BASIS_DEFECT — **THE HEADLINE OF THIS SUPPLEMENT**

**Checkpoint:** `CP-P09S22` *(added — material delta)* · **Layer:** 1 — clean-room.
**Classification: `CONTRADICTED` — the evidence base of the entire P09 programme is version-mismatched against every deployment it measures.**

---

## 1. THE FINDING

Every P09 round has reasoned from a **version-18** reference source tree. Verified this checkpoint from the deployments' own module registries — authoritative data, not inference:

| Deployment | Platform version | Budget module | Budget model present |
|---|---|---|---|
| **S** — the one carrying all the measurements | **16** | **installed**, v16 | the **legacy** budget model |
| B | **19** | uninstalled | the v19 report-budget model |
| E | **19** | uninstalled | the v19 report-budget model |
| T | **19** | uninstalled | the v19 report-budget model |

> **Zero deployments run version 18.** The source I have been reading matches **none** of them.

## 2. WHAT THIS INVALIDATES, AND WHAT IT DOES NOT

| Claim | Status |
|---|---|
| the **measurements** — 685 assets, 670 allocated, 339,382 management records, 226,612 on balance-sheet accounts, the depreciation legs and their near-cancellation | **UNAFFECTED.** These are facts about data. They stand |
| the **algebra** — negated balance × share, symmetric allocation annihilates | **UNAFFECTED as arithmetic**; but its attribution to the deployed code is now unproven |
| **every mechanism claim tied to v18 source** — the budget gate text, the eligibility chain, the sweep, the bridge path | **UNVERIFIED AGAINST ANY DEPLOYMENT.** Each is a correct reading of a version nobody runs |
| my `S02` statement that the deployment "holds zero budget records" | **CORRECTED** — the v18 budget tables do not **exist** there. My parser reported "0 rows" for **absent tables**. The v16 budget tables are present and separately empty |

## 3. THE NEW DEFECT THIS EXPOSED — LARGER THAN TH-F-01

In the **version-19** build that the project actually ships, the budget consumption gate was **changed**. It now reads, in both its expense branch and its outer filter:

> *…first token is income or expense · **OR the account type is one of current asset, non-current asset, or fixed asset** · OR the type is null…*

**Verified directly in the shipped v19 tree, at two places in the same query.**

> ### The v19 gate does not exclude the balance-sheet leg. It **explicitly admits** it.

This inverts the safety argument of `S01`/`S02`. Correct fixed-asset typing — which the deployed chart does have, and which I presented as the reason the defect does not fire — **is no protection in v19. It is the admitted class.**

And the offsetting population exists at scale: in deployment **S**, the accumulated-depreciation accounts carry **17,444** management records summing **+103,996,643.68** against **17,488** expense-leg records summing **−100,400,792.57** — matching to within 44 records and about 3.5 % of magnitude.

**Recorded as `TH-F-02` — and it is not a Thai finding at all.** It is version-general, needs no localization, no template and no mistyping, and it is **open**.

## 4. TH-F-01 — FINAL CLASSIFICATION, THIRD REVISION

| Round | Claim | Verdict |
|---|---|---|
| P09#03 | budget consumption nets to zero on a Thai-chart install | **CONTRADICTED** |
| this supplement, first pass | a template-only latent risk; correct typing protects | **CONTRADICTED — the protection does not exist in v19** |
| **final** | **a version-18-template defect, already FIXED in the version-19 template**, which types accumulated depreciation correctly. **Not a live risk on the shipping platform** | **SUPERSEDED — MATERIAL NEW EVIDENCE** |

**TH-F-01 is closed as a live risk and replaced by `TH-F-02`, which is larger, version-general, and open.**

## 5. A METHOD DEFECT IN MY OWN MEASUREMENT

My account census searched account **names** for an English substring. In two deployments the accumulated-depreciation accounts are named in **Thai script with no English substring** — my search would have returned zero and I would have concluded the accounts were absent. It happened not to bite only because the decisive deployment names them in English.

**The method was unsound and the correct result was luck.** Recorded as a third instance of the same family: a truncated listing, a template promoted to a deployment, and now a language-bound pattern.

## 6. THE STANDING RULE THIS ADDS

> **NC-10 — Establish the version of every deployment before reading any source, and cite source only from the version that deployment runs.**
> A mechanism claim carries a version. A measurement carries a deployment. **The two must match, and the match must be stated.**

## 7. WHAT THIS DOES TO THE PACKAGE

**No finding is withdrawn.** Every one is **re-scoped**: mechanism claims are now labelled *"verified in v18 source; not verified against any deployment"*, and measurements are labelled with the deployment version they came from. The two are no longer allowed to corroborate each other without an explicit version match.

**The single highest-value open item in the whole P09 line is now:** *which addons path does each v19 server actually run* — because two candidate v19 builds carry opposite budget filters, and that decides whether `TH-F-02` is live. **`HOLD — RUNTIME EVIDENCE REQUIRED`**, routed as `DEP-P09-29`.

## CHECKPOINT

**`CP-P09S22` — COMPLETE — EVIDENCE VERIFIED.** Version basis defect established; TH-F-01 superseded; `TH-F-02` raised; rule NC-10 added. Auto-continue.
