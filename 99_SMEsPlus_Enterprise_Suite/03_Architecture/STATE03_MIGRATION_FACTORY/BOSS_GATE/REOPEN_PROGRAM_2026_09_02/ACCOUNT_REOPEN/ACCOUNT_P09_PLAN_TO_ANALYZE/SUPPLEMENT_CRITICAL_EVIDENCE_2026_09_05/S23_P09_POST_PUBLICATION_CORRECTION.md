# S23 — P09_POST_PUBLICATION_CORRECTION

**Checkpoint:** `CP-P09S23` *(added — material delta after `CP-P09SFINAL`)* · **Layer:** 1 — clean-room.
**Trigger:** the fourth AAS-03 challenge returned **after** the supplement was committed and pushed at `39c3784`. It corrects the package's single most-quoted number. **Every figure below was re-measured by the author before acceptance.**

---

## 1. THE HEADLINE NUMBER WAS WRONG IN THREE WAYS

| | Published at `39c3784` | **Corrected, re-measured** |
|---|---|---|
| balance-sheet-leg records | 17,716 | **17,444** |
| expense-leg records | 18,483 | **17,488** |
| balance-sheet-leg sum | +101,778,591.13 | **+103,996,643.68** |
| expense-leg sum | −104,739,812.94 | **−100,400,792.57** |
| **net** | −2,961,221.81 | **+3,595,851.11** |
| gross | 206,518,404.07 | **204,397,436.25** |
| **annihilated** | 98.57 % | **98.24 %** |

### 1.1 Why my figures differed
I grouped by *the accounts each asset actually references*. The correct population is *every account of that type in the chart*. Mine was an **asset-derived subset**, not the population — a proxy chosen by the author of the claim it bounded. **The programme's own denominator rule, missed again.**

### 1.2 The correction that matters most is not the count — it is the **sign**

> **The net is `+3,595,851.11`. A net CREDIT.**

The package has said throughout that the attribution "nets to zero". It does not: in deployed data, depreciation contributes a **net positive** to a ledger the product itself labels a margin ledger. **Depreciation makes the cost centre look more profitable.**

That is **materially worse than zero** and no document in the package said it. Every use of "exact zeroing", "nets to zero" and "annihilates" as a description of the *deployed* result is hereby qualified: the mechanism produces near-cancellation with a **sign-inverted residue**.

## 2. `TH-F-02` IS MUCH LARGER THAN I PUBLISHED

I framed it at the scale of the depreciation pair. Measured across all 339,382 records, applying each gate:

| Gate | Records admitted | Admitted total |
|---|---|---|
| income/expense only *(v18 and three of four v19 builds)* | 112,770 | **+24,860,594.23** |
| **+ fixed, current and non-current asset types** *(the divergent v19 build)* | **282,724** | **−252,214,900.89** |
| **delta** | **+169,954** | **−277,075,495.12** |

**The gate change flips the admitted total from +24.9 M to −252.2 M across 169,954 additional records.** Not a depreciation-pair effect — a **277 M swing**.

**And my denominator was wrong there too:** I wrote *"two candidate builds carry opposite filters"*. It is **one of four** — three carry the income/expense gate, one admits the asset types. **Third denominator error in this package.**

## 3. TH-F-01's DEPLOYED REACH — I SAID IT DID NOT REACH; IT DOES

`S01` §5 concluded the code-block/type contradiction *"is internal to the template file and does not reach this deployment."* **CONTRADICTED.**

The deployed chart carries **nine** code-block/type contradictions of its own — including one account whose **code block and name both assert expense** and which is typed as a **balance-sheet fixed asset**. Under the income/expense gate its cost is **silently excluded** from consumption.

> **The defect class TH-F-01 names is present in this deployment, in the opposite direction.** My retraction was right about the Thai template and wrong about the deployment being clean.

`S01` §2's *"every other row conforms to its own code-block convention"* is also **CONTRADICTED** — a second violation sits in the same 28-line file I said I read in full.

## 4. TWO MORE ROUTING AND STATUS CORRECTIONS

| Item | Correction |
|---|---|
| **`S03` §3 "the complete list … is four items. All four are routed."** | **CONTRADICTED — it is 4 of 14.** Five remain unrouted, including the Thai statutory constraint on **cross-company management reporting**, which couples directly to the re-opened scope row. **A completeness claim over an author-chosen set, inside the document written to correct exactly that failure.** |
| **`S12` final status `P11 RECONCILIATION REQUIRED`** | **withdrawn → `OPEN — SCOPE EVIDENCE REQUIRED`.** Its own stated closure conditions were measurable on this host and I did not measure them. Also `S12` §2's stated cause — *"partial by the inter-company margin"* — is **CONTRADICTED**: price and quantity are preserved exactly on the mirror, so there is no margin. The real drivers are company-currency divergence, tax-inclusion policy, per-tax analytic flags, composite-key wholesale drop, and the receiving company's own defaults |
| **incidence, now measured** | **0 of 5 deployments carry all three preconditions; 2 of 5 carry two of three**, both v19 installs with inter-company already enabled and one holding **three company-less axis values**. One configuration act arms it |
| **`AAS+-VETO-03` scope** | widened from *"design adoption only"* to **design adoption *and platform build selection*** — the divergent build arms the identical arithmetic with no SMEsPlus design act. Its grounds must **stop citing 98.57 %** and cite instead *net +3.6 M against a 100.4 M economic cost, sign-inverted, measured* |

## 5. THE PATTERN, STATED PLAINLY

**Fourteen author errors across the P09 line. None self-caught.** This round alone: an asset-derived subset used as a population, a two-of-four denominator, a completeness claim over an author-chosen set, and a "does not reach this deployment" that reaches it nine times.

**Three of the four are denominator errors** — the defect the programme has a written rule against, committed inside the documents written to correct earlier instances of it.

> **The rule is understood and is not being applied to the author's own work.** That is a process finding, not an analytical one, and it is the most durable thing this round produced.

## 6. WHAT IS UNAFFECTED

The algebra; the eligibility structure; the version-basis defect (`B7`); that the mechanism fires at scale; the 226,612-of-339,382 balance-sheet-account measurement; every peer handoff's substance. **No finding is withdrawn — three are re-measured, one is widened, two are re-routed.**

## CHECKPOINT

**`CP-P09S23` — COMPLETE — EVIDENCE VERIFIED.** Headline re-measured, sign inversion recorded, `TH-F-02` re-scaled, two statuses corrected. Auto-continue to re-publication.
