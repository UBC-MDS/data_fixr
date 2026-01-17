"""
Unit tests for missing_values function.

These tests verify that missing_values correctly imputes
missing values in numeric and categorical columns using
the specified strategies, returns the expected filled
percentage, handles edge cases such as all-Nan columns,
and raises appropriate errors for invalid inputs.
"""

import pandas as pd
import numpy as np
import pytest
from data_fixr.missing_values import missing_values

# Expected test cases

def test_missing_values_median_numeric_and_mode_categorical():
    """
    Numeric columns should be imputed using the specified method,
    while categorical columns should always used mode imputation.
    """
    df = pd.DataFrame({
        "age": [25, 30, np.nan, 28],
        "income": [50000, np.nan, 52000, np.nan],
        "city": ["A", "B", np.nan, "B"]
    })

    result_df, filled_percentage = missing_values(df, method="median")

    assert result_df.loc[2, "age"] == 28
    assert result_df.loc[1, "income"] == 51000
    assert result_df.loc[2, "city"] == "B"

    assert isinstance(filled_percentage, float)
    assert filled_percentage == pytest.approx(33.333, rel=1e-2)


def test_missing_values_mean_imputation_numeric_only():
    """
    Mean imputation should be applied correctly to numeric columns.
    """
    df = pd.DataFrame({
        "a": [1.0, 2.0, np.nan],
        "b": [10.0, np.nan, 30.0]
    })

    result_df, filled_percentage = missing_values(df, method="mean")

    assert result_df.loc[2, "a"] == pytest.approx(1.5)
    assert result_df.loc[1, "b"] == pytest.approx(20.0)

    assert isinstance(filled_percentage, float)
    assert filled_percentage == pytest.approx(33.333, rel=1e-2)


def test_missing_values_categorical_only():
    """
    All categorical columns should be imputed using mode.
    """
    df = pd.DataFrame({
        "city": ["A", "B", np.nan, "B"],
        "country": ["CA", np.nan, "CA", "CA"]
    })

    result_df, filled_percentage = missing_values(df, method="mean")

    assert result_df.loc[2, "city"] == "B"
    assert result_df.loc[1, "country"] == "CA"

    assert isinstance(filled_percentage, float)
    assert filled_percentage == pytest.approx(25.0)


# Edge test cases











    