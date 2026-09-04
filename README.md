# Automotive Data Portfolio

A focused portfolio of data projects covering vehicle-market economics, fleet efficiency and car-rental market intelligence.

My interest in automotive and mobility analytics grew through my internship experience in the car rental industry. The projects in this portfolio are independent analyses built exclusively from public data; they do not use proprietary company, customer, employee or operational information.

## Portfolio Objective

The portfolio is designed around a vehicle lifecycle rather than a collection of unrelated datasets:

**vehicle acquisition and resale → operating efficiency → rental demand and market context**

Each repository is built to be reviewable by both business and technical audiences, with reproducible Python code, SQL analysis, explicit data provenance, executed notebooks, tested functions and decision-oriented documentation.

## Projects

| # | Project | Business focus | Technical focus | Build status |
|---|---|---|---|---|
| 01 | [**Used Car Market Intelligence**](https://github.com/atasardacagan/01-used-car-market-intelligence) | Pricing, mileage, depreciation patterns, resale-value benchmarking | Python, SQL, scikit-learn, Streamlit | Validated end-to-end |
| 02 | [**Fleet Efficiency Benchmark**](https://github.com/atasardacagan/02-fleet-efficiency-benchmark) | Fuel-efficiency screening, vehicle-class trade-offs, operating-cost proxy | Python, SQL, SciPy, statistical testing | Validated end-to-end |
| 03 | [**LAX Rental Market Intelligence**](https://github.com/atasardacagan/03-lax-rental-market-intelligence) | Airport rental seasonality, market concentration, share volatility | Python, SQL, public-data extraction, Streamlit | Validated end-to-end |

### 01 — Used Car Market Intelligence

Repository: https://github.com/atasardacagan/01-used-car-market-intelligence

Uses a CC0 UK used-car source to build a pricing and resale-oriented analytical workflow. The repository contains modular cleaning code, SQL cohort analysis, three regression benchmarks, feature importance, executed notebooks and an interactive dashboard. Committed model metrics are deliberately labeled as development-validation results rather than full-dataset claims.

### 02 — Fleet Efficiency Benchmark

Repository: https://github.com/atasardacagan/02-fleet-efficiency-benchmark

Uses an EPA-derived historical fuel-economy sample to compare vehicle classes, displacement segments and model-year distributions. The project deliberately avoids unnecessary machine learning and instead emphasizes SQL, statistical testing and honest interpretation of a limited historical benchmark.

### 03 — LAX Rental Market Intelligence

Repository: https://github.com/atasardacagan/03-lax-rental-market-intelligence

Transforms official Los Angeles World Airports aggregate rental-car statistics into a business-analysis layer for monthly demand, market concentration and revenue-per-transaction benchmarking. The analysis is explicitly market-level; it makes no claims about internal pricing, utilization, customer behavior or profitability.

## Skills Demonstrated

- Python data pipelines with pandas and NumPy
- SQL analytics with SQLite, CTEs and window functions
- Data quality validation and source reconciliation
- Exploratory data analysis and statistical testing
- Regression baselines and model evaluation
- Business KPI definition and careful interpretation
- Matplotlib and Plotly visualization
- Streamlit dashboard development
- pytest unit tests
- Reproducible dataset-ingestion scripts
- GitHub Actions CI configuration
- Licensing and data-provenance documentation
- Technical writing for recruiter and engineering audiences

## Data Principles

1. Use public, legally reusable sources.
2. Keep large or conservatively licensed raw data outside Git history.
3. Never present development-sample results as full-dataset findings.
4. Separate correlation, prediction and causal claims.
5. Document assumptions and data-quality exceptions.
6. Use machine learning only when it improves the business analysis.

See [`DATASET_RESEARCH.md`](DATASET_RESEARCH.md) for the source-selection and licensing review.

## Repository Standards

Every project follows the same practical standard without creating empty folders for appearance:

```text
project/
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── data/
│   └── README.md
├── notebooks/
├── scripts/
├── src/
├── sql/
├── reports/
│   └── figures/
├── tests/
└── .github/workflows/ci.yml
```

Dashboard folders are included only where an interactive view adds value.

## Portfolio Roadmap

The next logical additions, if the portfolio needs to expand beyond these three repositories, are **vehicle reliability / maintenance risk** using NHTSA complaints and recalls, followed by **EV adoption / charging-gap analysis** using explicitly licensed public EV and charging-infrastructure data. They are intentionally not opened as empty repositories.

## Supporting Documents

- [`CV_PROJECT_DESCRIPTIONS.md`](CV_PROJECT_DESCRIPTIONS.md) — concise CV-ready bullets
- [`SOCIAL_POSTS.md`](SOCIAL_POSTS.md) — technical LinkedIn post drafts
- [`DATASET_RESEARCH.md`](DATASET_RESEARCH.md) — dataset and licensing decisions
- [`QA_REPORT.md`](QA_REPORT.md) — build and validation record
