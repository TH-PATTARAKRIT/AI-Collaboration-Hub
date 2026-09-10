# INVENTORY_PILOT_SOURCE_RESOLUTION_REPORT.md
# Inventory Pilot — LESA Source Resolution Loop

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · Generation basis: **R1 (series-19, content-verified)**
Layer: **LAYER 1 — CLEAN-ROOM.**
Loop definition: `VDR_EXECUTION_ORDER.md` §3.

---

## 1. The rule this report exists to enforce

> When a source-related unknown is raised, **route it to LESA. Do not send general researchers to
> search the source blindly.**

Blind searching produces the programme's most expensive defect class: a negative result that reflects
where someone looked rather than what is there. Every item below names **what was unknown**, **where
LESA said to look**, and **what the evidence was** — or records honestly that the item is still open.

---

## 2. Resolutions completed in this session

### SR-01 — RESOLVED — Seven menus whose target object is not in their action record
**Raised by:** Register 01 `MM-F-01`. Static analysis resolved 55 of 62 menus to a target object and
failed on 7, including the three primary operational entry points.

**LESA resolution route:** the 7 are bound to **server actions**. A server action carries executable
code, not a target. The route is: *menu → server action record → the code fragment it holds → the
method that fragment calls on the object → the window action that method loads by identifier → that
action's target and context.* **Three hops, not one.**

**Executed:** an automated hop-2 resolver was written and run. It resolved **3 of 7** unaided. The
remaining 4 use an intermediate call form the resolver could not follow, and were resolved by targeted
reading of the named method. **All 7 are now resolved.**

**Evidence:** `LAYER2_AUDIT_QUARANTINE/MACHINE_REGISTERS/hop2_resolution.json`, plus the method bodies
cited in Register 08 `HA-F-01`/`HA-F-02`/`HA-F-03`.

**Material delta produced:** two findings that no menu-level or action-level analysis could have
reached — a menu that mutates data on open, and a menu whose record population changes with the
viewer's role.

### SR-02 — RESOLVED — Did the configuration-gating census miss surface?
**Raised by:** self-challenge on Register 02, applying instrument control I3.

**LESA resolution route:** gating is an attribute available on **any** element inside a view
definition, not only on the two element kinds the first instrument read.

**Executed:** instrument repaired and re-run. **87 → 633 gated elements; 14 → 43 groups; 2 → 12
element kinds.** Recorded as `CORR-F-07`.

### SR-03 — RESOLVED — Zero constraints reported for the domain
**Raised by:** instrument control I4 (mandatory zero re-test).

**LESA resolution route:** the target generation declares data constraints through a **different
construct** from the one the instrument matched. The instrument's pattern was valid for series-18 and
**could not fire at all** on series-19.

**Executed:** instrument repaired. **0 → 32 constraints.** Recorded as `CORR-F-08`.
This is the clearest single demonstration in the Pilot of why a zero must be re-tested: the first
result was not "few constraints", it was "the question was unanswerable as asked".

### SR-04 — RESOLVED — Is the inventory valuation object the same across generations?
**Raised by:** Register 05, on noticing an unfamiliar object in the series-19 owned set.

**LESA resolution route:** compare the declaring module's model directory across R1 and R2, then count
declarations (not textual mentions) in each.

**Executed:** series-18 declares a valuation-**layer** object referenced by **72** files. Series-19
declares it **0** times; **15** textual references remain, of which **14 are test files** and 1 is a
model file. A different object is declared in its place, documented in its own source as the history of
**manual** value updates, with current value carried on the movement.

**Material delta:** `CRITICAL-GAP-01` and `BOSS-DEC-01` — the programme's standing valuation and
cost-of-goods work was performed against a structure that does not exist in the target generation.

### SR-05 — RESOLVED — Is the series-18 comparator sound?
**Raised by:** self-challenge on an implausible cross-generation delta (scheduled jobs appearing to
grow 10 → 26).

**LESA resolution route:** compare **root scope**, not just generation, before attributing a delta to
a generation.

**Executed:** the first comparator carried **2** localisation modules against 523 in the primary — a
localisation-stripped build. A scope-matched comparator was located (1,273 modules, 433 localisations)
and a **second independent** series-18 comparator was then run as a control (1,300 modules, 454
localisations, carrying an authoritative release marker). The two agree within 0–3 on every dimension.
The true delta is **20 → 26**, not 10 → 26. Recorded in `00A_EVIDENCE_BASE_AND_PATH_SET.md` §3.

### SR-06 — RESOLVED — Does the domain have an approval mechanism?
**Raised by:** Register 07, Critical Area *Approval Control*.

**LESA resolution route:** three query forms plus a positive control against a domain known to carry
approval.

