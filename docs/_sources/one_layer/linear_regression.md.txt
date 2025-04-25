# One-Layer NN (Linear Regression)

The goal of the following document is to show linear regression is just a neural network with a single layer with no activation function (or identity) where the final loss function is the mean squared error.

To see the above, let's recall what is the goal of linear regression. It tries to model the output $y$ as the linear combinations of inputs plus a constant term, i.e.,

$$
y=\theta_0 + \theta_1 x_1 + \dots + \theta_n x_n
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

This table represents our dataset with 5 samples ($N=5$) and 3 features ($n=3$), where each row contains the input features and corresponding output value.

Then we can put $x$ values and create the data matrix $\mathbf{X}$ and take the column of $y$ and create the output vector $\mathbf{y}$. Thus, one needs to minimize the following to find the best $\boldsymbol{\theta}$:


$$
\|\tilde{\mathbf{X}}\boldsymbol{\theta} - \mathbf{y}\|^2,
$$

where 

$$
\tilde{\mathbf{X}} = 
\begin{bmatrix}
\mathbf{1} &
\mathbf{X}
\end{bmatrix},
$$

with $\mathbf{1}$ is a column of ones,
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