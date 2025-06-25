# K-Means Clustering on Student Mental Health Data

This notebook uses K-Means clustering to explore patterns in student mental health using a large survey dataset. The goal is to identify distinct psychological profiles among university students based on self-reported experiences with academic stress, anxiety, and depression.

---

## Dataset

The dataset, titled **"Mental Health Assessment of University Students"**, consists of responses from **2,028 university students** collected through a Google Forms survey. It is publicly available on [Figshare](https://figshare.com/articles/dataset/MHP_Anxiety_Stress_Depression_Dataset_of_University_Students/25771164).

### Source
- Distributed via: Figshare
- Format: CSV
- Instruments: The questions were adapted from the **PHQ-9** and **GAD-7**, with custom additions focused on academic stress and university life.
- Responses are given on **5-point Likert scales**, with variations like:
  - `"0 - Not at all"`, `"1 - Several days"`, `"2 - More than half the days"`, `"3 - Nearly every day"`
  - `"0 - Never"` through `"4 - Very Often"`

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

## File Structure

- `MentalHealth.csv`: Cleaned survey dataset
- `kmeans_notebook.ipynb`: Main notebook with all preprocessing, clustering, and visualization
- `Supplementary file - Questionnaire.pdf`: Raw question text
- `README.md`: This file
