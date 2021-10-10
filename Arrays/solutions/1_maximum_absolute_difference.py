class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        x_max = y_max = -10^9
        x_min = y_min = 10^9
        for i, val in enumerate(A):
            x = val + i
            if x > x_max:
                x_max = x
            if x < x_min:
                x_min = x
            y = val - i
            if y > y_max:
                y_max = y
            if y < y_min:
                y_min = y
        return max(x_max-x_min, y_max-y_min)


# Test Code
assert Solution().maxArr([1, 3, -1]) == 5
assert Solution().maxArr([2]) == 0
