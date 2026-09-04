# Automotive Data Portfolio

Data projects focused on automotive markets, fleet economics and mobility analytics.

My interest in automotive analytics developed through experience in the car-rental industry. The work in this portfolio is independent and uses public data only; no proprietary company, customer or operational data are included.

## Projects

| Project | Focus | Stack |
|---|---|---|
| [**Used Car Market Intelligence**](https://github.com/atasardacagan/01-used-car-market-intelligence) | Used-car pricing, mileage, depreciation patterns and resale-value benchmarking | Python, SQL, scikit-learn, Streamlit |
| [**Fleet Efficiency Benchmark**](https://github.com/atasardacagan/02-fleet-efficiency-benchmark) | Fuel economy, vehicle-class trade-offs and fleet-efficiency benchmarking | Python, SQL, SciPy, SQLite |
| [**LAX Rental Market Intelligence**](https://github.com/atasardacagan/03-lax-rental-market-intelligence) | Airport rental demand, seasonality, market share and concentration | Python, SQL, pdfplumber, Streamlit |

## Portfolio Structure

The projects follow a practical vehicle-lifecycle perspective:

**acquisition and resale → operating efficiency → rental demand and market context**

### Used Car Market Intelligence

A pricing and resale analysis built on a public UK used-car dataset. The project combines data cleaning, SQL segmentation, regression benchmarks, feature analysis and an interactive dashboard.

[View repository →](https://github.com/atasardacagan/01-used-car-market-intelligence)

### Fleet Efficiency Benchmark

A historical fuel-economy study based on an EPA-derived dataset. The analysis compares vehicle classes, engine displacement and model-year distributions using SQL and statistical testing.

[View repository →](https://github.com/atasardacagan/02-fleet-efficiency-benchmark)

### LAX Rental Market Intelligence

A market-level analysis of public Los Angeles World Airports rental-car statistics. The project covers monthly demand, market concentration, company share volatility and revenue-per-transaction benchmarking.

[View repository →](https://github.com/atasardacagan/03-lax-rental-market-intelligence)

## Core Skills

- Python data processing with pandas and NumPy
- SQL analytics with CTEs, window functions and segmentation
- Data validation, reconciliation and quality checks
- Exploratory analysis and statistical testing
- Regression modeling and model evaluation
- Business KPI design and interpretation
- Matplotlib and Plotly visualization
- Streamlit dashboard development
- pytest-based testing
- Reproducible data-ingestion workflows
- GitHub Actions CI
- Dataset licensing and provenance documentation

## Working Principles

The projects are built around a few consistent rules:

- use public data with documented provenance;
- keep raw data outside the repository when redistribution is unnecessary or unclear;
- distinguish descriptive analysis, prediction and causal interpretation;
- document assumptions and known data limitations;
- use machine learning only when it adds analytical value.

Dataset selection and licensing notes are documented in [`DATASET_RESEARCH.md`](DATASET_RESEARCH.md).

## Repository Standard

Each project separates analysis code, notebooks, SQL, tests and generated outputs:

```text
project/
├── README.md
├── data/
├── notebooks/
├── scripts/
├── src/
├── sql/
├── reports/
├── tests/
└── .github/workflows/ci.yml
```

Interactive dashboards are included where they improve exploration of the results.

## Supporting Material

- [`CV_PROJECT_DESCRIPTIONS.md`](CV_PROJECT_DESCRIPTIONS.md) — concise project bullets for CV use
- [`DATASET_RESEARCH.md`](DATASET_RESEARCH.md) — dataset and licensing review
- [`QA_REPORT.md`](QA_REPORT.md) — validation and publication checks
- [`SOCIAL_POSTS.md`](SOCIAL_POSTS.md) — project summaries for professional posts

## Next Areas of Interest

Potential extensions include vehicle reliability and maintenance-risk analysis using NHTSA data, and EV adoption / charging-infrastructure analysis using licensed public datasets.
