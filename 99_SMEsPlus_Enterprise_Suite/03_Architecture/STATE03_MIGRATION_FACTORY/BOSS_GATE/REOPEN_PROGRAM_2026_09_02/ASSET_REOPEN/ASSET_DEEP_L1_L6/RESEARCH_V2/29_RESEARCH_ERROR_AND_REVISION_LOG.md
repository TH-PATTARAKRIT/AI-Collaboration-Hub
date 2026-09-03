# 29 — RESEARCH ERROR AND REVISION LOG
**LAYER 2 — AUDIT QUARANTINE**

Mandatory under §80. **No incorrect historical finding is deleted.** Each entry
preserves the original conclusion and its evidence, then records what changed.

Two sources of revision are logged: corrections to the **prior session**
(`PRI-01`, commit `57cdb99`), and corrections made **within this session** as
better evidence arrived.

---

## REV-01 — The governing constraint of the prior session was wrong

**Original finding** (`PRI-01`, file `00` §2, file `01` §1):
> *"Search for local reference-ERP checkout/dump/DB: None found anywhere in this
> working tree or documented sibling folders. No source-code or database access
> exists for this session."*
> …*"No source code or database access existed for this session (confirmed by
> search), so this package leans heavily, and openly, on public documentation."*

**Original evidence:** directory inspection of the session working tree and its
documented sibling folders.

**Why it was wrong:** the search was **correctly executed and incorrectly
generalised**. The scope stated — working tree and sibling folders — did not
contain the source. The conclusion drawn — that no access exists — extended beyond
that scope. The complete v18 Enterprise source tree, the v14 legacy tree with the
project's own custom modules, and runtime ORM read-outs against the UAT all exist
in the workspace, outside the folders searched.

**New evidence:** `SRC-01`…`SRC-31`, `EV-RT-01`…`EV-RT-03`, `EV-XLS-01`, `EV-HND-01`.

**Corrected finding:** primary source code for the target version, for the legacy
version, and for the project's own custom modules is available, as are runtime
read-outs of the UAT population.

**Classification change:** the prior package's methodology rested on documentation
(evidence priority 6 and 11 under §9). This session works from primary source code
and runtime evidence (priorities 1–3).

**Architecture impact:** every material conclusion of the prior session required
re-derivation. Eleven were re-tested; results in `REV-02`…`REV-05` and §2 below.

**Lesson for future sessions, recorded as a method rule:** a negative search result
must be reported **with its scope attached** — *"not found in X"* — never as
*"does not exist"*. The prior session stated its scope honestly in file `00` and
then dropped it in file `01`. Every negative finding in *this* package therefore
carries the standing qualifier *"in the source trees available in this workspace"*
(`03` `G1-01`, Expert 4).

---

## REV-02 — "No native Equipment↔Asset link" — upgraded, not overturned

**Original finding** (`PRI-01`, file `01` §2.2): *"does not appear to have a
native, first-class Equipment↔Asset field link… a material negative finding, not a
gap in this session's search effort."*

**Original evidence:** absence of an official documentation page; only
community/third-party modules and forum threads found.

**Status: `CONFIRMED AGAIN`, and upgraded from `SUPPORTED INTERPRETATION` to
`FACT VERIFIED`.**

**New evidence:** exhaustive search of all 797 modules in the v18 Enterprise tree
(`SRC-15`). The asset model is referenced by three modules, none operational.

**What is added:** the prior session could not see **the project's own custom link**,
which does exist, or its **three defects** (`19`). The prior conclusion was right
about the product and blind to the deployment.

---

## REV-03 — "Maintenance cost integration is not evidenced as automatic" — upgraded and strengthened

**Original finding** (`PRI-01`, file `01` §2.3): *"not evidenced as automatic…
no documented pathway was found by which a maintenance request's cost automatically
flows into that rate or into product cost."*

**Status: `CONFIRMED AGAIN`, and strengthened.**

**New evidence:** `SRC-10`. Field enumeration of the maintenance models shows a
maintenance request has **no monetary field of any kind**, and equipment carries one
inert float with no currency, account, analytic or journal.

**Corrected finding:** it is not that maintenance cost does not *flow*. **There is
no maintenance cost figure in the system to flow.** Maintenance's only production
effect is on capacity.

**Architecture impact:** raises the finding from "integration gap" to "the data does
not exist", which changes what SMEsPlus would have to build.

---

## REV-04 — Within this session: the custom asset-link module was briefly misread

