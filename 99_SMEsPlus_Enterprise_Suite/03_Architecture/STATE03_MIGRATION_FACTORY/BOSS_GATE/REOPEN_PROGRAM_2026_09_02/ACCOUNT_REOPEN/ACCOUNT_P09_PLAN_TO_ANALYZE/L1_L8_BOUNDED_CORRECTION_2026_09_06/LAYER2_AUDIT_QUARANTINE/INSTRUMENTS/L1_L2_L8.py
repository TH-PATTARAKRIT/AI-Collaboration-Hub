#!/usr/bin/env python3
"""
L-1  K-2 materiality re-run with a TABLE-NAME predicate + its own positive control
L-2  control tables for BOTH K-2 and K-3 (every filter carries its own controls)
L-8  K-3 declaration-stripping on an AST basis, replacing the line-based strip

DECLARED BEFORE RESULTS
  UNIT           : the file
  DENOMINATOR    : K-2 = files reaching a P09 TABLE by raw SQL
                   K-3 = files REFERENCING a P09 MODEL without declaring/inheriting it
  SOURCE ROOT    : the already-declared root (unchanged, not widened)
  INCLUSION RULE : K-2 -> SQL context keyword + P09 table name
                   K-3 -> P09 model literal surviving an AST declaration strip
  EXCLUSION RULE : files inside the K-1 population reported separately
  BLIND SPOTS    : non-source carriers; dynamically built table/model names
"""
import ast, os, re, json

R = "/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons"
S = os.path.dirname(os.path.abspath(__file__))   # the package itself — no ephemeral locator
_K1 = json.load(open(S + "/k1_population.json"))
POP = set(_K1["files"])
# ELIGIBILITY (added): a string literal counts as a P09 model only if it is a model
# actually DECLARED in the root. This rejects dotted FIELD PATHS such as
# "account.analytic.account.id", which the bare regex admitted.
DECLARED = set()
for _f,(_o,_e) in _K1["files"].items():
    DECLARED |= set(_o) | set(_e)

P09_TABLES = ["account_analytic_line","account_analytic_account","account_analytic_plan",
              "account_analytic_applicability","account_analytic_distribution_model",
              "budget_line","budget_analytic","budget_report","budget_split_wizard",
              "account_report_budget","account_report_budget_item"]
PLANNING_TABLES = {"budget_line","budget_analytic","budget_report","budget_split_wizard",
                   "account_report_budget","account_report_budget_item"}
PLANNING_MODELS_PREFIX = ("budget.", "account.report.budget")

SQL_CTX = re.compile(r"\b(FROM|JOIN|INTO|UPDATE|TABLE|EXISTS)\s+[\"']?(" + "|".join(P09_TABLES) + r")\b", re.I)
MODEL_RE = re.compile(r"['\"](analytic\.mixin|analytic\.plan\.fields\.mixin|account\.analytic\.[a-z.]+|budget\.[a-z.]+|account\.report\.budget[a-z.]*)['\"]")

def planning_by_table(tables): return any(t in PLANNING_TABLES for t in tables)
def planning_by_model(models): return any(m.startswith(PLANNING_MODELS_PREFIX) for m in models)

def strip_declarations_ast(src):
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    lines = src.splitlines(); kill = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name) and t.id in ("_name", "_inherit", "_inherits"):
                    for ln in range(n.lineno, (n.end_lineno or n.lineno) + 1):
                        kill.add(ln)
    return "\n".join("" if i + 1 in kill else l for i, l in enumerate(lines))

sql_hits, ref_hits, unparseable = {}, {}, []
_decl_witness = {}   # file -> (models before strip, models after strip)
_lb_hits = {}        # line-based strip results, for the executed comparison
for dp, dn, fn in os.walk(R):
    dn[:] = [d for d in dn if d != "__pycache__"]
    for f in fn:
        if not f.endswith(".py"): continue
        p = os.path.join(dp, f); rel = os.path.relpath(p, R)
        try: t = open(p, encoding="utf-8", errors="replace").read()
        except Exception: continue
        m = SQL_CTX.findall(t)
        if m: sql_hits[rel] = sorted({x[1].lower() for x in m})
        _lb = re.sub(r"^\s*_(name|inherit|inherits)\s*=.*$", "", t, flags=re.M)   # the LINE-BASED strip, executed
        _lbr = [x for x in MODEL_RE.findall(_lb) if x in DECLARED]
        if _lbr: _lb_hits[rel] = sorted(set(_lbr))
        body = strip_declarations_ast(t)
        if body is None:
            unparseable.append(rel); continue
        r = [x for x in MODEL_RE.findall(body) if x in DECLARED]
        _bef = {x for x in MODEL_RE.findall(t) if x in DECLARED}
        if _bef: _decl_witness[rel] = (_bef, set(r))
        if r: ref_hits[rel] = sorted(set(r))

print("=== L-2 : K-2 CONTROL TABLE ===")
KP = "account_reports/models/account_report.py"
KF = "hr_timesheet/models/hr_employee.py"
c1 = KP in sql_hits and planning_by_table(sql_hits.get(KP, []))
c2 = KF in sql_hits and not planning_by_table(sql_hits.get(KF, []))
c3 = not planning_by_table(["account_analytic_line"])
c4 = planning_by_table(["account_report_budget"])
print("  POSITIVE  known planning-SQL file -> planning            : %s" % ("HOLDS" if c1 else "*** FAILS ***"))
print("  NEGATIVE  known fact-only file -> NOT planning           : %s" % ("HOLDS" if c2 else "*** FAILS ***"))
print("  NEGATIVE  fact table alone is not planning               : %s" % ("HOLDS" if c3 else "*** FAILS ***"))
print("  POSITIVE  predicate fires on the string that broke it    : %s" % ("HOLDS" if c4 else "*** FAILS ***"))
k2_ok = c1 and c2 and c3 and c4
print("  K-2 CLASSIFIER: %s" % ("ACCEPTED" if k2_ok else "REJECTED — result is not evidence"))

