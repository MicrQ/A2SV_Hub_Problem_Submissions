# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        mask = [0 for _ in range(n + 1)]

        # building the prefix sum list
        for left, right, direction in shifts:

            shift = 1 if direction == 1 else -1
            mask[left] += shift
            mask[right + 1] -= shift

        for i in range(1, n):
            mask[i] += mask[i - 1]

        # shifting the charachters accordingly
        result = []
        for i in range(n):

            char = ord(s[i]) - 97
            shifted = (char + mask[i]) % 26

            result.append(chr(shifted + 97))

        return ''.join(result)