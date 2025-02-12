# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nums_frq = Counter(nums)
        majority = len(nums) // 3

        return [num for num, frq in nums_frq.items() if frq > majority]
