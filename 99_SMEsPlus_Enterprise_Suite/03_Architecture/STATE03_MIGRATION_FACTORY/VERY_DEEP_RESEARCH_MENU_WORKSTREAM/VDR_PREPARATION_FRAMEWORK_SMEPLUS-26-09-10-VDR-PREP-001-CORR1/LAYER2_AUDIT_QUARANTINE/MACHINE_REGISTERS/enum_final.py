#!/usr/bin/env python3
import os,sys,json,ast,csv,collections
import xml.etree.ElementTree as ET
R=sys.argv[1]
MOD=json.load(open('inv_modset_final.json'))
FAM=set(json.load(open('inv_fam_final.json'))['owned'])
MODELS={}
for d in json.load(open('models_R1_v19e.json')):
    if d['name']: MODELS.setdefault('model_'+d['name'].replace('.','_'),d['name'])
def full(x,m): return x if x and '.' in x else (m+'.'+x if x else None)
def resolve_model(ref):
    """xmlid -> model name, by LOOKUP against the declared model census (not by transform)."""
    if not ref: return None
    return MODELS.get(ref.split('.')[-1])
out=collections.defaultdict(list); st=collections.Counter()
ACT={'ir.actions.act_window','ir.actions.server','ir.actions.report','ir.actions.client','ir.actions.act_url'}
for module in MOD:
    md=os.path.join(R,module)
    if not os.path.isdir(md): st['module_missing']+=1; continue
    st['module_processed']+=1
    for dp,dn,fns in os.walk(md):
        dn[:]=[d for d in dn if d not in ('static','__pycache__','i18n')]
        for fn in fns:
            p=os.path.join(dp,fn); rel=os.path.relpath(p,R); test='/tests/' in rel
            if fn.endswith('.csv') and 'ir.model.access' in fn:
                st['acl_files']+=1
                with open(p,newline='',encoding='utf-8',errors='replace') as fh:
                    for row in csv.DictReader(fh):
                        mm=resolve_model(row.get('model_id:id') or row.get('model_id/id') or '')
                        if mm in FAM:
                            out['acl'].append({'module':module,'id':row.get('id'),'model':mm,
                              'group':row.get('group_id:id') or row.get('group_id/id'),
                              'read':row.get('perm_read'),'write':row.get('perm_write'),
                              'create':row.get('perm_create'),'unlink':row.get('perm_unlink'),'file':rel})
                continue
            if not fn.endswith('.xml'): continue
            st['xml_files']+=1
            try: root=ET.parse(p).getroot()
            except Exception: st['xml_fail']+=1; continue
            for rec in root.iter('record'):
                model=rec.get('model'); xid=full(rec.get('id'),module)
                if not model: continue
                F={}
                for f in rec.findall('field'):
                    F[f.get('name')]=f.get('ref') or f.get('eval') or (f.text or '').strip()[:400]
                if model in ACT:
                    tgt=F.get('res_model') if F.get('res_model') in FAM else resolve_model(F.get('model_id'))
                    bind=resolve_model(F.get('binding_model_id'))
                    if tgt in FAM or bind in FAM:
                        out['action'].append({'xmlid':xid,'module':module,'kind':model,'name':F.get('name'),
                          'model':tgt or bind,'binding':bind,'binding_type':F.get('binding_type'),
                          'view_mode':F.get('view_mode'),'domain':F.get('domain'),'context':F.get('context'),
                          'target':F.get('target'),'groups':F.get('groups_id'),'state':F.get('state'),
                          'code':(F.get('code') or '')[:300],'file':rel,'test':test})
                elif model=='ir.ui.view' and F.get('model') in FAM:
                    out['view'].append({'xmlid':xid,'module':module,'model':F.get('model'),'name':F.get('name'),
                      'inherit_id':F.get('inherit_id'),'mode':F.get('mode'),'priority':F.get('priority'),
                      'groups':F.get('groups_id'),'active':F.get('active'),'file':rel,'test':test})
                    arch=rec.find("./field[@name='arch']")
                    if arch is not None:
                        for b in arch.iter('button'):
                            out['button'].append({'view':xid,'module':module,'model':F.get('model'),
                              'name':b.get('name'),'type':b.get('type'),'string':b.get('string'),
                              'class':b.get('class'),'invisible':b.get('invisible'),'groups':b.get('groups'),
                              'confirm':b.get('confirm'),'context':b.get('context'),'file':rel,'test':test})
                elif model=='ir.cron':
                    out['cron'].append({'xmlid':xid,'module':module,'name':F.get('name'),
                      'model':resolve_model(F.get('model_id')) or F.get('model_id'),'state':F.get('state'),
                      'code':(F.get('code') or '')[:300],'interval':f"{F.get('interval_number')}/{F.get('interval_type')}",
                      'active_attr':F.get('active'),'numbercall':F.get('numbercall'),'file':rel,'test':test})
                elif model=='ir.rule':
                    mm=resolve_model(F.get('model_id'))
                    if mm in FAM:
                        out['rule'].append({'xmlid':xid,'module':module,'model':mm,'name':F.get('name'),
                          'domain':(F.get('domain_force') or '').replace('\n',' ')[:300],'groups':F.get('groups'),
                          'global':F.get('global'),'file':rel,'test':test})
                elif model=='res.groups':
                    out['group'].append({'xmlid':xid,'module':module,'name':F.get('name'),
                      'category':F.get('category_id'),'implied':F.get('implied_ids'),'file':rel,'test':test})
                elif model=='ir.sequence':
                    out['sequence'].append({'xmlid':xid,'module':module,'name':F.get('name'),'code':F.get('code'),
                      'prefix':F.get('prefix'),'file':rel,'test':test})
                elif model=='ir.config_parameter':
                    out['sysparam'].append({'xmlid':xid,'module':module,'key':F.get('key'),'value':F.get('value'),'file':rel})
            for e in root.iter('menuitem'):
                if e.get('id'):
                    out['menu'].append({'xmlid':full(e.get('id'),module),'module':module,'name':e.get('name'),
                      'parent':full(e.get('parent'),module),'action':full(e.get('action'),module),
                      'groups':e.get('groups'),'sequence':e.get('sequence'),'file':rel})
    # python
    for dp,dn,fns in os.walk(md):
        dn[:]=[d for d in dn if d not in ('static','__pycache__','i18n')]
        for fn in fns:
            if not fn.endswith('.py'): continue
            p=os.path.join(dp,fn); rel=os.path.relpath(p,R); st['py_files']+=1
            src=open(p,encoding='utf-8',errors='replace').read()
            if '_name' not in src and '_inherit' not in src: continue
            try: tree=ast.parse(src)
            except Exception: st['py_fail']+=1; continue
            for node in ast.walk(tree):
                if not isinstance(node,ast.ClassDef): continue
                nm=None; inh=[]
                for s in node.body:
                    if isinstance(s,ast.Assign):
                        for t in s.targets:
                            if isinstance(t,ast.Name) and t.id=='_name' and isinstance(s.value,ast.Constant): nm=s.value.value
                            elif isinstance(t,ast.Name) and t.id=='_inherit':
                                v=s.value
                                inh=[v.value] if isinstance(v,ast.Constant) else [e.value for e in getattr(v,'elts',[]) if isinstance(e,ast.Constant)]
                mods=set(filter(None,[nm]+inh))
                if 'res.config.settings' in mods:
                    for s in node.body:
                        if isinstance(s,ast.Assign) and isinstance(s.value,ast.Call):
                            f2=s.value.func
                            if isinstance(f2,ast.Attribute) and isinstance(f2.value,ast.Name) and f2.value.id=='fields':
                                kw={k.arg:(ast.unparse(k.value)[:220] if k.arg else None) for k in s.value.keywords}
                                for t in s.targets:
                                    if isinstance(t,ast.Name):
                                        out['setting'].append({'module':module,'field':t.id,'type':f2.attr,
                                          'string':kw.get('string'),'implied_group':kw.get('implied_group'),
                                          'related':kw.get('related'),'config_parameter':kw.get('config_parameter'),
                                          'default':kw.get('default'),'readonly':kw.get('readonly'),
                                          'compute':kw.get('compute'),'file':rel,'line':s.lineno})
                if not (mods & FAM): continue
                tgt=nm if nm in FAM else next(iter(mods & FAM))
                for s in node.body:
                    if isinstance(s,ast.Assign):
                        for t in s.targets:
                            if not isinstance(t,ast.Name): continue
                            if isinstance(s.value,ast.Call):
                                fc=s.value.func
                                if isinstance(fc,ast.Attribute) and isinstance(fc.value,ast.Name):
                                    if fc.value.id=='fields':
                                        kw={k.arg:(ast.unparse(k.value)[:220] if k.arg else None) for k in s.value.keywords}
                                        out['field'].append({'model':tgt,'module':module,'field':t.id,'type':fc.attr,
                                          'string':kw.get('string'),'selection':kw.get('selection'),
                                          'compute':kw.get('compute'),'related':kw.get('related'),
                                          'required':kw.get('required'),'readonly':kw.get('readonly'),
                                          'groups':kw.get('groups'),'store':kw.get('store'),
                                          'tracking':kw.get('tracking'),'company_dependent':kw.get('company_dependent'),
                                          'default':kw.get('default'),'file':rel,'line':s.lineno})
                                    elif fc.value.id=='models' and fc.attr in ('Constraint','UniqueIndex','Index'):
                                        out['constraint'].append({'model':tgt,'module':module,'kind':fc.attr,'name':t.id,
                                          'detail':ast.unparse(s.value)[:400],'file':rel,'line':s.lineno})
                            if t.id=='_sql_constraints':
                                out['constraint'].append({'model':tgt,'module':module,'kind':'sql_legacy','name':t.id,
                                  'detail':ast.unparse(s.value)[:400],'file':rel,'line':s.lineno})
                    if isinstance(s,(ast.FunctionDef,ast.AsyncFunctionDef)):
                        decs=[ast.unparse(d)[:120] for d in s.decorator_list]
                        k=None
                        if any('api.constrains' in d for d in decs): k='constrains'
                        elif any('api.onchange' in d for d in decs): k='onchange'
                        elif any('api.depends' in d for d in decs): k='depends'
                        elif any('api.ondelete' in d for d in decs): k='ondelete'
                        elif s.name.startswith(('action_','button_')): k='ui_method'
                        elif s.name in ('create','write','unlink','copy','default_get','_check_company'): k='crud_override'
                        elif 'cron' in s.name.lower(): k='cron_method'
                        if k: out['method'].append({'model':tgt,'module':module,'class':node.name,'method':s.name,
                              'kind':k,'decorators':decs,'file':rel,'line':s.lineno})
for k,v in out.items():
    with open(f'F_{k}.jsonl','w') as fh:
        for r in v: fh.write(json.dumps(r)+'\n')
    st['OUT_'+k]=len(v)
print(json.dumps(dict(st),indent=2))