sql_out = {k: v for k, v in sql_hits.items() if k not in POP}
sql_plan = {k: v for k, v in sql_out.items() if planning_by_table(v)}
print("\n=== L-1 : K-2 MATERIALITY RE-RUN (table-name predicate) ===")
print("  DENOMINATOR: outside the K-1 population = %d files" % len(sql_out))
print("  touching a PLANNING table : %d   (previously published as 0)" % len(sql_plan))
for k, v in sorted(sql_plan.items()):
    print("     %-58s %s" % (k, ",".join(v)))
print("  touching ONLY the fact table: %d" % (len(sql_out) - len(sql_plan)))

print("\n=== L-2 : K-3 CONTROL TABLE ===")
KPOS = "account_budget/models/purchase_order_line.py"
KNEG = "account_budget/models/budget_analytic.py"
d1 = KPOS in ref_hits and planning_by_model(ref_hits.get(KPOS, []))
# RE-SPECIFIED (the first d2 asserted a property the instrument never claims).
# Correct assertion: a DECLARATION STATEMENT must not survive the strip.
# Witness: a file whose ONLY P09 occurrences are declarations.
# NEGATIVE CONTROL, third specification. History kept deliberately:
#   v1 asserted "a file's own declaration is not a reference" -> tested a property
#      the instrument never claims. FAILED for the right reason.
#   v2 drew its witness from the set defined by the property -> could not fail.
#   v3 (this) selects the witness INDEPENDENTLY (first owning file in the K-1
#      population, chosen by declaration) and asserts the only thing the strip
#      actually claims: the DECLARATION STATEMENT's text is removed. A file may
#      legitimately reference its own model elsewhere; that is not a defect.
_owning = sorted(_K1["owning"])
KNEG2 = _owning[0] if _owning else None
_src2 = open(os.path.join(R, KNEG2), encoding="utf-8", errors="replace").read() if KNEG2 else ""
_strip2 = strip_declarations_ast(_src2) or ""
_decl_stmts = re.findall(r"^\s*_(?:name|inherit|inherits)\s*=.*$", _src2, re.M)
d2 = bool(_decl_stmts) and all(s.strip() not in _strip2 for s in _decl_stmts)
_pure = [f for f,(bef,aft) in _decl_witness.items() if bef and not aft]
d3 = planning_by_model(["budget.line"])
d4 = not planning_by_model(["account.analytic.line"])
print("  POSITIVE  known planning-reference file -> planning      : %s" % ("HOLDS" if d1 else "*** FAILS ***"))
print("  NEGATIVE  declaration STATEMENTS removed from the source  : %s   (witness %s, %d statements)" % ("HOLDS" if d2 else "*** FAILS ***", KNEG2, len(_decl_stmts)))
print("  POSITIVE  model-namespace predicate fires                : %s" % ("HOLDS" if d3 else "*** FAILS ***"))
print("  NEGATIVE  fact model alone is not planning               : %s" % ("HOLDS" if d4 else "*** FAILS ***"))
# failure control, now ASSERTED: a declare+reference file keeps its reference and loses its declaration
_b,_a = _decl_witness.get(KNEG,(set(),set()))
d5 = bool(_a) and _a <= _b
print("  FAILURE   declare+reference file keeps only its reference : %s" % ("HOLDS" if d5 else "*** FAILS ***"))
k3_ok = d1 and d2 and d3 and d4 and d5
print("  K-3 CLASSIFIER: %s" % ("ACCEPTED" if k3_ok else "REJECTED"))

_lb_out = {k: v for k, v in _lb_hits.items() if k not in POP}
_lb_plan = {k: v for k, v in _lb_out.items() if planning_by_model(v)}
ref_out = {k: v for k, v in ref_hits.items() if k not in POP}
ref_plan = {k: v for k, v in ref_out.items() if planning_by_model(v)}
tests = [k for k in ref_plan if "/tests/" in k or "/test_" in k]
print("\n=== L-8 : K-3 RE-RUN WITH AST DECLARATION-STRIPPING ===")
print("  unparseable files: %d" % len(unparseable))
print("  outside the population : %d files / %d modules" % (len(ref_out), len(set(k.split('/')[0] for k in ref_out))))
print("  line-based strip, EXECUTED for comparison : %d files / %d modules" % (len(_lb_out), len(set(k.split('/')[0] for k in _lb_out))))
print("  touching a planning model: %d" % len(ref_plan))
print("  line-based planning      : %d   -> %s" % (len(_lb_plan), "IDENTICAL" if (len(_lb_out)==len(ref_out) and len(_lb_plan)==len(ref_plan)) else "DIFFERS"))
print("    test files: %d   non-test: %d" % (len(tests), len(ref_plan) - len(tests)))
for k in sorted(ref_plan):
    print("      %-58s %s%s" % (k, ",".join(ref_plan[k]), "   [TEST]" if k in tests else ""))
print("\n  NON-PLANNING K-3 residue (the L-4 population): %d files" % (len(ref_out) - len(ref_plan)))

json.dump({"line_based_out": len(_lb_out), "line_based_plan": len(_lb_plan), "sql_out": sql_out, "sql_plan": sorted(sql_plan), "ref_out": ref_out,
           "ref_plan": sorted(ref_plan), "tests": sorted(tests),
           "k2_controls_ok": k2_ok, "k3_controls_ok": k3_ok},
          open(S + "/L_results.json", "w"), indent=1)
