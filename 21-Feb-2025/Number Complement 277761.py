# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:

        if num == 1:
            return 0

        mask = 1
        # create a mask with all bits set to 1 and XOR it with num
        while mask <= num:
            mask <<= 1

        # To get the number with all bits set to 1
        mask -= 1

        return num ^ mask
