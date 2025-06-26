# Truncated SVD on Student Mental Health Data

This notebook applies **Truncated Singular Value Decomposition (SVD)** to uncover patterns in student mental health based on self-reported symptoms of academic stress, anxiety, and depression. By reducing the dataset’s dimensionality, we aim to reveal latent structure and visualize student variation in a compact 2D space.

---

## Dataset

We use the **"MHP (Anxiety, Stress, Depression) Dataset of University Students"**, which contains survey responses from **2,028 university students** across multiple institutions in Bangladesh. The dataset was collected via Google Forms in 2024 and is publicly available on Figshare.

- **Source**: [Figshare – MHP Dataset](https://doi.org/10.6084/m9.figshare.25771164.v1)
- **Respondents**: Undergraduate and graduate students
- **Instruments**: Adapted from PHQ-9 (depression), GAD-7 (anxiety), and custom academic stress items
- **Format**: CSV with responses on a 5-point Likert scale

### Features Used

From the full dataset, we selected **26 Likert-scale questions** measuring:

- **Academic Stress** (e.g., difficulty coping with assignments)
- **Anxiety Symptoms** (e.g., restlessness, worry, nervousness)
- **Depression Symptoms** (e.g., low mood, suicidal ideation, loss of interest)

These features were numerically encoded (0–4) and standardized prior to applying SVD.

---

## What is Truncated SVD?

**Singular Value Decomposition (SVD)** is a matrix factorization technique that breaks any data matrix $X$ into three components:

$$
X = U \Sigma V^T
$$

Where:
- $U$ contains the left singular vectors (relationships between observations)
- $\Sigma$ is a diagonal matrix of singular values (importance of each component)
- $V^T$ contains the right singular vectors (relationships between features)

**Truncated SVD** is a reduced form that retains only the top $k$ components. It is especially useful for:
- Dimensionality reduction
- Decomposing sparse or non-centered data
- Preserving structure while reducing noise

In this notebook, we use `TruncatedSVD` from `scikit-learn` to reduce the 26-dimensional dataset to 2 components for visualization.

---

## Methodology

1. **Preprocessing**:
   - Likert-scale responses were numerically mapped (0 to 4)
   - Missing values (e.g., "Prefer not to say") were dropped
   - Features were standardized using `StandardScaler`

2. **SVD Decomposition**:
   - We computed 26 components using `TruncatedSVD`
   - Explained variance was plotted to assess dimensionality
   - The first 2 components were used for projection

3. **Visualization**:
   - A **density map** was generated using `sns.kdeplot()` to visualize the distribution of students in SVD-reduced space

---

## Findings

- The first two SVD components captured a meaningful portion of the total variance
- Most students were concentrated in a dense central region of the plot, indicating **common patterns of distress**
- A few students appeared on the margins of the distribution, potentially representing **atypical or high-risk psychological profiles**
- The continuous, elliptical structure suggests that mental health symptoms form a **spectrum**, rather than falling into discrete categories

---

## Takeaways

- Truncated SVD successfully reduced the complexity of the dataset while preserving important structural information
- Visualization revealed both the **central tendency** of the population and **deviations** worth further study
- These findings support a dimensional rather than categorical view of student mental health

---

## Dataset Citation

Syeed, Mahbubul; Rahman, Ashifur; Akter, Laila; Fatema, Kaniz; Khan, Razib Hayat; Rajual Karim, Md.; *et al.* (2024).  
**MHP (Anxiety, Stress, Depression) Dataset of University Students**. Figshare. Dataset.  
[https://doi.org/10.6084/m9.figshare.25771164.v1](https://doi.org/10.6084/m9.figshare.25771164.v1)