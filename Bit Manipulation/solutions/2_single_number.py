class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):  # TC O(n), SC O(1)
        val = 0
        for i in A:
            val = val ^ i
        return val


# Test Code
assert Solution().singleNumber([1, 2, 2, 3, 1]) == 3
assert Solution().singleNumber([1, 2, 2]) == 1
