# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # base case
        if n == 1:
            return True
        if n < 3:
            return False

        return self.isPowerOfThree(n / 3)
