# Unsupervised Learning

This repository applies unsupervised learning techniques to explore patterns in student mental health using a real-world psychological dataset. We use clustering and dimensionality reduction to identify meaningful structure in how university students report academic stress, anxiety, and depression symptoms.

The methods included are:

- **K-Means Clustering**
- **DBSCAN (Density-Based Clustering)**
- **Truncated Singular Value Decomposition (SVD)** for dimensionality reduction and visualization

**Unsupervised learning** involves analyzing data that has **no explicit labels** or outcomes. The goal is to uncover **patterns, groupings, or structure** within the dataset based solely on the input features.

Unlike supervised models, unsupervised algorithms:
- Don’t know what the "correct" output is
- Must identify relationships within the data itself
- Are commonly used for:
  - **Clustering** (grouping similar observations)
  - **Dimensionality reduction** (visualizing or simplifying high-dimensional data)

In this project, we use unsupervised learning to explore patterns in mental health survey responses. By grouping students based on their symptoms, we can uncover latent psychological profiles without needing predefined diagnostic labels.

---

## Dataset Overview

All notebooks use the **MHP (Anxiety, Stress, Depression) Dataset of University Students**, a large-scale mental health survey from Bangladesh. It was collected in 2024 and published on Figshare.

- **Source**: [Figshare – MHP Dataset](https://doi.org/10.6084/m9.figshare.25771164.v1)
- **Format**: CSV
- **Size**: 2,028 university students across academic years and institutions
- **Tools Used**: PHQ-9 (Depression), GAD-7 (Anxiety), and custom Academic Stress items
- **Response Format**: 5-point Likert scale (e.g., “0 - Not at all” to “4 - Very Often”)

### Features Used

We focus on **26 questions** directly related to psychological symptoms, grouped into:

- **Academic Stress** (e.g., coping with assignments, exam pressure)
- **Anxiety** (e.g., restlessness, fear, irritability)
- **Depression** (e.g., low energy, suicidal ideation, lack of interest)

Responses were numerically mapped and standardized for use in unsupervised learning algorithms.

---

## 1. K-Means Clustering

- **Goal**: Identify discrete psychological profiles among students
- **Steps**:
  - Standardized the data
  - Used the **Elbow Method** to determine optimal number of clusters ($k = 3$)
  - Applied K-Means clustering
  - Visualized results using **PCA**

- **Findings**:
  - Three interpretable clusters emerged:
    - **High Distress**: Severe anxiety and depression
    - **Moderate Distress**: Mixed symptoms, partial coping
    - **Low Distress**: Emotionally resilient students
  - PCA confirmed separation between groups and showed outlier risk profiles

---

## 2. DBSCAN Clustering

- **Goal**: Discover clusters without assuming the number of groups
- **Method**: DBSCAN groups data based on **density** rather than distance
- **Steps**:
  - Tuned hyperparameters `eps` and `min_samples`
  - Used **PCA** to project results in 2D
  - Calculated **Silhouette Score** (excluding noise): *0.858*

- **Findings**:
  - DBSCAN identified multiple small, tight clusters
  - The majority of students were classified as **noise**, indicating they form a continuum rather than distinct groupings
  - High Silhouette Score suggests clusters were **internally coherent**

---

## 3. Truncated SVD

- **Goal**: Reduce dimensionality and visualize latent structure
- **Method**: Truncated SVD factorizes the data matrix into top components capturing most variance
- **Steps**:
  - Applied `TruncatedSVD` with 26 components
  - Plotted **cumulative variance explained**
  - Visualized students in 2D using **density plot**

- **Findings**:
  - Most variance captured by first 10 components
  - Students were heavily concentrated in central regions, with smooth gradients — indicating that mental health varies along a **spectrum**, not in discrete categories
  - SVD confirmed and enhanced insights from PCA

---

## Takeaways

- **K-Means** highlighted interpretable groupings of psychological symptoms
- **DBSCAN** revealed latent local clusters while recognizing that many students do not belong to any single group
- **SVD** demonstrated how mental health symptoms vary continuously in high-dimensional space and provided clear 2D visualizations
- The dataset is rich in structure and supports both **categorical and continuous interpretations** of mental health

---

## Dataset Citation

Syeed, Mahbubul; Rahman, Ashifur; Akter, Laila; Fatema, Kaniz; Khan, Razib Hayat; Rajual Karim, Md.; *et al.* (2024).  
**MHP (Anxiety, Stress, Depression) Dataset of University Students**. Figshare. Dataset.  
[https://doi.org/10.6084/m9.figshare.25771164.v1](https://doi.org/10.6084/m9.figshare.25771164.v1)
