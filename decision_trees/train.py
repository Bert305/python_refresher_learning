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
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

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
        
