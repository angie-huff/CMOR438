# Data Science & Machine Learning

This repository documents the implementation and evaluation of core machine learning algorithms in a structured, end-to-end project format. It reflects the development process of a typical machine learning pipeline—starting from data analysis and model selection, to training, validation, and interpretation.

---

## About the Project

Machine learning can be broadly divided into:

- **Supervised Learning**: Learning from labeled data to make predictions.
  - **Regression**: Predict continuous values (e.g., performance scores).
  - **Classification**: Predict categories (e.g., personality type, political ideology).

- **Unsupervised Learning**: Finding patterns in unlabeled data.
  - **Clustering**: Grouping observations based on feature similarity.
  - (Note: This project focuses only on **clustering**, not anomaly detection.)

To enable meaningful comparisons, multiple algorithms were applied to a **shared dataset whenever feasible**, enabling apples-to-apples insights across model types.

---

## Folder Structure

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

## Datasets Used

### MHP Mental Health Dataset (2024)
- Psychological survey of **2,028 university students**
- Measures **academic stress**, **anxiety**, and **depression**
- Used in all **unsupervised learning notebooks**

---

### General Social Survey (GSS) 2018
- U.S. public opinion and demographic survey
- Used in supervised models to predict **happiness** and **political ideology**

---

### Big Five Personality Inventory
- IPIP-style self-report questionnaire
- Used to classify **openness** and other **personality traits**

---

### Student Performance (Synthetic)
- Toy dataset with simple variables (e.g., **hours studied**, **test score**)
- Used to demonstrate **regression** and **gradient descent**

---

- Every notebook includes **detailed markdown explanations** and **social or psychological interpretations**
- Visualizations help **interpret model behavior** and highlight strengths/limitations
- Consistent use of **shared datasets** enables valid model comparisons
- Clustering methods are tied to **real-world mental health implications**, not just abstract math