#!/usr/bin/env python3
"""
Apply the BOSSDEC-003 edits to the two census collectors, exactly and verifiably (RED TEAM, 26 Sep 2026).
Run on the Mac:  python3 ~/ROOMB_WORKSPACE/ops/apply_census_script_edits_v1.01.py
Re-runnable: a replacement whose target text is already gone is reported as 'already applied'.
Each original is preserved first as _superseded/<name>_V1.00_pre-BOSSDEC-003.py (never overwritten).

Edit 1 (both collectors)   - use credentials/roomb_census.env when it exists (two-account model, BOSSDEC-003 A);
                             fall back to roomb_observer.env and SAY SO. Never silently.
Edit 2 (census_screens.py) - deterministic scope gate: leaf rows under Settings (BOSSDEC-003 D) and the
                             deferred sections Website / eLearning / Live Chat / Link Tracker (BOSSDEC-003 C)
                             are NOT navigated; recorded as REACHED: excluded with the decision reference.
"""
import os, re, sys, shutil, hashlib

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUP = os.path.join(W, "_superseded")
os.makedirs(SUP, exist_ok=True)

CRED_OLD = 'for line in open(os.path.join(W, "credentials/roomb_observer.env")):'
CRED_NEW = ('_CRED = os.path.join(W, "credentials/roomb_census.env")          # BOSSDEC-003 A: census account\n'
            'if not os.path.exists(_CRED):\n'
            '    _CRED = os.path.join(W, "credentials/roomb_observer.env")\n'
            '    print("WARNING: roomb_census.env not found - falling back to roomb_observer (narrow reach)")\n'
            'print(f"account    {os.path.basename(_CRED)}")\n'
            'for line in open(_CRED):')

SCOPE_OLD = 'todo = rows[START:START + COUNT]'
SCOPE_NEW = ('todo = rows[START:START + COUNT]\n'
             '# BOSSDEC-003 C + D (Boss, 26 Sep 2026): these root sections are not walked by Lane B.\n'
             '# Settings needs Role/Administrator (excluded from the UI census - feature switches come from S2\n'
             '# metadata); Website / eLearning / Live Chat / Link Tracker are NEXT PHASE sections.\n'
             'EXCLUDED_ROOT = {"Settings": "BOSSDEC-003 D", "Website": "BOSSDEC-003 C", "eLearning": "BOSSDEC-003 C",\n'
             '                 "Live Chat": "BOSSDEC-003 C", "Link Tracker": "BOSSDEC-003 C"}\n'
             'def excluded_reason(path):\n'
             '    return EXCLUDED_ROOT.get(path.split(" / ")[0])')

LOOP_OLD = ('        rec = {"MENU_ID": int(mid), "MENU_PATH": path, "OPENS": opens,\n'
            '               "CAPTURED_AT": datetime.datetime.now(datetime.timezone.utc).isoformat()}\n'
            '        try:\n')
LOOP_NEW = ('        rec = {"MENU_ID": int(mid), "MENU_PATH": path, "OPENS": opens,\n'
            '               "CAPTURED_AT": datetime.datetime.now(datetime.timezone.utc).isoformat()}\n'
            '        why = excluded_reason(path)\n'
            '        if why:\n'
            '            rec.update({"REACHED": "excluded", "SCREENSHOT": "",\n'
            '                        "NOTE": f"EXCLUDED - root section not walked by Lane B ({why})"})\n'
            '            print(f"  {i:>3}/{len(todo)}  excl.   {path[:60]}   ({why})")\n'
            '            results.append(rec)\n'
            '            json.dump(rec, open(os.path.join(RAW, f"{mid}.json"), "w"), indent=2, ensure_ascii=False)\n'
            '            continue\n'
            '        try:\n')

SUMMARY_OLD = ('           "not_reached": sum(1 for r in results if r.get("REACHED") == "no"),\n')
SUMMARY_NEW = ('           "not_reached": sum(1 for r in results if r.get("REACHED") == "no"),\n'
               '           "excluded": sum(1 for r in results if r.get("REACHED") == "excluded"),\n'
               '           "excluded_rule": "BOSSDEC-003 C (Website, eLearning, Live Chat, Link Tracker) + D (Settings)",\n')

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]

def apply(name, edits):
    p = os.path.join(W, "collectors", name)
    src = open(p, encoding="utf-8").read()
    keep = os.path.join(SUP, name.replace(".py", "_V1.00_pre-BOSSDEC-003.py"))
    if not os.path.exists(keep):
        shutil.copy2(p, keep); print(f"preserved  {os.path.relpath(keep, W)}  sha256 {sha(keep)}")
    changed = 0
    for label, old, new, marker in edits:
        if marker in src:
            print(f"  {label}: already applied"); continue
        n = src.count(old)
        if n != 1:
            print(f"  {label}: ABORT - target text found {n} time(s), expected 1. File untouched."); return False
        src = src.replace(old, new); changed += 1; print(f"  {label}: applied")
    if changed:
        open(p, "w", encoding="utf-8").write(src)
    print(f"{name}: {changed} edit(s) written  sha256 now {sha(p)}")
    return True

ok = True
print("census_menu_tree.py")
ok &= apply("census_menu_tree.py", [("edit1 credentials", CRED_OLD, CRED_NEW, "roomb_census.env")])
print("census_screens.py")
ok &= apply("census_screens.py", [("edit1 credentials", CRED_OLD, CRED_NEW, "roomb_census.env"),
                                  ("edit2 scope gate", SCOPE_OLD, SCOPE_NEW, "EXCLUDED_ROOT = {"),
                                  ("edit2 loop", LOOP_OLD, LOOP_NEW, "why = excluded_reason(path)"),
                                  ("edit2 summary", SUMMARY_OLD, SUMMARY_NEW, '"excluded_rule":')])
for name in ("census_menu_tree.py", "census_screens.py"):
    import py_compile
    py_compile.compile(os.path.join(W, "collectors", name), doraise=True); print(f"syntax ok  {name}")
sys.exit(0 if ok else 1)
