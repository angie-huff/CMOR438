# Perceptron: Predicting Happiness from Survey Data

## Introduction

The Perceptron is one of the simplest and most foundational types of artificial neural networks. Introduced by Frank Rosenblatt in 1958, it acts as a linear binary classifier that separates data into two classes using a weighted summation and a step function. While basic in structure, the Perceptron plays a crucial role in understanding how more complex models like multi-layer neural networks operate.

This project implements the Perceptron algorithm from scratch and applies it to data from the **General Social Survey (GSS) 2018** to predict whether individuals are "Very Happy" based on two key self-assessments: health and financial satisfaction.

## How the Perceptron Model Works

The Perceptron learns to classify inputs by adjusting weights and a bias term through iterative training. It uses:

- **Summation Function**:
  \[
  z = \sum w_i x_i + b
  \]

- **Step Activation Function**:
  \[
  \text{output} = 
  \begin{cases}
    1 & \text{if } z \geq 0 \\
    0 & \text{otherwise}
  \end{cases}
  \]

The Perceptron updates weights using the Perceptron Learning Rule, which corrects errors by moving weights in the direction that reduces misclassification.

## Task

This project performs the following:

- Load and preprocess the 2018 General Social Survey (GSS) dataset
- Filter the `HAPPY` variable to only include “Very Happy” and “Pretty Happy” responses
- Recode labels to binary: 1 = Very Happy, 0 = Pretty Happy
- Train a Perceptron model using two features:
  - Self-reported health (`HEALTH`)
  - Financial satisfaction (`SATFIN`)
- Visualize the data by label to observe separation patterns
- Evaluate model performance using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix

## Dataset

**Source**: [General Social Survey (GSS) 2018](https://gssdataexplorer.norc.org)

**Variables Used**:
- `HAPPY`: Subjective happiness, filtered to include only “Very Happy” (1) and “Pretty Happy” (2)
- `HEALTH`: Self-reported health on a 1–4 scale (1 = Excellent, 4 = Poor)
- `SATFIN`: Satisfaction with financial situation on a 1–3 scale (1 = Pretty Satisfied, 3 = Not at All)

**Preprocessing**:
- Dropped missing values
- Filtered responses to only the top two happiness categories
- Recoded labels to binary (1 = Very Happy, 0 = Pretty Happy)

## Results

The Perceptron achieved **65% accuracy**, largely by correctly identifying the majority class ("Pretty Happy"). However, its performance on the minority class ("Very Happy") was weak:

- **Recall (Very Happy)**: 16%
- **F1-score (Very Happy)**: 0.24
- **Confusion Matrix** revealed significant false negatives

These results reflect:
- **Class imbalance** skewing model predictions
- **Linear separability limits** of the Perceptron for subjective data
- The importance of using more complex models or feature-rich inputs in real-world applications

## Limitations

- Only two features used — happiness is likely influenced by many additional factors
- No oversampling or class-weight adjustment for imbalance
- Self-reported measures introduce subjectivity and potential bias
- Linear model cannot capture nonlinear decision boundaries

## Real-World Interpretation

Despite its simplicity, this model highlights the relationship between **self-rated health**, **financial well-being**, and **subjective happiness**. It also underscores challenges in modeling human sentiment using minimal features and linear methods.

The results suggest that improving public health and economic stability could meaningfully impact happiness — insights valuable for social science, policy, and behavioral research.

## Dataset Citation

Davern, Michael; Bautista, Rene; Freese, Jeremy; Herd, Pamela; and Morgan, Stephen L.; General Social Survey 1972-2024. [Machine-readable data file]. Principal Investigator, Michael Davern; Co-Principal Investigators, Rene Bautista, Jeremy Freese, Pamela Herd, and Stephen L. Morgan. Sponsored by National Science Foundation. NORC ed. Chicago: NORC, 2025: NORC at the University of Chicago [producer and distributor]. Data accessed from the GSS Data Explorer website at [gssdataexplorer.norc.org](https://gssdataexplorer.norc.org).
