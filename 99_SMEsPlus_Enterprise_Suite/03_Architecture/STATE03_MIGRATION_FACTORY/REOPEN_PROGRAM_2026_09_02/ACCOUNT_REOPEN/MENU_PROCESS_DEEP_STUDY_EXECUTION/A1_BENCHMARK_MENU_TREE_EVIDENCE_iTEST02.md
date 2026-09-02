# A1 — Benchmark Menu Tree Evidence — iTEST02 Instance (Metadata Only)

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001` |
| Jira | `ERPPLUS-138` |
| Project / STATE | `SMEsPlus ENTERPRISE SUITE` / `STATE03 - Architecture` |
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical Branch | `SMEsPlus` (base commit `788479552971940a126a542da5343944f7f3e0d4`, 2026-09-02 08:47 +0700) |
| Execution Branch | `audit/account-menu-process-deep-study-2026-09-02-001` (isolated worktree `ACCOUNT_MENU_PROCESS_DEEP_STUDY_2026_09_02_EXECUTION`) |
| Executor | Claude (this session), on behalf of Boss; Boss = Sole Final Approver |
| Mode | `READ ONLY / PROCESS BENCHMARK / CLEAN-ROOM / EVIDENCE-FIRST / MENU-BY-MENU / CHECKPOINT-CONTROLLED / L999.999` |
| Document status | `PROCESS REFERENCE ONLY` — not a Gate PASS, not a Final Solution, not development/production authorization, not an approved SMEsPlus UI/schema/workflow |
| Clean-room rule | Open ERP / Odoo and the iTEST02 dump are used only as `PROCESS BENCHMARK / MENU COVERAGE CHECKLIST / BUSINESS CAPABILITY REFERENCE / RISK DISCOVERY SOURCE`. No source code, ORM, schema, workflow-as-architecture, or menu name is adopted as final SMEsPlus design. Thai names below are **candidates only**. |
| Purpose of this file | Evidence appendix: the accounting menu tree actually installed in the benchmark instance dump `iTEST02_2026-06-14_14-41-19.dump`, extracted read-only from the `ir_ui_menu` metadata table (menu labels and Thai translations only; no business rows, no partner/product/amount data). Used as the menu-coverage checklist source for file 02. |

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.` `Open ERP / Odoo = Process Benchmark Only.` `SMEsPlus = New Thai Business Process Design Candidate, not final solution.`

## A. Extraction method (auditable)

- Source: `ACCOUNT/01 ACCOUNT/SOURCE CODE/iTEST02_2026-06-14_14-41-19.dump` (PostgreSQL custom-format archive v1.16; external to the git repository; never committed).
- Tooling: local `pg_restore` 16 cannot read the archive; a temporary copy of the dump was mounted read-only into a `postgres:18` container solely to run `pg_restore -a -t ir_ui_menu`, `-t ir_module_module`, `-t ir_act_window` (data of three **metadata** tables) and `-s -t ir_ui_menu` (schema). No database server was started; no network access; the temporary copy was deleted immediately after extraction.
- Tables extracted are system metadata (menu labels, module install states, action names). **No business, partner, product, invoice, amount, credential or personal data was extracted**, consistent with Team A quarantine rule Q-11.
- Parsing: menu `name` (JSON with `en_US` and `th_TH` keys) walked from the two root applications labelled `Invoicing` (id 130) and `Accounting` (id 321). Result: 116 menu nodes (2 roots + 114 descendants). Model names attached to actions are omitted below (Class F technical detail; retained only in the session scratchpad, not committed).
- Thai labels shown are the benchmark's own translations **as installed** — they are evidence of benchmark UX, not SMEsPlus candidate names. Several are visibly wrong for Thai accounting use (e.g. `Fiscal Positions` -> `ฐานะทางการเงิน`, `Closing` -> `ปิด`, `Secure Entries` -> `การเข้าสู่ระบบที่ปลอดภัย`), which is itself evidence that benchmark labels must not be copied.

## B. Menu tree (depth-indented)

