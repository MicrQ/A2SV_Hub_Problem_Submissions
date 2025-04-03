# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # creating frequency map of chars in t
        left = 0
        t_frqs = defaultdict(int)

        for char in t:
            t_frqs[char] += 1

        t_frq_size = len(t_frqs)

        s_window_frqs = defaultdict(int)
        complete = 0
        min_len = float('inf')
        result = ''

        # loop through s until all chars in t covered
        for right, char in enumerate(s):

            # expanding the frq window
            s_window_frqs[char] += 1

            if char in t_frqs and s_window_frqs[char] == t_frqs[char]:
                complete += 1

            while left <= right and complete == t_frq_size:
                # forming the resulting string and looking for the min window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # shrinking the window until it no longer contain all chars of t
                s_window_frqs[s[left]] -= 1

                if s[left] in t_frqs and s_window_frqs[s[left]] < t_frqs[s[left]]:
                    complete -= 1

                left += 1

        return result
