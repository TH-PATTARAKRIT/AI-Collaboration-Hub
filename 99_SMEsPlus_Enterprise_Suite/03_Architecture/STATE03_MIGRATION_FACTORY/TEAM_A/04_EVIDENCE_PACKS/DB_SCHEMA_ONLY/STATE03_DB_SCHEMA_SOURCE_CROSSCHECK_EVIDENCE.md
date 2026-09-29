> **STATUS CORRECTION — The source/schema finding is CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION. It is not runtime proof, Gate PASS, final gap closure, or STATE03 completion. Refer to STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF for the current qualified disposition.**

> **SCHEMA-ONLY — ไม่มีข้อมูลจริง (no row data)** | ส่วนที่ 2 — Evidence (data-minimized) | คู่กับ: `STATE03_DB_SCHEMA_SOURCE_CROSSCHECK_BUSINESS_SUMMARY.md`

# STATE03 DB Schema — Evidence (data-minimized restricted pointer)

## 0. REMEDIATION NOTE (สำคัญ)
เวอร์ชันก่อนหน้าของไฟล์นี้ (และไฟล์สรุปคู่กัน) ซึ่งอยู่ใน **git history ของ branch นี้** มีรายละเอียดโครงสร้างฐานข้อมูลเกินกติกา (รายชื่อตารางนอก Community, ข้อความนิยาม constraint, ตัวอย่างคำสั่ง query และคำอธิบายตาราง/คอลัมน์ระดับ implementation). รายละเอียดเหล่านั้น **ถูกลบออกจาก working tree ปัจจุบัน** ในการแก้ไขนี้ แต่ **ยังคงอยู่ในประวัติ Git** (ไม่ได้ลบ/เขียนประวัติใหม่ ไม่อ้างว่าลบล้างประวัติได้) และยังอยู่ภายใต้การทบทวน Clean-Room แบบอิสระ. ไฟล์นี้จึงเก็บเฉพาะ restricted pointer, hash, ผลด้านความสัมพันธ์/การตั้งค่า/การควบคุมแบบเป็นกลาง, ข้อจำกัด และ validation ที่ต้องทำ.

## 1. Restricted provenance pointer
| รายการ | ค่า |
|---|---|
| Artifact | `RESTRICTED-LOCAL:SMEsPlus19/iTEST02_2026-06-14_14-41-19 (1).dump` (ไม่ได้ commit) |
| sha256 | `d67fff6dbd3a957a5089e3bd7f982b1f8a98b954e8be2e40e6c227a70339d8c0` |
| Archive | สร้างจาก PostgreSQL 18.4, format custom v1.16, 2026-06-14 |
| Restore | schema-only เข้า cluster ชั่วคราวเฉพาะเครื่อง (localhost) ทำ 2 ครั้ง ; ตรวจเมตาดาต้าเท่านั้น ; ไม่มีการอ่านข้อมูลแถวของตารางธุรกิจ |
| Cleanup | ทั้งสองครั้งลบฐานชั่วคราว หยุด server และลบโฟลเดอร์ cluster แล้ว (ตรวจแล้ว) |

## 2. ผลแบบเป็นกลาง (Neutral findings) — ทั้งหมด `CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION`
| # | ผล | ระดับ | ข้อจำกัด |
|---|---|---|---|
| F1 | โครงสร้างฐานสอดคล้องกับสถาปัตยกรรมมูลค่าสต็อกที่พบใน source รุ่น 19 (มูลค่าเก็บที่ระดับรายการเคลื่อนไหว) — **ต้อง requalify ตาม Handoff §R** | `SCHEMA` | ผลจาก dump ฐานเดียวเมื่อ 2026-06-14 ; source เป็นรุ่นหลังกว่า |
| F2 | การควบคุมความถูกต้องระดับฐานข้อมูลสำหรับรายการบัญชีมีเฉพาะระดับบรรทัด ไม่พบในระดับหัวรายการ และไม่พบ trigger ที่ผู้ใช้สร้าง → การสมดุลและการล็อกงวดอยู่ที่ชั้นแอปพลิเคชัน | `SCHEMA` | ยังไม่ตรวจข้อมูลจริง ; ไม่ใช่ runtime |
| F3 | กฎของอัตราส่วนต้นทุนผลผลิตรองไม่มีตัวควบคุมที่ระดับฐานข้อมูล | `SCHEMA` | เช่นเดียวกัน |
| F4 | ค่าตั้งของหมวดสินค้าที่ขึ้นกับบริษัทถูกเก็บในรูปแบบภายในแถวเดียวกัน (ไม่ใช่ตารางแยก) | `SCHEMA` | ผลต่อการย้ายข้อมูลต้องยืนยันด้วย runtime |
| F5 | พบโครงสร้างที่ไม่อยู่ใน source Community จำนวนมาก (ประมาณ 700 ตาราง จากการจับคู่ชื่อโมเดลแบบประมาณ) ครอบคลุมพื้นที่การทำงาน: วางแผนผลิต/PLM, คุณภาพ, สินทรัพย์, บัญชีขั้นสูง, ภาษีหัก ณ ที่จ่าย, HR, เอกสาร, ลายเซ็น, Helpdesk, นัดหมาย ฯลฯ และโมเดลที่สร้างผ่านเครื่องมือปรับแต่ง | `SCHEMA` (ประมาณ) | ไม่ทราบที่มา/license ; **การไม่พบตาราง/คอลัมน์ ไม่พิสูจน์ว่าโมดูลไม่มีอยู่หรือไม่มีผลทางพฤติกรรม** |

## 3. Limitation และ Required validation
- dump ฐานเดียว (2026-06-14) เก่ากว่า source (`19.0.post20260921`) ; ผลไม่ใช่ตัวแทนของทุกฐาน
- ไม่มีข้อมูลแถว จึงตอบไม่ได้: ชุดโมดูลที่ติดตั้งจริง, ค่าตั้งค่า, ความละเอียดตัวเลข
- Required: Independent Clean-Room review ของประวัติ Git ; runtime/configuration validation ; ยืนยันที่มา/license ของโครงสร้างนอก Community ก่อนศึกษาเพิ่ม
