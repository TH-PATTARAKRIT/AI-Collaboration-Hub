#!/usr/bin/env python3
"""PREP-006 CP06 — MEASUREMENT INSTRUMENTS.

ANTI-SELF-REFERENCE CONTRACT (§2, §13). Each instrument declares its INPUT FIELDS. The harness
enforces that an instrument never reads a field that any instrument writes. An instrument that
would grade a field produced by the measurement process is rejected before it runs.

Every instrument returns (verdict, evidence) — never a boolean — so a verdict always carries
the observation it rests on.
"""
import os,re,json

ROOT=None   # set by the harness

# ---- INS-01  SOURCE PRESENCE -----------------------------------------------------------
INS01_INPUTS={'source_pointer'}
def INS01_source_presence(item):
    """OBSERVATION: does the pointer resolve to a file, and to a line inside it?"""
    p=(item.get('source_pointer') or '').strip()
    if not p: return ('SOURCE_UNRESOLVED','no pointer')
    path,_,ln=p.rpartition(':')
    if path and ln.isdigit():
        f=os.path.join(ROOT,path)
        if not os.path.exists(f): return ('SOURCE_UNRESOLVED',f'no such file: {path}')
        try: n=sum(1 for _ in open(f,encoding='utf-8',errors='replace'))
        except OSError: return ('SOURCE_UNRESOLVED','unreadable')
        if int(ln)>n: return ('SOURCE_UNRESOLVED',f'line {ln} beyond end of file ({n} lines)')
        return ('SOURCE_RESOLVED',f'{path}:{ln} of {n} lines')
    f=os.path.join(ROOT,p)
    if os.path.exists(f): return ('SOURCE_FILE_ONLY',f'{p} exists, no line')
    return ('SOURCE_UNRESOLVED',f'no such path: {p}')

# ---- INS-02  RUNTIME OBSERVATION --------------------------------------------------------
INS02_INPUTS={'observed_on'}
def INS02_runtime(item):
    d=[x for x in (item.get('observed_on') or '').split(';') if x]
    return (('OBSERVED',f'{len(d)} deployment(s): {",".join(d)}') if d else ('ABSENT','on no deployment'))

# ---- INS-03  FOUR-WAY CLASSIFICATION ----------------------------------------------------
INS03_INPUTS={'source_pointer','observed_on'}
def INS03_fourway(item):
    s=INS01_source_presence(item)[0]; r=INS02_runtime(item)[0]
    if s!='SOURCE_UNRESOLVED' and r=='OBSERVED': return ('BOTH','source resolves and runtime observed')
    if s!='SOURCE_UNRESOLVED': return ('SOURCE_ONLY','source resolves, observed nowhere')
    if r=='OBSERVED': return ('RUNTIME_ONLY','observed, source does not resolve')
    return ('NEITHER','neither resolves')

# ---- INS-04  EXCLUSION LEGITIMACY (§6 prohibited reasons) --------------------------------
INS04_INPUTS={'na_reason','gate','active','module','kind','gate_state','invisible_unless_state'}
PROHIBITED=('hidden','disabled','optional','configuration-dependent','another module owns',
            'cannot reach','default configuration','no access-control surface of its own',
            'holds no data of its own')
def INS04_exclusion(item):
    """An item may never leave the population for a §6 reason. A persistent model asserted to
    have no security or no data of its own is rejected outright."""
    reason=(item.get('na_reason') or '').lower()
    if reason:
        for p in PROHIBITED:
            if p in reason: return ('NA_REJECTED',f'§6-prohibited reason: "{p}"')
        return ('NA_ACCEPTED',reason[:60])
    return ('IN_POPULATION','no exclusion asserted')

# ---- INS-05  CANCEL / REVERSE PATH ------------------------------------------------------
INS05_INPUTS={'identity'}
CANCEL_TOK={'cancel','abort','discard','revert','unreserve'}
REVERSE_TOK={'reverse','refund','return','returns','undo','rollback','unbuild','scrap'}
def INS05_edge(item):
    name=(item.get('identity') or '').split('::')[-1]
    toks=set(re.split(r'[^a-zA-Z]+',name.lower()))-{''}
    if toks & CANCEL_TOK:  return ('CANCEL_PATH',f'identifier token in {sorted(toks & CANCEL_TOK)}')
    if toks & REVERSE_TOK: return ('REVERSE_PATH',f'identifier token in {sorted(toks & REVERSE_TOK)}')
    return ('NO_EDGE_PATH','no cancel or reverse token in the identifier')

# ---- INS-06  CONTRADICTION ---------------------------------------------------------------
INS06_INPUTS={'dim_state','rv_state','fallback'}
def INS06_contradiction(item):
    if item.get('dim_state')=='NOT_VERIFIED' and item.get('rv_state')=='RESEARCH_VERIFIED':
        return ('CONTRADICTION','not-verified and research-verified on the same cell')
    if item.get('fallback'): return ('FALLBACK_FLAGGED',f"silent fallback to {item['fallback']}")
    return ('CONSISTENT','no contradiction detected')

# ---- INS-07  DUPLICATE --------------------------------------------------------------------
INS07_INPUTS={'identity'}
def INS07_duplicate(item,seen):
    i=item.get('identity')
    if i in seen: return ('DUPLICATE_OF_'+seen[i],f'identity already seen as {seen[i]}')
    return ('UNIQUE','first occurrence')

INSTRUMENTS={
 'INS-01':('Source Presence',INS01_source_presence,INS01_INPUTS),
 'INS-02':('Runtime Observation',INS02_runtime,INS02_INPUTS),
 'INS-03':('Four-Way Classification',INS03_fourway,INS03_INPUTS),
 'INS-04':('Exclusion Legitimacy',INS04_exclusion,INS04_INPUTS),
 'INS-05':('Cancel / Reverse Path',INS05_edge,INS05_INPUTS),
 'INS-06':('Contradiction',INS06_contradiction,INS06_INPUTS),
 'INS-07':('Duplicate',INS07_duplicate,INS07_INPUTS),
}
# Fields any instrument WRITES. The anti-self-reference test asserts this is disjoint from
# every instrument's INPUTS. It is deliberately empty: no instrument writes to the item.
WRITTEN_FIELDS=set()
