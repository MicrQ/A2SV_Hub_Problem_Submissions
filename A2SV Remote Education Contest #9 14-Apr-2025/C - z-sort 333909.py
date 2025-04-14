# Problem: C - z-sort - https://codeforces.com/gym/603156/problem/C

n = int(input())
a = [int(num) for num in input().split()]

a.sort()
answer = []
left, right = 0, n - 1
lturn = True

while left <= right:

    if lturn:
        answer.append(a[left])
        left += 1

    else:
        answer.append(a[right])
        right -= 1

    lturn = not lturn

print(*answer)
