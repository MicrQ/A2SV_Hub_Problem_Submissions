# Problem: B - Square-Free Maximum - https://codeforces.com/gym/613405/problem/B

from math import isqrt


n = int(input())
a = [int(num) for num in input().split()]

def isPerfect(x):
    """ checks if a number is perfect """
    if x < 0:
        return False

    root = isqrt(x)
    return root * root == x

largest = float('-inf')
for num in a:
    if not isPerfect(num):
        largest = max(largest, num)

print(largest)
