# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        mins = 0
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))

        #bfs
        while queue:
            rotted = False

            for i in range(len(queue)):
                cellx, celly = queue.popleft()

                # adding fresh neighors to the queue
                for dx, dy in neighbors:
                    x, y = cellx + dx, celly + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                        queue.append((x, y))
                        grid[x][y] = 2
                        rotted = True

            if rotted:
                mins += 1

        # checking if there is unreached fresh orange
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return mins
