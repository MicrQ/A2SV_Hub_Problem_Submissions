# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_pal(s: str, left: int, right: int):
            """ helper """

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        # now do the normal check and use the helper when chars dont match
        left = 0
        right = len(s) - 1

        while left < right:

            # chars didnt match?
            if s[left] != s[right]:
                return is_pal(s, left + 1, right) or is_pal(s, left, right - 1)

            left += 1
            right -= 1

        return True
