# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        ops = 0

        # loop through the sorted elements
        for i in range(n - 1):

            # checking if the the num is not duplicated and adding
            # number of operations left
            if nums[i] != nums[i + 1]:
                ops += n - (i + 1)

        return ops
            