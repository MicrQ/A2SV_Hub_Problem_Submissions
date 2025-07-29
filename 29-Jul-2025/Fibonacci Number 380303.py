# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int, memo={}) -> int:
        if n <= 1:
            return n

        if n not in memo:
            memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)

        return memo[n]
