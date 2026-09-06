#!/usr/bin/env python3
"""
K-2 raw-SQL bounded pass and K-3 relational-reference bounded pass.
Declared root only. No widening. Each hit classified by whether it can
materially affect a P09 completeness or absence claim.
"""
import ast, os, re, json

R = "/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons"
S = "/private/tmp/claude-501/-Volumes-iMacSys-SMEsPlus-ENTERPRISE-SUITE/65b32750-dad1-47c5-99a2-7eb7ad31f2a2/scratchpad"
pop = json.load(open(S + "/k1_population.json"))
POP = set(pop["files"])

TABLES = ["account_analytic_line", "account_analytic_account", "account_analytic_plan",
          "account_analytic_applicability", "account_analytic_distribution_model",
          "budget_line", "budget_analytic", "budget_report",
          "account_report_budget", "account_report_budget_item"]
SQL_CTX = re.compile(r"\b(FROM|JOIN|INTO|UPDATE|TABLE|EXISTS)\s+[\"']?(" + "|".join(TABLES) + r")\b", re.I)

SEED_PREFIX = ("account.analytic.", "budget.", "account.report.budget")
SEED_EXACT = {"analytic.mixin", "analytic.plan.fields.mixin"}
def is_p09(n): return n in SEED_EXACT or n.startswith(SEED_PREFIX)

# K-3: a P09 model named as a STRING anywhere that is not a declaration/inheritance
REF = re.compile(r"['\"](" + "|".join([re.escape(x) for x in
        ["analytic.mixin", "analytic.plan.fields.mixin"]]) + r"|account\.analytic\.[a-z.]+|budget\.[a-z.]+|account\.report\.budget[a-z.]*)['\"]")

sql_hits, ref_hits = {}, {}
for dp, dn, fn in os.walk(R):
    dn[:] = [d for d in dn if d != "__pycache__"]
    for f in fn:
        if not f.endswith(".py"): continue
        p = os.path.join(dp, f); rel = os.path.relpath(p, R)
        try: t = open(p, encoding="utf-8", errors="replace").read()
        except Exception: continue
        m = SQL_CTX.findall(t)
        if m: sql_hits[rel] = sorted({x[1].lower() for x in m})
        # references: strip declaration/inheritance lines first
        body = re.sub(r"^\s*_(name|inherit|inherits)\s*=.*$", "", t, flags=re.M)
        r = REF.findall(body)
        if r: ref_hits[rel] = sorted(set(r))

def report(title, hits, floor):
    outside = {k: v for k, v in hits.items() if k not in POP}
    mods = sorted({k.split('/')[0] for k in outside})
    print("\n=== %s ===" % title)
    print("  total files hit        : %d" % len(hits))
    print("  OUTSIDE the population : %d files / %d modules   (prior floor: %s)"
          % (len(outside), len(mods), floor))
    return outside, mods

sql_out, sql_mods = report("K-2 RAW-SQL BOUNDED PASS", sql_hits, "12 files / 3 modules")
for k in sorted(sql_out):
    print("    %-62s %s" % (k, ",".join(sql_out[k])))
print("  modules absent from the population entirely: %s" %
      sorted(set(sql_mods) - {f.split('/')[0] for f in POP}))

ref_out, ref_mods = report("K-3 RELATIONAL-REFERENCE BOUNDED PASS", ref_hits, "164 files / 51 modules")
print("  modules absent from the population entirely: %d" %
      len(set(ref_mods) - {f.split('/')[0] for f in POP}))

# Materiality: does the hit reference a PLANNING model (the subject of the
# absence claims) or only the analytic dimension (already known to be estate-wide)?
PLAN = ("budget.", "account.report.budget")
def planning(v): return any(x.startswith(PLAN) for x in v)
print("\n--- MATERIALITY CLASSIFICATION ---")
for label, out in (("K-2 raw-SQL", sql_out), ("K-3 reference", ref_out)):
    mat = {k: v for k, v in out.items() if planning(v)}
    print("  %-14s outside-population hits touching a PLANNING model: %d" % (label, len(mat)))
    for k in sorted(mat): print("      %-58s %s" % (k, ",".join(mat[k])))
json.dump({"sql_outside": sql_out, "ref_outside": ref_out}, open(S + "/k2k3.json", "w"), indent=1)
