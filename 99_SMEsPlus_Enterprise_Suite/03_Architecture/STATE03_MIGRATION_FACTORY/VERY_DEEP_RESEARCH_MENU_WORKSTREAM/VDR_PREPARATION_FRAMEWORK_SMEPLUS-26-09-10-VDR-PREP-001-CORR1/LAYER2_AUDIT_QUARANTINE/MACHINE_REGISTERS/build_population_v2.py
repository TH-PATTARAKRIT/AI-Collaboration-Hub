#!/usr/bin/env python3
"""Source Learning Population v2 — rebuilt after the SMEs Core independent challenge.
Adds the mandatory schema columns that v1 omitted (C-03, C-20), adds the three
Learning Item classes whose register rows were orphans in v1 (C-04), and records an
honest per-item research state instead of a uniform S0 (C-02)."""
import json,csv,collections,os,sys
R1=sys.argv[1]; GEN='series-19 (content-verified: declarative-constraint construct present; inventory module 313 files)'
def rd(p): return [json.loads(l) for l in open(p)] if os.path.exists(p) else []
INV=set(json.load(open('inv_subtree_ids.json')))
FAM=json.load(open('inv_fam_final.json')); OWNED=set(FAM['owned']); BOUND=set(FAM['boundary'])
BASE=json.load(open('model_base.json'))
menus={m['xmlid']:m for m in rd('F_menu.jsonl')}
allacts=json.load(open('actions_all_R1.json'))
HOP={h['menu']:h for h in json.load(open('hop2_resolution.json'))}
FL=json.load(open('fields_all_R1.json'))
rows=[]; n=collections.Counter()
CRITMODELS={'stock.quant','stock.move','stock.move.line','stock.picking','stock.lot','product.value',
 'stock.scrap','stock.warehouse','stock.location','stock.landed.cost','stock.picking.type','stock.rule',
 'stock.route','stock.warehouse.orderpoint','stock.valuation.adjustment.lines'}
def own(model):
    if model in OWNED: return 'OWNED'
    if model in BOUND: return 'SHARED-CONSUMED'
    if model in ('res.config.settings',): return 'SHARED-EXTENDED'
    return 'EXTERNAL' if model else 'N/A'
def add(cls,ident,label,model,module,evid,extra=None,crit=None,status='S1_SOURCE_LOCATED',regs=''):
    n[cls]+=1
    rows.append({
      'learning_id':f'LI-INV-{cls}-{n[cls]:04d}','application':'Inventory','class':cls,
      'identity':ident,'label':(label or '')[:120],'model':model or '','module':module,
      'ownership_class':own(model),
      'source_root':'R1','generation_basis':GEN,
      'evidence_pointer':evid,'reachability':'UNMEASURED',
      'criticality':crit or ('CRITICAL' if (cls in ('RULE','ACL','GROUP','CONSTRAINT','AUTOMATION') or model in CRITMODELS) else 'STANDARD'),
      'research_status':status,'register_coverage':regs,
      'detail':json.dumps({k:(str(v)[:200] if v is not None else None) for k,v in (extra or {}).items()}),
      'open_question':'','material_delta':''})
S4_MENUS={'stock.menu_action_inventory_tree','stock.menu_valuation','stock.menu_reordering_rules_replenish',
          'stock.in_picking','stock.out_picking','stock.int_picking','stock.menu_procurement_compute',
          'mrp_workorder.menu_mrp_workorder_production','mrp_workorder.menu_mrp_workorder_workcenter'}
for x in sorted(INV):
    m=menus.get(x)
    if not m: continue
    a=m.get('action'); rm=(allacts.get(a) or {}).get('res_model','') if a else ''
    hops=1 if rm else (0 if not a else '?')
    if x in HOP: rm=HOP[x]['model']; hops=3
    st='S4_FUNCTION_VERIFIED' if x in S4_MENUS else 'S1_SOURCE_LOCATED'
    add('MENU',x,m.get('name'),rm,m['module'],m['file'],
        {'parent':m.get('parent'),'action':a,'groups':m.get('groups'),'sequence':m.get('sequence'),
         'kind':'CONTAINER' if not a else 'ACTION-BEARING','resolution_hops':hops},status=st,regs='01,02,08')
