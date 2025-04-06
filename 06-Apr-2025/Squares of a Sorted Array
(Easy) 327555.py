# Problem: Squares of a Sorted Array
(Easy) - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Solving with O(nlog(n)). just for now
        n = len(nums)

        for i in range(n):
            nums[i] *= nums[i]

        nums.sort()

        return nums