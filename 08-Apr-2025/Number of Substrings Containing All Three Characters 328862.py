# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        window = [0, 0, 0]
        left = 0
        count = 0

        for right in range(n):
            char_num = ord(s[right]) - ord('a')
            window[char_num] += 1

            while window[0] > 0 and window[1] > 0 and window[2] > 0:
                left_char = ord(s[left]) - 97
                window[left_char] -= 1

                left += 1

            count += left

        return count