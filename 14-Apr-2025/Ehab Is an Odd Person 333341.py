# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
a = [int(num) for num in input().split()]

evens = any(x % 2 == 0 for x in a)
odds = any(x % 2 == 1 for x in a)

if evens and odds:
    a.sort()
    
print(*a)
