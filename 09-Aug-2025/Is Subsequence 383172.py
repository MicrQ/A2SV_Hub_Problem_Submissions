# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        s_len, t_len = len(s), len(t)

        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == s_len
