# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        memo = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i][j - 1], memo[i - 1][j])

        return memo[n][m]


        # def dp(i, j):
        #     if i >= n or j >= m:
        #         return 0

        #     if memo[i][j] == -1:
        #         if text1[i] == text2[j]:
        #             memo[i][j] = 1 + dp(i + 1, j + 1)
        #         else:
        #             memo[i][j] = max(dp(i, j + 1), dp(i + 1, j))

        #     return memo[i][j]

        # return dp(0, 0)
