def detect_anomalies(df, method):
    """
    This function flags outliers in numeric columns using either the Z-score method or the IQR method.
    
    Outliers in a dataset can heavy impact our analysis negatively. This function helps to identify 
    potential anomalies in numeric columns of a Pandas DataFrame that is either Normally distributed 
    or skewed. 
    