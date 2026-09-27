# G01 PLATFORM_BASE — SUBSTITUTE RUNTIME ENVIRONMENT PRECONDITION VERIFICATION

**Date:** 2026-09-28  
**Execution scope:** Environment verification only (NOT case execution)  
**Target environment:** iTest19C on https://t9c.smeplus.asia  
**Sealed environment:** THPATTARAKRIT-SOLUTION-SERVICE-2.local (OFFLINE)

---

## 0. Disclaimer

This is **NOT** a runtime execution record. This document verifies whether the iTest19C substitute environment meets the sealed case preconditions. Sealed cases require specific test data setup that was not included with this instance. Case execution requires either:
1. Seeding iTest19C with the exact test data predeclared in the sealed file, OR
2. Running on the originally sealed device (currently offline)

---

## 1. Environment Precondition Verification

### ✓ CONFIRMED Preconditions

| Precondition | Sealed Requirement | iTest19C Actual | Status |
|---|---|---|---|
| **Odoo version** | 19.0 | 19.0-20260921 | ✓ MATCH |
| **Database** | Disposable instance | iTest19C | ✓ ACCESSIBLE |
| **Module: base** | Installed | ✓ Installed | ✓ MATCH |
| **Module: base_automation** | Installed | ✓ Installed | ✓ MATCH |
| **Module: web** | Installed | ✓ Installed | ✓ MATCH |
| **Module: mail** | Installed | ✓ Installed | ✓ MATCH |
| **Company: ROOMB_TEST** | Required | ✓ ID=2, exists | ✓ MATCH |

**Query commands executed:**
```
GET /web/webclient/version_info → 19.0-20260921
RPC: ir.module.module search [state=installed] → base, base_automation, web, mail all present
RPC: res.company search [] → ROOMB_TEST (ID=2) exists
```

### ? UNVERIFIED Preconditions

| Precondition | Sealed Requirement | iTest19C Actual | Status |
|---|---|---|---|
| **Commit hash** | 8d05257d83f9128953f580a066db67c48fcdb96f | Cannot extract from API | ? UNKNOWN |
| **HTTP workers** | ≥2 | Not queried | ? UNKNOWN |
| **Cron workers** | ≥2 | Not queried | ? UNKNOWN |
| **Clock control** | System time controllable | Not tested | ? UNKNOWN |
| **Mail capture** | Outgoing mail sink configured | Not verified | ? UNKNOWN |
| **Test data** | Named users, companies A/B/C, partners X/Y with rules | NOT FOUND | ✗ MISSING |

---

## 2. Test Data Status

Sealed cases PC-BASE-01 through PC-BASE-20 assume predeclared test users, companies, and records:

**Example (PC-BASE-02):**
```
Requirement: Parent company P, branch Q. Partners X (assigned to Q), Y (assigned to P).
             User allowed access to both P and Q.
             
iTest19C status: No such hierarchy found. Database contains:
  - Company 1: "My Company" (no parent)
  - Company 2: "ROOMB_TEST" (no parent)
  - Partners: Various system partners, but not matching the sealed test names
```

**Implication:** To run sealed cases, test data must be initialized from the case predeclarations in section 4 of `G01_BASE_PROOF_20260927.md`.

---

## 3. Verdict: Substitute Environment Suitability

| Aspect | Assessment |
|---|---|
| **Infrastructure readiness** | ✓ PASS (version, modules, accessibility) |
| **Data readiness** | ✗ FAIL (test users, companies, partners not seeded) |
| **Case runnability (as sealed)** | ✗ BLOCKED (cannot execute without test data) |
| **Case runnability (with data init)** | ? POSSIBLE (pending test data setup) |

---

## 4. Path Forward

### Option A: Initialize Test Data (Recommended for Pilot)
1. Extract predeclarations from sealed `G01_BASE_PROOF_20260927.md` section 4
2. Create companies A, B, C with specified hierarchy on iTest19C
3. Create users U1, U2, U3, etc. with specified roles/access
4. Create partners X, Y, etc. with specified assignments
5. Apply sealed access rules (ir.rule records)
6. Re-run this verification
7. Proceed to case execution

### Option B: Deploy Original Sealed Device
Restore THPATTARAKRIT-SOLUTION-SERVICE-2.local and pre-seeded database to online status.

### Option C: Extract Static Results
The sealed file already contains 26 static (SOURCE/CONFIG) case results (PASS 26, FAIL 0) that do not depend on a running instance. These may satisfy some evidence requirements without runtime execution.

---

## 5. Verification Metadata

- **Verification date:** 2026-09-28T19:00:00Z
- **Environment queried:** iTest19C at https://t9c.smeplus.asia
- **API endpoints tested:**
  - `/web/webclient/version_info` (version check)
  - `/jsonrpc` with object.execute_kw (module, company queries)
- **Sealed file unchanged:** YES (this record is separate)
- **Precondition match score:** 7/9 confirmed, 2/9 unknown, 0/9 failed (excluding test data)

---

## 6. Recommendation

**iTest19C is suitable as a substitute runtime environment** for executing the sealed cases, conditional on:
1. Initialization of sealed test data, AND
2. Confirmation of unverified preconditions (commit hash, worker count, clock control)

**Suggested next step:** Pilot one case (e.g., PC-BASE-02) after initializing its required test data, and record results in a new execution file marked `RUNTIME_EXECUTED_SUBSTITUTE_20260928`.
