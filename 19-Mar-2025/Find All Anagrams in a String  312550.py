# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        starts = []
        p_frq = defaultdict(int)
        k = len(p)
        s_len = len(s)

        if k > s_len:
            return starts

        for char in p:
            # count the frequency of each char in p
            p_frq[char] += 1

        window = defaultdict(int)
        for i in range(k):
            # count the first k elements frequency in s
            window[s[i]] += 1

        if window == p_frq:
            # check if the first window is matches and add it
            starts.append(0)

        for i in range(k, s_len):

            # removing the fisrt element from the window & add from the right
            left_char = s[i - k]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

            window[s[i]] += 1

            if window == p_frq:
                starts.append(i - k + 1)

        return starts