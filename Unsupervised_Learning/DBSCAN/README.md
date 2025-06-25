# DBSCAN Clustering on Student Mental Health Data

This notebook applies **DBSCAN**, a density-based clustering algorithm, to a dataset of university student mental health survey responses. The goal is to explore whether students form natural psychological groupings based on their experiences with academic stress, anxiety, and depression — or whether mental health exists on a continuous spectrum without distinct clusters.

---

## Dataset

The dataset is titled **"MHP (Anxiety, Stress, Depression) Dataset of University Students"**, publicly available via [Figshare](https://doi.org/10.6084/m9.figshare.25771164.v1). It contains **2,028 responses** from students enrolled at various universities in Bangladesh.

###  Data Collection:
- Format: CSV + survey questionnaire (Google Forms)
- Collection year: 2024
- Structure: 33 columns, including demographics and mental health indicators
- All psychological indicators are measured using **Likert-scale questions**

###  Focus of This Analysis:
We isolate **26 survey items** that measure:
- **Academic stress** (e.g., difficulty coping with assignments, feelings of control)
- **Anxiety symptoms** (e.g., nervousness, restlessness, fear)
- **Depression symptoms** (e.g., fatigue, suicidal ideation, low interest)

Each question was phrased:
> *"In a semester, how often have you..."*

Responses were given on a 5-point Likert scale:
- `"0 - Not at all"`, `"1 - Several days"`, `"2 - More than half the days"`, `"3 - Nearly every day"`, `"4 - Very Often"`
- Variants (e.g., `"0 - Never"`, `"2 - More than half the semester"`) were mapped to equivalent numeric values

### Preprocessing:
- **26 mental health items** selected and mapped to numeric scale (0–4)
- **Rows with missing or non-informative values** (e.g., "Prefer not to say") were dropped
- Data was **standardized** using `StandardScaler` to ensure fair clustering

---

## DBSCAN Method

### What is DBSCAN?
- A density-based clustering algorithm
- Groups points that are close together and labels low-density points as **noise**
- Requires **no specification of k (number of clusters)**
- Can identify **arbitrary cluster shapes** and **outliers**

### Parameters Used:
- `eps = 1.2`: Radius around each point for neighborhood search
- `min_samples = 5`: Minimum points to form a cluster

### Result Summary:
- **1,944 out of 2,028 students (96%)** were labeled as **noise**
- **Only 84 students** were grouped into **7 very small clusters**
- **Silhouette Score (excluding noise): 0.858**
  - Indicates that the few clusters formed were extremely well-separated

---

## Visualization

We used **PCA** to reduce the data to 2D and visualize the DBSCAN results:

- Noise points dominate the dataset and appear scattered
- A few **tight, well-separated clusters** are visible
- Most students do not form strong cluster structures

---

## Interpretation and Social Insights

### Psychological Interpretation:
- Mental health profiles among students **do not form clear, dense groupings**
- Instead, responses are **spread across a spectrum**
- DBSCAN was excellent at detecting **rare patterns** but found that **most students do not fall into sharply defined psychological types**

### Social Implication:
- Supports the view that **mental health exists on a continuum**
- Reinforces the need for **individualized care models** rather than strict categorical approaches
- Students with tightly clustered symptoms (e.g., high anxiety and suicidal ideation) may represent a **critical subgroup** in need of urgent intervention

---

## Dataset Citation

Syeed, Mahbubul; Rahman, Ashifur; Akter, Laila; Fatema, Kaniz; Khan, Razib Hayat; Rajual Karim, Md.; et al. (2024).  
**MHP (Anxiety, Stress, Depression) Dataset of University Students.** Figshare.  
[https://doi.org/10.6084/m9.figshare.25771164.v1](https://doi.org/10.6084/m9.figshare.25771164.v1)
