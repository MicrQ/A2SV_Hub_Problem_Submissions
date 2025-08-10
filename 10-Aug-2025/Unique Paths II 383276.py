# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[-1] * n for _ in range(m)]

        def dp(i, j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if (i, j) == (m - 1, n - 1):
                return 1

            if memo[i][j] == -1:
                memo[i][j] = dp(i + 1, j) + dp(i, j + 1)

            return memo[i][j]

        return dp(0, 0)
