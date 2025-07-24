# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev_graph = defaultdict(list)
        out_degrees = [0] * n
        queue = deque()
        safe = [False] * n

        # reversing the graph and counting out-degree of the nodes
        for i in range(n):
            for nei in graph[i]:
                rev_graph[nei].append(i)
                out_degrees[i] += 1

        # identifying terminal node
        for i in range(n):
            if out_degrees[i] == 0:
                queue.append(i)

        # identifying all safe nodes
        while queue:
            node = queue.popleft()
            safe[node] = True

            for nei in rev_graph[node]:
                out_degrees[nei] -= 1

                if out_degrees[nei] == 0: # is this node terminal now?
                    queue.append(nei)

        return [i for i in range(n) if safe[i]]
