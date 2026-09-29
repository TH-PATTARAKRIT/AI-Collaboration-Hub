# Source Map (candidate) — `hr_work_entry_holidays`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_work_entry_holidays` |
| Display name | Time Off in Payslips |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `769cf83ff5f2e222` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_work_entry_holidays/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_holidays`, `hr_work_entry`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `l10n_fr_hr_work_entry_holidays`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Payroll / Manage Time Off in Payslips
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `hr.version`, `hr.leave.type`, `hr.leave`, `hr.work.entry`, `hr.work.entry.type`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.version`, `hr.leave.type`, `hr.leave`, `hr.work.entry`, `hr.work.entry.type`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 27 of 27 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_work_entry_holidays
Revision 19.0.post20260921 | Bridge: Time Off (hr_holidays) <-> Work Entries (hr_work_entry)

## A. Capabilities (core / optional / conditional)
- Bridge that lets approved time off feed work entries used by payroll: manifest depends on hr_holidays and hr_work_entry (hr_work_entry_holidays/__manifest__.py:17); title "Time Off in Payslips" (:6).
- Auto-install: yes, installs itself once both parents are present (hr_work_entry_holidays/__manifest__.py:25). No settings toggle, no own groups.
- Adds a "Work Entry Type" on each time-off type (hr_work_entry_holidays/models/hr_leave.py:12), shown in the time-off type form under a "Payroll" group (hr_work_entry_holidays/views/hr_leave_type_views.xml:10-11) and as an optional list column (hr_work_entry_holidays/views/hr_leave_views.xml:8).
- Conditional: country-specific time-off types get preset work entry types only where those localisation types exist (AE, BE, CH, EG, HK, ID, JO, LU, MX, SA, SK, PL blocks: hr_work_entry_holidays/data/hr_leave_type_data.xml:21,30,79,105,118,167,196,201,206,219,240,245).
- On install, every existing work entry is re-checked for errors (post-install hook: hr_work_entry_holidays/__init__.py:7-8; manifest :26).

## B. Business objects and lifecycle
- Time off request (owner hr_holidays) gains a link from work entries: a work entry may point to a time off (hr_work_entry_holidays/models/hr_work_entry.py:12) and mirrors its state (:13).
- Work entry type gains a reverse list of time-off types that use it (hr_work_entry_holidays/models/hr_work_entry.py:62-64).
- Approval: when a time off is validated, a leave-type work entry is created for each contract period already generated; existing work entries fully inside the leave are archived (unless already validated); partially overlapping ones are detached from the leave (hr_work_entry_holidays/models/hr_leave.py:23-87, 127-130).
- Refusal, moving back to confirm, or user cancellation archives the leave's work entries and regenerates ordinary attendance entries for those days (hr_work_entry_holidays/models/hr_leave.py:132-165).
- Cancelling a work entry (state cancelled) refuses its linked time off if not already refused (hr_work_entry_holidays/models/hr_work_entry.py:15-18).
- Resource-calendar leaves created from time off carry the leave type's work entry type (hr_work_entry_holidays/models/hr_leave.py:18-21).

## C. Validations, automation, security
- Creating or editing a time off (employee, state, dates) runs work entry error checking over the affected window plus one day either side; checks skipped when other fields change (hr_work_entry_holidays/models/hr_leave.py:89-121).
- A time off cannot be cancelled by the user once any linked work entry is validated (hr_work_entry_holidays/models/hr_leave.py:167-175).
- When an entry is reset to conflicting state, non-leave (attendance) entries lose their leave link (hr_work_entry_holidays/models/hr_work_entry.py:20-23).
- Leaves whose work entry type code is LEAVE110/LEAVE210/LEAVE280 are excluded from the "leaves on public holiday" set (hr_work_entry_holidays/models/hr_leave.py:123-125).
- Priority when several leaves cover the same interval: leave types flagged as bypassing codes first, then company-wide (global) time off, then personal time off; fallback is the generic leave work entry type (hr_work_entry_holidays/models/hr_version.py:29-61).
- No new access rules, groups or CSV access in this module (data files list only views/data: hr_work_entry_holidays/__manifest__.py:18-22). Cancellation/regeneration work runs with elevated rights (hr_work_entry_holidays/models/hr_leave.py:129,149,155).

## D. Handoffs
- hr_holidays owns time off, leave types, public holidays; hr_work_entry owns work entry types, generation and validation; contract/version data (hr.version) owned by the employee/work entry stack (hr_work_entry_holidays/models/hr_version.py:9-10).
- Payroll consumption of work entries and leave durations by type is not in this module; a helper returns validated-leave durations per leave type for a date range (hr_work_entry_holidays/models/hr_work_entry.py:36-55). Payslip computation: UNKNOWN — EVIDENCE INSUFFICIENT (payroll not in Community tree; a test only touches work data: hr_work_entry_holidays/tests/test_payslip_holidays_computation.py:11 (TEST)).

## E. Configuration that changes outcomes
- Work entry type chosen on each time-off type decides how the leave appears in work entries (hr_work_entry_holidays/models/hr_leave.py:12,20).
- Preset mapping: paid time off -> legal leave; unpaid -> unpaid leave; sick -> sick leave; compensatory -> compensatory (hr_work_entry_holidays/data/hr_leave_type_data.xml:4-18); presets are non-updating on module upgrade (noupdate block, :3-19).
- Work entries only produced for periods the contract has already generated (hr_work_entry_holidays/models/hr_leave.py:45).

## F. Effective extension path
- hr_version (contract intervals), hr_holidays, hr_work_entry; localisation payroll modules supply the country work entry types referenced in data (module names only).

## G. Not verified
- Interaction with payroll rules/payslips: UNKNOWN — EVIDENCE INSUFFICIENT.
- Behaviour with flexible-hours employees beyond test names: test exists (hr_work_entry_holidays/tests/test_leave.py:175 (TEST)); detail UNKNOWN — EVIDENCE INSUFFICIENT.

