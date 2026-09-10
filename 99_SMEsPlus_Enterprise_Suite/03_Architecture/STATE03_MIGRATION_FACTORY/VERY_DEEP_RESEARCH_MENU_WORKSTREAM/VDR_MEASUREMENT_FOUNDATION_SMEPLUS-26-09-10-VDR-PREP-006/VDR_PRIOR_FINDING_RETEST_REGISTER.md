# VDR_PRIOR_FINDING_RETEST_REGISTER.md
# Eight prior findings retested — no conclusion preserved by default

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 16.

§22: *"Do not preserve earlier conclusion automatically."* Each is classified **CONFIRMED · REFUTED ·
PARTIAL · SUPERSEDED · UNRESOLVED**.

---

| # | Prior finding | Retest | Class |
|---|---------------|--------|-------|
| 1 | **A capability OFF does not revoke the capability** | The switch machinery adds and removes an *implication* on the holder group and never a user's own membership; a corpus-wide sweep for group→user revocation, with its predicate validated against the grant form, found **one** such site in 49. Runtime: **8, 7 and 6 gates** on three current-generation deployments are held directly with no implication. **A first instrument returned a clean 0 on all three; a control on the relation sizes failed it before any conclusion was drawn** | **CONFIRMED** — with the population separated into role gates, where direct assignment is intended, and capability gates, where it is not |
| 2 | **Module removal alters structures the module does not own** | The uninstall path drops owned tables and **foreign columns** with cascade, unlinks fields on surviving models whose target is removed, and **skips deletion guards declared not to run at uninstall**. Measured: **40 tables, 278 foreign columns** across 25 modules | **CONFIRMED from source; UNRESOLVED at runtime** — whether it has fired on any deployment is not established |
| 3 | **An interface gate is not a true security control** | Every internal user is a member by declaration; the framework discards it from the user's group set unless a debug flag is set and rewrites it in views as a display attribute; **the source's own comment says it is not a security group**. Present on all five deployments, as are the 56 elements it governs | **CONFIRMED** |
| 4 | **The inventory value field is writable** | Read from the deployment's own field registry: stored, monetary, **`readonly = false`**. Discriminating control: three sibling fields on the same object are `readonly = true` | **CONFIRMED** |
| 5 | **FEFO silently degrades to FIFO** | The strategy record is deleted on uninstall; the referencing fields declare no delete behaviour so the framework nulls them; the resolver falls through. **The researcher's own prediction was a hard error and the tested result was a silent fallthrough — the tested result was published** | **CONFIRMED from source; UNRESOLVED at runtime** |
| 6 | **The valuation configuration is perpetual on the transacted deployment** | **REFUTED.** The category property is **company-dependent** and was set for **company 1 of 44**. The governing company setting reads **periodic on 44 of 44**; `inventory_period = manual`. The one genuinely perpetual current-generation deployment is a different one, which the same table had labelled *"unset × 3,977"* | **REFUTED — and the premise it had overturned is restored** |
| 7 | **No accounting route exists from movement to entry** | **PARTIAL.** The per-movement writer **is** located in source and is gated on a valuation account being set on a location; **0 of 525 locations carry one**, so the link is null **by construction of the configuration**, not by absence of a mechanism. **A fourth route exists**: a daily superuser job posting a closing **at company level with no movement reference** — and that job is one of the actions no prior population carried | **PARTIAL — the observation holds, the explanation was wrong, and the enumeration was incomplete** |
| 8 | **48 of 52 button exclusions were false** | The excluded controls carry no method name or a label the framework's cancel attribute overrides; no definition of that label exists anywhere in the reference tree. Independently reproduced | **CONFIRMED** |

---

## Roll-up

| Class | Count |
|-------|------:|
| CONFIRMED | **4** |
| CONFIRMED from source, UNRESOLVED at runtime | **2** |
| PARTIAL | **1** |
| **REFUTED** | **1** |

## The one refutation, and why it is the most instructive entry here

Finding 6 was itself a **retraction** — it overturned an earlier, correct conclusion. It was published
with the confidence of a correction and propagated into a Critical Gap, a readiness finding and a
Boss-decision filter before an independent challenger caught it.

**The disproof was a file inside the same frozen package**: the company records were extracted, hashed,
shipped, and never read.

> **A retraction deserves more scrutiny than the finding it retracts, not less** — and the first place
> to look is the evidence the round has already collected and not yet examined.
