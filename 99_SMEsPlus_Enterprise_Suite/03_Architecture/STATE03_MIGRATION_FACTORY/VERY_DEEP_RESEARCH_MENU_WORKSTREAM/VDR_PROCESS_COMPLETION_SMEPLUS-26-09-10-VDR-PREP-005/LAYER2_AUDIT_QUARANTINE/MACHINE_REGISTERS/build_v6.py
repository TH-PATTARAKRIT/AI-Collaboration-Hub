#!/usr/bin/env python3
"""POPULATION_V6 — PREP-005.

GOVERNING RULE ADOPTED THIS ROUND, after SMEs Core proved the previous grading was a string
test over columns the register itself authored (0 exceptions in 5,074 rows):

    A dimension is RESEARCH-VERIFIED only when an instrument OUTSIDE THE REGISTER
    established it for that item, and that instrument has a control that can fail.

Everything else is DETERMINED. That is a retraction, and it costs more than half the
previously published coverage.
"""
import csv,json,collections,re
DIMS=['PROCESS','CONFIGURATION','OPTIONAL_FUNCTION','SOURCE','RUNTIME','DATA_MODEL','SECURITY','CROSS_MODULE','EDGE']
R=list(csv.DictReader(open('work4/POPULATION_V5.csv')))
PROC={x['learning_id']:x for x in json.load(open('work5/process20.json'))}
OBS={o['learning_id']:o for o in json.load(open('work4/runtime_observation.json'))}
log=collections.Counter()

# ---- C1  CONTAINER population corrected: 17 -> 54 (SMEs Core D-14) -----------------
NA_CONT={'PROCESS':'grouping container — invokes nothing',
         'CONFIGURATION':'grouping container — carries no gate of its own',
         'OPTIONAL_FUNCTION':'grouping container — cannot be optionally activated on its own'}
def action_null(r):
    try: return json.loads(r['detail']).get('action') in (None,'None')
    except Exception: return False

# ---- C2  the join keys that are NOT unique to the item (SMEs Core D-12) ------------
keyc=collections.Counter()
for r in R:
    c=r['class']
    if c=='FIELD': keyc[('F',r['identity'])]+=1
    elif c in ('OBJECT','HANDOFF','ACL','CONSTRAINT'): keyc[('M',r['identity'].split('::')[0])]+=1
def key_shared(r):
    c=r['class']
    if c=='FIELD': return keyc[('F',r['identity'])]>1
    if c in ('OBJECT','HANDOFF','ACL','CONSTRAINT'): return keyc[('M',r['identity'].split('::')[0])]>1
    return False

