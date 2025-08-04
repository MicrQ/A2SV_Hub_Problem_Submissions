# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        memo = {}

        def dp(idx):
            if idx >= n - 1: # it reached or passed the target
                return 0

            if idx not in memo:
                min_jump = float('inf')
                for i in range(nums[idx]): # for every possible jump
                    jump = i + 1
                    min_jump = min(min_jump, 1 + dp(idx + jump))

                memo[idx] = min_jump

            return memo[idx]

        return dp(0)