# 🧠 Big-Picture Breakdown (How This Decision Tree Works)

This project includes a simple, fully custom implementation of a **Decision Tree Classifier**.
Below is a high-level overview of how the code works internally — useful for understanding the algorithm and for documenting the project.

---

## 🌳 Classes Overview

### **`Node`**

Represents a single node in the decision tree.

A node can be:

* **Decision Node**
  Contains:

  * `feature` — the index of the feature to split on
  * `threshold` — the numeric value used to decide left vs right
  * `left` — left subtree
  * `right` — right subtree

* **Leaf Node**
  Contains:

  * `value` — the final predicted class
  * No children

The method `is_leaf_node()` simply checks whether the node stores a `value`.

---

## 🌲 `DecisionTree` Class

The `DecisionTree` class is responsible for:

* **Training** the tree with `fit(X, y)`
* **Recursively building** the tree using `_grow_tree`
* **Finding the best splits** using entropy + information gain
* **Predicting** classes for new samples with `predict(X)`

This implementation supports **numeric features only**, and class labels are assumed to be integers (`0, 1, ...`).

---

# 🚀 Training Process Overview

Training follows this flow:

---

## 🔹 1. `fit(X, y)`

* Determines how many features to use per split (`n_features`)
* Starts building the tree by calling `_grow_tree(X, y)`

---

## 🔹 2. `_grow_tree(X, y, depth)`

This is the **recursive heart** of the algorithm.

Stopping conditions:

* Maximum depth reached
* All labels in this node are identical (pure node)
* Not enough samples to split further

If any condition is met:

* It creates a **leaf node** using the most common label in `y`.

Otherwise:

* Randomly selects a subset of features (`feat_idxs`)
* Finds the best possible split using `_best_split`
* Splits the dataset based on that threshold
* Recursively builds:

  * Left subtree
  * Right subtree
* Returns a **decision node** containing:

  * best feature
  * best threshold
  * left & right child nodes

---

## 🔹 3. `_best_split(X, y, feat_idxs)`

For each selected feature:

* For each unique value in that column:

  * Computes **information gain**

Chooses the split (feature + threshold) that yields the **highest information gain**.

---

## 🔹 4. `_information_gain(y, X_column, threshold)`

Computes:

1. **Parent entropy**
2. Splits dataset into left/right using the threshold
3. Computes **child entropies**
4. Computes information gain:

```
IG = H(parent) - (n_l/n * H(left) + n_r/n * H(right))
```

Higher information gain = better split.

---

## 🔹 5. `_entropy(y)`

Entropy formula:

```
H = -Σ p log(p)
```

Where `p` are the class label probabilities.
Used to measure how "mixed" a node is.

---

## 🔹 6. `_most_common_label(y)`

Returns the most frequent label in the current node.
Used when creating leaf nodes.

---

# 🔮 Prediction Process Overview

Prediction follows this flow:

---

## 🔹 7. `predict(X)`

Loops through each sample in `X` and calls `_traverse_tree`.

Returns a NumPy array of predictions.

---

## 🔹 8. `_traverse_tree(x, node)`

For a single sample:

* If `node` is a leaf → return its stored class label.
* Otherwise:

  * Check the node's feature + threshold
  * Follow the appropriate branch:

    * `<= threshold` → go left
    * `> threshold`  → go right

Continues recursively until it reaches a leaf node.

This mirrors how real decision trees classify new input samples:

> "Walk down the tree, following decisions, until hitting a leaf.
> That leaf's value is the prediction."

---
