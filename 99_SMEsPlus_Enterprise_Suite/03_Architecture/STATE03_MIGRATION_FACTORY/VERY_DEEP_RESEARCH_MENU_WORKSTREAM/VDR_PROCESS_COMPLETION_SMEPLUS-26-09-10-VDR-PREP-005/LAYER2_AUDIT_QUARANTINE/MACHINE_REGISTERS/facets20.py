#!/usr/bin/env python3
"""PREP-005 Checkpoint 02 — the 20-FACET PROCESS MODEL, AST-derived.

Every predicate that a challenger falsified in PREP-003/004 is rebuilt here on AST nodes
rather than on substrings, and each rebuild is noted at its facet.

FACET STATUS VOCABULARY (§5): VERIFIED | NOT_APPLICABLE | UNVERIFIED | BLOCKED | CONTRADICTED
A facet is VERIFIED when its value is DETERMINED for that item, including a determination of
"absent". UNVERIFIED means the instrument could not reach it. Unknown is never NOT_APPLICABLE.
"""
import ast,os,sys,json,collections,re

R1=sys.argv[1]
POP=sys.argv[2]
P=json.load(open(POP))

# ---- the domain module set: used to tell an IN-DOMAIN model access from a CROSS-DOMAIN one.
# PREP-004 challenge A-13: the old predicate matched any ORM access and was labelled
# "calls another domain". It could not fail. This is the repair.
DOMAIN_MODULES={r['module'] for r in P if r.get('module')}
OWNED_MODELS={r['identity'] for r in P if r['class']=='OBJECT'}
BOUNDARY_MODELS={r['identity'] for r in P if r['class']=='HANDOFF'}

FACETS=[('PROCESS-01','Entry Point'),('PROCESS-02','Preconditions'),('PROCESS-03','Input Validation'),
 ('PROCESS-04','Business Rules'),('PROCESS-05','Decision Branches'),('PROCESS-06','Calculation Logic'),
 ('PROCESS-07','State Transition'),('PROCESS-08','Internal Actions'),('PROCESS-09','Data Read'),
 ('PROCESS-10','Data Write / Mutation'),('PROCESS-11','Automation'),('PROCESS-12','Scheduler'),
 ('PROCESS-13','Cross-Module Trigger'),('PROCESS-14','Cross-Module Consumption'),
 ('PROCESS-15','Error Handling'),('PROCESS-16','Failure Path'),('PROCESS-17','Retry / Recovery'),
 ('PROCESS-18','Cancel'),('PROCESS-19','Reverse / Return'),('PROCESS-20','Output / Handoff')]

# SELF-CAUGHT DEFECT, PREP-005: the first version of these used \b word boundaries.
# In an identifier like action_cancel the underscore IS a word character, so \bcancel\b
# cannot match — the predicate returned a clean 0 of 614 for CANCEL and could not fire.
# Caught by a positive control drawn from the corpus BEFORE publication. Now matched on
# underscore-separated identifier tokens, which is the shape identifiers actually have.
CANCEL_TOK={'cancel','abort','discard','revert','unreserve'}
REVERSE_TOK={'reverse','refund','return','returns','undo','rollback','unbuild','scrap','unbook'}
RETRY_TOK={'retry','reprocess','resend','savepoint','rollback','attempt','recover','resync'}
def _tok(name): return set(re.split(r'[^a-zA-Z]+',name.lower()))-{''}
class _M:
    def __init__(s,toks): s.t=toks
    def search(s,name): return bool(_tok(name)&s.t)
CANCEL_RE=_M(CANCEL_TOK); REVERSE_RE=_M(REVERSE_TOK); RETRY_RE=_M(RETRY_TOK)
ROUND_RE={'round','float_round','float_compare','float_is_zero','quantize'}

def env_models(node):
    """Models accessed via env['x.y'] — AST, so it cannot match a comment or a docstring."""
    out=set()
    for n in ast.walk(node):
        if isinstance(n,ast.Subscript):
            v=n.value
            if isinstance(v,ast.Attribute) and v.attr=='env':
                s=n.slice
                if isinstance(s,ast.Constant) and isinstance(s.value,str): out.add(s.value)
    return out

def called_methods(node):
    out=collections.Counter()
    for n in ast.walk(node):
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute): out[n.func.attr]+=1
    return out

