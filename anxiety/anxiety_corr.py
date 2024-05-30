import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#reading the datasheet from excel

df = pd.read_excel('docs.xlsx')

n_lifestyle = df[['LE_happy_lifestyle']]

n_anxiety = df[['LE_anxiety']]

new_df_anxiety = pd.concat([n_lifestyle, n_anxiety], axis='columns')

new_df_anxiety = new_df_anxiety[new_df_anxiety['LE_anxiety'] != ' ']

new_df_anxiety['LE_happy_lifestyle'] = pd.to_numeric(new_df_anxiety['LE_happy_lifestyle'], errors='coerce')

new_df_anxiety['LE_anxiety'] = pd.to_numeric(new_df_anxiety['LE_anxiety'], errors='coerce')

new_df_anxiety = new_df_anxiety.dropna()

# Display basic statistics to understand the data
print("Basic Statistics:")

print(new_df_anxiety.describe())

# Calculate the correlation coefficient
correlation = new_df_anxiety['LE_happy_lifestyle'].corr(new_df_anxiety['LE_anxiety'])

# Display the correlation coefficient
print(f"\nCorrelation between Anxiety and Lifestyle: {correlation}")
