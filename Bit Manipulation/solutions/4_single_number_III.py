class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        val = 0
        for i in A:
            val = val ^ i
        bit_set = 0
        while True:
            if val & (1 << bit_set):
                break
            bit_set += 1
        val_bit_set = 0
        val_bit_unset = 0
        for i in A:
            if i & (1 << bit_set):
                val_bit_set = val_bit_set ^ i
            else:
                val_bit_unset = val_bit_unset ^ i
        if val_bit_set > val_bit_unset:
            return [val_bit_unset, val_bit_set]
        return [val_bit_set, val_bit_unset]

    def solve2(self, A):  # Scaler Solution
        val = 0
        for i in A:
            val = val ^ i
        mask = (val & (val - 1)) ^ val
        val_bit_set = 0
        val_bit_unset = 0
        for i in A:
            if i & mask:
                val_bit_set = val_bit_set ^ i
            else:
                val_bit_unset = val_bit_unset ^ i
        if val_bit_set > val_bit_unset:
            return [val_bit_unset, val_bit_set]
        return [val_bit_set, val_bit_unset]


# Test code
assert Solution().solve([1, 2, 3, 1, 2, 4]) == [3, 4]
assert Solution().solve([1, 2]) == [1, 2]

assert Solution().solve2([1, 2, 3, 1, 2, 4]) == [3, 4]
assert Solution().solve2([1, 2]) == [1, 2]
