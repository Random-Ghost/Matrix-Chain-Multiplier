# Code Explanation
We have a sequence of numbers $` x = (x_0, x_1, \ldots, x_{n - 1}) `$. The goal is to place parentheses around $` x_0 / x_1 / x_2 / \ldots / x_{n - 1} `$ such that we either maximize or minimize the output.

We know to maximize the output of a fraction, we can maximize the numerator and minimize the denominator. The opposite is true if we want to minimize the fraction. Assuming we split the vector at the k-th index,
```math
max\_quotient(i, j) =
\begin{cases}
  x_i & i = j \\
  \frac{max\_quotient(i, k)}{min\_quotient(k + 1, j)} & otherwise
\end{cases}
```
and
```math
min\_quotient(i, j) =
\begin{cases}
  x_i & i = j \\
  \frac{min\_quotient(i, k)}{max\_quotient(k + 1, j)} & otherwise
\end{cases}
```
where max_quotient(i, j) is the highest possible value for $` x_i / \ldots / x_j `$ and min_quotient(i, j) is the lowest possible value. We will compare across all splits. If we split at index k, we get $` (x_i / \ldots / x_k) / (x_{k + 1} / \ldots / x_j) `$ so k can only be in the range of 0 to j - 1. Now we have the algorithm and base cases.
