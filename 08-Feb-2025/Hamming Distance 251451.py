# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        # XORing the integers
        result = x ^ y

        count = 0

        # counting the numbers of 1s in the result integer
        while result > 0:
            # using & operand to count 1s
            count += result & 1

            # shifting bits to right || result // 2 works in same way
            result >>= 1


        return count