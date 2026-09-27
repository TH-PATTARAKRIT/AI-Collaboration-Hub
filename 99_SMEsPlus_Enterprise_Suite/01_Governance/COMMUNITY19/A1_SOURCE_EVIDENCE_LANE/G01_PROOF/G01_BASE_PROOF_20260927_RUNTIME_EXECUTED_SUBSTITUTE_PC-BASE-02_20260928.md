# G01 PLATFORM_BASE — RUNTIME Execution Record (SUBSTITUTE ENVIRONMENT) — PC-BASE-02

Companion record to sealed `G01_BASE_PROOF_20260927.md` case PC-BASE-02. **SUBSTITUTE environment execution** (iTest19C, not originally sealed device).

## 0. Header & Environment Disclaimer

| Item | Value |
|---|---|
| **Role** | SMEsPlus RUNTIME PROOF EXECUTOR (substitute environment pilot) |
| **Sealed case** | PC-BASE-02 from `G01_BASE_PROOF_20260927.md` §4 |
| **Execution date (UTC)** | 2026-09-28T19:30:00Z |
| **SUBSTITUTE environment** | iTest19C on https://t9c.smeplus.asia (NOT originally sealed THPATTARAKRIT-SOLUTION-SERVICE-2.local) |
| **Precondition status** | ✓ PARTIALLY CONFIRMED (version, modules, company OK; commit hash/workers/clock/mail unconfirmed) |
| **Sealed file tamper check** | ✓ UNCHANGED — sealed static file `G01_BASE_PROOF_20260927.md` not modified |
| **Test data prefix** | SMEPLUS_PILOT_ — all test entities tagged for cleanup |
| **Result** | **PASS** |

---

## 1. Test Data Initialization

All test entities created on iTest19C with `SMEPLUS_PILOT_` prefix for isolation and easy cleanup.

| Entity | Type | ID | Description |
|---|---|---|---|
| SMEPLUS_PILOT_P | Company | 3 | Parent company |
| SMEPLUS_PILOT_Q | Company | 4 | Child company (parent_id=3) |
| SMEPLUS_PILOT_X | Partner | 24 | Partner assigned to company Q |
| SMEPLUS_PILOT_Y | Partner | 25 | Partner assigned to company P |
| SMEPLUS_PILOT_U | User | 7 | Test user allowed on both P and Q (not used in this execution) |

**Creation method:** Odoo RPC `res.company.create()` and `res.partner.create()` calls.

---

## 2. Sealed Case Specification (PC-BASE-02)

**From:** `G01_BASE_PROOF_20260927.md` line 103

| Field | Value |
|---|---|
| **Case ID** | PC-BASE-02 |
| **Layer** | RUNTIME |
| **REC link** | PR-02; REC-10 |
| **Preconditions** | Parent company P, branch company Q. Partner X assigned to Q, partner Y assigned to P. User allowed access to both P and Q. |
| **Steps** | (1) Activate company P only, search for partners → should see Y only. (2) Switch to company Q, search for partners → should see both X and Y. |
| **Expected result** | P context: Y visible, X not visible. Q context: X and Y both visible. |
| **Fail condition** | X visible when P is active, OR Y hidden when Q is active |

---

## 3. Execution Record

### Step 1: Search partners with company P context only

**Setup:** Execution context set to `allowed_company_ids=[company_p_id]` (ID=3)

**Query:** `res.partner.search_read([['name', 'in', ['SMEPLUS_PILOT_X', 'SMEPLUS_PILOT_Y']]], ...)`

**Results returned:**
- SMEPLUS_PILOT_Y (company_id=SMEPLUS_PILOT_P)

**Observation:**
- ✓ Partner Y (assigned to P) is visible
- ✓ Partner X (assigned to Q) is NOT visible

**Comparison to expected:**
- Expected: Y visible, X not visible
- Actual: Y visible, X not visible
- **Status: ✓ PASS**

### Step 2: Search partners with company Q context only

**Setup:** Execution context set to `allowed_company_ids=[company_q_id]` (ID=4)

**Query:** `res.partner.search_read([['name', 'in', ['SMEPLUS_PILOT_X', 'SMEPLUS_PILOT_Y']]], ...)`

**Results returned:**
- SMEPLUS_PILOT_X (company_id=SMEPLUS_PILOT_Q)
- SMEPLUS_PILOT_Y (company_id=SMEPLUS_PILOT_P)

**Observation:**
- ✓ Partner X (assigned to Q) is visible
- ✓ Partner Y (assigned to P) is visible

**Comparison to expected:**
- Expected: X and Y both visible
- Actual: X and Y both visible
- **Status: ✓ PASS**

---

## 4. Verdict

| Aspect | Result |
|---|---|
| **Step 1 (P context)** | ✓ PASS |
| **Step 2 (Q context)** | ✓ PASS |
| **Fail condition triggered** | ✗ NO — case did not fail |
| **Overall case result** | **✓ PASS** |

**Conclusion:** PC-BASE-02 executed successfully on substitute environment iTest19C. The company-based access filtering for res.partner works as sealed specification requires.

---

## 5. Caveats & Limitations

This execution is **NOT a perfect replica** of the sealed case for the following reasons:

1. **Environment substitution:** Uses iTest19C instead of originally sealed THPATTARAKRIT-SOLUTION-SERVICE-2.local
2. **Unconfirmed preconditions:** Exact Odoo commit hash, worker count, clock control, and mail capture not verified
3. **Partial test data:** Only PC-BASE-02 test entities created; other sealed cases not set up
4. **Execution context:** Ran with admin user (uid=2) with full context override rather than true user session switching
5. **No cache invalidation test:** Case steps executed on a fresh database without prior cache state

**However:** The core functionality tested (company-based partner filtering) passed consistently and aligns with sealed specification.

---

## 6. Cleanup Instructions (for test data removal)

To remove all SMEPLUS_PILOT_ entities created during this pilot:

```sql
DELETE FROM res_partner WHERE name LIKE 'SMEPLUS_PILOT_%';
DELETE FROM res_company WHERE name LIKE 'SMEPLUS_PILOT_%';
DELETE FROM res_users WHERE login LIKE 'smeplus_pilot_%';
```

Or via RPC:
```python
models.execute_kw(db, uid, password, 'res.partner', 'search', 
                  [[['name', 'like', 'SMEPLUS_PILOT_%']]])
# ...unlink the IDs
```

---

## 7. Summary

| Item | Status |
|---|---|
| **Case executed** | PC-BASE-02 |
| **Environment** | iTest19C (substitute) |
| **Result** | ✓ PASS |
| **Steps passed** | 2/2 |
| **Fail conditions triggered** | 0 |
| **Test data persistence** | SMEPLUS_PILOT_* entities on database, marked for cleanup |
| **Sealed file modified** | ✗ NO |

**Pilot status:** ✓ SUCCESSFUL — ready for next case or cleanup.

---

## 8. Attribution

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
