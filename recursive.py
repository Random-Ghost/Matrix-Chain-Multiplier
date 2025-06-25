def matrix_chain_multiplier_helper(dim_arr, i, j):
    if i + 1 == j:
        return 0  # base case with only one matrix, no multiplication

    res = float('inf')

    for k in range(i + 1, j):  # the cuts can only be from i + 1 to j - 1
        curr = (matrix_chain_multiplier_helper(dim_arr, i, k)
                + matrix_chain_multiplier_helper(dim_arr, k, j)
                + dim_arr[i] * dim_arr[k] * dim_arr[j])
        res = min(res, curr)  # find the minimum at that level

    return res


def matrix_chain_multiplier(dim_arr):
    n = len(dim_arr)
    return matrix_chain_multiplier_helper(dim_arr, 0, n - 1)


print(matrix_chain_multiplier([1, 2, 3, 4, 3]))
