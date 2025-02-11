# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        pairs = 0
        leftover = 0

        # creating a frequency map/table and looping over it
        for frq in Counter(nums).values():

            pairs += frq // 2
            leftover += frq % 2

        return [pairs, leftover]