| # | Depth | Benchmark path | en_US label | th_TH label (benchmark, as installed) | Has action |
|---|---|---|---|---|---|
| 1 | 0 | Invoicing | Invoicing | ออกใบแจ้งหนี้ | N (folder) |
| 2 | 0 | Accounting | Accounting | ระบบบัญชี | N (folder) |
| 3 | 1 | Accounting / Dashboard | Dashboard | แดชบอร์ด | Y |
| 4 | 1 | Accounting / Customers | Customers | ลูกค้า | N (folder) |
| 5 | 2 | Accounting / Customers / Invoices | Invoices | การแจ้งหนี้ | Y |
| 6 | 2 | Accounting / Customers / Credit Notes | Credit Notes | ใบลดหนี้ | Y |
| 7 | 2 | Accounting / Customers / Payments | Payments | การชำระเงิน | Y |
| 8 | 2 | Accounting / Customers / Products | Products | สินค้า | Y |
| 9 | 2 | Accounting / Customers / Customers | Customers | ลูกค้า | Y |
| 10 | 1 | Accounting / Vendors | Vendors | ผู้จำหน่าย | N (folder) |
| 11 | 2 | Accounting / Vendors / Bills | Bills | ใบเรียกเก็บเงิน | Y |
| 12 | 2 | Accounting / Vendors / Refunds | Refunds | การคืนเงิน | Y |
| 13 | 2 | Accounting / Vendors / Payments | Payments | การชำระเงิน | Y |
| 14 | 2 | Accounting / Vendors / Employee Expenses | Employee Expenses | รายจ่ายพนักงาน | Y |
| 15 | 2 | Accounting / Vendors / WT Certificates | WT Certificates | (no Thai translation) | Y |
| 16 | 2 | Accounting / Vendors / Products | Products | สินค้า | Y |
| 17 | 2 | Accounting / Vendors / Vendors | Vendors | ผู้จำหน่าย | Y |
| 18 | 1 | Accounting / Accounting | Accounting | การบัญชี | N (folder) |
| 19 | 2 | Accounting / Accounting / Transactions | Transactions | ธุรกรรม | N (folder) |
| 20 | 3 | Accounting / Accounting / Transactions / Journal Entries | Journal Entries | รายการบันทึกสมุดรายวัน | Y |
| 21 | 3 | Accounting / Accounting / Transactions / Analytic Items | Analytic Items | รายการวิเคราะห์ | Y |
| 22 | 2 | Accounting / Accounting / Assets & Liabilities | Assets & Liabilities | (no Thai translation) | N (folder) |
| 23 | 3 | Accounting / Accounting / Assets & Liabilities / Assets | Assets | สินทรัพย์ | Y |
| 24 | 3 | Accounting / Accounting / Assets & Liabilities / Loans | Loans | สินเชื่อ | Y |
| 25 | 3 | Accounting / Accounting / Assets & Liabilities / Fleet | Fleet | ระบบขนส่ง | Y |
| 26 | 2 | Accounting / Accounting / Closing | Closing | ปิด | N (folder) |
| 27 | 3 | Accounting / Accounting / Closing / Reconcile | Reconcile | กระทบยอด | Y |
| 28 | 3 | Accounting / Accounting / Closing / Tax Returns | Tax Returns | (no Thai translation) | Y |
| 29 | 3 | Accounting / Accounting / Closing / Lock Dates… | Lock Dates… | (no Thai translation) | Y |
| 30 | 3 | Accounting / Accounting / Closing / Secure Entries | Secure Entries | การเข้าสู่ระบบที่ปลอดภัย | Y |
| 31 | 1 | Accounting / Review | Review | รีวิว | N (folder) |
| 32 | 2 | Accounting / Review / Control | Control | ควบคุม | N (folder) |
| 33 | 3 | Accounting / Review / Control / Journal Items | Journal Items | รายการบันทึก | Y |
| 34 | 3 | Accounting / Review / Control / Journal Audit | Journal Audit | การตรวจสอบสมุดรายวัน | Y |
| 35 | 2 | Accounting / Review / Audit | Audit | ตรวจสอบบัญชี | N (folder) |
| 36 | 3 | Accounting / Review / Audit / Working Files | Working Files | (no Thai translation) | Y |
| 37 | 2 | Accounting / Review / Inventory | Inventory | สินค้าคงคลัง | N (folder) |
| 38 | 3 | Accounting / Review / Inventory / Inventory Valuation | Inventory Valuation | การประเมินมูลค่าสินค้าคงคลัง | Y |
| 39 | 3 | Accounting / Review / Inventory / Depreciation Schedule | Depreciation Schedule | ตารางค่าเสื่อมราคา | Y |
| 40 | 3 | Accounting / Review / Inventory / Loans Analysis | Loans Analysis | การวิเคราะห์สินเชื่อ | Y |
| 41 | 2 | Accounting / Review / Regularization Entries | Regularization Entries | (no Thai translation) | N (folder) |
| 42 | 3 | Accounting / Review / Regularization Entries / Unrealized Currencies | Unrealized Currencies | (no Thai translation) | Y |
| 43 | 3 | Accounting / Review / Regularization Entries / Deferred Revenues | Deferred Revenues | (no Thai translation) | Y |
| 44 | 3 | Accounting / Review / Regularization Entries / Deferred Expenses | Deferred Expenses | (no Thai translation) | Y |
| 45 | 2 | Accounting / Review / Purchases | Purchases | (no Thai translation) | N (folder) |
| 46 | 3 | Accounting / Review / Purchases / Bill To Receive | Bill To Receive | (no Thai translation) | Y |
| 47 | 3 | Accounting / Review / Purchases / Billed Not Received | Billed Not Received | (no Thai translation) | Y |
| 48 | 2 | Accounting / Review / Sales | Sales | การขาย | N (folder) |
| 49 | 3 | Accounting / Review / Sales / Invoices To Be Issued | Invoices To Be Issued | (no Thai translation) | Y |
| 50 | 3 | Accounting / Review / Sales / Invoiced Not Delivered | Invoiced Not Delivered | (no Thai translation) | Y |
| 51 | 2 | Accounting / Review / Logs | Logs | บันทึก | N (folder) |
| 52 | 3 | Accounting / Review / Logs / Audit Trail | Audit Trail | เส้นทางการตรวจสอบ | Y |
| 53 | 1 | Accounting / Reporting | Reporting | การรายงาน | N (folder) |
| 54 | 2 | Accounting / Reporting / Statement Reports | Statement Reports | รายงานรายการเดินบัญชี | N (folder) |
| 55 | 3 | Accounting / Reporting / Statement Reports / Balance Sheet | Balance Sheet | งบดุล | Y |
| 56 | 3 | Accounting / Reporting / Statement Reports / Profit and Loss | Profit and Loss | กำไรขาดทุน | Y |
| 57 | 3 | Accounting / Reporting / Statement Reports / Cash Flow Statement | Cash Flow Statement | งบกระแสเงินสด | Y |
| 58 | 2 | Accounting / Reporting / Ledgers | Ledgers | (no Thai translation) | N (folder) |
| 59 | 3 | Accounting / Reporting / Ledgers / Trial Balance | Trial Balance | งบทดลอง | Y |
| 60 | 3 | Accounting / Reporting / Ledgers / General Ledger | General Ledger | บัญชีแยกประเภททั่วไป | Y |
| 61 | 2 | Accounting / Reporting / Partner Reports | Partner Reports | รายงานพาร์ทเนอร์ | N (folder) |
| 62 | 3 | Accounting / Reporting / Partner Reports / Partner Ledger | Partner Ledger | สมุดบัญชีแยกประเภทคู่ค้า | Y |
| 63 | 3 | Accounting / Reporting / Partner Reports / Aged Receivable | Aged Receivable | อายุบัญชีลูกหนี้ | Y |
| 64 | 3 | Accounting / Reporting / Partner Reports / Aged Payable | Aged Payable | อายุบัญชีเจ้าหนี้ | Y |
| 65 | 2 | Accounting / Reporting / Taxes & Fiscal | Taxes & Fiscal | (no Thai translation) | N (folder) |
| 66 | 3 | Accounting / Reporting / Taxes & Fiscal / Tax Report | Tax Report | รายงานภาษี | Y |
| 67 | 3 | Accounting / Reporting / Taxes & Fiscal / EC Sales List | EC Sales List | รายการขาย EC | Y |
| 68 | 3 | Accounting / Reporting / Taxes & Fiscal / Intrastat | Intrastat | อินทราสแทต | Y |
| 69 | 3 | Accounting / Reporting / Taxes & Fiscal / Fiscal Report | Fiscal Report | (no Thai translation) | Y |
| 70 | 2 | Accounting / Reporting / Management | Management | การจัดการ | N (folder) |
| 71 | 3 | Accounting / Reporting / Management / Invoice Analysis | Invoice Analysis | การวิเคราะห์ใบแจ้งหนี้ | Y |
| 72 | 3 | Accounting / Reporting / Management / Analytic Report | Analytic Report | รายงานวิเคราะห์ | Y |
| 73 | 3 | Accounting / Reporting / Management / Executive Summary | Executive Summary | ข้อมูลสรุป | Y |
| 74 | 2 | Accounting / Reporting / WT Income Tax Report | WT Income Tax Report | (no Thai translation) | Y |
| 75 | 1 | Accounting / Configuration | Configuration | การกำหนดค่า | N (folder) |
| 76 | 2 | Accounting / Configuration / Settings | Settings | การตั้งค่า | Y |
| 77 | 2 | Accounting / Configuration / Cheque Format | Cheque Format | (no Thai translation) | Y |
| 78 | 2 | Accounting / Configuration / Accounting | Accounting | การบัญชี | N (folder) |
| 79 | 3 | Accounting / Configuration / Accounting / Chart of Accounts | Chart of Accounts | ผังบัญชี | Y |
| 80 | 3 | Accounting / Configuration / Accounting / Taxes | Taxes | ภาษี | Y |
| 81 | 3 | Accounting / Configuration / Accounting / Journals | Journals | สมุดรายวัน | Y |
| 82 | 3 | Accounting / Configuration / Accounting / Reporting | Reporting | การรายงาน | N (folder) |
| 83 | 3 | Accounting / Configuration / Accounting / Currencies | Currencies | สกุลเงิน | Y |
| 84 | 3 | Accounting / Configuration / Accounting / Fiscal Positions | Fiscal Positions | ฐานะทางการเงิน | Y |
| 85 | 3 | Accounting / Configuration / Accounting / Multi-Ledger | Multi-Ledger | บัญชีแยกประเภทหลายบัญชี | Y |
| 86 | 3 | Accounting / Configuration / Accounting / Tax Groups | Tax Groups | กลุ่มภาษี | Y |
| 87 | 3 | Accounting / Configuration / Accounting / Tax Units | Tax Units | หน่วยภาษี | Y |
| 88 | 3 | Accounting / Configuration / Accounting / Cash Roundings | Cash Roundings | การปัดเศษเงินสด | Y |
| 89 | 3 | Accounting / Configuration / Accounting / Account Tags | Account Tags | แท็กบัญชี | Y |
| 90 | 3 | Accounting / Configuration / Accounting / Account Groups | Account Groups | กลุ่มบัญชี | Y |
| 91 | 3 | Accounting / Configuration / Accounting / Fiscal Years | Fiscal Years | ปีงบประมาณ | Y |
| 92 | 3 | Accounting / Configuration / Accounting / Accounting Reports | Accounting Reports | รายงานทางบัญชี | Y |
| 93 | 3 | Accounting / Configuration / Accounting / Horizontal Groups | Horizontal Groups | กลุ่มแนวนอน: | Y |
| 94 | 3 | Accounting / Configuration / Accounting / Checks | Checks | ตรวจสอบ | Y |
| 95 | 3 | Accounting / Configuration / Accounting / Fiscal Categories | Fiscal Categories | (no Thai translation) | Y |
| 96 | 3 | Accounting / Configuration / Accounting / Asset Models | Asset Models | โมเดลสินทรัพย์ | Y |
| 97 | 3 | Accounting / Configuration / Accounting / Return Types | Return Types | (no Thai translation) | Y |
| 98 | 3 | Accounting / Configuration / Accounting / Financial Budgets | Financial Budgets | งบประมาณทางการเงิน | Y |
| 99 | 3 | Accounting / Configuration / Accounting / Online Synchronization | Online Synchronization | การซิงโครไนซ์ออนไลน์ | Y |
| 100 | 2 | Accounting / Configuration / Invoicing | Invoicing | ออกใบแจ้งหนี้ | N (folder) |
| 101 | 3 | Accounting / Configuration / Invoicing / Payment Terms | Payment Terms | เงื่อนไขการชําระเงิน | Y |
| 102 | 3 | Accounting / Configuration / Invoicing / Follow-up Levels | Follow-up Levels | ระดับการติดตามผล | Y |
| 103 | 3 | Accounting / Configuration / Invoicing / Incoterms | Incoterms | Incoterms | Y |
| 104 | 3 | Accounting / Configuration / Invoicing / Product Categories | Product Categories | หมวดหมู่สินค้า | Y |
| 105 | 3 | Accounting / Configuration / Invoicing / Withholding Tax | Withholding Tax | (no Thai translation) | Y |
| 106 | 3 | Accounting / Configuration / Invoicing / Intrastat Code | Intrastat Code | รหัสอินทราสแทต | Y |
| 107 | 2 | Accounting / Configuration / Assets and Revenues | Assets and Revenues | สินทรัพย์และรายได้ | N (folder) |
| 108 | 2 | Accounting / Configuration / Online Payments | Online Payments | การชำระเงินออนไลน์ | N (folder) |
| 109 | 3 | Accounting / Configuration / Online Payments / Payment Providers | Payment Providers | ผู้ให้บริการชำระเงิน | Y |
| 110 | 3 | Accounting / Configuration / Online Payments / Payment Methods | Payment Methods | วิธีการชำระเงิน | Y |
| 111 | 3 | Accounting / Configuration / Online Payments / Payment Tokens | Payment Tokens | โทเค็นการชำระเงิน | Y |
| 112 | 3 | Accounting / Configuration / Online Payments / Payment Transactions | Payment Transactions | ธุรกรรมการชำระเงิน | Y |
| 113 | 2 | Accounting / Configuration / Analytic Accounting | Analytic Accounting | บัญชีวิเคราะห์ | N (folder) |
| 114 | 3 | Accounting / Configuration / Analytic Accounting / Analytic Distribution Models | Analytic Distribution Models | โมเดลการกระจายการวิเคราะห์ | Y |
| 115 | 3 | Accounting / Configuration / Analytic Accounting / Analytic Accounts | Analytic Accounts | บัญชีวิเคราะห์ | Y |
| 116 | 3 | Accounting / Configuration / Analytic Accounting / Analytic Plans | Analytic Plans | แผนการวิเคราะห์ | Y |

