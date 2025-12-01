
# Important article on building basic ML Model with Python
# https://towardsdatascience.com/building-a-basic-machine-learning-model-in-python-d7cca929ee62/


# Load Dataset

# "Delaney of solubility in water" - benchmark dataset used in machine learning for predicting the water solubility of compounds.
# It contains structural information and water solubility data for 1128 compounds


# solubility - means the ability to be dissolved, especially in water

import pandas as pd
import numpy as np

# Load the dataset from a CSV file
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/delaney_solubility_with_descriptors.csv')


# Display the first few rows of the dataset
print(df.head())

# Display the shape of the dataset
print(f"Dataset shape: {df.shape}")

# Display the columns of the dataset
print(f"Dataset columns: {df.columns.tolist()}")

# Display the data types of each column
print(f"Dataset data types:\n{df.dtypes}")


#------------------------------------------------------------


# The logS column represents the y-variable, meaning the variable you want to predict.
# The other columns represent the x-variables, meaning the variables you will use to make predictions

# So when we build a machine learning model, we will use the x-variables to predict the y-variable.

# y = f(x)

# Data separation as X and Y
# We want to split the dataframe into X (features) and y (target variable):

X = df.drop(columns=['logS'])
y = df['logS']

# Display the first few rows of X and y
print(f"X:\n{X.head()}")
print(f"y:\n{y.head()}")


# Data Splitting
# Next is to split the dataset into training and testing sets.
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# >>>>>>>80% of 1144 rows is 915 rows for training and 229 rows for testing<<<<<<<
print(f"X_train shape: {X_train.shape}") # 915 rows, 4 columns
print(f"X_test shape: {X_test.shape}") # 229 rows, 4 columns
print(f"y_train shape: {y_train.shape}") # 915 rows --- Looks like the same percentage as X_train
print(f"y_test shape: {y_test.shape}") # 229 rows --- Looks like the same percentage as X_test

# We use the training set to build the model and the testing set to serve as a unknown data to evaluate its performance.

#-------------------------------------------------------------------
# Model Training
# Now we can train a machine learning model using the training data.

from sklearn.linear_model import LinearRegression
# Create a Linear Regression model

lr = LinearRegression()
# Fit the model to the training data
lr.fit(X_train, y_train) # So 80% of data is used to train the model

print("Model training complete.")

y_lr_train_pred = lr.predict(X_train) # 80% of data for training --> feature column values
y_lr_test_pred = lr.predict(X_test) # 20% of data for testing --> feature column values

print(f"y_lr_train_pred shape: {y_lr_train_pred}") # 915 rows of predictions  --> 80% of 1144 rows
print(f"y_lr_test_pred shape: {y_lr_test_pred}") # 229 rows of predictions  --> 20% of 1144 rows


# Compare the predicted values with the actual values in the training set

from sklearn.metrics import mean_squared_error, r2_score 

mse_train = mean_squared_error(y_train, y_lr_train_pred)
r2_train = r2_score(y_train, y_lr_train_pred)
lr_rmse = np.sqrt(mse_train)

lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)



# print(f"Training set - Mean Squared Error: {mse_train}") # Printing the MSE for training set
# print(f"Training set - R^2 Score: {r2_train}") # Printing the R^2 score for training set
# print(f"Test set - Mean Squared Error: {lr_test_mse}")
# print(f"Test set - R^2 Score: {lr_test_r2}")



# Create comparison DataFrames for Linear Regression
lr_train_comparison = pd.DataFrame({
    'Actual': y_train,
    'Predicted': y_lr_train_pred
})

lr_test_comparison = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_lr_test_pred
})

print("\nLinear Regression - Training Set Comparison:")
print(lr_train_comparison)
print("\nLinear Regression - Test Set Comparison:")
print(lr_test_comparison)

#----------------------------------------------------

# Random Forest Regression
# Random Forest - is an ensemble method that combines multiple decision trees to improve prediction accuracy and control over
# This model builds many mini decision trees and averages their predictions.
#**********
# A decision tree - is a flowchart-like structure used for both decision-making and machine learning. 
# It visually represents possible outcomes of a series of choices, helping individuals or organizations weigh different options based on costs, probabilities, and benefits. 
# In machine learning, decision trees are used for classification and regression tasks, helping to predict outcomes based on data patterns.
#**********

