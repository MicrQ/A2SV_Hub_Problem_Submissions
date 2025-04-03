# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
cards = [int(num) for num in input().split()]

sereja, dima = 0, 0
serejas_turn = True
left, right = 0, n - 1

while left <= right:
    # looping backward and taking cards on their turn

    if cards[left] > cards[right]:
        picked = cards[left]
        left += 1

    else:
        picked = cards[right]
        right -= 1

    if serejas_turn:
        sereja += picked

    else:
        dima += picked

    serejas_turn = not serejas_turn

print(sereja, dima)