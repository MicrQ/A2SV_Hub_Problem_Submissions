# Problem: E - NATOLI's String Quest - https://codeforces.com/gym/605795/problem/E

s = input()
t = []
u = []
n = len(s)

mins = [''] * n
mins[-1] = s[-1]

for i in range(n - 2, -1, -1):
    mins[i] = min(s[i], mins[i + 1])

for i in range(n):
    while t and t[-1] <= mins[i]:
        u.append(t.pop())

    if s[i] == mins[i]:
        u.append(s[i])
    else:
        t.append(s[i])

while t:
    u.append(t.pop())

print(''.join(u))