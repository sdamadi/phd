# Rolling Standardization

Data normalization is critical for optimization and convergence in machine learning models. As [Marquardt](https://www.jstor.org/stable/2098941?seq=1) showed in 1963, feature standardization plays a key role in the convergence of gradient-based optimization methods, particularly in nonlinear models. It prevents numerical instabilities and ensures that different features contribute proportionally to the learning process.

However, when applying feature normalization to time series data, careful consideration is required. Naive normalization can inadvertently destroy temporal dependencies between samples by mixing information from future and past observations. A rolling window normalization approach preserves the temporal structure while maintaining the benefits of feature scaling.

**Time Series to Data Matrix**

Given the closing prices of an asset, we can create a rolling window that slides by one step; the data in each sample window is then normalized independently using its own mean and standard deviation. Mathematically, for each window containing close prices $x_j$, the normalization is computed as:

$$z^c_j = \frac{x^c_j - \mu^c_i}{\sigma^c_i}$$

where $\mu^c_i$ and $\sigma^c_i$ are the mean and standard deviation of the $i$-th sample, respectively.

The figure below shows window-wise normalization or rolling standardization. This process converts the close time series matrix $\mathbf{X}^c$ into a new matrix $\mathbf{Z}^c$ with the same structure.

<figure style="text-align: center;">
  <img src="/phd/_static/images/ts/standardization.svg" alt="Rolling Standardization for the closing price" width="80%">
  <figcaption>Rolling Standardization for the closing price.</figcaption>
</figure>

<figure style="text-align: center;">
  <img src="/phd/_static/images/one_layer/single_layer_arch_wx.svg" alt="A one-layer neural network architecture" width="40%">
  <figcaption>A one-layer neural network architecture.</figcaption>
</figure>


**Rationale for Rolling Normalization**

Window-wise normalization has a theoretically appealing property: when each time window is normalized by its local statistics, the resulting row values approximately follow a normal distribution. This occurs because normalizing by the mean and standard deviation of each window aligns the data with a normal distribution.