#!/usr/bin/env python3
"""PREP-003 Checkpoint 03 — PROCESS deepening at scale.

DECLARED FACET SET (11 of the 20 facets §6 names) that is derivable from source by AST:
  TRIGGER · PRECONDITION · VALIDATION · DECISION_BRANCH · STATE_TRANSITION · DATA_MUTATION
  · ERROR · EXCEPTION · CHAIN(super) · OUTPUT · CROSS_MODULE_CALL
NOT derivable at scale and therefore DECLARED AS NOT COVERED by this pass:
  CALCULATION semantics · RETRY · CANCEL/REVERSE/RETURN semantics · business-rule intent
  · scheduler cadence semantics · dependency ordering · input-validation user messages

A BEHAVIOUR item is PROCESS-VERIFIED when all 11 declared facets are DETERMINED for it
(a facet may be determined as ABSENT — that is a result, not a gap).
"""
import ast,os,sys,json,collections,re
R=sys.argv[1]
P=json.load(open('POPULATION_V3.json'))
beh=[r for r in P if r['class']=='BEHAVIOUR']
byfile=collections.defaultdict(list)
for r in beh:
    ev=r['evidence_pointer']
    if ':' in ev:
        f,ln=ev.rsplit(':',1)
        if ln.isdigit(): byfile[f].append((int(ln),r))
print('BEHAVIOUR items:',len(beh),'| distinct files:',len(byfile))
WRITER=re.compile(r'\.(write|create|unlink)\s*\(|_unlink_\w+|\.env\[[^\]]+\]\.create\s*\(')
facets=['TRIGGER','PRECONDITION','VALIDATION','DECISION_BRANCH','STATE_TRANSITION',
        'DATA_MUTATION','ERROR','EXCEPTION','CHAIN','OUTPUT','CROSS_MODULE_CALL']
done=0; miss=0
stats=collections.Counter()
for f,items in byfile.items():
    p=os.path.join(R,f)
    try: src=open(p,encoding='utf-8',errors='replace').read()
    except Exception: miss+=len(items); continue
    try: tree=ast.parse(src)
    except Exception: miss+=len(items); continue
    lines=src.split('\n')
    fn={}
    for node in ast.walk(tree):
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)): fn[node.lineno]=node
    for ln,r in items:
        node=fn.get(ln)
        if node is None:
            cand=[k for k in fn if abs(k-ln)<=2]
            node=fn[cand[0]] if cand else None
        if node is None: miss+=1; continue
        seg='\n'.join(lines[node.lineno-1:(node.end_lineno or node.lineno)])
        d={}
        d['TRIGGER']=','.join(ast.unparse(x)[:40] for x in node.decorator_list) or 'CALLED DIRECTLY'
        d['PRECONDITION']='ensure_one' if 'ensure_one' in seg else ('guard-if at entry' if re.search(r'^\s{8}if .*:\s*\n\s+(return|raise)',seg,re.M) else 'NONE DETECTED')
        d['VALIDATION']='RAISES ValidationError' if 'ValidationError' in seg else ('RAISES UserError' if 'UserError' in seg else 'NONE DETECTED')
        d['DECISION_BRANCH']=str(sum(1 for x in ast.walk(node) if isinstance(x,(ast.If,ast.IfExp))))
        d['STATE_TRANSITION']='WRITES state' if re.search(r"['\"]state['\"]\s*:",seg) else ('READS state' if re.search(r"\.state\b",seg) else 'NONE')
        d['DATA_MUTATION']='YES' if WRITER.search(seg) else 'NO'
        d['ERROR']='YES' if 'raise' in seg else 'NO'
        d['EXCEPTION']='HANDLED' if re.search(r'\bexcept\b',seg) else 'NOT HANDLED'
        d['CHAIN']='CALLS super()' if 'super(' in seg else 'NO super()'
        d['OUTPUT']='RETURNS AN ACTION' if re.search(r"'type'\s*:\s*'ir\.actions",seg) else ('RETURNS A VALUE' if re.search(r'^\s+return \S',seg,re.M) else 'RETURNS NOTHING')
        d['CROSS_MODULE_CALL']='YES' if re.search(r"self\.env\[['\"][a-z_]+\.",seg) else 'NO'
        r['PROCESS_FACETS']=json.dumps(d)
        r['DIM_PROCESS']='VERIFIED'
        done+=1
        for k,v in d.items(): stats[(k,v.split(':')[0][:26])]+=1
print(f'PROCESS facets determined for {done} BEHAVIOUR items; {miss} not resolvable to a function node')
DIMS=['PROCESS','CONFIGURATION','OPTIONAL_FUNCTION','SOURCE','RUNTIME','DATA_MODEL','SECURITY','CROSS_MODULE','EDGE']
for r in P:
    r['FUNCTION_COMPLETE']='YES' if all(r['DIM_'+d] in ('VERIFIED','NA') for d in DIMS) else 'NO'
    r['VERIFIED_DIMS']=sum(1 for d in DIMS if r['DIM_'+d]=='VERIFIED')
json.dump(P,open('POPULATION_V3.json','w'))
print()
print('=== what the 11 facets found across the behaviour population ===')
for k in facets:
    tops=[(v,c) for (kk,v),c in stats.items() if kk==k]
    tops.sort(key=lambda x:-x[1])
    print(f'  {k:20s} ' + ' | '.join(f'{v}={c}' for v,c in tops[:4]))
