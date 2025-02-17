# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        # sliding window :)
        nums.sort()

        max_consecutive = 1

        current_consecutive = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
    
            if nums[i] - nums[i - 1] == 1:
                current_consecutive += 1
                max_consecutive = max(current_consecutive, max_consecutive)

            else:
                current_consecutive = 1

        return max_consecutive