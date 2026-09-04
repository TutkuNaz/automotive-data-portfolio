# Dataset Research and Licensing Review

Research date: **2026-09-04**.

The portfolio contains three completed standalone projects. Additional sources are maintained in the open-data catalog and are promoted to starter analyses or standalone repositories only when the scope supports a complete, reproducible project.

| Source | Potential use | License / reuse position | Decision |
|---|---|---|---|
| Kaggle — 100,000 UK Used Car Data Set | Used-car pricing and resale analysis | Dataset page marks it **CC0 / Public Domain** | Selected for Project 01; raw data kept out of Git for repository hygiene |
| U.S. EPA / fueleconomy.gov via `plotnine.data.mpg` | Fuel-efficiency benchmark | EPA standard open-data policy states agency-produced data are public domain unless otherwise specified; plotnine is MIT | Selected for Project 02 |
| Los Angeles World Airports CY2024 Rental Car Monthly Stats | Direct rental-market seasonality and share analysis | LAWA general disclaimer states website information is public domain unless otherwise indicated; Investor Relations publishes additional terms | Selected for Project 03 with conservative runtime retrieval; original PDF not redistributed |
| NHTSA Consumer Complaints | Reliability / maintenance-risk analysis | U.S. federal public data; large daily-updated bulk file | Cataloged with a reproducible API starter; a full-scale Project 04 remains deferred until it can be built fully |
| NHTSA Recalls | Reliability / recall-risk analysis | U.S. federal public data | Strong candidate to combine with complaints rather than create a separate small repo |
| Washington State Electric Vehicle Population | EV adoption and geospatial analysis | ODbL 1.0; current public data | Strong future EV project candidate |
| U.S. DOE AFDC Alternative Fuel Stations | Charging-infrastructure gap analysis | Public federal data with source-specific reuse terms | Candidate to combine with EV population data |
| NYC TLC Trip Record Data | Mobility-demand forecasting | Public city data; monthly Parquet files, very large | Strong demand-modeling candidate, but intentionally deferred until the portfolio needs a fourth/fifth project |
| U.S. Census / BTS Vehicle Inventory and Use Survey | Vehicle utilization / fleet analysis | Federal public-use file | Excellent fleet candidate; deferred because current build environment could not retrieve the source directly |
| UK MOT history | Reliability / mileage / maintenance | UK Open Government Licence workflow | High-value advanced project, but materially larger data-engineering scope |
| UK STATS19 Road Safety | Accident severity / geospatial risk | Open Government Licence | Useful but less directly tied to rental/fleet lifecycle than selected projects |
| IEA Global EV Outlook data | Global EV adoption | Dataset terms vary by edition; products do not necessarily share identical reuse treatment | Reference only unless the exact edition terms are documented in-repo |
| ACEA vehicle market reports | Sales / production | Copyrighted association material | Not selected for redistribution; use only as a linked reference unless permission/terms allow |

## Selected Project Rationale

### Project 01 — Used Car Market Intelligence

Best first project because it combines automotive domain knowledge, data cleaning, SQL, regression and business interpretation in one repository. CC0 licensing also makes the ingestion story clean.

### Project 02 — Fleet Efficiency Benchmark

Adds a distinct Data Analyst skill set: statistical comparison, segment analysis and operating-efficiency reasoning. It intentionally does not add ML simply to increase technology count.

### Project 03 — LAX Rental Market Intelligence

Provides the strongest direct bridge to car-rental and airport mobility using public aggregate data. It demonstrates data extraction, reconciliation, seasonality, concentration analysis and careful limitations.

## Primary Links

- UK used-car dataset: https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes
- plotnine MPG documentation: https://plotnine.org/reference/mpg.html
- EPA standard open-data license: https://edg.epa.gov/EPA_Data_License.html
- LAWA CY2024 rental-car report: https://www.lawa.org/sites/lawa/files/documents/CY2024%20LAX%20On%20and%20Off%20Airport%20Monthly%20Stats.pdf
- LAWA disclaimer: https://www.lawa.org/disclaimer
- NHTSA datasets/APIs: https://www.nhtsa.gov/nhtsa-datasets-and-apis
- Washington EV data: https://catalog.data.gov/dataset/electric-vehicle-population-data
- NYC TLC trip data: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- UK road-safety open data: https://www.gov.uk/government/statistical-data-sets/road-safety-open-data
