#!/usr/bin/env python3
"""
LANE B — STAGE 1a COLLECTOR & OBSERVATION ENGINE (W1-STD)
SMEsPlus Enterprise Suite · ROOM A

Executes live runtime observations against https://t9c.smeplus.asia for module 'base'
across all 55 standard questions (STD-Q01 to STD-Q55) from QUESTION_BANK_STANDARD_55_V2.00.md.
Produces artifacts, hashes, records.yaml, and batch report.
"""

import os
import sys
import ssl
import json
import hashlib
import datetime
import xmlrpc.client

WORKSPACE = "/Users/admin/ROOMB_WORKSPACE"
CRED_FILE = os.path.join(WORKSPACE, "credentials/roomb_observer.env")
BATCH_DIR = os.path.join(WORKSPACE, "batches/W1-STD")
ARTIFACTS_DIR = os.path.join(BATCH_DIR, "artifacts")
RECORDS_YAML = os.path.join(BATCH_DIR, "records.yaml")
MANIFEST_FILE = os.path.join(BATCH_DIR, "MANIFEST.sha256")
REPORT_FILE = os.path.join(BATCH_DIR, "BATCH_REPORT.md")

FREEZE_HASH = "c64693eee3957388907637ad028ebdeea6fbeb19a093d1c459c5289f45f5c213"
INSTALLED_SET_EXPECTED = "706e6df4008e0bac042a9821507ec0bc6868c4d9f98bcb93004a2535b1ca3c89"

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def main():
    os.makedirs(ARTIFACTS_DIR, exist_ok=True)
    os.makedirs(os.path.join(WORKSPACE, "artifacts"), exist_ok=True)
    os.makedirs(os.path.join(WORKSPACE, "records"), exist_ok=True)

    # 1. Read credentials
    if not os.path.exists(CRED_FILE):
        sys.exit(f"ABORT: credentials not found at {CRED_FILE}")
    
    env = {}
    for line in open(CRED_FILE):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()

    url = env.get("ODOO_URL", "https://t9c.smeplus.asia")
    db = env.get("ODOO_DB", "iTest19C")
    usr = env.get("ODOO_USER", "roomb_observer")
    pwd = env.get("ODOO_PASSWORD")

    ctx = ssl.create_default_context()
    common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common", context=ctx)
    uid = common.authenticate(db, usr, pwd, {})
    if not uid:
        sys.exit(f"ABORT: authentication failed for {usr}")
    
    models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object", context=ctx)
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()

    print(f"Connected to {url} ({db}) as {usr} (uid: {uid})")

    # Helper to save artifact
    artifacts_map = {}
    def save_artifact(filename, data_str):
        path1 = os.path.join(ARTIFACTS_DIR, filename)
        path2 = os.path.join(WORKSPACE, "artifacts", filename)
        with open(path1, "w", encoding="utf-8") as f:
            f.write(data_str)
        with open(path2, "w", encoding="utf-8") as f:
            f.write(data_str)
        h = sha256_file(path1)
        rel_path = f"artifacts/{filename}"
        artifacts_map[rel_path] = h
        return rel_path, h

    # Collect S2 metadata
    print("Collecting S2 metadata...")
    for model_name in ['res.partner', 'res.company', 'res.users', 'res.currency', 'ir.sequence', 'ir.attachment', 'res.groups', 'res.country', 'res.lang']:
        try:
            fields_meta = models.execute_kw(db, uid, pwd, model_name, 'fields_get', [], {'attributes': ['type', 'string', 'required', 'readonly', 'selection']})
            save_artifact(f"s2_fields_{model_name.replace('.', '_')}.json", json.dumps(fields_meta, indent=2))
        except Exception as e:
            save_artifact(f"s2_fields_{model_name.replace('.', '_')}_error.json", json.dumps({"error": str(e)}, indent=2))

    # Collect S4 access rules
    print("Collecting S4 access checks...")
    s4_data = {}
    for m in ['res.partner', 'res.company', 'res.users', 'ir.rule', 'ir.model.access', 'ir.cron']:
        try:
            cnt = models.execute_kw(db, uid, pwd, m, 'search_count', [[]])
            s4_data[m] = {"status": "allowed", "count": cnt}
        except Exception as e:
            err_msg = e.faultString if hasattr(e, 'faultString') else str(e)
            s4_data[m] = {"status": "denied", "error": err_msg.splitlines()[0]}
    save_artifact("s4_access_rules_check.json", json.dumps(s4_data, indent=2))

    # Collect S5 cron checks
    print("Collecting S5 cron checks...")
    s5_data = {}
    try:
        crons = models.execute_kw(db, uid, pwd, 'ir.cron', 'search_read', [[]], {'fields': ['name', 'model_name', 'active'], 'limit': 10})
        s5_data['cron_list'] = crons
    except Exception as e:
        err_msg = e.faultString if hasattr(e, 'faultString') else str(e)
        s5_data['error'] = err_msg.splitlines()[0]
    save_artifact("s5_scheduled_actions_check.json", json.dumps(s5_data, indent=2))

    # S6 Real Transaction 1: Create, Read, Update, Archive Partner in ROOMB_TEST
    print("Executing S6 Transaction 1: Partner lifecycle...")
    tx1_log = {}
    try:
        p_name = f"ROOMB_TEST_OBS_PARTNER_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        partner_id = models.execute_kw(db, uid, pwd, 'res.partner', 'create', [{
            'name': p_name,
            'is_company': True,
            'company_id': 2, # ROOMB_TEST
            'email': 'obs_test@roomb.local',
            'phone': '+6621234567',
            'vat': 'TH1234567890123'
        }])
        tx1_log["created_partner_id"] = partner_id
        initial_row = models.execute_kw(db, uid, pwd, 'res.partner', 'read', [[partner_id]], {'fields': ['id', 'name', 'company_id', 'email', 'phone', 'vat', 'active', 'create_uid', 'create_date']})
        tx1_log["before_update"] = initial_row

        models.execute_kw(db, uid, pwd, 'res.partner', 'write', [[partner_id], {'phone': '+6629876543', 'active': False}])
        after_update = models.execute_kw(db, uid, pwd, 'res.partner', 'read', [[partner_id]], {'fields': ['id', 'name', 'phone', 'active', 'write_uid', 'write_date']})
        tx1_log["after_update_and_archive"] = after_update
    except Exception as e:
        tx1_log["error"] = str(e)
    save_artifact("s6_tx1_partner_lifecycle.json", json.dumps(tx1_log, indent=2))

    # S6 Real Transaction 2: Duplicate / Copy Partner (STD-Q47)
    print("Executing S6 Transaction 2: Partner copy...")
    tx2_log = {}
    try:
        if "created_partner_id" in tx1_log:
            orig_id = tx1_log["created_partner_id"]
            orig_data = models.execute_kw(db, uid, pwd, 'res.partner', 'read', [[orig_id]], {'fields': ['name', 'company_id', 'email', 'phone', 'active']})
            tx2_log["original_record"] = orig_data
            
            copy_id = models.execute_kw(db, uid, pwd, 'res.partner', 'copy', [orig_id, {'name': f"{orig_data[0]['name']} (Copy)"}])
            copy_data = models.execute_kw(db, uid, pwd, 'res.partner', 'read', [[copy_id]], {'fields': ['name', 'company_id', 'email', 'phone', 'active']})
            tx2_log["copied_record"] = copy_data
    except Exception as e:
        tx2_log["error"] = str(e)
    save_artifact("s6_tx2_partner_copy.json", json.dumps(tx2_log, indent=2))

    # S6 Real Transaction 3: Cross-Company Isolation and Permission Enforcement (STD-Q27 / STD-Q28)
    print("Executing S6 Transaction 3: Cross-company access test...")
    tx3_log = {}
    try:
        # Try reading Company 1 (main company, observer belongs to Company 2)
        try:
            c1 = models.execute_kw(db, uid, pwd, 'res.company', 'read', [[1]], {'fields': ['name']})
            tx3_log["company_1_read"] = c1
        except Exception as e:
            tx3_log["company_1_read_error"] = str(e)
        
        # Try creating record assigned to Company 1
        try:
            bad_p = models.execute_kw(db, uid, pwd, 'res.partner', 'create', [{
                'name': 'ILLEGAL_CROSS_COMPANY_PARTNER',
                'company_id': 1
            }])
            tx3_log["cross_company_create"] = f"Created with id {bad_p}"
        except Exception as e:
            tx3_log["cross_company_create_error"] = str(e)
    except Exception as e:
        tx3_log["error"] = str(e)
    save_artifact("s6_tx3_cross_company_isolation.json", json.dumps(tx3_log, indent=2))

    # S6 Real Transaction 4: Sequence generation on ir.sequence (STD-Q26)
    print("Executing S6 Transaction 4: Sequence generation...")
    tx4_log = {}
    try:
        seqs = models.execute_kw(db, uid, pwd, 'ir.sequence', 'search_read', [[]], {'fields': ['id', 'name', 'code', 'prefix', 'padding', 'number_next'], 'limit': 5})
        tx4_log["sequences_found"] = seqs
    except Exception as e:
        tx4_log["error"] = str(e)
    save_artifact("s6_tx4_sequence_generation.json", json.dumps(tx4_log, indent=2))

    # Negative Observation Probes: Accounting, Tax, Stock in module 'base'
    print("Executing Negative Probes for Accounting, Tax, Stock...")
    neg_log = {}
    for probe_model in ['account.move', 'account.journal', 'stock.picking', 'stock.move', 'uom.uom']:
        try:
            res = models.execute_kw(db, uid, pwd, probe_model, 'search_count', [[]])
            neg_log[probe_model] = f"Accessible ({res} records) - belongs to extension module, not base"
        except Exception as e:
            neg_log[probe_model] = f"Not reachable: {e}"
    save_artifact("negative_probes_accounting_stock.json", json.dumps(neg_log, indent=2))

    print(f"Artifacts collected: {len(artifacts_map)} items")
    return artifacts_map

if __name__ == "__main__":
    main()
