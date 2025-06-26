class MemoizedMCM:
    def __init__(self, dim_arr):
        self.dim_arr = dim_arr
        self.n = len(dim_arr)
        self.memo = [[None for j in range(self.n)] for i in range(self.n)]  # memo array
        self.order = [[None for j in range(self.n)] for i in range(self.n)] # order array
        for i in range(0, self.n - 1):
            self.memo[i][i + 1] = 0  # base cases
            # these will be the starting matrices
            self.order[i][i + 1] = "(" + str(self.dim_arr[i]) + " x " + str(self.dim_arr[i + 1]) + ")"
        self.value = self.rec_matrix_chain_multiplier(0, self.n - 1)
        self.sequence = self.order[0][self.n - 1]

    def rec_matrix_chain_multiplier(self, i, j):
        if self.memo[i][j] is None:  # not computed
            temp = float('inf')
            cut = i + 1

            for k in range(i + 1, j):  # the cuts can only be from i + 1 to j - 1
                curr = (self.rec_matrix_chain_multiplier(i, k)
                        + self.rec_matrix_chain_multiplier(k, j)
                        + self.dim_arr[i] * self.dim_arr[k] * self.dim_arr[j])
                # self.memo[i][j] = min(self.memo[i][j], curr)  # find the minimum at that level

                # cut is the optimal cut point for the multiplication, we need to show the before and after.
                # python's min function only gets the first smallest value so this can change only if curr is less than
                # what we already have. I think it will be faster to replace both at the same time in the case where
                # we get a lower value
                if curr < temp:
                    temp = curr
                    cut = k

            # now we should have the optimal number of operations and the cut point
            self.memo[i][j] = temp

            # self.order[i][j] = "(" + str(self.order[i][cut]) + ") x (" + str(self.order[cut][j]) + ")"
            # normally, that set-up would work but there would be too many brackets
            if j == i + 2:  # I have to put this first so it does not affect the next two cases
                self.order[i][j] = str(self.order[i][cut]) + " x " + str(self.order[cut][j])
            elif cut == i + 1:
                self.order[i][j] = str(self.order[i][cut]) + " x (" + str(self.order[cut][j]) + ")"
            elif j == cut + 1:
                self.order[i][j] = "(" + str(self.order[i][cut]) + ") x " + str(self.order[cut][j])
            else:
                self.order[i][j] = "(" + str(self.order[i][cut]) + ") x (" + str(self.order[cut][j]) + ")"

        return self.memo[i][j]


def memoized_mcm(dim_arr):
    p = MemoizedMCM(dim_arr)
    return p.sequence
