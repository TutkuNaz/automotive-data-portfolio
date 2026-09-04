# Contributing

Contributions are welcome, especially additions that make the automotive open-data catalog more useful and easier to trust.

## Good contributions

- Add a public automotive, mobility, road-safety, fleet, charging or vehicle-market dataset.
- Correct a broken or outdated source URL.
- Clarify a dataset's access method, geography, cadence or license/terms.
- Add a focused project idea that can be built from an existing source.
- Improve the catalog search utility or validation tests.

## Dataset requirements

A catalog entry should have:

1. A stable first-party or authoritative source URL where possible.
2. A clear provider and geographic scope.
3. A realistic description of how the data can be accessed.
4. License or source-terms information that does not overstate redistribution rights.
5. A useful analytics or engineering use case.

Avoid sources that require redistributing proprietary, confidential, scraped-without-permission or personally sensitive data.

## Adding a dataset

Edit `datasets/catalog.csv` and add one row using the existing schema. Keep descriptions concise and avoid marketing language.

Then run:

```bash
python -m unittest discover -s tests -v
python scripts/search_catalog.py automotive
```

## Pull requests

Keep each pull request focused. For dataset additions, include the source URL and a short note explaining why the source is useful.
