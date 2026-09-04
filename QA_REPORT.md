# QA Report

Validation date: **2026-09-04**.

This document records the portfolio build checks performed before publication. It is intended to make the limits of the published outputs explicit rather than imply that every external data source could be downloaded from the restricted build runtime.

## Portfolio-Level Checks

- Three independent automotive/mobility analytics projects are published as public GitHub repositories.
- No Enterprise, employer, customer, employee, reservation-level or other proprietary data are included.
- Source and licensing notes are documented per project.
- Raw data are excluded where repository hygiene or conservative redistribution treatment calls for runtime retrieval.
- README claims were checked against generated metrics and reports.
- No TODO/TBD placeholder sections are intentionally published.
- No API tokens, passwords or private credentials are required by the repositories.

## 01 — Used Car Market Intelligence

**Local validation:** passed.

- `pytest -q`: **1 passed**.
- Python source compiled successfully.
- Three executed notebooks are included.
- SQL output, model metrics, feature importance and dashboard assets were generated.
- Five recruiter-facing figures are published.
- The public Kaggle downloader is included.
- Full Kaggle download could not be executed inside the restricted build runtime, so committed numeric findings are clearly labeled **development-validation snapshot** results and are not presented as full-dataset statistics.

## 02 — Fleet Efficiency Benchmark

**Local validation:** passed.

- `pytest -q`: **1 passed**.
- Python source compiled successfully.
- Two executed notebooks are included.
- SQL outputs and statistical-test metrics were generated from the EPA-derived `plotnine.data.mpg` source available in the build environment.
- The project intentionally does not include machine learning because it would not improve the analytical question.
- Historical 1999/2008 observations are explicitly described as a historical benchmark, not a current fleet dataset.

## 03 — LAX Rental Market Intelligence

**Local validation:** passed.

- Fresh-clone-style self-contained tests: **2 passed**.
- Python source compiled successfully.
- Test fixtures were redesigned so CI does not require committed raw LAWA tables.
- Monthly transaction, annual share, market-share heatmap and revenue-per-transaction figures were generated and published as SVG assets.
- The source transaction total reconciles to **2,273,819**.
- The source printed revenue total is **$816,143,884** while company rows sum to **$816,143,885**; the **$1 source discrepancy** is preserved rather than silently corrected.
- The PDF runtime extraction script is included, but direct external network execution was unavailable in the build container; the repository documents this limitation.

## Interpretation Guardrails

- Used-car listing prices are not realized transaction prices.
- Predictive feature importance is not causal depreciation.
- The fuel-efficiency weighted metric is an analyst-created proxy, not an official EPA combined MPG rating.
- One year of LAX aggregate data is not enough for robust forecasting.
- LAWA gross revenue after exclusions per transaction is not rental price, margin or profit.
- HHI is included as descriptive market-structure context, not as a regulatory or competition-law conclusion.

## Publication Status

| Repository | Public | README | Code / SQL | Tests / CI | Visuals |
|---|---|---|---|---|---|
| 01-used-car-market-intelligence | Yes | Yes | Yes | Yes | Yes |
| 02-fleet-efficiency-benchmark | Yes | Yes | Yes | Yes | Yes |
| 03-lax-rental-market-intelligence | Yes | Yes | Yes | Yes | Yes |
| automotive-data-portfolio | Yes | Yes | Portfolio index | N/A | Links to project visuals |

The portfolio should be read as an independent public-data body of work inspired by automotive and mobility interests, not as a representation of any employer's internal systems or datasets.
