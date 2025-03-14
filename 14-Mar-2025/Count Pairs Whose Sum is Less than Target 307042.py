# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        # using colliding two pointers        
        right = len(nums) - 1
        left = 0
        count = 0

        while left < right:

            while left < right:
                if target > nums[left] + nums[right]:
                    break
                right -= 1

            # left can be paired with the elements until right
            count += (right - left)
            left += 1

        return count