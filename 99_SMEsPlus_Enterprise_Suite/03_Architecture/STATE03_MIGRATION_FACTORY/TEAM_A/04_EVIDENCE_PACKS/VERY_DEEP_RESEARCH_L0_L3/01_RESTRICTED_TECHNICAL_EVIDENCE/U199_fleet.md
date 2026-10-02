# U199 — Fleet: Vehicle, Cost Tracking, Service Records
**Evidence Level**: L0–L3 Restricted Technical Evidence
**Module**: `fleet` (Community only)
**Source tree**: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/fleet/`
**Date**: 2026-10-02

---

## 1. Module Structure

```
fleet/
  __manifest__.py        version 0.1; depends: base, mail; application=True
  models/
    fleet_vehicle.py                   FleetVehicle
    fleet_vehicle_model.py             FleetVehicleModel
    fleet_vehicle_model_brand.py       FleetVehicleModelBrand
    fleet_vehicle_model_category.py    FleetVehicleModelCategory
    fleet_vehicle_state.py             FleetVehicleState
    fleet_vehicle_odometer.py          FleetVehicleOdometer
    fleet_vehicle_log_services.py      FleetVehicleLogServices
    fleet_vehicle_log_contract.py      FleetVehicleLogContract
    fleet_vehicle_assignation_log.py   FleetVehicleAssignationLog
    fleet_vehicle_tag.py               FleetVehicleTag
    fleet_service_type.py              FleetServiceType
    mail_activity_type.py
    res_config_settings.py
  data/
    fleet_data.xml    (noupdate=1: states New Request/To Order/Registered/Downgraded + service types)
    fleet_demo.xml    (demo states: Ordered/Reserve/Waiting List)
```

**MIGRATION FLAG**: There is NO `fleet.vehicle.cost` model in v19. Cost tracking is fully split:
- Service costs → `fleet.vehicle.log.services` (`fleet/models/fleet_vehicle_log_services.py`)
- Contract costs → `fleet.vehicle.log.contract` (`fleet/models/fleet_vehicle_log_contract.py`)

---

## 2. `fleet.vehicle` — Key Fields

**File**: `fleet/models/fleet_vehicle.py`

| Field | Type | Line | Notes |
|---|---|---|---|
| `name` | Char (computed) | 38 | `brand/model/license_plate` pattern; stored |
| `license_plate` | Char | 52 | tracking=True |
| `vin_sn` | Char | 54 | VIN/chassis; tracking=True; copy=False |
| `model_id` | Many2one `fleet.vehicle.model` | 61-62 | required=True; tracking=True |
| `brand_id` | Many2one `fleet.vehicle.model.brand` | 63 | related via model_id.brand_id; store=True |
| `driver_id` | Many2one `res.partner` | 59 | tracking=True; copy=False |
| `future_driver_id` | Many2one `res.partner` | 60 | tracking=True; check_company=True |
| `state_id` | Many2one `fleet.vehicle.state` | 78-81 | default=`_get_default_state()`; ondelete="set null" |
| `company_id` | Many2one `res.company` | 45-48 | default=env.company |
| `currency_id` | Many2one `res.currency` | 49 | related via company_id |
| `acquisition_date` | Date | 73-74 | tracking=True; "Registration Date"; default=today |
| `order_date` | Date | 72 | "Order Date" |
| `write_off_date` | Date | 75 | "Cancellation Date"; tracking=True |
| `odometer` | Float (computed) | 90-91 | inverse=`_set_odometer`; reads from `fleet.vehicle.odometer` |
| `odometer_unit` | Selection km/mi | 92-95 | default='kilometers'; required=True |
| `vehicle_type` | Selection | 132 | related via model_id.vehicle_type (car/bike) |
| `vehicle_properties` | Properties | 141 | definition='model_id.vehicle_properties_definition' |
| `car_value` | Float | 127 | "Catalog Value (VAT Incl.)"; tracking=True |
| `net_car_value` | Float | 128 | "Purchase Value" |
| `log_services` | One2many `fleet.vehicle.log.services` | 65 | via vehicle_id |
| `log_contracts` | One2many `fleet.vehicle.log.contract` | 66 | via vehicle_id |
| `service_count` | Integer (computed) | 68 | computed by `_compute_count_all` |
| `contract_count` | Integer (computed) | 67 | computed by `_compute_count_all` |
| `odometer_count` | Integer (computed) | 69 | computed by `_compute_count_all` |

**Default state method** (`fleet/models/fleet_vehicle.py:30-32`):
```python
def _get_default_state(self):
    state = self.env.ref('fleet.fleet_vehicle_state_new_request', raise_if_not_found=False)
    return state if state and state.id else False
