# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        # a and b can only be found in range of sqrt(c)
        left, right = 0, int(sqrt(c))

        # using two colliding pointers and looking for the targets
        while left <= right:

            value = left**2 + right**2
            if value == c:
                return True

            elif value < c:
                left += 1
            else:
                right -= 1

        return False
