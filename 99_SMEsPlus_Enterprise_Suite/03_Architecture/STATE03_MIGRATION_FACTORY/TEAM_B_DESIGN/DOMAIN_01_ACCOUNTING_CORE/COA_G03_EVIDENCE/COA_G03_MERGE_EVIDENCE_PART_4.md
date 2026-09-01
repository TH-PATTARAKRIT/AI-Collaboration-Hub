# COA-G03 Merge Evidence Part 4

Source: Boss-controlled ODOO18 workbook SHA256 `0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`; row key `r` = ODOO18 data row 0..388. Authority: G02 `497c80887f82dfca4967ca43f83b4ecc3c01d8d8`; G03 readiness `ad0451e7b6b1e8962659b35056c46dc10a1b6aa6`; prompt `8d3a974828ccde0c9e08964ebdeec1b58f2cc467`.

For each merged source: code/name/type/business meaning/target/equivalence/provenance. 13 DNM controls were tested before merge.

|r|code/name|type|business meaning|target|equivalence evidence|
|--:|---|---|---|---|---|
|267|531501019 ค่าเบี้ยประกัน - สินค้า|Expenses|Insurance by covered class|G03-CAND-124|Same insurance-expense treatment; coverage class retained as dimension.; provenance=ODOO18:267|
|277|531601010 ค่าบริการวิชาชีพ - บัญชี|Expenses|Accounting/audit/system/legal professional fees|G03-CAND-134|Same professional-service accounting family; profession retained as dimension.; provenance=ODOO18:277|
|278|531601011 ค่าบริการวิชาชีพ - ตรวจสอบบัญชี|Expenses|Accounting/audit/system/legal professional fees|G03-CAND-134|Same professional-service accounting family; profession retained as dimension.; provenance=ODOO18:278|
|279|531601012 ค่าบริการวิชาชีพ - วางระบบบัญชี|Expenses|Accounting/audit/system/legal professional fees|G03-CAND-134|Same professional-service accounting family; profession retained as dimension.; provenance=ODOO18:279|
|280|531601013 ค่าบริการวิชาชีพ - ที่ปรึกษากฎหมาย|Expenses|Accounting/audit/system/legal professional fees|G03-CAND-134|Same professional-service accounting family; profession retained as dimension.; provenance=ODOO18:280|
|281|531701010 ค่าซ่อมแซม - รถยนต์|Expenses|Repair expense by asset class|G03-CAND-135|Same repair/maintenance expense role; asset class retained as dimension.; provenance=ODOO18:281|
|282|531701011 ค่าซ่อมแซม - อุปกรณ์สำนักงาน|Expenses|Repair expense by asset class|G03-CAND-135|Same repair/maintenance expense role; asset class retained as dimension.; provenance=ODOO18:282|
|283|531701012 ค่าซ่อมแซม - ระบบไฟฟ้า|Expenses|Repair expense by asset class|G03-CAND-135|Same repair/maintenance expense role; asset class retained as dimension.; provenance=ODOO18:283|
|284|531701013 ค่าซ่อมแซม - อาคาร|Expenses|Repair expense by asset class|G03-CAND-135|Same repair/maintenance expense role; asset class retained as dimension.; provenance=ODOO18:284|
|289|531801011 ค่าธรรมเนียมหนังสือรับรองบริษัท|Expenses|Company/government/registration/inspection fees|G03-CAND-140|Same administrative/regulatory fee family; fee subtype retained as dimension.; provenance=ODOO18:289|
|290|531801012 ค่าธรรมเนียมรัฐ|Expenses|Company/government/registration/inspection fees|G03-CAND-140|Same administrative/regulatory fee family; fee subtype retained as dimension.; provenance=ODOO18:290|
|291|531801013 ค่าธรรมเนียมอื่น|Expenses|Company/government/registration/inspection fees|G03-CAND-140|Same administrative/regulatory fee family; fee subtype retained as dimension.; provenance=ODOO18:291|
|292|531801014 ค่าจดทะเบียนสิทธิและนิติกรรม|Expenses|Company/government/registration/inspection fees|G03-CAND-140|Same administrative/regulatory fee family; fee subtype retained as dimension.; provenance=ODOO18:292|
|293|531801015 ค่าตรวจสภาพรถยนต์|Expenses|Company/government/registration/inspection fees|G03-CAND-140|Same administrative/regulatory fee family; fee subtype retained as dimension.; provenance=ODOO18:293|
|295|531801017 ค่าธรรมเนียมตู้แดง|Expenses|Company/government/registration/inspection fees|G03-CAND-140|Same administrative/regulatory fee family; fee subtype retained as dimension.; provenance=ODOO18:295|
|296|531801018 ค่าเซ็นอนุมัติแบบงานก่อสร้าง|Expenses|Company/government/registration/inspection fees|G03-CAND-140|Same administrative/regulatory fee family; fee subtype retained as dimension.; provenance=ODOO18:296|
|298|531901011 ค่าเสื่อมราคา - ยานพาหนะส่วนสำนักงาน|Depreciation|Depreciation expense by tangible asset class|K15|Same depreciation treatment; asset class retained in asset subledger/dimension.; provenance=ODOO18:298|
|299|531901012 ค่าเสื่อมราคา - เครื่องตกแต่งสำนักงาน|Depreciation|Depreciation expense by tangible asset class|K15|Same depreciation treatment; asset class retained in asset subledger/dimension.; provenance=ODOO18:299|
|300|531901013 ค่าเสื่อมราคา - อุปกรณ์สำนักงาน|Depreciation|Depreciation expense by tangible asset class|K15|Same depreciation treatment; asset class retained in asset subledger/dimension.; provenance=ODOO18:300|
|301|531901014 ค่าเสื่อมราคา - คอมพิวเตอร์|Depreciation|Depreciation expense by tangible asset class|K15|Same depreciation treatment; asset class retained in asset subledger/dimension.; provenance=ODOO18:301|
|302|531901015 ค่าเสื่อมราคา - ระบบไฟฟ้าสำนักงาน|Depreciation|Depreciation expense by tangible asset class|K15|Same depreciation treatment; asset class retained in asset subledger/dimension.; provenance=ODOO18:302|
|303|531901016 ค่าเสื่อมราคา - ส่วนปรับปรุงภูมิทัศน์|Depreciation|Depreciation expense by tangible asset class|K15|Same depreciation treatment; asset class retained in asset subledger/dimension.; provenance=ODOO18:303|
|304|531901017 ค่าตัดจำน่าย - ซอฟต์แวร์|Depreciation|Amortization of software/rights|G03-CAND-142|Same intangible amortization role; intangible class retained as dimension.; provenance=ODOO18:304|
|305|531901018 ค่าตัดจำน่าย - ลิขสิทธิ์|Expenses|Amortization of software/rights|G03-CAND-142|Same intangible amortization role; intangible class retained as dimension.; provenance=ODOO18:305|
|320|551101010 ภาษีเงินได้นิติบุคคล|Expenses|Corporate income tax expense|K30|Same CIT expense accounting treatment as K30.; provenance=ODOO18:320|
|328|611101010 ต้นทุนบริการ - อาหารเครื่องดื่ม|Expenses|Direct service delivery cost|G03-CAND-161|Same direct service-cost purpose; service component retained as dimension.; provenance=ODOO18:328|
|329|611101011 ต้นทุนบริการ - จ้างภายนอกให้บริการ|Expenses|Direct service delivery cost|G03-CAND-161|Same direct service-cost purpose; service component retained as dimension.; provenance=ODOO18:329|
|330|611101012 ต้นทุนบริการ - การรักษาความปลอดภัย|Expenses|Direct service delivery cost|G03-CAND-161|Same direct service-cost purpose; service component retained as dimension.; provenance=ODOO18:330|
|338|711201010 ค่าจ้างแรงงาน - แผนกผลิต|Expenses|Production wages/overtime/special pay|G03-CAND-169|Same production-labor cost-flow; compensation component retained as dimension.; provenance=ODOO18:338|
|339|711201011 ค่าล่วงเวลาพนักงาน - แผนกผลิต|Expenses|Production wages/overtime/special pay|G03-CAND-169|Same production-labor cost-flow; compensation component retained as dimension.; provenance=ODOO18:339|
|340|711201012 ค่าจ้างพิเศษ - แผนกผลิต|Expenses|Production wages/overtime/special pay|G03-CAND-169|Same production-labor cost-flow; compensation component retained as dimension.; provenance=ODOO18:340|
|342|711301011 ค่าอุปกรณ์โรงงาน|Expenses|Factory equipment/consumables/packaging/ink/gas|G03-CAND-171|Same consumable overhead cost-flow; material subtype retained as dimension.; provenance=ODOO18:342|
|343|711301012 ค่าวัสดุสิ้นเปลืองโรงงาน|Expenses|Factory equipment/consumables/packaging/ink/gas|G03-CAND-171|Same consumable overhead cost-flow; material subtype retained as dimension.; provenance=ODOO18:343|
|344|711301013 ค่าบรรจุกล่อง|Expenses|Factory equipment/consumables/packaging/ink/gas|G03-CAND-171|Same consumable overhead cost-flow; material subtype retained as dimension.; provenance=ODOO18:344|
|345|711301014 ค่าน้ำมัน - รถโฟลคลิฟท์|Expenses|Fuel for production logistics vehicles|G03-CAND-172|Same factory fuel overhead role; vehicle type retained as dimension.; provenance=ODOO18:345|
|346|711301015 ค่าน้ำมัน - รถกระบะ|Expenses|Fuel for production logistics vehicles|G03-CAND-172|Same factory fuel overhead role; vehicle type retained as dimension.; provenance=ODOO18:346|
|347|711301016 ค่าหมึกพิมพ์กล่อง|Expenses|Factory equipment/consumables/packaging/ink/gas|G03-CAND-171|Same consumable overhead cost-flow; material subtype retained as dimension.; provenance=ODOO18:347|
|348|711301017 ค่าแก๊ส|Expenses|Factory equipment/consumables/packaging/ink/gas|G03-CAND-171|Same consumable overhead cost-flow; material subtype retained as dimension.; provenance=ODOO18:348|
|352|711302010 ค่าไฟฟ้าโรงงาน|Expenses|Factory electricity/water|G03-CAND-176|Same factory utility cost-flow; utility type retained as dimension.; provenance=ODOO18:352|
|353|711302011 ค่าน้ำประปาโรงงาน|Expenses|Factory electricity/water|G03-CAND-176|Same factory utility cost-flow; utility type retained as dimension.; provenance=ODOO18:353|
|355|711401010 ค่าเสื่อมราคา - อาคารโรงงาน|Depreciation|Depreciation of production assets|G03-CAND-178|Same manufacturing depreciation cost-flow; asset class retained as dimension.; provenance=ODOO18:355|
|356|711401011 ค่าเสื่อมราคา - เครื่องจักร|Depreciation|Depreciation of production assets|G03-CAND-178|Same manufacturing depreciation cost-flow; asset class retained as dimension.; provenance=ODOO18:356|
|357|711401012 ค่าเสื่อมราคา - ยานพาหนะส่วนโรงงาน|Depreciation|Depreciation of production assets|G03-CAND-178|Same manufacturing depreciation cost-flow; asset class retained as dimension.; provenance=ODOO18:357|
|358|711401013 ค่าเสื่อมราคา - อุปกรณ์โรงงาน|Depreciation|Depreciation of production assets|G03-CAND-178|Same manufacturing depreciation cost-flow; asset class retained as dimension.; provenance=ODOO18:358|
|359|711401014 ค่าเสื่อมราคา - ระบบไฟฟ้าโรงงาน|Depreciation|Depreciation of production assets|G03-CAND-178|Same manufacturing depreciation cost-flow; asset class retained as dimension.; provenance=ODOO18:359|
|362|911001010 ภาษีซื้อต้องห้าม / ขอคืนไม่ได้|Expenses|Input VAT not recoverable/claimed|G03-CAND-181|Same non-creditable input-VAT expense family; reason retained as dimension.; provenance=ODOO18:362|
|363|911001011 ภาษีซื้อไม่ประสงค์ขอคืน|Expenses|Input VAT not recoverable/claimed|G03-CAND-181|Same non-creditable input-VAT expense family; reason retained as dimension.; provenance=ODOO18:363|
|374|920001014 บัญชีพัก - ค่าบริการ GP-GRAB|Expenses|Marketplace GP/service-fee suspense by channel|G03-CAND-192|Same channel fee-suspense role; marketplace retained as dimension.; provenance=ODOO18:374|
|375|920001015 บัญชีพัก - ค่าบริการ GP-LINEMAN|Expenses|Marketplace GP/service-fee suspense by channel|G03-CAND-192|Same channel fee-suspense role; marketplace retained as dimension.; provenance=ODOO18:375|
|376|920001016 บัญชีพัก - ค่าบริการ GP-SHOPPEE|Expenses|Marketplace GP/service-fee suspense by channel|G03-CAND-192|Same channel fee-suspense role; marketplace retained as dimension.; provenance=ODOO18:376|