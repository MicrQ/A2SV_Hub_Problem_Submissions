# Problem: Shifting Letters - https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        n = len(s)

        # calculate the suffix sum
        for i in range(n - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        result = []
        # find the shifted value.(handling surpassing of alphabet)
        for i in range(n):
            
            letter = ord(s[i]) - 97
            shifted = (letter + shifts[i]) % 26

            result.append(chr(shifted + 97))

        return ''.join(result)