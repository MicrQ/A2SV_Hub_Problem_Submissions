# Problem: 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        left = 0
        window = defaultdict(int)
        max_len = 0

        for right in range(n):
            char = s[right]

            # adding the char to the window | expanding it
            window[char] += 1

            """
                checking is there is a character repetition
                and shrinkin from the left until it's no longer repeated
            """
            while window[char] > 1:
                window[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
