import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#reading the datasheet from excel

df = pd.read_excel('docs.xlsx')

df_mental_health = df.iloc[ : , 30 : 35]

df_mental_health = df_mental_health[df_mental_health['LE_happy_lifestyle'] != ' ']

new_df = df_mental_health[['LE_happy_lifestyle', 'LE_anxiety']]


from scipy.stats import chi2_contingency

# Create a contingency table
contingency_table = pd.crosstab(new_df['LE_happy_lifestyle'], new_df['LE_anxiety'])

# Display the contingency table
print("Contingency Table:")
print(contingency_table)

# Perform chi-squared test
chi2, p, _, _ = chi2_contingency(contingency_table)

# Display the results
print("\nChi-squared value:", chi2)
print("p-value:", p)
