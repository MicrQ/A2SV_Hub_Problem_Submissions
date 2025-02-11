# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nums_frq = Counter(nums)
        majority = len(nums) // 3

        return [num for num, frq in nums_frq.items() if frq > majority]
