import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

df = pd.read_excel('docs.xlsx')

df_depression = df.iloc[ : , 30:35]

n_alc = df_depression[['LE_alc_consumption']]

n_depress = df_depression[['LE_anxiety']]

new_df_depression = pd.concat([n_alc, n_depress], axis='columns')

new_df_depression = new_df_depression[new_df_depression['LE_anxiety'] != ' ']

new_df_depression['LE_anxiety'] = pd.to_numeric(new_df_depression['LE_anxiety'], errors='coerce')

new_df_depression = new_df_depression.dropna()


# Display basic statistics to understand the data
print("Basic Statistics:")

print(new_df_depression.describe())

# # Calculate the correlation coefficient
correlation = new_df_depression['LE_anxiety'].corr(new_df_depression['LE_alc_consumption'])

# Display the correlation coefficient
print(f"\nCorrelation between Alcohol Consumption and Anxiety: {correlation}")
