# Decision Trees and Regression Trees: Modeling Openness to Experience

This notebook implements both decision trees and regression trees to analyze the Openness to Experience trait based on personality survey data. Using responses to ten openness-related items (OPN1 through OPN10), we explore both classification and regression tasks on the same dataset.

## Dataset and Objective

The dataset consists of responses to ten items measuring openness from a larger Big Five personality assessment. After removing missing values and randomly sampling 2,000 observations, we construct two separate supervised learning tasks:

1. A **classification task** that predicts whether an individual scores above or below the median openness score.
2. A **regression task** that predicts the individual’s actual average openness score as a continuous value.

## Methods

The feature set was standardized using `StandardScaler`, and the dataset was split into training and test sets (80/20 split) for both tasks. 

For classification, we used `DecisionTreeClassifier` with a maximum depth of 4. For regression, we used `DecisionTreeRegressor` with a maximum depth of 3. These parameters were chosen to balance interpretability and performance.

The models were visualized using `plot_tree()` to illustrate decision rules and structure. Evaluation was conducted using classification metrics (accuracy, precision, recall, F1-score) and regression metrics (mean squared error), along with interpretive plots such as confusion matrices and predicted vs. actual score comparisons.

## Results

- The **decision tree classifier** achieved an accuracy of 84%, with balanced performance across high and low openness categories.
- The **regression tree** achieved a mean squared error (MSE) of 0.0937, capturing central trends in the data while maintaining a low average prediction error.
- Visualizations of both tree structures showed interpretable splits along OPN features such as OPN1, OPN4, and OPN8, providing insight into how the model distinguishes between different openness profiles.

## Conclusion

This notebook demonstrates how decision trees can be effectively used for both classification and regression tasks in psychological data analysis. The models provide intuitive, visual explanations for how predictions are made, while delivering strong performance on both categorical and continuous prediction tasks.
