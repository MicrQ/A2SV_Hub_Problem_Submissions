# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        new_s = list(s)

        for i in range(len(s)):

            new_s[indices[i]] = s[i]

        return ''.join(new_s)