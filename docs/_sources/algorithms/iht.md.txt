Iterative Hard Thresholding
=============================

The Iterative Hard Thresholding (IHT) algorithm is the sparse analogue of the gradient descent algorithm. After performing the gradient update, it projects a dense vector into a sparse vector. Mathematically speaking, it projects a given vector into a lower dimensional subspace by retaining only the most significant components.

Unlike standard gradient descent which updates all parameters, IHT enforces sparsity by keeping only the s largest (in magnitude) components after each gradient step, setting all other components to zero. This makes IHT particularly useful for problems where the solution is known to be sparse, such as compressed sensing, sparse regression, and sparse signal recovery.

$$
\textbf{Algorithm: Iterative Hard Thresholding (IHT)}
$$

$\textbf{Input:}$ Initial parameter vector $\boldsymbol{\theta}^0 \in \mathbb{R}^n$ satisfying $\|\boldsymbol{\theta}^0\|_0 \leq s$, sparsity level $s$, and stepsize $\gamma > 0$.

$\text{For } k = 0, 1, 2, \dots \text{ do:}$

$$
\mathbf{v}^k = \boldsymbol{\theta}^k - \gamma \nabla f(\boldsymbol{\theta}^k)
$$

$$
\boldsymbol{\theta}^{k+1} = H_s(\mathbf{v}^k),
$$

where $H_s$ is the hard-thresholding operator which is a set-valued operator meaning its ouput is not unique. It sorts the input vector in absolute value and keeps only the $s$ largest entries, setting all others to zero. 
For example, $H_2([1, -3, 1]^\top)=\{[1, -3, 0]^\top, [0, -3, 1]^\top\}$.