# Logistic Regression

## Overview

This project provides a complete implementation of **logistic regression from scratch**.

Logistic regression is a foundational algorithm for **binary classification**, where the goal is to predict whether an input belongs to class 0 or class 1. In this notebook, we:

- Explain logistic regression mathematically
- Build the model using NumPy
- Train and evaluate it on a synthetic dataset
- Visualize the decision boundary
- Track the loss during training to observe convergence

---

## What Is Logistic Regression?

Logistic regression models the **probability** that an input belongs to a certain class using a **sigmoid activation function**. It maps real-valued inputs into the (0, 1) range.

### 1. Linear Combination (Logit Function)
\[
z = \mathbf{w} \cdot \mathbf{x} + b
\]

Where:
- `x` is the input feature vector  
- `w` is the weight vector  
- `b` is the bias

### 2. Sigmoid Activation Function
\[
\hat{y} = \frac{1}{1 + e^{-z}}
\]

This output is interpreted as the **probability that the instance belongs to class 1**.

### 3. Binary Cross-Entropy Loss
\[
L = -\frac{1}{N} \sum \left[ y \log(\hat{y}) + (1 - y) \log(1 - \hat{y}) \right]
\]

Where:
- `y` is the true label  
- `ŷ` is the predicted probability  
- `N` is the number of samples

### 4. Gradient Descent

Weights and bias are updated using the gradient of the loss function:

\[
w_j \leftarrow w_j - \alpha \cdot \frac{\partial L}{\partial w_j}, \quad b \leftarrow b - \alpha \cdot \frac{\partial L}{\partial b}
\]

### 5. Prediction Rule

Class prediction is determined using a threshold:

- If ŷ ≥ 0.5 → class 1  
- If ŷ < 0.5 → class 0

---

## Dataset

We used a **synthetic dataset** designed for clarity and interpretability in binary classification tasks. It contains:

- Two input features (`x1`, `x2`)
- Binary labels (0 or 1)
- A moderate degree of linear separability, generated from two 2D Gaussian distributions

This clean setup allows us to:
- Focus on understanding the model behavior
- Visualize the decision boundary in 2D
- Avoid distractions like noise, imbalance, or missing data

---

## Results

- The model was trained using **stochastic gradient descent** on mini-batches.
- Performance was evaluated using:
  - Accuracy
  - Precision, Recall, and F1-score
  - Confusion matrix
- The **decision boundary** was visualized to show how the model separates the two classes.
- The **training loss** was plotted over time, showing convergence to a minimum.

---

## Interpretation and Real-World Relevance

Although trained on synthetic data, this project demonstrates the essential logic behind logistic regression: how it learns a linear boundary in feature space and assigns class probabilities.

In real-world applications, logistic regression is widely used because it is:
- Fast and easy to train
- Probabilistically interpretable
- Resilient with small datasets

Examples include:
- Medical diagnosis (e.g., disease vs. no disease)
- Credit scoring (default vs. no default)
- Email filtering (spam vs. not spam)

---

## Limitations

- **Linear Separability**: Logistic regression struggles with datasets that are not linearly separable without advanced feature engineering.
- **Synthetic Simplicity**: The dataset lacks real-world complexity such as noise, class imbalance, or missing values.
- **No Regularization**: Our scratch implementation lacks techniques like L1/L2 regularization, which are critical for robustness in practice.

Despite these, the model offers clear educational value and is still used professionally as a fast, transparent baseline.

---