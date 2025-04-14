# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        """ using two pointers, and comparing characters and merging """

        n = len(word1)
        m = len(word2)
        merge = []
        idx1 = 0
        idx2 = 0

        while idx1 < n and idx2 < m:

            if word1[idx1:] > word2[idx2:]:
                merge.append(word1[idx1])
                idx1 += 1

            else:
                merge.append(word2[idx2])
                idx2 += 1

        while idx1 < n:
            merge.append(word1[idx1])
            idx1 += 1

        while idx2 < m:
            merge.append(word2[idx2])
            idx2 += 1

        return ''.join(merge)
