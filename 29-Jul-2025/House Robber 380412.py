# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int], i=0, memo=None) -> int:
        memo = {}
        n = len(nums)

        def dp(i):
            if i >= n:
                return 0

            if i not in memo:
                memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))

            return memo[i]

        return dp(0)