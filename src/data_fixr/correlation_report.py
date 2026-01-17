
import pandas as pd

def correlation_report(df, method: str = "pearson"):
    """
    Compute pairwise correlations between numeric columns of a DataFrame.

    This function is intended for exploratory data analysis diagnostics without plotting.
    It computes pairwise correlations between numeric features and returns a long-format
    report table, where each row corresponds to a unique feature pair.

    Parameters
    ----------
    df: pandas.DataFrame
        Input pandas DataFrame containing the data to analyze.
    method: str, default: "pearson"
        Correlation method to use. Supported values are:
        - "pearson": linear correlation.
        - "spearman": rank-based correlation.
        - "kendall": rank-based correlation.

    Returns
    -------
    pandas.DataFrame
        A long-format correlation report with the following columns:
        - feature_1: name of the first feature
        - feature_2: name of the second feature
        - correlation: correlation value
        - abs_correlation: absolute value of the correlation

        Each row represents a unique pair of numeric features. Self-correlations
        and duplicate symmetric pairs are excluded.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame.
    ValueError
        If method is not one of the supported correlation methods.
        If fewer than two numeric columns are available for correlation.

    Notes
    -----
    - Only numeric columns are considered.
    - Missing values are handled according to pandas' correlation behavior.
    - This function does not generate plots or files.
    - The output is intended to be machine-readable and suitable for use in
      automated analysis or reporting pipelines.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "age": [20, 30, 40],
    ...     "income": [40000, 60000, 80000],
    ...     "score": [3, 2, 1],
    ... })
    >>> correlation_report(df, method="pearson")
      feature_1 feature_2  correlation  abs_correlation
    0       age    income          1.0              1.0
    1       age     score         -1.0              1.0
    2    income     score         -1.0              1.0

    """


    # Validating the Inputss

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")
    
    if method not in {"pearson", "spearman", "kendall"}:
        raise ValueError("method must be one of {'pearson', 'spearman', 'kendall'}.")

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        raise ValueError("At least two numeric columns are required for correlation.")
    
    corr_matrix = numeric_df.corr(method=method)

    records = []
    cols = corr_matrix.columns

    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            corr_value = corr_matrix.iloc[i, j]
            records.append({
                "feature_1": cols[i],
                "feature_2": cols[j],
                "correlation": corr_value,
                "abs_correlation": abs(corr_value),
            })


    result = pd.DataFrame.from_records(records,columns=["feature_1", "feature_2", "correlation", "abs_correlation"],)

    return result