# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int, memo={}) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        if n not in memo:
            memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        return memo[n]
