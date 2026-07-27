import pandas as pd
from scipy import stats

def churn_rate_by(df, column):
    """Calculate the churn rate (%) for each category of a given column."""
    table = pd.crosstab(df[column], df['Churn'], normalize='index') * 100
    return table.round(2)

def run_ttest(feature, group_yes, group_no, feature_name, alpha=0.05):
    """
    Run a two-sample t-test and print the results.
    
    Parameters:
        feature (str): Column name to test
        group_yes (DataFrame): Churners group
        group_no (DataFrame): Non-churners group
        feature_name (str): Nice name for printing
        alpha (float): Significance level
    """
    stat, p_value = stats.ttest_ind(
        group_yes[feature], 
        group_no[feature], 
        equal_var=False
    )
    
    print(f"\n{feature_name}")
    print(f"t-statistic: {stat:.4f}")
    print(f"p-value: {p_value:.4e}")
    
    if p_value <= alpha:
        print(f"→ Reject H0: There is a significant difference in mean {feature_name}.")
    else:
        print(f"→ Fail to reject H0: No significant difference found.")
    
    return stat, p_value