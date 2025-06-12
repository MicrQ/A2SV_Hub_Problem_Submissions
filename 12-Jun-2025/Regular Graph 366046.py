# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n, m = [int(num) for num in input().split()]

graph = [0] * (n + 1)
for i in range(m):
    node1, node2 = [int(num) for num in input().split()]
    graph[node1] += 1
    graph[node2] += 1

if all(graph[1] == value for value in graph[1:]):
    print('YES')
else:
    print('NO')
