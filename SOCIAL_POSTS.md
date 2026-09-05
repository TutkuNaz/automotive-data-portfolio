# Professional Project Summaries

## Used Car Market Intelligence

I built a used-car market analysis project using a public UK dataset to study the relationship between price, mileage, vehicle age and model characteristics.

The workflow combines Python-based data processing, SQL cohort analysis, regression benchmarks and an interactive Streamlit dashboard. One of the main takeaways was the importance of evaluating age and mileage together: raw brand-level averages can be misleading when the underlying vehicle mix differs substantially.

The project also includes data-quality checks, executed notebooks, model evaluation and reproducible data-ingestion scripts.

**Stack:** Python, pandas, SQL, scikit-learn, Plotly, Streamlit, pytest.

Repository: https://github.com/TutkuNaz/01-used-car-market-intelligence

---

## LAX Rental Market Intelligence

I analyzed public Los Angeles World Airports rental-car statistics to understand monthly demand, market concentration and company share movements at LAX.

The 2024 dataset contains approximately 2.27 million on-airport rental transactions. August recorded the highest monthly volume, while December recorded the lowest. The three largest companies represented just under half of annual transactions.

The project includes a Python/SQL data pipeline, source reconciliation, automated tests and a Streamlit dashboard. During validation, I also retained a $1 difference between LAWA's printed annual revenue total and the sum of company rows rather than modifying the source values.

**Stack:** Python, pandas, SQL, Plotly, Streamlit, pdfplumber, pytest.

Repository: https://github.com/TutkuNaz/03-lax-rental-market-intelligence

---

## Fleet Efficiency Benchmark

I used an EPA-derived historical fuel-economy dataset to compare vehicle classes, engine displacement and model-year groups from a fleet-efficiency perspective.

In the selected sample, median city and highway MPG were the same for the 1999 and 2008 groups, and a Mann–Whitney U test did not show a statistically clear shift in the weighted efficiency proxy. Vehicle class and engine displacement provided more useful segmentation for the analysis.

The project focuses on SQL, statistical comparison and transparent efficiency metrics rather than adding a machine-learning model where it would not improve the business question.

**Stack:** Python, pandas, SQL, SciPy, SQLite, Matplotlib, pytest.

Repository: https://github.com/TutkuNaz/02-fleet-efficiency-benchmark
