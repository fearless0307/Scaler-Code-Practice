class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return abs(A - B)


# Test code
assert Solution().solve(1, 2) == 1
assert Solution().solve(5, 10) == 5
