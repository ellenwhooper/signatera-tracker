# Signatera Tracker – MRD Compliance & Visualization Tool

## 🧬 Overview

This repository contains a complete, scalable solution for tracking Signatera draw compliance within oncology treatment plans. It is built to support:

- Flatiron EMR exports
- Signatera MRD draw schedules
- Compliance tracking for each patient (On-Time, Late, Missing)
- Integration with Power BI for timeline/scatter plots
- Future-ready support for MRD result decision support

---

## 📁 Folder Structure

```
signatera-tracker/
│
├── /docs/                          # Stakeholder and IT-facing guides
│   ├── Signatera_Tracker_Stakeholder_Deck.pdf
│   ├── PowerBI_Step_By_Step_Guide.pdf
│   ├── Setup_Guide_for_IT.pdf
│   └── Signatera_MRD_UseCase_Dashboard.pdf
│
├── /data/                          # Sample input files
│   ├── Signatera_Tracker_Input_FINAL.xlsx
│   └── Signatera_MRD_Tracker_Template.xlsx
│
├── /dashboard/                    # Power BI report
│   └── Signatera_Tracker.pbix
│
├── /etl/                          # ETL and transformation scripts
│   ├── etl_signatera.py
│   └── flatiron_to_tracker_template.csv
│
├── /automation/                   # Scripts for scheduling and GitHub Actions
│   ├── run_etl_task.bat
│   ├── github_push_script.bat
│   └── Signatera_Dashboard_Refresh.yaml
│
├── README.md
├── .gitignore
└── LICENSE
```

---

## ⚙️ How to Use

### 1. Run the ETL Script
```bash
python etl/etl_signatera.py
```

This will read your Excel file (e.g., `Signatera_Timeline_Expected_Actual_With_Cycles.xlsx`) and output a clean CSV ready for Power BI.

### 2. Open Power BI
Open the file `dashboard/Signatera_Tracker.pbix` and click **Refresh** to load the latest compliance and draw data.

---

## 🔒 Automation
- Windows Task Scheduler can run `run_etl_task.bat` on a schedule
- GitHub Actions are enabled via `Signatera_Dashboard_Refresh.yaml`

---

## 📬 Contact
Questions or feedback? Please contact:
**Ellen Hooper** – ehooper@natera.com