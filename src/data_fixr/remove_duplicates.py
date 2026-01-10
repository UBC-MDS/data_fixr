def remove_duplicates(df, cols=None, keep='first', report=False):
    """
    Identifies and removes duplicate rows for a given dataframe. Optionally, returns a summary
    report of the duplicate rows, including number of rows after removing duplicates, total number
    of rows remaining and the keep strategy used.

    Parameters
    ----------
    df: pandas.DataFrame
        Input DataFrame to check for and remove duplicate rows from.

    cols: list of str or None, default=None 
        Optional parameter. Subset of column names to consider when identifying duplicates. 
        If None, all columns are used to identify duplicate rows. 
    
    keep : {"first", "last", False}, default="first"
        Optional parameter. Determines which duplicate rows to keep:
        - "first": keep the first occurrence and remove subsequent duplicates
        - "last": keep the last occurrence and remove earlier duplicates
        - False: remove all duplicate rows
    
    report : bool, default=False
        Optional parameter. If True, returns a summary report containing information about duplicate rows.
    
    Returns
    -------
    pandas.DataFrame
        The input DataFrame with duplicate rows removed.
    dict, optional
        If `report` is True, a dictionary summarizing duplicate
        detection results is returned. The dictionary output includes:
        - total_rows: int, number of rows in the original input DataFrame
        - duplicate_rows: int, number of duplicate rows detected
        - rows_removed: int, number of rows removed
        - strategy: keep strategy used to remove duplicates, if any
        - cols_used: list of str or None(i.e. all), columns used for duplicate detection
    
    Raises 
    ------
    TypeError
        If df is not a pandas DataFrame.
    KeyError
        If any column in cols does not exist in the DataFrame.
    ValueError
        If keep is not one of {"first", "last", False}.
    
    Notes
    -----
    - This function is intended for early-stage data cleaning and EDA processes.
    - Missing values are considered in duplicate detection. If two or more rows 
    contain missing values in the same places, they are still considered duplicates.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "id": [1, 1, 2, 3],
    ...     "value": ["A", "A", "B", "C"]
    ... })

    Remove duplicate rows using all columns:

    >>> cleaned_df = remove_duplicates(df)
    >>> cleaned_df
       id value
    0   1     A
    2   2     B
    3   3     C

    Remove duplicates based on some specified columns and return a summary report:

    >>> cleaned_df, report = remove_duplicates(df,cols=["id"],keep="last",report=True)
    >>> cleaned_df
       id value
    1   1     A
    2   2     B
    3   3     C

    >>> report
    {'total_rows': 4,
    'duplicate_rows': 1,
    'rows_removed': 1,
    'subset_used': ['id']}
    """