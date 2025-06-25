class MemoizedMCM:
    def __init__(self, dim_arr):
        self.dim_arr = dim_arr
        self.n = len(dim_arr)
        self.memo = [[None] * self.n for i in range(self.n)]  # memo array
        for i in range(0, self.n - 1):
            self.memo[i][i + 1] = 0  # base cases
        self.value = self.rec_matrix_chain_multiplier(0, self.n - 1)

    def rec_matrix_chain_multiplier(self, i, j):
        if self.memo[i][j] is None:  # not computed
            self.memo[i][j] = float('inf')

            for k in range(i + 1, j):  # the cuts can only be from i + 1 to j - 1
                curr = (self.rec_matrix_chain_multiplier(i, k)
                        + self.rec_matrix_chain_multiplier(k, j)
                        + self.dim_arr[i] * self.dim_arr[k] * self.dim_arr[j])
                self.memo[i][j] = min(self.memo[i][j], curr)  # find the minimum at that level

        return self.memo[i][j]


def memoized_mcm(dim_arr):
    p = MemoizedMCM(dim_arr)
    return p.value
