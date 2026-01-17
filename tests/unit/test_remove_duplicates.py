"""
Unit tests for remove_duplicates() function.

The tests verify that the remove_duplicates() function correctly returns a 
dataframe with duplicate rows removed using default parameters and using 
optional user-specified parameters such as cols, keep and report. It also checks 
that the function can handle edge cases and raises clear errors for invalid 
inputs.
"""

import pandas as pd
import pytest

from data_fixr import remove_duplicates

#from data_fixr.remove_duplicates import remove_duplicates

def test_remove_duplicates_default():
    """
    Checking expected output of function using default parameters.
    """
    df = pd.DataFrame({
    "user_id": [101, 101, 205],
    "city": ["Vancouver", "Vancouver", "Toronto"],
    "age": [22, 22, 30]})

    result = remove_duplicates(df)

    assert len(result) == 2
    assert result["user_id"].tolist() == [101, 205]

def test_remove_duplicates_subset_cols_keep_last_with_report():
    """
    Checking that last instance of duplicate is returned, when
    optional parameter keep is specified as 'last' with a subset of columns
    and report=True.
    """
    df = pd.DataFrame({
    "user_id": [101, 101, 205],
    "city": ["Vancouver", "Toronto", "Montreal"],
    "age": [22, 23, 30]})

    cleaned_df, report = remove_duplicates(
        df,
        cols=["user_id"],
        keep="last",
        report=True)

    assert cleaned_df.iloc[0]["city"] == "Toronto"
    assert len(cleaned_df) == 2

    assert isinstance(report, dict)
    assert report["total_rows"] == 3
    assert report["duplicate_rows"] == 1
    assert report["rows_removed"] == 1
    assert report["strategy"] == "last"
    assert report["cols_used"] == ["user_id"]

def test_remove_duplicates_invalid_df_type():
    """
    Tests that invalid input for dataframe raises correct 
    TypeError message.
    """
    with pytest.raises(TypeError):
        remove_duplicates([1, 2, 3])

def test_remove_duplicates_invalid_keep_val():
    """
    Tests that error is raised when keep argument is not 
    one of first, last or False
    """
    df = pd.DataFrame({"a": [1, 1]})

    with pytest.raises(ValueError):
        remove_duplicates(df, keep="middle")

def test_remove_duplicates_invalid_col_type():
    """
    Tests that error is raised when col type is not a list
    """
    df = pd.DataFrame({
        "user_id": [1, 1, 2]})

    with pytest.raises(TypeError):
        remove_duplicates(df, cols="user_id")

def test_remove_duplicates_invalid_col_val():
    """
    Tests that Keyerror is raised when column does not 
    exist in dataframe.
    """
    
    df = pd.DataFrame({
        "user_id": [101, 101, 205],
        "city": ["Vancouver", "Vancouver", "Toronto"],
        "age": [22, 22, 30]
    })

    with pytest.raises(KeyError):
        remove_duplicates(df, cols=["user_id", "country"])

def test_remove_duplicates_missing_values():
    """
    Tests that rows with missing values in the same positions
    are treated as duplicates.
    """
    df = pd.DataFrame({
        "user_id": [101, 101],
        "city": [None, None],
        "age": [22, 22]})

    result = remove_duplicates(df)

    assert len(result) == 1

def test_remove_duplicates_keep_false():
    """
    Tests that keep=False removes all duplicate rows.
    """
    df = pd.DataFrame({
        "user_id": [101, 101, 101],
        "city": ["Vancouver", "Vancouver", "Vancouver"],
        "age": [22, 22, 22]
    })

    result = remove_duplicates(df, keep=False)

    assert result.empty
