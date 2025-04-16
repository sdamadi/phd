# One-layer neural network
A one-layer neural network architecture provides a lot of insights about fundamental understanding concepts like parameters, training, the role of loss function, backpropagation, and so on. Consider a one-layer neural network that has 4 inputs and 3 outputs as follows.

<figure style="text-align: center;">
  <img src="/phd/_static/images/one_layer/sing_layer_arch_wx.svg" alt="A one-layer neural network architecture" width="40%">
  <figcaption>A one-layer neural network architecture.</figcaption>
</figure>


**Parameters**

The size of the input and output determines the parameter set of this neural network. Since it has only a single linear layer, the output can be written as 

$$
\mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b},
$$
where $\mathbf{W}$ and $\mathbf{b}$ are weight matrix and bias vector of the network with sizes that are determined by the input and output size. Thus,

$$
\mathbf{W}=
\begin{bmatrix}
w_{11} & w_{12} & w_{13} & w_{14} \\
w_{21} & w_{22} & w_{23} & w_{24} \\
w_{31} & w_{32} & w_{33} & w_{34} \\
\end{bmatrix}
,
\mathbf{b}=
\begin{bmatrix}
b_{1} \\ b_{2} \\ b_{3}
\end{bmatrix}.
$$

The vector $\mathbf{z}$ is called logit.

**Loss function**

The above is only how we define the architecture of the network. Therefore, it is not considered as a neural network model. To convert any neural network architecture, we need to have a loss function that has to be a scalar-valued function. Notice, that right now the architecture returns a vector in $\mathbb{R}^3$.

Suppose the loss function is the cross-entropy function. This function measures how close two probability vectors are to one another. However, the problem is that logit vector is not a probability vector and we need to convert it to a probability vector. Transforming the logit vector to a probability vector is done by a softmax function (vector-valued) that simply raises each component to $e$ and divides by the sum of them as follows:

$$
\hat{\mathbf{y}}
=
\text{softmax}(\mathbf{z})
=
\begin{bmatrix}
\frac{e^{z_1}}{e^{z_1}+e^{z_2}+e^{z_3}}
\\
\frac{e^{z_2}}{e^{z_1}+e^{z_2}+e^{z_3}}
\\
\frac{e^{z_3}}{e^{z_1}+e^{z_2}+e^{z_3}}
\end{bmatrix}.
$$

The vector $\hat{\mathbf{y}}$ is now the output of the single layer neural network as the picture shows. 

<figure style="text-align: center;">
  <img src="/phd/_static/images/one_layer/sing_layer_model_wx.svg" alt="A one-layer neural network model" width="40%">
  <figcaption>A one-layer neural network model.</figcaption>
</figure>

Note that transformations that convert logit vectors of layers of a neural network are called activation functions. Thus, the above softmax function is an activation function.

Finally, we can write

$$
l
(
\mathbf{y}, \hat{\mathbf{y}}
)
=
\text{CE}
\Big(
\text{softmax}(
\mathbf{W}\mathbf{x}+\mathbf{b}), \mathbf{y}
\Big)
=
l
\Big(
\mathbf{f}(\mathbf{W}\mathbf{x}+\mathbf{b}), \mathbf{y}
\Big),
$$
where $\mathbf{f}:\mathbb{R}^3 \to (0,1)^3$ is $f(\mathbf{z})=\text{softmax}(\mathbf{z})$ that takes any arbitrary vector in $\mathbb{R}^3$ and maps it to a probability vector in $\mathbb{R}^3$. Notice that, a softmax function cannot provide zero or one in its components.

**Optimization**

Once we have a scalar-valued function we can minimize it using optimization algorithms like gradient descent. Algebraically speaking, we can minimize the following:

$$
\min_{\mathbf{W}\in \mathbb{R}^{3\times 4}, \mathbf{b} \in \mathbb{R}^3}
\text{CE}
\Big(
\text{softmax}(
\mathbf{W}\mathbf{x}+\mathbf{b}), \mathbf{y}
\Big),
$$
where $\mathbf{x}$ is a given data vector in $\mathbb{R}^{4}$ with its corresponding label

$$
\mathbf{y} \in \Big\{
\begin{bmatrix}
1
\\
0
\\
0
\end{bmatrix}
,
\begin{bmatrix}
0
\\
1
\\
0
\end{bmatrix}
,
\begin{bmatrix}
0
\\
0
\\
1
\end{bmatrix}
\Big\}.
$$

For sure minimizing the above is theoretically possible, but in practice we are given an $N$ set of pairs of data $\{(\mathbf{x}^{(1)}, \mathbf{y}^{(1)}), \dots, (\mathbf{x}^{(N)}, \mathbf{y}^{(N)})\}$. By looking at the above we can see that the loss now can be defined as the average loss over all data points
as follows

$$
\ell(X, Y, \mathbf{W}, \mathbf{b})
=
\frac{1}{N}
\sum_{i=1}^N
\text{CE}
\Big(
\text{softmax}(
\mathbf{W}\mathbf{x^{(i)}}+\mathbf{b}), \mathbf{y}^{(i)}
\Big),
$$
where 

$
X=\{\mathbf{x}^{(1)}, \dots, \mathbf{x}^{(N)}\}
$
and
$
Y=\{\mathbf{y}^{(1)}, \dots, \mathbf{y}^{(N)}\}.
$

For notational simplicity, $\ell(X, Y, \mathbf{W}, \mathbf{b})$ is usually written as
$\ell(\boldsymbol{\theta})$ where $\boldsymbol{\theta}=\{\mathbf{W}, \mathbf{b}\}$. Also, the loss associated to a data point $l
(
\mathbf{y}^{(i)}, \hat{\mathbf{y}}^{(i)}
)$
is written as $l_i
(
\boldsymbol{\theta}
)$.
Thus,

$$
\ell(\boldsymbol{\theta})
=
\frac{1}{N}
\sum_{i=1}^N
l_i
(
\boldsymbol{\theta}
)
=
\frac{1}{N}
\sum_{i=1}^N
\text{CE}
\Big(
\text{softmax}(
\mathbf{W}\mathbf{x^{(i)}}+\mathbf{b}), \mathbf{y}^{(i)}
\Big)
$$

Finally we can minimize the loss function as follows:

$$
\min_{\boldsymbol{\theta}}
\ell(\boldsymbol{\theta})
=
\min_{\mathbf{W}\in \mathbb{R}^{3\times 4}, \mathbf{b} \in \mathbb{R}^3}
\frac{1}{N}
\sum_{i=1}^N
\text{CE}
\Big(
\text{softmax}(
\mathbf{W}\mathbf{x^{(i)}}+\mathbf{b}), \mathbf{y}^{(i)}
\Big).
$$