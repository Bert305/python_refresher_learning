# Just run the file to train the model:
# python3 train_model_step2.py


# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Check if drive_log.csv exists
if not os.path.exists("drive_log.csv"):
    print("ERROR: drive_log.csv not found. Run log_data_step1.py first to generate training data.")
    exit(1)

df = pd.read_csv("drive_log.csv")

if len(df) == 0:
    print("ERROR: drive_log.csv is empty. Collect more data first.")
    exit(1)

if len(df) < 20:
    print(f"ERROR: Only {len(df)} samples found. Need at least 20 samples for training.")
    print("Run log_data_step1.py and collect more diverse driving data.")
    exit(1)

print(f"Loaded {len(df)} data samples")

X = df[["ultra_cm", "ir_left", "ir_right"]]
y = df["action"]

# Check for data balance
print("Action distribution:")
print(y.value_counts())

# Ensure we have at least 2 samples per class so stratified split works
class_counts = y.value_counts()
if class_counts.min() < 2:
    print("ERROR: Each action needs at least 2 samples to train reliably. Collect more data.")
    exit(1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = Pipeline([
    ("scaler", StandardScaler()),
    # Keep args minimal for older sklearn versions
    ("clf", LogisticRegression(max_iter=500, solver='lbfgs'))
])

model.fit(X_train, y_train)
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
print(f"Train accuracy: {train_accuracy:.4f}")
print(f"Test accuracy: {test_accuracy:.4f}")

joblib.dump(model, "car_policy.joblib")
print("Saved car_policy.joblib")
print("Ready to run run_policy_step3.py")