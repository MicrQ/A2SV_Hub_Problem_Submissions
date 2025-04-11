# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # bruteforce
        longest = ''
        n = len(s)

        for i in range(n):
            for j in range(i, n):

                sub_s = s[i:j + 1]
                if sub_s == sub_s[::-1] and len(sub_s) > len(longest):
                    longest = sub_s

        return longest


    #     """ using the helper method and looking for the longest palindrome """
    #     left, right = 0, len(s) - 1


    #     while left < right:
    #         if self.isPalindrome(s, left, right):
    #             return s[left:right + 1]

    #         elif self.isPalindrome(s, left + 1, right):
    #             return s[left + 1:right + 1]

    #         elif self.isPalindrome(s, left, right - 1):
    #             return s[left:right]

    #         left += 1
    #         right -= 1

    #     return s[left:right + 1]


    # def isPalindrome(self, s: str, left: int, right: int) -> bool:
    #     """ checks if a string is palinfrom """

    #     while left < right:

    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1

    #     return True
