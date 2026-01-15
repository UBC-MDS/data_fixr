"""
"""

import pandas as pd
import pytest
from data_fixr.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """
    Checking expected output of function.
    """
    df = pd.DataFrame({
        "id": [1, 1, 2],
        "value": ["A", "A", "B"]
    })

    result = remove_duplicates(df)

    assert len(result) == 2
    assert result["id"].tolist() == [1, 2]

def test_remove_duplicates_subset_keep_last():
    df = pd.DataFrame({
        "id": [1, 1, 2],
        "value": ["A", "B", "C"]
    })

    result = remove_duplicates(df, cols=["id"], keep="last")

    assert result.iloc[0]["value"] == "B"

def test_remove_duplicates_with_report():
    df = pd.DataFrame({
        "id": [1, 1, 2]
    })

    cleaned, report = remove_duplicates(df, report=True)

    assert isinstance(report, dict)
    assert report["total_rows"] == 3
    assert report["duplicate_rows"] == 1
    assert report["rows_removed"] == 1
    assert report["strategy"] == "first"

# def test_remove_duplicates_invalid_df_type():
#     with pytest.raises(TypeError):
#         remove_duplicates([1, 2, 3])

# def test_remove_duplicates_invalid_keep():
#     df = pd.DataFrame({"a": [1, 1]})

#     with pytest.raises(ValueError):
#         remove_duplicates(df, keep="middle")

#maybe also add invalid col type check