for x,m in sorted(menus.items()):
    if x in INV: continue
    add('MENUX',x,m.get('name'),'',m['module'],m['file'],
        {'parent':m.get('parent'),'action':m.get('action'),'groups':m.get('groups')},regs='01')
for a in sorted(rd('F_action.jsonl'),key=lambda r:r['xmlid']):
    add('ACTION',a['xmlid'],a.get('name'),a.get('model'),a['module'],a['file'],
        {'kind':a['kind'],'view_mode':a.get('view_mode'),'binding':a.get('binding'),
         'target':a.get('target'),'domain':a.get('domain'),'context':a.get('context'),'groups':a.get('groups')},regs='01,04')
for v in sorted(rd('F_view.jsonl'),key=lambda r:(r['model'] or '',r['xmlid'])):
    add('VIEW',v['xmlid'],v.get('name'),v['model'],v['module'],v['file'],
        {'inherit_id':v.get('inherit_id'),'mode':v.get('mode'),'groups':v.get('groups')},regs='04')
for i,b in enumerate(sorted(rd('F_button.jsonl'),key=lambda r:(r['model'] or '',str(r['name'])))):
    add('BUTTON',f"{b['view']}::{b.get('name')}",b.get('string'),b['model'],b['module'],b['file'],
        {'type':b.get('type'),'invisible':b.get('invisible'),'groups':b.get('groups'),'confirm':b.get('confirm')},regs='04')
for f in sorted(rd('F_field.jsonl'),key=lambda r:(r['model'],r['field'])):
    add('FIELD',f"{f['model']}.{f['field']}",f.get('string'),f['model'],f['module'],f"{f['file']}:{f['line']}",
        {'type':f['type'],'required':f.get('required'),'readonly':f.get('readonly'),'groups':f.get('groups'),
         'compute':f.get('compute'),'related':f.get('related'),'store':f.get('store'),
         'tracking':f.get('tracking'),'company_dependent':f.get('company_dependent')},regs='05')
S4_TOGGLES={'group_stock_lot_print_gs1','group_warning_stock','group_unlocked_by_default',
 'group_rental_stock_picking','group_lot_on_invoice','group_expiry_date_on_delivery_slip','group_lot_on_delivery_slip'}
for s in sorted(rd('F_setting.jsonl'),key=lambda r:(r['module'],r['field'])):
    st='S4_FUNCTION_VERIFIED' if s['field'] in S4_TOGGLES else 'S3_CONFIG_VERIFIED'
    add('SETTING',f"config.{s['field']}",s.get('string'),'res.config.settings',s['module'],f"{s['file']}:{s['line']}",
        {'type':s['type'],'implied_group':s.get('implied_group'),'related':s.get('related'),
         'config_parameter':s.get('config_parameter'),'default':s.get('default')},
        crit='CRITICAL' if s.get('implied_group') or s['field'].startswith('module_') else 'STANDARD',
        status=st,regs='02,03')
for c in sorted(rd('F_cron.jsonl'),key=lambda r:r['xmlid']):
    add('AUTOMATION',c['xmlid'],c.get('name'),c.get('model'),c['module'],c['file'],
        {'kind':'scheduled job','interval':c.get('interval'),'active_attr':c.get('active_attr'),
         'eligibility':c.get('eligibility')},regs='08')
S4_METH={'action_view_inventory','action_view_quants','action_open_orderpoints','run_scheduler','_quant_tasks'}
for m in sorted(rd('F_method.jsonl'),key=lambda r:(r['model'],r['method'])):
    if m['kind']=='depends': continue
    st='S4_FUNCTION_VERIFIED' if m['method'] in S4_METH else 'S1_SOURCE_LOCATED'
    add('BEHAVIOUR',f"{m['model']}::{m['class']}.{m['method']}",m['kind'],m['model'],m['module'],
        f"{m['file']}:{m['line']}",{'kind':m['kind'],'decorators':m['decorators']},status=st,regs='04,08')
