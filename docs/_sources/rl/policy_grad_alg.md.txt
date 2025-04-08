# Policy Gradient Algorithm


Some people think reinforcement learning reduces the need for compute (GPUs), but it doesn’t.

If you look at the vanilla policy gradient algorithm, you’ll see that the gradient is expressed as an expectation. And for those who understand how expectations are computed, it becomes immediately clear that it’s intractable. If we were God and we *knew* the expectation exactly, then we’d already have the exact gradient.

But what does that mean? It means we’d have to consider all possible trajectories and compute their returns—a task that’s computationally impossible, it is the first algorithm.

So what do we do instead?

We approximate the gradient. But how?

Unlike supervised learning, where the training data is static and available, in reinforcement learning we must *generate* data—by interacting with the environment—to approximate the gradient.

For a fixed policy parameter, we roll out multiple trajectories and use them to estimate the expectation in practice. This data generation phase—sampling trajectories—requires significant computation, especially when environments are complex or policies are large neural networks. The second algorithm shows how.

That’s why GPUs are heavily used. And that’s also where the concept of mini-batches comes into play—to make this expensive sampling and gradient estimation tractable within our compute budget.


$$
\textbf{Algorithm: Policy Gradient (Accessing the Exact Gradient)}
$$

$\textbf{Input:}$ Initial policy parameters $\theta^0$, learning rate $\gamma > 0$.

$\text{For } k = 1, 2, \dots \text{do}$  

$\quad (\text{Compute the exact gradient})$  

$$
\nabla_\theta J(\theta^{k-1}) = \mathbb{E}_{\tau \sim p_{\theta^{k-1}}} \left[ R(\tau) \sum_{t=1}^{T} \nabla_\theta \log \pi_{\theta^{k-1}}(a_{t-1} \mid s_{t-1}) \right]
$$

$
\quad (\text{Update the parameters}) 
$

$$
\theta^k = \theta^{k-1} + \gamma \cdot \nabla_\theta J(\theta^{k-1})
$$ 

$\text{End For.}$

$$
\textbf{Algorithm: Policy Gradient (Approximating the Gradient)}
$$

$\textbf{Input:}$ Initial policy parameters $\theta^0$, learning rate $\gamma > 0$, mini-batch size $N$.

$\text{For } k = 1, 2, \dots \text{do}$ 

$\quad (\text{Collect trajectories})$  

$\quad \text{Collect a mini-batch of } N \text{ trajectories } \{\tau^{(i)}\}_{i=1}^N \text{ by executing policy } \pi_{\theta^{k-1}}$  

$\quad (\text{Approximate the gradient})$  

$$
\nabla_\theta \hat{J}(\theta^{k-1}) = \frac{1}{N} \sum_{i=1}^{N} \left[ R(\tau^{(i)}) \sum_{t=1}^{T} \nabla_\theta \log \pi_{\theta^{k-1}}(a_{t-1}^{(i)} \mid s_{t-1}^{(i)}) \right]
$$

$
\quad (\text{Update the parameters}) 
$

$$
\theta^k = \theta^{k-1} + \gamma \cdot \nabla_\theta \hat{J}(\theta^{k-1})
$$ 

$\text{End For.}$