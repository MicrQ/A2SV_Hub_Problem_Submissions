# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        min_divisor = right

        while left <= right:
            divisor = left + (right - left) // 2

            sum_ = 0
            for num in nums:
                sum_ += ceil(num / divisor)

            if sum_ <= threshold:
                min_divisor = min(min_divisor, divisor)
                right = divisor - 1
            else:
                left = divisor + 1

        return min_divisor