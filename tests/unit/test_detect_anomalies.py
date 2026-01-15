"""Tests for detect_anomalies module.

This module contains tests for the detect_anomalies function,
covering expected use cases, edge cases, and error handling scenarios.

Test Categories
---------------
- Simple/Expected Use Cases: Normal DataFrame inputs with numerical columns
- Edge Cases: Empty DataFrames, no numeric column, DataFrames with NaN values 
or less than 3 data points.
- Abnormal/Error Cases: Invalid output paths, missing required columns

"""
import pytest
import pandas as pd
from src.data_fixr.detect_anomalies import detect_anomalies

@pytest.fixture
def test_data():
    df = pd.DataFrame({
        'temperature': [20, 21, 22, 19, 98, 23],
        'humidity': [45, 50, 48, 52, 49, 200]
    })
    return df
  
    
def test_zscore_detection_method(test_data):
    result_df, pct = detect_anomalies(test_data, method='zscore')
    assert isinstance(result_df, pd.DataFrame)
    assert isinstance(pct, float)
    assert 'temperature_outlier' in result_df.columns
    assert 'humidity_outlier' in result_df.columns
    assert result_df.loc[4, 'temperature_outlier'] == True  # outliers are correctly identified
    assert result_df.loc[5, 'humidity_outlier'] == True     # outliers are correctly identified
    assert result_df.loc[0, 'temperature_outlier'] == False # checks that normal values are not marked as outliers
    assert result_df.loc[1, 'humidity_outlier'] == False    # checks that normal values are not marked as outliers 
    assert 0 <= pct <= 100 # percentage should be between 0 and 100
    
def test_iqr_detection_method():
    result_df, pct = detect_anomalies(df, method='iqr')
    assert isinstance(result_df, pd.DataFrame)
    assert isinstance(pct, float)
    assert 'temperature_outlier' in result_df.columns
    assert 'humidity_outlier' in result_df.columns
    assert result_df.loc[4, 'temperature_outlier'] == True  # outliers are correctly identified
    assert result_df.loc[5, 'humidity_outlier'] == True     # outliers are correctly identified
    assert result_df.loc[0, 'temperature_outlier'] == False # checks that normal values are not marked as outliers
    assert result_df.loc[1, 'humidity_outlier'] == False    # checks that normal values are not marked as outliers 
    assert 0 <= pct <= 100 # percentage should be between 0 and 100
    
