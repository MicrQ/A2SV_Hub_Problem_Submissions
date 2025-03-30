# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        s_len = len(s)
        t_len = len(t)

        i, j = 0, 0

        # using two pointers and checking for character similarity
        while i < s_len and j < t_len:

            # looking for a char similar to t[j]
            while i < s_len and s[i] != t[j]:
                i += 1

            # increment j only if s[i] == t[j] or i < len(s)
            if i != s_len:
                j += 1

            i += 1

        return t_len - j