for r in R:
    lid=r['learning_id']; c=r['class']
    if c in ('MENU','MENUX') and action_null(r):
        r['class_rule']='CONTAINER'
        for d,reason in NA_CONT.items():
            r['DIM_'+d]='NA'; r['DET_'+d]='NA'; r['RV_'+d]='NA'; r['NA_'+d]=reason
        log['C1 CONTAINER rule applied']+=1
    # ---- C3  retract every grade that was a string test over an authored column ----
    for d in ('CONFIGURATION','OPTIONAL_FUNCTION','DATA_MODEL','SECURITY','CROSS_MODULE','EDGE'):
        if r['RV_'+d]=='RESEARCH_VERIFIED':
            r['RV_'+d]='NOT_RESEARCH_VERIFIED'; log[f'C3 retracted {d}']+=1
    # ---- C4  the self-fulfilling condition string is removed (D-05) ----------------
    if r['SECURITY_CONDITION'].startswith('OBJECT-LEVEL: no groups declared on the node itself'):
        r['SECURITY_CONDITION']='NO GROUPS DECLARED ON THE NODE ITSELF — visibility inherited from its parent'
        log['C4 self-fulfilling string removed']+=1
    # ---- C5  PROCESS graded by the 20-facet AST instrument ------------------------
    if r['DIM_PROCESS']!='NA':
        p=PROC.get(lid)
        if p and p['process_complete']=='YES':
            r['DET_PROCESS']='DETERMINED'; r['RV_PROCESS']='RESEARCH_VERIFIED'; log['C5 process 20/20 verified']+=1
        elif p:
            # SMEs Core D-09: a grade that cannot fail is not a test. An item whose facets
            # could not all be resolved is NOT determined, and says so.
            r['DET_PROCESS']='NOT_DETERMINED'; r['RV_PROCESS']='NOT_RESEARCH_VERIFIED'; log['C5 process NOT determined — facets unresolved']+=1
        else:
            r['DET_PROCESS']='NOT_DETERMINED'; r['RV_PROCESS']='NOT_RESEARCH_VERIFIED'; log['C5 process not determined']+=1
    # ---- C5b  SOURCE: an item whose pointer is prose is NOT source-determined (D-09) --
    ev=r['evidence_pointer'].strip()
    if r['DIM_SOURCE']!='NA' and not re.match(r'^[\w./+-]+\.[a-z]{2,4}(:\d+)?$',ev):
        r['DET_SOURCE']='NOT_DETERMINED'; log['C5b source pointer is prose, not a path']+=1
    # ---- C6  RUNTIME: drop the cells whose join key is not the item's own (D-12) ---
    if r['DIM_RUNTIME']!='NA' and r['RV_RUNTIME']=='RESEARCH_VERIFIED' and key_shared(r):
        r['RV_RUNTIME']='NOT_RESEARCH_VERIFIED'
        r['RUNTIME_CONDITION']=(r['RUNTIME_CONDITION']+' | RETRACTED: the join key is shared with '
            'another item, so the record found is not provably this element\'s own')
        log['C6 runtime retracted — shared join key']+=1
    # ---- C7  a cell may not be NOT_VERIFIED and RESEARCH_VERIFIED at once (D-13) ---
    for d in DIMS:
        if r['DIM_'+d]=='NOT_VERIFIED' and r['RV_'+d]=='RESEARCH_VERIFIED':
            r['DIM_'+d]='VERIFIED'; log['C7 DIM/RV contradiction repaired']+=1
    r['DETERMINED_COMPLETE']='YES' if all(r['DET_'+d] in ('DETERMINED','NA') for d in DIMS) else 'NO'
    r['RESEARCH_COMPLETE'] ='YES' if all(r['RV_'+d]  in ('RESEARCH_VERIFIED','NA') for d in DIMS) else 'NO'
    r['APPLICABLE_DIMS']=sum(1 for d in DIMS if r['DIM_'+d]!='NA')
    r['RESEARCH_VERIFIED_DIMS']=sum(1 for d in DIMS if r['RV_'+d]=='RESEARCH_VERIFIED')

with open('work5/POPULATION_V6.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(R[0].keys())); w.writeheader(); w.writerows(R)
json.dump(R,open('work5/POPULATION_V6.json','w'))
print('CORRECTIONS'); [print(f'   {v:6d}  {k}') for k,v in sorted(log.items())]
print()
print(f"{'DIMENSION':20s}{'APPLIC':>8s}{'DETERM':>8s}{'DET%':>8s}{'RES-VER':>9s}{'RV%':>8s}")
ta=td=tv=0
for d in DIMS:
    a=sum(1 for r in R if r['DIM_'+d]!='NA'); dt=sum(1 for r in R if r['DET_'+d]=='DETERMINED')
    v=sum(1 for r in R if r['RV_'+d]=='RESEARCH_VERIFIED'); ta+=a; td+=dt; tv+=v
    print(f"{d:20s}{a:8d}{dt:8d}{100.0*dt/a:7.2f}%{v:9d}{100.0*v/a:7.2f}%")
print(f"{'ALL CELLS':20s}{ta:8d}{td:8d}{100.0*td/ta:7.2f}%{tv:9d}{100.0*tv/ta:7.2f}%")
print()
print('DETERMINED-COMPLETE:',sum(1 for r in R if r['DETERMINED_COMPLETE']=='YES'),'of',len(R))
print('RESEARCH-COMPLETE  :',sum(1 for r in R if r['RESEARCH_COMPLETE']=='YES'),'of',len(R))
print('verified-dims dist :',dict(sorted(collections.Counter(int(r['RESEARCH_VERIFIED_DIMS']) for r in R).items())))
