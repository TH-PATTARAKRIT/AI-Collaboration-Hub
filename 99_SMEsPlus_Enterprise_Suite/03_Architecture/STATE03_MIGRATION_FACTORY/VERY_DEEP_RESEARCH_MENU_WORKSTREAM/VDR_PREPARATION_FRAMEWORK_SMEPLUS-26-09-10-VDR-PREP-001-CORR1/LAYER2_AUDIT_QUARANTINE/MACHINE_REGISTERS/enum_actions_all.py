import os,sys,json,collections
import xml.etree.ElementTree as ET
R=sys.argv[1]
KIND={'ir.actions.act_window','ir.actions.server','ir.actions.report','ir.actions.client','ir.actions.act_url'}
acts={}; files=0; fails=0
def full(x,m): return x if x and '.' in x else (m+'.'+x if x else None)
for module in sorted(os.listdir(R)):
    md=os.path.join(R,module)
    if not os.path.isdir(md) or not os.path.exists(os.path.join(md,'__manifest__.py')): continue
    for dp,dn,fns in os.walk(md):
        dn[:]=[d for d in dn if d not in ('static','__pycache__','i18n')]
        for fn in fns:
            if not fn.endswith('.xml'): continue
            p=os.path.join(dp,fn); files+=1
            try: t=ET.parse(p).getroot()
            except Exception: fails+=1; continue
            for rec in t.iter('record'):
                if rec.get('model') not in KIND or not rec.get('id'): continue
                F={}
                for f in rec.findall('field'):
                    F[f.get('name')]=f.get('ref') or f.get('eval') or (f.text or '').strip()[:300]
                acts[full(rec.get('id'),module)]={'module':module,'kind':rec.get('model'),
                  'name':F.get('name'),'res_model':F.get('res_model'),'model_id':F.get('model_id'),
                  'view_mode':F.get('view_mode'),'domain':F.get('domain'),'context':F.get('context'),
                  'binding_model_id':F.get('binding_model_id'),'binding_type':F.get('binding_type'),
                  'target':F.get('target'),'groups':F.get('groups_id'),'state':F.get('state'),
                  'file':os.path.relpath(p,R)}
json.dump(acts,open(sys.argv[2],'w'))
print(json.dumps({'xml_files':files,'parse_fail':fails,'actions':len(acts)},indent=2))
