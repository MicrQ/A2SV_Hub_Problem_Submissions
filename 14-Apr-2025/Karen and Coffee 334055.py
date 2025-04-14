# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = [int(num) for num in input().split()]
limit = 200002

prefix = [0 for _ in range(limit)]

for _ in range(n):
    li, ri = [int(num) for num in input().split()]

    prefix[li] += 1
    prefix[ri + 1] -= 1

# building the first prefix sum
for i in range(1, limit):
    prefix[i] += prefix[i - 1]

# making it binary based on k
for i in range(limit):
    if prefix[i] < k:
        prefix[i] = 0

    else:
        prefix[i] = 1

# building the last prefix sum
for i in range(1, limit):
    prefix[i] += prefix[i - 1]

for _ in range(q):
    qstart, qend = [int(num) for num in input().split()]

    left = prefix[qstart - 1] if qstart > 0 else 0
    right = prefix[qend]

    print(right - left)
