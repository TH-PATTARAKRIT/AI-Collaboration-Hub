# S09 — P09_ZEROING_RISK_CLASSIFICATION

**Checkpoint:** `CP-P09S09` · **Layer:** 1 — clean-room.

---

## 1. THE CLASSIFICATION REQUIRED

| Dimension | Verdict |
|---|---|
| **UNIVERSAL?** | **No** — it requires one allocation to reach every row of a balanced set |
| **THAI-CHART SPECIFIC?** | **No.** This was the prior round's error. It needs no localization |
| **EVENT-TYPE SPECIFIC?** | **Yes** — three mechanism families reproduce it exactly; two others fail by residue instead |
| **MODULE-SPECIFIC?** | **No** — predominantly core accounting, not the asset module |
| **CONFIGURATION-DEPENDENT?** | **Yes for the precondition** — the source object must carry an allocation. **No for the outcome** — once the precondition holds, the zero is arithmetic |
| **DEPLOYMENT-DEPENDENT?** | **Yes for incidence** — 670 of 781 assets across the population carry an allocation, **all in one deployment** |
| **VERSION-DEPENDENT?** | **NEWLY ADDED, and material** — see §3 |

**Final classification: `EVENT-TYPE SPECIFIC · CONFIGURATION-GATED PRECONDITION · ARITHMETIC OUTCOME · VERSION-SENSITIVE CONSEQUENCE`.**

## 2. THE EXACT CHAIN, AS THE DIRECTIVE REQUIRES

| Element | Value |
|---|---|
| source event | an asset consuming a period of its useful life |
| journal pair | two rows: accumulated depreciation (**balance sheet**) credited, depreciation expense (**profit and loss**) debited |
| allocation | the asset's own, written to **both** rows under a guard whose comment addresses only conditionality |
| account types, deployed | balance-sheet leg on a fixed-asset type (671 assets) or current-asset type (13); expense leg on a depreciation-expense type (671) or plain expense (13) |
| signs | the management amount is the **negated** row balance, so the balance-sheet leg yields **positive** and the expense leg **negative** |
| amounts, measured | balance-sheet leg **17,444 records / +103,996,643.68**; expense leg **17,488 records / −100,400,792.57** |
| cost object | whichever axis value the asset's allocation names |
| **net management effect** | **the two legs match to within 44 records and ~3.5 % of magnitude — they very nearly annihilate** |

## 3. THE VERSION DIMENSION — NEW THIS SUPPLEMENT

The **consequence** of the zeroing differs by platform version, and this was not known before:

| Version | Does the budget gate admit the balance-sheet leg? | Consequence |
|---|---|---|
| **18** *(the source read all programme long; **run by no deployment**)* | **no** — income/expense only | the zeroing is confined to net-balance surfaces; budget consumption is protected |
| **19** *(the shipping build)* | **YES — the gate explicitly admits fixed, current and non-current asset types** | **the protection does not exist.** The balance-sheet leg enters budget consumption and the offsetting population is present at scale |
| **16** *(the deployment carrying every measurement)* | a different budget model entirely; **not decidable** from any source tree on this host | **`HOLD — SOURCE EVIDENCE REQUIRED`** |

> **The zeroing risk is materially worse on the version the project ships than on the version it has been studying.**

## 4. SEVERITY

| Aspect | Rating |
|---|---|
| mechanism | **CRITICAL** — arithmetic, unconditional once the precondition holds |
| incidence | **HIGH** — 670 allocated assets, ~17,400 record pairs, in one live deployment |
| surface exposure on v18 | MEDIUM — confined to net-balance surfaces |
| **surface exposure on v19** | **CRITICAL — budget consumption is no longer protected** |
| detectability | **CRITICAL** — every record is individually well-formed; nothing is malformed; the defect is only visible in the sum |

## CHECKPOINT

**`CP-P09S09` — COMPLETE — EVIDENCE VERIFIED.** Seven-dimension classification including a newly-found version dimension. Auto-continue.
