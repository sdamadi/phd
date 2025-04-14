# GARCH

GARCH (Generalized AutoRegressive Conditional Heteroskedasticity) is a powerful statistical model that predicts volatility in time series data based on past patterns. It's widely used in finance, weather forecasting, energy markets, and economic analysis where the variability of data changes over time.

**How GARCH Works**

GARCH models the variance (volatility) of a time series, which we can understand through temperature forecasting:
1. ARCH component: If yesterday's temperature deviated greatly from the average (a large error), today's temperature is likely to be more unpredictable too. The variance depends on past squared errors.
2. GARCH component: If temperature has been highly variable over the past week, it's likely to remain variable. The variance depends on past variances.

**Understanding the Model Specification**

To model temperature variability using a GARCH process, we define:
- $\varepsilon_t$ as the error in our temperature prediction (actual - predicted)
- $\sigma_t$ as the time-dependent standard deviation (volatility) of temperature
- $z_t$ as a random noise component

The relationship is: 

$$
\varepsilon_t = \sigma_t z_t
$$

For a GARCH(p,q) model, the variance equation is:

$$
\sigma_t^2 = \omega + \sum_{i=1}^{q} \alpha_i \varepsilon_{t-i}^2 + \sum_{i=1}^{p} \beta_i \sigma_{t-i}^2
$$

Where:
- $\omega > 0$ is a constant term
- $\alpha_i \geq 0$ are parameters for past squared errors
- $\beta_i \geq 0$ are parameters for past variances
- $p$ is the number of past variance terms used
- $q$ is the number of past squared error terms used

**Estimating the Initial Variance**

To start a GARCH model, we need an initial variance value ($\sigma_1^2$ or whichever period we begin modeling). Common approaches include:

1. Using the unconditional variance of the series, calculated as:
   
   $$
   \sigma_{unconditional}^2 = \frac{\omega}{1 - \sum_{i=1}^{q}\alpha_i - \sum_{i=1}^{p}\beta_i}
   $$

2. Using the sample variance from a training period (e.g., the variance of errors from a preliminary model)

3. Using a simple moving average of available squared errors:
   
   $$
   \sigma_{initial}^2 = \frac{1}{n}\sum_{i=1}^{n}\varepsilon_i^2
   $$

4. Setting it to a reasonable value based on domain knowledge about the expected variability

For our temperature example, we'll use method 4 and start with $\sigma_3^2 = 4$ (standard deviation of 2°F) based on typical daily temperature variability.

**Worked Example: GARCH(1,1)**

Let's apply a GARCH(1,1) model to daily temperature forecasting using the same temperature series and predicted values from our ARIMA example: 

$$
\sigma_t^2 = \omega + \alpha_1 \varepsilon_{t-1}^2 + \beta_1 \sigma_{t-1}^2
$$

