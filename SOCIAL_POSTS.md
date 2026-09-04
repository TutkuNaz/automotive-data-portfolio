# Social Posts

## 1 — Used Car Market Intelligence

**What changes a used car's market position more: age, mileage, or the vehicle itself?**

I built a used-car market intelligence project around a public CC0 UK dataset, with a reproducible Python pipeline, SQL cohort analysis and price-model benchmarks.

The part I found most useful was not the model score itself. Age and mileage move together strongly in listing data, so simple brand averages can be misleading unless comparable vehicle cohorts are considered.

The repository includes data-quality rules, executed notebooks, SQL analysis, model evaluation and an interactive dashboard. Where the build environment only allowed a development validation snapshot, I label those metrics explicitly rather than presenting them as full-dataset results.

Tech: Python, pandas, SQL, scikit-learn, Plotly, Streamlit, pytest.

## 2 — LAX Rental Market Intelligence

**What does one year of public airport rental-car data reveal about demand?**

I analyzed Los Angeles World Airports' public CY2024 on-airport rental-car statistics and built a Python/SQL pipeline around monthly transactions, market share and gross revenue after exclusions.

The 2024 data contain 2.27M on-airport rental transactions. August was the highest-volume month, December the lowest, and the top three companies represented just under half of annual transactions.

I also kept a $1 reconciliation difference between LAWA's printed revenue total and the sum of company rows instead of silently “fixing” the source. That kind of source QA is often more important than another chart.

Tech: Python, SQL, pandas, Plotly, Streamlit, pdfplumber, pytest.

## 3 — Fleet Efficiency Benchmark

**A newer model year does not automatically mean a better result in every sample.**

I used an EPA-derived historical fuel-economy dataset to compare popular 1999 and 2008 vehicle configurations by class, displacement and drivetrain.

In this selected sample, median city/highway MPG was 17/25 in both model-year groups, and a Mann–Whitney test did not show a statistically clear shift in the weighted efficiency proxy. Vehicle class and displacement were more informative for the business question.

I intentionally left machine learning out of this project. The data and question were better suited to SQL, statistical comparison and transparent fleet-efficiency metrics.

Tech: Python, SQL, SciPy, SQLite, Matplotlib, pytest.
