# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_island = 0
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col):
            if not (0 <= row < m and 0 <= col < n) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            area = 1
            for dx, dy in neighbors:
                x, y = row + dx, col + dy
                area += dfs(x, y)

            return area

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    current = dfs(i, j)
                    max_island = max(max_island, current)

        return max_island