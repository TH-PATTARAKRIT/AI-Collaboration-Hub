# MCE01 — ENUMERATION RULE COMMAND FORMS (LAYER 2 / AUDIT QUARANTINE)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001`

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.** Contains vendor framework tokens.
> Boss / PMO / AI-Audit only. The Layer 1 derivative is `05_..._REVIEWER_FINDING_TO_ENUMERATION_RULE_MAP.md`.

`$A` = reference accounting addon root · `$AD` = addons tree root · `$O` = framework root.
All commands are single-pass, judgement-free, and return a count. This file is the reusable artefact:
a module adopting `SMEPLUS-DR-MC-001` substitutes its own `$A` and runs the set unchanged.

---

## `ER-01` — verify the evidence surface is current (run FIRST, always)

```bash
git fetch origin "$BRANCH" && git rev-parse HEAD && git rev-parse FETCH_HEAD
git diff --stat HEAD FETCH_HEAD
```
A negative claim made from a surface that is behind its origin is void. This round's `MCE-012`.

## `ER-00` — re-derive every published ratio from its own rows

```bash
for S in A B C D E F G H; do
  printf "%s rows=%s SC=%s PC=%s EO=%s NC=%s\n" "$S" \
    "$(grep -cE "^\| $S-[0-9]+ \|" "$F")" \
    "$(grep -E "^\| $S-[0-9]+ \|" "$F" | grep -c '`SC`')" \
    "$(grep -E "^\| $S-[0-9]+ \|" "$F" | grep -c '`PC`')" \
    "$(grep -E "^\| $S-[0-9]+ \|" "$F" | grep -c '`EO`')" \
    "$(grep -E "^\| $S-[0-9]+ \|" "$F" | grep -c '`NC`')"
done
```
Compare against the file's own summary table. This round: rows 108 `SC`, summary 104 `SC`.

## `ER-13` / `ER-14` — model, file, field and method denominators

```bash
grep -rhoE "^[[:space:]]+_name[[:space:]]*=[[:space:]]*['\"][^'\"]+" "$A" --include='*.py' | sed -E "s/.*['\"]//" | sort -u | wc -l   # 59
wc -l $WAVE_A_FILES | tail -1                                                        # 16,044 over 18 files
grep -cE "^[[:space:]]+[a-z_0-9]+ = fields\." $WAVE_A_FILES                           # 397
grep -cE "^[[:space:]]+def [a-zA-Z_]" $WAVE_A_FILES                                   # 750
```

## `ER-15` — enforcement layer: storage vs application

```bash
grep -n "_sql_constraints" $WAVE_A_FILES          # 6 blocks / 11 tuples
grep -h "@api.constrains" $WAVE_A_FILES | wc -l   # 32
```
The ratio **11 : 32** is the finding. `DR-AC-01` made mechanical.

## `ER-23` — failure and guard paths

```bash
grep -hEc "raise (UserError|ValidationError|RedirectWarning|AccessError)" $WAVE_A_FILES  # 153
```
For each guard on a measured value, read the predicate. `FX-07` is a guard testing `== 0` only.

## `ER-16` — access-control rows

```bash
tail -n +2 "$A/security/ir.model.access.csv" | grep -c .        # 132
tail -n +2 "$A/security/ir.model.access.csv" | awk -F, '$5==1 && $6==1 && $7==1'   # full-rights rows
```
Flag full rights on a measurement-defining entity held below administrator. Found `AC-01`:
`...,base.model_res_currency_rate,group_account_manager,1,1,1,1`.

## `ER-16a` — record-scoping coverage per model **(the highest-yield rule in the set)**

```bash
grep -oE 'ref="model_[a-z_0-9]+"' "$A"/security/*.xml | sed 's/.*ref="//;s/"//' | sort | uniq -c
# then, per Wave model, join against ir.model.access.csv write rights
```
Result: 31 rules over 20 models. `account.partial.reconcile`, `account.full.reconcile` and
`account.lock_exception` hold **0** rules while holding `1,1,1,1` for `group_account_user`.

Bounding the absence across the whole tree:
```bash
grep -rl "model_account_partial_reconcile" "$AD" | grep -v '\.po$'
# → only ir.model.access.csv files. No ir.rule record anywhere in 797 addons.
```

## `ER-21a` — company-scoping override declarations