**Original finding, made and corrected inside this session:** on first reading, the
custom asset-link module appeared to inherit a **different asset model** — one that
does not exist on v18 — and the conclusion was forming that the module could not
load at all.

**Original evidence:** a file in the module's models directory inheriting the
legacy model name, using field attributes removed after v16.

**Why it was wrong:** the module's **package initialiser was not read**. It imports
a *different* file, which correctly targets the v18 asset model. The legacy file is
present in the tree, unimported, and inert.

**New evidence:** `SRC-21` (initialiser), `SRC-20` (the file actually imported),
`SRC-24` (the inherited view, which confirms the v18 model), `SRC-25` (the dead
file).

**Corrected finding:** the module loads, and the Asset→Equipment field exists on
v18. Three of its four intended behaviours are nonetheless inert (`19` §3).

**Lesson, recorded:** reading a model file is not reading a module. The initialiser
determines what executes. This is the check that found `EQ-DEF-01`, and it would
have produced a false negative had it not been applied to this module too.

---

## REV-05 — Within this session: the custom Thai method was briefly judged non-compliant

**Original finding, made and corrected inside this session:** reading the custom
Thai depreciation override alone, it appeared to charge a **full month** in the
acquisition month — including days before acquisition — which would conflict with
Revenue Code s.65 bis (2)'s requirement of deduction *in proportion to the period
from the acquisition*. A finding was forming that the module believed to be
"the Thai-compliant one" was in fact less compliant than the standard behaviour.

**Original evidence:** the custom override, read in isolation.

**Why it was wrong:** the override replaces only the **per-period amount**. The
standard v14 board loop that calls it applies a **first-period prorata factor** on
top. Read together, the acquisition month is correctly prorated.

**New evidence:** `SRC-30` — the v14 board loop, which applies the prorata factor
after the amount computation and adds one extra period when prorata is enabled.

**Corrected finding:** the custom method prorates correctly from the acquisition
date. `17` §2.1 carries the corrected algorithm and states the correction inline.

**Lesson, recorded:** an override cannot be evaluated without the method that calls
it. This one nearly produced a serious and wrong compliance accusation.

---

## REV-06 — Within this session: the custom Thai method was expected to be unreproducible

**Original expectation, held into Level 2** (`05`, Expert 3, `D2-01`): that the
custom Thai method and the standard calendar-day mode were different arithmetics and
should not be assumed equivalent; the risk was framed as a **lost compliance
capability requiring redevelopment**.

**Why it needed revision:** the two *are* different algorithms — one per-period
independent, one cumulative-difference — but they produce the same numbers.

**New evidence:** `EV-SIM-02`. Side-by-side execution across four acquisition
patterns: maximum difference **0.03 THB per period**, **0.01 THB cumulative**, on a
1.2 million baht asset.

**Corrected finding:** the capability is reproducible by **one configuration field**.

**Classification change:** the risk moves from *High — regression requiring
redevelopment* to *Medium — configuration verification*. The **exposure is
unchanged**; only the remedy became cheaper.

**Note on process:** Expert 3's demand ("do not accept the substitute until proven
line-by-line") was **correct as a demand and wrong in its expectation**. Both halves
are recorded. `05` marks `D2-01` resolved-by-evidence rather than deleting it.

---

## REV-07 — The Thai daily-depreciation assertion — upgraded

**Original finding** (`PRI-01`, file `01` §2.4): `SUPPORTED INTERPRETATION`, on the
basis of a community discussion plus a rates summary, with the primary Royal Decree
text not retrieved.

**New evidence:** `LAW-01` and `LAW-02` — primary text from the Revenue Department
for both Revenue Code s.65 bis (2) and Royal Decree 145 s.4.

**Corrected finding, split into two:**

| Claim | Prior | Now |
|---|---|---|
| Depreciation must be pro-rated from acquisition | `SUPPORTED INTERPRETATION` | **`FACT VERIFIED`** |
| The pro-ration unit is specifically the **day** | `SUPPORTED INTERPRETATION` | **`SUPPORTED INTERPRETATION`** — unchanged. The primary text says *period*, not *days* |

**Architecture impact:** the statutory requirement is now established. The remaining
open question is narrower and better defined — `UNR-01`.

---

## REV-08 — The post-depreciation internal usage formula — confirmed as design candidate

**Original finding** (`PRI-01`, file `01` §2.5): `DESIGN CANDIDATE`, no precedent in
the reference ERP's documented feature set, not a requirement of IAS/TAS 16.

**Status: `CONFIRMED AGAIN`**, now against source rather than documentation.