**Executed:** the vocabulary scan matches **238 files** — a number that would have supported a
confident answer in either direction. Reading the **23** matching declared fields resolves them into
regulatory authorisation codes, recipient signature capture, operational validation flags and
confirmation dialogs. **None is a segregation-of-duties control.** A first draft had recorded
"zero approval mechanisms found"; that statement was false and was caught before publication.
Recorded in full at Register 07 `SS-F-09`.

### SR-07 — RESOLVED — Was the evidence-base sweep complete?
**Raised by:** self-challenge on the PATH SET, after two sweeps returned different root sets.

**LESA resolution route:** the two sweeps had **different reach**. One was rooted at a cloud-storage
directory and reached deep paths; the other was rooted at the home directory with a depth limit that
could not reach them. **Neither was complete, and their disagreement was the only signal.**

**Executed:** re-swept every mount plus the home directory at sufficient depth, de-duplicated by
resolved real path. **36 → 50 roots.** The corrected sweep also located a **better** series-18
comparator and confirmed that generations 14, 16, 17, 18 and 19 are all present on the host.

**Method finding:** *a sweep that is not compared against a second sweep of different reach cannot
report its own incompleteness.*

### SR-08 — RESOLVED — Where do the "inert" configuration toggles take effect?
**Raised by:** Register 02 `CD-F-03` / `GAP-INV-02`. Seven group-toggles activate groups that gate no
screen element.

**LESA resolution route:** do not search the domain's views. A group can be consumed in four places:
a screen element, a **printed template**, a **runtime code test**, and **another domain's object**.
Trace every non-test reference to the group identifier across the whole root, then classify by
consumer kind.

**Executed:** all 7 resolved. **4** take effect in printed/report templates, **3** in runtime code
branches; one of the three additionally reaches a boundary object's view. **None is inert.**

**Material delta:** framework correction `CORR-F-21` — printed output and runtime code are
configuration effect surfaces and had no place in the original nine-register design.

**Method note:** the first classifier written for this trace mis-parsed its own tool output and
returned *"other"* for 100% of the 73 references it classified — a clean, uniform, entirely wrong answer. It was caught
because a result in which every reference falls into the residual bucket is not a result.

### SR-09 — RESOLVED — Can a completed write-off or teardown be undone?
**Raised by:** Register 04 `FN-F-04`. Both documents declare only `draft` and `done`.

**LESA resolution route:** absence of a cancelled state does not establish irreversibility. Three
routes must be checked, not one: a **cancel state**, a **reverse/undo method**, and **deletion**.
Deletion in turn has two layers — the access grant and any code-level deletion guard.

**Executed:** all three checked on both objects. No cancelled state. No reverse, undo or cancel method
in either object's full method census. Deletion is **granted** to the manager role by access row — and
**refused** by a code-level guard whenever the state is `done`.

**Result:** a completed write-off or teardown is **irreversible, uncancellable and undeletable**. The
only remedy is a compensating entry.

**Material delta:** two — `BOSS-DEC-11` (terminal-plus-compensation vs reversal-with-linkage) and
`GAP-INV-13` (**an access-grant census overstates the effective delete surface**, because guards live
in code and override grants; 2 of 15 guards read, 13 unread).

---

## 3. Items routed to LESA and still OPEN

| ID | Unknown | Why it is not closed | Disposition |
|----|---------|----------------------|-------------|
| `GAP-INV-06` | Financial postings created in code without a stored reference | Requires call-graph tracing from the domain's methods into the accounting domain; not performed | `SOURCE RESOLUTION REQUIRED` — **size unmeasured** |
| `GAP-INV-08` | The true population of menu-open side effects | Two were found by resolving seven menus; no systematic sweep of all 200 actions was run | `SOURCE RESOLUTION REQUIRED` — **floor of 2, not a census** |
| `GAP-INV-13` | How much smaller the effective delete surface is than the granted one | 13 of 15 deletion guards unread | `SOURCE RESOLUTION REQUIRED` — **floor of 2, ceiling unmeasured** |
| `GAP-INV-09` | All runtime / deployment evidence | No database server running; archive artefacts located but **not opened** | `HOLD` — this is the largest single bound on the package |

---

## 4. Loop discipline observed

| Control | Evidence |
|---------|----------|
| No general researcher was sent to free-search the source | Every item above names the resolution route before the search |
| No repeated research without material delta | Each resolution produced a delta; none was re-run |
| Negatives carry their scope | `SR-06` and `HA-F-08` both state the set they are negative about |
| A resolved item updated the population first, then the registers | `SR-02`, `SR-03`, `SR-04` all re-ran the population build before the registers were written |
| Open items are named with an owner and a trigger, not left implicit | §3 |
