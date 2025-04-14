(arima)
# ARIMA

ARIMA (AutoRegressive Integrated Moving Average) is a powerful statistical model that predicts future values based on patterns in historical data. It's widely used in finance, sales forecasting, weather prediction, and economic analysis.

**How ARIMA Works**

ARIMA consists of three components, which we can understand through temperature forecasting:
1. AR (AutoRegressive): If today is hot, tomorrow is likely to be hot too. Temperature values tend to correlate with recent past values.
2. I (Integrated): If we're in a warming period (like summer), ARIMA removes this trend to focus on the day-to-day patterns.
3. MA (Moving Average): If there was an unexpected temperature spike yesterday (perhaps due to unusual weather), this effect gets smoothed out over time.

**Understanding Differencing**

Differencing is a crucial step that makes non-stationary time series data stationary by removing trends and seasonal patterns. The "I" (Integrated) component in ARIMA refers to this process.

- First differencing ($d=1$) computes the difference between consecutive observations: 

$$\Delta X_t = X_t - X_{t-1}$$

- Second differencing ($d=2$) applies differencing twice: 

$$\Delta^2 X_t = \Delta(\Delta X_t) = (X_t - X_{t-1}) - (X_{t-1} - X_{t-2}) = X_t - 2X_{t-1} + X_{t-2}$$

Higher order differencing follows the same pattern.

**The Complete ARIMA Formula**

For an ARIMA(p,d,q) model:

1. First, apply d-th order differencing to obtain $\Delta^d X_t$
2. Then apply the ARMA(p,q) model to the differenced series:

$$\Delta^d X_t - \alpha_1 \Delta^d X_{t-1} - \cdots - \alpha_p \Delta^d X_{t-p} = \varepsilon_t + \theta_1 \varepsilon_{t-1} + \cdots + \theta_q \varepsilon_{t-q}$$

This can be rewritten as:

$$\Delta^d X_t = \alpha_1 \Delta^d X_{t-1} + \cdots + \alpha_p \Delta^d X_{t-p} + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \cdots + \theta_q \varepsilon_{t-q}$$

Where:
- $\Delta^d X_t$ is the d-times differenced series
- $\alpha_i$ are the parameters of the autoregressive part
- $\theta_j$ are the parameters of the moving average part
- $\varepsilon_t$ are error terms (white noise)

**Worked Example:** ARIMA(2,1,3)

Let's say our temperature time series data begins with: $X_1 = 75, X_2 = 77, X_3 = 76, X_4 = 78, \dots$, where:
- 2 = AR order (using 2 previous observations)
- 1 = Differencing order (taking first differences)
- 3 = MA order (using 3 previous errors)

Step 1: Calculate First Differences
First, we need to difference the data to make it stationary. The first difference is:
$\Delta X_t = X_t - X_{t-1}$

For our temperature data:
- Day 1: 75°F
- Day 2: 77°F, $\Delta X_2 = 77 - 75 = +2$
- Day 3: 76°F, $\Delta X_3 = 76 - 77 = -1$

Step 2: Apply the ARIMA Model
For an ARIMA(2,1,3) model, the equation is:
$\Delta X_t = \alpha_1 \Delta X_{t-1} + \alpha_2 \Delta X_{t-2} + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \theta_2 \varepsilon_{t-2} + \theta_3 \varepsilon_{t-3}$

Where:
- $\alpha_1 = 0.7, \alpha_2 = 0.2$ (AR coefficients)
- $\theta_1 = 0.3, \theta_2 = 0.2, \theta_3 = 0.1$ (MA coefficients)
- $\varepsilon_t$ is the error term

Step 3: Make Predictions
To predict Day 4's temperature:

1. Calculate the expected first difference: 
   $\Delta X_4^{expected} = \alpha_1 \Delta X_3 + \alpha_2 \Delta X_2 + \theta_1 \varepsilon_3 + \theta_2 \varepsilon_2 + \theta_3 \varepsilon_1$
   $\Delta X_4^{expected} = 0.7 \times (-1) + 0.2 \times (+2) + 0.3 \times (-1.2) + 0.2 \times (0) + 0.1 \times (0)$
   $\Delta X_4^{expected} = -0.7 + 0.4 - 0.36 = -0.66$

2. Convert back to temperature: 
   $X_4^{expected} = X_3 + \Delta X_4^{expected} = 76 + (-0.66) = 75.34$

3. Calculate error: 
   $\varepsilon_4 = X_4^{actual} - X_4^{expected} = 78 - 75.34 = 2.66$

Complete Calculation Example for Day 5:

1. AR Component: 
   $\alpha_1 \Delta X_4 + \alpha_2 \Delta X_3 = 0.7 \times (+2) + 0.2 \times (-1) = 1.4 - 0.2 = 1.2$

