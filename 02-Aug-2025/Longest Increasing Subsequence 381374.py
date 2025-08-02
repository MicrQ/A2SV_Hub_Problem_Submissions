# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * n for _ in range(n)]

        def dp(i, prev):
            if i == n:
                return 0

            if memo[i][prev] == -1:
                include = 0
                if prev == -1 or nums[i] > nums[prev]:
                    include = 1 + dp(i + 1, i)

                exclude = dp(i + 1, prev)

                memo[i][prev] = max(include, exclude)

            return memo[i][prev]

        return dp(0, -1)