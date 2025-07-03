# Code Explanation
We have a sequence of matrices $` (m_0, m_1, \ldots, m_{n-1}) `$ that have to be multiplied. There are many ways that can be done but we have to have the optimal way that uses the least number of operations.

Since we are multiplying the matrices, the number of rows of a matrix must be the same as the number of columns of the previous matrix. So we can write the dimensions array as $` (a_0, a_1, \ldots, a_n) `$ where matrix $` m_i `$ has dimensions $` (a_k, a_{k + 1}) `$.

To multiply two matrices with dimensions $` (l, m) `$ and $` (m, n) `$, each of the elements require a dot product of a row of the first matrix and a column of the second. To get the dot product, we perform $` m `$ multiplications. And since the product matrix has dimensions $` (l, n) `$, we perform $` l * m * n `$ operations. We only count multiplication operations here.

To get the optimal ordering, we compare across splits. If we want to get the best ordering on $` (m_i, \ldots, m_{j-1}) `$, we split at $` m_k `$. So we get two matrix sequences, $` (m_i, \ldots, m_k) `$ and $` (m_{k+1}, \ldots, m_{j-1}) `$. They will have dimensions $` (a_i, a_{k+1}) `$ and $` (a_{k+1}, a_j) `$. So the work cost for the split is $` a_i * a_{k+1} * a_j `$. We compare across splits recursively till we get the final optimal ordering.

We can write this as
```math
mcm(a, i, j) =
\begin{cases}
  0 & j = i + 1 \\
  \min(mcm(a, i, k) + mcm(a, k, j) + a_i * a_k * a_j) & \text{otherwise}
\end{cases}
```
It is 0 in the case where $` j = i + 1 `$ because we only get one matrix and no multiplication.
