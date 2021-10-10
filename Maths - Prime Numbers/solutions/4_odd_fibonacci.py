class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def solve(self, A, B):
        A = A-1
        return ((B//3) * 2 + B%3) - ((A//3) * 2 + A%3)


# Test code
assert Solution().solve(2, 6) == 3
assert Solution().solve(6, 20) == 10
