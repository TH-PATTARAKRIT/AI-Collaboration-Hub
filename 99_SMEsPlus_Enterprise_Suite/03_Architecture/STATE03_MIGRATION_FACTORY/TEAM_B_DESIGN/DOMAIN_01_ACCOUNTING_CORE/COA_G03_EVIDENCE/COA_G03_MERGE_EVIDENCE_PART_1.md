# COA-G03 Merge Evidence Part 1

Source: Boss-controlled ODOO18 workbook SHA256 `0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`; row key `r` = ODOO18 data row 0..388. Authority: G02 `497c80887f82dfca4967ca43f83b4ecc3c01d8d8`; G03 readiness `ad0451e7b6b1e8962659b35056c46dc10a1b6aa6`; prompt `8d3a974828ccde0c9e08964ebdeec1b58f2cc467`.

For each merged source: code/name/type/business meaning/target/equivalence/provenance. 13 DNM controls were tested before merge.

|r|code/name|type|business meaning|target|equivalence evidence|
|--:|---|---|---|---|---|
|0|110000002 Cash Bakery|Bank and Cash|Cash on hand / petty/reserve cash|K01|Same cash recognition/control; custodian/company-specific naming retained as dimension/provenance.; provenance=ODOO18:0|
|2|111000020 เงินสดย่อย - ผู้รักษาเงินสดย่อย|Bank and Cash|Cash on hand / petty/reserve cash|K01|Same cash recognition/control; custodian/company-specific naming retained as dimension/provenance.; provenance=ODOO18:2|
|3|111000030 เงินสำรอง - ผู้รักษาเงินสำรอง|Bank and Cash|Cash on hand / petty/reserve cash|K01|Same cash recognition/control; custodian/company-specific naming retained as dimension/provenance.; provenance=ODOO18:3|
|6|111200011 เงินฝากกระแสรายวัน|Bank and Cash|Bank deposit|K02|Same bank-deposit accounting treatment; account/bank identity retained outside canonical GL identity.; provenance=ODOO18:6|
|7|111200012 เงินฝากกระแสรายวัน |Bank and Cash|Bank deposit|K02|Same bank-deposit accounting treatment; account/bank identity retained outside canonical GL identity.; provenance=ODOO18:7|
|8|111300010 เงินฝากออมทรัพย์ XXX-XXXXXX|Bank and Cash|Bank deposit|K02|Same bank-deposit accounting treatment; account/bank identity retained outside canonical GL identity.; provenance=ODOO18:8|
|16|111600015 ลูกหนี้ - ขายออนไลน์ - GRAB|Receivable|Trade receivable by sales channel|K07|Same AR control and reconcile=True; channel/POS identity is operational dimension.; provenance=ODOO18:16|
|17|111600016 ลูกหนี้ - ขายออนไลน์ - LINEMAN|Receivable|Trade receivable by sales channel|K07|Same AR control and reconcile=True; channel/POS identity is operational dimension.; provenance=ODOO18:17|
|18|111600017 ลูกหนี้ - ขายออนไลน์ - SHOPEE|Receivable|Trade receivable by sales channel|K07|Same AR control and reconcile=True; channel/POS identity is operational dimension.; provenance=ODOO18:18|
|19|111600018 ลูกหนี้ - ขายออนไลน์ - LAZADA|Receivable|Trade receivable by sales channel|K07|Same AR control and reconcile=True; channel/POS identity is operational dimension.; provenance=ODOO18:19|
|24|111600023 ลูกหนี้การค้า (PoS)|Receivable|Trade receivable by sales channel|K07|Same AR control and reconcile=True; channel/POS identity is operational dimension.; provenance=ODOO18:24|
|26|111700011 สินค้าคงเหลือ - วัตถุดิบ|Current Assets|Inventory by stock class|K10|Same current-asset inventory valuation role; stock class retained as dimension.; provenance=ODOO18:26|
|27|111700012 สินค้าคงเหลือ - สำเร็จรูปการผลิต|Current Assets|Inventory by stock class|K10|Same current-asset inventory valuation role; stock class retained as dimension.; provenance=ODOO18:27|
|28|111700013 สินค้าคงเหลือ - วัตถุโรงงาน|Current Assets|Inventory by stock class|K10|Same current-asset inventory valuation role; stock class retained as dimension.; provenance=ODOO18:28|
|32|111801013 ค่าใช้จ่ายจ่ายล่วงหน้า - ค่าสินค้า|Current Assets|Prepaid operating expenses by nature|G03-CAND-014|Same prepayment timing role; expense nature retained as dimension/source attribute.; provenance=ODOO18:32|
|33|111801014 ค่าใช้จ่ายจ่ายล่วงหน้า - ค่าเช่า|Current Assets|Prepaid operating expenses by nature|G03-CAND-014|Same prepayment timing role; expense nature retained as dimension/source attribute.; provenance=ODOO18:33|
|34|111801015 ค่าใช้จ่ายจ่ายล่วงหน้า - เบี้ยประกันภัย|Current Assets|Prepaid operating expenses by nature|G03-CAND-014|Same prepayment timing role; expense nature retained as dimension/source attribute.; provenance=ODOO18:34|
|35|111801016 ค่าใช้จ่ายจ่ายล่วงหน้า - วัสดุสิ้นเปลืองสำนักงาน|Current Assets|Prepaid operating expenses by nature|G03-CAND-014|Same prepayment timing role; expense nature retained as dimension/source attribute.; provenance=ODOO18:35|
|36|111801017 ค่าใช้จ่ายจ่ายล่วงหน้า - อื่น ๆ|Current Assets|Prepaid operating expenses by nature|G03-CAND-014|Same prepayment timing role; expense nature retained as dimension/source attribute.; provenance=ODOO18:36|
|37|111802010 รายได้ค้างรับ - ดอกเบี้ย|Current Assets|Accrued income receivable|G03-CAND-015|Same accrual asset role; income nature retained as dimension.; provenance=ODOO18:37|
|38|111802011 รายได้ค้างรับอื่น|Current Assets|Accrued income receivable|G03-CAND-015|Same accrual asset role; income nature retained as dimension.; provenance=ODOO18:38|
|40|111803011 เงินมัดจำจ่าย|Current Assets|Security/deposit paid|G03-CAND-017|Same refundable deposit treatment; deposit purpose retained as dimension.; provenance=ODOO18:40|
|41|111803021 เงินประกันจ่าย - หม้อไฟฟ้า|Current Assets|Security/deposit paid|G03-CAND-017|Same refundable deposit treatment; deposit purpose retained as dimension.; provenance=ODOO18:41|
|47|111805010 กรมธรรม์ประกันอัคคีภัย - สินค้าและอาคาร|Current Assets|Insurance policy asset by covered class|G03-CAND-019|Same insurance-prepayment treatment; coverage class retained as dimension.; provenance=ODOO18:47|
|48|111805011 กรมธรรม์ประกันอัคคีภัย - ยานพาหนะ|Current Assets|Insurance policy asset by covered class|G03-CAND-019|Same insurance-prepayment treatment; coverage class retained as dimension.; provenance=ODOO18:48|
|49|111805012 กรมธรรม์ประกันอุบัติเหตุ - พนักงาน|Current Assets|Insurance policy asset by covered class|G03-CAND-019|Same insurance-prepayment treatment; coverage class retained as dimension.; provenance=ODOO18:49|
|57|141000012 ยานพาหนะส่วนสำนักงาน|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:57|
|58|141000013 เครื่องตกแต่งสำนักงาน|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:58|
|59|141000014 อุปกรณ์สำนักงาน|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:59|
|60|141000015 คอมพิวเตอร์|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:60|
|61|141000016 ระบบไฟฟ้าสำนักงาน|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:61|
|62|141000017 ส่วนปรับปรุงภูมิทัศน์|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:62|
|63|141000018 ส่วนปรับปรุงที่ดิน|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:63|
|64|141100010 อาคารโรงงาน|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:64|
|65|141100011 เครื่องจักร|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:65|
|66|141100012 ยานพาหนะส่วนโรงงาน|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:66|
|67|141100013 อุปกรณ์โรงงาน|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:67|
|68|141100014 ระบบไฟฟ้าโรงงาน|Fixed Assets|Depreciable tangible fixed assets|K13|Same gross tangible fixed-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:68|
|69|141200010 ซอฟแวร์|Fixed Assets|Software / rights intangible assets|G03-CAND-026|Same intangible recognition; class retained as dimension.; provenance=ODOO18:69|
|70|141200011 ลิขสิทธิ์|Fixed Assets|Software / rights intangible assets|G03-CAND-026|Same intangible recognition; class retained as dimension.; provenance=ODOO18:70|
|72|141300011 ค่าเสื่อมราคาสะสม - ยานพาหนะส่วนสำนักงาน|Fixed Assets|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:72|
|73|141300012 ค่าเสื่อมราคาสะสม - เครื่องตกแต่งสำนักงาน|Fixed Assets|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:73|
|74|141300013 ค่าเสื่อมราคาสะสม - อุปกรณ์สำนักงาน|Depreciation|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:74|
|75|141300014 ค่าเสื่อมราคาสะสม - คอมพิวเตอร์|Fixed Assets|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:75|
|76|141300015 ค่าเสื่อมราคาสะสม - ระบบไฟฟ้าสำนักงาน|Fixed Assets|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:76|
|77|141300016 ค่าเสื่อมราคาสะสม - ส่วนปรับปรุงภูมิทัศน์|Fixed Assets|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:77|
|78|141400010 ค่าเสื่อมราคาสะสม - อาคารโรงงาน|Fixed Assets|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:78|
|79|141400011 ค่าเสื่อมราคาสะสม - เครื่องจักร|Fixed Assets|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:79|
|80|141400012 ค่าเสื่อมราคาสะสม - ยานพาหนะส่วนโรงงาน|Fixed Assets|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:80|
|81|141400013 ค่าเสื่อมราคาสะสม - อุปกรณ์โรงงาน|Fixed Assets|Accumulated depreciation by tangible asset class|K14|Same contra-asset role; asset class retained in asset subledger/dimension.; provenance=ODOO18:81|