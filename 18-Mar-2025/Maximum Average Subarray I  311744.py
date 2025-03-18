# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        sum_ = 0

        for i in range(k):
            sum_ += nums[i]

        max_sum = sum_
        for i in range(k, len(nums)):

            sum_ += nums[i] - nums[i - k]
            max_sum = max(max_sum, sum_)

        return max_sum / k