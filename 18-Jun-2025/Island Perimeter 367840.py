# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        n = len(grid)
        m = len(grid[0])
        res = 0

        for row in range(n):
            for col in range(m):
                # check if there is neighor land
                if grid[row][col] == 1:
                    count = 4
                    for dx, dy in neighbors:
                        x, y = row + dx, col + dy
                        if (0 <= x < n and 0 <= y < m) and grid[x][y] == 1:
                            count -= 1

                    res += count

        return res