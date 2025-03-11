# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = [int(num) for num in input().split()]
nums1 = [int(num) for num in input().split()]
nums2 = [int(num) for num in input().split()]
 
result = []
 
i = j = 0
 
while j < m and i < n:
    
    if nums1[i] < nums2[j]:
        result.append(nums1[i])
        i += 1
    else:
        result.append(nums2[j])
        j += 1
        
while i < n:
    result.append(nums1[i])
    i += 1
    
while j < m:
    result.append(nums2[j])
    j += 1
    
print(*result)