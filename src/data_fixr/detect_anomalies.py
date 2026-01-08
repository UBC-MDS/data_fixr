def detect_anomalies(df, method):
    """
    This function flags outliers in numeric columns using either the Z-score method or the IQR method.
    
    Outliers in a dataset can heavy impact our analysis negatively. This function helps to identify 
    potential anomalies in numeric columns of a Pandas DataFrame that is either Normally distributed 
    or skewed. It takes in a DataFrame, identifies numeric columns, and applies the specified method 
    to flag outliers. The z-score method is suitable for normally distributed data but sensitive to 
    extreme outliers, while the IQR method is better for Skewed distributions and robust to extreme 
    values. Furthermore, the Z-score method dentifies points that are X standard deviations away from 
    the mean. The IQR method identifies points that fall below Q1 - 1.5*IQR or above Q3 + 1.5*IQR.
    
Parameters
    ----------
   - df (pd.DataFrame): The Dataframe containing numeric columns to analyze for anomalies.
    method (Z-Score or IQR): The method to use for anomaly detection. Choose 'Z-Score' for normally
    distributed data or 'IQR' for skewed data.

    Returns
    -------
    - pd.DataFrame: A DataFramme with the same structure as the input DataFrame, but only 
        containing numeric columns with the outliers specified method and additional columns indicating that
        the outliers have been flagged with a boolean value (True for outlier).
    - float: The percentage of outliers detected across all numeric columns.
    """
    

    