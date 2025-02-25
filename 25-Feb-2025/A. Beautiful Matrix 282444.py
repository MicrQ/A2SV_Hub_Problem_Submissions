# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = [[int(bit) for bit in input().split()]
          for _ in range(5)]

row = 0

for i in range(5):
    if 1 in matrix[i]:
        row = i
        break

col = matrix[row].index(1)

print(abs(2 - row) + abs(2 - col))