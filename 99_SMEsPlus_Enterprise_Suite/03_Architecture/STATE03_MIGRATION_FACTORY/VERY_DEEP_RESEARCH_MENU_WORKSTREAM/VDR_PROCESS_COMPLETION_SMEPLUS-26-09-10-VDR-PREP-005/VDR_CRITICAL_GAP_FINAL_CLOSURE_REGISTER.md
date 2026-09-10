# VDR_CRITICAL_GAP_FINAL_CLOSURE_REGISTER.md
# Six Critical Gaps — CLOSED or HOLD, and one closure withdrawn

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 09.

---

## `CRITICAL-GAP-01` — the valuation object was replaced between generations
**Process evidence, new:** the movement object's behaviours are now facet-complete, so the paths that
write value are traced rather than inferred.
**Runtime:** both sides of the replacement observed — value on the movement row in the current
generation on 3,680 of 3,680 completed movements; **absent from the movement row on 127,957 completed
movements across two prior-generation deployments**, where it lives in the ledger instead.
**Configuration — CORRECTED:** the transacted deployment is **periodic on 44 of 44 companies**. PREP-004
read a company-dependent category property set for one company of 44 and published it as the deployment's
configuration. **The premise PREP-004 retracted is restored**, and now rests on the deployments' own
company records rather than on an assumption.
**The writability half:** the value field is **`readonly = false`**, read from the deployment's own field
registry, with three sibling fields on the same object at `readonly = true` as the discriminating control.
**Status: HOLD.** The relocation is closed; the writability exposure is confirmed and is a design
constraint, not a research question.

## `CRITICAL-GAP-02` — persistent objects with no row-level isolation
**13 of 47 (27.7%)**, re-stated smaller and runtime-confirmed: 44 of 46 rules element-observed.
**Not advanced this round.** The per-object exposure assessment still has not been performed.
**Status: HOLD.**

## `CRITICAL-GAP-03` — role-dependent record filter on an audit screen
**RE-OPENED on traceability.** The technical claim may well be right; **no reviewer can check it.** The
gap names **no learning ID, no element identity, no module and no Critical Area** — uniquely among the
six. An independent challenger could neither confirm nor refute it, and said so.
**A closed gap whose subject cannot be located is not auditable, and an unauditable closure is not one.**
**Status: HOLD** until its affected population is named.

## `CRITICAL-GAP-04` — company-less transactional records
**RE-OPENED.** PREP-004 closed it on **16** record rules derived from source. The transacted deployment's
own rule records say **60 distinct rules across 60 models**, all active — roughly four times the closed
figure, and three of them come from modules with **no source in the declared path set**, so they could
never have been counted from source at all.
**The direction of the finding is unchanged and its magnitude was understated fourfold.** The design
recommendation it carries — *no transactional record without an owning scope* — is **strengthened**, not
weakened.
**Status: HOLD.** A closure at a quarter of the measurable population is not a closure.

## `CRITICAL-GAP-05` — opening a menu mutates data
**New this round:** the menus concerned are now facet-complete, so the mutation is visible in
`PROCESS-10` and the scheduler path in `PROCESS-12` rather than asserted. **4 of 9 menus mutate on open**;
the suppression switch guards 2 of its 5 call sites and is itself undeclared.
**The remaining 5 menus are still untraced to the same depth.**
**Status: HOLD.**

## `CRITICAL-GAP-06` — the reference object
Element-observed on all three current-generation deployments · **11,878 rows** on the transacted one ·
**1 access grant, 0 record rules** · reachable only through the technical-only gate — **and that gate is
now established as not a security control at all**, so the object is not protected by it.
**Its severity is higher again than when raised.**
**Status: HOLD.** The nine-dimension study has not been done.

---

## The withdrawal

**Both of PREP-004's closures are withdrawn**, on independent grounds — one on evidence, one on
traceability. Neither was withdrawn because a number was wanted; both were withdrawn because an
independent reviewer went to the deployment's own records and to the package's own citations, and the
closures did not survive either.

## Roll-up

| | |
|---|---|
| Open at round start | 6 |
| **CLOSED** | **0** |
| **HOLD** | **6** — including `-03` and `-04`, whose PREP-004 closures are **withdrawn** |
| Advanced by new evidence this round | 3 (`-01`, `-05`, `-06`) |
| Referred to the Boss as an open technical question | **0** |

**Zero gaps closed. The programme's only two closures are withdrawn** — one because it was closed at a
quarter of the measurable population, one because it named no subject a reviewer could audit.

That is a worse result than PREP-004 published, and it is the correct one. Each of the six names the
specific measurement that would close it, and **none names the Boss.**
