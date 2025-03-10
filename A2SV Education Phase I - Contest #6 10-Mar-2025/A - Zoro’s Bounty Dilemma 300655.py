# Problem: A - Zoro’s Bounty Dilemma - https://codeforces.com/gym/594356/problem/A

tests = int(input())

for test in range(tests):

    s = input()

    res = ''

    for char in s:
        if not res and char != '=':
            res = char

        elif res and char != res and char != '=':
            print('?')
            break

    else:
        print(res if res else '=')
