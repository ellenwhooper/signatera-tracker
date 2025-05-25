
# Signatera Tracker for Clinical Compliance

This project is a Power BI-driven reporting solution designed to track Signatera testing adherence using EMR data (e.g., Flatiron/OncoEMR) across gynecologic oncology care plans.

## Features

- Tracks Signatera draws by patient MRN, regimen, and treatment cycle
- Calculates expected draw timing (C1, C3, C4, and 3 weeks post-C6)
- Flags missed, overdue, or non-compliant draws
- Supports both clinical care and retrospective research review
- Can be published to Power BI Service for mobile access

## Files

- `Signatera_PowerBI_Dashboard_FINAL.xlsx`: Core dataset for visualizations
- `Signatera_PowerBI_Walkthrough.pdf`: Step-by-step build guide
- `push_to_github.bat`: Optional script to push local changes to GitHub

## Getting Started

1. Clone this repo using GitHub Desktop or `git clone`.
2. Open Power BI Desktop and load the provided Excel file.
3. Build visuals using fields like:
   - `Draw_Status_Category`
   - `Draw_Overdue`
   - `Days_Until_Draw`
4. Add filters for diagnosis, timepoint, and action needed.
5. Publish to Power BI Service to view on mobile devices.

## Credits

Created by Ellen Hooper  
Power BI and workflow support by OpenAI

## License

This project is open for collaboration under a custom clinical data use agreement. Contact Ellen for access or integration support.
