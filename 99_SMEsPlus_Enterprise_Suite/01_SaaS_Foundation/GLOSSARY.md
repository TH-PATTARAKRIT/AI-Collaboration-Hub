GLOSSARY.md

Version: v1.0
Status: Approved Baseline
Owner: SMEsPlus Product & Architecture Team
Target Path: 01_SaaS_Foundation/GLOSSARY.md

## Purpose

เอกสารนี้กำหนดคำศัพท์กลางของ SMEsPlus SaaS Foundation เพื่อให้ Product, UX, Development, QA, DevOps และ Security เข้าใจตรงกัน

## Core Terms

| Term | Definition |
|---|---|
| SaaS | Software as a Service ระบบซอฟต์แวร์ที่ให้บริการผ่าน cloud และรองรับผู้ใช้หลายองค์กร |
| Platform | ชั้นระบบกลางที่บริหาร tenant, plan, module, security และ governance |
| Tenant | ลูกค้าหรือองค์กรหลักที่ใช้งานระบบ SMEsPlus |
| Company | นิติบุคคลหรือบริษัทภายใต้ tenant |
| Branch | สาขาภายใต้ company |
| Division | หน่วยงานหรือแผนกภายใน company หรือ branch |
| User | ผู้ใช้งานระบบ |
| Role | กลุ่มสิทธิ์ที่กำหนดให้ user |
| Permission | สิทธิ์ย่อยที่อนุญาตให้ทำ action เฉพาะ |
| Policy | เงื่อนไขการอนุญาตใช้งาน เช่น scope, branch, company หรือ module |
| Scope | ขอบเขตการเข้าถึงข้อมูล เช่น tenant, company, branch, division |
| Module | ชุดความสามารถทางธุรกิจ เช่น Accounting, Sales, Inventory, HR, CRM |
| Plan | แพ็กเกจการใช้งานที่กำหนดราคาและ module ที่ใช้ได้ |
| Subscription | สถานะการสมัครใช้งานของ tenant |
| Module Activation | การเปิดใช้งาน module ให้ tenant |
| API Client | แอปหรือระบบภายนอกที่เชื่อมต่อผ่าน API |
| Webhook | กลไกส่ง event จาก SMEsPlus ไปยังระบบภายนอก |
| Event | เหตุการณ์ในระบบ เช่น user.created, module.activated |
| Audit Log | บันทึกการกระทำสำคัญในระบบแบบตรวจสอบย้อนหลังได้ |
| Approval Workflow | กระบวนการอนุมัติที่มีลำดับขั้น |
| Approval Request | รายการที่ถูกส่งเข้ากระบวนการอนุมัติ |
| Notification | ข้อความแจ้งเตือนผู้ใช้ |
| JWT Token | สำหรับยืนยันตัวตนและส่งข้อมูล identity/context |
| MFA | Multi-Factor Authentication |
| RBAC | Role-Based Access Control |
| ABAC | Attribute-Based Access Control |
| RLS | Row-Level Security ใน database |
| Tenant Isolation | การป้องกันไม่ให้ tenant หนึ่งเข้าถึงข้อมูลของ tenant อื่น |
| API Gateway | จุดรับ request หลักก่อนส่งต่อไป service |
| Service | หน่วย logic ที่รับผิดชอบ business capability เฉพาะ |
| Repository | ชั้นเข้าถึง database |
| DTO | Data Transfer Object |
| UAT | User Acceptance Test |
| DR | Disaster Recovery |
| RTO | ระยะเวลาสูงสุดที่ระบบควรกู้คืนได้ |
| RPO | ระยะข้อมูลสูญหายสูงสุดที่ยอมรับได้ |

## Hierarchy

```text
Platform
└── Tenant
    └── Company
        └── Branch
            └── Division
                └── User
```

## Access Control Meaning

| Concept | Meaning |
|---|---|
| Authentication | การยืนยันว่า user คือใคร |
| Authorization | การตรวจว่า user ทำสิ่งนั้นได้หรือไม่ |
| Role | กลุ่มสิทธิ์ |
| Permission | สิทธิ์ระดับ action |
| Scope | ขอบเขตข้อมูลที่เข้าถึงได้ |
| Policy | กฎประกอบการตัดสินใจ |
| Tenant Context | tenant_id และ scope ที่ผูกกับ request |

## Document Usage Rule

คำศัพท์ในเอกสารทั้งหมดของ `01_SaaS_Foundation` ต้องอ้างอิงนิยามจากไฟล์นี้ หากมีคำใหม่ต้องเพิ่มใน `GLOSSARY.md` ก่อนนำไปใช้ใน FDS, SDS, API, Database, Security, UI หรือ QA
