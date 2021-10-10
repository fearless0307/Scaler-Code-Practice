class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, A, B):
        if B == 0:
            return A
        return self.gcd(B, A%B)

    def solve(self, A):
        n = len(A)
        max_gcd = 0
        pre_gcd = 0
        post_gcd = 0
        prefix_gcd_list = [0]
        postfix_gcd_list = [0]
        for i in range(n-1):
            pre_gcd = self.gcd(pre_gcd, A[i])
            prefix_gcd_list.append(pre_gcd)
        for i in range(n-1, 0, -1):
            post_gcd = self.gcd(post_gcd, A[i])
            postfix_gcd_list.insert(0, post_gcd)
        for i in range(n):
            max_gcd = max(max_gcd, self.gcd(prefix_gcd_list[i], postfix_gcd_list[i]))
        return max_gcd


# Test code
assert Solution().solve([12, 15, 18]) == 6
assert Solution().solve([5, 15, 30]) == 15
