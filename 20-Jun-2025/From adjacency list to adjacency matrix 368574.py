# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())

adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    neighbors = [int(num) for num in input().split()]
    for neighbor in neighbors[1:]:
        adj_matrix[i][neighbor - 1] = 1

for row in adj_matrix:
    print(*row)
