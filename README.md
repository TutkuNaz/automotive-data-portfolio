# Automotive Open Data & Analytics

[![Catalog CI](https://github.com/TutkuNaz/automotive-data-portfolio/actions/workflows/catalog-ci.yml/badge.svg)](https://github.com/TutkuNaz/automotive-data-portfolio/actions/workflows/catalog-ci.yml)
![GitHub stars](https://img.shields.io/github/stars/TutkuNaz/automotive-data-portfolio?style=social)

**38 curated datasets · 14 categories · CSV + JSON · zero-dependency search · reproducible starters**

A practical index of public automotive and mobility data, plus reproducible analytics projects covering vehicle safety, EV infrastructure, used-car markets, fleet efficiency and rental demand.

The goal is simple: make it faster to find trustworthy vehicle data, understand how it can be used, and turn it into a real analysis project.

## Automotive Dataset Catalog

The catalog currently covers public sources for:

- vehicle safety, complaints, recalls and crash data;
- fuel economy and fleet-efficiency analysis;
- EV and alternative-fuel infrastructure;
- VIN and vehicle-specification enrichment;
- road safety and MOT/inspection history;
- taxi, FHV and urban mobility demand;
- airport rental-car statistics;
- used-car pricing and resale analysis.

Use the catalog as [`CSV`](datasets/catalog.csv), [`JSON`](datasets/catalog.json), or from the command line. Sources favor first-party public agencies and are selected for practical usefulness.

Each entry records the provider, geography, access method, license/source terms, update cadence and a concrete project idea.

### Search the catalog

No third-party packages are required.

```bash
python scripts/search_catalog.py safety
python scripts/search_catalog.py "ev charging"
python scripts/search_catalog.py --category mobility --format table
python scripts/search_catalog.py vehicle --geography "United States" --format json
python scripts/search_catalog.py --list-categories
```

Example sources include NHTSA complaints and recalls, EPA fuel-economy data, DOE alternative-fuel infrastructure, UK STATS19 road-safety data, anonymised MOT records, NYC TLC trip records and LAWA rental-car statistics.

### Start an analysis in minutes

The [NHTSA vehicle-complaint starter](examples/README.md) retrieves public complaint records for a selected make, model and year, then summarizes crash/fire flags and the most frequently reported components. It is available as both a [notebook](examples/nhtsa_reliability_starter.ipynb) and a zero-dependency [Python script](examples/nhtsa_reliability_starter.py).

```bash
python examples/nhtsa_reliability_starter.py --make HONDA --model CIVIC --year 2020
```

Complaint volume is a signal, not a failure rate; the example documents the exposure and reporting-bias limitations that matter when interpreting it.

## Featured Analytics Projects

| Project | Focus | Stack |
|---|---|---|
| [**Used Car Market Intelligence**](https://github.com/TutkuNaz/01-used-car-market-intelligence) | Used-car pricing, mileage, depreciation patterns and resale-value benchmarking | Python, SQL, scikit-learn, Streamlit |
| [**Fleet Efficiency Benchmark**](https://github.com/TutkuNaz/02-fleet-efficiency-benchmark) | Fuel economy, vehicle-class trade-offs and fleet-efficiency benchmarking | Python, SQL, SciPy, SQLite |
| [**LAX Rental Market Intelligence**](https://github.com/TutkuNaz/03-lax-rental-market-intelligence) | Airport rental demand, seasonality, market share and concentration | Python, SQL, pdfplumber, Streamlit |

These projects follow a practical vehicle-lifecycle perspective:

**acquisition and resale → operating efficiency → rental demand and market context**

### 01 — Used Car Market Intelligence

Pricing and resale analysis built on a public UK used-car dataset, combining data cleaning, SQL segmentation, regression benchmarks, feature analysis and an interactive dashboard.

[View project →](https://github.com/TutkuNaz/01-used-car-market-intelligence)

### 02 — Fleet Efficiency Benchmark

Historical fuel-economy analysis based on an EPA-derived dataset, with vehicle-class and displacement benchmarking plus statistical comparison of model-year groups.

[View project →](https://github.com/TutkuNaz/02-fleet-efficiency-benchmark)

### 03 — LAX Rental Market Intelligence

Market-level analysis of public Los Angeles World Airports rental-car statistics covering monthly demand, market concentration, company-share volatility and revenue-per-transaction benchmarking.

[View project →](https://github.com/TutkuNaz/03-lax-rental-market-intelligence)

## Why This Repository Exists

Automotive datasets are spread across government portals, APIs, reports and third-party platforms. Access methods and usage terms vary, and finding a useful source often takes longer than the first analysis.

This repository keeps a compact, reviewable catalog and pairs it with working examples. It prioritizes first-party sources, clear provenance and realistic project ideas over collecting links without context.

## Contributing

New dataset suggestions, source corrections and tooling improvements are welcome.

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md), or open a **Dataset suggestion** issue. Every pull request validates the schema, generated JSON, catalog breadth, unique names and search behavior. A scheduled workflow also checks source-link health each week.

```bash
python -m unittest discover -s tests -v
```

See [`ROADMAP.md`](ROADMAP.md) for planned categories and tooling.

## Data Principles

- Prefer first-party or authoritative public sources.
- Record license or source terms without overstating redistribution rights.
- Keep proprietary, confidential and personally sensitive data out of the repository.
- Separate descriptive findings, predictive modeling and causal claims.
- Document known source limitations and reconciliation issues.

Dataset selection and licensing notes are available in [`DATASET_RESEARCH.md`](DATASET_RESEARCH.md).

## Technical Coverage

Python · pandas · NumPy · SQL · SQLite · scikit-learn · SciPy · Matplotlib · Plotly · Streamlit · pytest · GitHub Actions · public-data APIs · data-quality validation

## Supporting Material

- [`datasets/catalog.csv`](datasets/catalog.csv) — searchable automotive open-data catalog
- [`datasets/catalog.json`](datasets/catalog.json) — programmatic catalog export
- [`examples/`](examples/) — reproducible starter analyses
- [`DATASET_RESEARCH.md`](DATASET_RESEARCH.md) — source and licensing research
- [`CV_PROJECT_DESCRIPTIONS.md`](CV_PROJECT_DESCRIPTIONS.md) — concise CV project descriptions
- [`QA_REPORT.md`](QA_REPORT.md) — validation and publication checks
- [`SOCIAL_POSTS.md`](SOCIAL_POSTS.md) — project launch drafts
- [`ROADMAP.md`](ROADMAP.md) — planned catalog and analysis extensions

---

If this catalog saves you time or gives you a useful project idea, consider starring the repository so you can find future additions easily.
