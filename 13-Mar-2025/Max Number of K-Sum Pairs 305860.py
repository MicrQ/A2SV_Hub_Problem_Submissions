# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        left, right = 0, len(nums) - 1
        count = 0

        while left < right:

            target = nums[left] + nums[right]
            if target == k:
                count += 1
                left += 1
                right -= 1

            elif target < k:
                left += 1

            else:
                right -= 1

        return count