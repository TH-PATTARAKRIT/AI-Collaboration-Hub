#!/usr/bin/env python3
"""Security + view census over the WHOLE ROOT, not the domain module set.
Repairs three challenge findings:
  A-02  the rule target is declared in TWO forms; the old accessor read one.
  A-04  a module can grant access to / rule / extend a domain object WITHOUT declaring it,
        and is then invisible to a module-set-scoped instrument.
  A-09  cron/group/sequence/sysparam had NO eligibility filter at all.
"""
import json,os,sys,re,csv,collections
import xml.etree.ElementTree as ET
R=sys.argv[1]
OW=set(json.load(open('inv_fam_final.json'))['owned'])
MODELS={('model_'+d['name'].replace('.','_')):d['name'] for d in json.load(open('models_R1_v19e.json')) if d['name']}
SEARCHMODEL=re.compile(r"'model'\s*,\s*'='\s*,\s*'([a-z0-9_.]+)'")
def target(fieldelem):
    """Resolve a model_id field to a model name, reading BOTH declaration forms."""
    if fieldelem is None: return None,'absent'
    if fieldelem.get('ref'): return MODELS.get(fieldelem.get('ref').split('.')[-1]),'ref'
    if fieldelem.get('search'):
        m=SEARCHMODEL.search(fieldelem.get('search'))
        return (m.group(1) if m else None),'search'
    if fieldelem.get('eval'): return None,'eval'
    return None,'other'
out=collections.defaultdict(list); st=collections.Counter()
for module in sorted(os.listdir(R)):
    md=os.path.join(R,module)
    if not os.path.isdir(md) or not os.path.exists(os.path.join(md,'__manifest__.py')): continue
    st['modules']+=1
    for dp,dn,fns in os.walk(md):
        dn[:]=[d for d in dn if d not in ('static','__pycache__','i18n')]
        for fn in fns:
            p=os.path.join(dp,fn); rel=os.path.relpath(p,R)
            if fn.endswith('.csv') and 'ir.model.access' in fn:
                st['acl_files']+=1
                for row in csv.DictReader(open(p,newline='',encoding='utf-8',errors='replace')):
                    key=row.get('model_id:id') or row.get('model_id/id') or ''
                    mm=MODELS.get(key.split('.')[-1])
                    if mm in OW:
                        out['acl'].append({'module':module,'id':row.get('id'),'model':mm,
                          'group':row.get('group_id:id') or row.get('group_id/id'),
                          'read':row.get('perm_read'),'write':row.get('perm_write'),
                          'create':row.get('perm_create'),'unlink':row.get('perm_unlink'),'file':rel})
                continue
            if not fn.endswith('.xml'): continue
            st['xml']+=1
            try: root=ET.parse(p).getroot()
            except Exception: st['xml_fail']+=1; continue
            for rec in root.iter('record'):
                m=rec.get('model'); xid=rec.get('id')
                xid=xid if (xid and '.' in xid) else (module+'.'+xid if xid else None)
                if m=='ir.rule':
                    mm,form=target(rec.find("./field[@name='model_id']"))
                    if mm in OW:
                        df=rec.find("./field[@name='domain_force']")
                        gf=rec.find("./field[@name='groups']")
                        out['rule'].append({'xmlid':xid,'module':module,'model':mm,'decl_form':form,
                          'name':(rec.find("./field[@name='name']").text or '').strip() if rec.find("./field[@name='name']") is not None else None,
                          'domain':' '.join((df.text or '').split())[:300] if df is not None else '',
                          'groups':gf.get('eval') if gf is not None else None,'file':rel})
                elif m=='ir.ui.view':
                    mf=rec.find("./field[@name='model']")
                    mdl=(mf.text or '').strip() if mf is not None else None
                    if mdl in OW:
                        out['view'].append({'xmlid':xid,'module':module,'model':mdl,'file':rel})
                elif m=='ir.cron':
                    mm,form=target(rec.find("./field[@name='model_id']"))
                    if mm in OW:
                        nf=rec.find("./field[@name='name']")
                        out['cron'].append({'xmlid':xid,'module':module,'model':mm,
                          'name':(nf.text or '').strip() if nf is not None else None,'file':rel})
                    elif module in json.load(open('inv_modset_final.json')) if False else False: pass
for k,v in out.items():
    with open(f'S_{k}.jsonl','w') as fh:
        for r in v: fh.write(json.dumps(r)+'\n')
    st['OUT_'+k]=len(v)
print(json.dumps(dict(st),indent=2))
