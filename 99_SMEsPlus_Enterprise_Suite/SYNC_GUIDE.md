# Google Drive ↔ GitHub Sync Guide

**Purpose:** Coordinate documentation between Google Drive (primary content) and GitHub (registry/config)

**Created:** 2026-07-01  
**Status:** Active

---

## 📍 Repository Structure

### Google Drive (Primary Content Repository)
**Location:** https://drive.google.com/drive/folders/1qKb44UCgM4HBuA16rE4DZja2atSH1Y3P

**Stores:**
- ✅ Functional Specifications
- ✅ Architecture Decisions
- ✅ UX/UI Designs
- ✅ Test Plans & Results
- ✅ All working documents
- ✅ Collaborative content
- ✅ Evidence Records

**Why:** Easy to share, comment, edit collaboratively

### GitHub (Configuration & Registry)
**Location:** https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub  
**Branch:** SMEsPlus  
**Access:** Public (all AI roles can clone)

**Stores:**
- ✅ SMEPLUS_REGISTRY.yaml (folder & document registry)
- ✅ Bootstrap documents
- ✅ README files (folder guides)
- ✅ Configuration files
- ✅ Sync documentation
- ✅ AI role definitions

**Why:** Central source of truth for structure and process

---

## 🔄 Sync Workflow

### For Creating New Work

1. **Plan in Google Drive**
   - Create new folder if needed
   - Follow naming conventions
   - Add README

2. **Register in GitHub**
   - Update SMEPLUS_REGISTRY.yaml
   - Add folder to repository structure
   - Create folder in 99_SMEsPlus_Enterprise_Suite/

3. **Create Evidence Record**
   - Use EVIDENCE_RECORD_TEMPLATE.md (in Google Drive)
   - Link to both locations
   - Track status in Evidence Record

4. **Share with AI Roles**
   - Announcement in Google Drive (where content is)
   - Reference GitHub for structure (where to navigate)

### For Handoff to Next AI Role

1. **Document in Google Drive**
   - Prepare complete package
   - Create handoff summary
   - Collect evidence records

2. **Update Registry in GitHub**
   - Mark handoff in SMEPLUS_REGISTRY.yaml
   - Add new entry to next folder
   - Commit handoff record

3. **Create GitHub Issue (Optional)**
   - Link to Google Drive document
   - Specify receiving AI role
   - Set status and timeline

4. **Verify Receipt**
   - Get confirmation from receiving AI role
   - Update Evidence Record
   - Mark handoff complete

---

## 📋 What Goes Where

| Item | Storage | Sync |
|------|---------|------|
| Functional Specifications | Google Drive 02_Functional_Design | Link in GitHub README |
| Architecture Decisions | Google Drive 03_Architecture_Decisions | Link in GitHub README |
| UX/UI Designs | Google Drive 02_Functional_Design | Reference in GitHub |
| Test Plans | Google Drive 08_Testing_Evidence | Link in GitHub README |
| Evidence Records | Both (cross-referenced) | Update GitHub registry |
| Registry Files | GitHub (primary) | Refer from Google Drive |
| Folder Structure | GitHub (primary) | Mirror in Google Drive |
| Templates | GitHub for reference | Working copies in Google Drive |
| Prompts | Google Drive 05_Prompts | Index in GitHub |

---

## 🔍 File Naming Conventions

### Google Drive Files
```
[PROJECT_CODE]_[DOCUMENT_TYPE]_[DESCRIPTION]_v[VERSION]

Examples:
SMEPLUS_FUNCSPEC_UserManagement_v1.0
SMEPLUS_ADR_DatabaseStrategy_v1.0
SMEPLUS_TESTPLAN_PaymentFlow_v1.0
```

### GitHub Files
```
00_FOLDER/
└── DOCUMENT_TYPE_description_v1.0.md

Examples:
02_Functional_Design/
└── FUNCTIONAL_SPECIFICATION_v1.0.md
```

---

## 🔐 Access Control

### Google Drive
- **Shared with:** All team members
- **Edit permissions:** Document owner + reviewers
- **View permissions:** All team members
- **Share:** Can share files or folders

### GitHub
- **Repository:** Public (anyone can clone)
- **Branch:** SMEsPlus
- **Push rights:** Collaborators only
- **Workflow:** Fork → Branch → Pull Request → Merge

---

## 📊 Status Tracking

### In Google Drive Evidence Record
```
Document Status:
- [ ] Draft (being created)
- [ ] Submitted for Review
- [ ] Under PMO Review
- [ ] Under Technical Review
- [ ] Ready for Boss Approval
- [ ] Approved
- [ ] In Use
- [ ] Archived
```

### In GitHub SMEPLUS_REGISTRY.yaml
```yaml
documents:
  DOCUMENT_ID:
    title: Document Title
    location_google_drive: URL
    location_github: Path/to/reference
    status: approved | pending | archived
    owner: AI Role
    last_updated: 2026-07-01
```