```

**Odometer getter** (`fleet/models/fleet_vehicle.py:247-254`):
```python
def _get_odometer(self):
    FleetVehicalOdometer = self.env['fleet.vehicle.odometer']
    for record in self:
        vehicle_odometer = FleetVehicalOdometer.search([('vehicle_id', 'in', record.ids)], limit=1, order='value desc')
        if vehicle_odometer:
            record.odometer = vehicle_odometer.value
        else:
            record.odometer = 0
```
Note: Returns `value desc` (highest odometer reading), NOT date-ordered.

**Odometer write guard** (`fleet/models/fleet_vehicle.py:401-402`):
```python
if 'odometer' in vals and any(vehicle.odometer > vals['odometer'] for vehicle in self):
    raise UserError(_('The odometer value cannot be lower than the previous one.'))
```

**Computed vehicle name** (`fleet/models/fleet_vehicle.py:234-237`):
```python
record.name = (record.model_id.brand_id.name or '') + '/' + (record.model_id.name or '') + '/' + (record.license_plate or _('No Plate'))
```

**MODEL_FIELDS_TO_VEHICLE mapping** (`fleet/models/fleet_vehicle.py:14-20`): Copies transmission, model_year, electric_assistance, color, seats, doors, trailer_hook, co2, co2_standard, fuel_type, power, horsepower, horsepower_tax, category_id, vehicle_range, power_unit, range_unit from model to vehicle on model_id change.

---

## 3. `fleet.vehicle.log.services` — Service Cost Records

**File**: `fleet/models/fleet_vehicle_log_services.py`

| Field | Type | Line | Notes |
|---|---|---|---|
| `vehicle_id` | Many2one `fleet.vehicle` | 15 | required=True; index=True |
| `service_type_id` | Many2one `fleet.service.type` | 33-36 | required=True; category='service' |
| `amount` | Monetary | 19 | "Cost" |
| `state` | Selection | 37-42 | new/running/done/cancelled; group_expand=True |
| `odometer_id` | Many2one `fleet.vehicle.odometer` | 21 | linked odometer reading |
| `odometer` | Float (computed) | 22-24 | inverse creates odometer record |
| `date` | Date | 26 | default=context_today |
| `company_id` | Many2one `res.company` | 27 | default=env.company |
| `purchaser_id` | Many2one `res.partner` | 29 | computed from vehicle.driver_id |
| `vendor_id` | Many2one `res.partner` | 31 | "Vendor" |
| `inv_ref` | Char | 32 | "Vendor Reference" |
| `model_id` | Many2one `fleet.vehicle.model` | 16 | related; store=True |
| `brand_id` | Many2one `fleet.vehicle.model.brand` | 17 | related; store=True |

State lifecycle: **new → running → done** (or cancelled). No automated transitions — manual.

---

## 4. `fleet.vehicle.log.contract` — Contract Cost Records

**File**: `fleet/models/fleet_vehicle_log_contract.py`

| Field | Type | Line | Notes |
|---|---|---|---|
| `vehicle_id` | Many2one `fleet.vehicle` | 20 | required=True; check_company=True; tracking=True; index=True |
| `cost_subtype_id` | Many2one `fleet.service.type` | 21 | category='contract'; domain enforced |
| `amount` | Monetary | 22 | "Cost" (one-time activation cost) |
| `cost_generated` | Monetary | 57 | "Recurring Cost"; tracking=True |
| `cost_frequency` | Selection | 58-64 | no/daily/weekly/monthly/yearly; required=True |
| `state` | Selection | 47-55 | futur/open/expired/closed |
| `start_date` | Date | 33-35 | default=context_today |
| `expiration_date` | Date | 36-40 | default=+1 year from today |
| `days_left` | Integer (computed) | 41 | warning countdown |
| `company_id` | Many2one `res.company` | 24 | default=env.company |
| `service_ids` | Many2many `fleet.service.type` | 65 | "Included Services" |
| `insurer_id` | Many2one `res.partner` | 44 | "Vendor" |

**Contract state machine** (transitions triggered by `write()` on start/expiration_date changes):
- `futur` (New) → `open` (Running) → `expired` (Expired) → `closed` (Cancelled)
- Automated by cron `ir_cron_contract_costs_generator` → `model.run_scheduler()` daily

---

## 5. `fleet.vehicle.state` — Vehicle State

**File**: `fleet/models/fleet_vehicle_state.py`

- Simple model: `name` (Char, required, translate), `sequence` (Integer), `fold` (Boolean for kanban)
- **No code-enforced transitions** — purely configurable; free-form Many2one on fleet.vehicle
- Unique constraint on `name`

**Seeded states** (fleet_data.xml, noupdate=1):
| XML ID | Name | Sequence |
|---|---|---|
| `fleet_vehicle_state_new_request` | New Request | 4 |
| `fleet_vehicle_state_to_order` | To Order | 5 |
| `fleet_vehicle_state_registered` | Registered | 7 |
| `fleet_vehicle_state_downgraded` | Downgraded | 8 |

**Demo-only states** (fleet_demo.xml — NOT installed in production):
| XML ID | Name | Sequence |
|---|---|---|
| `fleet_vehicle_state_ordered` | Ordered | 6 |
| `fleet_vehicle_state_reserve` | Reserve | 9 |
| `fleet_vehicle_state_waiting_list` | Waiting List | 10 |

`fleet_vehicle_state_waiting_list` is referenced in `fleet_vehicle.py:372` for `future_driver_id` assignment logic — but it is demo-only. Code uses `raise_if_not_found=False`.

---

## 6. `fleet.vehicle.odometer`

**File**: `fleet/models/fleet_vehicle_odometer.py`

| Field | Type | Line | Notes |
|---|---|---|---|
| `value` | Float | 14 | aggregator="max" |
| `date` | Date | 13 | default=context_today |
| `vehicle_id` | Many2one `fleet.vehicle` | 15 | required=True |
| `unit` | Selection | 16 | related via vehicle_id.odometer_unit |
| `driver_id` | Many2one `res.partner` | 17 | computed from vehicle driver; store=True |
| `name` | Char (computed) | 12 | "{vehicle_name} / {date}" |

Order: `date desc` (`_order = 'date desc'` — line 9).
Note: `_get_odometer()` searches by `order='value desc'`, not date — returns highest value, not most recent date.

---

## 7. `fleet.vehicle.model` & `fleet.vehicle.model.brand` — Hierarchy

**File**: `fleet/models/fleet_vehicle_model.py`

`fleet.vehicle.model`:
- `brand_id` (Many2one `fleet.vehicle.model.brand`, required) — line 33
- `vehicle_type` (Selection: car/bike, required, default='car') — line 38
- `FUEL_TYPES` constant: diesel/gasoline/full_hybrid/plug_in_hybrid_diesel/plug_in_hybrid_gasoline/cng/lpg/hydrogen/electric — lines 9-18
- `drive_type` (Selection: fwd/awd/rwd/4wd) — lines 66-71 **MIGRATION FLAG: new field in v19**
- `vehicle_properties_definition` (PropertiesDefinition) — line 63 **MIGRATION FLAG: new in v16+**
- `vehicle_range`, `range_unit`, `power_unit` fields — new

**File**: `fleet/models/fleet_vehicle_model_brand.py`

`fleet.vehicle.model.brand`:
- `name`, `active`, `image_128`, `model_count` (computed), `model_ids` (One2many)

---

## 8. `fleet.service.type` — Unified Service/Contract Type

**File**: `fleet/models/fleet_service_type.py`

```python
class FleetServiceType(models.Model):
    _name = 'fleet.service.type'
    category = fields.Selection([('contract', 'Contract'), ('service', 'Service')], required=True)
