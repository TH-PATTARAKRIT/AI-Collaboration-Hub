# SMEsPlus Data Model Overview

## 🗄️ Database Design Philosophy

SMEsPlus uses a relational database model optimized for:
- Transactional consistency
- Real-time reporting
- Data integrity
- Scalability
- Security

---

## 📊 Core Entity Categories

### **Master Data Tables**
- Companies
- Branches
- Departments
- Employees
- Customers
- Vendors
- Products
- Chart of Accounts

### **Transactional Tables**
- Sales Orders
- Purchase Orders
- Inventory Movements
- GL Entries
- Leave Requests
- Work Orders
- Invoices
- Receipts

### **Supporting Tables**
- Users
- Roles
- Permissions
- Configurations
- Audit Logs
- Workflows
- Document Versions
- Attachments

---

## 🏢 Company Structure Entities

```
Company (tenant)
├── Branches
├── Departments
├── Cost Centers
└── GL Segments
```

### **Company Table**
- CompanyID (PK)
- CompanyName
- RegistrationNumber
- Address
- Phone
- Email
- TaxID
- Status
- CreatedDate

### **Branch Table**
- BranchID (PK)
- CompanyID (FK)
- BranchName
- Address
- Manager
- Status

---

## 👥 People Management Entities

### **Employee Table**
- EmployeeID (PK)
- CompanyID (FK)
- FirstName
- LastName
- Email
- Phone
- Department (FK)
- Position
- StartDate
- Status

### **User Table**
- UserID (PK)
- EmployeeID (FK)
- Username
- Email
- HashedPassword
- Role
- LastLogin
- Status

---

## 🛍️ Sales Order Data Model

```
SalesOrder
├── SalesOrderItem (1:N)
├── Shipment (1:N)
├── SalesInvoice (1:1)
└── Approval (1:N)
```

### **SalesOrder Table**
- OrderID (PK)
- CustomerID (FK)
- OrderDate
- DueDate
- TotalAmount
- Status
- ApprovedBy
- ApprovedDate

### **SalesOrderItem Table**
- ItemID (PK)
- OrderID (FK)
- ProductID (FK)
- Quantity
- UnitPrice
- Total
- TaxAmount

---

## 🛒 Purchase Order Data Model

```
PurchaseOrder
├── PurchaseOrderItem (1:N)
├── GoodsReceipt (1:N)
├── VendorInvoice (1:1)
└── Approval (1:N)
```

### **PurchaseOrder Table**
- POID (PK)
- VendorID (FK)
- PODate
- DueDate
- TotalAmount
- Status
- ApprovedBy

### **PurchaseOrderItem Table**
- ItemID (PK)
- POID (FK)
- ProductID (FK)
- Quantity
- UnitPrice
- Total

---

## 📦 Inventory Data Model

### **Product Table**
- ProductID (PK)
- ProductCode
- ProductName
- Category
- UnitOfMeasure
- StandardCost
- Status

### **Stock Table**
- StockID (PK)
- ProductID (FK)
- WarehouseID (FK)
- OnHandQty
- SafetyStock
- ReorderPoint
- LastCountDate

### **StockMovement Table**
- MovementID (PK)
- ProductID (FK)
- WarehouseID (FK)
- MovementType (In/Out/Transfer)
- Quantity
- ReferenceDocument
- MovementDate
- CreatedBy

---

## 💰 Accounting Data Model

### **ChartOfAccounts Table**
- AccountID (PK)
- AccountCode
- AccountName
- AccountType (Asset/Liability/Equity/Revenue/Expense)
- Status
- Balance

### **GLEntry Table**
- EntryID (PK)
- CompanyID (FK)
- JournalID (FK)
- AccountID (FK)
- LineNumber
- DebitAmount
- CreditAmount
- Description
- EntryDate
- PostedDate

### **Invoice Table**
- InvoiceID (PK)
- CustomerID (FK)
- InvoiceDate
- DueDate
- Amount
- TaxAmount
- Status
- PaidDate

---

## 👔 HR/Payroll Data Model

### **Attendance Table**
- AttendanceID (PK)
- EmployeeID (FK)
- AttendanceDate
- CheckInTime
- CheckOutTime
- Status (Present/Absent/Leave)

### **Leave Table**
- LeaveID (PK)
- EmployeeID (FK)
- LeaveType
- StartDate
- EndDate
- Days
- Status
- ApprovedBy
- ApprovedDate

### **Payroll Table**
- PayrollID (PK)
- EmployeeID (FK)
- PayrollDate
- BaseSalary
- Allowances
- Deductions
- NetSalary
- Status

---

## 📋 Document & Approval Data Model

### **Document Table**
- DocumentID (PK)
- DocumentType
- DocumentName
- CreatedBy
- CreatedDate
- Status
- FileSize
- FileLocation

### **ApprovalWorkflow Table**
- WorkflowID (PK)
- DocumentID (FK)
- ApprovalStep
- ApproverID (FK)
- Status (Pending/Approved/Rejected)
- Comments
- SubmittedDate
- ApprovedDate

---

## 🔐 Security & Audit

### **AuditLog Table**
- AuditID (PK)
- UserID (FK)
- Action
- TableName
- RecordID
- OldValue
- NewValue
- Timestamp
- IPAddress

### **Permission Table**
- PermissionID (PK)
- RoleID (FK)
- Module
- Operation (Create/Read/Update/Delete)
- DataLevel (Company/Branch/Department/Personal)

---

## 📊 Relationships Summary

```
CompanyID (Parent Key used in most tables)
├── Employee → User
├── Customers
├── Vendors
├── Products → Stock → StockMovement
├── SalesOrder → SalesOrderItem → Shipment → Invoice
├── PurchaseOrder → PurchaseOrderItem → GoodsReceipt → VendorInvoice
├── GLEntry → ChartOfAccounts
├── Leave, Attendance → Employee
└── ApprovalWorkflow → Document
```

---

## 🎯 Data Governance

### **Data Quality**
- Data validation rules
- Referential integrity constraints
- Check constraints
- Unique constraints

### **Data Security**
- Encryption at rest
- Row-level security (RLS)
- Column masking for sensitive data
- Audit logging for all changes

### **Data Retention**
- Transaction data: 7 years
- Audit logs: 5 years
- Temporary data: 90 days
- Archived data: 10 years

---

## 📈 Performance Optimization

### **Indexing Strategy**
- Primary key indexes
- Foreign key indexes
- Search column indexes (Name, Code)
- Composite indexes for joins

### **Query Optimization**
- Views for common reports
- Materialized views for dashboards
- Query hints for complex queries
- Partitioning for large tables

### **Backup Strategy**
- Full backup: Daily
- Incremental backup: Hourly
- Transaction log backup: Every 15 minutes
- Retention: 30 days

---

## 🔄 Integration with Other Systems

### **Data Exchange Formats**
- JSON for APIs
- CSV for bulk import/export
- XML for external integrations

### **Data Synchronization**
- Event-driven updates
- Scheduled batch processes
- Real-time API calls
- Message queue integration

---

## 📊 Reporting Tables

### **Summary Tables** (Materialized views)
- Daily_Sales_Summary
- Monthly_Revenue_Summary
- Inventory_Summary
- Payroll_Summary

### **Dimension Tables** (for OLAP)
- DimDate
- DimProduct
- DimCustomer
- DimVendor
- DimEmployee

---

**Status**: ✅ Active  
**Version**: 1.0  
**Last Updated**: 2026-07-02  
**Database**: PostgreSQL / SQL Server
