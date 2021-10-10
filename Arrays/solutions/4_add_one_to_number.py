class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A[-1] += 1
        temp = 0
        tempSum = 0
        for i in range(len(A)-1,-1,-1):
            tempSum = A[i]+temp
            temp = (A[i]+temp)/10
            A[i] = tempSum%10
        if temp > 0:
            A = [temp] + A
        i = 0
        while i < len(A):
            if A[i] > 0:
                break
            i += 1
        return A[i:]


# Test code
assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
