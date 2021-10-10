class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        diff = 0
        max = 0
        start = 0
        r = []
        for i in range(len(A)):
            c = A[i]
            diff += 1 if c == '0' else -1
            if diff < 0:
                diff = 0
                start = i if c == '0' else i+1
            elif max < diff:
                max = diff
                r = [start+1, i+1]
        return r


# Test code
assert Solution().flip("010") == [1, 1]
assert Solution().flip("111") == []