def analyse(node,seg,item):
    d={}; st={}
    def put(fid,val,status='VERIFIED'):
        d[fid]=val; st[fid]=status
    # 01 ENTRY POINT — decorators, or how it is reached
    decs=[ast.unparse(x) for x in node.decorator_list]
    put('PROCESS-01', ('DECORATED: '+', '.join(x[:44] for x in decs)) if decs else 'CALLED DIRECTLY')
    # 02 PRECONDITIONS — AST: first statement is a guard, or a single-record assertion anywhere
    body=node.body
    first=body[1] if (body and isinstance(body[0],ast.Expr) and isinstance(getattr(body[0],'value',None),ast.Constant) and len(body)>1) else (body[0] if body else None)
    entry_guard = isinstance(first,ast.If) and all(isinstance(s,(ast.Return,ast.Raise,ast.Continue,ast.Pass)) for s in first.body)
    cm=called_methods(node)
    pre=[]
    if 'ensure_one' in cm: pre.append('single-record assertion')
    if entry_guard: pre.append('entry guard')      # AST-anchored; PREP-004 B-12 showed the old regex counted guards anywhere
    put('PROCESS-02', ' + '.join(pre) if pre else 'NONE DETECTED')
    # 03 INPUT VALIDATION — raises of a validation/user error
    raises=[n for n in ast.walk(node) if isinstance(n,ast.Raise)]
    exc_names=set()
    for r_ in raises:
        e=r_.exc
        f=e.func if isinstance(e,ast.Call) else e
        nm=getattr(f,'id',None) or getattr(f,'attr',None)
        if nm: exc_names.add(nm)
    val=[e for e in exc_names if 'Validation' in e or 'UserError' in e]
    put('PROCESS-03', ('RAISES '+', '.join(sorted(val))) if val else 'NONE DETECTED')
    # 04 BUSINESS RULES — a constrains decorator, or a guard that raises
    guard_raise=any(isinstance(n,ast.If) and any(isinstance(s,ast.Raise) for s in ast.walk(n)) for n in ast.walk(node))
    br=[]
    if any('constrains' in x for x in decs): br.append('declared constraint')
    if guard_raise: br.append('conditional refusal')
    put('PROCESS-04', ' + '.join(br) if br else 'NONE DETECTED')
    # 05 DECISION BRANCHES
    put('PROCESS-05', str(sum(1 for n in ast.walk(node) if isinstance(n,(ast.If,ast.IfExp)))))
    # 06 CALCULATION LOGIC — arithmetic on values, or a rounding/comparison helper. NEW.
    arith=sum(1 for n in ast.walk(node) if isinstance(n,ast.BinOp) and isinstance(n.op,(ast.Add,ast.Sub,ast.Mult,ast.Div,ast.FloorDiv,ast.Mod,ast.Pow)))
    rounders=sorted(ROUND_RE & set(cm))
    aug=sum(1 for n in ast.walk(node) if isinstance(n,ast.AugAssign))
    if arith or rounders or aug:
        put('PROCESS-06', f'ARITHMETIC {arith+aug} op(s)'+(f'; rounding via {",".join(rounders)}' if rounders else '; NO ROUNDING CONTROL'))
    else:
        put('PROCESS-06','NO CALCULATION')
    # 07 STATE TRANSITION — writes a state key, vs merely reads .state
    writes_state=False
    for n in ast.walk(node):
        if isinstance(n,ast.Dict):
            for k in n.keys:
                if isinstance(k,ast.Constant) and k.value=='state': writes_state=True
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='write':
            for a in n.args:
                if isinstance(a,ast.Dict):
                    for k in a.keys:
                        if isinstance(k,ast.Constant) and k.value=='state': writes_state=True
    reads_state=any(isinstance(n,ast.Attribute) and n.attr=='state' for n in ast.walk(node))
    put('PROCESS-07','WRITES state' if writes_state else ('READS state' if reads_state else 'NONE'))
    # 08 INTERNAL ACTIONS — calls to other methods on self
    selfcalls=sorted({n.func.attr for n in ast.walk(node) if isinstance(n,ast.Call)
                      and isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='self'})
    put('PROCESS-08', f'{len(selfcalls)} self-method call(s)'+(': '+', '.join(selfcalls[:6]) if selfcalls else ''))
    # 09 DATA READ — NEW
    readers=sorted({m for m in cm if m in ('search','search_read','search_count','read','browse','mapped','filtered','read_group','_read_group','exists')})
    models=env_models(node)
    put('PROCESS-09', (f'{", ".join(readers)}' if readers else 'NO EXPLICIT READ')+(f'; via env: {len(models)} model(s)' if models else ''))
    # 10 DATA WRITE — AST call nodes only. PREP-004 CH-07: the old pattern matched the method's own name.
    writers=sorted({m for m in cm if m in ('write','create','unlink','copy','_write','_create')})
    put('PROCESS-10', 'WRITES via '+', '.join(writers) if writers else 'NO WRITE')
    # 11 AUTOMATION — is this behaviour referenced by an automated rule or a job?
    put('PROCESS-11','SEE PROCESS-12; no automated-rule reference resolvable from the body alone','UNVERIFIED')
    # 12 SCHEDULER — decorator/name evidence of background execution
    sched = any('_cron' in x or 'autovacuum' in x for x in decs) or node.name.startswith('_cron') or '_cron_' in node.name
    put('PROCESS-12','SCHEDULED ENTRY POINT' if sched else 'NOT A SCHEDULED ENTRY POINT')
    # 13/14 CROSS-MODULE — split IN-DOMAIN from OUT-OF-DOMAIN. The PREP-004 repair.
    ext=sorted(m for m in models if m not in OWNED_MODELS)
    ind=sorted(m for m in models if m in OWNED_MODELS)
    trig=[m for m in ext if m in BOUNDARY_MODELS]
    put('PROCESS-13', f'{len(trig)} boundary object(s): {", ".join(trig[:5])}' if trig else 'NO BOUNDARY TRIGGER')
    put('PROCESS-14', f'{len(ext)} external model(s) accessed; {len(ind)} in-domain' if ext else f'IN-DOMAIN ONLY ({len(ind)} model(s))')
    # 15 ERROR HANDLING — AST Try, not the word "except"
    tries=[n for n in ast.walk(node) if isinstance(n,ast.Try)]
    handlers=sum(len(t.handlers) for t in tries)
    bare=any(h.type is None for t in tries for h in t.handlers)
    put('PROCESS-15', (f'{len(tries)} try block(s), {handlers} handler(s)'+(' — INCLUDES A BARE CATCH-ALL' if bare else '')) if tries else 'NOT HANDLED')
    # 16 FAILURE PATH — what happens when it refuses
    put('PROCESS-16', f'{len(raises)} raise site(s): {", ".join(sorted(exc_names)[:4])}' if raises else 'NO EXPLICIT FAILURE PATH')
    # 17 RETRY / RECOVERY — NEW
    commits=[m for m in cm if m in ('commit','rollback','savepoint','flush')]
    if commits or RETRY_RE.search(node.name):
        put('PROCESS-17', 'TRANSACTION CONTROL: '+', '.join(sorted(set(commits))) if commits else 'NAMED AS A RETRY PATH')
    else:
        put('PROCESS-17','NO RETRY OR RECOVERY PATH')
    # 18 CANCEL — NEW
    cancels=sorted({m for m in cm if CANCEL_RE.search(m)})
    put('PROCESS-18', ('IS A CANCEL PATH' if CANCEL_RE.search(node.name) else 'CALLS '+', '.join(cancels[:4])) if (cancels or CANCEL_RE.search(node.name)) else 'NO CANCEL PATH')
    # 19 REVERSE / RETURN — NEW
    revs=sorted({m for m in cm if REVERSE_RE.search(m)})
    put('PROCESS-19', ('IS A REVERSE/RETURN PATH' if REVERSE_RE.search(node.name) else 'CALLS '+', '.join(revs[:4])) if (revs or REVERSE_RE.search(node.name)) else 'NO REVERSE/RETURN PATH')
    # 20 OUTPUT / HANDOFF
    returns=[n for n in ast.walk(node) if isinstance(n,ast.Return) and n.value is not None]
    act=any(isinstance(n,ast.Dict) and any(isinstance(k,ast.Constant) and k.value=='type' for k in n.keys)
            and any(isinstance(v,ast.Constant) and isinstance(v.value,str) and v.value.startswith('ir.actions') for v in n.values)
            for n in ast.walk(node))
    put('PROCESS-20','RETURNS AN ACTION' if act else (f'RETURNS A VALUE ({len(returns)} site(s))' if returns else 'RETURNS NOTHING'))
    return d,st

