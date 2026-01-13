import pandas as pd
import pytest

from data_fixr.correlation_report import correlation_report

    

def test_correlation_report_non_numeric_columns():

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

    



def test_correlation_report_non_dataframe_raises():
    """ If df is not dataframe, We pass"""
    with pytest.raises(TypeError):
        correlation_report(["not", "a", "df"])