---

## 🚀 Regular Sync Tasks

### Daily
- [ ] Check Google Drive for new deliverables
- [ ] Update Evidence Records with current status
- [ ] Note any blockers or delays

### Weekly
- [ ] Review Evidence Records for new handoffs
- [ ] Update GitHub registry with any changes
- [ ] Commit registry updates
- [ ] Send status summary to team

### Bi-Weekly
- [ ] Review overall project progress
- [ ] Update README files
- [ ] Verify all links still valid
- [ ] Archive old/completed documents

### Monthly
- [ ] Full registry audit
- [ ] Review folder structure effectiveness
- [ ] Update timelines and targets
- [ ] Generate metrics report

---

## 🔗 How to Link Between Repositories

### From Google Drive to GitHub
```
GitHub Reference:
https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/tree/SMEsPlus/99_SMEsPlus_Enterprise_Suite/02_Functional_Design

Include in Google Drive Evidence Record:
"See registry reference: [link above]"
```

### From GitHub to Google Drive
```
In SMEPLUS_REGISTRY.yaml:
location_google_drive: https://drive.google.com/drive/folders/[FOLDER_ID]

In README.md:
[See detailed specification in Google Drive](link)
```

---

## 🔄 Handoff Example

### Step 1: Specialist AI Completes Work (Google Drive)
- Create document in Google Drive
- Complete Evidence Record template
- Get signatures from reviewers
- Mark status: "Ready for Handoff"

### Step 2: Update GitHub Registry
```yaml
functional_design:
  functional_specification:
    status: approved
    version: 1.0
    location_google_drive: [URL]
    handoff_to: Figma UX UI AI
    handoff_date: 2026-07-05
```

### Step 3: Commit to GitHub
```bash
git add 99_SMEsPlus_Enterprise_Suite/SMEPLUS_REGISTRY.yaml
git commit -m "Update registry: Functional Spec v1.0 approved for UX handoff"
git push origin SMEsPlus
```

### Step 4: Create GitHub Issue (Optional)
- Title: "Handoff: Functional Spec v1.0 → Figma UX UI AI"
- Assign to: Figma UX UI AI
- Link: Google Drive document
- Status: Ready for handoff

### Step 5: Verify Handoff
- Receiving AI confirms receipt
- Update Evidence Record: "Handoff complete"
- Close GitHub issue
- Move to next phase

---

## ✅ Checklist for Each Handoff

**Before GitHub Commit:**
- [ ] Document complete in Google Drive
- [ ] Evidence Record filled
- [ ] All reviews documented
- [ ] Boss approval obtained
- [ ] Receiving AI identified
- [ ] Links verified

**GitHub Registry Update:**
- [ ] SMEPLUS_REGISTRY.yaml updated
- [ ] Folder references correct
- [ ] Dates recorded
- [ ] Status field updated
- [ ] Handoff_to field set
- [ ] Commit message clear

**GitHub Commit:**
- [ ] Message references document ID
- [ ] Message references version
- [ ] Commit pushed to SMEsPlus
- [ ] No sensitive data in commit

**Verification:**
- [ ] Receiving AI can access Google Drive
- [ ] Receiving AI can access GitHub
- [ ] Registry entry visible
- [ ] Links all work
- [ ] README guides clear

---

## 🚨 Important Rules

### Never
- ❌ Store sensitive data in GitHub (public repository)
- ❌ Commit Evidence Records (they stay in Google Drive)
- ❌ Use GitHub as primary content store
- ❌ Skip Google Drive for collaborative editing
- ❌ Forget to update registry when adding documents

### Always
- ✅ Use Google Drive for content creation
- ✅ Use GitHub for structure/registry
- ✅ Link between them
- ✅ Update registry when status changes
- ✅ Document everything

---

## 📞 Support

**Questions about:**
- **Google Drive structure** → See folder README.md
- **GitHub structure** → See SMEPLUS_REGISTRY.yaml
- **Sync process** → See this guide
- **Specific document** → Check Evidence Record

---

## 🔄 Sync Checklist Template

```
Date: [2026-07-01]
Sync Type: [Daily/Weekly/Monthly]

Google Drive Status:
- [ ] New documents added: [list]
- [ ] Evidence Records updated: [count]
- [ ] Blockers identified: [list]

GitHub Status:
- [ ] Registry updated: [Yes/No]
- [ ] Commits made: [count]
- [ ] Issues created: [list]
- [ ] Pull Requests: [status]

Cross-Check:
- [ ] Links verified: [Yes/No]
- [ ] Statuses aligned: [Yes/No]
- [ ] No conflicts: [Yes/No]

Notes:
[Any issues or observations]
```

---

**Last Updated:** 2026-07-01  
**Maintained By:** SMEsPlus AI Orchestrator  
**Review Frequency:** Weekly
