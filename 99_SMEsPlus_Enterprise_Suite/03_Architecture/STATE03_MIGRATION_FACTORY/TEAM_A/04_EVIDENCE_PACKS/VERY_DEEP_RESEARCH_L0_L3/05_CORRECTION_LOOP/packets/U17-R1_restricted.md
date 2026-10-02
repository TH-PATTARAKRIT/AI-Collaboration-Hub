# Correction packet U17-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U17-R1` |
| Correction request | CR-021 |
| Classification | CORRECTION_REQUIRED · priority Normal |
| Boundary | U17 |
| Subject | Vehicle assignment log end date is set by the employee-departure wizard of the fleet bridge |
| Original evidence | U17 content 0556fad6 / packet HP_U17; found by U39 (CONTRA on VDR-U39-C513) (originals unchanged; lineage preserved) |
| Supersession | VDR-U17-C399 / its neutral statement and U17 report finding 'the assignment log end date is never set by code' (SUPERSEDED-IN-PART: true only for the model code searched; the departure wizard sets it) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U17R1-C001 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle_assignation_log.py:15 | date_end = fields.Date | FACT | always | — | The fleet module defines the assignment-log end date as a plain date field. | N-U17R1-001 |
| VDR-U17R1-C002 | FUNCTION MAPPING REQUIRED | hr_fleet/wizard/hr_departure_wizard.py:25 | ('date_end', '=', False) | FACT | fleet bridge installed (hr_fleet is in the dump) | — | The employee-departure wizard of the fleet bridge selects the employee's open assignment logs (no end date, or an end date after the departure date). | N-U17R1-001 |
| VDR-U17R1-C003 | FUNCTION MAPPING REQUIRED | hr_fleet/wizard/hr_departure_wizard.py:28 | assignations.write({'date_end': self.departure_date}) | FACT | fleet bridge installed | — | The wizard writes the departure date as the end date of those assignment logs, so the end date is set by code on employee departure. | N-U17R1-001 |
| VDR-U17R1-C004 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | fleet without the bridge or outside the departure flow | RT | UNKNOWN — whether the end date is set when a vehicle is reassigned or the driver changes outside the departure wizard; no setter was found in the model code searched (INFERENCE kept from U17-C399 for that scope). | N-U17R1-002 |
