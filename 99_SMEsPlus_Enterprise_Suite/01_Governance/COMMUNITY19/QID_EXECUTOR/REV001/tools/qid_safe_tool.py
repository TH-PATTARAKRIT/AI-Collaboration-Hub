#!/usr/bin/env python3
import hashlib,json,subprocess,sys
from pathlib import Path

def sha(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def manifest(root):
 rows=[]
 for p in sorted(root.rglob('*')):
  if p.is_file() and not p.is_symlink() and p.name!='MANIFEST_SHA256.txt': rows.append((p.relative_to(root).as_posix(),sha(p)))
 (root/'MANIFEST_SHA256.txt').write_text(''.join(f'{d}  {r}\n' for r,d in rows),encoding='utf-8')
def main():
 if len(sys.argv)<3: print('USAGE config preflight|seal|validate|finalize');return 2
 cfg=Path(sys.argv[1]);cmd=sys.argv[2];c=json.loads(cfg.read_text(encoding='utf-8'));root=Path(c['output_dir']);root.mkdir(parents=True,exist_ok=True)
 pre=[sys.executable,str(Path(__file__).with_name('qid_preflight.py')),'--config',str(cfg)]
 val=[sys.executable,str(Path(__file__).with_name('validate_qid_answer_package.py')),'--module',c['module'],'--answer-dir',str(root),'--standard-bank',c['standard_bank'],'--module-bank',c['module_bank'],'--expected-count',str(c['expected_answer_rows'])]
 if cmd=='preflight':return subprocess.call(pre)
 if cmd=='seal':manifest(root);print(json.dumps({'status':'PASS','manifest_sha256':sha(root/'MANIFEST_SHA256.txt')}));return 0
 if cmd=='validate':return subprocess.call(val)
 if cmd=='finalize':
  if subprocess.call(pre):return 2
  manifest(root)
  rc=subprocess.call(val)
  print(json.dumps({'status':'PASS' if rc==0 else 'FAIL','manifest_sha256':sha(root/'MANIFEST_SHA256.txt')}))
  return rc
 return 2
if __name__=='__main__':raise SystemExit(main())
