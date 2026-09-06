#!/usr/bin/env python3
"""
K-1 — P09 population instrument v5, rebuilt from scratch (NOT copied forward).

UNIT (explicit): the FILE. A file is counted once regardless of how many P09
models it declares or extends.

INSTRUMENT: parse each source file with Python's own AST, so that
  - list position is irrelevant (D3),
  - multi-line lists are handled natively,
  - `comodel_name=` cannot be mistaken for `_name =` (D1) because a keyword
    argument is a different AST node from a class-body assignment.

OWNERSHIP RULE: a file OWNS a model iff, in one class body, it assigns
_name = <P09 model> and does NOT also inherit that same model (D2).

CONTROLS — the instrument is rejected unless every one passes.
"""
import ast, os, sys, json

R = "/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons"
SEED_PREFIX = ("account.analytic.", "budget.", "account.report.budget")
SEED_EXACT  = {"analytic.mixin", "analytic.plan.fields.mixin"}

def is_p09(name):
    return name in SEED_EXACT or name.startswith(SEED_PREFIX)

def literals(node):
    """Every string literal in a value node, whether scalar or list."""
    out = []
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        out.append(node.value)
    elif isinstance(node, (ast.List, ast.Tuple)):
        for e in node.elts:
            out += literals(e)
    return out

def scan(path):
    """Return (owns, extends) sets of P09 model names for one file."""
    try:
        tree = ast.parse(open(path, encoding="utf-8", errors="replace").read())
    except SyntaxError:
        return None  # unparseable — reported separately, never silently dropped
    owns, ext = set(), set()
    for cls in [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]:
        names, inhs = set(), set()
        for stmt in cls.body:
            if not isinstance(stmt, ast.Assign):
                continue
            for t in stmt.targets:
                if not isinstance(t, ast.Name):
                    continue
                if t.id == "_name":
                    names |= {l for l in literals(stmt.value) if is_p09(l)}
                elif t.id in ("_inherit", "_inherits"):
                    inhs |= {l for l in literals(stmt.value) if is_p09(l)}
        owns |= (names - inhs)          # D2: declare-and-inherit == extension
        ext  |= inhs | (names & inhs)
    return owns, ext

files, unparseable = {}, []
scanned = 0
for dp, dn, fn in os.walk(R):
    dn[:] = [d for d in dn if d != "__pycache__"]
    for f in fn:
        if not f.endswith(".py"):
            continue
        p = os.path.join(dp, f)
        scanned += 1
        r = scan(p)
        if r is None:
            unparseable.append(os.path.relpath(p, R)); continue
        owns, ext = r
        if owns or ext:
            files[os.path.relpath(p, R)] = (sorted(owns), sorted(ext))

owning = {f: v for f, v in files.items() if v[0]}
extending = {f: v for f, v in files.items() if not v[0]}

print("=== K-1 INSTRUMENT v5 (AST) ===")
print("UNIT: the file.  Root: the already-declared root.  No new root.")
print("source files parsed : %d" % scanned)
print("UNPARSEABLE         : %d  <- must be 0 or individually dispositioned" % len(unparseable))
for u in unparseable[:10]:
    print("    " + u)

print("\n--- POSITIVE CONTROLS (instrument must SEE each) ---")
pos = {
    "the plan header file"            : "account_budget/models/budget_analytic.py",
    "the fact-table declaring file"   : "analytic/models/analytic_line.py",
    "the second planning family"      : "account_reports/models/budget.py",
    "non-first list position #1"      : "account_asset/models/account_asset.py",
    "non-first list position #2"      : "hr_expense/models/hr_expense.py",
    "non-first list position #3"      : "mrp_account/models/mrp_workcenter.py",
    "MULTI-LINE list"                 : "project/models/project_project.py",
    "declare+inherit (must EXTEND)"   : "timesheet_grid/models/analytic.py",
}
ok = True
for label, path in pos.items():
    seen = path in files
    cls = "OWNS" if path in owning else ("EXTENDS" if path in extending else "—")
    if label.startswith("declare+inherit"):
        good = seen and path in extending
    elif label in ("the plan header file", "the fact-table declaring file", "the second planning family"):
        good = seen and path in owning
    else:
        good = seen
    ok &= good
    print("  %-32s %-9s %s" % (label, cls, "HOLDS" if good else "*** FAILED ***"))

print("\n--- NEGATIVE CONTROL (instrument must NOT see) ---")
neg = "account_reports/models/account.py"   # only a comodel_name= reference
ncls = "OWNS" if neg in owning else ("EXTENDS" if neg in extending else "absent")
ngood = neg not in owning
ok &= ngood
print("  comodel_name-only reference      %-9s %s" % (ncls, "HOLDS (not counted as a declaration)" if ngood else "*** FAILED ***"))

print("\n--- RESULT ---")
print("  INSTRUMENT: %s" % ("ACCEPTED" if ok else "REJECTED — count is NOT evidence"))
print("  population : %d files / %d modules" % (len(files), len(set(f.split('/')[0] for f in files))))
print("  OWNING     : %d files / %d modules  %s" % (
    len(owning), len(set(f.split('/')[0] for f in owning)),
    sorted(set(f.split('/')[0] for f in owning))))
print("  EXTENDING  : %d files / %d modules" % (len(extending), len(set(f.split('/')[0] for f in extending))))

S = "/private/tmp/claude-501/-Volumes-iMacSys-SMEsPlus-ENTERPRISE-SUITE/65b32750-dad1-47c5-99a2-7eb7ad31f2a2/scratchpad"
json.dump({"files": files, "owning": list(owning), "extending": list(extending)},
          open(S + "/k1_population.json", "w"), indent=1)

print("\n--- per-model extension counts (unit = file) ---")
from collections import Counter
c = Counter()
for f, (o, e) in files.items():
    for m in set(e):
        c[m] += 1
for m, n in sorted(c.items(), key=lambda x: -x[1]):
    print("  %-42s %d" % (m, n))
