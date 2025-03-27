# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # constant extra spaces
        red, white, blue = 0, 0, 0

        for color in nums:
            if color == 0:
                red += 1

            elif color == 1:
                white += 1

            else:
                blue += 1

        # sorting them
        for i in range(len(nums)):

            if red > 0:
                nums[i] = 0
                red -= 1

            elif white > 0:
                nums[i] = 1
                white -= 1

            else:
                nums[i] = 2




        # # counting sort
        # count = [0] * (max(nums) + 1)

        # for num in nums:
        #     count[num] += 1

        # pos = 0
        # for i in range(len(count)):

        #     # handling duplicates
        #     for _ in range(count[i]):
        #         nums[pos] = i
        #         pos += 1
