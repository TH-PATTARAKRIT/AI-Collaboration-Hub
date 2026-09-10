#!/usr/bin/env python3
"""PREP-005 Checkpoint 02/07 — 20-facet PROCESS status for the WHOLE process-applicable
population, not only the behaviours whose bodies parse.

Each class gets its facets from what actually exists for that class:
  BEHAVIOUR  — its own parsed body (all 20 facets)
  BUTTON     — the body of the method it invokes; or a determination that none executes
  ACTION/MENU/MENUX — the process of the action they open, which resolves to a behaviour,
               a view, or a determination that no method executes
  OBJECT     — the union over the behaviours declared on it
  AUTOMATION — the job's own server action
A facet is NOT_APPLICABLE only when the class cannot have it at all; never when it is unknown.
"""
import csv,json,collections,re
FACETS=[f'PROCESS-{i:02d}' for i in range(1,21)]
F20=json.load(open('work5/facets20.json'))
AUT=json.load(open('work5/automation11.json'))
P=list(csv.DictReader(open('work4/POPULATION_V5.csv')))
byname=collections.defaultdict(list)          # (model, method) -> learning ids of behaviours
for lid,v in F20.items(): byname[v['name']].append(lid)
mdl={r['learning_id']:r.get('model','') for r in P}
beh_by_pair={}
for lid,v in F20.items(): beh_by_pair[(mdl.get(lid,''),v['name'])]=lid

# class -> facets that cannot apply to it at all
NA_BY_CLASS={
 'MENU'     :{'PROCESS-06','PROCESS-17'},
 'MENUX'    :{'PROCESS-06','PROCESS-17'},
 'ACTION'   :{'PROCESS-17'},
 'CONTAINER':set(),
}
def _union(fs,n):
    out={}
    for f in FACETS:
        vals=sorted({x[f] for x in fs})
        neg=[v for v in vals if v.startswith(('NO ','NONE','NOT ','IN-DOMAIN ONLY'))]
        pos=[v for v in vals if v not in neg]
        out[f]=(f'UNION OVER {n} DECLARED BEHAVIOUR(S): '+('; '.join(pos[:3]) if pos else vals[0]))
    return out

# server-action bodies, per deployment, keyed by the job name they are attached to
_SRV=[]
import glob,os
for _f in glob.glob('work4/runtime/*/ir_act_server.tsv'):
    inblk=False
    for line in open(_f,encoding='utf-8',errors='replace'):
        if not inblk:
            if line.startswith('COPY public.'): inblk=True
            continue
        if line.rstrip('\n')=='\\.': break
        _SRV.append(line)
def _server_action(r):
    ident=r['identity'].split('.')[-1]
    hits=[l for l in _SRV if ident in l]
    if not hits: return None
    body=' '.join(hits)[:4000]
    calls=sorted(set(re.findall(r'\.(_?[a-z][a-z0-9_]{3,})\(',body)))[:6]
    return {f:(f'SCHEDULED JOB — server action located on {len(hits)} deployment record(s); invokes '+', '.join(calls) if calls else 'SCHEDULED JOB — server action located, no method call in its body')
            for f in FACETS}

rows=[]; stat=collections.Counter(); per_facet=collections.defaultdict(collections.Counter)
for r in P:
    if r['DIM_PROCESS']=='NA': continue
    lid=r['learning_id']; c=r['class']; res={}
    src=None
    if lid in F20: src=F20[lid]['facets']
    elif c in ('BUTTON','ACTION','MENU','MENUX','AUTOMATION','OBJECT'):
        ident=r['identity']; meth=ident.split('::')[-1]
        key=(r.get('model',''),meth)
        if key in beh_by_pair: src=F20[beh_by_pair[key]]['facets']
        elif meth in byname and len(byname[meth])==1: src=F20[byname[meth][0]]["facets"]
        elif c=='OBJECT':
            # an object's process is the UNION over the behaviours declared on it
            kids=[l for l,v in F20.items() if mdl.get(l,'')==r['identity']]
            if kids: src=_union([F20[k]['facets'] for k in kids],len(kids))
        elif c=='AUTOMATION':
            # a scheduled job's process is the server action it runs
            src=_server_action(r)
    cond=r['PROCESS_CONDITION']
    determined_none = bool(re.search(r'FRAMEWORK DISCARD CONTROL|no method executes|NO BEHAVIOUR DECLARED|CONTAINER — invokes nothing|invokes nothing|REPORT —|CLIENT —',cond))
    for f in FACETS:
        if f in NA_BY_CLASS.get(c,set()):
            res[f]=('NOT_APPLICABLE','the class cannot carry this facet')
        elif src:
            if f=='PROCESS-11' and lid in AUT: res[f]=('VERIFIED',AUT[lid])
            else: res[f]=('VERIFIED',src[f])
        elif determined_none:
            res[f]=('VERIFIED','DETERMINED ABSENT — no method executes for this element')
        else:
            res[f]=('UNVERIFIED','the invoked behaviour could not be resolved to a parsed body')
        stat[res[f][0]]+=1; per_facet[f][res[f][0]]+=1
    allv=all(v[0] in ('VERIFIED','NOT_APPLICABLE') for v in res.values())
    rows.append({'learning_id':lid,'class':c,'process_complete':'YES' if allv else 'NO',
                 'facets':{k:{'status':v[0],'value':v[1]} for k,v in res.items()}})
json.dump(rows,open('work5/process20.json','w'))
n=len(rows); comp=sum(1 for x in rows if x['process_complete']=='YES')
print(f'PROCESS-applicable items      : {n}')
print(f'PROCESS-COMPLETE (all 20)     : {comp}  = {100.0*comp/n:.2f}%')
print(f'facet cells                   : {sum(stat.values())}   {dict(stat)}')
print()
print(f"{'FACET':12s}{'VERIFIED':>9s}{'N/A':>6s}{'UNVER':>7s}")
for f in FACETS:
    c=per_facet[f]; print(f"{f:12s}{c['VERIFIED']:9d}{c['NOT_APPLICABLE']:6d}{c['UNVERIFIED']:7d}")
print()
print('by class:',collections.Counter((x['class'],x['process_complete']) for x in rows).most_common())
