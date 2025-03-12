# Problem: B - Thousand Sunny's Network Setup - https://codeforces.com/gym/594356/problem/B

n, k = [int(num) for num in input().split()]
speeds = [int(num) for num in input().split()]

speeds.sort()
print(speeds[n - k])
