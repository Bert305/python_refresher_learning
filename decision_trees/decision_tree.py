import numpy as np  # Import NumPy for numerical operations and array manipulation
from collections import Counter  # Import Counter to easily count label frequencies


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        # 'feature' is the index of the feature (column) used to split at this node
        self.feature = feature
        # 'threshold' is the numeric value used to decide left vs right branch
        self.threshold = threshold
        # 'left' is the left child node (subtree where feature <= threshold)
        self.left = left
        # 'right' is the right child node (subtree where feature > threshold)
        self.right = right
        # 'value' is the class label if this is a leaf node; otherwise None
        self.value = value
        
    def is_leaf_node(self):
        # A node is a leaf if it has a 'value' set (no further splitting)
        # If the tree has reached a leaf node, STOP and return the 
        # A leaf node is the end of a branch — it contains a final class label
        return self.value is not None


class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        # Minimum number of samples required to split a node
        self.min_samples_split = min_samples_split
        # Maximum depth of the tree (how many levels it can grow)
        self.max_depth = max_depth
        # Number of features to consider when looking for the best split
        # (If None, it will use all features)
        self.n_features = n_features
        # Root node of the decision tree (will be set after training)
        self.root = None

    def fit(self, X, y):
        # If n_features is not set, use all features; otherwise use the given number
        # X.shape[1] = number of columns (features) in X
        self.n_features = X.shape[1] if not self.n_features else min(X.shape[1], self.n_features)
        # Build the tree recursively starting from the root
        self.root = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        # Get number of samples (rows) and number of features (columns)
        n_samples, n_feats = X.shape
        # Get how many unique class labels exist in this subset of y
        n_labels = len(np.unique(y))

        # ----- Stopping conditions for recursion -----
        # Stop if:
        # - We've reached max_depth
        # - All samples belong to the same class (n_labels == 1)
        # - There are fewer samples than min_samples_split
        if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):
            # If we stop, create a leaf node with the most common label
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)

        # Randomly select a subset of features to consider for splitting
        feat_idxs = np.random.choice(n_feats, self.n_features, replace=False)

        # ----- Find the best split among the selected features -----
        best_feature, best_thresh = self._best_split(X, y, feat_idxs)

        # ----- Split the data into left and right subsets -----
        # X[:, best_feature] = the column for the chosen feature
        # best_thresh = the threshold value for splitting
        left_idxs, right_idxs = self._split(X[:, best_feature], best_thresh)
        # Recursively grow the left subtree using the samples in left_idxs
        left = self._grow_tree(X[left_idxs, :], y[left_idxs], depth + 1)
        # Recursively grow the right subtree using the samples in right_idxs
        right = self._grow_tree(X[right_idxs, :], y[right_idxs], depth + 1)
        # Return a non-leaf node with info about how to split and its children
        return Node(best_feature, best_thresh, left, right)

    def _best_split(self, X, y, feat_idxs):
        # Initialize best information gain as -1 (so any positive gain will be better)
        best_gain = -1
        # Initialize the best feature index and threshold as None
        split_idx, split_threshold = None, None

        # Loop over each candidate feature index
        for feat_idx in feat_idxs:
            # Extract the column for this feature
            X_column = X[:, feat_idx]
            # Get all unique values in this column as possible thresholds
            thresholds = np.unique(X_column)

            # Try splitting on each possible threshold
            for thr in thresholds:
                # Calculate information gain if we split on this threshold
                gain = self._information_gain(y, X_column, thr)

                # If this gain is better than what we have so far, update best split
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_threshold = thr

        # Return the feature index and threshold that gave the best information gain
        return split_idx, split_threshold

    def _information_gain(self, y, X_column, threshold):
        # Compute entropy of the parent (current) node labels
        parent_entropy = self._entropy(y)

        # Split the indices of samples based on the threshold
        left_idxs, right_idxs = self._split(X_column, threshold)

        # If either side is empty, this split is useless (no gain)
        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0
        
        # Total number of samples in this node
        n = len(y)
        # Number of samples in left and right child
        n_l, n_r = len(left_idxs), len(right_idxs)
        # Entropy of the left child labels
        e_l = self._entropy(y[left_idxs])
        # Entropy of the right child labels
        e_r = self._entropy(y[right_idxs])
        # Weighted average entropy of the children
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r

        # Information gain = parent_entropy - weighted child_entropy
        information_gain = parent_entropy - child_entropy
        # Return how much uncertainty (entropy) was reduced by this split
        return information_gain

    def _split(self, X_column, split_thresh):
        # Get indices of samples where feature value <= threshold (go to left)
        left_idxs = np.argwhere(X_column <= split_thresh).flatten()
        # Get indices of samples where feature value > threshold (go to right)
        right_idxs = np.argwhere(X_column > split_thresh).flatten()
        # Return both sets of indices
        return left_idxs, right_idxs

    def _entropy(self, y):
        # Count how many times each label appears (assuming labels are 0,1,2,...)
        hist = np.bincount(y)
        # Convert counts to probabilities by dividing by total number of samples
        ps = hist / len(y)
        # Compute entropy = -sum(p * log(p)) for all p > 0
        return -np.sum([p * np.log(p) for p in ps if p > 0])

    def _most_common_label(self, y):
        # Count occurrences of each label using Counter
        counter = Counter(y)
        # Get the label with the highest count (most_common(1) returns list [(label, count)])
        value = counter.most_common(1)[0][0]
        # Return that most frequent label
        return value

    def predict(self, X):
        # For each sample x in X, traverse the tree starting at root and collect predictions
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        # If current node is a leaf, return its stored class value
        # If the tree has reached a leaf node, STOP and return the predictioned class label (0 or 1)
        # A leaf node is the end of a branch — it contains a final class label - like 0 or 1 for our binary classification
        if node.is_leaf_node():
            return node.value

        # Otherwise, check the feature at this node for the given sample x
        # If x's feature value is <= threshold, go down the left branch
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        # If x's feature value is > threshold, go down the right branch
        return self._traverse_tree(x, node.right)

