import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#reading the datasheet from excel

df = pd.read_excel('docs.xlsx')

df_mental_health = df.iloc[ : , 30 : 35]

df_mental_health = df_mental_health[df_mental_health['LE_happy_lifestyle'] != ' ']

new_df = df_mental_health[['LE_happy_lifestyle', 'LE_depression']]

new_df['LE_happy_lifestyle'] = pd.to_numeric(new_df['LE_happy_lifestyle'], errors='coerce')

new_df['LE_depression'] = pd.to_numeric(new_df['LE_depression'], errors='coerce')

new_df = new_df.dropna()

# Display basic statistics to understand the data
print("Basic Statistics:")
print(new_df.describe())

# Calculate the correlation coefficient
correlation = new_df['LE_happy_lifestyle'].corr(new_df['LE_depression'])

# Display the correlation coefficient
print(f"\nCorrelation between Lifestyle and Depression: {correlation}")
