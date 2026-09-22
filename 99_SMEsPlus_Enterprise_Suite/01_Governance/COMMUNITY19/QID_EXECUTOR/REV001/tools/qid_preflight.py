#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,os,subprocess,sys
from pathlib import Path

def sha(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def freeze_hash(d):
 p=d['batch_id']+'\n'+'\n'.join(sorted(d['modules']))+'\n'+'\n'.join(f'{k}:{v}' for k,v in sorted(d['bank_files'].items()))+'\n';return hashlib.sha256(p.encode()).hexdigest()
def main():
 a=argparse.ArgumentParser();a.add_argument('--config',required=True);x=a.parse_args();c=json.loads(Path(x.config).read_text(encoding='utf-8'))
 v1=Path(c['v1_register']); rows=[]
 with v1.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
 rec=next((r for r in rows if r['technical_name']==c['module']),None)
 errors=[]
 if not rec: errors.append('module absent from V1.00')
 else:
  if rec['license']!='LGPL-3' or rec['admissibility']!='ALLOW': errors.append('module not admitted LGPL-3')
  root=Path(c['clean_source_root']); mod=(root/rec['relative_module_path']).resolve();
  if root.resolve() not in mod.parents: errors.append('path escape')
  man=mod/'__manifest__.py'
  if not man.is_file() or sha(man)!=rec['manifest_sha256']: errors.append('manifest hash mismatch')
  for p in mod.rglob('*'):
   if p.is_symlink(): errors.append(f'symlink:{p}'); break
 for freeze_key in ['standard_freeze','module_freeze']:
  fp=Path(c[freeze_key]['file']); d=json.loads(fp.read_text(encoding='utf-8'))
  if freeze_hash(d)!=d['freeze_hash'] or d['freeze_hash']!=c[freeze_key]['freeze_hash']: errors.append(f'{freeze_key} hash mismatch')
  for name,digest in d['bank_files'].items():
   bp=fp.parent/name
   if not bp.is_file() or sha(bp)!=digest: errors.append(f'bank drift:{name}')
 try:
  auth=json.loads(subprocess.check_output(['claude','auth','status','--json'],text=True))
  if not auth.get('loggedIn') or auth.get('authMethod')!='claude.ai' or str(auth.get('subscriptionType','')).lower()!='max': errors.append('Claude Max auth not verified')
 except Exception as e: errors.append(f'auth check failed:{e}')
 if os.environ.get('ANTHROPIC_API_KEY'): errors.append('ANTHROPIC_API_KEY is set')
 out={'status':'PASS' if not errors else 'FAIL','module':c['module'],'errors':errors,'v1_register_sha256':sha(v1),'standard_freeze':c['standard_freeze']['freeze_hash'],'module_freeze':c['module_freeze']['freeze_hash']}
 print(json.dumps(out,sort_keys=True));return 0 if not errors else 2
if __name__=='__main__':sys.exit(main())
