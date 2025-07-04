# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n ,m = len(mat), len(mat[0])
        queue = deque()
        visited = set()
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        while queue:
            for _ in range(len(queue)):
                cellx, celly = queue.popleft()

                for dx, dy in neighbors:
                    x, y = cellx + dx, celly + dy
                    if 0 <= x < n and 0 <= y < m and (x, y) not in visited:
                        visited.add((x, y))
                        queue.append((x, y))
                        mat[x][y] = mat[cellx][celly] + 1

        return mat