import pandas as pd
def detect_anomalies(df, method):
    """
    This function flags outliers in numeric columns using either the
    Z-score method or the IQR method.

    Outliers in a dataset can heavily impact our analysis negatively.
    This function helps to identify potential anomalies in numeric
    columns of a pandas DataFrame, whether the data is normally
    distributed or skewed.

    The function takes in a DataFrame, automatically identifies numeric
    columns, and applies the specified method to flag outliers. Each
    numeric column is analyzed independently to detect anomalous values.

    The z-score method is suitable for normally distributed data but
    sensitive to extreme outliers, while the IQR method is better for
    skewed distributions and robust to extreme values.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing numeric columns to analyze for anomalies.
        Non-numeric columns will be excluded from the analysis.
    method : str
        The anomaly detection method to use. Valid options are:

        - 'zscore' : For normally distributed data
        - 'iqr' : For skewed data or robust detection

    Returns
    -------
    tuple of (pd.DataFrame, float)
        result_df : pd.DataFrame
            A DataFrame containing the original numeric columns plus 
            additional boolean columns (named as '{column}_outlier') 
            indicating whether each value is an outlier. True indicates 
            an outlier, False indicates a normal value.
        outlier_percentage : float
            The percentage of outliers detected across all numeric columns,
            calculated as (total outliers / total values) * 100.

    Raises
    ------
    ValueError
        If method is not 'zscore' or 'iqr', or if any numeric column
        contains fewer than 3 data points, or if any numeric column
        contains NaN values.
    TypeError
        If df is not a pandas DataFrame or contains no numeric columns.

    Notes
    -----
    Z-score method:
        Identifies points that are more than 3 standard deviations away 
        from the mean. The z-score is calculated as: z = (x - mean) / std.
        A data point is flagged as an outlier if |z| > 3.

    IQR method:
        Uses the interquartile range to identify outliers. Calculates Q1 
        (25th percentile) and Q3 (75th percentile), then IQR = Q3 - Q1.
        A data point is flagged as an outlier if it falls below 
        Q1 - 1.5×IQR or above Q3 + 1.5×IQR.

    Assumptions:
        - Requires at least 3 data points per numeric column for
          meaningful analysis
        - Non-numeric columns are automatically excluded
        - Missing values (NaN) are not flagged as outliers

    Examples
    --------
    >>> import pandas as pd
    >>> # Create sample data with clear outliers
    >>> df = pd.DataFrame({
    ...     'temperature': [20, 21, 22, 19, 98, 23],
    ...     'humidity': [45, 50, 48, 52, 49, 200],
    ...     'location': ['A', 'B', 'C', 'D', 'E', 'F']
    ... })
    >>> result_df, pct = detect_anomalies(df, method='zscore')
    >>> print(result_df)
       temperature  humidity  temperature_outlier  humidity_outlier
    0           20        45                False             False
    1           21        50                False             False
    2           22        48                False             False
    3           19        52                False             False
    4           98        49                 True             False
    5           23       200                False              True
    >>> print(f"{pct:.1f}% of data points are outliers")
    16.7% of data points are outliers
    """
