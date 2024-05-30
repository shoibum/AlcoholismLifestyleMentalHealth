import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

df = pd.read_excel('docs.xlsx')

df_depression = df.iloc[ : , 26:40]

n_alc = df_depression[['LE_alc_consumption']]

n_depress = df_depression[['LE_anxiety']]

new_df_depression = pd.concat([n_alc, n_depress], axis='columns')

new_df_depression = new_df_depression[new_df_depression['LE_anxiety'] != ' ']
print(new_df_depression)

from scipy.stats import chi2_contingency

# Create a contingency table
contingency_table = pd.crosstab(new_df_depression['LE_alc_consumption'], new_df_depression['LE_anxiety'])

# Display the contingency table
print("Contingency Table:")
print(contingency_table)

# Perform chi-squared test
chi2, p, _, _ = chi2_contingency(contingency_table)

# Display the results
print("\nChi-squared value:", chi2)
print("p-value:", p)