2. MA Component: 
   $\theta_1 \varepsilon_4 + \theta_2 \varepsilon_3 + \theta_3 \varepsilon_2 = 0.3 \times (2.66) + 0.2 \times (-1.2) + 0.1 \times (0) = 0.798 - 0.24 = 0.558$

3. Expected first difference: 
   $\Delta X_5^{expected} = 1.2 + 0.558 = 1.758$

4. Predicted temperature: 
   $X_5^{expected} = X_4 + \Delta X_5^{expected} = 78 + 1.758 = 79.758$

5. Actual Error: 
   $\varepsilon_5 = X_5^{actual} - X_5^{expected} = 77 - 79.758 = -2.758$

**Temperature Prediction Table**

| Day | Actual Temp | Previous Temp | Diff | Expected Temp | Error | Previous Errors |
|-----|-------------|--------------|------------|--------------|-------|-----------------|
| 1   | 75°F        | -            | -          | -            | -     | -               |
| 2   | 77°F        | 75°F         | +2         | -            | -     | -               |
| 3   | 76°F        | 77°F         | -1         | -            | -1.2  | -               |
| 4   | 78°F        | 76°F         | +2         | 75.34°F      | 2.66  | -1.2, 0, 0      |
| 5   | 77°F        | 78°F         | -1         | 79.76°F      | -2.76 | 2.66, -1.2, 0   |
| 6   | 79°F        | 77°F         | +2         | 76.28°F      | 2.72  | -2.76, 2.66, -1.2 |
| 7   | 78°F        | 79°F         | -1         | 80.39°F      | -2.39 | 2.72, -2.76, 2.66 |
| 8   | 80°F        | 78°F         | +2         | 77.31°F      | 2.69  | -2.39, 2.72, -2.76 |

This example demonstrates how ARIMA incorporates past patterns, adjusts for trends, and accounts for errors to make increasingly accurate temperature predictions over time.

**1-Day Ahead Forecast**

To perform a 1-day ahead temperature forecast using our ARIMA(2,1,3) model, we follow these steps:

1) First, we identify our most recent data points: Day 8 temperature was 80°F and Day 7 was 78°F, giving us a first difference of $\Delta X_8 = +2$.

2) Next, we apply the AR component using our coefficients ($\alpha_1 = 0.7$, $\alpha_2 = 0.2$) and the two most recent first differences:

   $0.7(\Delta X_8) + 0.2(\Delta X_7) = 0.7(+2) + 0.2(-1) = 1.4 - 0.2 = 1.2$

3) Then, we calculate the MA component using our coefficients ($\theta_1 = 0.3$, $\theta_2 = 0.2$, $\theta_3 = 0.1$) and the three most recent error terms:

   $0.3(\varepsilon_8) + 0.2(\varepsilon_7) + 0.1(\varepsilon_6) = 0.3(2.69) + 0.2(-2.39) + 0.1(2.72) = 0.601$

4) We combine these components to get our expected first difference:
   $\Delta X_9^{expected} = \text{AR component} + \text{MA component} = 1.2 + 0.601 = 1.801$

5) Finally, we add this expected difference to our most recent temperature to get our forecast:
   $X_9^{expected} = X_8 + \Delta X_9^{expected} = 80°F + 1.8 = 81.8°F$

Therefore, our 1-day ahead forecast predicts a temperature of approximately 81.8°F for Day 9.

**Limitations**

ARIMA models, despite their popularity, have several notable limitations:
1.	They require stationary data: ARIMA models assume that after differencing, the time series becomes stationary (constant mean, variance, and autocorrelation). This requirement can be difficult to achieve with many real-world datasets.
2.	Linear relationships only: ARIMA models can only capture linear relationships in data, making them less effective for complex, non-linear patterns that are common in many real-world phenomena.
3.	Sensitivity to parameter selection: The performance of an ARIMA model heavily depends on correctly identifying the appropriate p, d, and q parameters, which can be challenging even for experienced analysts.
4.	Struggles with seasonal data: Standard ARIMA doesn't handle seasonality well (though SARIMA, a seasonal extension, addresses this).
5.	Poor with long-term forecasting: ARIMA models tend to converge to the mean for long-term forecasts, making them less reliable for extended prediction horizons.
6.	Limited contextual understanding: These models don't incorporate external variables that might significantly impact the time series (though ARIMAX models attempt to address this).
7.	Computational intensity: Fitting ARIMA models to large datasets can be computationally expensive and time-consuming.
8.	Outlier sensitivity: ARIMA models can be disproportionately influenced by outliers and anomalies in the data.
These limitations have led to the development of more sophisticated approaches, including machine learning methods that can better handle complex, non-linear relationships in time series data.