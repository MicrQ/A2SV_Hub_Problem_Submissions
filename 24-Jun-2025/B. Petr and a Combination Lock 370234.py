# Problem: B. Petr and a Combination Lock - https://codeforces.com/contest/1097/problem/B

def dfs(curr, total, n, a):
    if curr == n:
        return total == 0
    if dfs(curr + 1, (total + a[curr]) % 360, n, a):
        return True
    if dfs(curr + 1, (total - a[curr]) % 360, n, a):
        return True
    return False

n = int(input())
a = [int(input()) for _ in range(n)]
if dfs(0, 0, n, a):
    print("YES")
else:
    print("NO")
