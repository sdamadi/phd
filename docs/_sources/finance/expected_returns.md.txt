(expected-returns)= 
# Expected Returns

In portfolio theory, we define the **sample mean return vector** of $n$ assets ($\hat{\boldsymbol{\mu}} \in \mathbb{R}^n$) (also called the **expected return vector**) as the column‑wise average of each asset’s [log‑returns](log_returns.md#log‑returns) over the sample period. As I explained in [log‑returns](log_returns.md#log‑returns), the term “return” refers to log‑returns. You can read [Osborne's work](normality.md#osborne) to see why we use log‑returns in the first place.

Since you work with log‑returns, recall

$$
r_t^{(i)} \;=\;\ln\!\Bigl(\frac{p^{(i)}_{t+1}}{p^{(i)}_{t}}\Bigr),
$$

which represents the log‑return of the $i$‑th asset on day $t+1$ relative to day $t$.

Assume we observe each asset’s closing price over $T$ consecutive trading days. Because each log‑return compares day $t$ to day $t+1$, this yields $T-1$ returns per asset. You first compute the $T-1$ log‑returns for each of the $n$ assets, and then stack them column‑wise into the $(T-1)\times n$ return matrix

$$
\mathbf R
=
\begin{bmatrix}
\mathbf r^{(1)} & \mathbf r^{(2)} & \cdots & \mathbf r^{(n)}
\end{bmatrix},
$$

with

$$
\mathbf r^{(i)}
=
\begin{pmatrix}
r_1^{(i)}&
r_2^{(i)}&
\cdots&
r_{T-1}^{(i)}
\end{pmatrix}^{\top}.
$$

Finally, taking the mean of each column gives the mean‐return vector

$$
\hat{\boldsymbol\mu}
=
\frac{1}{T-1}
\begin{pmatrix}
\hat{\mu}^{(1)}&
\hat{\mu}^{(2)}&
\cdots&
\hat{\mu}^{(n)}
\end{pmatrix}^{\top}
$$

where $\hat{\mu}^{(i)}=\frac{1}{T-1}\sum_{t=1}^{T-1}r_t^{(i)}.$

Another way to compute it is via the matrix‑vector product:

$$
\hat{\boldsymbol{\mu}} \;=\;\frac{1}{T-1}\,\mathbf{R}^{\top}\mathbf{1},
$$

where $\mathbf{1}$ is a vector of ones.

---

**Numerical Example**

To illustrate these steps in practice, consider a simple example. We have daily closing prices for six assets over a ten‑day period. First, we construct the price table and then compute the corresponding log‑returns. Finally, by averaging each asset’s log‑returns, we obtain the mean return vector shown below.

---

**Stock Prices Table**

| Date       | AAPL   | AMZN   | GOOG   | MSFT   | TQQQ  | TSLA   |
| ---------- | ------ | ------ | ------ | ------ | ----- | ------ |
| 2025‑04‑28 | 210.14 | 187.70 | 162.42 | 391.16 | 53.82 | 285.88 |
| 2025‑04‑29 | 211.21 | 187.39 | 162.06 | 394.04 | 54.87 | 292.03 |
| 2025‑04‑30 | 212.50 | 184.42 | 160.89 | 395.26 | 54.88 | 282.16 |
| 2025‑05‑01 | 213.32 | 190.20 | 162.79 | 425.40 | 56.77 | 280.52 |
| 2025‑05‑02 | 205.35 | 189.98 | 165.81 | 435.28 | 59.43 | 287.21 |
| 2025‑05‑05 | 198.89 | 186.35 | 166.05 | 436.17 | 58.40 | 280.26 |
| 2025‑05‑06 | 198.51 | 185.01 | 165.20 | 433.31 | 56.74 | 275.35 |
| 2025‑05‑07 | 196.25 | 188.71 | 152.80 | 433.35 | 57.40 | 276.22 |
| 2025‑05‑08 | 197.49 | 192.08 | 155.75 | 438.17 | 59.11 | 284.82 |
| 2025‑05‑09 | 198.53 | 193.06 | 154.38 | 438.73 | 58.97 | 298.26 |

**Log‑Returns Table**

| Date       | AAPL    | AMZN    | GOOG    | MSFT    | TQQQ    | TSLA    |
| ---------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 2025‑04‑29 | 0.0051  | −0.0017 | −0.0022 | 0.0073  | 0.0193  | 0.0213  |
| 2025‑04‑30 | 0.0061  | −0.0160 | −0.0072 | 0.0031  | 0.0002  | −0.0344 |
| 2025‑05‑01 | 0.0039  | 0.0309  | 0.0117  | 0.0735  | 0.0339  | −0.0058 |
| 2025‑05‑02 | −0.0381 | −0.0012 | 0.0184  | 0.0230  | 0.0458  | 0.0236  |
| 2025‑05‑05 | −0.0320 | −0.0193 | 0.0014  | 0.0020  | −0.0175 | −0.0245 |
| 2025‑05‑06 | −0.0019 | −0.0072 | −0.0051 | −0.0066 | −0.0288 | −0.0177 |
| 2025‑05‑07 | −0.0115 | 0.0198  | −0.0780 | 0.0001  | 0.0116  | 0.0032  |
| 2025‑05‑08 | 0.0063  | 0.0177  | 0.0191  | 0.0111  | 0.0294  | 0.0307  |
| 2025‑05‑09 | 0.0053  | 0.0051  | −0.0088 | 0.0013  | −0.0024 | 0.0461  |

---

The sample mean return vector is:

$$
\hat{\boldsymbol{\mu}} \;=\;[-0.0063,\;0.0031,\;-0.0056,\;0.0128,\;0.0102,\;0.0047]^{\!\top}.
$$

This means that over this 10‑day period:

* Apple (AAPL) decreased by 0.63 % on average
* Amazon (AMZN) increased by 0.31 % on average
* Google (GOOG) decreased by 0.56 % on average
* Microsoft (MSFT) increased by 1.28 % on average
* TQQQ increased by 1.02 % on average
* Tesla (TSLA) increased by 0.47 % on average
