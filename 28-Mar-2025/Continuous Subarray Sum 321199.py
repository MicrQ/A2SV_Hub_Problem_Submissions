# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        # building the prefix sum
        for i in range(1, n):
            nums[i] += nums[i - 1]

        memo = {0: -1}
        for i in range(n):

            reminder = nums[i] % k

            # check if a reminder is found previously
            if reminder in memo and i - memo[reminder] > 1:
                # it is found because the new subarray is multiple of k
                return True

            # never found this reminder? now you did.
            if reminder not in memo:
                memo[reminder] = i

        return False
