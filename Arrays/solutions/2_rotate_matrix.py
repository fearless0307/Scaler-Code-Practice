class Solution:
    # @param A : list of list of integers
    def solve(self, A):  # Swapping Cell Val - O(N^2) : O(1)
        n = len(A)
        for i in range(0, n//2):
            for j in range(i, n-i-1):
                A[i][j], A[j][n-i-1], A[n-i-1][n-j-1], A[n-j-1][i] = A[n-j-1][i], A[i][j], A[j][n-i-1], A[n-i-1][n-j-1]
        return A

    # Approach 1 - O(N^2) : O(1)
    def approach_1(self, A):
        n = len(A)
        B = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                B[j][n-i-1] = A[i][j]
        return B


# Test Code
assert Solution().solve([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
assert Solution().solve([[1]]) == [[1]]
