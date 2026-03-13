# Linear Regressor

A simple implementation of **linear regression** trained using **gradient descent**.

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
