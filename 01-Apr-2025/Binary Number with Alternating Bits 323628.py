# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        # bit manipulation is the best technique
        # shifting n to right by 1bit and XORing it with the old n is the solution
        shifted = n >> 1
        shifted ^= n

        # make sure all bits are 1's and return
        return shifted & (shifted + 1) == 0