# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        colored = {}
        def dfs(node, color):
            if node in colored:
                return colored[node] == color

            colored[node] = color
            for neighbor in graph[node]:
                if not dfs(neighbor, 1 - color):
                    return False

            return True

        for i in range(n):
            if i not in colored:
                if not dfs(i, 0):
                    return False

        return True
