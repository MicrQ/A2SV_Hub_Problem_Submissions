# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for anagram in strs:
            key = ''.join(sorted(anagram))
            anagrams[key].append(anagram)

        return list(anagrams.values())