**What is added:** `10` §3.2 finds that the reference system has **no "fully
depreciated" state at all**, so the *trigger* for the Boss's mechanism must also be
constructed. That was not visible from documentation and it is a new requirement on
the design.

---

## REV-09 — "No contradictions found" — superseded

**Original finding** (`PRI-01`, file `01` §4): *"`CONTRADICTED`: None found at the
'two authoritative sources disagree' level in this pass."*

**Status: `SUPERSEDED`.**

**New evidence:** six contradictions are registered in `37`, including one
(`CTR-02`) that is a straightforward code defect and one (`CTR-03`) that concerns
the project's own legacy configuration.

**Why the prior session found none:** with documentation as the only evidence source,
code-versus-code and code-versus-runtime contradictions are structurally invisible.
This is a **consequence of `REV-01`, not an independent error.**

---

## REV-10 — The unresolved register's scale — superseded in character

**Original finding** (`PRI-01`, file `01` §2.6): a large share of the matrices
unresolved because *"no code/DB access exists and public documentation does not
reach implementation-level mechanism detail."*

**Status: `SUPERSEDED`.**

Most of those cells are now resolved from source. The unresolved items in `41` are
of a **different kind**: they need the **running system**, not more analysis. That is
a genuinely different research boundary.

---

## §80's worked example, re-tested

The prompt cites a historical correction: *"Asset Model should own Production
Allocation Method"* → *"Asset Model governs depreciation/accounting logic;
Production Equipment allocation belongs to the MRP production context."*

**Re-tested against source this session: `CONFIRMED AGAIN`**, and strengthened by
three independent findings — the Asset Model does not govern anything after
creation (`14` §5); on this deployment it governs **nothing at all** (280 assets,
zero links); and the reference product already places production cost configuration
on the work centre. `27` §4.

---

## REV-11 — Within this session: the Jira connector was assumed unavailable without testing

**Original finding, made and corrected inside this session:** the PMO verification,
the evidence manifest and the session record were all written stating that the
Atlassian connector was not authorised and that §96 could therefore not be met. The
first commit message repeated it.

**Original evidence:** the prior session (`PRI-01`, file `00`, file `26`) recorded the
connector as unauthorised, and a session notice listed the productivity Atlassian
plugin among servers requiring authorisation.

**Why it was wrong:** **the assumption was never tested.** A single call to enumerate
accessible resources returned an authorised site with Jira read and write scopes.

**New evidence:** an authorised Atlassian site with `read:jira-work` and
`write:jira-work`; the target epic located; a comment successfully posted.

**Corrected finding:** §96 is met. `43` §10 records the Jira update. `43` §8
deviation 2 is withdrawn.

**Lesson, recorded — and it is the same lesson as `REV-01`:** a limitation inherited
from a previous session is a **hypothesis**, not a fact. `REV-01` was this session's
central correction of the prior session, and the same error was then reproduced here
about a different capability. **Test the constraint before writing it down.**

This entry is retained rather than quietly fixed, because the pattern matters more
than the instance.

---

## Summary of prior-session findings re-tested

| Prior finding | Result |
|---|---|
| No code/DB access exists | **CORRECTED** — `REV-01` |
| Asset engine coherent on method mechanics | `CONFIRMED AGAIN` |
| Three depreciation methods; three prorata modes | `CONFIRMED AGAIN`, and materially deepened (`16`) |
| No native Equipment↔Asset link | `CONFIRMED AGAIN`, upgraded to `FACT VERIFIED` — `REV-02` |
| Maintenance cost integration not evidenced | `CONFIRMED AGAIN`, strengthened — `REV-03` |
| Work Center hourly cost feeds operation cost | `CONFIRMED AGAIN`, and extended through to GL and COGS (`27` §1) |
| Thai daily depreciation is `SUPPORTED INTERPRETATION` | **Split and partly upgraded** — `REV-07` |
| Not Depreciable Value concept and formula | `CONFIRMED AGAIN` (`18`) |
| Modify posts a value change and recalculates unposted entries | `CONFIRMED AGAIN`, and made precise (`24`) |
| Post-depreciation formula is a `DESIGN CANDIDATE` | `CONFIRMED AGAIN` — `REV-08` |
| No contradictions found | **SUPERSEDED** — `REV-09` |
| Matrices largely unresolved | **SUPERSEDED** — `REV-10` |

**Five confirmed again · four corrected or split · two superseded.**

The prior session's reasoning was sound within the evidence it had. Its single
material error was `REV-01`, and every other difference follows from it.
