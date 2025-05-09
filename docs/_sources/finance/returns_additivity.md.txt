(additivity)=
# Returns Additivity

Let

* $p_t$ = price at time $t$
* $\hat r_t = \frac{p_t}{p_{t-1}} - 1$ be the actual (arithmetic) return at time $t$
* $r_t = \ln\frac{p_t}{p_{t-1}}$ be the log return at time $t$.

Consider the following table of TQQQ prices for ten trading days and their corresponding returns:

| Period | Date       |    $p_t$    | Actual return $\hat r_t$ | Log return $r_t$ |
| :----: | :--------- | ----------: | :----------------------: | :--------------: |
|    0   | 2025‑04‑25 |       53.86 |             –            |         –        |
|    1   | 2025‑04‑28 |       53.82 |         −0.000743        |     −0.000743    |
|    2   | 2025‑04‑29 |       54.87 |         0.019509         |     0.019322     |
|    3   | 2025‑04‑30 |       54.88 |         0.000182         |     0.000182     |
|    4   | 2025‑05‑01 |       56.77 |         0.034439         |     0.033859     |
|    5   | 2025‑05‑02 |       59.43 |         0.046856         |     0.045791     |
|    6   | 2025‑05‑05 |       58.40 |         −0.017331        |     −0.017483    |
|    7   | 2025‑05‑06 |       56.74 |         −0.028425        |     −0.028836    |
|    8   | 2025‑05‑07 |       57.40 |         0.011632         |     0.011565     |
|    9   | 2025‑05‑08 |       59.11 |         0.029791         |     0.029356     |

**Analysis of Returns**

* **Sum of actual returns:**

  $$
    \sum_{t=1}^{9} \hat r_t
    = -0.000743 + 0.019509 + \cdots + 0.029791
    = 0.09591\;(=9.59\%).
  $$

* **Compounded actual return:**

  $$
    \prod_{t=1}^{9}(1+\hat r_t) - 1
    = 1.02\ldots - 1
    = 0.09747\;(=9.75\%).
  $$

* **Sum of log returns:**

  $$
    \sum_{t=1}^{9} r_t
    = -0.000743 + 0.019322 + \cdots + 0.029356
    = 0.09301\;(=9.30\%).
  $$

* **Converted to actual return:**

  $$
    e^{\sum_{t=1}^{9} r_t} - 1
    = e^{0.09301} - 1
    = 0.09747\;(=9.75\%).
  $$


**Key Insights**

* The sum of log returns equals the log of the total price ratio:
  $\displaystyle \sum_{t=1}^T r_t = \ln\frac{p_T}{p_0}.$
* Exponentiating the sum of log returns reproduces the compounded return.
* Simply summing arithmetic returns (9.59%) underestimates the true compounded return (9.75%).
* The return obtained via exponentiating the sum of log returns (9.75%) and the compounded actual return (9.75%) are effectively identical—showing how closely these methods agree.
* The gap between summed and compounded returns widens with more periods or greater volatility.
