# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        nums[:] = sorted(set(nums))

        return nums[-1] if 3 > len(nums) else nums[-3]
        