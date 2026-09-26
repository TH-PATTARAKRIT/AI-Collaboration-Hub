#!/usr/bin/env python3
"""
LANE B - STAGE 1a COLLECTOR  V2.00
SMEsPlus Enterprise Suite / ROOM A / batch W1-STD

Fixes over V1 (RED TEAM findings RT-LANEB-010..014):
  - self-test runs FIRST and ABORTS on failure (scoped to workspace, not '/')
  - installed-set hash verified BEFORE any collection
  - NO traceback is ever written to an artifact (source-leak containment)
  - writes only inside the observer's own company; no cross-company write attempt
  - test records are DELETED after observation and the deletion is verified
  - handles xmlrpc 'copy' returning a list
  - writes RECORD_SKELETON.yaml + MANIFEST.sha256 + BATCH_REPORT.md (V1 wrote none)
  - records NO conclusions - observation only
"""
import os, re, sys, ssl, json, hashlib, datetime, xmlrpc.client

WORKSPACE   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED_FILE   = os.path.join(WORKSPACE, "credentials/roomb_observer.env")
BATCH_ID    = "W1-STD"
BATCH_DIR   = os.path.join(WORKSPACE, "batches", BATCH_ID)
ART_DIR     = os.path.join(BATCH_DIR, "artifacts")
OBSERVER_COMPANY_ID = 2          # ROOMB_TEST - the ONLY company we may write in
INSTALLED_SET_EXPECTED = "706e6df4008e0bac042a9821507ec0bc6868c4d9f98bcb93004a2535b1ca3c89"

SOURCE_PAT = re.compile(r"(Traceback|site-packages|/opt/odoo|File \"/)", re.I)

def scrub(text):
    """Never let reference-implementation source reach a Lane B artifact."""
    if not isinstance(text, str):
        text = str(text)
    if not SOURCE_PAT.search(text):
        return text.strip().splitlines()[0][:400] if text.strip() else ""
    lines = [l for l in text.replace("\\n", "\n").splitlines() if l.strip()]
    last = lines[-1] if lines else ""
    last = re.sub(r"[\w/\.\-]*site-packages[\w/\.\-]*", "<REDACTED_PATH>", last)
    last = re.sub(r"/opt/[\w/\.\-]*", "<REDACTED_PATH>", last)
    return "SOURCE_SCRUBBED :: " + last.strip()[:400]

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while (c := f.read(65536)):
            h.update(c)
    return h.hexdigest()

