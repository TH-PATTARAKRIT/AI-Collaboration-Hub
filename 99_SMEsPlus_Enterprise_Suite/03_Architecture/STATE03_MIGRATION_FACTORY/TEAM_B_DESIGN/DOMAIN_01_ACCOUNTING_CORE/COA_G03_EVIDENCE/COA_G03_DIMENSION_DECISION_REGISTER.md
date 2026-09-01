# COA-G03 Dimension Decision Register

Date: 2026-09-01
Project: SMEsPlus ENTERPRISE SUITE
Repo/Branch: `TH-PATTARAKRIT/AI-Collaboration-Hub` / `SMEsPlus`
Gate: `COA-G03 — AI Semantic Consolidation`
Authority: G02 Boss closure `497c80887f82dfca4967ca43f83b4ecc3c01d8d8`; G03 readiness `ad0451e7b6b1e8962659b35056c46dc10a1b6aa6`; prompt `8d3a974828ccde0c9e08964ebdeec1b58f2cc467`.
Primary evidence: Boss-controlled ODOO18 workbook, 389 rows, SHA-256 `0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`.
Candidate IDs are evidence-only, not production IDs. No Evidence = No Progress. Never Skip Gate. Boss is sole Final Approver.


Operational/analytical distinctions are dimensioned only when accounting treatment/control is materially equivalent.

|Target|Rows|Dimension/source attribute retained|
|---|---|---|
|`K01` Cash on Hand|0,1,2,3|cash custodian / company/journal|
|`K02` Bank Deposit|5,6,7,8|bank account / bank / branch|
|`K07` Trade Receivables|11,16,17,18,19,24|sales channel / marketplace / POS|
|`K10` Inventory|25,26,27,28|inventory class / location|
|`G03-CAND-014` Prepaid Operating Expenses|32,33,34,35,36|expense nature / contract|
|`G03-CAND-015` Accrued Income|37,38|income nature|
|`G03-CAND-017` Security Deposits Paid|40,41|deposit purpose / counterparty|
|`G03-CAND-019` Prepaid Insurance|47,48,49|insurance class / asset/employee|
|`K13` Fixed Assets|56,57,58,59,60,61,62,63,64,65,66,67,68|asset class / location|
|`G03-CAND-026` Intangible Assets|69,70|intangible class|
|`K14` Accumulated Depreciation|71,72,73,74,75,76,77,78,79,80,81,82|asset class|
|`G03-CAND-027` Accumulated Amortization|83,84|intangible class|
|`K08` Trade Payables|85,88|purchase nature / asset class|
|`G03-CAND-034` Staff/Director Reimbursement Payable|93,94|counterparty role|
|`G03-CAND-035` Unearned / Deferred Revenue|96,97|revenue nature|
|`G03-CAND-037` Payroll Accrual|99,100,101|department|
|`G03-CAND-040` Employee Compensation Accrual|104,105,106,107|compensation type|
|`G03-CAND-041` Consultant Expense Accrual|108,109,110,111|expense nature|
|`G03-CAND-043` Utilities / Service Accrual|113,114,115,116,117,118,119,120|service type|
|`G03-CAND-044` Rent Accrual|121,122,123,124,125|leased asset type|
|`G03-CAND-045` Insurance Accrual|126,127,128|coverage class|
|`G03-CAND-050` Professional Fee Accrual|133,134,135,136|professional service type|
|`G03-CAND-051` Repair & Maintenance Accrual|137,138,139,140|asset class|
|`G03-CAND-054` Factory Supply Accrual|143,144|factory supply type|
|`G03-CAND-055` Logistics Accrual|145,146,147|logistics type|
|`G03-CAND-056` Capital Improvement Accrual|148,149|project / improvement type|
|`G03-CAND-059` Deposits / Security Received|152,153|deposit type|
|`K19` Operating Revenue|177,183,184,185,186|sales channel / marketplace|
|`G03-CAND-081` Scrap Sales Income|190,191,194|scrap category|
|`K12` Cost of Goods Sold|196,197,198|inventory class|
|`G03-CAND-094` Sales Travel & Subsistence|209,210,211|travel type|
|`G03-CAND-095` Marketing & Promotion Expense|212,213,214,215|marketing activity / campaign|
|`G03-CAND-096` Outbound Logistics Expense|216,217|logistics service type|
|`G03-CAND-097` Marketplace Service Fee|218,219,220,221|marketplace/channel|
|`G03-CAND-098` Marketplace Shipping/Promotion Discount|222,223,224,225|marketplace/channel|
|`G03-CAND-099` Salary Expense|226,227|department|
|`G03-CAND-101` Employee Variable Compensation|229,230,231,232|compensation type|
|`G03-CAND-117` Utilities Expense|248,249|utility type|
|`G03-CAND-118` Communications Expense|250,251,255|service type|
|`G03-CAND-119` Cloud / Domain / Platform Services|252,253,254|digital service type|
|`G03-CAND-122` Rent Expense|258,259,260,261|leased asset type|
|`G03-CAND-124` Insurance Expense|263,264,265,266,267|coverage class|
|`G03-CAND-134` Professional Services Expense|277,278,279,280|professional service type|
|`G03-CAND-135` Repair & Maintenance Expense|281,282,283,284|asset class|
|`G03-CAND-140` Government / Registration Fees|289,290,291,292,293,295,296|fee type|
|`K15` Depreciation Expense|297,298,299,300,301,302,303|asset class|
|`G03-CAND-142` Amortization Expense|304,305|intangible class|
|`K30` CIT Expense|315,320|tax period/source|
|`G03-CAND-161` Direct Cost of Services|328,329,330|service cost component|
|`G03-CAND-169` Production Labor Cost|338,339,340|compensation type|
|`G03-CAND-171` Factory Consumables Overhead|342,343,344,347,348|factory overhead type|
|`G03-CAND-172` Factory Vehicle/Forklift Fuel Overhead|345,346|vehicle type|
|`G03-CAND-176` Factory Utilities|352,353|utility type|
|`G03-CAND-178` Manufacturing Depreciation|355,356,357,358,359|asset class|
|`G03-CAND-181` Non-creditable Input VAT Expense|362,363|non-credit reason|
|`G03-CAND-192` Marketplace Fee Suspense|374,375,376|marketplace/channel|