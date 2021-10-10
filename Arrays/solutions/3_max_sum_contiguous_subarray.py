class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = A[0]
        max_ending_here = 0

        for i in range(0, len(A)):
            max_ending_here = max_ending_here + A[i]
            max_so_far = max(max_so_far, max_ending_here)
            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far


# Test code
assert Solution().maxSubArray([1, 2, 3, 4, -10]) == 10
assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
