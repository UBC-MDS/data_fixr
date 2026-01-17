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
from data_fixr import missing_values
#from data_fixr.missing_values import missing_values


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


def test_missing_values_mode_imputation_numeric_only():
    """
    Mode imputation should be applied correctly to numeric columns.
    """
    df = pd.DataFrame({
        "a": [1, 2, 2, np.nan, 2, 3]
    })

    result_df, filled_percentage = missing_values(df, method="mode")

    assert result_df.loc[3, "a"] == 2
    assert isinstance(filled_percentage, float)
    assert filled_percentage == pytest.approx(16.6667, rel=1e-2)
    

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


def test_missing_values_does_not_modify_original():
    """
    The original DataFrame should remain unchanged.
    """
    df = pd.DataFrame({
        "a": [1, np.nan, 3],
        "b": ["x", np.nan, "z"]
    })

    df_original = df.copy()
    result_df, filled_percentage = missing_values(df, method="mean")

    pd.testing.assert_frame_equal(df, df_original)
    assert result_df is not df


# Edge test cases


def test_missing_values_all_nan_column_unchanged():
    """
    Columns containing all NaN values should be left unchanged
    and should not contribute filled values.
    """
    df = pd.DataFrame({
        "a": [1, np.nan, 3],
        "b": [np.nan, np.nan, np.nan]
    })

    result_df, filled_percentage = missing_values(df, method="mean")

    assert result_df["b"].isna().all()
    assert isinstance(filled_percentage, float)
    assert filled_percentage == pytest.approx(16.6667, rel=1e-2)


def test_missing_values_uses_first_mode():
    """
    When multiple modes exist, the first mode returned by pandas
    should be used.
    """
    df = pd.DataFrame({
        "a": [1, 2, np.nan, np.nan]
    })

    result_df, filled_percentage = missing_values(df, method="mode")

    assert result_df.loc[2, "a"] == 1
    assert result_df.loc[3, "a"] == 1


def test_missing_values_no_missing_values():
    """
    If there are no missing values, the DataFrame should be unchanged
    and filled_percentage should be 0.
    """
    df = pd.DataFrame({
        "a": [1, 2, 3],
        "b": ["x", "y", "z"]
    })

    result_df, filled_percentage = missing_values(df, method="mean")

    pd.testing.assert_frame_equal(df, result_df)
    assert filled_percentage == 0.0


def test_missing_values_all_nan_dataframe():
    """
    DataFrame with all NaN values should remain unchanged.
    """
    df = pd.DataFrame({
        "a": [np.nan, np.nan],
        "b": [np.nan, np.nan]
    })

    result_df, filled_percentage = missing_values(df, method="mean")

    assert result_df.isna().all().all()
    assert filled_percentage == 0.0


def test_missing_values_empty_dataframe():
    """
    Empty DataFrame should return empty DataFrame with 0% filled.
    """
    df = pd.DataFrame()
    result_df, filled_percentage = missing_values(df, method="mean")

    assert result_df.empty
    assert filled_percentage == 0.0


# Error handling test cases


def test_missing_values_invalid_df_type():
    """
    Non-DataFrame input should raise TypeError.
    """
    with pytest.raises(TypeError):
        missing_values([1, 2, 3], method="mean")


def test_missing_values_invalid_method():
    """
    Invalid numeric imputation method should raise ValueError.
    """
    df = pd.DataFrame({
        "a": [1, np.nan, 3]
    })

    with pytest.raises(ValueError):
        missing_values(df, method="average")