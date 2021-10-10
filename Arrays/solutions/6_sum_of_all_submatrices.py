class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        n = len(A)
        m = len(A[0])
        for i in range(n):
            for j in range(m):
                ans += A[i][j]*(i+1)*(n-i)*(j+1)*(m-j)
        return ans


# Test code
assert Solution().solve([ [1, 1], [1, 1] ]) == 16
