from sklearn import datasets  # Import scikit-learn datasets module to load sample datasets
from sklearn.model_selection import train_test_split  # Import function to split data into train/test sets
import numpy as np  # Import NumPy for numerical operations
from decision_tree import DecisionTree  # Import the custom DecisionTree class we wrote


# Load the breast cancer dataset from scikit-learn
data = datasets.load_breast_cancer()
# 'data.data' is the feature matrix X, 'data.target' is the label vector y
X, y = data.data, data.target

# Split data into training and test sets
# test_size=0.2 means 20% of data goes to test set, 80% to training
# random_state=1234 sets a seed so the split is reproducible

# The breast cancer dataset has 569 samples total
# So with the test size = 0.2
# 569 * 0.2 = 113.8, approximately 114 samples will be in the test set, y_test
# The remaining 455 samples will be in the training set, y_train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
) # X_test contains 114 rows
  # X_train contains 455 rows

# Create an instance of our DecisionTree classifier with max depth = 10
clf = DecisionTree(max_depth=10)
# Train (fit) the decision tree on the training data
clf.fit(X_train, y_train)
# Use the trained model to predict labels for the test set
predictions = clf.predict(X_test)

def accuracy(y_test, y_pred):
    # Compute accuracy as: number of correct predictions / total predictions
    return np.sum(y_test == y_pred) / len(y_test)

# Calculate accuracy of our model on the test data
acc = accuracy(y_test, predictions)
# Print the accuracy value
print(acc)
print(f"Accuracy: {acc * 100:.2f}%") 
        # Initialize variables to track the best feature, threshold, and information gain

# The output shows that your Decision Tree classifier achieved:

# 91.23% accuracy (or 0.9122807017543859 in decimal form)

# This means:

# Out of 114 test samples (20% of 569 total samples), the model correctly predicted 104 cases
# The model misclassified approximately 10 cases
# What this accuracy indicates:

# Good Performance: 91.23% is a solid accuracy for a custom-implemented decision tree on medical diagnosis
# Clinical Context: In breast cancer diagnosis, this means the model correctly identifies whether a tumor is malignant or benign in about 9 out of 10 cases
        
correct = np.sum(y_test == predictions)
total = len(y_test)
incorrect = total - correct

print("Correct predictions:", correct) # Print the number of correct predictions
print("Incorrect predictions:", incorrect) # Print the number of incorrect predictions
print("Actual labels:", y_test) # Print the actual labels
print("Total samples:", total) # Print the total number of samples
print("Accuracy:", correct / total) # Print the accuracy of the model

# Clinical Context: In breast cancer diagnosis, this means the model correctly identifies whether a tumor is malignant or benign in about 9 out of 10 cases