def main():
    beh=[r for r in P if r['class']=='BEHAVIOUR']
    byfile=collections.defaultdict(list)
    for r in beh:
        ev=r['evidence_pointer']
        if ':' in ev:
            f,ln=ev.rsplit(':',1)
            if ln.isdigit(): byfile[f].append((int(ln),r))
    out={}; miss=0; readfail=0; parsefail=0; exact=0; fallback=0
    for f,items in byfile.items():
        p=os.path.join(R1,f)
        try: src=open(p,encoding='utf-8',errors='replace').read()
        except Exception: readfail+=len(items); continue
        try: tree=ast.parse(src)
        except Exception: parsefail+=len(items); continue
        lines=src.split('\n')
        fn={n.lineno:n for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
        for ln,r in items:
            node=fn.get(ln)
            if node is None:
                cand=sorted(fn,key=lambda k:abs(k-ln))
                node=fn[cand[0]] if cand and abs(cand[0]-ln)<=2 else None
                if node is not None: fallback+=1
            else: exact+=1
            if node is None: miss+=1; continue
            seg='\n'.join(lines[node.lineno-1:(node.end_lineno or node.lineno)])
            d,st=analyse(node,seg,r)
            out[r['learning_id']]={'facets':d,'status':st,'name':node.name,'file':f,'line':node.lineno}
    json.dump(out,open('work5/facets20.json','w'))
    print(f'BEHAVIOUR items {len(beh)} | resolved {len(out)} (exact {exact}, ±2 fallback {fallback}) | unresolved {miss} | read-fail {readfail} | parse-fail {parsefail}')
    print(f'COVERAGE ASSERTION: {len(out)}/{len(beh)} = {100.0*len(out)/len(beh):.1f}%')
    print()
    for fid,fname in FACETS:
        c=collections.Counter(v['status'][fid] for v in out.values())
        vals=collections.Counter(v['facets'][fid].split(';')[0].split(':')[0].strip() for v in out.values())
        top=' | '.join(f'{k}={n}' for k,n in vals.most_common(3))
        print(f"{fid} {fname:26s} VERIFIED={c['VERIFIED']:4d} UNVERIFIED={c['UNVERIFIED']:4d}   {top[:72]}")
main()
