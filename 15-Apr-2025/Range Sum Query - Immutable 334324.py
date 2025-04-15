# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = nums
        for i in range(1, len(nums)):
            self.prefix[i] += self.prefix[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        
        left_sum = 0 if left == 0 else self.prefix[left - 1]

        return self.prefix[right] - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)