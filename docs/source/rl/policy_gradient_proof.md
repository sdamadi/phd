(policy-gradien)= 
# Policy Gradient

In reinforcement learning, the reward function forms the foundation of how an agent learns to make decisions. The expected cumulative reward, denoted as $J(\theta)$, represents the objective that we aim to maximize:

$J(\theta) = \mathbb{E}_{\tau\sim p_{\theta}(\tau)}[R(\tau)]$

where $\tau$ represents a trajectory (sequence of states and actions), $\pi_\theta$ is our policy parameterized by $\theta$, and $R(\tau)$ is the reward associated with trajectory $\tau$.

We can define $L(\theta) = -J(\theta)$ and minimize this loss function instead. Minimizing the loss requires calculating the gradient of the loss function, which depends on the gradient of the policy function. The policy function is a scalar function that assigns a probability to an action, hence the name "policy gradient."

The derivation of the policy gradient is as follows:

$$ \begin{aligned}
J(\theta) &= \mathbb{E}_{\tau \sim p_{\theta}} \left[ R(\tau) \right] \\
&= \sum_\tau P_{\theta}(\tau) R(\tau)
\end{aligned} $$

Taking the gradient with respect to the parameters $\theta$:

$$ \begin{aligned} 
\nabla_\theta J(\theta) &= \sum_\tau R(\tau) \nabla_\theta P_{\theta}(\tau) \\ 
& \stackrel{1}{=} \sum_\tau R(\tau) P_{\theta}(\tau) \nabla_\theta \log P_{\theta}(\tau) \\ 
& \stackrel{2}{=} \sum_\tau R(\tau) P_{\theta}(\tau) \nabla_\theta \log \left(p(s_0)\prod_{t=1}^T \pi_\theta(a_{t-1}|s_{t-1}) p(s_{t}|s_{t-1},a_{t-1}) \right) \\ 
&= \sum_\tau R(\tau) P_{\theta}(\tau) \nabla_\theta \left(\sum_{t=1}^T \log \pi_\theta(a_{t-1}|s_{t-1}) + \sum_{t=1}^T \log p(s_{t}|s_{t-1},a_{t-1}) + \log p(s_0) \right) \\ 
& \stackrel{3}{=} \sum_\tau R(\tau) P_{\theta}(\tau) \nabla_\theta \left(\sum_{t=1}^T \log \pi_\theta(a_{t-1}|s_{t-1})\right) \\ 
&= \sum_\tau R(\tau) P_{\theta}(\tau) \left(\sum_{t=1}^T \nabla_\theta \log \pi_\theta(a_{t-1}|s_{t-1})\right) \\ 
& \stackrel{4}{=} \mathbb{E}_{\tau \sim p_{\theta}} \left[R(\tau) \sum_{t=1}^T \nabla_\theta \log \pi_\theta(a_{t-1}|s_{t-1})\right]
\end{aligned} $$

Where:
- In step 1, we apply the identity $\nabla_\theta \log f(\theta) = \frac{\nabla_\theta f(\theta)}{f(\theta)}$  
([$\log$-derivative formula](log_derivative_trick.md#log-derivative)),
 which gives us $\nabla_\theta P_{\theta}(\tau) = P_{\theta}(\tau) \nabla_\theta \log P_{\theta}(\tau)$.
- In step 2, we use the trajectory probability formula derived [here](trajectory_probability.md#trajectory-probability).
- In step 3, we observe that the terms involving $p(s_t|s_{t-1},a_{t-1})$ and $p(s_0)$ do not depend on $\theta$, so their gradients with respect to $\theta$ are zero
- In step 4, we convert the summation back to expectation notation using the definition of expectation: $\mathbb{E}_{\tau \sim p_\theta}[f(\tau)] = \sum_\tau P_{\theta}(\tau)f(\tau)$

This final expression is the policy gradient theorem, which provides a way to estimate the gradient of the expected return with respect to policy parameters.