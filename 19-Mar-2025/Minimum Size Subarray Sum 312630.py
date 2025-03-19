# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n =  len(nums)
        min_len = n + 1
        sum_ = 0
        left = 0

        for right in range(n):
            sum_ += nums[right]

            while sum_ >= target:

                sum_ -= nums[left]
                min_len = min(min_len, right - left + 1)
                left += 1

        return min_len if min_len <= n else 0
            