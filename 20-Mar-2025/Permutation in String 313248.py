# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # frquency map of s1
        k = len(s1)
        s2_len = len(s2)

        if k > s2_len:
            return False

        s1_frq = {}
        for char in s1:
            s1_frq[char] = s1_frq.get(char, 0) + 1

        # creating window with size of k(len(s))
        frq_window = {}
        for i in range(k):
            frq_window[s2[i]] = frq_window.get(s2[i], 0) + 1

        left = 0
        for right in range(k, s2_len):

            if s1_frq == frq_window:
                return True

            # shinking the window from the left
            if frq_window[s2[left]] > 1:
                frq_window[s2[left]] -= 1
            else:
                del frq_window[s2[left]]

            # expanding the window to the right
            frq_window[s2[right]] = frq_window.get(s2[right], 0) + 1
            left += 1

        return s1_frq == frq_window
            