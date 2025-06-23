# Random Forest

This notebook uses a Random Forest classifier to predict political ideology (liberal, moderate, or conservative) using demographic and socioeconomic features from the General Social Survey (GSS) 2018 dataset.

---

## Dataset

The [General Social Survey (GSS)](https://gss.norc.org/) is one of the longest-running and most respected surveys of U.S. public opinion. Conducted by NORC at the University of Chicago, the GSS collects nationally representative data on a wide range of social, political, and demographic indicators.

This notebook uses a subset of the 2018 wave, focusing on the following features:

- `AGE`: Age of respondent
- `SEX`: Gender
- `EDUC`: Years of education completed
- `INCOME`: Total family income
- `RACE`: Racial self-identification
- `RELIG`: Religious preference
- `MARITAL`: Marital status

The target variable is `POLVIEWS`, which records self-identified political ideology on a 7-point scale from “extremely liberal” to “extremely conservative.” These values are grouped into:

- **0** = Liberal (original values 1–3)
- **1** = Moderate (original value 4)
- **2** = Conservative (original values 5–7)

---

## Model

Random Forest is an ensemble learning method that builds multiple decision trees and aggregates their predictions. Each tree is trained on a random subset of the data and features, making the overall model less prone to overfitting.

Key benefits:
- Handles both numeric and categorical data
- Provides built-in feature importance rankings
- Reduces variance by averaging across trees

---

## Performance Summary

- **Accuracy**: ~42%
- **Moderate class** was the most accurately predicted
- **Top features** included age, education, income, and religious affiliation
- Confusion matrix revealed overlap between liberal/conservative classes and moderates

---

## Takeaways

- Political ideology can be partially predicted using standard demographic variables
- Age, education, and income were the most influential predictors
- Random Forest provides a useful baseline for classification, with interpretable feature rankings
