# Unstructured Sparsity

The following experiment tries to show that using the Iterative Hard Thresholding (IHT) algorithm does not lead to a trained neural network that has structured sparsity. Structured sparsity means that we have columns or rows that are completely zero.

To illustrate this, we use the Iris dataset, which contains 150 data points representing three different flower species. Each sample includes four numerical features: sepal length, sepal width, petal length, and petal width, as shown in the picture.

<figure style="text-align: center;">
  <img src="/phd/_static/images/iris/iris_dataset.svg" alt="Iris dataset visualization" width="60%">
  <figcaption>The three Iris species. Measurements are shown only for Iris Versicolor.</figcaption>
</figure>

We exclude one sample from the dataset, which is:

$$
\mathbf{x} = [6.4, 3.2, 4.5, 1.5]^T
$$

This sample is belong to versicolor flowers, i.e., 

$$
\text{The original sample class} = \text{2 (versicolor)}.
$$

Thus, we have 149 samples in total. If we split the data into 80% training and 20% testing (inference), we get approximately (120, 30).
We consider a one-layer neural network architecture, as shown below. This network has four inputs and three outputs. Therefore, we train a single-layer network using almost 120 data points.

<figure style="text-align: center;">
  <img src="/phd/_static/images/iris/single_layer_nn.svg" alt="Single-layer neural netowrk." width="30%">
  <figcaption>A single-layer neural network with 4 inputs and 3 outputs.</figcaption>
</figure>


We initialize the network by setting the sparsity level to 5, i.e., $s=5$. The initial weights are the following:



$$
\mathbf{W}_{\text{init}} =
\begin{bmatrix}
-0.99 & 0 & 0 & 0.41 \\
-0.73 & -0.06 & 0 & 0 \\
0 & 0.62 & 0 & 0 \\
\end{bmatrix}, \quad
\mathbf{b}_{\text{init}} = 
\begin{bmatrix}
0 \\ 0 \\ 0
\end{bmatrix}.
$$



After training, the trained weights are as follows:

$$
\mathbf{W}_{\text{final}} =
\begin{bmatrix}
-1.44 & 0 & -4.74 & 0 \\
0 & -0.5 & 0 & 0 \\
0 & 0 & 0 & 5.45 \\
\end{bmatrix}, \quad
\mathbf{b}_{\text{final}} =
\begin{bmatrix}
0 \\ 3.14 \\ 0
\end{bmatrix}.
$$

The network accuracy is 93.33% and it correctly classifies the sample that we kept at the beginning.

$$
\text{Mean vector: } \boldsymbol{\mu} = [5.79, 3.08, 3.62, 1.13]^T
$$

$$
\text{Standard deviation vector: } \boldsymbol{\sigma} = [0.86, 0.45, 1.84, 0.79]^T
$$

$$
\text{Normalized vector: } \mathbf{x_{norm}} = [0.71, 0.27, 0.48, 0.47]^T
$$

$$
\mathbf{z} = \mathbf{W}\mathbf{x_{norm}} + \mathbf{b}
$$

$$
\mathbf{z} =
\begin{bmatrix} 
-1.44 & 0 & -4.74 & 0 \\ 
0 & -0.5 & 0 & 0 \\ 
0 & 0 & 0 & 5.45 \\
\end{bmatrix} 
\begin{bmatrix} 0.71 \\ 0.27 \\ 0.48 \\ 0.47 \end{bmatrix} + \begin{bmatrix} 0 \\ 3.14 \\ 0 \end{bmatrix}
$$

$$
\mathbf{z} =
\begin{bmatrix} -3.27 & \\ 3.01 & \leftarrow \max \\ 2.55 & \end{bmatrix}
$$

The predicted class is 2 which matches the true class!

As you can see, neither a row nor a column is completely zero in the trained network, clearly verifying there is no pattern in the sparsity of the trained network.

This is much more clear if we look at the weights and biases on the trained network. As the picture shows, there is at least a connection between an input and output neuron.

<figure style="text-align: center;">
  <img src="/phd/_static/images/iris/unstructured.svg" alt="Unstructured Sparsity as a result of the ITH algorithm" width="30%">
  <figcaption>The unstructured sparsity pattern after training the network using IHT algorithm.</figcaption>
</figure>

On the other hand, if you look at the following trained network, it has 96.67% accuracy on the test set with two columns that are completely zero. 

$$
\mathbf{W}_{\text{final}} =
\begin{bmatrix}
0 & 0 & -4.88 & -3.62 \\
0 & 0 & 0 & 0 \\
0 & 0 & 3.41 & 4.91 \\
\end{bmatrix}, \quad
\mathbf{b}_{\text{final}} =
\begin{bmatrix}
0 \\ 5.34 \\ 0
\end{bmatrix}.
$$

The network achieves a test accuracy of 96.67% and correctly classifies our sample.

$$
\text{Mean vector: } \boldsymbol{\mu} = [5.78, 3.04, 3.7, 1.18]^T
$$

$$
\text{Standard deviation vector: } \boldsymbol{\sigma} = [0.81, 0.42, 1.77, 0.78]^T
$$

$$
\text{Normalized sample: } \mathbf{x_{norm}} = [0.77, 0.38, 0.46, 0.41]^T
$$

$$
\mathbf{z} = \mathbf{W}\mathbf{x_{norm}} + \mathbf{b}
$$

$$
\mathbf{z} =
\begin{bmatrix} 
0 & 0 & -4.88 & -3.62 \\ 
0 & 0 & 0 & 0 \\ 
0 & 0 & 3.41 & 4.91 \\
\end{bmatrix} 
\begin{bmatrix} 0.77 \\ 0.38 \\ 0.46 \\ 0.41 \end{bmatrix} + \begin{bmatrix} 0 \\ 5.34 \\ 0 \end{bmatrix}
$$

$$
\mathbf{z} =
\begin{bmatrix} -3.72 & \\ 5.34 & \leftarrow \max \\ 3.59 & \end{bmatrix}
$$

The predicted class is 2, which matches the true class!


These zero columns result in no connection to two input neurons as you can see this clealry in the picture.

<figure style="text-align: center;">
  <img src="/phd/_static/images/iris/structured.svg" alt="Structured Sparsity as a result of the ITH algorithm" width="30%">
  <figcaption>The structuredd sparsity pattern in a trained network that performs as well as the dense one.</figcaption>
</figure>


This demonstrates that IHT may result in an unstructured sparsity patterns when some structured sparsity patterns exist.