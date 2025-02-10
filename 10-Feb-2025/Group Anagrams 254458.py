# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}

        # looping through all words in strs and using their sorted
        # version as key and appending the orginal to the list value
        for word in strs:

            sorted_word = ''.join(sorted(word))

            # appending to the existing list or creating a key with new list
            if anagram_groups.get(sorted_word) is None:
                anagram_groups[sorted_word] = [word]

            else:
                anagram_groups[sorted_word].append(word)

        return list(anagram_groups.values())