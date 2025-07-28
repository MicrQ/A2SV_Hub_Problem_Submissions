# Problem: B - Planning Journey - https://codeforces.com/gym/625306/problem/B

tests = int(input())
 
for _ in range(tests):
    n, k = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
 
    count = 0
    sum_ = sum(a[:k])
    i = 0
 
    while i <= n - k:
        if sum_ == 0:
            count += 1
            i += k + 1
            sum_ = sum(a[i:i+k])
        else:
            if i + k < n:
                sum_ += a[i + k] - a[i]
            i += 1
 
    print(count)