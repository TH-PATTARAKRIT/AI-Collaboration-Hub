#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, json, sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
ROOT = Path('/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/01_ACTIVE/AI-Collaboration-Hub-C19-OPTION-B')
COMM = ROOT / '99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19'
GMVQ = COMM / 'GMVQ/G01_PLATFORM_BASE'
S1 = Path('/Volumes/iMacSys/SMEsPlus_COMMUNITY19_CLEAN_EXECUTION_20260922/RESEARCH/COMM-G01/COMM-G01-B101-S1/A1_ATT001')
S2 = Path('/Volumes/iMacSys/SMEsPlus_COMMUNITY19_CLEAN_EXECUTION_20260922/RESEARCH/COMM-G01/COMM-G01-B101-S2/A1_ATT002')


def sha(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()


def manifest_entries(path: Path):
    out={}
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        digest, rel = line.split('  ',1)
        out[rel]=digest
    return out


def tree_hash(root: Path):
    rows=[]
    for p in sorted(root.rglob('*')):
        if p.is_symlink(): raise RuntimeError(f'symlink {p}')
        if p.is_file():
            rel=p.relative_to(root).as_posix(); rows.append((rel,sha(p),p.stat().st_size))
    payload=''.join(f'{r}\t{d}\t{s}\n' for r,d,s in rows).encode()
    return len(rows),hashlib.sha256(payload).hexdigest()


def freeze_hash(data):
    payload=data['batch_id']+'\n'+'\n'.join(sorted(data['modules']))+'\n'+\
        '\n'.join(f'{k}:{v}' for k,v in sorted(data['bank_files'].items()))+'\n'
    return hashlib.sha256(payload.encode()).hexdigest()


def fail(msg):
    print('FAIL',msg); return False

def main():
    checks=[]
    man=PKG/'MANIFEST_SHA256.txt'
    entries=manifest_entries(man)
    payload={p.relative_to(PKG).as_posix() for p in PKG.rglob('*') if p.is_file() and p.name!='MANIFEST_SHA256.txt'}
    checks.append(('inventory equality',set(entries)==payload,{'manifest':len(entries),'payload':len(payload),'missing':sorted(payload-set(entries)),'extra':sorted(set(entries)-payload)}))
    bad=[rel for rel,d in entries.items() if not (PKG/rel).is_file() or sha(PKG/rel)!=d]
    checks.append(('manifest verification',not bad,{'bad':bad}))
    with (PKG/'04_GMVQ_CANDIDATE_CROSSWALK.tsv').open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f,delimiter='\t'))
    checks.append(('crosswalk 47 unique',len(rows)==47 and len({r['source_gap_id'] for r in rows})==47,{'rows':len(rows),'unique':len({r['source_gap_id'] for r in rows})}))
    checks.append(('no coverage/reconciliation credit',all(r['coverage_eligible']=='NO' and r['reconciliation_eligible']=='NO' for r in rows),{}))
    checks.append(('no frozen mutation',all(r['frozen_bank_mutation']=='PROHIBITED' for r in rows),{}))
    known=set()
    import re
    for q in re.findall(r'\*\*(STD-Q\d{2})\s+—', (GMVQ/'QUESTION_BANK_STANDARD_55_V2.00.md').read_text(encoding='utf-8')): known.add(q)
    for q in re.findall(r'## (G01-BASE-Q\d{3})', (GMVQ/'G01_BASE_GMVQ_MVQ_50_V1.00_DRAFT.md').read_text(encoding='utf-8')): known.add(q)
    unknown=[]
    for r in rows:
        for q in r['mapped_frozen_qids'].split(';'):
            if q and q!='NONE' and q not in known: unknown.append((r['source_gap_id'],q))
    checks.append(('mapped QIDs exist',not unknown,{'unknown':unknown}))
    binds=json.loads((PKG/'05_FROZEN_QUESTION_MODEL_BINDINGS.json').read_text(encoding='utf-8'))
    checks.append(('answer row universe 105',binds['answer_row_universe']['exact_rows_for_base']==105 and binds['standard_freeze']['question_count']==55 and binds['module_freeze']['question_count']==50,{}))
    for batch,file in [('W1-STD','FREEZE_W1-STD.json'),('W1-B01','FREEZE_W1-B01.json')]:
        data=json.loads((GMVQ/file).read_text(encoding='utf-8'))
        bank_ok=all(sha(GMVQ/k)==v for k,v in data['bank_files'].items())
        checks.append((f'{batch} freeze replay',bank_ok and freeze_hash(data)==data['freeze_hash'],{'freeze':data['freeze_hash']}))
    seal_rows=[]
    with (PKG/'03_A1_PREMODEL_EXTERNAL_SEAL_REGISTER.tsv').open(encoding='utf-8',newline='') as f:
        seal_rows=list(csv.DictReader(f,delimiter='\t'))
    for rec,root in zip(seal_rows,[S1,S2]):
        count,tree=tree_hash(root)
        checks.append((f"{rec['package_id']} original unchanged",count==int(rec['original_file_count']) and tree==rec['original_tree_sha256'],{'count':count,'tree':tree}))
    forbidden=[]
    for p in (PKG/'prompts').glob('*.md'):
        t=p.read_text(encoding='utf-8')
        if 'Formal Coverage = ' in t or 'FINAL APPROVED' in t: forbidden.append(p.name)
    checks.append(('no unsupported approval language in prompts',not forbidden,{'files':forbidden}))
    ok=True
    for name,status,detail in checks:
        print(('PASS' if status else 'FAIL'),name,json.dumps(detail,ensure_ascii=False,sort_keys=True))
        ok &= status
    print('SUMMARY',f'{sum(1 for _,s,_ in checks if s)}/{len(checks)} PASS')
    return 0 if ok else 1

if __name__=='__main__': sys.exit(main())
