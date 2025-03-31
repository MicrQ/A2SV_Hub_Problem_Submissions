# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # calculation the products of left for each
        prefix = 1
        for i in range(n):
            answer[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        # looping over the answer and nums to get the resulting array
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
