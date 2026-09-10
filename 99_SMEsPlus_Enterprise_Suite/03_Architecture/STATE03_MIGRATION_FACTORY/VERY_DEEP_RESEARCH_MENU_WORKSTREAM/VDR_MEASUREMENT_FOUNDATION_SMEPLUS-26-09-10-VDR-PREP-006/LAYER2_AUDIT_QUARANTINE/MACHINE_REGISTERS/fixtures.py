#!/usr/bin/env python3
"""PREP-006 CP07 — ADVERSARIAL TEST FIXTURES.  VERSION 3.

v2 -> v3: FX-16 and FX-17 carried FABRICATED source paths, so they tested "no such file"
rather than "source present, runtime absent". The INSTRUMENT was right to refuse to call a
non-existent path source-present; the FIXTURE DATA was wrong. Real paths substituted; the
EXPECTATIONS were not touched. v1 and v2 results are preserved verbatim.

v1 -> v2: FX-06's expected value was malformed (a missing hyphen in the identifier it
expects the instrument to echo). The INSTRUMENT was correct and the EXPECTATION was wrong.
v1's result is preserved verbatim in fixture_results_v1.json; the expectation was NOT edited
until after v1 was recorded.

Every fixture's EXPECTED RESULT is written HERE, before any instrument runs, and this file is
the only place it is written. An instrument that reads this file would be self-referential;
none does — the harness compares, the instruments never see the expectations.
"""
FIXTURES=[
 # id, class, the item as the instrument would see it, expected verdict, why
 ('FX-01','TRUE POSITIVE',      {'kind':'MENU','identity':'stock.menu_stock_root','source_pointer':'stock/views/stock_menu_views.xml','observed_on':'BK12MAY26;iEVING'}, 'OBSERVED','declared and present on a deployment'),
 ('FX-02','TRUE NEGATIVE',      {'kind':'MENU','identity':'zz_fake.menu_nothing','source_pointer':'','observed_on':''},                                         'ABSENT','declared nowhere, present nowhere'),
 ('FX-03','FALSE POSITIVE TRAP',{'kind':'FIELD','identity':'stock.move.value_not_real','source_pointer':'stock/models/stock_move.py:999999','observed_on':''},  'SOURCE_UNRESOLVED','the pointer names a real file and an impossible line'),
 ('FX-04','FALSE NEGATIVE TRAP',{'kind':'BEHAVIOUR','identity':'stock.picking::action_cancel','source_pointer':'stock/models/stock_picking.py:1','observed_on':''},'CANCEL_PATH','an identifier whose token is separated by an underscore, which a word-boundary predicate cannot see'),
 ('FX-05','MISSING DATA',       {'kind':'FIELD','identity':'stock.move.value','source_pointer':'','observed_on':'BK12MAY26'},                                    'SOURCE_UNRESOLVED','observed at runtime, no source pointer at all'),
 ('FX-06','DUPLICATE ITEM',     {'kind':'FIELD','identity':'stock.move.value','source_pointer':'stock_account/models/stock_move.py:20','observed_on':'BK12MAY26'},'DUPLICATE_OF_FX-05','the same identity twice with different provenance'),
 ('FX-07','INVALID N/A',        {'kind':'HANDOFF','identity':'account.account','na_reason':'the class carries no access-control surface of its own','observed_on':'BK12MAY26'},'NA_REJECTED','a persistent model asserted to have no security surface'),
 ('FX-08','HIDDEN FUNCTION',    {'kind':'MENU','identity':'stock.menu_hidden','gate':'base.group_no_one','observed_on':'BK12MAY26'},                             'IN_POPULATION','hidden must never mean excluded'),
 ('FX-09','DISABLED PRESENT',   {'kind':'CRON','identity':'stock.ir_cron_x','active':'f','observed_on':'BK12MAY26'},                                             'IN_POPULATION','disabled must never mean excluded'),
 ('FX-10','OPTIONAL FUNCTION',  {'kind':'FIELD','identity':'stock.lot.expiration_date','module':'product_expiry','observed_on':''},                              'IN_POPULATION','optional and uninstalled must never mean excluded'),
 ('FX-11','CONFIG OFF',         {'kind':'GATEDELEM','identity':'x#field[y]','gate':'stock.group_production_lot','gate_state':'off'},                             'IN_POPULATION','a gate being off must never remove the element'),
 ('FX-12','CONFIG ON',          {'kind':'GATEDELEM','identity':'x#field[y]','gate':'stock.group_production_lot','gate_state':'on'},                              'IN_POPULATION','symmetric with FX-11'),
 ('FX-13','CONFIG ALTERNATIVE', {'kind':'SETTING','identity':'config.inventory_valuation','value':'real_time'},                                                  'IN_POPULATION','an alternative value is a third state, not a second'),
 ('FX-14','SECURITY RESTRICTED',{'kind':'MODEL','identity':'stock.reference','grants':1,'rules':0,'observed_on':'BK12MAY26'},                                    'IN_POPULATION','restricted must never mean excluded'),
 ('FX-15','STATE RESTRICTED',   {'kind':'BUTTON','identity':'v::action_x','invisible_unless_state':'done'},                                                      'IN_POPULATION','state-gated must never mean excluded'),
 ('FX-16','RUNTIME UNREACHABLE',{'kind':'MENU','identity':'l10n_cl_edi_stock.menu_sii_chile','source_pointer':'l10n_cl_edi_stock/views/menuitems.xml','observed_on':''},  'SOURCE_ONLY','present in source, on no deployment'),
 ('FX-17','SRC PRESENT/RT ABSENT',{'kind':'VIEW','identity':'stock.view_never_installed','source_pointer':'stock/views/stock_picking_views.xml','observed_on':''},'SOURCE_ONLY','same shape, different kind'),
 ('FX-18','RT PRESENT/SRC PATH DIFFERS',{'kind':'FIELD','identity':'stock.picking.custom_x','source_pointer':'','observed_on':'iTEST02'},                        'RUNTIME_ONLY','installed from a module with no source in the declared path set'),
 ('FX-19','CROSS-MODULE OWNERSHIP',{'kind':'FIELD','identity':'stock.picking.sale_id','module':'sale_stock','observed_on':'BK12MAY26'},                          'IN_POPULATION','owned elsewhere, on a domain model — must not be excluded for ownership'),
 ('FX-20','INHERITED MODEL',    {'kind':'MODEL_EXTENSION','identity':'product.product','module':'stock','source_pointer':'stock/models/product.py:1'},           'IN_POPULATION','an extension is surface'),
 ('FX-21','MODULE EXTENSION',   {'kind':'FIELD','identity':'product.template.tracking','module':'stock','observed_on':'BK12MAY26'},                              'IN_POPULATION','a field added by the domain to a foreign model'),
 ('FX-22','SILENT FALLBACK',    {'kind':'BEHAVIOUR','identity':'stock.quant::_get_removal_strategy','fallback':'fifo'},                                          'FALLBACK_FLAGGED','a resolver that falls through must be visible, not silent'),
 ('FX-23','CANCEL / REVERSE',   {'kind':'BEHAVIOUR','identity':'stock.picking::action_cancel'},                                                                  'CANCEL_PATH','the reverse of FX-04, as a plain case'),
 ('FX-24','CONTRADICTORY EVIDENCE',{'kind':'FIELD','identity':'stock.move.value','dim_state':'NOT_VERIFIED','rv_state':'RESEARCH_VERIFIED'},                     'CONTRADICTION','a cell may not be not-verified and verified at once'),
]
if __name__=='__main__':
    import json,collections
    json.dump([{'id':i,'class':c,'item':it,'expected':e,'why':w} for i,c,it,e,w in FIXTURES],
              open('work6/fixtures.json','w'),indent=1)
    print(f'fixtures defined: {len(FIXTURES)}')
    for k,v in collections.Counter(c for _,c,_,_,_ in FIXTURES).most_common():
        print(f'   {v}  {k}')
