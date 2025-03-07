# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n, k = [int(num) for num in input().split()]
nums = [int(num) for num in input().split()]

nums.sort()

if k == 0:
    print(1 if nums[0] > 1 else -1)

elif k >= n:
    print(nums[-1])
    
elif nums[k] == nums[k - 1]:
    print(-1)
    
else:
    print(nums[k - 1])
