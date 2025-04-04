# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # base case
        if n == 1:
            return True

        # if n is not divisible by 3, it's not power of 3
        if n <= 0 or n % 3 != 0:
            return False

        return self.isPowerOfThree(n // 3)
