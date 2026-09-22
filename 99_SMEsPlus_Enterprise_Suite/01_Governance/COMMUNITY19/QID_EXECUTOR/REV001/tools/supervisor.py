#!/usr/bin/env python3
from __future__ import annotations
import csv,json,os,signal,subprocess,sys,time
from datetime import datetime,timezone,timedelta
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; QUEUE=ROOT/'01_MODULE_QUEUE.tsv'; RUNTIME=ROOT/'runtime'; MAX_WIP=4
ICT=timezone(timedelta(hours=7))
def now():return datetime.now(ICT).isoformat(timespec='seconds')
def load():
 with QUEUE.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def save(rows):
 with QUEUE.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def alive(pid):
 if not pid:return False
 try:os.kill(int(pid),0);return True
 except (OSError,ValueError):return False
def launch(row):
 m=row['module'];cfg=ROOT/'config/modules'/f'{m}.json';c=json.loads(cfg.read_text());out=Path(c['output_dir']);out.mkdir(parents=True,exist_ok=True)
 prompt=ROOT/'prompts'/f'A1_{m}.md';log=RUNTIME/f'{m}_A1_ATT001.log';lf=log.open('ab')
 cmd=['claude','-p','--safe-mode','--restricted','--strict-mcp-config','--tools','Read','Glob','Grep','Write','Bash','--model','sonnet','--effort','high','--permission-mode','auto','--permission-prompts','none','--add-dir',c['source_module_root'],'--add-dir',str(Path(c['standard_bank']).parent),'--add-dir',str(ROOT),'--add-dir','/Users/admin/.claude/bin']
 p=subprocess.Popen(cmd,stdin=prompt.open('rb'),stdout=lf,stderr=subprocess.STDOUT,cwd=out,start_new_session=True)
 row.update(state='A1-RUNNING',session_pid=str(p.pid),started_at=now())
 (RUNTIME/f'{m}_session.json').write_text(json.dumps({'pid':p.pid,'module':m,'started_at':row['started_at'],'cmd':cmd},indent=2),encoding='utf-8')
def evaluate(row):
 c=json.loads((ROOT/'config/modules'/f"{row['module']}.json").read_text());out=Path(c['output_dir'])
 if alive(row['session_pid']):return
 row['ended_at']=now()
 term=out/'TERMINAL_RESULT.json'
 if term.is_file():
  try:tr=json.loads(term.read_text());row['terminal_result']=tr.get('result','')
  except Exception:row['terminal_result']='INVALID-TERMINAL-JSON'
 val=[sys.executable,str(ROOT/'tools/validate_qid_answer_package.py'),'--module',row['module'],'--answer-dir',str(out),'--standard-bank',c['standard_bank'],'--module-bank',c['module_bank'],'--expected-count',str(c['expected_answer_rows'])]
 vr=subprocess.run(val,capture_output=True,text=True);(RUNTIME/f"{row['module']}_validation.txt").write_text(vr.stdout+vr.stderr,encoding='utf-8')
 if vr.returncode==0:
  row['state']='A1-QID-SEALED';row['terminal_result']='A1-QID-SEALED';row['output_manifest_sha256']=__import__('hashlib').sha256((out/'MANIFEST_SHA256.txt').read_bytes()).hexdigest()
 else:row['state']='A1-CORRECTION-REQUIRED';row['terminal_result']=row['terminal_result'] or 'VALIDATION-FAILED'
def main():
 RUNTIME.mkdir(exist_ok=True);(RUNTIME/'SUPERVISOR_STARTED.txt').write_text(now()+'\n')
 while True:
  rows=load()
  for r in rows:
   if r['state']=='A1-RUNNING':evaluate(r)
  active=sum(1 for r in rows if r['state']=='A1-RUNNING' and alive(r['session_pid']))
  for r in rows:
   if active>=MAX_WIP:break
   if r['state']=='ELIGIBLE-A1':launch(r);active+=1
  save(rows)
  status={'at':now(),'active_wip':active,'max_wip':MAX_WIP,'states':{}}
  for r in rows:status['states'][r['state']]=status['states'].get(r['state'],0)+1
  (RUNTIME/'STATUS.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
  time.sleep(60)
if __name__=='__main__':main()