from sklearn.ensemble import RandomForestRegressor


rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(X_train, y_train)

y_rf_train_pred = rf.predict(X_train)
y_rf_test_pred = rf.predict(X_test)


from sklearn.metrics import mean_squared_error, r2_score

rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2 = r2_score(y_train, y_rf_train_pred)
rf_rmse = np.sqrt(rf_train_mse)

rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2 = r2_score(y_test, y_rf_test_pred)


# Create comparison DataFrames for Random Forest
rf_train_comparison = pd.DataFrame({
    'Actual': y_train,
    'Predicted': y_rf_train_pred
})

rf_test_comparison = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_rf_test_pred
})

print("\nRandom Forest - Training Set Comparison:")
print(rf_train_comparison)
print("\nRandom Forest - Test Set Comparison:")
print(rf_test_comparison)


# what's the difference between Linear Regression and Random Forest Regression?

# Linear Regression is a simple model that assumes a linear relationship between the features and the target variable.


# Linear Regression vs Random Forest Regression

# Model Comparison - Test Set Only
model_comparison = pd.DataFrame({
    'Actual': y_test,
    'LR Predicted': y_lr_test_pred,
    'RF Predicted': y_rf_test_pred
})
print("\nModel Comparison - Test Set:")
print(model_comparison)

# print the accuracy metrics for Random Forest versus Linear Regression
print(f"Random Forest - Test set - Mean Squared Error: {rf_test_mse:.4f}") # Printing the MSE for test set - predicted vs actual
print(f"Random Forest - Test set - R^2 Score: {rf_test_r2:.4f}") # Printing the R^2 score for test set - the accuracy of the model
print(f"Random Forest - Test set - Root Mean Squared Error: {rf_rmse:.4f}") # Printing the RMSE for test set - how far off the predictions are from ground truth on average
print(f"Linear Regression - Test set - Mean Squared Error: {lr_test_mse:.4f}") # Printing the MSE for test set - predicted vs actual
print(f"Linear Regression - Test set - R^2 Score: {lr_test_r2:.4f}") # Printing the R^2 score for test set - the accuracy of the model
print(f"Linear Regression - Test set - Root Mean Squared Error: {lr_rmse:.4f}") # Printing the RMSE for test set - how far off the predictions are from ground truth on average


# The Mean Squared Error (MSE) is a measure of how close the predicted values are to the actual values.
# A lower MSE indicates a better fit of the model to the data.
# R^2 Score shows how well the model explains it's accuracy.
# A Root Mean Squared Error (RMSE) is the square root of the MSE, showing how far predictions are from ground truth on average




# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of seaborn
sns.set(style="whitegrid")
# Create a scatter plot for the actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_lr_test_pred, color='blue', label='Linear Regression', alpha=0.5)
plt.scatter(y_test, y_rf_test_pred, color='red', label='Random Forest', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2, label='Perfect Prediction')
plt.xlabel('Actual Values') # LogS values from the test set
plt.ylabel('Predicted Values') # Predicted LogS values from both models
plt.title('Actual vs Predicted Values') # Scatter plot of actual vs predicted values
plt.legend()
plt.show()
# This scatter plot shows the actual values of the target variable (y_test) on the x-axis and the predicted values from both models on the y-axis.



# Random Forest (Test set)-----

# MSE: 1.0521
# R²: 0.7584
# RMSE: 1.0282


# Linear Regression (Test set)------

# MSE: 0.9991
# R²: 0.7706
# RMSE: 1.0070

# ✔ Linear Regression performed slightly better than Random Forest

# Because it has:

# Lower MSE → better

# Lower RMSE → better

# Higher R² Score → more variance explained

# ✔ R² Score comparison:

# Random Forest R² = 0.7584

# Linear Regression R² = 0.7706

# This means:

# LR explains 77.06% of the variability in solubility

# RF explains 75.84%

# Linear Regression is the winner, but only by a small margin.