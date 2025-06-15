# Perceptron: Predicting Happiness from Survey Data

## Introduction

The Perceptron is one of the simplest types of artificial neural networks and serves as the foundational building block for more complex architectures. Inspired by the human neuron, it receives multiple inputs, each associated with a weight, and produces a binary output through an activation function. The learning process adjusts the weights based on the error between predicted and actual outputs using the Perceptron Learning Rule.

This project implements the Perceptron algorithm from scratch and applies it to real-world survey data to predict subjective happiness based on individuals' self-rated health and financial satisfaction.

## How the Perceptron Model Works

The Perceptron Network functions as a linear binary classifier using a "hardlim" (unit step) activation function. It performs classification in two steps:
- **Summation function**: Computes a weighted sum of input features and a bias.
- **Transfer function**: Applies the step function to generate binary output (0 or 1).

The model is trained using labeled data, adjusting its weights during each iteration (epoch) to minimize misclassifications.

Mathematically:
```
output = 1 if (w · x + b) ≥ 0 else 0
```

## Task

In this notebook, we:
- Load and preprocess the **General Social Survey (GSS) 2018** dataset
- Convert multi-class labels to binary (1 for 'Very Happy', 0 otherwise)
- Train a custom Perceptron model on survey features (health, financial satisfaction)
- Evaluate performance using accuracy, precision, recall, and confusion matrix

## Dataset

**Source**: General Social Survey (2018)

**Features Used**:
- `HEALTH`: Self-reported health
- `SATFIN`: Satisfaction with financial situation

**Label**:
- `HAPPY`: Recoded to 1 (Very Happy), 0 (All others)

## Libraries Used

- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/)

## Results

Despite the simplicity of the model, it was able to classify a majority class effectively. However, the performance was skewed due to class imbalance. This project shows the importance of data preprocessing and evaluation in machine learning workflows.