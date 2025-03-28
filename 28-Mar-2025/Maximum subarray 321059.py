# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)

        # calculating the prefix sum
        for i in range(1, n):
            nums[i] += nums[i - 1]

        # calculating the maximum subarray
        max_subarray = nums[0]
        min_prefix = 0

        for i in range(n):
            # finding the max subarray by subtracting the minimum
            # cause i dont need it to find maximum subarray sum
            max_subarray = max(max_subarray, nums[i] - min_prefix)
            min_prefix = min(min_prefix, nums[i])

        return max_subarray
