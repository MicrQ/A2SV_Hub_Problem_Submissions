# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

from collections import defaultdict

n = int(input())
adj_list = defaultdict(list)

for i in range(n):
    row = [int(num) for num in input().split()]
    for j in range(n):
        if row[j] == 1:
            adj_list[i + 1].append(j + 1)

for node, neighbors in adj_list.items():
    print(len(neighbors), *neighbors)
