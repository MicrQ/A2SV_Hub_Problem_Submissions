# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # creating a number, frequency map and checking if it's double
        return [num for num, frq in Counter(nums).items() if frq == 2]