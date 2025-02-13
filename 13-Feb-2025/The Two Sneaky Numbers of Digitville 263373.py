# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        # creating num, num-frequency map and adding the num if its frq is more than 1
        return [num for num, frq in Counter(nums).items() if frq > 1]