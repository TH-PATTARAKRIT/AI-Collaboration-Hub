#!/usr/bin/env python3
"""
L-4  assess the 160 unassessed K-3 files against NON-PLANNING completeness claims
L-5  state what the 6 test files assert, before excluding them
"""
import json, os, re, collections

R = "/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons"
S = "/private/tmp/claude-501/-Volumes-iMacSys-SMEsPlus-ENTERPRISE-SUITE/65b32750-dad1-47c5-99a2-7eb7ad31f2a2/scratchpad"
D = json.load(open(S + "/L_results.json"))
ref_out, ref_plan, tests = D["ref_out"], set(D["ref_plan"]), D["tests"]
nonplan = {k: v for k, v in ref_out.items() if k not in ref_plan}

print("=== L-4 : THE 160 NON-PLANNING K-3 FILES, ASSESSED ===")
print("  DENOMINATOR: %d files outside the K-1 population that reference a P09 model" % len(nonplan))
print("  UNIT: the file.  INCLUSION: references a P09 model, declares/inherits none.\n")

c = collections.Counter()
for v in nonplan.values():
    for m in v: c[m] += 1
print("  which P09 models these 160 reference (unit = file):")
for m, n in c.most_common():
    print("    %-40s %d" % (m, n))

# The non-planning P09 claims that a REFERENCE could in principle disturb.
print("\n  P09's current NON-PLANNING claims, and whether a reference can disturb each:")
rows = [
 ("ownership: 10 owning files / 3 modules",
  "NO — ownership is declaration, not reference. A reference cannot make a file an owner."),
 ("extension counts: fact table 17, mixin 11, value 8, applicability 7, plan-fields 4",
  "NO — these count _inherit, a different relation from reference. Disjoint by construction."),
 ("population 52 files / 29 modules",
  "NO — the population is defined as declare-or-inherit; references are excluded BY DEFINITION, and that exclusion is the population's stated rule, not an oversight."),
 ("the analytic dimension is written into across the estate",
  "NO — these 160 CORROBORATE it; they cannot contradict a claim of breadth."),
 ("absence claims (forecast/scenario/target/baseline/simulation/variance)",
  "NO — every one of those is a PLANNING concept. A non-planning reference is outside their subject."),
]
for claim, verdict in rows:
    print("    - %-72s %s" % (claim, verdict))

print("""
  L-4 RESULT: the 160 reference the ANALYTIC DIMENSION only. Every current P09
  completeness or absence claim they could touch is either (a) defined on
  declaration/inheritance, which reference is disjoint from, or (b) a planning
  claim, which these files are outside of by measurement.

  EXCLUSION AUTHORITY, now stated rather than assumed:
    the 160 are excluded because NO current P09 claim is stated over the
    'references a P09 model' relation. If any future P09 claim IS stated over
    that relation, these 160 become its denominator and must be re-assessed.
""")

print("=== L-5 : WHAT THE 6 TEST FILES ASSERT ===")
print("  Stated before exclusion, per the exclusion-needs-authority rule.\n")
for t in sorted(tests):
    p = os.path.join(R, t)
    try: src = open(p, encoding="utf-8", errors="replace").read()
    except Exception: continue
    cls = re.findall(r"^class\s+(\w+)", src, re.M)
    defs = [d for d in re.findall(r"^\s+def\s+(test_\w+)", src, re.M)]
    doc = re.search(r'"""(.{0,160}?)"""', src, re.S)
    print("  %s" % t)
    print("    classes: %s" % (", ".join(cls[:3]) or "—"))
    print("    test methods (%d): %s" % (len(defs), ", ".join(defs[:6]) + (" …" if len(defs) > 6 else "")))
    if doc: print("    docstring: %s" % " ".join(doc.group(1).split())[:150])
    print()
