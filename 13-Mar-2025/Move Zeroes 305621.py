# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, right = 0, 0

        while right < len(nums):

            # if non-zero found by right, swap it with left
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

            right += 1
        