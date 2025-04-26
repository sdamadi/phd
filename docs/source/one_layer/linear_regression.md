# One-Layer NN (Linear Regression)

The goal of the following document is to show linear regression is just a neural network with a single layer with no activation function (or identity) where the final loss function is the mean squared error.

To see the above, let's recall what is the goal of linear regression. It tries to find a linear model whose output $\hat{y}$ is the linear combinations of inputs plus a constant term, i.e.,

$$
\hat{y}=\theta_0 + \theta_1 x_1 + \dots + \theta_n x_n
$$

When we collect data, we have $N$ such $(x_1^{(i)}, x_2^{(i)},\dots, x_n^{(i)})$
for each $y^{(i)}$ where $i=1, \dots, N$.

Suppose $N=5$, $n=3$, then we have the following table.


| $x_1$ | $x_2$ | $x_3$ | $y$ |
|-------|-------|-------|-----|
| $x_1^{(1)}$ | $x_2^{(1)}$ | $x_3^{(1)}$ | $y^{(1)}$ |
| $x_1^{(2)}$ | $x_2^{(2)}$ | $x_3^{(2)}$ | $y^{(2)}$ |
| $x_1^{(3)}$ | $x_2^{(3)}$ | $x_3^{(3)}$ | $y^{(3)}$ |
| $x_1^{(4)}$ | $x_2^{(4)}$ | $x_3^{(4)}$ | $y^{(4)}$ |
| $x_1^{(5)}$ | $x_2^{(5)}$ | $x_3^{(5)}$ | $y^{(5)}$ |

This table represents our dataset with 5 samples ($N=5$) and 3 features ($n=3$), where each row contains the input features and corresponding label value.

Then we can stack $x$ values together and create the data matrix $\mathbf{X}$ and take the column of $y$ and create the label vector $\mathbf{y}$. Thus, one needs to minimize the following to find the best $\boldsymbol{\theta}$:


$$
\|\mathbf{\hat{y}} - \mathbf{y}\|^2 = \|\tilde{\mathbf{X}}\boldsymbol{\theta} - \mathbf{y}\|^2,
$$

where $\mathbf{\hat{y}}$ is the model output vector, 

$$
\tilde{\mathbf{X}}= 
\begin{bmatrix}
\mathbf{1} &
\mathbf{X}
\end{bmatrix},
$$

with $\mathbf{1}$ as a column of ones,
and 
$\boldsymbol{\theta}=[\theta_0, \theta_1, \dots, \theta_n]^{\top}$.


Notice that we can write the above as follows:

$$
\begin{aligned}
\|\tilde{\mathbf{X}}\boldsymbol{\theta} - \mathbf{y}\|^2
&=
\|
\begin{bmatrix}
\tilde{\mathbf{X}}_{1\bullet}\\
\tilde{\mathbf{X}}_{2\bullet}\\
\vdots\\
\tilde{\mathbf{X}}_{N\bullet}
\end{bmatrix}\boldsymbol{\theta}
-
\begin{bmatrix}
y_{1}\\
y_{2}\\
\vdots\\
y_{N}
\end{bmatrix}
\|^2
\\
&=
\|
\begin{bmatrix}
\tilde{\mathbf{X}}_{1\bullet}\boldsymbol{\theta} - y_{1}\\
\vdots\\
\tilde{\mathbf{X}}_{N\bullet}\boldsymbol{\theta} - y_{N}
\end{bmatrix}
\|^2
\\
&=
(\tilde{\mathbf{X}}_{1\bullet}\boldsymbol{\theta} - y_{1})^2
+ \dots +
(\tilde{\mathbf{X}}_{N\bullet}\boldsymbol{\theta} - y_{N})^2
\\
&=
\sum_{i=1}^{N} (\tilde{\mathbf{X}}_{i\bullet}\boldsymbol{\theta} - y_{i})^2
\\
&=
\sum_{i=1}^{N} \text{MSE}(\tilde{\mathbf{X}}_{i\bullet}\boldsymbol{\theta} - y_{i})
\\
&=
\sum_{i=1}^{N} l_i(\boldsymbol{\theta}),
\end{aligned}
$$

where $\text{MSE}$ is the mean squared error loss funciton.

Sounds very complicated, but if you notice, you can see that the following neural network does the same thing where $\mathbf{w}=[\theta_1, \dots, \theta_n]$ and $b=\theta_0$. This single-layer neural network with no activation function (or using the identity function) and MSE loss is mathematically equivalent to linear regression.

<figure style="text-align: center;">
  <img src="/phd/_static/images/one_layer/linear_regression.svg" alt="Linear regression as a one-layer neural network" width="40%">
  <figcaption>Linear regression as a one-layer neural network.</figcaption>
</figure>


The image shows a single-layer neural network with:

* Input nodes ($x_1$, $x_2$, ..., $x_n$) in purple
* Weights connecting the inputs to the output ($w_1$, $w_2$, ..., $w_n$)
* A bias term $b$
* A summation node (the green + symbol)
* An output $\hat{y}$

In this formulation, the neural network directly computes:

$$\hat{y} = w_1x_1 + w_2x_2 + ... + w_nx_n + b$$

This is identical to the linear regression formula:

$$y = \theta_0 + \theta_1x_1 + \theta_2x_2 + ... + \theta_nx_n$$

Where:
* The bias $b$ in the neural network corresponds to $\theta_0$ in linear regression
* The weights $w_1$, $w_2$, ..., $w_n$ correspond to $\theta_1$, $\theta_2$, ..., $\theta_n$

When using MSE (Mean Squared Error) as the loss function, we're essentially minimizing:

$$\sum_{i=1}^{N}(\hat{y}_i - y_i)^2 = \sum_{i=1}^{N}(\mathbf{w}\cdot\mathbf{x}^{(i)} + b - y^{(i)})^2$$

Which is exactly the same optimization objective as in standard linear regression.

The key insight is that while neural networks typically use non-linear activation functions to model complex relationships, when you use:
1. A single layer
2. No activation function (or the identity function)
3. MSE as the loss function

You end up with precisely the mathematical formulation of linear regression. This demonstrates that linear regression is essentially the simplest possible neural network.
