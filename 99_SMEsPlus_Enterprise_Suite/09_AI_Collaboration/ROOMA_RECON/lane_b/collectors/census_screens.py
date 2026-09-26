#!/usr/bin/env python3
"""
LANE B CENSUS - SCREEN CAPTURE  V1.00
One command. Logs in as the observer, walks the menu rows, screenshots each
screen and dumps the text that is actually on it.

Lane B's agent does NOT need to invent browser commands for this - that is
mechanical work and belongs in a script. The agent's job starts afterwards:
reading these outputs and writing the census records.

Usage:  python3 collectors/census_screens.py [START] [COUNT]
        default: first 10 leaf menus

Records what is on the screen. Attributes NOTHING to a module - one screen is
composed of several modules and that attribution would require reading source.
"""
import os, sys, csv, json, re, datetime

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(W, "batches", "W1-SCREENS")
SHOTS = os.path.join(OUT, "screens")
RAW = os.path.join(OUT, "raw")
for d in (SHOTS, RAW):
    os.makedirs(d, exist_ok=True)

START = int(sys.argv[1]) if len(sys.argv) > 1 else 0
COUNT = int(sys.argv[2]) if len(sys.argv) > 2 else 10

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("ABORT: playwright is not installed for this python.\n"
             f"  fix:  {sys.executable} -m pip install playwright\n"
             f"        {sys.executable} -m playwright install chromium\n"
             "  Nothing was changed.")

env = {}
_CRED = os.path.join(W, "credentials/roomb_census.env")          # BOSSDEC-003 A: census account
if not os.path.exists(_CRED):
    _CRED = os.path.join(W, "credentials/roomb_observer.env")
    print("WARNING: roomb_census.env not found - falling back to roomb_observer (narrow reach)")
print(f"account    {os.path.basename(_CRED)}")
for line in open(_CRED):
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1); env[k.strip()] = v.strip()
URL, DB, USER, PWD = env["ODOO_URL"], env["ODOO_DB"], env["ODOO_USER"], env["ODOO_PASSWORD"]

tsv = os.path.join(OUT, "MENU_TREE.tsv")
if not os.path.exists(tsv):
    sys.exit(f"ABORT: {tsv} not found - run collectors/census_menu_tree.py first")
with open(tsv, encoding="utf-8") as f:
    rows = [r for r in csv.DictReader(f, delimiter="\t") if r["is_leaf"] == "1" and r["opens"]]
todo = rows[START:START + COUNT]
# BOSSDEC-003 C + D (Boss, 26 Sep 2026): these root sections are not walked by Lane B.
# Settings needs Role/Administrator (excluded from the UI census - feature switches come from S2
# metadata); Website / eLearning / Live Chat / Link Tracker are NEXT PHASE sections.
EXCLUDED_ROOT = {"Settings": "BOSSDEC-003 D", "Website": "BOSSDEC-003 C", "eLearning": "BOSSDEC-003 C",
                 "Live Chat": "BOSSDEC-003 C", "Link Tracker": "BOSSDEC-003 C"}
def excluded_reason(path):
    return EXCLUDED_ROOT.get(path.split(" / ")[0])
print(f"menu rows  {len(rows)} leaf screens total, doing {START}..{START+len(todo)-1}")

def texts(page, sel, limit=60):
    out = []
    for el in page.query_selector_all(sel)[:limit]:
        try:
            t = (el.inner_text() or "").strip().replace("\n", " ")
        except Exception:
            continue
        t = re.sub(r"\s+", " ", t)
        if t and len(t) < 80 and t not in out:
            out.append(t)
    return out

results = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1600, "height": 1000}, locale="en-US")
    page = ctx.new_page()

    page.goto(f"{URL}/web/login", wait_until="domcontentloaded", timeout=60000)
    page.fill("input[name='login']", USER)
    page.fill("input[name='password']", PWD)
    page.click("button[type='submit']")
    page.wait_for_load_state("networkidle", timeout=60000)
    if "/web/login" in page.url:
        browser.close()
        sys.exit("ABORT: login failed for the observer account. Nothing captured.")
    print(f"logged in  {USER}")

    for i, r in enumerate(todo, 1):
        mid, path, opens = r["menu_id"], r["path"], r["opens"]
        act = opens.split(",")[-1] if "," in opens else ""
        rec = {"MENU_ID": int(mid), "MENU_PATH": path, "OPENS": opens,
               "CAPTURED_AT": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        why = excluded_reason(path)
        if why:
            rec.update({"REACHED": "excluded", "SCREENSHOT": "",
                        "NOTE": f"EXCLUDED - root section not walked by Lane B ({why})"})
            print(f"  {i:>3}/{len(todo)}  excl.   {path[:60]}   ({why})")
            results.append(rec)
            json.dump(rec, open(os.path.join(RAW, f"{mid}.json"), "w"), indent=2, ensure_ascii=False)
            continue
        try:
            page.goto(f"{URL}/odoo/action-{act}", wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(2500)
            if page.query_selector(".o_action_manager .o_nocontent_help, .o_list_view, .o_kanban_view, .o_form_view, .o_content"):
                pass
            shot = os.path.join(SHOTS, f"{mid}.png")
            page.screenshot(path=shot, full_page=False)
            rec.update({
                "REACHED": "yes",
                "SCREENSHOT": f"screens/{mid}.png",
                "URL_AFTER_LOAD": page.url,
                "TITLE_ON_SCREEN": (page.query_selector(".o_breadcrumb, .o_control_panel .o_breadcrumb, h1") or
                                    page).inner_text().strip().split("\n")[0][:120],
                "VIEW_SWITCHERS": texts(page, ".o_cp_switch_buttons button, .o_switch_view"),
                "BUTTONS": texts(page, ".o_control_panel button, .o_cp_buttons button, button.btn-primary, button.btn-secondary"),
                "FILTERS": texts(page, ".o_search_options .dropdown-item, .o_facet_value, .o_searchview_facet"),
                "COLUMNS_OR_FIELDS": texts(page, "table.o_list_table thead th, .o_form_label, .o_kanban_record .o_field_widget"),
                "RECORD_COUNT": ((page.query_selector(".o_pager_counter, .o_pager") or None) and
                                 page.query_selector(".o_pager_counter, .o_pager").inner_text().strip()) or "not shown",
            })
            print(f"  {i:>3}/{len(todo)}  ok      {path[:70]}")
        except Exception as e:
            rec.update({"REACHED": "no", "SCREENSHOT": "",
                        "NOTE": f"{type(e).__name__}: {str(e).splitlines()[0][:150]}"})
            print(f"  {i:>3}/{len(todo)}  FAILED  {path[:60]}")
        results.append(rec)
        json.dump(rec, open(os.path.join(RAW, f"{mid}.json"), "w"), indent=2, ensure_ascii=False)

    browser.close()

out = os.path.join(OUT, f"SCREEN_RAW_{START}_{START+len(todo)}.json")
json.dump({"collected_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "range": [START, START + len(todo)], "total_leaf_screens": len(rows),
           "reached": sum(1 for r in results if r.get("REACHED") == "yes"),
           "not_reached": sum(1 for r in results if r.get("REACHED") == "no"),
           "excluded": sum(1 for r in results if r.get("REACHED") == "excluded"),
           "excluded_rule": "BOSSDEC-003 C (Website, eLearning, Live Chat, Link Tracker) + D (Settings)",
           "note": "No element is attributed to a module. One screen is composed of "
                   "several modules and that attribution would require reading source.",
           "screens": results}, open(out, "w"), indent=2, ensure_ascii=False)

print(f"\nreached    {sum(1 for r in results if r.get('REACHED')=='yes')} / {len(todo)}")
print(f"shots      {SHOTS}")
print(f"written    {out}")
