# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        res = []

        # building the grapg
        for i, equ in enumerate(equations):
            a, b = equ
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))


        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1
            if start == end:
                return 1

            visited.add(start)
            for nei, weight in graph[start]:
                if nei not in visited:
                    res = dfs(nei, end, visited)

                    if res != -1:
                        return res * weight

            return -1 # wrong path

        for a, b in queries:
            res.append(dfs(a, b, set()))

        return res