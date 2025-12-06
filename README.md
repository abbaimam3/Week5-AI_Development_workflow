# AI Development Workflow Assignment

This directory contains the submission for the "AI Development Workflow" assignment.

## Directory Structure

*   **`AI_Workflow_Report.md`**: The main report containing:
    *   Part 1: Short Answer Questions (Student Dropout Problem).
    *   Part 2: Case Study (Hospital Readmission).
    *   Part 3: Critical Thinking (Ethics & Trade-offs).
    *   Part 4: Reflection & Workflow Diagram.
*   **`hospital_readmission_metrics.py`**: Python script for Part 2 that generates synthetic data, trains a Logistic Regression model, and outputs performance metrics.
*   **`requirements.txt`**: List of Python dependencies.

## Setup & Installation

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

### Run the Model Metrics Script
To see the model training and evaluation metrics for the Hospital Case Study:
```bash
python hospital_readmission_metrics.py
```
This will output the Classification Report and a Confusion Matrix.
