# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        first = second = third = -float('inf')

        for num in nums:

            # checking if it's the max
            if first < num:
                first, second, third = num, first, second

            elif second < num < first:
                second, third = num, second

            elif third < num < second:
                third = num

        return third if third != -float('inf') else first



        # n = len(nums)
        # nums[:] = sorted(set(nums))

        # return nums[-1] if 3 > len(nums) else nums[-3]
        