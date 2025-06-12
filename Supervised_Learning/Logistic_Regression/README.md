# Logistic Regression

## Overview

This project provides a complete implementation of **logistic regression from scratch**

Logistic regression is a foundational machine learning algorithm for **binary classification**, where the target variable is either 0 or 1. In this notebook, we:

- Explain logistic regression mathematically
- Build the model from scratch in Python
- Train and evaluate it using a custom-generated dataset
- Visualize the decision boundary
- Track the loss during training

---

## What Is Logistic Regression?

Logistic regression models the **probability** that a given input belongs to a particular class using a **sigmoid function**.

### 1. Linear Combination (Logit Function)

We first compute a weighted sum of the inputs:

z = w · x + b


Where:
- `x` is the input vector  
- `w` is the weight vector  
- `b` is the bias term

### 2. Sigmoid Activation Function

The sigmoid function transforms `z` into a probability between 0 and 1:

ŷ = 1 / (1 + e^(-z))


This output is interpreted as the probability that the instance belongs to **class 1**.

### 3. Binary Cross-Entropy Loss

The loss function used is **binary cross-entropy**, which penalizes incorrect predictions:

L = -(1/N) * Σ [ y * log(ŷ) + (1 - y) * log(1 - ŷ) ]


Where:
- `y` is the true label  
- `ŷ` is the predicted probability  
- `N` is the number of training samples

### 4. Gradient Descent

The weights and bias are updated to minimize the loss:

w_j ← w_j - α * ∂L/∂w_j
b ← b - α * ∂L/∂b


Where `α` is the learning rate.

### 5. Prediction Rule

After training, predictions are converted to class labels using a threshold:

ŷ ≥ 0.5 → class 1
ŷ < 0.5 → class 0


---

## Dataset

We used a **synthetic dataset** generated for this project, specifically crafted for logistic regression. It features:

- Two features (`x1`, `x2`)
- Binary labels (0 or 1)
- A clear nonlinear boundary

Using a synthetic dataset avoids complications from noise or imbalance and enables effective visualization of decision boundaries.

---

## Results

- The model was trained using **stochastic gradient descent**.
- Evaluation included:
  - Accuracy
  - Precision, Recall, F1-score
  - Confusion matrix
- We **visualized the decision boundary** to illustrate how logistic regression separates the two classes.
- We also **plotted the training loss across epochs**, showing convergence.

---

## Libraries Used

- `NumPy`
- `Matplotlib`
- `scikit-learn` (for evaluation metrics and data generation)

---