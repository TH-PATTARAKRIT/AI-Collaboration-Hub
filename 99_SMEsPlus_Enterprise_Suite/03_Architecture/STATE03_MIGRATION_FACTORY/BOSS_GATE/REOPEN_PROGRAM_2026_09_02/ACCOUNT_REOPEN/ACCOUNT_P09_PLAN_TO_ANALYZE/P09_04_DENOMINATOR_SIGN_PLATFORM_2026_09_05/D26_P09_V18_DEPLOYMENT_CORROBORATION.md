# D26 — P09_V18_DEPLOYMENT_CORROBORATION — **incoming P04 finding, verified; blocker B7 partly withdrawn**

**Checkpoint:** `CP-P09D26` *(added — material delta)* · **Layer:** 1 — clean-room.
**Peer:** P04, commit `72286ce`, findings `P04-F-99` / `P04-F-100`. **Every claim re-measured by P09 before acceptance.**

---

## 1. THE BLOCKER I RAISED IS CONTRADICTED — BY MY OWN RE-CENSUS

`B7` (CRITICAL) stated: *"the programme's source is version 18; **no deployment runs version 18**."*

**Verified false.** Two version-18 deployments exist on this host, both matching the source tree the programme has been reading:

| Deployment | Platform | Modules installed | Analysis module |
|---|---|---|---|
| **U** *(a UAT database)* | **V18-BASE** *(major line 18, third point release — exact string held in Layer 2)* | 361 | installed, **V18-ANALYSIS** *(major line 18, first point release)* |
| **P** *(a second database)* | **V18-BASE** *(major line 18, third point release — exact string held in Layer 2)* | 478 | installed, **V18-ANALYSIS** *(major line 18, first point release)* |

> **`B7` is PARTIALLY WITHDRAWN.** The version-mismatch finding stands for the four databases previously censused; it does **not** stand as a statement about the population. **Every mechanism claim in this programme is version-matched to at least two real deployments.**

## 2. A FIFTH EVIDENCE-BASE DEFECT — AND THE LARGEST CENSUS FAILURE YET

My "exhaustive" population was **six database artefacts**. An unbounded census of the home directory alone returns **far more**:

| Location | Databases | In my census? |
|---|---|---|
| the downloads directory | 5 | yes |
| a further subdirectory of it | 1 | **no** |
| **a dedicated backup directory** | **1** — deployment U | **no** |
| **a version-18 simulation lab** | **7 snapshots** | **no** |
| **cloud-synced storage** | **1** — deployment P | **no** |
| a second cloud store | 5 further copies | **no** |

**Root cause:** my path set was *"the project volume, plus the downloads directory at depth 2"*. It excluded the home directory generally — where a backup folder, a **simulation lab named for the very platform version in question**, and cloud-synced storage all sat.

**Five consecutive rounds, five evidence-base defects:** a truncated listing · a template read as a deployment · a version mismatch asserted from an incomplete population · a silent sub-population · **and now a path set that excluded most of the host.**

## 3. THE CORROBORATION — THE MECHANISM MEASURED ON THE RIGHT VERSION

Deployment **P**, measured by P09 directly:

| Measure | Result |
|---|---|
| journal rows | **956** |
| **rows carrying an allocation** | **30**, across **14** distinct entries |
| analysis records | 84 |
| — resolvable to a journal row | **52** |
| — **not** resolvable *(the ledger-less operational population)* | **32** |
| entries measurable for netting | **13** |
| **entries netting EXACTLY 0.00** | **13 of 13 — 100 %** |
| positive controls | balance non-null on 956 of 956; account non-null on 953 |

> **On the platform version this programme has been reading, every measurable allocated entry nets to exactly zero.** This is the version-matched corroboration `B7` said was missing.

**One correction to the peer's figure:** P04 reported *"all 14 net to exactly 0.00"*. **13** of the 14 distribution-carrying entries produced resolvable analysis records; all 13 net to zero. The fourteenth is not a counter-example — it is **unmeasurable**, and should be stated as such rather than counted as a confirmation.

## 4. DEPLOYMENT U — "SCHEMA, NOT DATA", MEASURED

| Measure | Result |
|---|---|
| analysis module | **installed** |
| analysis plans | **1** |
| **analysis accounts** | **0** |
| analysis records | **0** |

**A dimension that is installed, carries a plan, and has never had a single value created — in a database of 40,000-odd journal rows.**

This is the base package's root-cause finding — *the analytic dimension is schema, not data* — **measured rather than inferred**. It was reasoned from source in P09#01 and has never had a deployed witness until now.

## 5. THE DISTINCTION P04 SUPPLIES, AND IT BELONGS IN MY CHAIN

P04's point is correct and I had not drawn it:

| Deployment state | How attribution fails | Would populating the dimension fix it? |
|---|---|---|
| **no analysis accounts ever created** (U) | the dimension is schema only; nothing is attributed because there is nothing to attribute to | **yes** |
| **accounts created** (P) | the charge reaches the cost centre and **leaves it in the same entry** | **no — this is where populating it leads** |

> **Two mechanisms defeat attribution, and a design that fixes one does not fix the other.** A reader who takes *"schema, not data"* as the whole story will conclude that populating the dimension is the remedy — and in the one deployment where it **is** populated, attribution still does not survive.

**Adopted into the eleven-defect chain as its terminal statement.** It is the strongest single argument for the event-level completeness check the programme has proposed: **neither failure is detectable from the dimension's own contents.**

## 6. CONSEQUENCES FOR P04, RETURNED

P04 notes its own netting finding describes code that never ran in deployment U. **P09 confirms and sharpens:** with no analysis accounts there is no attribution at row level either, so the netting defect sits **downstream of a more basic absence** — and the companion claim about mandatory dimensions is latent for a reason needing no code at all, since **nothing can be mandatory over an empty set.**

## 7. STATUS CHANGES

| Item | Change |
|---|---|
| **`B7`** | **CRITICAL → HIGH, PARTIALLY WITHDRAWN.** The mismatch was asserted from an incomplete population |
| **`B5`** *(denominator discipline)* | **HIGH → CRITICAL.** Fifth consecutive evidence-base defect; this one excluded most of the host |
| **zeroing mechanism** | **corroborated on the source version**, 13 of 13 |
| **root cause** | **corroborated in deployment** for the first time |
| **new open item** | the seven simulation-lab snapshots are **unexamined** — `DEP-P09-30`, class **C** |

## CHECKPOINT
**`CP-P09D26` — COMPLETE — EVIDENCE VERIFIED.** Peer finding verified, one blocker withdrawn, one raised, census failure recorded.
