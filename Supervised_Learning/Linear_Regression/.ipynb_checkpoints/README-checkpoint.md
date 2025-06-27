# Linear Regression

Linear regression is one of the most foundational techniques in both statistics and machine learning. It models the relationship between an input feature and a continuous output by fitting a straight line to observed data points. Inspired by the basic idea of a biological neuron, it mimics how a system might generate a continuous response based on a weighted sum of inputs.

In this project, a custom linear regression model was implemented from scratch using gradient descent, then applied to real-world-inspired data on student study habits and academic performance.

---

## How Linear Regression Works

The model assumes a linear relationship between input and output:

\[
\hat{y} = w \cdot x + b
\]

Where:
- `w` is the weight (slope),
- `b` is the bias (intercept),
- `x` is the input (hours studied),
- `ŷ` is the predicted performance.

To minimize prediction error, the model uses **Mean Squared Error (MSE)** as a cost function:

\[
C(w, b) = \frac{1}{2} (w \cdot x + b - y)^2
\]

Gradient descent updates the parameters using:

- ∂C/∂w = (w * x + b - y) * x  
- ∂C/∂b = (w * x + b - y)

Update rules:
- `w ← w - α * ∂C/∂w`
- `b ← b - α * ∂C/∂b`

---

## Task

This project builds a linear regression model from scratch and applies it to the **Student Performance** dataset to predict a student’s academic score (`Performance Index`) based on the number of hours they studied (`Hours Studied`).

Both the raw data and a grouped version (averaged by hour) were used to compare performance and evaluate the impact of preprocessing.

---

## Dataset

**Source**: Student Performance dataset (synthetic or simplified educational dataset)

**Features**:
- `Hours Studied` – input feature representing number of hours studied
- `Performance Index` – target output representing academic score

**Preprocessing**:
- Removed missing values
- Grouped by hours studied and averaged performance to reduce variance

---

## Results

| Dataset       | MSE     |
|---------------|---------|
| Raw Data      | 326.37  |
| Grouped Data  | 6.20    |

- Training on raw data yielded high error due to overlapping clusters and noise.
- Grouping the data revealed a much clearer linear trend and allowed for drastically better performance.
- The decreasing MSE over epochs confirmed that gradient descent effectively minimized the cost.

---

## Interpretation and Limitations

- The model identified a clear positive trend between hours studied and performance.
- This result aligns with expectations in educational research: more study generally improves outcomes.
- However, the model assumes a linear relationship and only uses one feature. Real student performance depends on many factors (prior knowledge, test difficulty, mental health, etc.).
- The simplicity of the dataset may not reflect the complexity of real-world data, limiting the generalizability of the model.

---

## Real-World Significance

This project illustrates the power and limitations of linear models. While not perfect predictors, they offer interpretable insights and serve as a strong foundation for understanding more advanced machine learning techniques.

In practice, linear regression can be useful for early intervention systems, education policy modeling, and personal learning analytics — provided the data quality and assumptions are handled with care.
