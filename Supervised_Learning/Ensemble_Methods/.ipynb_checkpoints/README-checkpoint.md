# Ensemble Methods

This notebook explores ensemble learning techniques—Voting, Bagging, and Boosting—to classify political ideology using data from the 2018 General Social Survey (GSS). Ensemble methods improve predictive performance by combining multiple models, either in parallel or sequentially, to overcome the limitations of individual learners.

We build on previous work with decision trees and random forests, expanding our approach to include multiple ensemble strategies.

---

## Dataset

The [General Social Survey (GSS) 2018](https://gss.norc.org/) provides structured, nationally representative data on U.S. attitudes and demographics. In this notebook, we aim to predict respondents' self-reported political ideology (`POLVIEWS`), recoded into:

- **0** = Liberal (original responses 1–3)
- **1** = Moderate (response 4)
- **2** = Conservative (responses 5–7)

### Features Used:
- `AGE`: Age of respondent
- `SEX`: Gender
- `EDUC`: Years of education
- `INCOME`: Total family income
- `RACE`: Racial identity
- `RELIG`: Religious preference
- `MARITAL`: Marital status

Categorical variables were one-hot encoded, and the data was cleaned to remove missing or ambiguous values.

---

## Ensemble Methods Applied

### 1. Voting Classifier
A hard voting ensemble combining logistic regression, decision tree, and Naive Bayes classifiers. This method achieved an accuracy of **44%**, with strong conservative recall (65%) but limited ability to distinguish moderates and liberals.

### 2. Bagging Classifier
An ensemble of 100 shallow decision trees trained on bootstrapped samples. Bagging stabilized predictions and achieved balanced class-level performance with **44% accuracy**, demonstrating improved generalization over standalone decision trees.

### 3. AdaBoost
A sequential ensemble using 100 decision stumps. AdaBoost achieved the **highest accuracy (46%)**, with particularly strong recall and F1-score for moderate and conservative respondents. The model adjusted iteratively to focus on difficult-to-classify samples, improving overall predictive power.

---

## Takeaways

- **Boosting outperformed both bagging and voting**, especially in recall for moderates and conservatives.
- **Conservatives were most consistently classified**, suggesting clearer demographic clustering in this group.
- **Liberals had lower recall**, indicating greater within-group variability and demographic overlap with moderates.
- Ensemble methods are powerful tools for sociopolitical prediction tasks, particularly when class boundaries are noisy or overlapping.