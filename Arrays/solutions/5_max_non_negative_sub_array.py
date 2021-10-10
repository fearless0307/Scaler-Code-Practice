class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        temp_a = []
        temp_sum = 0
        final_a = []
        max_sum = 0
        n = len(A)
        for i in range(n):
            if A[i] >= 0:
                temp_a.append(A[i])
                temp_sum += A[i]
            elif temp_sum >= 0:
                if temp_sum > max_sum:
                    final_a = [i for i in temp_a]
                    max_sum = temp_sum
                elif temp_sum == max_sum:
                    if len(temp_a) > len(final_a):
                        final_a = [i for i in temp_a]
                temp_a = list()
                temp_sum = 0
            if i == n-1:
                if temp_sum > max_sum:
                    final_a = list(temp_a)
                    max_sum = temp_sum
                elif temp_sum == max_sum:
                    if len(temp_a) > len(final_a):
                        final_a = list(temp_a)
                temp_a = list()
                temp_sum = 0
        return final_a


# Test code
assert Solution().maxset([1, 2, 5, -7, 2, 3]) == [1, 2, 5]
assert Solution().maxset([10, -1, 2, 3, -4, 100]) == [100]
