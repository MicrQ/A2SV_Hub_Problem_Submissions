# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        queue = deque([entrance])
        visited = set()
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited.add(tuple(entrance))
        steps = 0
        while queue:
            for _ in range(len(queue)):
                cellx, celly = queue.popleft()
                if (entrance != [cellx, celly]) and (cellx in (0, n - 1) or celly in (0, m - 1)):
                    return steps

                for dx, dy in neighbors:
                    x, y = cellx + dx, celly + dy
                    if 0 <= x < n and 0 <= y < m and (x, y) not in visited and maze[x][y] == '.':
                        queue.append([x, y])
                        visited.add((x, y))

            steps += 1

        return -1