```

Single model serves both:
- `fleet.vehicle.log.services.service_type_id` → category='service'
- `fleet.vehicle.log.contract.cost_subtype_id` → category='contract' (domain enforced)

---

## 9. Multi-Company Support

All cost-bearing models carry `company_id`:
- `fleet.vehicle.company_id` (`fleet_vehicle.py:45`) — default=env.company
- `fleet.vehicle.log.services.company_id` (`fleet_vehicle_log_services.py:27`) — default=env.company
- `fleet.vehicle.log.contract.company_id` (`fleet_vehicle_log_contract.py:24`) — default=env.company
- `fleet.vehicle.log.contract.vehicle_id` has `check_company=True` — line 20
- `fleet.vehicle.future_driver_id` has `check_company=True` — line 60

---

## 10. MIGRATION FLAGS Summary

| Flag | Detail |
|---|---|
| `fleet.vehicle.cost` REMOVED | No such model in v19. Cost split: log.services + log.contract |
| `acquisition_date` | Field name in v19 (prior versions used `acqui_date`) |
| `drive_type` field NEW | `fleet.vehicle.model` gains fwd/awd/rwd/4wd selection (v19) |
| `vehicle_properties_definition` NEW | PropertiesDefinition on fleet.vehicle.model |
| `vehicle_properties` NEW | Properties field on fleet.vehicle linked to model definition |
| `vehicle_range` + `range_unit` NEW | Range fields on both model and vehicle |
| `fleet_vehicle_state_waiting_list` DEMO-ONLY | Referenced in code but only loaded via demo data |
| `odometer._get_odometer` uses `order='value desc'` | Returns MAX value, not most recent date |
| `fleet.vehicle.log.services.state` | new/running/done/cancelled (not in older versions) |
| `cost_frequency` on contract | no/daily/weekly/monthly/yearly — recurring cost mechanism |
