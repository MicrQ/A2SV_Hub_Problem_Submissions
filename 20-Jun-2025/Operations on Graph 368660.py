# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict

class Operations:
    def __init__(self):
        """ initializes the graph """
        self.graph = defaultdict(list)

    def addEdge(self, u: int, v: int) -> None:
        """ adds undirected edge b/n u and v """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def vertix(self, u: int) -> None:
        """ print neighbors of u """
        print(*self.graph[u])

op = Operations()
n = int(input())
k = int(input())

for _ in range(k):
    line = [int(num) for num in input().split()]

    if line[0] == 1:
        op.addEdge(line[1], line[2])
    else:
        op.vertix(line[1])
