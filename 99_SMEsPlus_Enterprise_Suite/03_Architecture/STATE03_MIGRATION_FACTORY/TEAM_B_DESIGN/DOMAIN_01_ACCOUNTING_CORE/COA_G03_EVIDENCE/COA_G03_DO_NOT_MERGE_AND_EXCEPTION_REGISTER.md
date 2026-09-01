# COA-G03 Do-NOT-Merge and Exception Register

Source: Boss-controlled ODOO18 workbook SHA256 `0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`; row key `r` = ODOO18 data row 0..388. Authority: G02 `497c80887f82dfca4967ca43f83b4ecc3c01d8d8`; G03 readiness `ad0451e7b6b1e8962659b35056c46dc10a1b6aa6`; prompt `8d3a974828ccde0c9e08964ebdeec1b58f2cc467`.

Controls: D1 Account Type; D2 BS/P&L; D3 Thai tax/VAT/WHT/CIT; D4 reconciliation; D5 AR/AP; D6 cash/bank/clearing/suspense; D7 inventory/valuation/cost-flow; D8 currency/monetary; D9 statutory; D10 earnings; D11 contra/allowance/depreciation; D12 multi-company; D13 system dependency. Any material difference prohibited merge.

|r|outcome|DNM material reason|
|--:|---|---|
|9|KEEP_SEPARATE|D6 cash/bank behaviour and D8 monetary restriction may differ.|
|10|KEEP_SEPARATE|D1 class/measurement and D8 monetary treatment may differ.|
|12|KEEP_SEPARATE|D11 contra-account role differs.|
|13|KEEP_SEPARATE|D9 statutory/reporting and counterparty control may differ.|
|14|KEEP_SEPARATE|D9 statutory/reporting and counterparty control may differ.|
|15|KEEP_SEPARATE|D9 statutory/reporting and counterparty control may differ.|
|20|KEEP_SEPARATE|D6 clearing behaviour / D4 reconciliation control differs in business purpose.|
|21|KEEP_SEPARATE|D1 Account Type and D6 payment-instrument behaviour differ.|
|22|KEEP_SEPARATE|D6 instrument behaviour differs.|
|23|KEEP_SEPARATE|D5 AR control role is non-trade.|
|29|KEEP_SEPARATE|D7 inventory cost-flow role may differ.|
|30|KEEP_SEPARATE|D7 inventory/valuation/cost-flow differs.|
|31|KEEP_SEPARATE|D2 presentation / D8 monetary treatment may differ.|
|39|KEEP_SEPARATE|D7/asset acquisition control differs.|
|46|KEEP_SEPARATE|D3 Thai tax treatment differs/uncertain.|
|50|KEEP_SEPARATE|D6 contract/control specifics may differ.|
|51|KEEP_SEPARATE|D6 clearing/instrument behaviour differs.|
|52|KEEP_SEPARATE|D5 AR control role and D8 monetary/interest treatment differ.|
|53|KEEP_SEPARATE|D6 clearing and D12 related-party/employee meaning differ.|
|54|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|55|KEEP_SEPARATE|D7 asset lifecycle and D11 depreciation relationship differ.|
|86|KEEP_SEPARATE|D6 cash/clearing/payment instrument behaviour differs.|
|87|KEEP_SEPARATE|D6 instrument / D8 financing treatment differs.|
|89|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|90|KEEP_SEPARATE|D8 monetary/interest treatment differs.|
|91|KEEP_SEPARATE|D12 multi-company/related-party meaning and D9 disclosure may differ.|
|92|KEEP_SEPARATE|D12 employee-related financing meaning differs.|
|98|KEEP_SEPARATE|D6 control/settlement behavior differs.|
|102|KEEP_SEPARATE|D9/D12 related-party/statutory meaning may differ.|
|103|KEEP_SEPARATE|D4 reconciliation requirement differs.|
|112|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|129|KEEP_SEPARATE|D3 tax treatment/documentation may differ.|
|130|KEEP_SEPARATE|D3 tax treatment/documentation may differ.|
|131|KEEP_SEPARATE|D3 tax treatment/documentation may differ.|
|132|KEEP_SEPARATE|D3 tax treatment/documentation may differ.|
|141|KEEP_SEPARATE|D3 tax deductibility and D12 related-party meaning may differ.|
|142|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|150|KEEP_SEPARATE|D2 P&L finance classification / D8 monetary treatment differs.|
|151|KEEP_SEPARATE|D10 retained earnings/distribution semantics differ.|
|154|KEEP_SEPARATE|D3/D9 statutory tax/reporting requirement differs by PND form.|
|155|KEEP_SEPARATE|D3/D9 statutory tax/reporting requirement differs by PND form.|
|156|KEEP_SEPARATE|D3/D9 statutory tax/reporting requirement differs by PND form.|
|158|KEEP_SEPARATE|D3/D9 statutory tax/reporting requirement differs by PND form.|
|162|KEEP_SEPARATE|D3/D9 statutory tax meaning differs.|
|163|KEEP_SEPARATE|D3/D9 statutory VAT treatment differs.|
|164|KEEP_SEPARATE|D3 tax treatment differs.|
|165|KEEP_SEPARATE|D9 statutory reporting requirement differs.|
|166|KEEP_SEPARATE|D9 statutory reporting requirement differs.|
|168|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|169|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|170|KEEP_SEPARATE|D12 related-party/multi-company meaning differs.|
|171|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|172|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|175|RESERVED / NOT DEFAULT-TH|G02 control boundary|
|176|RESERVED / NOT DEFAULT-TH|G02 control boundary|
|179|KEEP_SEPARATE|D11 contra role / D2 presentation differs.|
|180|KEEP_SEPARATE|D11 contra role / D2 presentation differs.|
|181|KEEP_SEPARATE|D3 tax/WHT/VAT and D2 presentation may differ.|
|182|KEEP_SEPARATE|D3 tax/VAT and business nature differ.|
|187|KEEP_SEPARATE|D2 presentation / D8 monetary treatment differs.|
|188|KEEP_SEPARATE|D7 asset disposal and D2 sign/presentation semantics differ.|
|189|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|192|KEEP_SEPARATE|D7 inventory/cost-flow linkage differs.|
|193|KEEP_SEPARATE|D7 fixed-asset disposal role differs.|
|195|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|199|KEEP_SEPARATE|D7 inventory/valuation/cost-flow role differs.|
|200|KEEP_SEPARATE|D7 inventory/valuation/cost-flow role differs.|
|201|KEEP_SEPARATE|D7 inventory/valuation/cost-flow role differs.|
|202|KEEP_SEPARATE|D7 inventory/valuation/cost-flow role differs.|
|203|KEEP_SEPARATE|D7 inventory/valuation/cost-flow role differs.|
|204|KEEP_SEPARATE|D7 inventory/valuation/cost-flow role differs.|
|205|KEEP_SEPARATE|D3 payroll/statutory treatment differs.|
|206|KEEP_SEPARATE|D3 WHT/VAT/lease treatment may differ.|
|208|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|228|KEEP_SEPARATE|D3/D9/D12 related-party/statutory treatment differs.|
|233|KEEP_SEPARATE|D3 tax deductibility/statutory treatment may differ.|
|234|KEEP_SEPARATE|D3 tax deductibility/statutory treatment may differ.|
|235|KEEP_SEPARATE|D3 tax deductibility/statutory treatment may differ.|
|236|KEEP_SEPARATE|D3 tax deductibility/statutory treatment may differ.|
|237|KEEP_SEPARATE|D3 tax deductibility/statutory treatment may differ.|
|238|KEEP_SEPARATE|D3 tax deductibility/statutory treatment may differ.|
|239|KEEP_SEPARATE|D3 tax deductibility/statutory treatment may differ.|
|240|KEEP_SEPARATE|D3 tax deductibility/statutory treatment may differ.|
|241|KEEP_SEPARATE|D3 tax deductibility/statutory treatment may differ.|
|242|KEEP_SEPARATE|D3 tax/WHT/documentation may differ.|
|243|KEEP_SEPARATE|D3 tax/WHT/documentation may differ.|
|244|KEEP_SEPARATE|D3 tax/WHT/documentation may differ.|
|245|KEEP_SEPARATE|D3 tax/WHT/documentation may differ.|
|246|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|247|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|256|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|257|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|262|KEEP_SEPARATE|D3 tax/statutory treatment differs.|
|268|KEEP_SEPARATE|D3 tax/documentation treatment may differ.|
|269|KEEP_SEPARATE|D3 tax/documentation treatment may differ.|
|270|KEEP_SEPARATE|D3 tax/documentation treatment may differ.|
|271|KEEP_SEPARATE|D3 tax/documentation treatment may differ.|
|272|KEEP_SEPARATE|D3 tax/documentation treatment may differ.|
|273|KEEP_SEPARATE|D3 tax/documentation treatment may differ.|
|274|KEEP_SEPARATE|D3 tax/documentation treatment may differ.|
|275|KEEP_SEPARATE|D3 tax/documentation treatment may differ.|
|276|KEEP_SEPARATE|D3 tax/documentation treatment may differ.|
|285|KEEP_SEPARATE|D3 tax deductibility and D12 related-party meaning differ.|
|286|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|287|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|288|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|294|KEEP_SEPARATE|D3/D9 tax/statutory treatment differs.|
|306|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|307|KEEP_SEPARATE|D2 sign/presentation and D8 monetary treatment ambiguity.|
|308|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|309|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|310|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|311|KEEP_SEPARATE|D11 allowance/write-off role differs.|
|312|KEEP_SEPARATE|D11 allowance/provision role differs.|
|313|KEEP_SEPARATE|D3/D9 tax treatment differs.|
|314|KEEP_SEPARATE|D3/D9 tax treatment differs.|
|317|KEEP_SEPARATE|D6 instrument / D8 finance treatment differs.|
|318|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|321|KEEP_SEPARATE|D3/D9 statutory treatment differs.|
|322|KEEP_SEPARATE|D3/D9 statutory treatment differs.|
|323|KEEP_SEPARATE|D3/D9 statutory treatment differs.|
|324|KEEP_SEPARATE|D3/D9 statutory treatment differs.|
|325|KEEP_SEPARATE|D3/D9 statutory treatment differs.|
|326|KEEP_SEPARATE|D3/D9 statutory treatment differs.|
|327|KEEP_SEPARATE|D4 reconciliation requirement differs.|
|331|KEEP_SEPARATE|D7 inventory/valuation/cost-flow differs.|
|332|KEEP_SEPARATE|D7 inventory/valuation/cost-flow differs.|
|333|KEEP_SEPARATE|D7 inventory/valuation/cost-flow differs.|
|334|KEEP_SEPARATE|D7 inventory/valuation/cost-flow differs.|
|335|KEEP_SEPARATE|D7 inventory/valuation/cost-flow differs.|
|336|KEEP_SEPARATE|D7 inventory/valuation/cost-flow differs.|
|337|KEEP_SEPARATE|D7 inventory/valuation/cost-flow differs.|
|341|KEEP_SEPARATE|D3 WHT and D7 production cost nature differ.|
|349|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|350|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|351|KEEP_SEPARATE|No evidenced accounting-treatment equivalence with another source row; preserve distinct semantic/control role.|
|354|KEEP_SEPARATE|D3 rent tax/WHT and D7 cost-flow differ.|
|360|KEEP_SEPARATE|D7/D11 amortization role differs.|
|361|KEEP_SEPARATE|D7 fixed-asset acquisition/capitalization role may differ.|
|364|KEEP_SEPARATE|D3/D9 Thai tax treatment differs.|
|365|KEEP_SEPARATE|D3/D9 Thai tax treatment differs.|
|366|KEEP_SEPARATE|D3/D9 Thai tax treatment differs.|
|367|KEEP_SEPARATE|D3/D9 Thai tax treatment differs.|
|368|KEEP_SEPARATE|D3/D9 Thai tax treatment differs.|
|369|KEEP_SEPARATE|D2 sign/presentation and D6 cash-control behavior differ.|
|370|KEEP_SEPARATE|D3/D13 tax + system-generated dependency differs/unknown.|
|371|KEEP_SEPARATE|D7 inventory cost-flow and D13 system-generated dependency may differ.|
|372|KEEP_SEPARATE|D7 inventory cost-flow and D13 system-generated dependency may differ.|
|373|KEEP_SEPARATE|D7 inventory cost-flow and D13 system-generated dependency may differ.|
|377|KEEP_SEPARATE|D6 clearing and D13 system dependency differ.|
|378|KEEP_SEPARATE|D3 tax timing / D13 system-generated dependency differs.|
|379|KEEP_SEPARATE|D7 inventory cost-flow and D13 system-generated dependency may differ.|
|388|KEEP_SEPARATE|D3/D13; name similarity alone prohibited.|