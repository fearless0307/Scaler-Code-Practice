class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, A, B):
        if B == 0:
            return A
        return self.gcd(B, A%B)

    def solve(self, A):
        gcd = 0
        for i in A:
            gcd = self.gcd(gcd, i)
        return gcd


# Test code
assert Solution().solve([6, 4]) == 2
assert Solution().solve([2, 3, 4]) == 1
