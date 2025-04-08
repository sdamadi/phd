(trajectory-probability)=
# Trajectory Probability

In Markov Decision Processes (MDPs), the trajectory represents the sequence of states and actions as the agent interacts with the environment over time. We start with an initial state $s_0$, then the agent takes an action $a_0$, which causes the environment to transition to a new state $s_1$, and this process continues, resulting in a trajectory $\tau = (s_0, a_0, s_1, a_1, ..., s_T)$. It is of interest to determine the probability of a specific trajectory $\tau$, which can be factorized using the Markov property and policy definitions.

We start with the full trajectory probability and apply the conditional probability formula:

$$
\begin{aligned}
P(\tau)
& =
p(s_{T}, a_{T-1},s_{T-1},\dots,a_{1},s_{1},a_{0},s_{0}) \\
& =
p(s_{T} \bigl \vert a_{T-1},s_{T-1},\dots,a_{0},s_{0}) 
p(a_{T-1},s_{T-1},\dots,a_{0},s_{0}) \\
&\stackrel{1}{=} 
p(s_{T} \bigl \vert a_{T-1},s_{T-1})
p(a_{T-1},s_{T-1},\dots,a_{0},s_{0}) \\
&=
p(s_{T} \bigl \vert a_{T-1},s_{T-1}) \;
p(a_{T-1} \bigl \vert s_{T-1},\dots,a_{0},s_{0}) 
p(s_{T-1},\dots,a_{0},s_{0}) \\
&\stackrel{2}{=} 
p(s_{T} \bigl \vert a_{T-1},s_{T-1}) \;
p(a_{T-1} \bigl \vert s_{T-1}) \;
p(s_{T-1},\dots,a_{0},s_{0}) \\
& \stackrel{3}{=} 
p(s_{T} \bigl \vert a_{T-1},s_{T-1})
\pi(a_{T-1} \bigl \vert s_{T-1}) \;
p(s_{T-1},\dots,a_{0},s_{0}) \\
& =
\prod_{t=1}^T \Bigl(
p(s_{t} \bigl \vert a_{t-1},s_{t-1})
\pi(a_{t-1} \bigl \vert s_{t-1})
\Bigr)
p(s_{0})\\
&=
p(s_{0})
\prod_{t=1}^T
p(s_{t} \bigl \vert a_{t-1},s_{t-1})
\pi(a_{t-1} \bigl \vert s_{t-1}).
\end{aligned}
$$

where in step 1 we used the Markov property of the environment (i.e., the next state depends only on the current state and action), in step 2 we assumed that the policy is memoryless (i.e., the probability of taking an action depends only on the current state), and in step 3 we replaced the action probability with the policy function $\pi(a_{T-1} \bigl \vert s_{T-1})$.

Now, when we parameterize the policy with $\theta$:

$P_\theta(\tau) = p(s_0)\prod_{t=1}^{T}p(s_t|a_{t-1},s_{t-1})\pi_\theta(a_{t-1}|s_{t-1})$

This makes explicit that:
1. Only the policy $\pi$ is parameterized by $\theta$ (becoming $\pi_\theta$)
2. The environment dynamics $p(s_t|a_{t-1},s_{t-1})$ are independent of $\theta$
3. The initial state distribution $p(s_0)$ is independent of $\theta$
4. The overall trajectory distribution $P_\theta(\tau)$ depends on $\theta$ only through the policy

This clarifies why we can write expectations as $\mathbb{E}_{\tau\sim p_\theta(\tau)}[\cdot]$ when computing [policy gradients](policy_gradient_proof.md#policy-gradient).


