# Welcome to data_fixr

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/data_fixr.svg)](https://pypi.org/project/data_fixr/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/data_fixr.svg)](https://pypi.org/project/data_fixr/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI.
If you don't plan to publish to PyPI, you can remove them.*

## Package Summary

data_fixr is a lightweight Python package designed to support exploratory data analysis and early-stage data cleaning for tabular datasets. The package provides standardized, machine-readable diagnostics and cleaning utilities that help users quickly assess data quality, identify common issues, and prepare datasets for downstream analysis or machine learning workflows. Rather than generating plots or reports, data_fixr focuses on returning clean, structured outputs that can be easily tested, logged, or integrated into automated pipelines.

## Functions
- **Correlation report**
Computes pairwise correlations between numeric columns in a pandas DataFrame and returns a long-format diagnostic table. The output summarizes the strength and direction of relationships between features in a standardized, machine-readable format suitable for exploratory analysis and preprocessing workflows.

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install data_fixr
```

TODO: Add a brief example of how to use the package to this section

To use data_fixr in your code:

```python
>>> import data_fixr
>>> data_fixr.hello_world()
```

## Contributors
- Apoorva Srivastava
- Chikire Aku-Ibe
- Nour Shawky
- Zain Nofal

## Copyright

- Copyright © 2026 Nour Shawky, Apoorva Srivastava, Zain Nofal, Chikire Aku-Ibe
.
- Free software distributed under the [MIT License](./LICENSE).
