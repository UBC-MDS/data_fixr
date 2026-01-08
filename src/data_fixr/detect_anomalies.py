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
        If method is not 'zscore' or 'iqr'
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
        - Requires at least 3 data points per numeric column for meaningful analysis
        - Non-numeric columns are automatically excluded
        - Missing values (NaN) are not flagged as outliers
    
    
    """   
