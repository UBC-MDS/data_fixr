# Welcome to data_fixr

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/data_fixr.svg)](https://pypi.org/project/data_fixr/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/data_fixr.svg)](https://pypi.org/project/data_fixr/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

## Package Summary

data_fixr is a lightweight Python package designed to support exploratory data analysis and early-stage data cleaning for tabular datasets. The package provides standardized, machine-readable diagnostics and cleaning utilities that help users quickly assess data quality, identify common issues, and prepare datasets for downstream analysis or machine learning workflows. Rather than generating plots or reports, data_fixr focuses on returning clean, structured outputs that can be easily tested, logged, or integrated into automated pipelines.

## Documentation

To view usage examples and function details, refer to the reference page of the [documentation](https://ubc-mds.github.io/data_fixr/reference/).

### Example Use Case

A common early-stage data analysis workflow involves checking for correlations, missing values, duplicates, and anomalies before modeling. data_fixr allows these checks to be performed with minimal code and consistent outputs:

```python
from data_fixr import (
    correlation_report,
    remove_duplicates,
    detect_anomalies,
    missing_values
)
import pandas as pd

data = pd.DataFrame({
    'age': [25, 30, 25, 150, 35, 30, 28, 45, 32, 29],  # 150 is an anomaly
    'income': [50000, 60000, 50000, 70000, None, 60000, 55000, 85000, 62000, 58000], #contains missing value and duplicates
    'years_experience': [3, 7, 3, 25, 10, 7, 5, 20, 8, 6]
})

# Fill missing values and fill them with method 'mode'
missing_report = missing_values(data, method='mode')

# Identify and remove duplicate rows, keeping the first instance of the duplicated observation
clean_data = remove_duplicates(data, keep='first', report=True)

# Find outliers or anomalous values with default zscore method in the age and years experience columns
anomalies = detect_anomalies(data[['age', 'years_experience']])

# Generate a correlation report showing pairwise correlations between all numeric variables in the data using the spearman correlation method:
corr_report = correlation_report(data, method='spearman')

```

## Installation

### Install from Github

```bash
git clone https://github.com/UBC-MDS/data_fixr.git
cd data_fixr
pip install -e .
```

### Install from Test PyPI

To install the latest development release of **data_fixr** from Test PyPI:

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ data-fixr
```

If you already have data_fixr installed and want to upgrade to the newest available version on Test PyPI, run:

```bash
pip install --upgrade -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ data-fixr
```

### Verfify installation via python interpreter

```python
from data_fixr import (
    correlation_report,
    remove_duplicates,
    detect_anomalies,
    missing_values
)
```

## Functions

- `correlation_report()`:
Computes pairwise correlations between numeric columns in a pandas DataFrame and returns a long-format diagnostic table. The output summarizes the strength and direction of relationships between features in a standardized, machine-readable format suitable for exploratory analysis and preprocessing workflows.

- `remove_duplicates()`:
Identifies and removes duplicate rows for a given dataset. Users can specify the retention strategy for handling duplicates and choose whether duplicates are detected using all columns or a specified subset. Optionally, the function can return a useful summary report describing the number of duplicate rows detected and removed.

- `detect_anomalies()`':
This function identifies and flags outliers in numeric columns of a pandas DataFrame using either the Z-score method (for normally distributed data) or the IQR (Interquartile Range) method (for skewed data). It returns a DataFrame with the numeric columns and boolean outlier flags for each numeric column, as well as the overall percentage of outliers detected.

- `missing_values`:
This function fills missing values (NaN) in both numeric and categorical (non-numeric) columns of a pandas DataFrame. Numeric columns are filled using a user-specified method (mean, median, or mode), while categorical (non-numeric) columns are automatically filled using mode imputation. The function returns a DataFrame with missing values filled and the overall percentage of missing values that were imputed across all columns.

## Position in Python Environment

The functionality provided by **data_fixr** overlaps partially with capabilities available in established Python data analysis libraries, most notably [pandas](https://pandas.pydata.org/) and [scikit-learn](https://scikit-learn.org/stable/). Pandas provides low-level methods for computing correlations between numeric variables and for removing duplicate rows, while scikit-learn and related libraries offer utilities for identifying outliers as part of preprocessing or feature selection workflows. However, these tools typically expose such functionality as individual operations without producing standardized, diagnostics-oriented summaries. 


In particular, while duplicate removal and missing-value imputation functionality already exist in pandas, the corresponding functions in data_fixr extend this behavior by optionally returning structured summary information. The duplicate removal function can return a summary report describing how many duplicate rows were detected and removed, while the missing-value filling function reports the overall percentage of missing values that were imputed across the dataset. Additionally, automated exploratory data analysis tools such as [ydata-profiling](https://ydata.ai/) focus on generating comprehensive visual or HTML reports, whereas data_fixr emphasizes lightweight, modular functions that return machine-readable outputs intended for exploratory diagnostics, reproducible preprocessing pipelines, and downstream machine learning workflows.

## Development and Testing

To contribute, run the tests, or build documentation, follow the steps below.

First, clone the repository and navigate to the root:

```bash
$ git clone https://github.com/UBC-MDS/data_fixr.git
$ cd data_fixr
```

(Optional) To run the package in a clean environment with Python 3.11.

```bash
$ conda env create -f environment.yml
$ conda activate data_fixr
```

Install the package in editable mode:

```bash
$ pip install -e .
```

Install the required dependencies:

```bash
$ pip install -e ".[tests, dev, docs]"
```

To run tests:

```bash
$ pytest --cov=src --cov-branch --cov-report=term-missing
```

To build documentation locally:

```bash
quartodoc build
quarto render 
```

To preview the documentation:

```bash
quarto preview
```

**Documentation is automatically built and deployed via GitHub Actions when changes are merged into ```main```.**

If you have opted to use the conda environment, deactivate the environment once finished with:

```bash
$ conda deactivate
```

## Requirements
- Python ≥ 3.10

## Contributors
- Apoorva Srivastava
- Chikire Aku-Ibe
- Nour Shawky
- Zain Nofal

## Copyright

- Copyright © 2026 Nour Shawky, Apoorva Srivastava, Zain Nofal, Chikire Aku-Ibe.
- Free software distributed under the [MIT License](./LICENSE).
