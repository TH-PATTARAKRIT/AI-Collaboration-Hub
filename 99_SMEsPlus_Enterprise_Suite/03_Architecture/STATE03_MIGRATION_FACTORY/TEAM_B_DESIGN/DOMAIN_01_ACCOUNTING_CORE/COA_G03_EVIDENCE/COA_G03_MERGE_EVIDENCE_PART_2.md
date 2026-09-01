# COA-G03 Merge Evidence Part 2

Source: Boss-controlled ODOO18 workbook SHA256 `0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`; row key `r` = ODOO18 data row 0..388. Authority: G02 `497c80887f82dfca4967ca43f83b4ecc3c01d8d8`; G03 readiness `ad0451e7b6b1e8962659b35056c46dc10a1b6aa6`; prompt `8d3a974828ccde0c9e08964ebdeec1b58f2cc467`.

For each merged source: code/name/type/business meaning/target/equivalence/provenance. 13 DNM controls were tested before merge.

|r|code/name|type|business meaning|target|equivalence evidence|
|--:|---|---|---|---|---|
|82|141400014 ค่าเสื่อมราคาสะสม - ระบบไฟฟ้าโรงงาน|Fixed Assets|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:82|
|83|141500010 ค่าตัดจำหน่ายสะสม - ซอฟแวร์|Fixed Assets|Accumulated amortization of intangibles|G03-CAND-027|Same contra-intangible role; intangible class retained as dimension.; provenance=ODOO18:83|
|84|141500011 ค่าตัดจำหน่ายสะสม - ลิขสิทธิ์|Fixed Assets|Accumulated amortization of intangibles|G03-CAND-027|Same contra-intangible role; intangible class retained as dimension.; provenance=ODOO18:84|
|88|211100013 เจ้าหนี้การค้าอื่น - สินทรัพย์ถาวร|Payable|Trade payable for fixed-asset vendor purchases|K08|Same Payable type and reconcile=True; purchase nature retained as source attribute.; provenance=ODOO18:88|
|93|211501010 เงินสำรองจ่าย - กรรมการ|Payable|Reimbursement/advance payable to staff/director|G03-CAND-034|Same reimbursement payable clearing; person role retained as dimension.; provenance=ODOO18:93|
|94|211501011 เงินสำรองจ่าย - พนักงาน|Payable|Reimbursement/advance payable to staff/director|G03-CAND-034|Same reimbursement payable clearing; person role retained as dimension.; provenance=ODOO18:94|
|96|221101010 รายได้รับล่วงหน้า|Current Liabilities|Revenue received in advance|G03-CAND-035|Same timing liability role; revenue type retained as dimension.; provenance=ODOO18:96|
|97|221101011 รายได้รับล่วงหน้า - ค่านายหน้า|Current Liabilities|Revenue received in advance|G03-CAND-035|Same timing liability role; revenue type retained as dimension.; provenance=ODOO18:97|
|99|222101010 เงินเดือนค้างจ่าย - แผนกบริหาร|Current Liabilities|Salary accrued by department|G03-CAND-037|Same payroll accrual treatment; department retained as dimension.; provenance=ODOO18:99|
|100|222101011 เงินเดือนค้างจ่าย - แผนกขาย|Current Liabilities|Salary accrued by department|G03-CAND-037|Same payroll accrual treatment; department retained as dimension.; provenance=ODOO18:100|
|101|222101012 เงินเดือนค้างจ่าย - แผนกผลิต|Current Liabilities|Salary accrued by department|G03-CAND-037|Same payroll accrual treatment; department retained as dimension.; provenance=ODOO18:101|
|104|222101021 ค่าตอบแทนพนักงานค้างจ่าย - เงินพิเศษ|Current Liabilities|Variable employee compensation accrued|G03-CAND-040|Same employee-compensation accrual role; compensation component retained as dimension.; provenance=ODOO18:104|
|105|222101022 ค่าตอบแทนพนักงานค้างจ่าย - ค่าล่วงเวลา|Current Liabilities|Variable employee compensation accrued|G03-CAND-040|Same employee-compensation accrual role; compensation component retained as dimension.; provenance=ODOO18:105|
|106|222101023 ค่าตอบแทนพนักงานค้างจ่าย - ค่าเบี้ยขยัน|Current Liabilities|Variable employee compensation accrued|G03-CAND-040|Same employee-compensation accrual role; compensation component retained as dimension.; provenance=ODOO18:106|
|107|222101039 ค่าตอบแทนพนักงานค้างจ่าย - อื่นๆ|Current Liabilities|Variable employee compensation accrued|G03-CAND-040|Same employee-compensation accrual role; compensation component retained as dimension.; provenance=ODOO18:107|
|108|222201010 ค่าใช้จ่ายที่ปรึกษาค้างจ่าย - ค่าเดินทาง|Current Liabilities|Consultant-related expense accrual|G03-CAND-041|Same consultant accrual role; reimbursable nature retained as dimension.; provenance=ODOO18:108|
|109|222201011 ค่าใช้จ่ายที่ปรึกษาค้างจ่าย - ค่าที่พัก|Current Liabilities|Consultant-related expense accrual|G03-CAND-041|Same consultant accrual role; reimbursable nature retained as dimension.; provenance=ODOO18:109|
|110|222201012 ค่าใช้จ่ายที่ปรึกษาค้างจ่าย - ค่ารับรอง|Current Liabilities|Consultant-related expense accrual|G03-CAND-041|Same consultant accrual role; reimbursable nature retained as dimension.; provenance=ODOO18:110|
|111|222201013 ค่าใช้จ่ายที่ปรึกษาค้างจ่าย - อื่นๆ|Current Liabilities|Consultant-related expense accrual|G03-CAND-041|Same consultant accrual role; reimbursable nature retained as dimension.; provenance=ODOO18:111|
|113|222401010 ค่าไฟฟ้าค้างจ่าย|Current Liabilities|Utilities and recurring service expense accrued|G03-CAND-043|Same accrued-service timing role; service nature retained as dimension.; provenance=ODOO18:113|
|114|222401011 ค่าน้ำประปาค้างจ่าย|Current Liabilities|Utilities and recurring service expense accrued|G03-CAND-043|Same accrued-service timing role; service nature retained as dimension.; provenance=ODOO18:114|
|115|222401012 ค่าโทรศัพท์ค้างจ่าย|Current Liabilities|Utilities and recurring service expense accrued|G03-CAND-043|Same accrued-service timing role; service nature retained as dimension.; provenance=ODOO18:115|
|116|222401013 ค่าอินเตอร์เน็ตค้างจ่าย|Current Liabilities|Utilities and recurring service expense accrued|G03-CAND-043|Same accrued-service timing role; service nature retained as dimension.; provenance=ODOO18:116|
|117|222401014 ค่าแก๊สค้างจ่าย|Current Liabilities|Utilities and recurring service expense accrued|G03-CAND-043|Same accrued-service timing role; service nature retained as dimension.; provenance=ODOO18:117|
|118|222401015 ค่าโฆษณาค้างจ่าย|Current Liabilities|Utilities and recurring service expense accrued|G03-CAND-043|Same accrued-service timing role; service nature retained as dimension.; provenance=ODOO18:118|
|119|222401016 ค่าธรรมเนียมเก็บขยะมูลฝอยค้างจ่าย|Current Liabilities|Utilities and recurring service expense accrued|G03-CAND-043|Same accrued-service timing role; service nature retained as dimension.; provenance=ODOO18:119|
|120|222401017 ค่าบริการคลาวด์ค้างจ่าย|Current Liabilities|Utilities and recurring service expense accrued|G03-CAND-043|Same accrued-service timing role; service nature retained as dimension.; provenance=ODOO18:120|
|121|222501010 ค่าเช่าค้างจ่าย - โกดัง|Current Liabilities|Rent accrued by leased asset type|G03-CAND-044|Same rental-accrual recognition; asset type retained as dimension.; provenance=ODOO18:121|
|122|222501011 ค่าเช่าค้างจ่าย - สำนักงาน|Current Liabilities|Rent accrued by leased asset type|G03-CAND-044|Same rental-accrual recognition; asset type retained as dimension.; provenance=ODOO18:122|
|123|222501012 ค่าเช่าค้างจ่าย - รถยนต์|Current Liabilities|Rent accrued by leased asset type|G03-CAND-044|Same rental-accrual recognition; asset type retained as dimension.; provenance=ODOO18:123|
|124|222501013 ค่าเช่าค้างจ่าย - เครื่องถ่ายเอกสาร|Current Liabilities|Rent accrued by leased asset type|G03-CAND-044|Same rental-accrual recognition; asset type retained as dimension.; provenance=ODOO18:124|
|125|222501014 ค่าเช่าค้างจ่าย - คอมพิวเตอร์|Current Liabilities|Rent accrued by leased asset type|G03-CAND-044|Same rental-accrual recognition; asset type retained as dimension.; provenance=ODOO18:125|
|126|222501015 ค่าเบี้ยประกันภัยค้างจ่าย - รถยนต์|Current Liabilities|Insurance expense accrued|G03-CAND-045|Same insurance-accrual treatment; coverage class retained as dimension.; provenance=ODOO18:126|
|127|222501016 ค่าเบี้ยประกันภัยค้างจ่าย - อาคาร|Current Liabilities|Insurance expense accrued|G03-CAND-045|Same insurance-accrual treatment; coverage class retained as dimension.; provenance=ODOO18:127|
|128|222501017 ค่าเบี้ยประกันภัยค้างจ่าย - กลุ่มพนักงาน|Current Liabilities|Insurance expense accrued|G03-CAND-045|Same insurance-accrual treatment; coverage class retained as dimension.; provenance=ODOO18:128|
|133|222601010 ค่าบริการวิชาชีพค้างจ่าย - บัญชี|Current Liabilities|Professional service fees accrued|G03-CAND-050|Same professional-service accrual treatment; profession retained as dimension.; provenance=ODOO18:133|
|134|222601011 ค่าบริการวิชาชีพค้างจ่าย - ตรวจสอบบัญชี|Current Liabilities|Professional service fees accrued|G03-CAND-050|Same professional-service accrual treatment; profession retained as dimension.; provenance=ODOO18:134|
|135|222601012 ค่าบริการวิชาชีพค้างจ่าย - วางระบบบัญชี|Current Liabilities|Professional service fees accrued|G03-CAND-050|Same professional-service accrual treatment; profession retained as dimension.; provenance=ODOO18:135|
|136|222601013 ค่าบริการวิชาชีพค้างจ่าย - ที่ปรึกษากฎหมาย|Current Liabilities|Professional service fees accrued|G03-CAND-050|Same professional-service accrual treatment; profession retained as dimension.; provenance=ODOO18:136|
|137|222701010 ค่าซ่อมแซมค้างจ่าย - เครื่องจักร|Current Liabilities|Repair expense accrued by asset class|G03-CAND-051|Same repair-accrual treatment; asset class retained as dimension.; provenance=ODOO18:137|
|138|222701011 ค่าซ่อมแซมค้างจ่าย - รถยนต์|Current Liabilities|Repair expense accrued by asset class|G03-CAND-051|Same repair-accrual treatment; asset class retained as dimension.; provenance=ODOO18:138|
|139|222701012 ค่าซ่อมแซมค้างจ่าย - อุปกรณ์สำนักงาน|Current Liabilities|Repair expense accrued by asset class|G03-CAND-051|Same repair-accrual treatment; asset class retained as dimension.; provenance=ODOO18:139|
|140|222701013 ค่าซ่อมแซมค้างจ่าย - ระบบไฟฟ้า|Current Liabilities|Repair expense accrued by asset class|G03-CAND-051|Same repair-accrual treatment; asset class retained as dimension.; provenance=ODOO18:140|
|143|222801010 ค่าอุปกรณ์โรงงานค้างจ่าย|Current Liabilities|Factory supply/consumable accrual|G03-CAND-054|Same factory-overhead accrual; supply type dimension.; provenance=ODOO18:143|
|144|222801011 ค่าใช้จ่ายวัสดุสิ้นเปลืองโรงงานค้างจ่าย|Current Liabilities|Factory supply/consumable accrual|G03-CAND-054|Same factory-overhead accrual; supply type dimension.; provenance=ODOO18:144|
|145|222901010 ค่าขนส่งเข้าค้างจ่าย|Current Liabilities|Inbound/outbound/unloading logistics accrued|G03-CAND-055|Same logistics accrual timing; direction/service retained as dimension.; provenance=ODOO18:145|
|146|222901011 ค่าขนส่งออกค้างจ่าย|Current Liabilities|Inbound/outbound/unloading logistics accrued|G03-CAND-055|Same logistics accrual timing; direction/service retained as dimension.; provenance=ODOO18:146|
|147|222901012 ค่าลงสินค้าค้างจ่าย|Current Liabilities|Inbound/outbound/unloading logistics accrued|G03-CAND-055|Same logistics accrual timing; direction/service retained as dimension.; provenance=ODOO18:147|
|148|222901013 ค่าส่วนปรับปรุงที่ดินค้างจ่าย|Current Liabilities|Land/landscape improvement accrual|G03-CAND-056|Same capital-improvement accrual role; project class retained as dimension.; provenance=ODOO18:148|
|149|222901014 ค่าปรับปรุงภูมิทัศน์ค้างจ่าย|Current Liabilities|Land/landscape improvement accrual|G03-CAND-056|Same capital-improvement accrual role; project class retained as dimension.; provenance=ODOO18:149|