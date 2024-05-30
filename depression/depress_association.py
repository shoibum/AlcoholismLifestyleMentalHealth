import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#reading the datasheet from excel
df = pd.read_excel('docs.xlsx')

df_mental_health = df.iloc[ : , 30 : 35]
# #print(df_mental_health)

df_mental_health = df_mental_health[df_mental_health['LE_happy_lifestyle'] != ' ']

new_df = df_mental_health[['LE_happy_lifestyle', 'LE_depression']]
# #print(len(df_mental_health))

# performing apriori algorithm on 2 columns of JSS_DATASET.xlsx, one column is the alc_consumption and other column is mental_health_for_alc.

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

frequent_itemsets = apriori(new_df, min_support=0.1, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.4)

name_mapping = {
    'LE_happy_lifestyle': 'Lifestyle',
    'LE_depression': 'Depression'
}

# Replace original names with new names in antecedents and consequents columns
rules['antecedents'] = rules['antecedents'].apply(lambda x: {name_mapping.get(item, item) for item in x})
rules['consequents'] = rules['consequents'].apply(lambda x: {name_mapping.get(item, item) for item in x})
# Print the association rules
print("Association Rules:")
for index, row in rules.iterrows():
    antecedents = ', '.join(list(row['antecedents']))
    consequents = ', '.join(list(row['consequents']))
    support = row['support']
    confidence = row['confidence']
    lift = row['lift']

    print("Rule: " + antecedents + " -> " + consequents)
    print("Support: " + str(support))
    print("Confidence: " + str(confidence))
    print("Lift: " + str(lift))
    print("=====================================")
