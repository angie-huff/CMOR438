# K-Nearest Neighbors Classifier: Predicting Openness to Experience

This project applies the K-Nearest Neighbors (KNN) classification algorithm to predict whether individuals score high or low on the "Openness to Experience" trait based on their responses to a personality assessment.

## Dataset and Problem Setup

The dataset consists of responses to ten survey items (OPN1 through OPN10) measuring openness. A random sample of 2,000 observations was selected, and rows with missing values were removed. Each individual's mean openness score was calculated, and a binary label was assigned: 1 for scores above the median (high openness), and 0 for scores at or below the median (low openness).

The dataset was standardized using `StandardScaler`, and then split into training and test sets using an 80/20 ratio.

## Methodology

A KNN classifier was implemented using `scikit-learn`. The model was initially trained with k = 2 and evaluated using accuracy, a confusion matrix, and a classification report. To assess the effect of k on performance, the model was tested with values of k ranging from 1 to 19. Accuracy scores for each value of k were plotted to visualize trends and identify the optimal number of neighbors.

## Results

The model achieved strong performance across a wide range of k values. The best test accuracy, 90.5%, occurred at k = 16. Initial evaluation at k = 2 showed an accuracy of 89% with well-balanced precision and recall between classes. The confusion matrix indicated that the model was particularly effective at identifying low-openness individuals, with minor misclassification of high-openness cases.

## Visualizations

- Histogram of average openness scores with median threshold line
- Confusion matrix heatmap (k = 2)
- Accuracy vs. k plot (k = 1 to 19)

## Conclusion

K-Nearest Neighbors proved to be a reliable model for predicting openness based on survey data. The model demonstrated consistent performance, was easy to interpret, and required minimal parameter tuning. Results suggest that KNN is a viable approach for similar classification tasks involving standardized psychological survey data.

## Requirements

- pandas
- numpy
- matplotlib
- scikit-learn
- seaborn
