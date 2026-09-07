#!/usr/bin/env python3
"""
Q-P09-01 — resolve L-4's authority limb.

Re-test required by the queue row: "the residue AND the denominator, both
published with their populations."

DECLARED BEFORE RESULTS
  unit            : the file
  denominator     : every file in the declared root that REFERENCES a P09 model
                    without declaring or inheriting it  (the "reference relation")
  source root     : the already-declared root — UNCHANGED, not widened
  inclusion rule  : a string literal that is a model ACTUALLY DECLARED in the root,
                    surviving an AST declaration strip
  partition       : inside the K-1 population / outside it; then planning / non-planning
  blind spots     : non-source carriers; dynamically built model names
"""
import ast, os, re, json, collections

R = "/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons"
I = ("/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_P09_PLAN_TO_ANALYZE_2026_09_04_EXECUTION/"
     "99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/"
     "REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_P09_PLAN_TO_ANALYZE/"
     "L1_L8_BOUNDED_CORRECTION_2026_09_06/LAYER2_AUDIT_QUARANTINE/INSTRUMENTS")
K1 = json.load(open(I + "/k1_population.json"))
POP = set(K1["files"])
DECLARED = set()
for f, (o, e) in K1["files"].items():
    DECLARED |= set(o) | set(e)

MODEL_RE = re.compile(r"['\"](analytic\.mixin|analytic\.plan\.fields\.mixin|account\.analytic\.[a-z.]+|budget\.[a-z.]+|account\.report\.budget[a-z.]*)['\"]")
PLAN_PREFIX = ("budget.", "account.report.budget")

def strip_decl(src):
    try: tree = ast.parse(src)
    except SyntaxError: return None
    lines = src.splitlines(); kill = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name) and t.id in ("_name", "_inherit", "_inherits"):
                    for ln in range(n.lineno, (n.end_lineno or n.lineno) + 1): kill.add(ln)
    return "\n".join("" if i + 1 in kill else l for i, l in enumerate(lines))

refs = {}
for dp, dn, fn in os.walk(R):
    dn[:] = [d for d in dn if d != "__pycache__"]
    for f in fn:
        if not f.endswith(".py"): continue
        p = os.path.join(dp, f); rel = os.path.relpath(p, R)
        try: src = open(p, encoding="utf-8", errors="replace").read()
        except Exception: continue
        body = strip_decl(src)
        if body is None: continue
        hits = sorted({m for m in MODEL_RE.findall(body) if m in DECLARED})
        if hits: refs[rel] = hits

inside  = {k: v for k, v in refs.items() if k in POP}
outside = {k: v for k, v in refs.items() if k not in POP}
def planning(v): return any(m.startswith(PLAN_PREFIX) for m in v)
out_plan = {k: v for k, v in outside.items() if planning(v)}
out_non  = {k: v for k, v in outside.items() if not planning(v)}
tests    = {k for k in out_plan if "/tests/" in k or "/test_" in k}

def mods(d): return len({k.split('/')[0] for k in d})

print("=== THE DENOMINATOR — the reference relation, published in full ===")
print("  files referencing a P09 model, declaration/inheritance stripped : %3d  / %d modules" % (len(refs), mods(refs)))
print("    partition A — INSIDE the K-1 population                       : %3d  / %d modules" % (len(inside), mods(inside)))
print("    partition B — OUTSIDE the K-1 population                      : %3d  / %d modules" % (len(outside), mods(outside)))
print("  A + B = %d  (checks against the denominator: %s)" % (len(inside)+len(outside), len(inside)+len(outside) == len(refs)))

print("\n=== THE RESIDUE — partition B, split by subject ===")
print("    B1 — touching a PLANNING model                                : %3d  / %d modules" % (len(out_plan), mods(out_plan)))
print("         of which test files                                      : %3d" % len(tests))
print("         of which non-test                                        : %3d" % (len(out_plan)-len(tests)))
print("    B2 — touching only the ANALYTIC DIMENSION  (the 159)          : %3d  / %d modules" % (len(out_non), mods(out_non)))
print("  B1 + B2 = %d  (checks against partition B: %s)" % (len(out_plan)+len(out_non), len(out_plan)+len(out_non) == len(outside)))

print("\n=== B2 POPULATION — which models the 159 reference (unit = file) ===")
c = collections.Counter()
for v in out_non.values():
    for m in v: c[m] += 1
for m, n in c.most_common(): print("    %-40s %3d" % (m, n))

print("\n=== B2 MODULE POPULATION (top 12 of %d) ===" % mods(out_non))
mc = collections.Counter(k.split('/')[0] for k in out_non)
for m, n in mc.most_common(12): print("    %-40s %3d" % (m, n))

json.dump({"denominator": len(refs), "inside": len(inside), "outside": len(outside),
           "planning": len(out_plan), "tests": sorted(tests), "non_planning": len(out_non),
           "b2_files": sorted(out_non), "b2_models": dict(c), "b2_modules": dict(mc)},
          open(os.path.dirname(os.path.abspath(__file__)) + "/q1_results.json", "w"), indent=1)
