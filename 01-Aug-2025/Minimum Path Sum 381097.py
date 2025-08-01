# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dp(i, j):
            if (i, j) == (m - 1, n - 1):
                return grid[i][j]

            if i == m or j == n:
                return float('inf')

            if (i, j) not in memo:
                right = dp(i, j + 1)
                down = dp(i + 1, j)

                memo[(i, j)] = min(right, down) + grid[i][j]

            return memo[(i, j)]

        return dp(0, 0)
            