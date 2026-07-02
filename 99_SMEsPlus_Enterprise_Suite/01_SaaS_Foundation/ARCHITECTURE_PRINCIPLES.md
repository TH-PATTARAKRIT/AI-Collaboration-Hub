ARCHITECTURE_PRINCIPLES.md

Version: v1.0
Status: Approved Baseline
Owner: SMEsPlus Product & Architecture Team
Target Path: 01_SaaS_Foundation/ARCHITECTURE_PRINCIPLES.md

## 1. Purpose

เอกสารนี้กำหนดหลักการ (Architecture Principles) ที่ทุกทีมต้องยึดถือในการออกแบบ พัฒนา ทดสอบ และดูแลระบบ SMEsPlus Enterprise Suite

Architecture Principle ถือเป็นข้อกำหนดระดับบน (Architecture Constraints) ซึ่งมีผลกับทุกโมดูลของระบบ

## 2. Scope

ใช้กับทุกส่วนของโครงการ

- SaaS Foundation
- Accounting
- Sales
- Purchasing
- Inventory
- Manufacturing
- CRM
- HR
- AI
- Integration
- Reporting
- Mobile
- Public API

## 3. Architecture Principles

### AP-001 SaaS First

**Principle**
ทุกฟังก์ชันต้องออกแบบเป็น SaaS ก่อนเสมอ

**Rules**
- รองรับ Multi-Tenant
- Tenant Provisioning อัตโนมัติ
- Subscription Driven
- Module Activation
- Self-Service Administration

**Success Criteria**
Feature ใหม่สามารถเปิดใช้งานเฉพาะบาง Tenant ได้โดยไม่ต้อง Deploy ระบบใหม่

### AP-002 Multi-Tenant by Design

**Principle**
Tenant คือขอบเขตหลักของข้อมูล

**Rules**
- ทุกข้อมูลต้องมี Tenant Context
- Database ต้องบังคับ Tenant Isolation
- API ทุกตัวต้อง Resolve Tenant ก่อน Business Logic
- ห้าม Hardcode Tenant

**Success Criteria**
ไม่สามารถ Query ข้อมูลข้าม Tenant ได้

### AP-003 Security by Design

**Principle**
Security เป็นส่วนหนึ่งของการออกแบบ ไม่ใช่เพิ่มภายหลัง

**Rules**
- MFA Ready
- JWT Authentication
- RBAC + ABAC
- Database RLS
- Encryption in Transit
- Encryption at Rest

**Success Criteria**
ทุก Endpoint ผ่าน Security Review ก่อน Production

### AP-004 API First

**Principle**
API Contract คือแหล่งอ้างอิงหลักระหว่าง Frontend และ Backend

**Rules**
- ออกแบบ OpenAPI ก่อน Implementation
- Version ทุก API
- Response Format มาตรฐานเดียวกัน
- Error Code มาตรฐานเดียวกัน

**Success Criteria**
Frontend สามารถทำงานจาก Mock API ได้ก่อน Backend เสร็จ

### AP-005 Domain Driven Design

**Principle**
Business Domain เป็นตัวกำหนดโครงสร้างระบบ

**Rules**
- แยก Domain ชัดเจน
- หลีกเลี่ยง Shared Business Logic
- Service ต้องรับผิดชอบ Domain เดียว

**Success Criteria**
การเปลี่ยนแปลงใน Domain หนึ่งไม่กระทบ Domain อื่นโดยไม่จำเป็น

### AP-006 Modular Architecture

**Principle**
ทุกโมดูลสามารถเปิดหรือปิดได้ผ่าน Configuration

**Rules**
- Loose Coupling
- High Cohesion
- Module Activation
- Dependency Validation

**Success Criteria**
Tenant สามารถเปิดใช้เฉพาะ Module ที่ซื้อได้

### AP-007 Configuration over Customization

**Principle**
หลีกเลี่ยงการ Fork Source Code

**Rules**
- ใช้ Configuration
- ใช้ Feature Flags
- ใช้ Tenant Settings

**Success Criteria**
Tenant แต่ละรายสามารถกำหนดค่าต่างกันได้โดยไม่ต้องแก้โค้ด

### AP-008 Audit by Design

**Principle**
ทุก Critical Action ต้องตรวจสอบย้อนหลังได้

**Rules**
Audit ต้องบันทึก
- Actor
- Tenant
- Action
- Resource
- Timestamp
- Request ID

**Success Criteria**
Audit Log ต้อง Immutable

### AP-009 Cloud Native

**Principle**
ระบบต้องออกแบบเพื่อรันบน Cloud

**Rules**
- Stateless Services
- Containerized
- Horizontal Scaling
- External Configuration

**Success Criteria**
สามารถเพิ่มจำนวน Instance ได้โดยไม่ต้องแก้โค้ด

### AP-010 Automation First

**Principle**
งานที่ทำซ้ำต้องสามารถ Automate ได้

**Rules**
- CI/CD
- Infrastructure as Code
- Automated Testing
- Automated Deployment

**Success Criteria**
Deployment Production ไม่ต้องทำ Manual Step ที่มีความเสี่ยง

### AP-011 Observability by Default

**Principle**
ทุก Service ต้องสามารถสังเกตและตรวจสอบได้

**Rules**
- Structured Logging
- Metrics
- Distributed Tracing
- Health Check
- Alerting

**Success Criteria**
สามารถวิเคราะห์ Incident จากข้อมูลที่ระบบสร้างได้

### AP-012 Performance by Design

**Principle**
Performance ต้องถูกออกแบบตั้งแต่ต้น

**Rules**
- Database Index
- Pagination
- Caching
- Async Processing
- Queue

**Success Criteria**
Performance Target ต้องกำหนดใน SDS และทดสอบก่อน Release

## 4. Principle Priority

กรณีเกิดความขัดแย้ง ให้ใช้ลำดับดังนี้

1. Security
2. Tenant Isolation
3. Data Integrity
4. Compliance
5. Availability
6. Performance
7. Maintainability
8. Extensibility
9. Cost Optimization

## 5. Architecture Review Checklist

ทุก Architecture Review ต้องตอบคำถามต่อไปนี้

- รองรับ Multi-Tenant หรือไม่
- ผ่าน Security Principle หรือไม่
- Audit ได้หรือไม่
- API เป็นมาตรฐานหรือไม่
- Database รองรับ RLS หรือไม่
- Module แยกอิสระหรือไม่
- Configurable หรือไม่
- Scale ได้หรือไม่
- Test ได้หรือไม่
- Monitoring ได้หรือไม่

หากข้อใดตอบ "ไม่" ต้องระบุเหตุผลและมี Architecture Decision Record (ADR) รองรับ

## 6. Compliance

เอกสารที่ต้องสอดคล้องกับ Principle นี้

- FDS
- SDS
- ADR
- API
- Database
- Security
- UI
- QA
- DevOps
- Deployment

## 7. Related Documents

- README.md
- DOCUMENT_MAP.md
- ARCHITECTURE_GOVERNANCE.md
- ARCHITECTURE_DECISION_LOG.md
- ADR/*
- SECURITY/SECURITY_ARCHITECTURE.md

## 8. Revision Rule

Architecture Principle เปลี่ยนแปลงได้เฉพาะเมื่อ

- Architecture Review Board อนุมัติ
- มี ADR รองรับ
- Traceability Matrix ได้รับการอัปเดต
- Change Log ได้รับการบันทึก
