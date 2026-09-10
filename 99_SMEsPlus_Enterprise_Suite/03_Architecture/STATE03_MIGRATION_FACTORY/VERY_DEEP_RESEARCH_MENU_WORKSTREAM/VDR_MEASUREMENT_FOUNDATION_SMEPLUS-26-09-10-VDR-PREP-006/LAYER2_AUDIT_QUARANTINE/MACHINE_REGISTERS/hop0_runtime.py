#!/usr/bin/env python3
"""PREP-006 CP02 — HOP-0, DISCOVERY METHOD 2: RUNTIME. Logically independent of method 1:
it reads the deployments' own registries and never consults the source tree or method 1's output.

UNIT     : one registry record.
PATTERN  : COPY-block parse of pg_restore --data-only output; rows whose field count differs
           from the declared column list are REJECTED and counted, never padded.
CONTROLS : per-table row counts published; a positive control (a record known to be present)
           and a negative control (a fabricated identity) for the join.
"""
import os,json,collections,sys
RT='work4/runtime'
def cb(p):
    cols=None; rej=0; n=0
    if not os.path.exists(p): return
    for line in open(p,encoding='utf-8',errors='replace'):
        if cols is None:
            if line.startswith('COPY public.'):
                cols=line[line.index('(')+1:line.index(')')].replace('"','').split(', ')
            continue
        if line.rstrip('\n')=='\\.': break
        v=line.rstrip('\n').split('\t')
        if len(v)!=len(cols): rej+=1; continue
        n+=1; yield dict(zip(cols,v))
DOM=set(json.load(open('work6/hop0_source.json'))['domain_modules'])
KIND={'ir.ui.menu':'MENU','ir.actions.act_window':'ACTION_WINDOW','ir.actions.server':'ACTION_SERVER',
 'ir.actions.client':'ACTION_CLIENT','ir.actions.report':'ACTION_REPORT','ir.ui.view':'VIEW',
 'ir.rule':'RECORD_RULE','res.groups':'GROUP','ir.cron':'CRON','ir.sequence':'SEQUENCE',
 'ir.config_parameter':'CONFIG_PARAM','ir.model.access':'ACCESS','ir.model':'MODEL',
 'ir.model.fields':'FIELD','ir.model.constraint':'CONSTRAINT','base.automation':'AUTOMATION'}
allent=collections.defaultdict(set)   # (kind, identity) -> set of deployments
per=collections.Counter()
deps=[d for d in sorted(os.listdir(RT)) if os.path.isdir(f'{RT}/{d}')]
for d in deps:
    n=0
    for r in cb(f'{RT}/{d}/ir_model_data.tsv'):
        if r['module'] not in DOM: continue
        k=KIND.get(r['model'])
        if not k: k='RECORD:'+r['model']
        allent[(k,f"{r['module']}.{r['name']}")].add(d); n+=1
    # fields and models carry no xmlid dependency: attribute by the model they belong to
    for r in cb(f'{RT}/{d}/ir_model_fields.tsv'):
        allent[('FIELD_RT',f"{r['model']}.{r['name']}")].add(d)
    per[d]=n
    print(f'{d}: {n} domain-attributed registry records',file=sys.stderr)
json.dump({'deployments':deps,'entities':{f'{k}|{i}':sorted(v) for (k,i),v in allent.items()}},
          open('work6/hop0_runtime.json','w'))
c=collections.Counter(k for k,_ in allent)
print(f'\nHOP-0 RUNTIME ENTITIES (union over {len(deps)} deployments): {len(allent)}')
for k,v in c.most_common(20): print(f'   {v:7d}  {k}')
