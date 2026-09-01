# COA-G03 Merge Evidence Part 3

Source: Boss-controlled ODOO18 workbook SHA256 `0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`; row key `r` = ODOO18 data row 0..388. Authority: G02 `497c80887f82dfca4967ca43f83b4ecc3c01d8d8`; G03 readiness `ad0451e7b6b1e8962659b35056c46dc10a1b6aa6`; prompt `8d3a974828ccde0c9e08964ebdeec1b58f2cc467`.

For each merged source: code/name/type/business meaning/target/equivalence/provenance. 13 DNM controls were tested before merge.

|r|code/name|type|business meaning|target|equivalence evidence|
|--:|---|---|---|---|---|
|152|223001010 เงินมัดจำรับ|Current Liabilities|Refundable deposits received|G03-CAND-059|Same refundable-deposit obligation; deposit type retained as dimension.; provenance=ODOO18:152|
|153|223001011 เงินประกันรับ|Current Liabilities|Refundable deposits received|G03-CAND-059|Same refundable-deposit obligation; deposit type retained as dimension.; provenance=ODOO18:153|
|183|441001010 รายได้จากการขายออนไลน์ - GRAB|Income|Online sales revenue|K19|Same Income type and sales recognition; marketplace identity retained as dimension.; provenance=ODOO18:183|
|184|441001011 รายได้จากการขายออนไลน์ - LINEMAN|Income|Online sales revenue|K19|Same Income type and sales recognition; marketplace identity retained as dimension.; provenance=ODOO18:184|
|185|441001012 รายได้จากการขายออนไลน์ - SHOPEE|Income|Online sales revenue|K19|Same Income type and sales recognition; marketplace identity retained as dimension.; provenance=ODOO18:185|
|186|441001013 รายได้จากการขายออนไลน์ - LAZADA|Income|Online sales revenue|K19|Same Income type and sales recognition; marketplace identity retained as dimension.; provenance=ODOO18:186|
|190|451001013 รายได้จากการขายเศษวัสดุโรงงาน|Other Income|Income from sale of scrap materials|G03-CAND-081|Same scrap-disposal income treatment; scrap source retained as dimension.; provenance=ODOO18:190|
|191|451001014 รายได้จากการขายเศษวัตถุดิบ|Other Income|Income from sale of scrap materials|G03-CAND-081|Same scrap-disposal income treatment; scrap source retained as dimension.; provenance=ODOO18:191|
|194|451001017 รายได้จากการขายเศษวัสดุสำนักงาน|Other Income|Income from sale of scrap materials|G03-CAND-081|Same scrap-disposal income treatment; scrap source retained as dimension.; provenance=ODOO18:194|
|197|511001011 ต้นทุนสินค้าเพื่อขาย - วัตถุดิบ|Cost of Revenue|COGS by inventory class|K12|Same Cost of Revenue role; inventory class retained as dimension.; provenance=ODOO18:197|
|198|511001012 ต้นทุนสินค้าเพื่อขาย - สินค้าสำเร็จรูปการผลิต|Cost of Revenue|COGS by inventory class|K12|Same Cost of Revenue role; inventory class retained as dimension.; provenance=ODOO18:198|
|209|522101011 ค่าเบี้ยเลี้ยง - แผนกขาย|Expenses|Sales travel/per diem/accommodation|G03-CAND-094|Same sales-travel business purpose; travel component retained as dimension.; provenance=ODOO18:209|
|210|522101012 ค่าที่พัก - แผนกขาย|Expenses|Sales travel/per diem/accommodation|G03-CAND-094|Same sales-travel business purpose; travel component retained as dimension.; provenance=ODOO18:210|
|211|522101013 ค่าเดินทาง - แผนกขาย|Expenses|Sales travel/per diem/accommodation|G03-CAND-094|Same sales-travel business purpose; travel component retained as dimension.; provenance=ODOO18:211|
|212|522101014 ค่าโฆษณา|Expenses|Advertising/sample/promotion/market research|G03-CAND-095|Same marketing purpose; campaign/expense subtype retained as dimension.; provenance=ODOO18:212|
|213|522101015 ค่าสินค้าตัวอย่าง|Expenses|Advertising/sample/promotion/market research|G03-CAND-095|Same marketing purpose; campaign/expense subtype retained as dimension.; provenance=ODOO18:213|
|214|522101016 ค่าส่งเสริมการขาย|Expenses|Advertising/sample/promotion/market research|G03-CAND-095|Same marketing purpose; campaign/expense subtype retained as dimension.; provenance=ODOO18:214|
|215|522101017 ค่าวิจัยตลาด|Expenses|Advertising/sample/promotion/market research|G03-CAND-095|Same marketing purpose; campaign/expense subtype retained as dimension.; provenance=ODOO18:215|
|216|522101018 ค่าขนส่งออก|Expenses|Outbound freight/distribution center service|G03-CAND-096|Same distribution/logistics purpose; service type retained as dimension.; provenance=ODOO18:216|
|217|522101019 ค่าบริการศูนย์กระจายสินค้า|Expenses|Outbound freight/distribution center service|G03-CAND-096|Same distribution/logistics purpose; service type retained as dimension.; provenance=ODOO18:217|
|218|523101010 ค่าบริการ - SF-GRAB|Expenses|Marketplace/service platform fee|G03-CAND-097|Same platform-service fee treatment; channel retained as dimension.; provenance=ODOO18:218|
|219|523101011 ค่าบริการ - SF-LINEMAN|Expenses|Marketplace/service platform fee|G03-CAND-097|Same platform-service fee treatment; channel retained as dimension.; provenance=ODOO18:219|
|220|523101012 ค่าบริการ - SF-SHOPEE|Expenses|Marketplace/service platform fee|G03-CAND-097|Same platform-service fee treatment; channel retained as dimension.; provenance=ODOO18:220|
|221|523101013 ค่าบริการ - SF-LAZADA|Expenses|Marketplace/service platform fee|G03-CAND-097|Same platform-service fee treatment; channel retained as dimension.; provenance=ODOO18:221|
|222|523101014 ค่าส่วนลดจัดส่งโดยร้าน - GRAB|Expenses|Seller-funded shipping/discount expense by channel|G03-CAND-098|Same channel-funded discount/shipping support; marketplace retained as dimension.; provenance=ODOO18:222|
|223|523101015 ค่าส่วนลดจัดส่งโดยร้าน - LINEMAN|Expenses|Seller-funded shipping/discount expense by channel|G03-CAND-098|Same channel-funded discount/shipping support; marketplace retained as dimension.; provenance=ODOO18:223|
|224|523101016 ค่าส่วนลดจัดส่งโดยร้าน - SHOPEE|Expenses|Seller-funded shipping/discount expense by channel|G03-CAND-098|Same channel-funded discount/shipping support; marketplace retained as dimension.; provenance=ODOO18:224|
|225|523101017 ค่าส่วนลดจัดส่งโดยร้าน - LAZADA|Expenses|Seller-funded shipping/discount expense by channel|G03-CAND-098|Same channel-funded discount/shipping support; marketplace retained as dimension.; provenance=ODOO18:225|
|226|531101010 เงินเดือน - แผนกบริหาร|Expenses|Employee salary by department|G03-CAND-099|Same salary treatment; department retained as dimension.; provenance=ODOO18:226|
|227|531101011 เงินเดือน - แผนกขาย|Expenses|Employee salary by department|G03-CAND-099|Same salary treatment; department retained as dimension.; provenance=ODOO18:227|
|229|531101021 ค่าตอบแทนพนักงาน - เงินพิเศษ|Expenses|Bonus/overtime/attendance/other compensation|G03-CAND-101|Same employee-compensation family; component retained as dimension.; provenance=ODOO18:229|
|230|531101022 ค่าตอบแทนพนักงาน - ค่าล่วงเวลา|Expenses|Bonus/overtime/attendance/other compensation|G03-CAND-101|Same employee-compensation family; component retained as dimension.; provenance=ODOO18:230|
|231|531101023 ค่าตอบแทนพนักงาน - ค่าเบี้ยขยัน|Expenses|Bonus/overtime/attendance/other compensation|G03-CAND-101|Same employee-compensation family; component retained as dimension.; provenance=ODOO18:231|
|232|531101039 ค่าตอบแทนพนักงาน - อื่นๆ|Expenses|Bonus/overtime/attendance/other compensation|G03-CAND-101|Same employee-compensation family; component retained as dimension.; provenance=ODOO18:232|
|248|531401010 ค่าไฟฟ้า|Expenses|Electricity and water utilities|G03-CAND-117|Same utility operating-cost family; utility type retained as dimension.; provenance=ODOO18:248|
|249|531401011 ค่าน้ำประปา|Expenses|Electricity and water utilities|G03-CAND-117|Same utility operating-cost family; utility type retained as dimension.; provenance=ODOO18:249|
|250|531401012 ค่าโทรศัพท์มือถือ|Expenses|Mobile/internet/communications service|G03-CAND-118|Same communications-service cost family; service retained as dimension.; provenance=ODOO18:250|
|251|531401013 ค่าบริการอินเตอร์เน็ต|Expenses|Mobile/internet/communications service|G03-CAND-118|Same communications-service cost family; service retained as dimension.; provenance=ODOO18:251|
|252|531401014 ค่าบริการคลาวด์โฮสติ้งค์|Expenses|Cloud hosting/domain/platform service|G03-CAND-119|Same digital platform/service-cost family; service retained as dimension.; provenance=ODOO18:252|
|253|531401015 ค่าบริการ - โดเมน|Expenses|Cloud hosting/domain/platform service|G03-CAND-119|Same digital platform/service-cost family; service retained as dimension.; provenance=ODOO18:253|
|254|531401016 ค่าบริการใช้แพลตฟอร์ม|Expenses|Cloud hosting/domain/platform service|G03-CAND-119|Same digital platform/service-cost family; service retained as dimension.; provenance=ODOO18:254|
|255|531401017 ค่าบริการสัญญาณสื่อสารอื่น|Expenses|Mobile/internet/communications service|G03-CAND-118|Same communications-service cost family; service retained as dimension.; provenance=ODOO18:255|
|258|531501010 ค่าเช่า - สำนักงาน|Expenses|Rent by leased asset class|G03-CAND-122|Same rent-expense recognition; leased asset type retained as dimension.; provenance=ODOO18:258|
|259|531501011 ค่าเช่า - รถยนต์|Expenses|Rent by leased asset class|G03-CAND-122|Same rent-expense recognition; leased asset type retained as dimension.; provenance=ODOO18:259|
|260|531501012 ค่าเช่า - เครื่องถ่ายเอกสาร|Expenses|Rent by leased asset class|G03-CAND-122|Same rent-expense recognition; leased asset type retained as dimension.; provenance=ODOO18:260|
|261|531501013 ค่าเช่า - คอมพิวเตอร์|Expenses|Rent by leased asset class|G03-CAND-122|Same rent-expense recognition; leased asset type retained as dimension.; provenance=ODOO18:261|
|263|531501015 ค่าเบี้ยประกัน - อาคาร|Expenses|Insurance by covered class|G03-CAND-124|Same insurance-expense treatment; coverage class retained as dimension.; provenance=ODOO18:263|
|264|531501016 ค่าเบี้ยประกันภัย - กลุ่มพนักงาน|Expenses|Insurance by covered class|G03-CAND-124|Same insurance-expense treatment; coverage class retained as dimension.; provenance=ODOO18:264|
|265|531501017 ค่าเบี้ยประกัน - เครื่องตกแต่ง|Expenses|Insurance by covered class|G03-CAND-124|Same insurance-expense treatment; coverage class retained as dimension.; provenance=ODOO18:265|
|266|531501018 ค่าเบี้ยประกัน - อุปกรณ์|Expenses|Insurance by covered class|G03-CAND-124|Same insurance-expense treatment; coverage class retained as dimension.; provenance=ODOO18:266|