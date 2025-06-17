# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        visited = set()
        def dfs(node):
            if node == destination:
                return True

            visited.add(node)
            for negh in graph[node]:
                if negh not in visited:
                    if dfs(negh):
                        return True

            return False

        return dfs(source)
