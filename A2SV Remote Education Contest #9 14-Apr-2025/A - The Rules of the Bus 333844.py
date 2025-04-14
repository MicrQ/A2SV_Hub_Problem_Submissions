# Problem: A - The Rules of the Bus - https://codeforces.com/gym/603156/problem/A

tests = int(input())

for _ in range(tests):

    n = int(input())
    seats = [int(num) for num in input().split()]

    captured = set()
    captured.add(seats[0])

    for i in range(1, n):

        seat = seats[i]
        if seat - 1 not in captured and seat + 1 not in captured:
            print('NO')
            break

        captured.add(seat)

    else:
        print('YES')
