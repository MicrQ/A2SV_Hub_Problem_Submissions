# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        max_width = 0
        right_max = [0] * n
        right_max[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        left = 0
        for right in range(n):
            while nums[left] > right_max[right]:
                left += 1

            max_width = max(max_width, right - left)

        return max_width
