# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mono_stack = []
        left_min = nums[0]

        for i in range(1, len(nums)):
            while mono_stack and mono_stack[-1][0] <= nums[i]:
                mono_stack.pop()

            if mono_stack and mono_stack[-1][1] < nums[i]:
                return True

            mono_stack.append((nums[i], left_min))
            left_min = min(left_min, nums[i])

        return False