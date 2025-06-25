# K-Means Clustering on Student Mental Health Data

This notebook uses K-Means clustering to explore patterns in student mental health using a large survey dataset. The goal is to identify distinct psychological profiles among university students based on self-reported experiences with academic stress, anxiety, and depression.

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

We applied the K-Means algorithm to the standardized dataset:

1. **Standardization**: Features were scaled using `StandardScaler` to have mean = 0 and standard deviation = 1.
2. **Optimal k**: We used the **Elbow Method** to determine the ideal number of clusters, identifying **k = 3** as the elbow point.
3. **Clustering**: K-Means grouped students into three clusters based on symptom patterns.
4. **PCA Visualization**: We reduced the 26D data to 2D using **Principal Component Analysis** to visualize the clusters.

---

## Cluster Interpretation

Each cluster reflects a distinct mental health profile:

- **Cluster 0 (High Distress)**: Severe anxiety, stress, and depressive symptoms. Highest rates of suicidal ideation.
- **Cluster 1 (Moderate Distress)**: Mid-range symptoms with partial coping ability.
- **Cluster 2 (Low Distress)**: Rarely experiences symptoms; emotionally stable and resilient.

---

## \Takeaways

- K-Means successfully grouped students into interpretable psychological profiles.
- The largest group (Cluster 1) represents students under moderate distress — a key population for preventative intervention.
- Visualization via PCA confirms that clusters are distinct in reduced dimensional space.

---

## Dataset Citation

Syeed, Mahbubul; Rahman, Ashifur; Akter, Laila; Fatema, Kaniz; Khan, Razib Hayat; Rajual Karim, Md.; *et al.* (2024).  
**MHP (Anxiety, Stress, Depression) Dataset of University Students**. Figshare. Dataset.  
[https://doi.org/10.6084/m9.figshare.25771164.v1](https://doi.org/10.6084/m9.figshare.25771164.v1)

