# Data Science & Machine Learning
![](./MachineLearning.png)

This repository showcases the end-to-end implementation of core machine learning algorithms — from scratch and with libraries — applied to real-world datasets in the domains of **psychology**, **education**, and **public opinion**. It reflects both the technical rigor of model-building and the interpretive thinking needed to draw meaningful conclusions from human data.

The work was completed as part of a university course project and is designed to demonstrate mastery of the full machine learning pipeline: data preparation, model selection, training, evaluation, and interpretation. Special attention is given to **psychologically relevant variables** (e.g., personality, stress, happiness), linking model behavior to social insights.

---

## Project Purpose

This repository serves two educational goals:

1. **Conceptual Understanding**  
   - Implement classic machine learning algorithms (e.g., linear regression, KNN, decision trees, neural nets)
   - Learn how hyperparameters, loss functions, and optimization affect performance

2. **Applied Insight**  
   - Use real survey data to understand how psychological traits (e.g., openness, depression) are modeled
   - Evaluate which models work best in predicting human outcomes, and why

By applying multiple algorithms to **shared datasets**, the project enables controlled comparisons between models while grounding technical concepts in social applications.

---

## Structure

```bash
CMOR438/
│
├── Supervised_Learning/
│   ├── Linear_Regression.ipynb
│   ├── Logistic_Regression.ipynb
│   ├── Perceptron.ipynb
│   ├── KNN.ipynb
│   ├── Decision_Tree.ipynb
│   ├── Random_Forest.ipynb
│   ├── Ensemble_Methods.ipynb
│   ├── Neural_Network.ipynb
│   ├── README.md
│
├── Unsupervised_Learning/
│   ├── KMeans.ipynb
│   ├── DBSCAN.ipynb
│   ├── SVD.ipynb
│   ├── README.md
│
├── MentalHealth.csv
├── MentalHealthCodebook.pdf
├── Supplementary file - Questionnaire.pdf
├── final_project_summary_README.md (this file)
```

---

## Datasets Used

### MHP Mental Health Dataset (2024)
- Survey of **2,028 university students**
- Captures academic stress, anxiety, and depression scores
- Used in all **unsupervised learning** notebooks

### General Social Survey (GSS) 2018
- Large U.S. public opinion survey
- Used for **supervised tasks** (e.g., happiness classification)

### Big Five Personality Inventory
- Self-report items from an IPIP-style openness questionnaire
- Used to classify individuals by **Openness to Experience**

### Student Performance (Synthetic)
- Simplified data on hours studied and test scores
- Used to explain **regression** and **gradient descent** conceptually

---

## Features of This Repository

- Each notebook includes **in-depth markdown**, math explanations, and training visualizations
- Clear **social or psychological interpretations** accompany all model results
- Consistent use of **standardized datasets** for apples-to-apples model comparison
- Emphasis on **limitations**, **interpretability**, and **real-world implications**
- Unsupervised learning is framed in terms of **mental health research**, not just mathematical grouping

---

This repository is meant to bridge the gap between **machine learning theory** and **real-world insight**, especially in contexts where understanding people matters as much as predicting outcomes.
