import numpy as np # helps with numbers and math
import matplotlib.pyplot as plt # lets us draw charts and graphs
import pandas as pd # helps us organize and look at data in tables

# Google spreadsheet link: https://docs.google.com/spreadsheets/d/1UCzr-blVPeniy54ACmL9DciXGEYxk-Vdf2sHCAC_po8/edit?gid=618160176#gid=618160176
url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"

# grabbing the data from the URL
# and loading it into a pandas dataframe
df=pd.read_csv(url)


df.head() # Shows the first 5 rows of the dataframe
df.sample(5) # random sample of 5 rows
print(f"Entire dataset:\n{df.head(5)}") # print the first 5 rows of the dataframe
df.describe() # shows the statistics of the dataframe


# Making a small subset of the dataframe to work with
# We will use the following columns:
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','CO2EMISSIONS']]
cdf.sample(9) # random sample of 9 rows from the subset
# Plotting the data
print(f"Sample size dataset of what fields are being trained for the model:\n {cdf[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','CO2EMISSIONS']].head(9)}") # print the first 9 rows of the subset
print(f"x features:\n {cdf[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY']].head(3)}") # print the first 3 rows of the input features
print(f"y label:\n {cdf['CO2EMISSIONS'].head(3)}") # print the first 3 rows of the target variable
# This draws histograms (bar graphs) to show how often different values appear for each selected column.
viz = cdf[['CYLINDERS','ENGINESIZE','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
viz.hist() # Shows a histogram of the data
plt.show() # displays the histogram


# Scatter plot for FUELCONSUMPTION_COMB vs CO2EMISSIONS
# x = FUELCONSUMPTION_COMB, y = CO2EMISSIONS, color = blue
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("FUELCONSUMPTION_COMB") # The x-axis label
plt.ylabel("Emission") # The y-axis label
plt.show() # displays the scatter plot


# Scatter plot for ENGINESIZE vs CO2EMISSIONS
# x = ENGINESIZE, y = CO2EMISSIONS, color = blue
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size") # The x-axis label
plt.ylabel("Emission") # The y-axis label
plt.xlim(0,27) # Sets the x-axis limits
plt.show() # displays the scatter plot



# Scatter plot for CYLINDERS vs CO2EMISSIONS
# x = CYLINDERS, y = CO2EMISSIONS, color = blue
plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("CYLINDERS") # The x-axis label
plt.ylabel("CO2 Emission") # The y-axis label
plt.show() # displays the scatter plot




#-------------------------------------------------------------------------------------------------------------------------------------------# Splitting the data into training and testing sets
# This is a common practice in machine learning to evaluate the model's performance on unseen data.
# We will use 80% of the data for training and 20% for testing.
# Goal: Predict CO2 emissions based on engine size using linear regression.
# Extracting the 'ENGINESIZE' and 'CO2EMISSIONS' columns from the dataframe
# cdf is a subset of the original dataframe df, containing only the columns we are interested in.
# X is the input feature (engine size) and y is the target variable (CO2 emissions).


X = cdf[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY']].to_numpy()  # Extracting the ENGINESIZE, CYLINDERS, FUELCONSUMPTION_CITY, and FUELCONSUMPTION_HWY columns as a numpy array --> list of engine sizes, cylinders, and certain fuel consumption values
y = cdf['CO2EMISSIONS'].to_numpy() # Extracting the 'CO2EMISSIONS' column as a numpy array # --> list of CO2 emissions


# Break down the data into 2 parts for training and testing sets
from sklearn.model_selection import train_test_split
# train_test_split is a function that splits the data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Training data is 80% of the original data, and testing data is 20% of the original data.


type(X_train), np.shape(X_train), np.shape(X_train)

from sklearn import linear_model

# create a linear regression model --- Like drawing a straight line through the data points to predict CO2 emissions based on engine size.
regressor = linear_model.LinearRegression()

# train the model on the training data
# X_train is a 1-D array but sklearn models expect a 2D array as input for the training data, with shape (n_observations, n_features).
# So we need to reshape it. We can let it infer the number of observations using '-1'.

regressor.fit(X_train, y_train) # fit means learn from the training data.
# The fit method trains the model using the training data (X_train and y_train).

# Print the coefficients
# With multiple linear regression, we have multiple coefficients (one for each feature)
print ('Intercept: ',regressor.intercept_) # --> Intercept = the pollution when all features are 0.
print ('Coefficients: ', regressor.coef_) # --> Coefficients for ENGINESIZE, CYLINDERS, FUELCONSUMPTION_CITY, FUELCONSUMPTION_HWY



from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Use the predict method to make test predictions
y_test_ = regressor.predict(X_test) # This uses the trained model to predict CO2 emissions for the test data (X_test).
# The predict method takes the test data (X_test) and returns the predicted CO2 emissions (y_test_).



# Plotting the predicted values vs actual values
# Note: Since we have multiple features (ENGINESIZE, FUELCONSUMPTION_CITY, FUELCONSUMPTION_HWY),
# we'll plot predicted vs actual values directly instead of against a single feature
plt.scatter(y_test, y_test_, color='blue', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Perfect Prediction')
plt.xlabel("Actual CO2 Emissions")
plt.ylabel("Predicted CO2 Emissions")
plt.legend()
plt.title("Actual vs Predicted CO2 Emissions (Multiple Linear Regression)")
plt.show()
plt.scatter(X_test[:, 0], y_test, color='blue', label='Actual')
plt.scatter(X_test[:, 0], y_test_, color='red', label='Predicted')
plt.xlabel("Engine Size")
plt.ylabel("CO2 Emissions")
plt.legend()
plt.title("Actual vs Predicted CO2 Emissions")
plt.show()

# Plot residuals (difference between actual and predicted)
# Residuals are horizontal distances from the predicted values to the actual values often started at y=0
residuals = y_test - y_test_
plt.scatter(y_test_, residuals, color='green')
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.axhline(y=0, color='r', linestyle='--')
plt.title("Residual Plot")
plt.show()

# Print predicted vs actual values for the test set
print("Predicted CO2 emissions for the test set:", y_test_)
print("Actual CO2 emissions for the test set:", y_test)



# Evaluation of the model
# We will use the mean absolute error, mean squared error, root mean squared error, and R2-score to evaluate the model's performance.
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, y_test_)) # Mean Absolute Error (MAE) means calculating the average data point value: +- over under the ground truth data points.
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_test_)) # calculates the average squared difference between the actual and predicted values.
print("Root mean squared error: %.2f" % np.sqrt(mean_squared_error(y_test, y_test_))) # calculates the square root of the mean squared error, which gives us an idea of how far off our predictions are on average also going +- over under the ground truth data points.
print("R2-score: %.2f" % r2_score(y_test, y_test_)) # R2-score is a measure of how well the model fits the data. It ranges from 0 to 1, where 1 means perfect fit and 0 means no fit at all.
# if the engine size is 5, cylinders is 4, fuel consumption city is 10, and fuel consumption hwy is 8, the predicted CO2 emissions would be:
engine_size = 5
cylinders = 4
fuel_city = 10
fuel_hwy = 8
predicted_emission = regressor.predict(np.array([[engine_size, cylinders, fuel_city, fuel_hwy]])) # We need to reshape the input to be a 2D array with one row and four columns.
print(f"Predicted CO2 emissions for engine size {engine_size}L, cylinders {cylinders}, city fuel {fuel_city}, hwy fuel {fuel_hwy}: {predicted_emission[0]:.2f} g/km")