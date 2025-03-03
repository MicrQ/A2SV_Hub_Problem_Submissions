# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        return self.helper(n)

    def helper(self, n, memo={}):
        """ used to help the main function for efficiency """

        if n in memo:
            return memo[n]

        if n <= 2:
            return n

        memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)

        return memo[n]