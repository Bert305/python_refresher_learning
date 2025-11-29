


from sklearn.model_selection import train_test_split  # For splitting into train/test sets
import numpy as np
from decision_tree import DecisionTree  # Your custom DecisionTree implementation

# ---------------------------------------
# 1. Create a simple Titanic-like dataset
# ---------------------------------------
# Feature 1: sex (0 = male, 1 = female)
# Feature 2: age (in years)
#
# Each row: [sex, age]
# This is our input data representing X_test
X = np.array([
    [0, 22],  # male,   22 → did not survive
    [1, 38],  # female, 38 → survived
    [1, 26],  # female, 26 → survived
    [1, 35],  # female, 35 → survived
    [0, 35],  # male,   35 → did not survive
    [0, 8],   # male,    8 → survived (child)
    [0, 54],  # male,   54 → did not survive
    [1, 2],   # female,  2 → survived (child)
    [0, 19],  # male,   19 → did not survive
    [1, 17],  # female, 17 → survived
])

# This is the ground truth labels for whether each passenger survived representing y_test
# Target: survived? (0 = No, 1 = Yes)
y = np.array([
    0,  # male,   22
    1,  # female, 38
    1,  # female, 26
    1,  # female, 35
    0,  # male,   35
    1,  # male,    8
    0,  # male,   54
    1,  # female,  2
    0,  # male,   19
    1,  # female, 17
])

# ---------------------------------------
# 2. Split into train and test sets
# ---------------------------------------
# test_size=0.3 → 30% test (3 samples), 70% train (7 samples)
# random_state ensures the split is reproducible
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
# test_size = 0.3   
# → 30% of the full dataset goes to X_test and y_test
# → 70% goes to X_train and y_train
# X_test → test input features
# y_test → test ground truth labels

)



    #                               Original Dataset (10 samples)
    #                               /                            \
    #                              /                              \
    #  70% to Training Set                                      30% to Test Set
    #  X_train (7 rows - input dataset sex & age)                X_test (3 rows - input dataset sex & age)
    #  y_train (7 labels - ground truth yes or no survived)      y_test (3 labels - ground truth yes or no survived)
    
    
    
#     | Passenger | X (row of features) | Meaning of Features   | y (label) | Survival Meaning |
# | --------- | ------------------- | --------------------- | --------- | ---------------- |
# | 1         | **[0, 22]**         | male,   age 22        | **0**     | did NOT survive  |
# | 2         | **[1, 38]**         | female, age 38        | **1**     | survived         |
# | 3         | **[1, 26]**         | female, age 26        | **1**     | survived         |
# | 4         | **[1, 35]**         | female, age 35        | **1**     | survived         |
# | 5         | **[0, 35]**         | male,   age 35        | **0**     | did NOT survive  |
# | 6         | **[0, 8]**          | male,   age 8 (child) | **1**     | survived         |
# | 7         | **[0, 54]**         | male,   age 54        | **0**     | did NOT survive  |
# | 8         | **[1, 2]**          | female, age 2 (child) | **1**     | survived         |
# | 9         | **[0, 19]**         | male,   age 19        | **0**     | did NOT survive  |
# | 10        | **[1, 17]**         | female, age 17        | **1**     | survived         |



# ---------------------------------------
# 3. Create and train the Decision Tree
# ---------------------------------------
# max_depth limits how deep the tree can grow (to keep it simple)
clf = DecisionTree(max_depth=3)
clf.fit(X_train, y_train)

# ---------------------------------------
# 4. Make predictions on the test set (30% of data)
# ---------------------------------------
predictions = clf.predict(X_test)
# If the tree has reached a leaf node, STOP and return the predicted class label (0 or 1)
# A leaf node is the end of a branch — it contains a final class label - like 0 or 1 for our binary classification



# ---------------------------------------
# 5. Define an accuracy function (same style as before)
# ---------------------------------------
def accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)

acc = accuracy(y_test, predictions)

print("y_test (true labels -> ground truth dataset):     ", y_test)
print("predictions (model):      ", predictions)
print("Accuracy on test set:", acc)



# y_test (ground truth): [0 1 1]
# predictions:           [0 1 0] --> TN, TP, FN
# accuracy:              0.6666...


# | Index | True (y_test) | Predicted | Result Type             |
# | ----- | ------------- | --------- | ----------------------- |
# | 0     | 0             | 0         | **TN** (True Negative)  |
# | 1     | 1             | 1         | **TP** (True Positive)  |
# | 2     | 1             | 0         | **FN** (False Negative) |





# ---------------------------------------
# 6. Try some new hypothetical passengers
# ---------------------------------------
new_passengers = np.array([
    [0, 30],  # male,   30
    [1, 30],  # female, 30
    [0, 6],   # male,    6 (child)
    [1, 6],   # female,  6 (child)
])

new_preds = clf.predict(new_passengers)
print("\nNew passengers (sex, age):")
print("sex (0 = male, 1 = female)")
print(new_passengers)
print("Predicted survival (0=No, 1=Yes):", new_preds)
