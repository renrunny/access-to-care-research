# Variable Definitions

Data dictionary for fields used across access-to-care analyses. All variables reference de-identified, aggregated data.

---

## Referral & Admission Variables

| Variable | Type | Description |
|----------|------|-------------|
| `referral_date` | date | Date referral was received |
| `admission_date` | date | Date patient was admitted to program |
| `days_to_admission` | int | Calendar days between referral and admission |
| `referral_source` | categorical | Source of referral (e.g., provider, self, hospital, school) |
| `referral_disposition` | categorical | Outcome of referral (admitted, declined, lost, barrier) |
| `program_type` | categorical | PHP or IOP |
| `site` | categorical | Treatment site identifier |

## Payer Variables

| Variable | Type | Description |
|----------|------|-------------|
| `payer_category` | categorical | Commercial, Medicaid, Medicare, Self-Pay, Other |
| `payer_name` | categorical | Specific insurance carrier |
| `auth_requested_date` | date | Date authorization was requested |
| `auth_approved_date` | date | Date authorization was approved |
| `auth_denied` | boolean | Whether authorization was denied |
| `denial_reason` | categorical | Reason for denial (if applicable) |
| `auth_turnaround_days` | int | Days from auth request to decision |

## Geographic Variables

| Variable | Type | Description |
|----------|------|-------------|
| `patient_zip` | string | Patient ZIP code (5-digit) |
| `patient_county` | string | Patient county |
| `site_lat` | float | Treatment site latitude |
| `site_lon` | float | Treatment site longitude |
| `drive_time_minutes` | float | Estimated drive time from patient ZIP to site |
| `drive_distance_miles` | float | Estimated driving distance |
| `svi_score` | float | CDC Social Vulnerability Index score for patient area |

## Clinical Variables (Aggregated Only)

| Variable | Type | Description |
|----------|------|-------------|
| `primary_dx_category` | categorical | Primary diagnosis grouping |
| `phq9_intake` | float | PHQ-9 score at intake (group mean) |
| `gad7_intake` | float | GAD-7 score at intake (group mean) |
| `acuity_level` | categorical | Clinical acuity at referral |

## Barrier Variables

| Variable | Type | Description |
|----------|------|-------------|
| `barrier_type` | categorical | Insurance, capacity, transportation, clinical fit, preference, other |
| `barrier_detail` | string | Specific barrier description |
| `barrier_resolved` | boolean | Whether barrier was resolved |
| `resolution_days` | int | Days to barrier resolution (if resolved) |
