# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = [int(num) for num in input().split()]
nums = [int(num) for num in input().split()]

left = 0
max_len = 0
sum_ = 0

for right in range(n):

    sum_ += nums[right]

    while sum_ > s:
        sum_ -= nums[left]
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)
