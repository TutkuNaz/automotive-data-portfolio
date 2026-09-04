# Portfolio Validation Report

Validation date: **2026-09-04**

This report summarizes the checks completed before publication of the automotive analytics repositories.

## Portfolio-Level Checks

- Three independent automotive and mobility analytics projects are published as public repositories.
- All projects use public data; no employer, customer, employee or proprietary operational data are included.
- Data provenance and licensing notes are documented for each source.
- Raw data are excluded where redistribution is unnecessary or where runtime retrieval is the more appropriate approach.
- README findings were checked against generated metrics and analytical outputs.
- No API tokens, passwords or private credentials are stored in the repositories.
- GitHub Actions CI is configured for all three technical projects.
- The open-data hub validates 38 catalog entries, its generated JSON export,
  search behavior, starter analysis and source-link health in GitHub Actions.

## 01 — Used Car Market Intelligence

**Validation status: passed**

- Local tests: **1 passed**
- Python source compilation: passed
- Executed notebooks: 3
- SQL outputs and model metrics generated successfully
- Five analysis figures published
- GitHub Actions: **success**

The complete Kaggle source was not available during the publication validation run. Published model metrics therefore refer to the development-validation sample and are labeled accordingly.

## 02 — Fleet Efficiency Benchmark

**Validation status: passed**

- Local tests: **1 passed**
- Python source compilation: passed
- Executed notebooks: 2
- SQL outputs and statistical-test results generated successfully
- GitHub Actions: **success**

The dataset covers selected 1999 and 2008 vehicle configurations and is treated as a historical benchmark rather than a representation of a current fleet.

## 03 — LAX Rental Market Intelligence

**Validation status: passed**

- Self-contained tests: **2 passed**
- Python source compilation: passed
- Executed notebooks: 2
- Four analytical figures published
- Source annual transaction total reconciled to **2,273,819**
- GitHub Actions: **success**

The LAWA revenue table contains a $1 difference between the printed annual total (**$816,143,884**) and the sum of company rows (**$816,143,885**). The difference is retained as a source-quality observation.

## Interpretation Notes

- Used-car listing prices are not realized transaction prices.
- Predictive feature importance should not be interpreted as causal depreciation.
- The weighted MPG measure is a project-specific analytical proxy rather than an official EPA combined MPG rating.
- One year of LAX aggregate data is not sufficient for robust forecasting.
- LAWA gross revenue after exclusions per transaction is not equivalent to rental price, margin or profit.
- HHI is presented as descriptive market-structure context only.

## Publication Status

| Repository | Public | Documentation | Code / SQL | Tests / CI | Visuals |
|---|---|---|---|---|---|
| 01-used-car-market-intelligence | Yes | Yes | Yes | Passed | Yes |
| 02-fleet-efficiency-benchmark | Yes | Yes | Yes | Passed | Yes |
| 03-lax-rental-market-intelligence | Yes | Yes | Yes | Passed | Yes |
| automotive-data-portfolio | Yes | Yes | Python + data catalog | Passed | Starter notebook + project links |
