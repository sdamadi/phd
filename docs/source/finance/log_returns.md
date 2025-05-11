(log-returns)=
# Log-returns

In practice, most portfolio‑optimization and tracking models (mean–variance, index‑tracking, risk‑parity, etc.) are estimated on **logarithmic returns** rather than simple (arithmetic) returns. 

This is well-justified by [Osborne's seminal work](normality.md#osborne) on Brownian motion in stock markets (1959), which demonstrated that logarithmic returns tend to follow a normal distribution. This property not only provides mathematical convenience but also aligns with the empirical observation of how price changes propagate through financial markets.

Here are some convenient statistical and mathematical properties:


**Time‑additivity (continuous compounding)**

If you define the one‐period log‐return as
$r_t = \ln\frac{p_t}{p_{t-1}},$
then over multiple periods the total log‐return is simply the sum
$\ln\frac{p_T}{p_0} = \sum_{t=1}^T r_t.$
By contrast, arithmetic returns must be compounded multiplicatively, which complicates multi‐period aggregation. Check [the example](returns_additivity.md#additivity) on the additivity of returns.

**Approximate Normality**

Empirically, log‐returns tend to be (more) bell‐shaped and closer to Gaussian—especially at daily or lower frequencies—making the classic Markowitz mean–variance framework (which assumes normality) more sound. If returns are normally distributed, then mean and variance capture everything about the distribution.

**Stationarity of Volatility**

Log‐returns often exhibit more stable variances over time, which leads to more reliable estimates of the covariance matrix $\Sigma$. Stable covariances are crucial when you solve

- Mean-Variance Optimization

$$\min_{\mathbf{w}\geq 0, \mathbf{w}^{\top}\mathbf{w}=1}\;\;\lambda \mathbf{w}^{\top}\Sigma\,\mathbf{w} - \boldsymbol{\mu}^\top \mathbf{w}$$

- Tracking Error Minimization

$$\min_{\mathbf{w}\geq 0, \mathbf{w}^{\top}\mathbf{w}=1}\;\;\|\mathbf{R}\mathbf{w} - \mathbf{r}\|^2.$$


**Symmetry and Unboundedness**

With simple returns, losses are bounded at $-100\%$ but gains are unbounded, skewing distributional estimates. Log‐returns are symmetric in that they map $(0,\infty)$ price ratios onto $(-\infty,\infty)$, which simplifies many risk‐metric calculations. Because $\hat r_t = \tfrac{p_t}{p_{t-1}} - 1$ is limited to $[-1,\infty)$—compressing all negative losses into $[-1,0)$ (at most -%100 loss) while permitting unbounded gains—the distribution of $\hat r_t$ is right‑skewed; by contrast, log-returns

$$
r_t = \ln\frac{p_t}{p_{t-1}}
$$

provide a one‑to‑one mapping of price ratios $(0,\infty)$ onto $(-\infty,\infty)$, yielding a symmetric support.


**Analytical Convenience**

Many closed‐form results (e.g. formulas for risk contributions in a risk‐parity portfolio) become algebraically cleaner when expressed in terms of log‐returns.

In short, using log‐returns makes your inputs more additive, more Gaussian, and more stable—properties that directly improve the robustness and tractability of mean–variance, index‐tracking, and risk‐parity optimizations.
