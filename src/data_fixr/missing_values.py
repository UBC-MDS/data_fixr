import pandas as pd
import numpy as np

def missing_values(df, method="median"):
    """
    This function fills missing values (NaN) in a pandas DataFrame using
    column-appropriate imputation strategies.

    This function imputes missing values in both numeric and categorical
    columns. Numeric columns are filled using a user-specified method
    (mean, median, or mode), while categorical (non-numeric) columns are
    automatically filled using mode imputation.
    
    Missing values can distort statistical analyses and machine learning
    models. This function provides common strategies for imputing missing
    values depending on the nature of the data distribution.

    The function identifies numeric and non-numeric columns and applies
    imputation independently to each column. 

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing missing values to be imputed.
    method : str, default="median"
        The imputation method to use for numeric columns. 
        Valid options are:
        - 'mean'   : Replace NaN with column mean (suitable for symmetric data)
        - 'median' : Replace NaN with column median (robust to outliers)
        - 'mode'   : Replace NaN with column mode

        Categorical (non-numeric) columns always use mode imputation 
        regardless of the selected method.

    Returns
    -------
    (pd.DataFrame, float)
        result_df : pd.DataFrame
            A DataFrame with missing values filled in both numeric and
            categorical (non-numeric) columns.
        filled_percentage : float
            The percentage of total DataFrame values that were originally
            missing and have been filled, calculated as:
            (number of filled values / number of total values) * 100.

            Columns containing only NaN values are left unchanged and do not
            contribute any filled values to this percentage. 

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame.
    ValueError
        If method is not one of the 3 supported numeric options.

    Notes
    -----
    - Numeric columns are imputed using the specified method.
    - Categorical (non-numeric) columns are imputed using mode.
    - Imputation is applied column-wise.
    - Columns containing all NaN values are left unchanged and do not
      affect the filled percentage.
    - If multiple modes exist (for both numeric and categorical columns), 
      the first mode returned by pandas is used.
    - The original DataFrame is not modified; a copy is returned. 
    - The filled percentage includes values filled in both numeric 
    and categorical (non-numeric) columns.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'age': [25, 30, np.nan, 28],
    ...     'income': [50000, np.nan, 52000, np.nan],
    ...     'city': ['A', 'B', np.nan, 'B']
    ... })
    >>> result_df, filled_percentage = missing_values(df, method='median')
    >>> print(result_df)
        age   income city
    0  25.0  50000.0    A
    1  30.0  51000.0    B
    2  28.0  52000.0    B
    3  28.0  51000.0    B
    >>> print(f"{filled_percentage:.1f}% of values were filled.")
    33.3% of values were filled.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if method not in ["mean", "median", "mode"]:
        raise ValueError("Method must be one of: 'mean', 'median', 'mode'.")

    result_df = df.copy()

    if df.empty:  # Empty dataframe
        return result_df, 0.0

    total_missing_before = result_df.isna().sum().sum()
    total_values = result_df.size

    # Separate numeric and non-numeric columns
    numeric_cols = result_df.select_dtypes(include=[np.number]).columns
    categorical_cols = result_df.select_dtypes(exclude=[np.number]).columns

    # Impute numeric columns
    for col in numeric_cols:
        if result_df[col].isna().all():
            continue  # Leave all-NaN columns unchanged

        if method == "mean":
            fill_value = result_df[col].mean()
        elif method == "median":
            fill_value = result_df[col].median()
        elif method == "mode":
            mode_result = result_df[col].mode()
            fill_value = mode_result.iloc[0] if len(mode_result) > 0 else np.nan

        result_df[col] = result_df[col].fillna(fill_value)

    # Impute categorical columns using mode
    for col in categorical_cols:
        if result_df[col].isna().all():
            continue  # Leave all-NaN columns unchanged

        mode_result = result_df[col].mode()
        fill_value = mode_result.iloc[0] if len(mode_result) > 0 else np.nan
        result_df[col] = result_df[col].fillna(fill_value)

    # Compute filled percentage
    total_missing_after = result_df.isna().sum().sum()
    filled_values = total_missing_before - total_missing_after
    filled_percentage = (filled_values / total_values) * 100

    return result_df, filled_percentage