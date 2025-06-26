# K-Means Clustering and PCA

This notebook uses **K-Means clustering** to explore patterns in student mental health using a large survey dataset. The goal is to identify distinct psychological profiles among university students based on self-reported experiences with academic stress, anxiety, and depression.

To support visualization and understand structure in the data, we also apply **Principal Component Analysis (PCA)** for dimensionality reduction.

---

## Dataset

The dataset used is the **"MHP (Anxiety, Stress, Depression) Dataset of University Students"**, which contains survey responses from **2,028 students** across multiple universities in Bangladesh. It was collected through a Google Form and is publicly available on Figshare.

- **Source**: [MHP Dataset on Figshare](https://doi.org/10.6084/m9.figshare.25771164.v1)
- **Format**: CSV
- **Collection Year**: 2024
- **Respondents**: University students, all academic years and majors
- **Instruments**: Adapted from PHQ-9, GAD-7, and custom academic stress questions
- **Response Format**: 5-point Likert scale (e.g., "0 - Not at all" to "3 - Nearly every day")

### Features Used

Out of the 33 columns, we selected **26 Likert-scale items** related to psychological states, grouped into three domains:

#### Academic Stress
- Examples:
  - *"How often have you felt upset due to something that happened in your academic affairs?"*
  - *"How often have you felt as if academic difficulties are piling up so high that you could not overcome them?"*

#### Anxiety Symptoms
- Examples:
  - *"How often have you felt nervous, anxious or on edge due to academic pressure?"*
  - *"How often have you been so restless that it is hard to sit still?"*

#### Depression Symptoms
- Examples:
  - *"How often have you been feeling down, depressed or hopeless?"*
  - *"How often have you had thoughts that you would be better off dead, or of hurting yourself?"*

Each question measures **frequency** of the symptom over a semester and was numerically encoded for clustering.

---

## Methodology

We used a combination of **K-Means clustering** and **Principal Component Analysis (PCA)**:

1. **Standardization**  
   Features were standardized using `StandardScaler` to ensure equal weighting.

2. **PCA (Principal Component Analysis)**  
   PCA was applied to reduce the 26-dimensional dataset to 2 principal components for visualization. PCA identifies the directions (components) that capture the most variance in the data. This allows:
   - Visualization of complex psychological patterns
   - Detection of linear structure in the dataset
   - Improved interpretability of clustering output

3. **Elbow Method**  
   We used the **Elbow Method** to find the optimal number of clusters. The plot suggested **k = 3** as the inflection point.

4. **K-Means Clustering**  
   Students were clustered into 3 groups based on standardized symptom responses. These groups were then visualized in the PCA-reduced 2D space.

---

## Cluster Interpretation

Each cluster reflects a distinct mental health profile:

- **Cluster 0 (High Distress)**  
  High scores on anxiety, stress, and depression. Includes students with severe symptoms, including suicidal ideation.

- **Cluster 1 (Moderate Distress)**  
  Mixed symptom presence. Students report some emotional difficulty but maintain partial coping abilities.

- **Cluster 2 (Low Distress)**  
  Minimal symptoms across all dimensions. Represents emotionally stable students with low mental health burden.

---

## PCA Findings

- The **first two principal components** captured a large portion of total variance in the dataset.
- Visualization in PCA space revealed that the clusters are **distinctly separated**, validating the clustering results.
- PCA also confirmed that while clusters exist, **mental health symptoms form a spectrum**, with most students concentrated in the center and a few distributed on the margins.

---

## Takeaways

- **K-Means clustering**, supported by **PCA**, effectively grouped students into interpretable mental health profiles.
- The largest group was students under **moderate distress**, suggesting this is a key population for scalable preventative interventions.
- PCA proved essential for:
  - Visualizing high-dimensional psychological data
  - Validating the distinctness of clusters
  - Uncovering the latent structure of mental health symptom reporting

---

## Dataset Citation

Syeed, Mahbubul; Rahman, Ashifur; Akter, Laila; Fatema, Kaniz; Khan, Razib Hayat; Rajual Karim, Md.; *et al.* (2024).  
**MHP (Anxiety, Stress, Depression) Dataset of University Students**. Figshare. Dataset.  
[https://doi.org/10.6084/m9.figshare.25771164.v1](https://doi.org/10.6084/m9.figshare.25771164.v1)
