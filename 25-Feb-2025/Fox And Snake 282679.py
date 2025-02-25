# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

m, n = [int(num) for num in input().split()]

right = True

for row in range(m):

    if row % 2 == 0:
        print('#' * n)

    else:
        if right:
            print('.' * (n - 1) + '#')
            right = False
        else:
            print('#' + '.' * (n - 1))
            right = True
