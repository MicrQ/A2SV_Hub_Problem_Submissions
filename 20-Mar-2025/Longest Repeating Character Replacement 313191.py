# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        max_frq = 0
        max_substring = 0
        frqs = defaultdict(int)

        # loop over string and count frequency
        for right in range(len(s)):

            # expand the window
            frqs[s[right]] += 1
            # track the max frequency
            max_frq = max(max_frq, frqs[s[right]])

            # check if the replacement is greater than k
            if (right - left + 1) - max_frq > k:
                # shrink the window from left
                frqs[s[left]] -= 1
                left += 1

            max_substring = max(max_substring, right - left + 1)

        return max_substring
