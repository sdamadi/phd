# One-Layer NN (Logistic Regression)

The goal of this document is to show that **logistic regression** is exactly a neural network with a single layer, a sigmoid activation, and the binary cross-entropy loss.

**Model definition**

Logistic regression models the probability that $y=1$ given inputs $\mathbf{x}=(x_1,\dots,x_n)$ by
$
\hat p(\mathbf{x}) \;=\;\sigma\!\bigl(\theta_0 + \theta_1 x_1 + \dots + \theta_n x_n\bigr),
\qquad
\sigma(z)=\frac1{1+e^{-z}}.
$


Equivalently, if we write
$\tilde{\mathbf x}=[1,\,x_1,\dots,x_n]$ and $\boldsymbol\theta=[\theta_0,\theta_1,\dots,\theta_n]^\top$, then
$
\hat p^{(i)}
=\sigma\bigl(\tilde{\mathbf x}^{(i)\top}\boldsymbol\theta\bigr).
$

**Data**

We observe $N$ samples $\{(\mathbf x^{(i)},y^{(i)})\}_{i=1}^N$, where each $y^{(i)}\in\{0,1\}$.  
For example, if $N=5$ and $n=3$:

| $x_1$ | $x_2$ | $x_3$ | $y$ |
|:-------:|:-------:|:-------:|:-----:|
| $x_1^{(1)}$ | $x_2^{(1)}$ | $x_3^{(1)}$ | $y^{(1)}$ |
| $x_1^{(2)}$ | $x_2^{(2)}$ | $x_3^{(2)}$ | $y^{(2)}$ |
| $x_1^{(3)}$ | $x_2^{(3)}$ | $x_3^{(3)}$ | $y^{(3)}$ |
| $x_1^{(4)}$ | $x_2^{(4)}$ | $x_3^{(4)}$ | $y^{(4)}$ |
| $x_1^{(5)}$ | $x_2^{(5)}$ | $x_3^{(5)}$ | $y^{(5)}$ |

As before, stack these into
$\tilde{\mathbf X} = [\mathbf1\;\;\mathbf X]\in\mathbb R^{N\times(n+1)}$
and $\mathbf y=(y^{(1)},\dots,y^{(N)})^\top$.

**Maximum Likelihood Estimation**

Logistic regression fits $\boldsymbol\theta$ by maximizing the likelihood function. For binary classification with $y^{(i)}\in\{0,1\}$, we can write the likelihood as:

$
\begin{aligned}
\mathcal{L}(\boldsymbol\theta) &= \prod_{i=1}^N (\hat p^{(i)})^{y^{(i)}} (1-\hat p^{(i)})^{1-y^{(i)}}
\end{aligned}
$

This expresses the probability of observing our dataset under the model. Taking the logarithm (which preserves the maximum):

$
\begin{aligned}
\log\mathcal{L}(\boldsymbol\theta) &= \sum_{i=1}^N \Bigl[y^{(i)}\log\hat p^{(i)} + (1-y^{(i)})\log(1-\hat p^{(i)})\Bigr]
\end{aligned}
$

Substituting $\hat p^{(i)} = \sigma(\tilde{\mathbf{x}}^{(i)\top}\boldsymbol\theta)$ and simplifying:

$
\begin{aligned}
\log\mathcal{L}(\boldsymbol\theta) &= \sum_{i=1}^N \Bigl[y^{(i)}\log\sigma(\tilde{\mathbf{x}}^{(i)\top}\boldsymbol\theta) + (1-y^{(i)})\log(1-\sigma(\tilde{\mathbf{x}}^{(i)\top}\boldsymbol\theta))\Bigr] \\
&= \sum_{i=1}^N \Bigl[y^{(i)}\tilde{\mathbf{x}}^{(i)\top}\boldsymbol\theta - \log(1+e^{\tilde{\mathbf{x}}^{(i)\top}\boldsymbol\theta})\Bigr]
\end{aligned}
$

In practice, we often minimize the negative log-likelihood (divided by N to get the average):

$
\begin{aligned}
-\frac{1}{N}\log\mathcal{L}(\boldsymbol\theta) &= \frac{1}{N}\sum_{i=1}^N \Bigl[\log(1+e^{\tilde{\mathbf{x}}^{(i)\top}\boldsymbol\theta}) - y^{(i)}\tilde{\mathbf{x}}^{(i)\top}\boldsymbol\theta\Bigr].
\end{aligned}
$

Therefore, 

$$
\boldsymbol\theta^* \in \text{Argmax}_{\boldsymbol\theta} \frac{1}{N}\sum_{i=1}^N \Bigl[\log(1+e^{\tilde{\mathbf{x}}^{(i)\top}\boldsymbol\theta}) - y^{(i)}\tilde{\mathbf{x}}^{(i)\top}\boldsymbol\theta\Bigr].
$$

