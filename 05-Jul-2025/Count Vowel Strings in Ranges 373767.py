# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        prefix = [0]
        result = []

        for word in words:
            val = 0
            if word[0] in vowels and word[-1] in vowels:
                val = 1
            prefix.append(prefix[-1] + val)

        for start, end in queries:
            count = prefix[end + 1] - prefix[start]
            result.append(count)

        return result