```bash
grep -rn "_check_company_domain = " "$A"/models/ "$A"/wizard/     # 11, all *_parent_of
grep -n -A6 "^def check_company_domain_parent_of" "$O/models.py"  # semantics: null OR parent
```
Models **without** an override use the framework default (exact). `account.journal` overrides;
`account.move` does not. That asymmetry is `AC-03`.

## `ER-21b` — privilege-elevation sites

```bash
grep -rh '\.sudo()' "$A"/models/ | wc -l    # 93
grep -rn '\.sudo()' "$A"/models/            # then: does the guarded query carry a company clause?
```
`X-04` and `X-05` are both members. `X-05`:
`self.sudo().env['account.move'].search([('partner_id','in',self.ids)])` at
`models/partner.py:791-806` — no company clause.

## `ER-21c` — root-vs-company divergence

```bash
grep -rn "root_id" "$A"/models/ | wc -l     # 37 across 11 files
```
Pair each reader with its writer. `MCE-007` rules 2, 3, 5 are one such triple over one table.

## `ER-21d` — raw-SQL sites

```bash
grep -rh "cr.execute" "$A"/models/ | wc -l  # 62
```
Each bypasses record scoping by construction. `AC-02` is a member — and `MCE-008` shows the accepted
description of it was wrong in two particulars.

## `ER-21e` — named control-bypass tokens

```bash
for t in bypass_lock_check BYPASS_LOCK_CHECK defer_account_code_checks check_move_validity tracking_disable; do
  printf "%-28s %s\n" "$t" "$(grep -rh "$t" "$A"/models/ "$A"/wizard/ | wc -l)"
done
```
`BYPASS_LOCK_CHECK` 5 · `bypass_lock_check` 3 · `defer_account_code_checks` 3 ·
`check_move_validity` 1 · `tracking_disable` 7 · `skip_*` 48.

## `ER-10a` — database-wide configuration keys **(population closed by this rule)**

```bash
grep -rhoE "(get_param|set_param)\(['\"][a-zA-Z_0-9.]+['\"]" "$A"/models/ "$A"/wizard/ \
  | sed -E "s/.*\(['\"]//" | sort -u        # exactly 5
```

## `ER-10b` — ownership-field nullability on measurement-defining entities

```bash
grep -n "company_id = fields.Many2one" "$O/addons/base/models/res_currency.py"
grep -n -A4 "res_currency_rate_rule" "$O/addons/base/security/base_security.xml"
```
Nullable owner (no `required=True`) + a scoping rule with an explicit
`('company_id','=',False)` disjunct = cross-boundary by design. That is `SB-05`.

## `ER-20` — cross-module producers

```bash
grep -rl "env\['account.move'\]" "$AD" --include='*.py' | grep -v "/account/" \
  | grep -vE "/tests?/" | sed "s|$AD/||;s|/.*||" | sort -u | wc -l    # 38
```

## `ER-24` — negative-claim scan over the **manifest**, never over a list

```bash
ALL=$(find "$PKG" -name '*.md')                       # 64 files / 14,575 lines — the denominator
for tok in never always cannot "does not exist" "there is no" "no such" impossible \
           "no support" "no control" "no validation" anywhere; do
  printf "%-18s %s\n" "$tok" "$(grep -ohi "$tok" $ALL | wc -l)"
done
```
Scanning a *list* of files instead of the manifest is how `G06` reached 41.9% coverage while
believing it was complete.

---

## Adoption checklist for another module

1. `ER-01` — confirm the surface is current.
2. `ER-13`/`ER-14` — models, files, fields, methods. Four numbers.
3. `ER-15`, `ER-23` — enforcement layers and guard predicates.
4. `ER-16`, `ER-16a` — access rows and per-model scoping coverage. **Run `ER-16a` early; it is cheap
   and it found the most severe structural gap in this domain.**
5. `ER-21a`…`ER-21e` — the five mechanism populations. Domain-independent.
6. `ER-10a`, `ER-10b` — configuration keys and ownership nullability.
7. `ER-20`, `ER-20a` — producers and unattended jobs.
8. `ER-00`, `ER-24` — before any gate.

Total cost this round: **under one hour of mechanical execution**, for 24 verified denominators, one
closed population, one closed residual, and three defects the reviewers had not reached.
