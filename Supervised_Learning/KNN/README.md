# K-Nearest Neighbors Classifier: Predicting Openness to Experience

This project applies the K-Nearest Neighbors (KNN) classification algorithm to predict whether individuals score high or low on the **"Openness to Experience"** trait — one of the Big Five personality dimensions — based on their responses to a standardized personality assessment.

---

## Dataset and Problem Setup

The dataset consists of responses to ten openness-related survey items (`OPN1` through `OPN10`) from a large personality inventory. A random sample of 2,000 participants was drawn, and rows with missing data were removed.

Each individual's **average openness score** was computed, and a binary classification target was assigned:
- `1` = high openness (above the median)
- `0` = low openness (at or below the median)

All features were standardized using `StandardScaler` to ensure fair contribution to distance calculations. The dataset was split into **training (80%)** and **testing (20%)** subsets.

---

## Methodology

A KNN classifier was implemented using `scikit-learn` and tested with multiple values of **k** (number of neighbors):

- Initial evaluation was done with **k = 2**
- Accuracy scores were computed for **k values from 1 to 19**
- Performance was assessed using:
  - **Accuracy**
  - **Confusion matrix**
  - **Precision, recall, F1-score**

---

## Results

The KNN model showed consistently strong performance:

- **Best test accuracy: 90.5% at k = 16**
- At **k = 2**, the model achieved 89% accuracy with well-balanced precision and recall
- The confusion matrix showed that both high- and low-openness individuals were effectively classified, with only minor misclassification

These results suggest the survey responses form meaningful clusters in feature space, making KNN a viable approach.

---

## Conclusion and Interpretation

KNN proved to be a robust, interpretable classifier for openness prediction using personality data. It required no explicit training phase and produced high accuracy across multiple k values. This confirms that standardized self-report responses contain informative structure that KNN can leverage effectively.

### Real-World Relevance

This approach could be used in:
- Psychology research to group participants by personality type
- Career or lifestyle recommendation systems
- Pre-screening tools in education or counseling

### Limitations

- **Binary label simplification** loses nuance in openness (e.g., those near the median may be miscategorized)
- **Sensitivity to distance metric and feature scaling**
- **Computational cost** grows with dataset size since KNN stores all training data
- **No feature selection** — all 10 items are treated equally regardless of predictive value

Despite these limitations, KNN offers a transparent and reliable baseline model in structured survey settings.
