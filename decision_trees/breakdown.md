# Decision Tree Implementation

A custom implementation of a decision tree classifier built from scratch using NumPy.

## Overview

This implementation uses information gain (based on entropy) to recursively build a binary decision tree for classification tasks.

## Classes

### `Node`

Represents a single node in the decision tree.

**Properties:**
- **Decision node**: Contains `feature`, `threshold`, `left`, and `right` child nodes
- **Leaf node**: Contains `value` (the predicted class) with no children

**Methods:**
- `is_leaf_node()`: Returns `True` if the node is a leaf (i.e., has a `value` set)

### `DecisionTree`

The main classifier class that builds and uses the decision tree.

**Methods:**
- `fit(X, y)`: Trains the tree on feature matrix `X` and labels `y`
- `predict(X)`: Returns class predictions for input samples `X`

## Training Process

### 1. `fit(X, y)`
- Determines the number of features to consider at each split
- Initiates recursive tree building via `_grow_tree(X, y)`

### 2. `_grow_tree(X, y, depth)`
Recursively builds the tree by:

**Stopping conditions:**
- Maximum depth reached
- All labels are identical
- Insufficient samples to split further

**If stopping:** Creates a leaf node with the most common label

**If continuing:**
- Randomly selects a subset of features to consider
- Finds the best split using `_best_split()`
- Splits the data and recursively grows left and right subtrees
- Returns a decision node with split information and child nodes

### 3. `_best_split(X, y, feat_idxs)`
- Evaluates each candidate feature
- Tests each unique value as a potential threshold
- Computes information gain for each split
- Returns the feature and threshold with maximum information gain

### 4. `_information_gain(y, X_column, threshold)`
Calculates information gain using:

```
IG = H(parent) - (n_left/n × H(left) + n_right/n × H(right))
```

Where higher IG indicates a better split.

### 5. `_entropy(y)`
- Counts label frequencies using `np.bincount`
- Converts counts to probabilities
- Returns `-Σ p log p` for non-zero probabilities

## Prediction Process

### 1. `predict(X)`
- Iterates through each sample in `X`
- Calls `_traverse_tree()` for each sample
- Returns predictions as a NumPy array

### 2. `_traverse_tree(x, node)`
Traverses the tree recursively:
- **If leaf node:** Returns `node.value`
- **If decision node:** 
  - Compares `x[node.feature]` to `node.threshold`
  - Recurses left if `<= threshold`, otherwise recurses right

## Usage

```python
# Create and train the tree
tree = DecisionTree(max_depth=10)
tree.fit(X_train, y_train)

# Make predictions
predictions = tree.predict(X_test)
```