**Neural-network view**

Notice that we can represent logistic regression as a single-layer neural network with a sigmoid activation function. This is exactly analogous to how we represented linear regression as a single-layer neural network with no activation function (or identity).

<figure style="text-align:center;">
  <img src=src="/phd/_static/images/one_layer/logistic_regression.svg" alt="Logistic regression as a one-layer neural network" width="40%">
  <figcaption>Logistic regression as a one-layer neural network.</figcaption>
</figure>

In this network:
* **Input nodes**: $x_1, x_2, \ldots, x_n$ (shown in purple)
* **Weights**: $w_j = \theta_j$ for $j=1,\ldots,n$
* **Bias**: $b = \theta_0$
* **Summation node**: Computes $z = \sum_{j=1}^n w_j x_j + b$ (shown as the green "+" symbol)
* **Activation function**: Sigmoid $\sigma(z) = \frac{1}{1+e^{-z}}$
* **Output**: $\hat{y} = \hat{p} = \sigma(z)$

The forward propagation through this network is:

$$
\begin{aligned}
z^{(i)} &= \mathbf{w}^\top\mathbf{x}^{(i)} + b \\
&= w_1 x_1^{(i)} + w_2 x_2^{(i)} + \ldots + w_n x_n^{(i)} + b \\
&= \theta_1 x_1^{(i)} + \theta_2 x_2^{(i)} + \ldots + \theta_n x_n^{(i)} + \theta_0 \\
&= \tilde{\mathbf{x}}^{(i)\top}\boldsymbol{\theta}
\end{aligned}
$$

And the final output is:

$$
\hat{p}^{(i)} = \sigma(z^{(i)}) = \sigma(\tilde{\mathbf{x}}^{(i)\top}\boldsymbol{\theta})
$$

This is identical to the logistic regression formula we defined at the beginning.

When training this neural network, we use the binary cross-entropy loss:

$$
\text{BCE}(\hat{p}^{(i)}, y^{(i)}) = -[y^{(i)}\log\hat{p}^{(i)} + (1-y^{(i)})\log(1-\hat{p}^{(i)})]
$$

Let's show that minimizing this BCE loss in the neural network is equivalent to maximizing the likelihood in logistic regression:

$$
\begin{aligned}
\text{BCE}(\hat{p}^{(i)}, y^{(i)}) &= -[y^{(i)}\log\sigma(z^{(i)}) + (1-y^{(i)})\log(1-\sigma(z^{(i)}))]
\end{aligned}
$$

This is exactly the negative log-likelihood for a single observation. Summing over all observations and dividing by N:

$$
\begin{aligned}
\frac{1}{N}\sum_{i=1}^{N}\text{BCE}(\hat{p}^{(i)}, y^{(i)}) &= -\frac{1}{N}\sum_{i=1}^{N}[y^{(i)}\log\sigma(z^{(i)}) + (1-y^{(i)})\log(1-\sigma(z^{(i)}))] \\
&= -\frac{1}{N}\log\mathcal{L}(\boldsymbol{\theta})
\end{aligned}
$$

So minimizing the average binary cross-entropy loss in the neural network is mathematically equivalent to maximizing the likelihood function in the statistical formulation of logistic regression.

Using the substitution $z^{(i)} = \tilde{\mathbf{x}}^{(i)\top}\boldsymbol{\theta}$ and simplifying:

$$
\begin{aligned}
\frac{1}{N}\sum_{i=1}^{N}\text{BCE}(\hat{p}^{(i)}, y^{(i)}) &= \frac{1}{N}\sum_{i=1}^{N}[\log(1+e^{\tilde{\mathbf{x}}^{(i)\top}\boldsymbol{\theta}}) - y^{(i)}\tilde{\mathbf{x}}^{(i)\top}\boldsymbol{\theta}].
\end{aligned}
$$

**Key takeaway** 

**Logistic regression** = **one-layer neural network**
* **Activation:** sigmoid
* **Loss/Objective:** binary cross-entropy (equivalent to negative log-likelihood)

This shows that, just as linear regression is a single-layer neural network with identity activation and MSE loss, logistic regression is nothing more than the simplest possible neural network for binary classification with a sigmoid activation and binary cross-entropy loss.

The main differences between linear regression and logistic regression as neural networks are:
1. Linear regression uses no activation function (or identity), while logistic regression uses the sigmoid function
2. Linear regression uses MSE loss, while logistic regression uses binary cross-entropy (which corresponds to maximum likelihood estimation)
3. Linear regression predicts continuous values, while logistic regression predicts probabilities for binary classification

This connection illustrates how neural networks naturally extend traditional statistical methods, with the optimization objective (maximizing likelihood in statistics or minimizing loss in neural networks) being mathematically equivalent formulations of the same goal.