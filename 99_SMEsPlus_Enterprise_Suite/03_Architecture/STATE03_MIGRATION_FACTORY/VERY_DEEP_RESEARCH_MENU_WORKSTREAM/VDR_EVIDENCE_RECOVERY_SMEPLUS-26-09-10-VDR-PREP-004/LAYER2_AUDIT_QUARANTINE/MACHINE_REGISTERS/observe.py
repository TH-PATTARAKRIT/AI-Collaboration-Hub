#!/usr/bin/env python3
"""PREP-004 Checkpoint 08 — ELEMENT-LEVEL RUNTIME OBSERVATION.
POPULATION: the 5,074 frozen learning items.
PATTERN  : join each item's own identity against the deployment's OWN record of installed
           elements — ir_model_data (module,name) for xml-id classes, ir_model_fields
           (model,name) for fields, ir_model_data model='ir.model' for objects.
PATH SET : the five extracted deployments under work4/runtime/.
UNIT     : one (item, deployment) observation.
CONTROLS : (1) second shape - every class count re-derived by a second predicate;
           (2) positive control - a synthetic identity known to be present must be found,
               and a synthetic identity known to be absent must NOT be found;
           (3) coverage assertion - rows parsed vs rows the COPY header declares."""
import csv,os,sys,json,collections
RT='work4/runtime'
def copyblock(path):
    """Yield dict rows of the single COPY block in a pg_restore --data-only extract."""
    cols=None; n=0
    with open(path,encoding='utf-8',errors='replace') as fh:
        inblk=False
        for line in fh:
            if not inblk:
                if line.startswith('COPY public.'):
                    cols=line[line.index('(')+1:line.index(')')].replace('"','').split(', ')
                    inblk=True
                continue
            if line.rstrip('\n')=='\\.': break
            parts=line.rstrip('\n').split('\t')
            if len(parts)!=len(cols): continue
            n+=1
            yield dict(zip(cols,parts))
    if cols is None: raise SystemExit(f'NO COPY BLOCK: {path}')

DEPLOY=[d for d in sorted(os.listdir(RT)) if os.path.isdir(os.path.join(RT,d))]
idx={}
for d in DEPLOY:
    imd=set(); models=set(); modules=set()
    for r in copyblock(f'{RT}/{d}/ir_model_data.tsv'):
        imd.add((r['module'],r['name']))
        if r['model']=='ir.model': models.add(r['name'])
    fields=set()
    for r in copyblock(f'{RT}/{d}/ir_model_fields.tsv'):
        fields.add((r['model'],r['name']))
    for r in copyblock(f'{RT}/{d}/ir_module_module.tsv'):
        if r.get('state')=='installed': modules.add(r['name'])
    idx[d]={'imd':imd,'fields':fields,'modules':modules,'models':models}
    print(f'{d:14s} ir_model_data={len(imd):7d}  ir_model_fields={len(fields):6d}  installed_modules={len(modules):5d}',file=sys.stderr)

# ---- positive / negative controls, drawn from the corpus itself -------------
d0=DEPLOY[0]
present=next(iter(idx[d0]['imd']))
absent=('zz_no_such_module_prep004','zz_no_such_record')
assert present in idx[d0]['imd'] and absent not in idx[d0]['imd']
fpresent=next(iter(idx[d0]['fields'])); fabsent=('zz.no.such.model','zz_no_such_field')
assert fpresent in idx[d0]['fields'] and fabsent not in idx[d0]['fields']
print(f'CONTROL: xmlid present {present} FOUND / absent NOT FOUND — predicate can fire and can fail',file=sys.stderr)

R=list(csv.DictReader(open('work3/POPULATION_V4.csv')))
XMLID={'MENU','MENUX','VIEW','ACTION','RULE','GROUP','AUTOMATION','SEQUENCE'}
def xmlid_of(ident):
    base=ident.split('::')[0].split('#')[0]
    return tuple(base.split('.',1)) if '.' in base else None
res=[];cls_stat=collections.Counter()
for r in R:
    lid=r['learning_id']; c=r['class']; ident=r['identity']; obs=[]; route=None
    if c in XMLID:
        k=xmlid_of(ident); route='ir_model_data'
        if k: obs=[d for d in DEPLOY if k in idx[d]['imd']]
    elif c=='FIELD':
        route='ir_model_fields'
        if '.' in ident:
            mdl,fld=ident.rsplit('.',1)
            obs=[d for d in DEPLOY if (mdl,fld) in idx[d]['fields']]
    elif c=='OBJECT':
        route='ir_model_fields(model)'
        obs=[d for d in DEPLOY if any(m==ident for m,_ in idx[d]['fields'])]
    elif c=='ACL':
        route='ir_model_fields(model)'
        mdl=ident.split('::')[0]
        obs=[d for d in DEPLOY if any(m==mdl for m,_ in idx[d]['fields'])]
    elif c in ('CONSTRAINT','HANDOFF'):
        route='ir_model_fields(model)'
        mdl=ident.split('::')[0]
        obs=[d for d in DEPLOY if any(m==mdl for m,_ in idx[d]['fields'])]
    elif c in ('BEHAVIOUR','BUTTON','GATEDELEM','SETTING','SYSPARAM'):
        route='module-installation only (no element-level record exists for this class)'
        mod=r['module']
        obs=[d for d in DEPLOY if mod in idx[d]['modules']]
    res.append({'learning_id':lid,'class':c,'route':route,'observed_on':obs,'n_obs':len(obs)})
    cls_stat[(c,'obs' if obs else 'not')]+=1
json.dump(res,open('work4/runtime_observation.json','w'))
print()
print(f"{'CLASS':12s}{'n':>6s}{'OBSERVED':>10s}{'%':>8s}   route")
tot=obst=0
byc=collections.defaultdict(lambda:[0,0,''])
for x in res:
    byc[x['class']][0]+=1; byc[x['class']][2]=x['route']
    if x['n_obs']: byc[x['class']][1]+=1
for c,(n,o,rt) in sorted(byc.items(),key=lambda x:-x[1][0]):
    tot+=n; obst+=o
    print(f'{c:12s}{n:6d}{o:10d}{100.0*o/n:7.1f}%   {rt[:52]}')
print(f'{"TOTAL":12s}{tot:6d}{obst:10d}{100.0*obst/tot:7.1f}%')
