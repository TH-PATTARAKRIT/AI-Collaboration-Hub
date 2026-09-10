# VDR_FALSE_EXCLUSION_CORRECTION_REGISTER.md
# Every exclusion re-opened, with its correction and its effect on the denominator

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 03.

---

## 1. The rule this register enforces

§6 of the commissioning instruction: **no exclusion may stand solely because**

> the menu is hidden · the button is disabled · the function is optional · the feature is
> configuration-dependent · another module owns the workflow · the current user cannot reach it ·
> the current default configuration does not expose it

**These conditions require classification, not exclusion.** This register re-opens every exclusion in
the lineage and tests it against that list.

## 2. Exclusions re-opened, and their disposition

| # | Set | n | Original exclusion reason | Test against §6 | Corrected disposition | Denominator effect |
|---|-----|--:|---------------------------|-----------------|----------------------|-------------------|
| `FE-01` | Buttons whose invoked method was "not located" | **52** | *"the process belongs to another domain"* | **FALSE for 48.** Read at their own cited pointers, 41 carry **no method name at all** and 7 name a label that the framework's cancel attribute overrides; `def cancel_button` exists **nowhere** in the reference tree. They are framework discard controls **declared inside domain modules** | **48 → applicable, DETERMINED** with the corrected condition *"no method executes, in this domain or any other"*; **4 → applicable, NOT_DETERMINED** (genuinely external) | **+52 PROCESS cells** |
| `FE-02` | Extension menus whose action is owned outside the domain census | **38** | *"owned outside the domain action census"* | **§6 violation** — this is "another module owns the workflow", listed verbatim as a prohibited reason | **applicable, NOT_DETERMINED** | **+38 PROCESS cells** |
| `FE-03` | Handoff elements' runtime cell | **90** | *"that domain's measurement, not this one's"* | **§6 violation** — ownership by another domain is not an exclusion ground. Their own reachability field read `UNMEASURED`, i.e. in-scope and unmeasured | **applicable.** Now **79 of 90 element-observed** on real deployments | **+90 RUNTIME cells** |
| `FE-04` | Grouping-container menus | **3 of 17** | container rule, applied to the three rows a challenger named | **Defect of a different kind — a rule applied to a named subset.** The other **14** carried the full menu profile. The justifying sentence claimed *"14 were already correct"*; enumerated, the 14 are precisely those that **did not** receive the rule | **CONTAINER promoted to a class in the published rule table and applied to all 17.** Runtime and security remain applicable — a container **is** a record and its visibility is determinable | **−42 cells** (14 × 3) |
| `FE-05` | Items whose module is installed on no observed deployment | **617** | — *(never excluded)* | **conformant** | conformant: they are **in** the population and carry a determination of absent | none |
| `FE-06` | Elements gated to a technical-only group | **55** | — *(never excluded)* | **conformant** | conformant: "the current user cannot reach it" was correctly not treated as an exclusion | none |
| `FE-07` | Optional-module and optional-core elements | **970** | — *(never excluded)* | **conformant** | conformant with §8 and §6 | none |
| `FE-08` | Edition-restricted items | **1,411** | published as a class with **zero** members | the classifier **had no branch capable of emitting the class** — an exclusion by construction, invisible because nothing was ever written down | class populated: **71 of 126 resolvable domain modules are edition-restricted** | none *(classification, not denominator)* |

## 3. `FE-04` in full — because it is the most instructive entry

The container correction was made in the previous round **to the three rows a challenger named by
identifier, and to none of the other fourteen nodes of the same kind.** Enumerated from the register:

```
nodes carrying kind=CONTAINER            : 17
had the container rule applied (R2)      :  3   LI-INV-MENU-0028 / -0034 / -0042
carried the full menu profile            : 14
```

Three compounding problems, all now closed:

1. **The rule table had no CONTAINER class at all**, so the correction was defended as *"a rule-table application"* when no such rule existed. **CONTAINER is now a published class row.**
2. Under the exclusion register's own standard — *"a per-row `NA` that is not in this register is a defect"* — with that register deliberately empty, **the package's own rule classified its own three cells as defects.**
3. The denominator was reproducible from **no** published rule. It now is.

> **This is the third consecutive round in this family to state a correction rule and not apply it to
> its own population.** The rule that catches it was written in the same package: *corrections land on
> the row naming the identifier and nowhere else — audit by identifier, never by disposition.* Applying
> a rule only where a reviewer pointed is the same defect wearing the reviewer's clothes.

## 4. Denominator effect, netted

| | Cells |
|---|---:|
| PREP-003 R2 published | 30,906 |
| restored process cells — entries `FE-01` and `FE-02` | +90 |
| restored handoff runtime cells — entry `FE-03` | *(already restored in R2)* |
| Container rule applied to all 17 | −42 |
| Container runtime + security restored | +6 |
| **PREP-004 V5** | **30,870** |

**Every movement is traceable to a numbered entry above, and the denominator is now derivable from the
published rule table alone.**

## 5. §6 conformance audit — the whole population, not a sample

Every `NA` reason surviving in V5 was enumerated and tested against §6's prohibited list:

| Surviving `NA` reason | Cells | Class-based? | §6-conformant? |
|---|---:|---|---|
| *the class is a declaration, not an invocable behaviour* | 3,510 | yes | yes |
| *the class has no lifecycle and therefore no reverse/cancel/return path* | 3,907 | yes | yes |
| *the class holds no data of its own* | 2,211 | yes | yes |
| *the class has no cross-boundary relation of its own* | 2,165 | yes | yes |
| *the class carries no access-control surface of its own* | 1,016 | yes | yes |
| *the class cannot be optionally activated independently of its module* | 974 | yes | yes |
| *the class carries no configuration condition* | 962 | yes | yes |
| *grouping container — invokes nothing / carries no gate / cannot be activated alone* | 51 | yes (17 × 3) | yes |

**Zero surviving exclusions rest on a §6-prohibited reason. Zero per-row `NA` remains.** The exclusion
register stays deliberately empty: nothing was authorised out — everything was either restored or
governed by a published class rule.
