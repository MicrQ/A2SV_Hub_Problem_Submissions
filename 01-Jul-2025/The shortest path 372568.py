# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque

n, m = [int(num) for num in input().split()]
src, dest = [int(num) for num in input().split()]

queue = deque([src])
prev = defaultdict(int)
graph = defaultdict(list)
found = False

for _ in range(m):
    u, v = [int(num) for num in input().split()]
    graph[u].append(v)
    graph[v].append(u)

prev[src] = -1
while queue:
    node = queue.popleft()
    if node == dest:
        found = True
        break

    for neighbor in graph[node]:
        if neighbor not in prev:
            prev[neighbor] = node
            queue.append(neighbor)

if not found:
    print(-1)
else:
    # building the result
    path = []
    curr = dest
    while curr != -1:
        path.append(curr)
        curr = prev[curr]

    print(len(path) - 1)
    print(*path[::-1])
