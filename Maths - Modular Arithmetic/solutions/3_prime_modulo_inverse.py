class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def mod_of_power(self, a, b, m):
        if b == 0:
            return 1
        res = self.mod_of_power(a, b // 2, m) % m
        res = (res * res) % m
        if (b % 2 == 0):
            return res
        return (a * res) % m

    def solve(self, A, B):
        return self.mod_of_power(A, B-2, B)


# Test code
assert Solution().solve(3, 5) == 2
assert Solution().solve(6, 23) == 4
