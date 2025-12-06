import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# ==========================================
# Part 2: Case Study Application - Model Development
# ==========================================

# 1. Generate Synthetic Data (Hypothetical)
np.random.seed(42)
n_samples = 1000

data = {
    'age': np.random.randint(18, 90, n_samples),
    'num_prior_admissions': np.random.randint(0, 5, n_samples),
    'chronic_conditions': np.random.randint(0, 3, n_samples),
    'days_in_hospital': np.random.randint(1, 14, n_samples),
    'discharged_to_home': np.random.choice([0, 1], n_samples, p=[0.2, 0.8]) # 1=Home, 0=Rehab/Other
}

df = pd.DataFrame(data)

# Target: Readmitted within 30 days (1=Yes, 0=No)
# Logic: Older patients with more prior admissions are more likely to be readmitted
def assign_readmission(row):
    score = (row['age'] / 90) + (row['num_prior_admissions'] * 0.3) + (row['chronic_conditions'] * 0.2)
    if row['discharged_to_home'] == 0: score += 0.2
    
    # Add some randomness
    score += np.random.normal(0, 0.2)
    
    return 1 if score > 1.2 else 0

df['readmitted'] = df.apply(assign_readmission, axis=1)

print("Dataset Head:")
print(df.head())
print("-" * 30)

# 2. Model Development
X = df.drop('readmitted', axis=1)
y = df['readmitted']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model (Logistic Regression - chosen for interpretability)
model = LogisticRegression()
model.fit(X_train, y_train)

# 3. Evaluation
y_pred = model.predict(X_test)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Visualize Confusion Matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix: Patient Readmission")
plt.show()

print("\nAnalysis:")
print("Precision: The ability not to label a healthy patient as 'at risk'.")
print("Recall: The ability to find all the patients who actually need help.")
print("In this healthcare context, we typically prioritize Recall to ensure no high-risk patient is missed.")
