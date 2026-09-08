# 01 — `RC-01` P09 CHALLENGE

**Frozen surface** `corr/p09-phase-s-final-2026-09-07-001` @ `2079a2594a6a76eb91bdb528f22eaf928d42c0d6`
**Lane** B — host-dependent
**Result** `RC-HOLD — REQUIRED EVIDENCE OR INDEPENDENCE UNAVAILABLE`
**Cause** independence, **not** evidence. See `00_` §3: this session authored the repair.

## 1. Exact scope restated before testing (prompt §5)

Re-execute the frozen P09 `q1.py` against the correct frozen population; establish the **deployed
generation** before relying on the declared source root; source `k1_population.json` **from the
frozen repository ref**, not from a peer session clone; verify `L-4` authority and denominator; test
the **actual producer surface**; preserve superseded lineage; prove the corrected disposition does
not silently overclaim exclusion authority.

## 2. Not run — and the reason is not the evidence

`RC-01` was **NOT RUN**. `q1.py` was not executed, `L-4` was not adjudicated, no denominator was
re-derived and no disposition was tested. Nothing in this file may be read as evidence about the
correctness of P09's repair in either direction.

## 3. Executor-neutral readiness evidence (not `RC` evidence)

| Item | Declared in handoff `961b2ec` | Measured on this host 2026-09-08 | Result |
|---|---|---|---|
| Source root `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons` | EXISTS | directory present | **PRESENT** |
| `.py` count under that root | **13,515** | `find <root> -name '*.py' -type f \| wc -l` → **13,515** | **REPRODUCES EXACTLY** |

**This is a file-count, not a finding.** It confirms the handoff's provenance claim is checkable and
that the RC-01 input is reachable from a host-local session. It says **nothing** about whether that
root is the *right* generation — the handoff itself flags that as the verifier's first task, and
`[[smeplus-version-basis-defect-rule]]` records that P09 read v18 source for four rounds while
deployments ran v16 and v19. **The generation question is open and is the appointed verifier's.**

## 4. Carried forward to the eligible verifier

- Source `k1_population.json` from `2079a25` (in-repo, `L1_L8_BOUNDED_CORRECTION_2026_09_06/LAYER2_AUDIT_QUARANTINE/INSTRUMENTS/`), **not** from any local peer clone.
- Establish the deployed generation from `ir_module_module` **before** reading source.
- The declared root exists and is reachable. **Reachability is not correctness.**
