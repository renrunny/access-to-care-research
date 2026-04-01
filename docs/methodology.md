# Methodology

## Overview

This document describes the analytical methods used across the access-to-care research program. All analyses use de-identified, aggregated data in compliance with HIPAA and institutional data governance policies.

---

## 1. Referral-to-Admission Timeline Analysis

**Objective:** Quantify the time between referral receipt and program admission, and identify factors associated with longer wait times.

**Approach:**
- Calculate referral-to-admission interval in calendar days
- Stratify by payer, referral source, diagnosis category, program type (PHP/IOP), and site
- Use Kaplan-Meier survival curves to model time-to-admission
- Cox proportional hazards regression to identify independent predictors of delay
- Sensitivity analysis excluding weekends/holidays

**Key Metrics:**
- Median days from referral to admission
- 75th and 90th percentile wait times
- Conversion rate (referrals that result in admission)

---

## 2. Geographic Access Analysis

**Objective:** Map patient origin patterns and evaluate geographic barriers to care.

**Approach:**
- Geocode patient ZIP codes to centroids
- Calculate drive-time isochrones (30, 60, 90 minute zones) from each treatment site
- Identify underserved areas with high behavioral health need but low access
- Overlay census and community health data (SVI, MHPSS indicators)
- Cluster analysis to identify geographic catchment patterns

**Tools:** GeoPandas, Folium, OpenRouteService API, Census TIGER/Line shapefiles

---

## 3. Payer Disparity Analysis

**Objective:** Evaluate whether access to PHP/IOP differs systematically by payer type.

**Approach:**
- Compare referral-to-admission timelines by payer (commercial, Medicaid, Medicare, self-pay)
- Analyze authorization denial rates and appeal outcomes by payer
- Logistic regression: probability of admission as a function of payer, controlling for diagnosis, acuity, and geography
- Chi-square and Mann-Whitney U tests for categorical and continuous comparisons

**Key Metrics:**
- Denial rate by payer
- Median authorization turnaround time
- Admission probability by payer category

---

## 4. Barrier Identification

**Objective:** Catalog and quantify structural, financial, and logistical barriers to entering PHP/IOP treatment.

**Approach:**
- Descriptive analysis of referral disposition (admitted, declined, lost to follow-up, insurance barrier, etc.)
- Categorize barriers: insurance/authorization, capacity/waitlist, transportation/distance, clinical fit, patient preference
- Frequency and proportion analysis by barrier type, payer, and geography
- Trend analysis over time to evaluate whether barriers are improving or worsening

---

## Variable Definitions

See `variables.md` for a complete data dictionary of all fields used in these analyses.
