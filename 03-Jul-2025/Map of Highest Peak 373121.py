# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        queue = deque()
        visited = set()
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if isWater[i][j]:
                    queue.append((i, j))
                    ans[i][j] = 0
                    visited.add((i, j))

        while queue:
            rowx, rowy = queue.popleft()
            for dx, dy in neighbors:
                x, y = rowx + dx, rowy + dy
                if 0 <= x < n and 0 <= y < m and (x, y) not in visited:
                    queue.append((x, y))
                    ans[x][y] = ans[rowx][rowy] + 1
                    visited.add((x, y))

        return ans
