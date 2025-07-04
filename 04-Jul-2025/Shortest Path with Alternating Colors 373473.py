# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        reds = defaultdict(list)
        blues = defaultdict(list)
        visited = set()
        res = [-1] * n
        queue = deque([[0, 0, None]])

        for u, v in redEdges:
            reds[u].append(v)
        for u, v in blueEdges:
            blues[u].append(v)

        visited.add((0, None))
        while queue:
            node, path, color = queue.popleft()
            if res[node] == -1:
                res[node] = path

            if color != 'RED':
                for neighbor in reds[node]:
                    if (neighbor, 'RED') not in visited:
                        visited.add((neighbor, 'RED'))
                        queue.append([neighbor, path + 1, 'RED'])

            if color != 'BLUE':
                for neighbor in blues[node]:
                    if (neighbor, 'BLUE') not in visited:
                        visited.add((neighbor, 'BLUE'))
                        queue.append([neighbor, path + 1, 'BLUE'])


        return res