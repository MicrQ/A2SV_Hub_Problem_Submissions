# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        left = 0
        long_semi_rep = 0
        count = 0

        for right in range(len(s)):

            # checking if there is a consecutive digit
            if right > 0 and s[right - 1] == s[right]:
                count += 1

            # if more than 1 consecutive is found, shrink the left part
            while count > 1:

                left += 1
                if s[left] == s[left - 1]:
                    count -= 1

            # compute the max semi-repetitive substring
            long_semi_rep = max(long_semi_rep, right - left + 1)

        return long_semi_rep