for c in sorted(rd('F_constraint.jsonl'),key=lambda r:(r['model'],str(r.get('name')))):
    add('CONSTRAINT',f"{c['model']}::{c.get('name')}",c['kind'],c['model'],c['module'],f"{c['file']}:{c['line']}",
        {'detail':c['detail']},regs='05')
for r in sorted(rd('F_rule.jsonl'),key=lambda r:r['xmlid']):
    add('RULE',r['xmlid'],r.get('name'),r['model'],r['module'],r['file'],
        {'domain':r.get('domain'),'groups':r.get('groups'),'decl_form':r.get('decl_form')},
        status='S4_FUNCTION_VERIFIED',regs='07')
for a in sorted(rd('F_acl.jsonl'),key=lambda r:(r['model'],str(r.get('group')))):
    add('ACL',f"{a['model']}::{a.get('group')}",a.get('id'),a['model'],a['module'],a['file'],
        {'read':a['read'],'write':a['write'],'create':a['create'],'unlink':a['unlink']},regs='07')
for g in sorted(rd('F_group.jsonl'),key=lambda r:r['xmlid']):
    add('GROUP',g['xmlid'],g.get('name'),'res.groups',g['module'],g['file'],
        {'category':g.get('category'),'implied':g.get('implied')},regs='02,07')
for s in sorted(rd('F_sequence.jsonl'),key=lambda r:r['xmlid']):
    add('SEQUENCE',s['xmlid'],s.get('name'),'ir.sequence',s['module'],s['file'],{'code':s.get('code')},regs='08')
for p in sorted(rd('F_sysparam.jsonl'),key=lambda r:r['xmlid']):
    add('SYSPARAM',p['xmlid'],p.get('key'),'ir.config_parameter',p['module'],p['file'],{'value':p.get('value')},regs='03,08')
# ---- NEW CLASSES (challenge C-04: register rows were orphans)
for m in sorted(OWNED|BOUND):
    add('OBJECT',m,BASE['base'].get(m,'?'),m,','.join(sorted({d['module'] for d in json.load(open('models_R1_v19e.json')) if d['name']==m})) or '-',
        'derived from the model-declaration census',
        {'kind':BASE['base'].get(m,'?'),'persistent':m in set(BASE['persistent'])},regs='05,06,07')
for i,r in enumerate(sorted(rd('F_archgroups.jsonl'),key=lambda x:(x['model'],x['file'],x['tag'],str(x.get('name'))))):
    add('GATEDELEM',f"{r['file']}#{r['tag']}[{r.get('name') or i}]",r['tag'],r['model'],r['module'],r['file'],
        {'tag':r['tag'],'element_name':r.get('name'),'groups':r['groups']},
        status='S3_CONFIG_VERIFIED',regs='02')
ext=collections.defaultdict(lambda:[0,0])
for f in FL:
    if f['type'] not in ('Many2one','One2many','Many2many') or not f['comodel']: continue
    if f['model'] in OWNED and f['comodel'] not in OWNED: ext[f['comodel']][0]+=1
    if f['comodel'] in OWNED and f['model'] not in OWNED: ext[f['model']][1]+=1
for m in sorted(ext):
    o,i=ext[m]
    add('HANDOFF',m,f'outbound {o} / inbound {i}',m,'-','derived from the system-wide field census',
        {'outbound_refs':o,'inbound_refs':i},regs='06')
cols=list(rows[0].keys())
with open('LEARNING_POPULATION.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=cols); w.writeheader(); w.writerows(rows)
json.dump(rows,open('LEARNING_POPULATION.json','w'))
st=collections.Counter(r['research_status'] for r in rows)
dist=collections.Counter()
for cls in n:
    dist[cls]=len({r['identity'] for r in rows if r['class']==cls})
print(json.dumps({'TOTAL_ROWS':len(rows),'TOTAL_DISTINCT_IDENTITIES':len({r['identity'] for r in rows}),
 'by_class_rows':dict(n),'by_class_distinct':dict(dist),'by_status':dict(st),
 'critical':sum(1 for r in rows if r['criticality']=='CRITICAL'),
 'ownership':dict(collections.Counter(r['ownership_class'] for r in rows)),
 'columns':cols},indent=2))
