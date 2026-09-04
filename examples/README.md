# Starter analyses

## NHTSA vehicle complaints

The NHTSA starter fetches complaint records for one make, model and model year, then reports total complaints, crash/fire flags and the most frequently named components.

```bash
python examples/nhtsa_reliability_starter.py --make HONDA --model CIVIC --year 2020
```

It uses the public NHTSA API and the Python standard library. Results are descriptive signals—not failure rates: complaint counts are not normalized by vehicles in service and are affected by reporting behavior. Multi-component complaints are counted once under each named component.

A saved API response can be used for reproducible/offline work. The vehicle label is read from the response when product metadata are present:

```bash
python examples/nhtsa_reliability_starter.py --input path/to/complaints.json
```

The starter validates the response structure and fails clearly if NHTSA returns an API error or an unexpected schema instead of silently reporting zero complaints.

Open [`nhtsa_reliability_starter.ipynb`](nhtsa_reliability_starter.ipynb) for the notebook version.
