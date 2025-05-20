# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumleft = [0] * n
        sumright = [0] * n

        for i in range(1, n):
            sumleft[i] = sumleft[i - 1] + nums[i - 1]

        for i in range(n - 2, -1, -1):
            sumright[i] = sumright[i + 1] + nums[i + 1]

        for i in range(n):
            if sumright[i] == sumleft[i]:
                return i

        return -1