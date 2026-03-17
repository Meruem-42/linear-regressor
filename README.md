# Linear Regressor

*A simple implementation of linear regression trained using gradient descent*.

---

# Model

The linear regression model predicts a value \( \hat{y} \) from an input feature \( x \).

$$
\hat{y} = \theta_0 + \theta_1 x
$$

Where:

- \( \theta_0 \) : intercept (bias)
- \( \theta_1 \) : slope (weight)
- \( x \) : input feature
- \( \hat{y} \) : predicted value

---

# Normalization

Normalize data in case of different magnitudes for features which could makes it more difficult for the model to converge or even makes it diverge.

---

# Cost Function

The model is trained by minimizing the **Mean Squared Error (MSE)** cost function.

$$
J(\theta_0, \theta_1) =
\frac{1}{2m}
\sum_{i=1}^{m}
(\theta_0 + \theta_1 x^{(i)} - y^{(i)})^2
$$

Where:

- \( m \) : number of training examples
- \( y^{(i)} \) : true value
- \( x^{(i)} \) : input feature for sample \( i \)

---

# Gradient Calculation

To minimize the cost function, we compute the **partial derivatives** of $J$.

## Gradient with respect to $\theta_0$

$$
\frac{\partial J}{\partial \theta_0} = \frac{1}{m} \sum_{i=1}^{m} (\theta_0 + \theta_1 x^{(i)} - y^{(i)})
$$

## Gradient with respect to $\theta_1$

$$
\frac{\partial J}{\partial \theta_1} = \frac{1}{m} \sum_{i=1}^{m} (\theta_0 + \theta_1 x^{(i)} - y^{(i)})x^{(i)}
$$

---

# Feature Normalization

To make gradient descent converge faster and more reliably, input features are scaled using **Min-Max Normalization**.

$$
x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$$

Where:

- $x$ : original feature value
- $x_{\min}$ : minimum value of the feature
- $x_{\max}$ : maximum value of the feature
- $x'$ : normalized feature value, scaled to $[0, 1]$

---

# Gradient Descent Update Rule

The parameters are updated iteratively using gradient descent.

Let \( \alpha \) be the **learning rate**.

## Update for \( \theta_0 \)

$$
\theta_0 :=
\theta_0 - \alpha
\frac{1}{m}
\sum_{i=1}^{m}
(\theta_0 + \theta_1 x^{(i)} - y^{(i)})
$$

## Update for \( \theta_1 \)

$$
\theta_1 :=
\theta_1 - \alpha
\frac{1}{m}
\sum_{i=1}^{m}
(\theta_0 + \theta_1 x^{(i)} - y^{(i)})x^{(i)}
$$

---

# Evaluating

To assess model performance, the following regression metrics are commonly used.

## Mean Absolute Error (MAE)

$$
\mathrm{MAE} = \frac{1}{m}\sum_{i=1}^{m} \left| y^{(i)} - \hat{y}^{(i)} \right|
$$

## Mean Squared Error (MSE)

$$
\mathrm{MSE} = \frac{1}{m}\sum_{i=1}^{m} \left( y^{(i)} - \hat{y}^{(i)} \right)^2
$$

## Root Mean Squared Error (RMSE)

$$
\mathrm{RMSE} = \sqrt{\frac{1}{m}\sum_{i=1}^{m} \left( y^{(i)} - \hat{y}^{(i)} \right)^2}
$$

## Coefficient of Determination ($R^2$)

$$
R^2 = 1 - \frac{\sum_{i=1}^{m} \left( y^{(i)} - \hat{y}^{(i)} \right)^2}{\sum_{i=1}^{m} \left( y^{(i)} - \bar{y} \right)^2}
$$

Where:

- $\hat{y}^{(i)}$ : predicted value for sample $i$
- $y^{(i)}$ : true value for sample $i$
- $\bar{y}$ : mean of true values
- $m$ : number of samples

---
