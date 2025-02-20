# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        max_product = 0
        bitmasks = []

        # looping through all words and creating their bitmask representation
        for word in words:

            # calculating their decimal representation
            dec_rep = 0
            for char in word:
                dec_rep |= 1 << (ord(char) - 97)

            bitmasks.append(dec_rep)

        length = len(bitmasks)
        # now, looking for max_product if 2 words have no common char
        for i in range(length - 1):
            for j in range(i + 1, length):
                if bitmasks[i] & bitmasks[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        return max_product
        