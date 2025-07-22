# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = [0] * n
        queue = deque()
        ancestors = [set() for _ in range(n)]

        # building the graph
        for frm, to in edges:
            graph[frm].append(to)
            in_degree[to] += 1

        # identifying the source nodes
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        # topologically orering
        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                ancestors[nei].add(node)
                ancestors[nei].update(ancestors[node])
                in_degree[nei] -= 1

                if in_degree[nei] == 0:
                    queue.append(nei)

        return [sorted(anc) for anc in ancestors]
