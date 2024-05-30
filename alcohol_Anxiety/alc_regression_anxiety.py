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

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt


# Split the data into training and testing sets
X = new_df_depression['LE_alc_consumption'].values.reshape(-1, 1)  # Independent variable (feature)
y = new_df_depression['LE_anxiety']     # Dependent variable (target)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
lr = LinearRegression()

# Fit the model to the training data
lr.fit(X_train, y_train)

# Make predictions on the test data
y_pred = lr.predict(X_test)

# Evaluate the model
print("Regression Model Evaluation:")
print("Coefficients:", lr.coef_)
print("Intercept:", lr.intercept_)
print("Mean Absolute Error:", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred, squared=False))

# Visualize the regression line
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Alcohol Consumption')
plt.ylabel('Anxiety')
plt.title('Linear Regression: Alcohol Consumption vs. Anxiety')
plt.show()
