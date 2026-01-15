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
    """Fixture to provide a sample DataFrame for testing."""
    df = pd.DataFrame({
        'temperature': [20, 21, 22, 19, 98, 23],
        'humidity': [45, 50, 48, 52, 49, 200]
    })
    return df

@pytest.fixture
def skewed_data():
    """Fixture providing skewed data for IQR method testing."""
    df = pd.DataFrame({
        'income': [25000, 28000, 30000, 32000, 35000, 38000, 40000, 42000, 45000, 500000],  
        'response_time': [1.2, 1.5, 1.8, 2.0, 2.3, 2.5, 2.8, 3.0, 3.5, 45.0],  # Right-skewed
        'age': [22, 25, 27, 30, 32, 35, 38, 40, 42, 95]  # Mostly normal with one outlier
    })
    return df
  
 # Simple/Expected Use Cases   
def test_zscore_detection_method(test_data):
    """Test z-score anomaly detection method."""
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
    
def test_iqr_detection_method(skewed_data):
    """Test IQR anomaly detection method on skewed data."""
    result_df, pct = detect_anomalies(skewed_data, method='iqr')
    assert isinstance(result_df, pd.DataFrame)
    assert isinstance(pct, float)
    # Check correct column names from skewed_data fixture
    assert 'income_outlier' in result_df.columns 
    assert 'response_time_outlier' in result_df.columns 
    assert 'age_outlier' in result_df.columns 
    # Check extreme outliers are flagged (index 9 has all outliers)
    assert result_df.loc[9, 'income_outlier'] == True  # outliers are correctly identified
    assert result_df.loc[9, 'response_time_outlier'] == True  # outliers are correctly identified
    assert result_df.loc[9, 'age_outlier'] == True  # outliers are correctly identified
    # Check normal values are not flagged
    assert result_df.loc[0, 'income_outlier'] == False
    assert 0 <= pct <= 100  # percentage should be between 0 and 100
 
def test_mixed_dataframe(test_data):
    """Test that function processes only numeric columns and ignores non-numeric columns."""
    # Add non-numeric columns to the test data
    df = test_data.copy()
    df['location'] = ['A', 'B', 'J', 'D', 'E', 'Z']
    df['city'] = ['NYC', 'LA', 'SF', 'Boston', 'Seattle', 'Miami']
    
    result_df, pct = detect_anomalies(df, method='zscore')
    
    assert 'temperature_outlier' in result_df.columns
    assert 'humidity_outlier' in result_df.columns
    assert 'location_outlier' not in result_df.columns
    assert 'city_outlier' not in result_df.columns
    assert 'location' in result_df.columns
    assert 'city' in result_df.columns
    assert result_df.loc[4, 'temperature_outlier'] == True
    assert result_df.loc[5, 'humidity_outlier'] == True
    
 # Edge Cases
 # Empty DataFrame, no numeric columns, DataFrames with NaN values or less than 3 data points.   
def test_empty_dataframe():
    """Test that empty DataFrame raises appropriate error."""
    df = pd.DataFrame()  # Completely empty
    with pytest.raises(TypeError, match="empty DataFrame"):
        detect_anomalies(df, method='zscore')

def test_empty_numeric_columns():
    """Test DataFrame with columns but zero rows raises error."""
    df = pd.DataFrame({'temperature': [], 'humidity': []})
    with pytest.raises(ValueError, match="No data points found for numeric columns"):
        detect_anomalies(df, method='zscore')
        
def test_insufficient_datapoints(test_data):
    """Test DataFrame with fewer than 3 data points raises error."""
    df_first_two = test_data.iloc[:2]  # Only 2 rows
    with pytest.raises(ValueError, match="Not enough data points for numeric columns"):
        detect_anomalies(df_first_two, method='zscore')
        

def test_dataframe_with_only_non_numeric_columns():
    """Test DataFrame with only non-numeric data."""
    df = pd.DataFrame({
        'name': ['A', 'B', 'C'],
        'location': ['X', 'Y', 'Z']
    })
    with pytest.raises(TypeError, match="no numeric columns found"):
        detect_anomalies(df, method='zscore')
        
def test_dataframe_with_nan_values():
    """Test DataFrame with NaN values in numeric columns raises error."""
    df = pd.DataFrame({
        'temperature': [20, 21, None, 19, 98, 23],
        'humidity': [45, None, 48, 52, 49, 200]
    })
    with pytest.raises(ValueError, match="contains NaN values"):
        detect_anomalies(df, method='zscore')
        
def test_no_outliers_detected_zscore():
    """Test case where no outliers exist using Z-score method."""
    df = pd.DataFrame({
        'values': [10, 11, 12, 13, 14, 15]  # No extreme values
    })
    result_df, pct = detect_anomalies(df, method='zscore')
    assert (result_df['values_outlier'] == False).all()
    assert pct == 0.0

def test_no_outliers_detected_iqr():
    """Test case where no outliers exist using IQR method."""
    df = pd.DataFrame({
        'values': [10, 11, 12, 13, 14, 15]  # No extreme values
    })
    result_df, pct = detect_anomalies(df, method='iqr')
    assert (result_df['values_outlier'] == False).all()
    assert pct == 0.0

def test_outlier_percentage_calculation(test_data):
    """Verify percentage calculation is accurate."""
    result_df, pct = detect_anomalies(test_data, method='zscore')
    total_outliers = result_df['temperature_outlier'].sum() + result_df['humidity_outlier'].sum()
    total_values = len(test_data) * 2  # 6 rows × 2 numeric columns = 12 values
    expected_pct = (total_outliers / total_values) * 100
    assert abs(pct - expected_pct) < 0.01

def test_columns_analyzed_separately():
    """Test that each numeric column is analyzed independently."""
    df = pd.DataFrame({
        'col1': [1, 2, 3, 100],     # Outlier at index 3
        'col2': [10, 20, 200, 40]   # Outlier at index 2
    })
    result_df, pct = detect_anomalies(df, method='iqr')
    # Verify outlier indices
    assert result_df.loc[3, 'col1_outlier'] == True
    assert result_df.loc[2, 'col2_outlier'] == True
    # Verify non-outlier indices
    assert result_df.loc[3, 'col2_outlier'] == False  # col2 index 3 is normal
    assert result_df.loc[2, 'col1_outlier'] == False  # col1 index 2 is normal
        
# Abnormal/Error Cases: Invalid method parameter
def test_invalid_method_parameter(test_data):
    """Test that invalid method parameter raises ValueError."""
    with pytest.raises(ValueError, match="method must be either 'zscore' or 'iqr'"):
        detect_anomalies(test_data, method='invalid_method')    

def test_non_dataframe_input():
    """Test that non-DataFrame input raises TypeError."""
    non_df_input = [1, 2, 3, 4, 5]
    with pytest.raises(TypeError, match="Input must be a pandas DataFrame"):
        detect_anomalies(non_df_input, method='zscore')    
    with pytest.raises(TypeError, match="Input must be a pandas DataFrame"):
        detect_anomalies(non_df_input, method='iqr')
        