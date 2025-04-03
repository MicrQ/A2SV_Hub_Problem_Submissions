# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = [int(num) for num in input().split()]
books = [int(mins) for mins in input().split()]

max_books = 0
left = 0
total_mins = 0

for right in range(n):
    """
        using dynamic sliding window to find
        the maximum number of books he can read
    """

    # expanding the window
    total_mins += books[right]

    if total_mins > t:
        # shrinking the window if it exeeds the free time
        total_mins -= books[left]
        left += 1

    max_books = max(max_books, right - left + 1)

print(max_books)
