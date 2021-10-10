class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if B == 0:
            return 1
        return self.gcd(B, A%B)


# Test code
assert Solution().gcd(4, 6) == 2
assert Solution().gcd(6, 7) == 1
