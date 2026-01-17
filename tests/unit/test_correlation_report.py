"""
Unit tests for the correlation_report function.

This module contains tests that validate the behavior of the
correlation_report function in the data_fixr package. The tests
cover expected functionality, including correct output structure
and values, as well as edge cases such as handling non-numeric
columns, invalid input types, invalid correlation methods, and
insufficient numeric data.

The tests are written using pytest and are designed to ensure
that correlation_report behaves as specified and fails gracefully
when given invalid input.
"""

import pandas as pd
import pytest
from data_fixr.correlation_report import correlation_report



def test_correlation_report_three_numeric_columns_values_and_schema():
    """
    Happy path: 3 numeric columns -> 3 unique pairs with correct columns and values.
    """
    df = pd.DataFrame(
        {
            "a": [1, 2, 3, 4],
            "b": [1, 2, 3, 4],  
            "c": [4, 3, 2, 1],   
        }
    )

    result = correlation_report(df, method="pearson")

    assert list(result.columns) == ["feature_1", "feature_2", "correlation", "abs_correlation"]
    assert len(result) == 3  
    pairs = set(map(tuple, result[["feature_1", "feature_2"]].to_numpy()))
    assert pairs == {("a", "b"), ("a", "c"), ("b", "c")}

    corr_map = {tuple(r[:2]): r[2] for r in result[["feature_1", "feature_2", "correlation"]].to_numpy()}
    assert corr_map[("a", "b")] == pytest.approx(1.0)
    assert corr_map[("a", "c")] == pytest.approx(-1.0)
    assert corr_map[("b", "c")] == pytest.approx(-1.0)
    assert (result["abs_correlation"] == result["correlation"].abs()).all()



def test_correlation_report_ignores_non_numeric_columns():

    """
    Ensure that non-numeric (categorical/object) columns are ignored
    when computing pairwise correlations.
    """
    df = pd.DataFrame({
        "a": [1, 2, 3, 4],
        "b": [10, 20, 30, 40],
        "city": ["Vancouver", "Toronto", "Montreal", "Calgary"],
    })

    result = correlation_report(df, method="pearson")
    assert len(result) == 1
    feature_pair = tuple(result.loc[0, ["feature_1", "feature_2"]])
    assert feature_pair == ("a", "b")

    assert "city" not in result["feature_1"].values
    assert "city" not in result["feature_2"].values
    assert result.loc[0, "correlation"] == pytest.approx(1.0)
    assert result.loc[0, "abs_correlation"] == pytest.approx(1.0)




def test_correlation_report_invalid_method_raises_value_error():
    """
    Invalid method should raise ValueError.
    """
    df = pd.DataFrame({"a": [1, 2, 3], "b": [1, 2, 3]})
    with pytest.raises(ValueError, match="method"):
        correlation_report(df, method="not_a_method")


def test_correlation_report_requires_two_numeric_columns():
    """
    Fewer than two numeric columns should raise ValueError.
    """
    df_one_numeric = pd.DataFrame({"a": [1, 2, 3], "city": ["x", "y", "z"]})
    with pytest.raises(ValueError, match="numeric"):
        correlation_report(df_one_numeric)

    df_no_numeric = pd.DataFrame({"city": ["x", "y", "z"]})
    with pytest.raises(ValueError, match="numeric"):
        correlation_report(df_no_numeric) 


def test_correlation_report_non_dataframe_raises():
    """Non-DataFrame input should raise TypeError."""
    with pytest.raises(TypeError):
        correlation_report(["not", "a", "df"])