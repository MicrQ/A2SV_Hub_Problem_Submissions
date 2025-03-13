# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = 0

        for right in range(len(nums)):

            # making sure that right is not pointing on val
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

            right += 1

        return left