# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting sort
        count = [0] * (max(nums) + 1)

        for num in nums:
            count[num] += 1

        pos = 0
        for i in range(len(count)):

            # handling duplicates
            for _ in range(count[i]):
                nums[pos] = i
                pos += 1
