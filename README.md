# Access to Care in Behavioral Healthcare

Research repository investigating barriers to accessing behavioral healthcare services in Partial Hospitalization Program (PHP) and Intensive Outpatient Program (IOP) settings.

## Research Focus

This project examines access-to-care dynamics across multiple dimensions:

- **Referral-to-Admission Timelines** — Measuring the interval between initial referral and treatment start, identifying bottlenecks in the intake pipeline, and quantifying delays by referral source, payer, diagnosis, and geography.
- **Geographic Access Patterns** — Geospatial analysis of patient origin, drive-time catchment areas, and underserved regions. Evaluating whether proximity to treatment sites predicts engagement, completion, and outcomes.
- **Payer-Level Access Disparities** — Comparing authorization timelines, denial rates, and treatment access across commercial insurers, Medicaid, and Medicare. Identifying payer-specific barriers that delay or prevent admission.
- **Barriers to Treatment** — Cataloging structural, financial, and logistical obstacles to entering and completing PHP/IOP treatment, including wait times, insurance friction, transportation, and capacity constraints.

## Why This Matters

Access to timely behavioral healthcare is a critical determinant of treatment outcomes. Longer wait times between referral and admission are associated with higher dropout rates, clinical deterioration, and increased downstream utilization (emergency department visits, inpatient admissions). Understanding where and why access breaks down — and for whom — is essential to improving the behavioral health delivery system.

## Repository Structure

```
access-to-care-research/
├── data/                # Data documentation (no patient data included)
├── notebooks/           # Jupyter analysis notebooks
├── src/                 # Reusable Python modules
│   ├── geo.py           # Geospatial analysis utilities
│   ├── stats.py         # Statistical testing functions
│   └── viz.py           # Visualization helpers
├── docs/                # Methodology, variable definitions, literature
├── figures/             # Output visualizations and charts
├── requirements.txt     # Python dependencies
└── LICENSE              # MIT License
```

## Data Privacy

**This repository does not contain any patient-level data.** All analyses reference de-identified, aggregated metrics. Any data files included are synthetic examples or structural documentation only. This project adheres to HIPAA privacy standards and institutional data governance policies.

## Methods Overview

Analyses in this repository use a combination of:

- Survival analysis and time-to-event modeling for referral-to-admission intervals
- Geospatial clustering and drive-time isochrone mapping
- Chi-square tests, Mann-Whitney U tests, and logistic regression for payer disparity analysis
- Descriptive epidemiology for barrier identification and categorization

See the [`docs/`](docs/) directory for detailed methodology documentation.

## Getting Started

```bash
# Clone the repository
git clone https://github.com/renrunny/access-to-care-research.git
cd access-to-care-research

# Create a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

## Requirements

- Python 3.9+
- See `requirements.txt` for package dependencies

## Citation

If you reference this work, please cite:

> Ren. (2026). *Access to Care in Behavioral Healthcare: Referral Patterns, Geographic Disparities, and Payer-Level Barriers in PHP/IOP Settings.* GitHub repository. https://github.com/renrunny/access-to-care-research

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
