# Problem: Team - https://codeforces.com/contest/231/problem/A

n = int(input())

count = 0
for _ in range(n):

    if input().count('1') >= 2:
        count += 1
        
print(count)