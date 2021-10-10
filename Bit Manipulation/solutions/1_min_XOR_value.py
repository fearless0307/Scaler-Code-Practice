class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        min_xor = 10**9
        A.sort()
        n = len(A)
        for i in range(0, n-1):
            min_xor = min(min_xor, A[i]^A[i+1])
        return min_xor


# Test code
assert Solution().findMinXor([0, 2, 5, 7]) == 2
assert Solution().findMinXor([0, 4, 7, 9]) == 3
