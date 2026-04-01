# Data Directory

## ⚠️ Data Privacy Notice

**This directory does not and must not contain any real patient data.**

All patient-level data used in this research is stored in secure, HIPAA-compliant environments and is never committed to version control. Any data files in this directory are limited to:

- Synthetic / simulated example datasets for demonstration
- Aggregated summary statistics (no individual-level records)
- Data dictionaries and schema documentation
- Public reference data (e.g., ZIP code shapefiles, census data)

## Expected Data Sources

The analyses in this repository reference the following data domains (accessed via secure institutional data warehouses):

| Domain | Description |
|--------|-------------|
| Referral records | Referral date, source, payer, diagnosis, program type |
| Admission records | Admission date, program, site location |
| Geographic data | Patient ZIP/county, site coordinates, drive-time zones |
| Payer authorization | Authorization request/approval dates, denial flags |
| Assessment scores | PHQ-9, GAD-7 at intake and discharge (aggregated only) |

## File Naming Conventions

If synthetic or aggregated data files are added:

- `synthetic_*.csv` — Simulated data for code testing
- `agg_*.csv` — Aggregated summary tables
- `ref_*.csv` — Public reference/lookup tables
