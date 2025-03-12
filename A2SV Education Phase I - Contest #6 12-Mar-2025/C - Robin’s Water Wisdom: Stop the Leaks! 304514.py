# Problem: C - Robin’s Water Wisdom: Stop the Leaks! - https://codeforces.com/gym/594356/problem/C

n, A, B = [int(num) for num in input().split()]
nums = [int(num) for num in input().split()]

target = nums[0]
sum_ = sum(nums)
nums = sorted(nums[1:])


# 2 # 1,3,4,5
blocked = 0
for i in range(n - 2, -1, -1):
    if target/sum_ * A >= B:
        break

    sum_ -= nums[i]
    blocked += 1

print(blocked)