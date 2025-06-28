# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        directions = {
            1: [(0,-1),(0,1)],
            2: [(-1,0),(1,0)],
            3: [(0,-1),(1,0)],
            4: [(0,1),(1,0)],
            5: [(0,-1),(-1,0)],
            6: [(0,1),(-1,0)]
        }
        visited = set([0, 0])

        def dfs(r, c):
            if (r, c) == (n - 1, m - 1):
                return True

            for dx, dy in directions[grid[r][c]]:
                x, y = r + dx, c + dy
                if (
                    0 <= x < n and 0 <= y < m and
                    (x, y) not in visited and
                    (-dx, -dy) in directions[grid[x][y]]):

                    visited.add((x, y))
                    if dfs(x, y):
                        return True

            return False

        return dfs(0, 0)