Where:
- $\omega = 0.2$ (baseline temperature variability)
- $\alpha_1 = 0.3$ (impact of yesterday's prediction error)
- $\beta_1 = 0.6$ (persistence of previous day's volatility)

Step 1: Start with initial values from the ([ARIMA example](arima.md#arima)) , we have:
- Actual temperatures: $X = [75, 77, 76, 78, 77, 79, 78, 80]$
- Predicted temperatures from ARIMA model: $X^{expected} = [-, -, 77.2, 75.3, 79.8, 76.3, 80.4, 77.3]$
- Initial variance estimate $\sigma_3^2 = 4$ (a standard deviation of $2°F$)

Step 2: Calculate the error terms using the ARIMA predictions
- Day 3: Actual = $76°F$, Predicted = $77.2°F$, $\varepsilon_3 = 76 - 77.2 = -1.2°F$
- Day 4: Actual = $78°F$, Predicted = $75.34°F$, $\varepsilon_4 = 78 - 75.34 = 2.66°F$
- Day 5: Actual = $77°F$, Predicted = $79.76°F$, $\varepsilon_5 = 77 - 79.76 = -2.76°F$
- Day 6: Actual = $79°F$, Predicted = $76.28°F$, $\varepsilon_6 = 79 - 76.28 = 2.72°F$
- Day 7: Actual = $78°F$, Predicted = $80.39°F$, $\varepsilon_7 = 78 - 80.39 = -2.39°F$
- Day 8: Actual = $80°F$, Predicted = $77.31°F$, $\varepsilon_8 = 80 - 77.31 = 2.69°F$

Step 3: Calculate the conditional variance for Day 4 

$$
\sigma_4^2 = \omega + \alpha_1\varepsilon_3^2 + \beta_1\sigma_3^2
$$

$$
\sigma_4^2 = 0.2 + 0.3 \times (-1.2)^2 + 0.6 \times 4
$$

$$
\sigma_4^2 = 0.2 + 0.3 \times 1.44 + 0.6 \times 4
$$

$$
\sigma_4^2 = 0.2 + 0.432 + 2.4
$$

$$
\sigma_4^2 = 3.032
$$

This means we expect a standard deviation of $\sqrt{3.032} = 1.74°F$ in our Day 4 temperature prediction.

Step 4: Calculate the conditional variance for Day 5 

$$
\sigma_5^2 = \omega + \alpha_1\varepsilon_4^2 + \beta_1\sigma_4^2
$$

$$
\sigma_5^2 = 0.2 + 0.3 \times (2.66)^2 + 0.6 \times 3.032
$$

$$
\sigma_5^2 = 0.2 + 0.3 \times 7.08 + 0.6 \times 3.032
$$

$$
\sigma_5^2 = 0.2 + 2.124 + 1.819
$$

$$
\sigma_5^2 = 4.143
$$

Step 5: Calculate the conditional variance for Day 6 

$$
\sigma_6^2 = \omega + \alpha_1\varepsilon_5^2 + \beta_1\sigma_5^2
$$

$$
\sigma_6^2 = 0.2 + 0.3 \times (-2.76)^2 + 0.6 \times 4.143
$$

$$
\sigma_6^2 = 0.2 + 0.3 \times 7.62 + 0.6 \times 4.143
$$

$$
\sigma_6^2 = 0.2 + 2.286 + 2.486
$$

$$
\sigma_6^2 = 4.972
$$

Step 6: Continue calculating for Days 7 and 8 

$$
\sigma_7^2 = 0.2 + 0.3 \times (2.72)^2 + 0.6 \times 4.972
$$

$$
\sigma_7^2 = 0.2 + 0.3 \times 7.40 + 0.6 \times 4.972
$$

$$
\sigma_7^2 = 0.2 + 2.22 + 2.983
$$

$$
\sigma_7^2 = 5.403
$$

$$
\sigma_8^2 = 0.2 + 0.3 \times (-2.39)^2 + 0.6 \times 5.403
$$

$$
\sigma_8^2 = 0.2 + 0.3 \times 5.71 + 0.6 \times 5.403
$$

$$
\sigma_8^2 = 0.2 + 1.713 + 3.242
$$

$$
\sigma_8^2 = 5.155
$$

**Temperature Volatility Prediction Table**

| Day | Actual Temp | Previous Temp | Diff | Expected Temp | Error | Previous Errors | Squared Error | Predicted Variance | Volatility | 95% Confidence Interval |
|-----|-------------|--------------|------|--------------|-------|----------------|--------------|-------------------|------------|--------------------------|
| 1   | 75°F        | -            | -    | -            | -     | -              | -            | -                 | -          | -                        |
| 2   | 77°F        | 75°F         | +2   | -            | -     | -              | -            | -                 | -          | -                        |
| 3   | 76°F        | 77°F         | -1   | 77.2°F       | -1.2  | -              | 1.44         | 4.000 (initial)   | 2.000°F    | [73.2°F, 81.2°F]         |
| 4   | 78°F        | 76°F         | +2   | 75.34°F      | 2.66  | -1.2           | 7.08         | 3.032             | 1.741°F    | [71.9°F, 78.8°F]         |
| 5   | 77°F        | 78°F         | -1   | 79.76°F      | -2.76 | 2.66, -1.2     | 7.62         | 4.143             | 2.035°F    | [75.8°F, 83.7°F]         |
| 6   | 79°F        | 77°F         | +2   | 76.28°F      | 2.72  | -2.76, 2.66    | 7.40         | 4.972             | 2.230°F    | [71.9°F, 80.6°F]         |
| 7   | 78°F        | 79°F         | -1   | 80.39°F      | -2.39 | 2.72, -2.76    | 5.71         | 5.403             | 2.325°F    | [75.8°F, 85.0°F]         |
| 8   | 80°F        | 78°F         | +2   | 77.31°F      | 2.69  | -2.39, 2.72    | 7.24         | 5.155             | 2.270°F    | [72.9°F, 81.8°F]         |

**1-Day Ahead Forecast**

To create a forecast for the day ahead (Day 9), we need to:
1. Calculate the predicted variance (volatility) for Day 9 using the GARCH(1,1) model
2. Combine this with an ARIMA forecast for the temperature on Day 9

Step 1: Calculate Day 9's Predicted Variance Using the GARCH(1,1) equation: 

$$
\sigma_9^2 = \omega + \alpha_1 \varepsilon_{8}^2 + \beta_1 \sigma_{8}^2
$$

$$
\sigma_9^2 = 0.2 + 0.3 \times (2.69)^2 + 0.6 \times 5.155
$$

$$
\sigma_9^2 = 0.2 + 0.3 \times 7.24 + 0.6 \times 5.155
$$

$$
\sigma_9^2 = 0.2 + 2.172 + 3.093
$$

$$
\sigma_9^2 = 5.465
$$

This gives us a volatility (standard deviation) of: $\sigma_9 = \sqrt{5.465} = 2.338°F$

Step 2: Use the ARIMA 1-day ahead forecast from our previous example

From our ARIMA(2,1,3) model, we predicted a temperature of $81.8°F$ for Day 9.

Step 3: Provide a Complete Forecast with Confidence Interval 

The complete forecast for Day 9 would be:
- Expected temperature: $81.8°F$
- Volatility (standard deviation): $2.338°F$
- 95% confidence interval: $81.8°F \pm 1.96 \times 2.338°F = 81.8°F \pm 4.58°F = [77.22°F, 86.38°F]$

This means we can be 95% confident that the actual temperature on Day 9 will fall between approximately $77°F$ and $86°F$.

**Practical Interpretation**

1. Weather Forecasting Application:
   - Days with higher $\sigma_t$ values indicate times when temperature is harder to predict
   - Weather forecasters could communicate larger confidence intervals to the public
   - $\sigma_t = 2.0°F$ might be reported as "High today of $76°F$, plus or minus $4°F$"
   - $\sigma_t = 2.3°F$ might be reported as "High today of $78°F$, plus or minus $4.6°F$"

2. Pattern Recognition:
   - The model captures how prediction uncertainty evolves over time
   - Errors tend to cluster (volatile periods tend to be followed by more volatile periods)
   - Once volatility increases, it takes time to decrease (persistence effect)

**Testing for GARCH Effects in Temperature Data**

To determine if temperature data exhibits GARCH effects, we would:
1. Create a temperature prediction model (like ARIMA)
2. Collect the errors ($\varepsilon_t$) from this model
3. Square the errors ($\varepsilon_t^2$)
4. Test if these squared errors are autocorrelated (related to their own past values)

If significant autocorrelation exists in the squared errors, GARCH modeling would be appropriate.

**Limitations**

GARCH models for temperature forecasting have several limitations:
1. They assume symmetry in how positive and negative temperature shocks affect future volatility
2. They work best for high-frequency data (daily temperatures rather than monthly averages)
3. They may not adequately capture seasonal patterns in temperature volatility
4. Extreme weather events (outliers) can disproportionately impact the model
5. They require sufficient historical data to estimate parameters accurately
6. The assumption that volatility is completely predetermined by past values is a simplification

Despite these limitations, GARCH models provide valuable information about the changing uncertainty in temperature predictions, helping meteorologists communicate more accurate confidence intervals.