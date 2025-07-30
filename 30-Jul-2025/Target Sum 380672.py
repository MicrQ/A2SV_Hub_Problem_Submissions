# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dp(i, total):
            """ recursively checking with dp involvement """
            if i == n:
                return 1 if total == target else 0

            if (i, total) not in memo:
                memo[(i, total)] = dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])

            return memo[(i, total)]

        return dp(0, 0)