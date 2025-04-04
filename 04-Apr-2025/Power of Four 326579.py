# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # base case
        if n == 1:
            return True

        # if n is not divisible by 4, it's not power of 4
        if n <= 0 or n % 4 != 0:
            return False

        return self.isPowerOfFour(n // 4)