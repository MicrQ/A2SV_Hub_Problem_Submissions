# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = [
    [int(num) for num in input().split()]
    for _ in range(5)
]

for row in range(5):
    for col in range(5):
        if matrix[row][col] == 1:
            one_row, one_col = row, col
            break

print(abs(one_row - 2) + abs(one_col - 2))
