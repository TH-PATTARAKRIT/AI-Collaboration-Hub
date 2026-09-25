# W1-B12 OVQDT Review

Module: resource

40 unique QIDs: PASS
40 DISCONFIRMING_OBSERVATION: PASS
Functional Review: PASS
QA/Testability: PASS
SaaS Challenge: PASS where applicable
Adversarial Review: PASS
Duplicate-QID: PASS
Duplicate-hypothesis semantic review: PASS
Source-neutral/Clean-Room: PASS
Structural lint: PASS
Padding review: PASS

Authoring source-trace used for QA only, not copied into the question bank:
- Odoo 19.0 addons/resource/__manifest__.py
- addons/resource/models/resource_resource.py
- addons/resource/models/resource_calendar.py
- addons/resource/models/resource_calendar_attendance.py
- addons/resource/models/resource_calendar_leaves.py
- addons/resource/models/resource_mixin.py
- addons/resource/models/res_company.py
- addons/resource/models/res_users.py

Review notes:
- Questions cover resource identity/type, company/calendar boundary, timezone, efficiency, flexible schedules, attendance, leave, batch interval computation, mixin lifecycle, copy/idempotence behavior, and SaaS isolation.
- No source-path or implementation wording is required to answer the questions.
- No A1/A2/A3/MASTER result is asserted.
- Counts are not Formal Coverage.

Bank SHA-256: 2632ff345b758258f8c5b8537b502d1b1145dde3b0788ea57bcb4fbfd8c71d08
Formal Coverage: NOT AUTHORIZED
