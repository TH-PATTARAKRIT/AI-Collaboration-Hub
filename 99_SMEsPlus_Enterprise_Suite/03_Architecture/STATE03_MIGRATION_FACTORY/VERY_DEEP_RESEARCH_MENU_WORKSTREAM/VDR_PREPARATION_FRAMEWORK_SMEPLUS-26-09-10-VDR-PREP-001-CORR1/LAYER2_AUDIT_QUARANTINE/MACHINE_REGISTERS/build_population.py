#!/usr/bin/env python3
"""Build the Source Learning Population (Learning Items) from the extracted surface.
UNIT: one addressable functional element = one Learning Item. No author-chosen rows."""
import json,csv,collections,os
def rd(p):
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []
INV=set(json.load(open('inv_subtree_ids.json')))
FAM=json.load(open('inv_fam_final.json'))
OWNED=set(FAM['owned']); BOUND=set(FAM['boundary'])
MODS=json.load(open('inv_modset_final.json'))
menus={m['xmlid']:m for m in rd('F_menu.jsonl')}
acts={a['xmlid']:a for a in rd('F_action.jsonl')}
allacts=json.load(open('actions_all_R1.json'))
rows=[]; n=collections.Counter()
def add(cls,ident,label,model,module,evid,extra=None,crit='STANDARD'):
    n[cls]+=1
    rows.append({'learning_id':f'LI-INV-{cls}-{n[cls]:04d}','class':cls,'identity':ident,
      'label':(label or '')[:120],'model':model or '','module':module,'evidence_pointer':evid,
      'criticality':crit,'detail':json.dumps({k:(str(v)[:200] if v is not None else None) for k,v in (extra or {}).items()}),
      'research_status':'DISCOVERED','register_coverage':'','open_question':'','material_delta':''})
CRITMODELS={'stock.quant','stock.move','stock.move.line','stock.picking','stock.lot',
 'stock.valuation.layer','stock.scrap','stock.warehouse','stock.location','stock.landed.cost',
 'product.value','stock.picking.type','stock.rule','stock.route','stock.warehouse.orderpoint'}
def crit_of(model,cls):
    if cls in ('RULE','ACL','GROUP'): return 'CRITICAL'
    if model in CRITMODELS: return 'CRITICAL'
    return 'STANDARD'
# MENU (Inventory root subtree) -- the menu-by-menu spine
for x in sorted(INV):
    m=menus.get(x)
    if not m: continue
    a=m.get('action'); rm=(allacts.get(a) or {}).get('res_model','') if a else ''
    add('MENU',x,m.get('name'),rm,m['module'],f"{m['file']}",
        {'parent':m.get('parent'),'action':a,'groups':m.get('groups'),'sequence':m.get('sequence'),
         'kind':'CONTAINER' if not a else 'ACTION-BEARING'},crit_of(rm,'MENU'))
# MENU-OUTSIDE : menus defined by INV-MODSET modules that do NOT hang under the Inventory root
for x,m in sorted(menus.items()):
    if x in INV: continue
    add('MENUX',x,m.get('name'),'',m['module'],m['file'],
        {'parent':m.get('parent'),'action':m.get('action'),'groups':m.get('groups')})
for a in sorted(acts.values(),key=lambda r:r['xmlid']):
    add('ACTION',a['xmlid'],a.get('name'),a.get('model'),a['module'],a['file'],
        {'kind':a['kind'],'view_mode':a.get('view_mode'),'binding':a.get('binding'),
         'binding_type':a.get('binding_type'),'target':a.get('target'),'domain':a.get('domain'),
         'context':a.get('context'),'groups':a.get('groups')},crit_of(a.get('model'),'ACTION'))
for v in sorted(rd('F_view.jsonl'),key=lambda r:(r['model'] or '',r['xmlid'])):
    add('VIEW',v['xmlid'],v.get('name'),v['model'],v['module'],v['file'],
        {'inherit_id':v.get('inherit_id'),'mode':v.get('mode'),'groups':v.get('groups'),
         'priority':v.get('priority')},crit_of(v['model'],'VIEW'))
for b in sorted(rd('F_button.jsonl'),key=lambda r:(r['model'] or '',str(r['name']))):
    add('BUTTON',f"{b['view']}::{b.get('name')}",b.get('string'),b['model'],b['module'],b['file'],
        {'type':b.get('type'),'invisible':b.get('invisible'),'groups':b.get('groups'),
         'confirm':b.get('confirm'),'class':b.get('class')},crit_of(b['model'],'BUTTON'))
