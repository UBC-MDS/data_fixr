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
- **Correlation Report:**
Computes pairwise correlations between numeric columns in a pandas DataFrame and returns a long-format diagnostic table. The output summarizes the strength and direction of relationships between features in a standardized, machine-readable format suitable for exploratory analysis and preprocessing workflows.

- **Remove Duplicates:**
Identifies and removes duplicate rows for a given dataset. Users can specify the retention strategy for handling duplicates and choose whether duplicates are detected using all columns or a specified subset. Optionally, the function can return a useful summary report describing the number of duplicate rows detected and removed.

- **Detect Anomalies:**
This function identifies and flags outliers in numeric columns of a pandas DataFrame using either the Z-score method (for normally distributed data) or the IQR (Interquartile Range) method (for skewed data). It returns a DataFrame with the numeric columns and boolean outlier flags for each numeric column, as well as the overall percentage of outliers detected.

- **Missing Values:**
This function fills missing values (NaN) in both numeric and categorical (non-numeric) columns of a pandas DataFrame. Numeric columns are filled using a user-specified method (mean, median, or mode), while categorical (non-numeric) columns are automatically filled using mode imputation. The function returns a DataFrame with missing values filled and the overall percentage of missing values that were imputed across all columns.


## Position in Python Environment

The functionality provided by **data_fixr** overlaps partially with capabilities available in established Python data analysis libraries, most notably [pandas](https://pandas.pydata.org/) and [scikit-learn](https://scikit-learn.org/stable/). Pandas provides low-level methods for computing correlations between numeric variables and for removing duplicate rows, while scikit-learn and related libraries offer utilities for identifying outliers as part of preprocessing or feature selection workflows. However, these tools typically expose such functionality as individual operations without producing standardized, diagnostics-oriented summaries. 


In particular, while duplicate removal and missing-value imputation functionality already exist in pandas, the corresponding functions in data_fixr extend this behavior by optionally returning structured summary information. The duplicate removal function can return a summary report describing how many duplicate rows were detected and removed, while the missing-value filling function reports the overall percentage of missing values that were imputed across the dataset. Additionally, automated exploratory data analysis tools such as [ydata-profiling](https://ydata.ai/) focus on generating comprehensive visual or HTML reports, whereas data_fixr emphasizes lightweight, modular functions that return machine-readable outputs intended for exploratory diagnostics, reproducible preprocessing pipelines, and downstream machine learning workflows.


## Get started

First, clone the repository:

```bash
$ git clone https://github.com/UBC-MDS/data_fixr.git
```

Navigate into the package directory:

```bash
$ cd data_fixr
```

Install the package in editable mode:

```bash
$ pip install -e .
```

To run the tests:

```bash
$ pytest
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
