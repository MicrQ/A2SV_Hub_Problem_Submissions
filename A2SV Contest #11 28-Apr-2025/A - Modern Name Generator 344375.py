# Problem: A - Modern Name Generator - https://codeforces.com/gym/605795/problem/A

tests = int(input())

for _ in range(tests):

    name = ''.join([s[0] for s in input().split()])

    print(name)