## C. Observations for file 02 (facts, not conclusions)

1. Root applications: `Invoicing` (community `account`) and `Accounting` (enterprise `accountant`) both exist; the `Accounting` root carries the full tree.
2. Present in tree and in Boss Section 6 list: Chart of Accounts, Account Groups, Account Tags, Taxes, Tax Groups, Tax Units, Fiscal Years, Fiscal Positions, Currencies, Journals, Multi-Ledger (= Journal Groups), Horizontal Groups, Accounting Reports, Payment Terms, Follow-up Levels, Incoterms, Withholding Tax, Cheque Format, Journal Entries, Journal Items, Journal Audit (= Journal Report), Assets, Asset Models, Deferred Revenues, Deferred Expenses, Analytic Items/Accounts/Plans/Distribution Models, General Ledger, Trial Balance, Balance Sheet, Profit and Loss, Cash Flow Statement, Executive Summary, Tax Report, WT Income Tax Report, EC Sales List, Invoice Analysis, Unrealized Currencies, Lock Dates, Audit Trail, Depreciation Schedule, Partner Ledger, Aged Receivable, Aged Payable, Online Synchronization.
3. **Listed by Boss but NOT present in this instance's tree:** Sources; Reconciliation Models; Add a Bank Account (dashboard action, not a menu); Bank transactions (journal dashboard, not a menu); Debit Note (`account_debit_note` not installed); Receipt (no separate menu; customer payments + PromptPay report); Deferred Revenue Models; Deferred Expense Models; Budgets / Budgetary Positions / Budget Analysis (`account_budget` not installed; `Financial Budgets` under Configuration exists instead).
4. Present in tree but NOT in Boss list (benchmark-version extras): Loans, Fleet, Tax Returns, Secure Entries, Working Files (Audit), Loans Analysis, Bill To Receive / Billed Not Received, Invoices To Be Issued / Invoiced Not Delivered, Intrastat, Fiscal Report, Cash Roundings, Checks (return check templates), Fiscal Categories, Return Types, Financial Budgets, Intrastat Code, Online Payments (providers/methods/tokens/transactions), Employee Expenses, WT Certificates, Assets and Revenues (empty folder).
5. `WT Certificates` and `Withholding Tax` and `WT Income Tax Report` have **no Thai translation** in the instance although they are the Thailand-specific menus — a UX-fitness finding for TBRAC.
