# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:

        def helper(n: int, memo: dict[int, int]={}) -> int:
            """ helper """

            if n == 0:
                return 0
            if n == 1:
                return 1

            if memo.get(n) is None:
                memo[n] = self.fib(n - 1) + self.fib(n - 2)

            return memo[n]

        return helper(n)
