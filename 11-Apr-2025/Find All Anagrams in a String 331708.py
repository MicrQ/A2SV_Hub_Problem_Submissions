# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        left = 0
        k = len(p)
        s_len = len(s)
        p_frq = defaultdict(int)
        window = defaultdict(int)
        anagram_starts = []

        if s_len < k:
            return []

        # counting the frequency of characters in p
        for i in range(k):
            p_frq[p[i]] += 1

        # building the first window
        for i in range(k):
            window[s[i]] += 1

        # checking if the first window is anagram
        if window == p_frq:
            anagram_starts.append(0)

        # sliding the window and looking for anagrams
        for right in range(k, s_len):

            window[s[right]] += 1

            if window[s[left]] == 1:
                del window[s[left]]
            else:
                window[s[left]] -= 1

            left += 1

            if window == p_frq:
                anagram_starts.append(left)

        return anagram_starts
