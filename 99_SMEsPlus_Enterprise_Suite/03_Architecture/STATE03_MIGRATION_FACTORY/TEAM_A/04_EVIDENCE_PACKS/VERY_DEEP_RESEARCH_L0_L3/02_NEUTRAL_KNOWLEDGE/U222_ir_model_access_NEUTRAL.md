# U222 — Neutral Knowledge: Access Control List Model and Group-Based Security

**Research Unit**: U222  
**Module**: Access Control List Model  
**Version**: Odoo Community 19.0.post20260921  
**Claim Count**: 20  

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U222-C01 | FIELD-MODEL | ir_model.py:2088 | model_id | IrModelAccess | always | FACT | The access control record links to a model via a required many-to-one field with cascade deletion; removing the model removes all its access records | Access control record to model link field |
| U222-C02 | FIELD-GROUP | ir_model.py:2089 | group_id | IrModelAccess | always | FACT | The group field is optional; a null value designates a global access record that applies to all users regardless of group membership | Optional group field on access record |
| U222-C03 | FIELD-PERMS | ir_model.py:2090-2093 | perm_read/write/create/unlink | IrModelAccess | always | FACT | Four boolean permission fields individually control read, write, create, and delete operations; each is evaluated independently per access record | Four-permission boolean fields |
| U222-C04 | FIELD-SUDO-BLOCK | ir_model.py:2084 | _allow_sudo_commands | IrModelAccess | always | SECURITY | Setting the allow-sudo-commands attribute to false on the access control model prevents elevated-privilege operations on the access control table itself | Sudo command block on access control model |
| U222-C05 | GROUP-NAMES | ir_model.py:2096-2115 | group_names_with_access | IrModelAccess | access_mode in read/write/create/unlink | FACT | The method returns human-readable group names that have a given permission on a model by joining the access table with the group and privilege tables; groups without a privilege category are returned without a prefix | Visible group names for a permission mode |
| U222-C06 | GROUP-NAMES-PRIV | ir_model.py:2109 | group_names_with_access SQL | IrModelAccess | always | V19-NEW | The query joins a privilege category table (left join) so that group names are prefixed with their privilege category in the format Category/Group; this privilege table is new in version 19 | Group name with privilege category prefix |
| U222-C07 | ACCESS-GROUPS | ir_model.py:2119-2134 | _get_access_groups | IrModelAccess | no accesses found | FACT | When no access control records exist for a model and mode the method returns an empty group expression meaning no user has access | Empty group expression when no access records |
| U222-C08 | ACCESS-GROUPS-GLOBAL | ir_model.py:2132-2133 | _get_access_groups | IrModelAccess | at least one access record has null group | FACT | When any access record for the model and mode has no group the method returns a universe group expression meaning every user has access regardless of group membership | Universe expression for global access record |
| U222-C09 | ACCESS-GROUPS-CACHE | ir_model.py:2118 | _get_access_groups decorator | IrModelAccess | always | PERF | The access groups result is stored in a stable registry-level cache keyed by model name and access mode; it is cleared only when access control records are created, modified, or deleted | Stable cache for access group expressions |
| U222-C10 | ALLOWED-MODELS | ir_model.py:2141-2160 | _get_allowed_models | IrModelAccess | always | FACT | The method queries all model names for which at least one active access record grants the required permission to the current user, either through a global record or through a record whose group matches one of the user's groups | Per-user allowed models query |
| U222-C11 | ALLOWED-MODELS-OR | ir_model.py:2147-2160 | _get_allowed_models SQL | IrModelAccess | always | FACT | The SQL uses a group-by on the model name so that having any matching access record is sufficient; the combination logic is OR across all matching access records for a model | OR combination across multiple access records |
| U222-C12 | ALLOWED-MODELS-CACHE | ir_model.py:2141 | _get_allowed_models decorator | IrModelAccess | always | PERF | The allowed models result is cached per user identifier and mode; the cache is invalidated by the cache-clearing method called on every create, write, or delete of access control records | Per-user per-mode allowed models cache |
| U222-C13 | CHECK-SU | ir_model.py:2164-2166 | check method | IrModelAccess | self.env.su is True | SECURITY | When the environment has the superuser flag set the check method immediately returns true without consulting any access control record; this is the admin bypass for model-level access | Superuser bypass in access check |
| U222-C14 | CHECK-ALGO | ir_model.py:2163-2176 | check method | IrModelAccess | env.su is False | FACT | For non-superuser calls the check delegates to the allowed-models cache lookup; if the model is absent from the result and raise-exception is true an access error is raised with group information | Non-superuser access check algorithm |
| U222-C15 | GLOBAL-DEPRECATED | ir_model.py:2209-2214 | create method | IrModelAccess | group_id is null and any permission is true | V19-MIGRATE | Creating a global access record (no group) in version 19 emits a deprecation warning; every access-granting record should specify a group; global access records are a deprecated feature | Global access record deprecation warning |
| U222-C16 | CHECK-RIGHTS-DEPRECATED | orm/models.py:4167-4179 | check_access_rights | BaseModel | always | V19-MIGRATE | The check-access-rights method is marked deprecated since version 18 and delegates to check-access or has-access; callers migrating to version 19 should use the new unified access check method instead | Check access rights method deprecated since 18 |
| U222-C17 | CHECK-RULE-DEPRECATED | orm/models.py:4181-4189 | check_access_rule | BaseModel | always | V19-MIGRATE | The check-access-rule method is marked deprecated since version 18 and delegates to the unified check-access method; it is no longer a separate record-level check call | Check access rule method deprecated since 18 |
| U222-C18 | CHECK-ACCESS-UNIFIED | orm/models.py:4141-4164 | _check_access | BaseModel | always | FACT | The unified internal access check first tests model-level permission via the access control table, then tests record-level permission via record rules; record rules are only evaluated if the model-level check passes and the record set contains real stored records | Two-stage unified access check |
| U222-C19 | RULE-SU-BYPASS | ir_rule.py:120-121 | _get_rules | IrRule | self.env.su is True | SECURITY | The record rule retrieval method returns an empty rule set when the environment has the superuser flag set, meaning record rules do not apply to superuser environments; both access control and record rules share the same superuser bypass mechanism | Superuser bypass in record rule retrieval |
| U222-C20 | ACL-VS-RULE | ir_rule.py:141-173 vs ir_model.py:2163 | _compute_domain vs check | IrRule vs IrModelAccess | always | FACT | Access control records operate at model level and grant or deny access to all records of a model, while record rules operate at record level through domain filters; the check order is model-level first then record-level; failing the model-level check prevents evaluation of record-level rules | Model-level versus record-level security boundary |

---

## Key Architecture Observations

### OR Logic for ACL
Multiple ACL records for the same model are combined with OR logic: if any single record grants a user access (directly or via group membership), access is granted. This means a user with multiple groups accumulates permissions from all matching ACL records.

### Global ACL (No Group) is Deprecated
In v19, the creation of a global ACL record (null `group_id`) triggers a deprecation warning. This is a significant migration consideration: any custom modules or data files that create access records without a `group_id` should be updated to specify a group.

### Caching Architecture
Two cache levels:
1. **Per-user allowed-models cache** (`_get_allowed_models`): keyed by `uid` + `mode`; cleared on any ACL change
2. **Stable group-expression cache** (`_get_access_groups`): keyed by `model_name` + `access_mode`; cleared on any ACL change; survives across requests until ACL data changes

### Superuser Bypass Scope
`env.su` bypasses BOTH model-level ACL (in `IrModelAccess.check()`) and record-level rules (in `IrRule._get_rules()`). This is a complete security bypass for the ORM access system.

### v18/v19 API Migration
The v18 introduced `check_access()` as a unified replacement. In v19, the old `check_access_rights()` and `check_access_rule()` are still present but deprecated. Migration from older Odoo versions must replace all calls to these deprecated methods.
