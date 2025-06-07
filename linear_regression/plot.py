import numpy as np # helps with numbers and math
import matplotlib.pyplot as plt # lets us draw charts and graphs
import pandas as pd # helps us organize and look at data in tables


url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"

# grabbing the data from the URL
# and loading it into a pandas dataframe
df=pd.read_csv(url)


df.head() # Shows the first 5 rows of the dataframe
df.sample(5) # random sample of 5 rows

df.describe() # shows the statistics of the dataframe


# Making a small subset of the dataframe to work with
# We will use the following columns:
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.sample(9) # random sample of 9 rows from the subset
# Plotting the data


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


X = cdf['ENGINESIZE'].to_numpy()  # Extracting the 'ENGINESIZE' column as a numpy array --> list of engine sizes
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

regressor.fit(X_train.reshape(-1, 1), y_train) # fit means learn from the training data.
# The fit method trains the model using the training data (X_train and y_train).

# Print the coefficients
# with simple linear regression there is only one coefficient, here we extract it from the 1 by 1 array.
print ('Intercept: ',regressor.intercept_) # --> Coefficient = how much pollution goes up when engine size goes up.
print ('Coefficients: ', regressor.coef_[0]) # --> Intercept = the pollution when engine size is 0.

# Engine size vs CO2 Emissions
# This is a scatter plot of the training data with the regression line.
# X_train is the engine size, y_train is the CO2 emissions.
plt.scatter(X_train, y_train,  color='blue')
plt.plot(X_train, regressor.coef_ * X_train + regressor.intercept_, '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")


from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Use the predict method to make test predictions
y_test_ = regressor.predict(X_test.reshape(-1,1)) # This uses the trained model to predict CO2 emissions for the test data (X_test).
# The predict method takes the test data (X_test) and returns the predicted CO2 emissions (y_test_).

# Evaluation
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, y_test_)) # calculates the average absolute difference between the actual and predicted values.
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_test_)) # calculates the average squared difference between the actual and predicted values.
print("Root mean squared error: %.2f" % np.sqrt(mean_squared_error(y_test, y_test_))) # calculates the square root of the mean squared error, which gives us an idea of how far off our predictions are on average.
print("R2-score: %.2f" % r2_score(y_test, y_test_)) # R2-score is a measure of how well the model fits the data. It ranges from 0 to 1, where 1 means perfect fit and 0 means no fit at all.
# if the engine size is 5, the predicted CO2 emissions would be:
engine_size = 5
predicted_emission = regressor.predict(np.array([[engine_size]])) # We need to reshape the input to be a 2D array with one row and one column.
print(f"Predicted CO2 emissions for engine size {engine_size}L: {predicted_emission[0]:.2f} g/km")