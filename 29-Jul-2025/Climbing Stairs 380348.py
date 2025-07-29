# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0

        if n not in memo:
            memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return memo[n]