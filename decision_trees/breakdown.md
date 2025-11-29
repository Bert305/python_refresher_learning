

## 📦 Dataset Loading & Configuration

```python
data = datasets.load_breast_cancer()
```

### Dataset Details

- **Source**: scikit-learn's built-in datasets
- **Purpose**: Binary classification problem (malignant vs benign breast cancer)
- **Features**: 30 numeric features computed from digitized images of breast mass
- **Target Classes**: 
    - 0 = Malignant (cancerous)
    - 1 = Benign (non-cancerous)
- **Total Samples**: 569 instances
- **Use Case**: Medical diagnosis - predicting whether a breast tumor is malignant or benign based on cell characteristics

### Data Split Configuration

- **Training Set**: 80% of the data
- **Test Set**: 20% of the data
- **Random State**: 1234 (for reproducibility)

---



# Decision Tree Classifier for Breast Cancer Diagnosis

A custom implementation of a Decision Tree algorithm from scratch, applied to the Wisconsin Breast Cancer dataset for binary classification of tumors as malignant or benign.

---

## 📋 Project Overview

This project demonstrates a ground-up implementation of a Decision Tree classifier without relying on scikit-learn's built-in decision tree model. The implementation uses fundamental machine learning concepts to build a tree-based classifier capable of medical diagnosis prediction.

---

## 🎯 Dataset

**Breast Cancer Wisconsin Dataset**
- **Source**: scikit-learn's built-in datasets (`load_breast_cancer()`)
- **Purpose**: Binary classification (malignant vs benign breast cancer)
- **Features**: 30 numeric features computed from digitized images of breast mass
- **Target Classes**: 
  - 0 = Malignant (cancerous)
  - 1 = Benign (non-cancerous)
- **Total Samples**: 569 instances
- **Feature Types**: Real-valued features including radius, texture, perimeter, area, smoothness, etc.

---

## 🗂️ Project Structure

```
decision_trees/
├── decision_tree.py    # Custom DecisionTree class implementation
├── train.py           # Training script and model evaluation
├── breakdown.md       # Dataset details and project notes
└── README.md         # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Install the required dependencies:

```bash
pip install numpy scikit-learn
```

### Running the Model

1. Ensure you're in the `decision_trees` directory
2. Run the training script:

```bash
python train.py
```

The script will:
- Load the breast cancer dataset
- Split data into training (80%) and testing (20%) sets
- Train the decision tree with max depth of 10
- Evaluate and print the accuracy on the test set

---

## 🔧 Implementation Details

### DecisionTree Class

The custom `DecisionTree` class (in `decision_tree.py`) implements:
- **Splitting Logic**: Information gain or Gini impurity-based splits
- **Tree Building**: Recursive tree construction
- **Pruning**: Max depth parameter to prevent overfitting
- **Prediction**: Traversal-based classification

### Training Configuration

```python
clf = DecisionTree(max_depth=10)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
```

- **Max Depth**: 10 levels (prevents overfitting)
- **Train/Test Split**: 80/20 ratio
- **Random State**: 1234 (for reproducibility)

---

## 📊 Model Evaluation

The model is evaluated using a simple accuracy metric:

```python
accuracy = number_of_correct_predictions / total_predictions
```

Expected accuracy range: ~90-95% on the test set

---

## 🧠 Key Concepts

- **Decision Trees**: Non-parametric supervised learning method
- **Binary Classification**: Two-class prediction problem
- **Feature Splitting**: Selecting optimal features at each node
- **Overfitting Prevention**: Using max_depth parameter
- **Information Gain**: Measure of how well a feature separates classes

---

## 📚 Learning Objectives

- Understand decision tree algorithm from first principles
- Implement tree-based learning without libraries
- Apply machine learning to medical diagnosis
- Practice model evaluation and metrics
- Gain experience with scikit-learn datasets

---

## 🤝 Contributing

This is a learning project. Feel free to fork and experiment with different:
- Splitting criteria (Gini vs Entropy)
- Tree depths
- Pruning strategies
- Feature engineering techniques

---

## 📝 License

This project is part of a Python learning repository and is available for educational purposes.

---

## 🔗 Related Projects

Part of the [Python Refresher Learning](../) repository covering various Python and ML concepts.