# Principal Component Analysis (PCA)

This notebook applies **Principal Component Analysis (PCA)** to explore structure and reduce dimensionality in a dataset of university student responses to mental health survey questions. The goal is to better understand variation in psychological distress and prepare the data for clustering and visualization.

---

## What is PCA?

**Principal Component Analysis (PCA)** is an unsupervised linear transformation technique used to reduce the dimensionality of high-dimensional datasets while retaining the most meaningful variation.

PCA works by:
- Identifying **principal components**, which are new axes (directions) that maximize variance in the data
- Ensuring that these components are **orthogonal (uncorrelated)** to each other
- Ranking components in order of the **variance they capture**, so that the first few components explain the most information

In practice, PCA transforms the data into a new coordinate system, allowing us to:
- Eliminate redundancy across features
- Simplify datasets with many correlated variables
- **Visualize complex data in 2 or 3 dimensions**
- Feed reduced features into clustering or classification algorithms with improved performance and interpretability

---

## Dataset

We use the **Mental Health Assessment of University Students** dataset, originally published on [Figshare](https://doi.org/10.6084/m9.figshare.25771164.v1). The dataset contains responses from **2,028 students** from Bangladeshi universities who answered a detailed mental health questionnaire.

### 🔍 Features Used:
The notebook focuses on **26 Likert-scale questions** capturing three major psychological dimensions:

- **Academic Stress**  
  e.g., "How often have you felt overwhelmed by academic responsibilities?"

- **Anxiety**  
  e.g., "How often have you felt nervous or on edge?"

- **Depression**  
  e.g., "How often have you had little interest or pleasure in doing things?"

Responses were mapped from Likert categories (e.g., `"0 - Not at all"` to `"4 - Very Often"`) into numerical values from 0 to 4.

---

## Methodology

1. **Feature Selection:** We isolate the 26 symptom-related questions and drop non-numeric values (e.g., "Prefer not to say").

2. **Numeric Encoding:** All Likert responses are mapped into integers to allow for matrix operations.

3. **Standardization:** We scale the features using `StandardScaler` so that each variable has a mean of 0 and a standard deviation of 1. This is essential because PCA is sensitive to scale.

4. **Dimensionality Reduction:** We apply PCA to:
   - Visualize variance explained across components (scree plot)
   - Project students onto the **first 2 principal components** for visualization
   - Prepare for downstream unsupervised learning (e.g., clustering)

---

## Key Findings

- The **first component alone** explained over 40% of the total variance in mental health symptom responses.
- Roughly **10 components** were sufficient to capture over 85% of the dataset’s structure.
- The 2D projection of students revealed:
  - A **dense core** of students with moderate symptom profiles
  - A **lack of strong clustering**, suggesting mental health patterns are **continuous, not categorical**
  - A few **outlier students** with highly distinct combinations of symptoms

---

## Social Implications

This PCA analysis reinforces that student mental health is best modeled as a **spectrum** rather than a set of discrete categories. Most students cluster near the center, but some show extreme or unique combinations of symptoms that may not be captured by traditional diagnostic labels.

PCA provides a **data-driven foundation** for:
- Personalized interventions
- Early detection of high-risk cases
- Dimensional psychological modeling

---

## Dataset Citation

Syeed, Mahbubul; Rahman, Ashifur; Akter, Laila; Fatema, Kaniz; Khan, Razib Hayat; Rajual Karim, Md.; et al. (2024).  
**MHP (Anxiety, Stress, Depression) Dataset of University Students.** Figshare.  
[https://doi.org/10.6084/m9.figshare.25771164.v1](https://doi.org/10.6084/m9.figshare.25771164.v1)
