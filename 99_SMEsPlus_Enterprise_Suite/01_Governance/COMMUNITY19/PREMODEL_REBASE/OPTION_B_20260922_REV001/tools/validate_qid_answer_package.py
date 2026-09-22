#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,re,sys
from pathlib import Path

REQ_FIELDS=['MODULE','QID','QUESTION_TYPE','QUESTION_BANK_FILE','QUESTION_BANK_SHA256','FREEZE_ID','FREEZE_HASH','LAYER','ANSWER_STATUS','ANSWER_TEXT','DISCONFIRMING_RESULT','EVIDENCE_IDS','SOURCE_UNIT_IDS','SOURCE_PROOF','CONFIGURATION_PROOF','RUNTIME_PROOF','CROSS_MODULE_PROOF','E2E_PROOF','APPLICABILITY_REASON','FUNCTION_CANDIDATE_IDS','RULE_IDS','SCENARIO_IDS','GAP_IDS','CRQ_IDS','WORKER_CONTEXT_ID','ATTEMPT','ANSWERED_AT']
STATUSES={'ANSWERED','NOT_APPLICABLE','NOT_OBSERVED','NOT_FOUND_IN_SOURCE'}
LAYERS={'BASE','PROCESS'}

def sha(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def qids(path):
 t=path.read_text(encoding='utf-8'); return set(re.findall(r'\*\*(STD-Q\d{2})\s+—',t))|set(re.findall(r'## (G\d{2}-[A-Z0-9_]+-Q\d{3})',t))
def manifest(path):
 out={}
 for ln in path.read_text(encoding='utf-8').splitlines():
  if ln.strip():
   d,r=ln.split('  ',1);out[r]=d
 return out
def main():
 a=argparse.ArgumentParser();a.add_argument('--module',required=True);a.add_argument('--answer-dir',required=True);a.add_argument('--standard-bank',required=True);a.add_argument('--module-bank',required=True);a.add_argument('--expected-count',type=int,required=True);x=a.parse_args()
 root=Path(x.answer_dir); checks=[]
 expected=qids(Path(x.standard_bank))|qids(Path(x.module_bank))
 checks.append(('question universe',len(expected)==x.expected_count,{'expected':x.expected_count,'actual':len(expected)}))
 reg=root/'01_ANSWER_REGISTER.tsv'
 if not reg.is_file(): print('FAIL missing answer register');return 1
 with reg.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
 fields=set(rows[0]) if rows else set(); checks.append(('mandatory fields',set(REQ_FIELDS)<=fields,{'missing':sorted(set(REQ_FIELDS)-fields)}))
 keys=[(r.get('MODULE'),r.get('QID')) for r in rows]
 actual={q for m,q in keys if m==x.module}
 checks.append(('exact MODULE+QID set',len(rows)==x.expected_count and len(set(keys))==x.expected_count and actual==expected,{'rows':len(rows),'unique':len(set(keys)),'missing_qids':sorted(expected-actual),'extra_qids':sorted(actual-expected)}))
 checks.append(('answer status vocabulary',all(r.get('ANSWER_STATUS') in STATUSES for r in rows),{}))
 checks.append(('layer vocabulary',all(r.get('LAYER') in LAYERS for r in rows),{}))
 blanks=[]
 for i,r in enumerate(rows,2):
  for k in REQ_FIELDS:
   if not str(r.get(k,'')).strip(): blanks.append(f'{i}:{k}')
 checks.append(('no blank mandatory fields',not blanks,{'blanks':blanks[:30],'count':len(blanks)}))
 bad_reason=[]
 for i,r in enumerate(rows,2):
  if r['ANSWER_STATUS']!='ANSWERED' and r['APPLICABILITY_REASON'] in {'NONE','N/A',''}: bad_reason.append(i)
 checks.append(('non-answered rows have reason',not bad_reason,{'rows':bad_reason}))
 old=[]
 old_rx=re.compile(r'(C19-RE-|CF-B101S[12]-|RUL-B101S1-|GAP-B101S1-|GAP-A1-S2-)')
 for i,r in enumerate(rows,2):
  for k in ['EVIDENCE_IDS','FUNCTION_CANDIDATE_IDS','RULE_IDS','GAP_IDS','CRQ_IDS']:
   if old_rx.search(r.get(k,'')): old.append(f'{i}:{k}')
 checks.append(('no pre-model answer carry-forward',not old,{'hits':old[:30],'count':len(old)}))
 ev=root/'02_EVIDENCE_INDEX.tsv'; evid=set()
 if ev.is_file():
  with ev.open(encoding='utf-8',newline='') as f:
   er=list(csv.DictReader(f,delimiter='\t'))
  if er:
   idcol='EVIDENCE_ID' if 'EVIDENCE_ID' in er[0] else 'evidence_id'
   evid={r.get(idcol,'') for r in er}
 unresolved=[]
 for i,r in enumerate(rows,2):
  if r['ANSWER_STATUS']=='ANSWERED':
   ids=[z.strip() for z in re.split(r'[;,]',r['EVIDENCE_IDS']) if z.strip() and z.strip()!='NONE']
   if not ids or any(z not in evid for z in ids): unresolved.append((i,ids))
 checks.append(('answered evidence resolves',not unresolved,{'rows':unresolved[:20],'count':len(unresolved)}))
 man=root/'MANIFEST_SHA256.txt'
 if man.is_file():
  me=manifest(man); payload={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST_SHA256.txt'}
  bad=[r for r,d in me.items() if not (root/r).is_file() or sha(root/r)!=d]
  checks.append(('manifest inventory equality',set(me)==payload,{'manifest':len(me),'payload':len(payload),'missing':sorted(payload-set(me)),'extra':sorted(set(me)-payload)}))
  checks.append(('manifest hashes verify',not bad,{'bad':bad}))
 else: checks.append(('manifest present',False,{}))
 ok=True
 for n,s,d in checks:print(('PASS' if s else 'FAIL'),n,d);ok&=s
 print('SUMMARY',f'{sum(s for _,s,_ in checks)}/{len(checks)} PASS')
 return 0 if ok else 1
if __name__=='__main__':sys.exit(main())
