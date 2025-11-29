import numpy as np
from decision_tree import DecisionTree

# Simple dataset: Outlook (0=Sunny, 1=Overcast, 2=Rain), Temperature
X = np.array([
    [0, 85],  # Sunny → Yes
    [0, 80],  # Sunny → Yes
    [1, 83],  # Overcast → Yes
    [2, 70],  # Rain → No
    [2, 68],  # Rain → No
    [2, 65],  # Rain → No
])

# Labels: Play Tennis? (1 = Yes, 0 = No)
y = np.array([1, 1, 1, 0, 0, 0])

# Train the decision tree
clf = DecisionTree(max_depth=3) # how deep the tree can grow
# Depth 0 → root
# Depth 1 → children
# Depth 2 → grandchildren
clf.fit(X, y) # means -> Learn patterns in X that can correctly predict y

# Predict on the same dataset to test understanding
predictions = clf.predict(X) # Should ideally match y
# runs each sample through the trained decision tree,
# following feature-threshold decisions from the root down to a leaf,
# and returns the leaf’s stored class label for each sample

print("Predictions:", predictions)
print("Actual:     ", y)

accuracy = np.sum(predictions == y) / len(y)
print("Accuracy:", accuracy)
