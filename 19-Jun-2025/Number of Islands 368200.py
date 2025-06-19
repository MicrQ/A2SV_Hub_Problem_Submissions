# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        row = len(grid)
        col = len(grid[0])
        count = 0

        def dfs(rw, cl):
            if not (0 <= rw < row and 0 <= cl < col) or grid[rw][cl] == '0':
                return

            grid[rw][cl] = '0'
            for rr, cc in neighbors:
                x, y = rw + rr, cl + cc
                dfs(x, y)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count