# Supervised Learning

This folder explores a range of **supervised machine learning methods**—from foundational algorithms like linear and logistic regression to advanced ensemble models and neural networks. Each notebook applies a different algorithm to real-world survey data, primarily from the **General Social Survey (GSS)** and **Big Five Personality Inventory**, to predict psychological traits, performance outcomes, or political ideology.

**Supervised learning** refers to training a model using data that includes both **features (inputs)** and **labels (outputs)**. The goal is for the algorithm to learn a function that maps inputs to known outcomes, so that it can make accurate predictions on new, unseen data.

- A **label** is the correct answer or target associated with each observation.
- Examples of supervised tasks include:
  - Predicting student performance from study time (regression)
  - Predicting political ideology from demographic traits (classification)
  - Classifying personality type from survey responses (classification)

Supervised learning is most effective when we have a **clear target variable** and enough labeled examples to learn from.

---

## Learning Objectives

- Understand how supervised models work in theory and practice
- Apply classification and regression algorithms to sociopsychological data
- Evaluate model performance using appropriate metrics
- Visualize predictions and decision logic for interpretability

---

## Datasets

### 1. Big Five Personality Inventory
Used in:
- Perceptron
- Decision Trees
- KNN
- Neural Networks

This dataset captures personality traits using Likert-scale responses to items like `OPN1` through `OPN10` (Openness to Experience). It enables both binary and multiclass trait prediction.

### 2. General Social Survey (GSS) 2018
Used in:
- Random Forest
- Ensemble Methods
- Perceptron

A nationally representative U.S. survey covering political views, demographics, health, income, and life satisfaction. Ideal for public opinion and behavioral modeling tasks.

### 3. Synthetic Dataset
Used in:
- Logistic Regression

A generated dataset designed to test binary classification boundaries and visual decision surfaces.

### 4. Student Performance Data
Used in:
- Linear Regression

A basic dataset with variables like `Hours Studied` and `Performance Index` to demonstrate linear modeling and gradient descent.

---

## Models and Tasks

### Linear Regression
- **Task**: Predict student performance from study time
- **Method**: Closed-form and gradient descent solutions
- **Result**: Grouping data improved MSE from 326 to 6.2

### Logistic Regression
- **Task**: Binary classification with a sigmoid output
- **Method**: Custom implementation with gradient updates
- **Dataset**: Synthetic 2D points for clear visualization
- **Result**: Accurate decision boundary with tracked training loss

### Perceptron
- **Task**: Predict "very happy" vs. not happy (GSS)
- **Method**: Hard threshold activation, learned from scratch
- **Result**: Simple model classified happiness based on health and financial satisfaction

### K-Nearest Neighbors (KNN)
- **Task**: Classify openness to experience (binary)
- **Result**: Highest accuracy at **k = 16** with ~90% test accuracy

### Decision Trees & Regression Trees
- **Task**: Predict openness trait as both class and score
- **Features**: OPN1–OPN10
- **Result**:
  - Classifier: 84% accuracy
  - Regressor: MSE = 0.0937
  - Visualizations showed interpretable decision paths

### Random Forest
- **Task**: Classify political ideology (GSS)
- **Result**: 42% accuracy with moderate class best predicted; key features were age, income, and religion

### Ensemble Methods (Voting, Bagging, Boosting)
- **Task**: Same as above
- **Result**:
  - Voting: 44% accuracy (best for conservatives)
  - Bagging: 44% balanced accuracy
  - AdaBoost: **46%** accuracy, strongest overall performance

### Neural Networks (TensorFlow)
- **Task**: Multiclass classification of openness (low, medium, high)
- **Structure**: Two hidden layers + dropout + softmax output
- **Result**: **93% validation accuracy**, strong F1-score across classes

---

## Takeaways

- **Linear models** are simple, interpretable, and ideal for visual teaching
- **Tree-based methods** provide visual explanations and good real-world performance
- **KNN and Perceptron** perform well on structured survey data with minimal tuning
- **Neural networks and boosting** deliver top accuracy but require careful tuning
- **Survey data** like the GSS and Big Five Inventory are highly compatible with supervised learning tasks in both psychology and political science

