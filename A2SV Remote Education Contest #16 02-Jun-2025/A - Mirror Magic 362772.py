# Problem: A - Mirror Magic - https://codeforces.com/gym/613405/problem/A

tests = int(input())

for _ in range(tests):

    a = input()
    maps = {'p': 'q', 'q': 'p', 'w': 'w'}

    b = ''.join(maps[c] for c in reversed(a))

    print(b)