for f in sorted(rd('F_field.jsonl'),key=lambda r:(r['model'],r['field'])):
    add('FIELD',f"{f['model']}.{f['field']}",f.get('string'),f['model'],f['module'],
        f"{f['file']}:{f['line']}",
        {'type':f['type'],'required':f.get('required'),'readonly':f.get('readonly'),
         'groups':f.get('groups'),'compute':f.get('compute'),'related':f.get('related'),
         'store':f.get('store'),'tracking':f.get('tracking'),
         'company_dependent':f.get('company_dependent'),'selection':f.get('selection')},
        crit_of(f['model'],'FIELD'))
for s in sorted(rd('F_setting.jsonl'),key=lambda r:(r['module'],r['field'])):
    add('SETTING',f"res.config.settings.{s['field']}",s.get('string'),'res.config.settings',
        s['module'],f"{s['file']}:{s['line']}",
        {'type':s['type'],'implied_group':s.get('implied_group'),'related':s.get('related'),
         'config_parameter':s.get('config_parameter'),'default':s.get('default'),
         'readonly':s.get('readonly')},'CRITICAL' if s.get('implied_group') or s['field'].startswith('group_') else 'STANDARD')
for c in sorted(rd('F_cron.jsonl'),key=lambda r:r['xmlid']):
    add('AUTOMATION',c['xmlid'],c.get('name'),c.get('model'),c['module'],c['file'],
        {'kind':'ir.cron','interval':c.get('interval'),'active_attr':c.get('active_attr'),
         'numbercall':c.get('numbercall'),'state':c.get('state')},'CRITICAL')
for m in sorted(rd('F_method.jsonl'),key=lambda r:(r['model'],r['method'])):
    if m['kind'] in ('depends',): continue
    add('BEHAVIOUR',f"{m['model']}::{m['class']}.{m['method']}",m['kind'],m['model'],m['module'],
        f"{m['file']}:{m['line']}",{'kind':m['kind'],'decorators':m['decorators']},
        crit_of(m['model'],'BEHAVIOUR'))
for c in sorted(rd('F_constraint.jsonl'),key=lambda r:(r['model'],str(r.get('name')))):
    add('CONSTRAINT',f"{c['model']}::{c.get('name')}",c['kind'],c['model'],c['module'],
        f"{c['file']}:{c['line']}",{'detail':c['detail']},'CRITICAL')
for r in sorted(rd('F_rule.jsonl'),key=lambda r:r['xmlid']):
    add('RULE',r['xmlid'],r.get('name'),r['model'],r['module'],r['file'],
        {'domain':r.get('domain'),'groups':r.get('groups'),'global':r.get('global')},'CRITICAL')
for a in sorted(rd('F_acl.jsonl'),key=lambda r:(r['model'],str(r.get('group')))):
    add('ACL',f"{a['model']}::{a.get('group')}",a.get('id'),a['model'],a['module'],a['file'],
        {'read':a['read'],'write':a['write'],'create':a['create'],'unlink':a['unlink']},'CRITICAL')
for g in sorted(rd('F_group.jsonl'),key=lambda r:r['xmlid']):
    add('GROUP',g['xmlid'],g.get('name'),'res.groups',g['module'],g['file'],
        {'category':g.get('category'),'implied':g.get('implied')},'CRITICAL')
for s in sorted(rd('F_sequence.jsonl'),key=lambda r:r['xmlid']):
    add('SEQUENCE',s['xmlid'],s.get('name'),'ir.sequence',s['module'],s['file'],
        {'code':s.get('code'),'prefix':s.get('prefix')})
for p in sorted(rd('F_sysparam.jsonl'),key=lambda r:r['xmlid']):
    add('SYSPARAM',p['xmlid'],p.get('key'),'ir.config_parameter',p['module'],p['file'],{'value':p.get('value')})
with open('LEARNING_POPULATION.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(rows,open('LEARNING_POPULATION.json','w'))
print(json.dumps({'TOTAL_LEARNING_ITEMS':len(rows),'by_class':dict(n),
 'critical_items':sum(1 for r in rows if r['criticality']=='CRITICAL')},indent=2))
