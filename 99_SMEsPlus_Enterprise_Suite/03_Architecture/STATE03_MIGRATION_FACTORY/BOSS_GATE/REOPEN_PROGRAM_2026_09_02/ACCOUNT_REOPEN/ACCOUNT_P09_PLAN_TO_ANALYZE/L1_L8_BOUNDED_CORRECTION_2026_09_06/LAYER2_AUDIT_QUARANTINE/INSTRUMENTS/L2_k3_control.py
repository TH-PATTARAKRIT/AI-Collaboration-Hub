#!/usr/bin/env python3
"""
L-2 — K-3 control table, RE-SPECIFIED.

The first attempt asserted "a file's own declaration is not counted as a
reference" and chose a witness that ALSO references the model legitimately
elsewhere (self-referencing revision links). That control tested a claim the
instrument never makes. It failed for the right reason: it was wrong.

Correct assertion: the DECLARATION STATEMENT ITSELF must not survive the strip.
Witness: a file whose ONLY occurrences of a P09 model are its declarations.
"""
import ast, os, re, json

R = "/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons"
MODEL_RE = re.compile(r"['\"](analytic\.mixin|analytic\.plan\.fields\.mixin|account\.analytic\.[a-z.]+|budget\.[a-z.]+|account\.report\.budget[a-z.]*)['\"]")

def strip_declarations_ast(src):
    tree = ast.parse(src); lines = src.splitlines(); kill = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name) and t.id in ("_name","_inherit","_inherits"):
                    for ln in range(n.lineno, (n.end_lineno or n.lineno)+1): kill.add(ln)
    return "\n".join("" if i+1 in kill else l for i,l in enumerate(lines))

# find witnesses: files where every P09 occurrence lies inside a declaration
pure, mixed = [], []
for dp, dn, fn in os.walk(R):
    dn[:] = [d for d in dn if d != "__pycache__"]
    for f in fn:
        if not f.endswith(".py"): continue
        p = os.path.join(dp, f); rel = os.path.relpath(p, R)
        try: src = open(p, encoding="utf-8", errors="replace").read()
        except Exception: continue
        if not MODEL_RE.search(src): continue
        try: stripped = strip_declarations_ast(src)
        except SyntaxError: continue
        before = set(MODEL_RE.findall(src)); after = set(MODEL_RE.findall(stripped))
        if before and not after: pure.append(rel)
        elif before != after: mixed.append(rel)

print("=== L-2 : K-3 CONTROL TABLE, RE-SPECIFIED ===")
print("  witnesses whose ONLY P09 occurrences are declarations : %d" % len(pure))
print("  witnesses with declarations AND other references      : %d" % len(mixed))
w = sorted(pure)[0] if pure else None
print("\n  NEGATIVE control witness: %s" % w)
if w:
    src = open(os.path.join(R, w), encoding="utf-8", errors="replace").read()
    print("    P09 models before strip : %s" % sorted(set(MODEL_RE.findall(src))))
    print("    P09 models after  strip : %s" % sorted(set(MODEL_RE.findall(strip_declarations_ast(src)))))
    ok_neg = not MODEL_RE.findall(strip_declarations_ast(src))
else:
    ok_neg = False
print("    NEGATIVE  declaration statements do not survive the strip : %s" % ("HOLDS" if ok_neg else "*** FAILS ***"))

# positive: a file that references without declaring
POS = "account_budget/models/purchase_order_line.py"
src = open(os.path.join(R, POS), encoding="utf-8", errors="replace").read()
after = set(MODEL_RE.findall(strip_declarations_ast(src)))
ok_pos = any(m.startswith(("budget.","account.report.budget")) for m in after)
print("    POSITIVE  a pure reference survives the strip             : %s  %s"
      % ("HOLDS" if ok_pos else "*** FAILS ***", sorted(after)))

# failure control: a declaring file that also references -> must keep ONLY the reference
MIX = "account_budget/models/budget_analytic.py"
src = open(os.path.join(R, MIX), encoding="utf-8", errors="replace").read()
b = set(MODEL_RE.findall(src)); a = set(MODEL_RE.findall(strip_declarations_ast(src)))
print("    FAILURE   a declare+reference file keeps only its reference: before=%s after=%s" % (sorted(b), sorted(a)))
print("              (this file is INSIDE the K-1 population, so it never entered the K-3 residue)")
print("\n  K-3 CLASSIFIER: %s" % ("ACCEPTED" if (ok_neg and ok_pos) else "REJECTED"))