# ---------------------------------------------------------------- self-test
def self_test():
    r = {"ts": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    hits = []
    for root, dirs, files in os.walk(WORKSPACE):
        if "__manifest__.py" in files:
            hits.append(os.path.join(root, "__manifest__.py"))
    r["t1_no_source_in_workspace"] = {"scanned": WORKSPACE, "hits": hits,
                                      "result": "PASS" if not hits else "FAIL"}
    r["t2_write_scope"] = {"only_company_id": OBSERVER_COMPANY_ID, "result": "DECLARED"}
    r["t3_baseline_expected"] = INSTALLED_SET_EXPECTED
    r["t4_tooling"] = {"note": "deterministic script; no MCP server, no connector, "
                               "no web search, no filesystem access outside workspace",
                       "result": "DECLARED"}
    return r

# ---------------------------------------------------------------- main
def main():
    os.makedirs(ART_DIR, exist_ok=True)
    st = self_test()
    if st["t1_no_source_in_workspace"]["result"] != "PASS":
        sys.exit("ABORT self-test 1: source manifests found inside the workspace:\n  " +
                 "\n  ".join(st["t1_no_source_in_workspace"]["hits"]))

    if not os.path.exists(CRED_FILE):
        sys.exit(f"ABORT: credentials not found at {CRED_FILE}")
    env = {}
    for line in open(CRED_FILE):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1); env[k.strip()] = v.strip()
    url = env.get("ODOO_URL"); db = env.get("ODOO_DB")
    usr = env.get("ODOO_USER"); pwd = env.get("ODOO_PASSWORD")
    if not all([url, db, usr, pwd]):
        sys.exit("ABORT: credential file incomplete")

    ctx = ssl.create_default_context()
    common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common", context=ctx)
    uid = common.authenticate(db, usr, pwd, {})
    if not uid:
        sys.exit(f"ABORT: authentication failed for {usr}")
    models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object", context=ctx)
    print(f"connected  {url} ({db}) uid={uid}")

    def call(model, method, args, kw=None):
        """Every server call goes through here. Errors are scrubbed, never raised."""
        try:
            return {"status": "ok", "value": models.execute_kw(db, uid, pwd, model, method, args, kw or {})}
        except Exception as e:
            raw = getattr(e, "faultString", None) or str(e)
            return {"status": "refused", "message": scrub(raw)}

    # --- baseline verification BEFORE collecting -------------------------
    mods = call("ir.module.module", "search_read",
                [[["state", "=", "installed"]]], {"fields": ["name"]})
    if mods["status"] != "ok":
        sys.exit("ABORT: cannot read installed module set: " + mods["message"])
    names = sorted(m["name"] for m in mods["value"])
    got = hashlib.sha256(("\n".join(names) + "\n").encode()).hexdigest()
    st["t3_baseline_actual"] = got
    st["t3_result"] = "PASS" if got == INSTALLED_SET_EXPECTED else "FAIL"
    print(f"baseline   {st['t3_result']}  ({len(names)} modules)")
    if st["t3_result"] != "PASS":
        sys.exit(f"ABORT self-test 3: installed-set hash moved\n  expected {INSTALLED_SET_EXPECTED}\n  actual   {got}")

    artifacts = {}
    def save(name, obj):
        p = os.path.join(ART_DIR, name)
        with open(p, "w", encoding="utf-8") as f:
            f.write(json.dumps(obj, indent=2, ensure_ascii=False))
        artifacts[f"artifacts/{name}"] = sha256_file(p)

    save("self_test.json", st)

    # --- S2 field metadata ----------------------------------------------
    print("S2 metadata")
    for m in ["res.partner", "res.company", "res.users", "res.currency",
              "ir.sequence", "ir.attachment", "res.groups", "res.country", "res.lang"]:
        r = call(m, "fields_get", [], {"attributes": ["type", "string", "required", "readonly", "selection"]})
        save(f"s2_fields_{m.replace('.', '_')}.json", r)

    # --- S4 access -------------------------------------------------------
    print("S4 access")
    s4 = {}
    for m in ["res.partner", "res.company", "res.users", "ir.rule", "ir.model.access", "ir.cron"]:
        r = call(m, "search_count", [[]])
        s4[m] = {"reachable": r["status"] == "ok",
                 "count": r.get("value"), "refusal": r.get("message")}
    save("s4_access_rules_check.json", s4)

    # --- S5 scheduled ----------------------------------------------------
    print("S5 scheduled")
    save("s5_scheduled_actions_check.json",
         call("ir.cron", "search_read", [[]], {"fields": ["name", "model_name", "active"], "limit": 25}))

    # --- S6 transactions, own company only, cleaned up afterwards --------
    print("S6 transactions")
    created = []
    tx = {"write_scope_company_id": OBSERVER_COMPANY_ID}
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    pname = f"ROOMB_TEST_OBS_PARTNER_{stamp}"

    c = call("res.partner", "create", [{"name": pname, "is_company": True,
                                        "company_id": OBSERVER_COMPANY_ID,
                                        "email": "obs_test@roomb.local",
                                        "phone": "+6621234567"}])
    tx["create"] = c
    if c["status"] == "ok":
        pid = c["value"][0] if isinstance(c["value"], list) else c["value"]
        created.append(pid)
        flds = ["id", "name", "company_id", "email", "phone", "active", "create_uid", "create_date"]
        tx["after_create"] = call("res.partner", "read", [[pid]], {"fields": flds})
        tx["update"] = call("res.partner", "write", [[pid], {"phone": "+6629876543"}])
        tx["after_update"] = call("res.partner", "read", [[pid]], {"fields": ["id", "phone", "write_uid", "write_date"]})
        tx["archive"] = call("res.partner", "write", [[pid], {"active": False}])
        tx["after_archive"] = call("res.partner", "read", [[pid]], {"fields": ["id", "active"]})
        cp = call("res.partner", "copy", [pid], {"default": {"name": pname + "_COPY"}})
        tx["copy"] = cp
        if cp["status"] == "ok":
            cid = cp["value"][0] if isinstance(cp["value"], list) else cp["value"]
            created.append(cid)
            tx["after_copy"] = call("res.partner", "read", [[cid]],
                                    {"fields": ["id", "name", "company_id", "email", "phone", "active"]})
    save("s6_partner_lifecycle.json", tx)

    save("s6_sequence_read.json",
         call("ir.sequence", "search_read", [[]],
              {"fields": ["id", "name", "code", "prefix", "padding", "number_next"], "limit": 10}))

    # --- probes: record reachability only, no conclusions -----------------
    print("probes")
    probes = {}
    for m in ["account.move", "account.journal", "stock.picking", "stock.move", "uom.uom"]:
        r = call(m, "search_count", [[]])
        probes[m] = {"reachable": r["status"] == "ok",
                     "count": r.get("value"), "refusal": r.get("message")}
    save("probe_reachability.json", probes)

    # --- CLEANUP: remove every record this run created --------------------
    print("cleanup")
    leftovers = call("res.partner", "search",
                     [[["name", "like", "ROOMB_TEST_OBS_PARTNER"]]],
                     {"context": {"active_test": False}})
    ids = sorted(set(created + (leftovers["value"] if leftovers["status"] == "ok" else [])))
    cl = {"created_this_run": created, "found_including_previous_runs": ids}
    cl["unlink"] = call("res.partner", "unlink", [ids]) if ids else {"status": "ok", "value": "nothing to remove"}
    verify = call("res.partner", "search",
                  [[["name", "like", "ROOMB_TEST_OBS_PARTNER"]]],
                  {"context": {"active_test": False}})
    cl["remaining_after_cleanup"] = verify.get("value") if verify["status"] == "ok" else verify
    cl["result"] = "CLEAN" if verify.get("value") == [] else "RESIDUE_REMAINS"
    save("s6_cleanup.json", cl)
    print(f"cleanup    {cl['result']}")

    # --- record skeleton: OBSERVED only, interpretation left to Lane B ----
    lines = ["# RECORD SKELETON - Stage 1a / batch W1-STD",
             "# BUSINESS_STATEMENT is intentionally EMPTY.",
             "# A deterministic script may not author a business statement - that is",
             "# interpretation and belongs to Lane B, working from these artifacts alone.",
             ""]
    for rel, h in sorted(artifacts.items()):
        lines += [f"- ARTIFACT: {rel}",
                  f"  ARTIFACT_SHA256: {h}",
                  f"  SURFACE: {'S2' if '/s2_' in rel else 'S4' if '/s4_' in rel else 'S5' if '/s5_' in rel else 'S6' if '/s6_' in rel else 'META'}",
                  "  BUSINESS_STATEMENT: PENDING_LANE_B_INTERPRETATION",
                  "  QID: PENDING",
                  "  LAYER: PENDING",
                  "  EVIDENCE_TIER: OBSERVED",
                  "  OBSERVED_BY: stage1a_collector_V2",
                  f"  OBSERVED_AT: {datetime.datetime.now(datetime.timezone.utc).isoformat()}",
                  f"  INSTALLED_SET_HASH: {got}",
                  "  STATUS: DRAFT", ""]
    open(os.path.join(BATCH_DIR, "RECORD_SKELETON.yaml"), "w", encoding="utf-8").write("\n".join(lines))

    with open(os.path.join(BATCH_DIR, "MANIFEST.sha256"), "w") as f:
        for rel, h in sorted(artifacts.items()):
            f.write(f"{h}  {rel}\n")

    rep = f"""# BATCH REPORT - {BATCH_ID}

Batch ID            : {BATCH_ID}
Scope               : module `base`, standard question set only
Collector           : collectors/stage1a_collector_V2.py
Run at              : {datetime.datetime.now(datetime.timezone.utc).isoformat()}
Server              : {url} ({db}) as {usr} uid={uid}

## Self-test
1 no source in workspace : {st['t1_no_source_in_workspace']['result']}
2 write scope            : company_id {OBSERVER_COMPANY_ID} only
3 installed-set hash     : {st['t3_result']}  {got}
4 tooling declaration    : deterministic script; no MCP server, no connector,
                           no web search, no filesystem access outside the workspace

## Results
Artifacts            : {len(artifacts)}
Records              : 0 written - RECORD_SKELETON.yaml awaits Lane B interpretation
Test-record cleanup  : {cl['result']}
Remaining test rows  : {cl['remaining_after_cleanup']}

## Statement
No reference source was read during this batch, by any tool, connector,
MCP server or web search. All server errors were scrubbed of source paths
before being written. No conclusion was recorded - observation only.

Status: DRAFT - NOT READY FOR RECONCILIATION
        (records.yaml not yet authored; single-lane until Lane A answers the same QIDs)
"""
    open(os.path.join(BATCH_DIR, "BATCH_REPORT.md"), "w", encoding="utf-8").write(rep)
    print(f"done       {len(artifacts)} artifacts -> {BATCH_DIR}")

if __name__ == "__main__":
    main()
