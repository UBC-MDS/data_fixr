import pandas as pd
import numpy as np

def fill_missing_values(df, method):
    """
    This function fills missing values (NaN) in numeric columns of a
    pandas DataFrame using the specified imputation method.

    Missing values can distort statistical analyses and machine learning
    models. This function provides common strategies for imputing missing
    values depending on the nature of the data distribution.

    The function automatically identifies numeric columns and applies
    the selected method independently to each numeric column. 
    
    Non-numeric columns are left unchanged.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing missing values to be imputed.
        Non-numeric columns will be excluded from imputation.
    method : str
        The imputation method to use. Valid options are:
        - 'mean'   : Replace NaN with column mean (suitable for symmetric data)
        - 'median' : Replace NaN with column median (robust to outliers)
        - 'mode'   : Replace NaN with column mode

    Returns
    -------
    tuple of (pd.DataFrame, float)
        result_df : pd.DataFrame
            A DataFrame with missing values filled in numeric columns.
        missing_percentage : float
            The percentage of missing values filled across all numeric
            columns, calculated as:
            (number of filled values / total numeric values) * 100.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame or if no numeric columns are present.
    ValueError
        If method is not one of the 3 supported options.

    Notes
    -----
    - Imputation is applied column-wise.
    - Non-numeric columns are not modified.
    - If a column contains all NaN values, it is left unchanged.
    - If multiple modes exist, the first mode returned by pandas is used.
    
    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'age': [25, 30, None, 28],
    ...     'income': [50000, None, 52000, None],
    ...     'city': ['A', 'B', 'C', 'D']
    ... })
    >>> result_df, missing_percentage = fill_missing_values(df, method='median')
    >>> print(result_df)
        age   income city
    0  25.0  50000.0    A
    1  30.0  51000.0    B
    2  28.0  52000.0    C
    3  28.0  51000.0    D
    >>> print(f"{missing_percentage:.1f}% of values were filled.")
    37.5% of values were filled.
    """