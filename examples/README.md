# Starter analyses

## NHTSA vehicle complaints

The NHTSA starter fetches complaint records for one make, model and model year, then reports total complaints, crash/fire flags and the most frequently named components.

```bash
python examples/nhtsa_reliability_starter.py --make HONDA --model CIVIC --year 2020
```

It uses the public NHTSA API and the Python standard library. Results are descriptive signals—not failure rates: complaint counts are not normalized by vehicles in service and are affected by reporting behavior. A saved API response can be used for reproducible/offline work with `--input path/to/complaints.json`.

Open [`nhtsa_reliability_starter.ipynb`](nhtsa_reliability_starter.ipynb) for the notebook version.
