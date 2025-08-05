# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]

        for i in range(2, n + 1):
            i_fib = dp[i - 1] + dp[i - 2]
            dp.append(i_fib)

        return dp[n]
