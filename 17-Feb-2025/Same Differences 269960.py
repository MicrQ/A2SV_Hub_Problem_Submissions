# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import Counter

tests = int(input())

for i in range(tests):
    # for each test cases

    n = int(input())
    a = list(map(int, input().split()))

    count = 0

    num_idx_diff = [num - i for i, num in enumerate(a)]
    num_idx_diff_frq = Counter(num_idx_diff)

    # looping through the frequencies and counting unique pairs
    for _, frq in num_idx_diff_frq.items():

        # addeding the unique pairs(calculating using combination formula)
        count += frq * (frq - 1) // 2

    print(count)

    # bruteforce
    # for i in range(n):
    #     for j in range(i + 1, n):

    #         if a[j] - a[i] == j - i:
    #             count += 1