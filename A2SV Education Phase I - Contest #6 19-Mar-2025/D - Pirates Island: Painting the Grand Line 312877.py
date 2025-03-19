# Problem: D - Pirates Island: Painting the Grand Line - https://codeforces.com/gym/594356/problem/D

tests = int(input())
 
for _ in range(tests):
 
    n, m = map(int, input().split())
 
    colors = []
    max_ = 0
    for row in range(n):
        colr = [int(num) for num in input().split()]
        max_ = max(max_, max(colr))
        colors.append(colr)
 
 
    has_color = [0] * (max_ + 1)
 
    for i in range(n):
        for j in range(m):
 
            color = colors[i][j]
            has_color[color] = 1 if has_color[color] != 2 else 2
 
            if (i + 1 < n and colors[i + 1][j] == color
                or j + 1 < m and colors[i][j + 1] == color):
                has_color[color] = 2
 
 
    val = sum(has_color)
    mx = max(has_color)
    print(val - mx)