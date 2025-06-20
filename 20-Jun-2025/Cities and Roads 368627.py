# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())

count = 0
for i in range(n):
    row = [int(num) for num in input().split()]
    for j in range(i + 1, n):

        if row[j] == 1:
            count += 1

print(count)
