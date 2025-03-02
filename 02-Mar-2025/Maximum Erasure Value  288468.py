# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        # using sliding window
        max_sum = 0
        current_sum = 0
        uniques = set()
        left = 0

        # iterating through the list and sum unique elements
        for right in range(len(nums)):

            # remove elements from the left if duplicate is found
            # until no more duplicate
            while nums[right] in uniques:
                uniques.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            uniques.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)

        return max_sum