"""
Statistical testing functions for access-to-care research.

Includes hypothesis tests, effect size calculations, and
survival analysis utilities for referral-to-admission timelines.
"""

import numpy as np
import pandas as pd
from scipy import stats


def cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:
    """
    Calculate Cohen's d effect size between two groups.
    """
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std if pooled_std > 0 else 0.0


def compare_groups_continuous(df: pd.DataFrame, value_col: str, group_col: str) -> dict:
    """
    Compare a continuous variable across groups.
    Uses Mann-Whitney U for 2 groups, Kruskal-Wallis for 3+.
    """
    groups = df[group_col].dropna().unique()
    group_data = [df[df[group_col] == g][value_col].dropna().values for g in groups]

    result = {
        "n_groups": len(groups),
        "groups": {str(g): {"n": len(d), "median": float(np.median(d)), "mean": float(np.mean(d))} for g, d in zip(groups, group_data)},
    }

    if len(groups) == 2:
        stat, p = stats.mannwhitneyu(group_data[0], group_data[1], alternative="two-sided")
        result.update({"test": "Mann-Whitney U", "statistic": float(stat), "p_value": float(p),
                        "effect_size_d": float(cohens_d(group_data[0], group_data[1]))})
    elif len(groups) > 2:
        stat, p = stats.kruskal(*group_data)
        result.update({"test": "Kruskal-Wallis H", "statistic": float(stat), "p_value": float(p)})

    return result


def compare_groups_categorical(df: pd.DataFrame, outcome_col: str, group_col: str) -> dict:
    """
    Compare a categorical outcome across groups using chi-square test.
    """
    ct = pd.crosstab(df[group_col], df[outcome_col])
    chi2, p, dof, _ = stats.chi2_contingency(ct)
    return {"test": "Chi-square", "statistic": float(chi2), "p_value": float(p),
            "degrees_of_freedom": int(dof), "contingency_table": ct.to_dict()}


def summarize_wait_times(df: pd.DataFrame, days_col: str = "days_to_admission", group_col: str = None) -> pd.DataFrame:
    """
    Summarize referral-to-admission wait times with key percentiles.
    """
    def agg(x):
        return pd.Series({
            "n": len(x), "mean_days": x.mean(), "median_days": x.median(),
            "p75_days": x.quantile(0.75), "p90_days": x.quantile(0.90), "std_days": x.std()
        })
    if group_col:
        return df.groupby(group_col)[days_col].apply(agg).round(1)
    return df[days_col].apply(agg).round(1)
