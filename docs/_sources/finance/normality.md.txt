(osborne)= 
# Osborne's work (Normality)

**Explaining Osborne's Normality in Quantitative Finance**

**Empirical Foundation**
Maurice Osborne's 1959 [research](https://www.jstor.org/stable/167153?seq=1) added empirical evidence to the use of normality in quantitative finance. Before that, models like Bachelier's and Samuelson's common models weren't grounded in real-world data. Osborne analyzed years of NYSE stock data, focusing on daily log-returns, and found these data closely followed a Gaussian distribution. His research showed that normally distributed log-returns were not just useful math but a realistic way to model price changes—this foundation influenced major financial theories like Markowitz portfolio theory and the Black-Scholes model.

**From Pooled Normality to Individual Returns**

Osborne's work gave quantitative finance the empirical backup needed to assume normality in log-returns. He demonstrated that pooled lagged returns fit a normal distribution, though this doesn't imply individual returns do. To bridge this gap, we make two key assumptions:

1. **Stationarity**: The distribution of returns doesn't change over time, meaning:

   $$\mathbb{E}[r_t]=\mu \quad \text{and} \quad \text{Cov}(r_t,r_{t+h})=C(h)$$

   This allows us to pool returns across time, treating each $r_t$ as a draw from the same distribution.

2. **Exchangeability**: A sequence $\{r_1,...,r_n\}$ is exchangeable if its joint distribution remains unchanged under any reordering. This property:

   - Ensures all returns share an identical marginal distribution
   - Justifies pooling across different assets
   - By de Finetti's theorem, makes the pooled histogram a consistent estimator of the common marginal distribution

Together, these assumptions create a logical pathway:

1. **Osborne's empirical finding**: The pooled distribution of log-returns follows a Gaussian pattern
2. **Stationarity**: Justifies treating returns across different time periods as samples from the same distribution
3. **Exchangeability**: Justifies treating returns across different assets as samples from the same distribution
4. **Parametric modeling**: We choose to model this common distribution as Normal

Therefore, we can conclude:

$$r_t = \ln{\frac{p_t}{p_{t-1}}} \sim N(\mu, \sigma^2)$$

This unified framework explains why, despite Osborne only showing normality in pooled returns, we can reasonably model each individual return as normally distributed.

The following flow chart shows the why Osborne's work can lead to normal distribution for each asset.

```{mermaid}
:align: center
:zoom: 0.6

graph TD;
  A["Osborne’s Study"] -->|Shows Gaussian fit| B["Pooled Distribution"];
  B -->|Shows Gaussian fit| C1["Assumption 1: Stationarity"];
  B -->|Shows Gaussian fit| C2["Assumption 2: Exchangeability"];
  C1 -->|Same distribution over time| D["Common Marginal Distribution"];
  C2 -->|Same distribution across assets| D;
  D -->|Parametric modeling choice| E["Each Return Follows Normal"];

  %% node styles
  classDef blue   fill:#d4f1f9,stroke:#0077be;
  classDef orange fill:#ffe6cc,stroke:#d79b00;
  classDef green  fill:#d5e8d4,stroke:#82b366;

  class A,B blue;
  class C1,C2 orange;
  class D,E green;


