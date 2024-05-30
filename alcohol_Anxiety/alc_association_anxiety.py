import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Reading the datasheet from excel
df = pd.read_excel('docs.xlsx')

df_depression = df.iloc[ : , 30:35]

n_alc = df_depression[['LE_alc_consumption']]

n_depress = df_depression[['LE_anxiety']]

new_df_depression = pd.concat([n_alc, n_depress], axis='columns')

new_df_depression = new_df_depression[new_df_depression['LE_anxiety'] != ' ']

# Performing apriori algorithm on 2 columns of JSS_DATASET.xlsx, one column is the alc_consumption and other column is n_anxiety_233.

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

frequent_itemsets = apriori(new_df_depression, min_support=0.1, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.4)

name_mapping = {
    'LE_alc_consumption': 'Alcohol Consumption ',
    'LE_anxiety': 'Anxiety'
}

# Replacing original names with new names in antecedents and consequents columns
rules['antecedents'] = rules['antecedents'].apply(lambda x: {name_mapping.get(item, item) for item in x})
rules['consequents'] = rules['consequents'].apply(lambda x: {name_mapping.get(item, item) for item in x})

print("Association Rules:")
for index, row in rules.iterrows():
    antecedents = ', '.join(list(row['antecedents']))
    consequents = ', '.join(list(row['consequents']))
    support = row['support']
    confidence = row['confidence']
    lift = row['lift']

    print("Rule: " + antecedents + "-> " + consequents)
    print("Support: " + str(support))
    print("Confidence: " + str(confidence))
    print("Lift: " + str(lift))
    print("=====================================")

# Check if there's any rule with "Anxiety" as the antecedent and "Alcohol Consumption" as the consequent
anxiety_to_alcohol_rule = rules[(rules['antecedents'].apply(lambda x: 'Anxiety' in x)) & 
                                (rules['consequents'].apply(lambda x: 'Alcohol Consumption' in x))]

# If the rule exists, print it
if not anxiety_to_alcohol_rule.empty:
    print("Rule: Anxiety -> Alcohol Consumption")
    print("Support: " + str(anxiety_to_alcohol_rule['support'].values[0]))
    print("Confidence: " + str(anxiety_to_alcohol_rule['confidence'].values[0]))
    print("Lift: " + str(anxiety_to_alcohol_rule['lift'].values[0]))
else:
    print("No rule found for Anxiety -> Alcohol Consumption")

