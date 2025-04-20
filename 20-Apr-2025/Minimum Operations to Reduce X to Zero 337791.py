# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        n = len(nums)
        target = sum(nums) - x
        max_len = -1
        window_sum = 0
        left = 0

        for right in range(n):

            # expanding the window,
            window_sum += nums[right]

            while window_sum > target and left <= right:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return n - max_len
