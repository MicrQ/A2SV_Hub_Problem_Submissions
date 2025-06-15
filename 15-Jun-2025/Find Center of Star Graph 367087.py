# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        graph = defaultdict(int)

        for u, v in edges:
            graph[u] += 1
            graph[v] += 1

        for node, edge in graph.items():
            if edge > 1:
                return node

        return -1
