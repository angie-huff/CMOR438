# Linear Regression

The linear regression model is a foundational method in machine learning that aims to find the best-fitting straight line through a set of data points. Inspired by neurons in the brain, it mimics how a biological system might produce a continuous output from a weighted sum of inputs.


## How Linear Regression Works

Linear regression tries to model the relationship between two variables by fitting a straight line:

ŷ = w * x + b

Where:
- `w` is the weight (slope),
- `b` is the bias (intercept),
- `x` is the input feature,
- `ŷ` is the predicted output.

The model is trained to minimize the **Mean Squared Error (MSE)** between the actual values and predicted values:

C(w, b) = (1/2) * (w * x + b - y)<sup>2</sup>

To minimize this cost function, we use **gradient descent**, which updates the weight and bias based on the following derivatives:

∂C/∂w = (w * x + b - y) * x \
∂C/∂b = (w * x + b - y)

Update rules:

w ← w - α * ∂C/∂w \
b ← b - α * ∂C/∂b

---

## Task

In this project, I built a linear regression model from scratch and applied it to a real-world dataset on student performance. The model was trained to predict a student’s performance index based on the number of hours they studied.


## Dataset

The dataset used for this algorithm is the **Student Performance** dataset, which includes:
- `Hours Studied` – input feature
- `Performance Index` – target output

To reduce variance, the dataset was also **grouped by hours studied** and averaged. This created a clearer linear pattern and improved model accuracy.


## Libraries

- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/) 



## Results

| Dataset       | MSE     |
|---------------|---------|
| Raw Data      | 326.37  |
| Grouped Data  | 6.20    |

- The raw data included noisy clusters, making the linear trend difficult to learn.
- Grouping improved the signal-to-noise ratio and revealed a clean, linear relationship.
- The model’s performance improved drastically after preprocessing.