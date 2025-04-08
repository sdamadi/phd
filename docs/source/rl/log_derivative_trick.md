(log-derivative)= 
# Log-derivative formula

The $\log$-derivative formula states that for a function composition involving logarithms:

$$\frac{d}{dx}\log(f(x)) = \frac{1}{f(x)} \frac{df(x)}{dx}.$$

If we have a function $f(\mathbf{x})$ ($\mathbf{x} \in \mathbb{R}^n$) and we're looking for the gradient of $\log(f(\mathbf{x}))$, we can apply the $\log$-derivative formula in the multivariable setting:

$$\nabla_{\mathbf{x}} \log(f(\mathbf{x})) = \frac{1}{f(\mathbf{x})} \nabla_{\mathbf{x}} f(\mathbf{x})$$

This is the vector calculus equivalent of the scalar $\log$-derivative formula. The gradient $\nabla_{\mathbf{x}}$ gives us a vector of partial derivatives with respect to each component of $\mathbf{x}$.

For each component $x_i$ of the vector $\mathbf{x}$, we have:

$$\frac{\partial}{\partial x_i} \log(f(\mathbf{x})) = \frac{1}{f(\mathbf{x})} \frac{\partial f(\mathbf{x})}{\partial x_i}$$

So the full gradient is:

$$\nabla_{\mathbf{x}} \log(f(\mathbf{x})) = \frac{1}{f(\mathbf{x})} \begin{bmatrix} 
\frac{\partial f(\mathbf{x})}{\partial x_1} \\
\frac{\partial f(\mathbf{x})}{\partial x_2} \\
\vdots \\
\frac{\partial f(\mathbf{x})}{\partial x_n}
\end{bmatrix}$$

This generalizes the scalar $\log$-derivative to the vector setting, maintaining the same core principle: the gradient of the logarithm of a function equals the gradient of the function divided by the function itself.