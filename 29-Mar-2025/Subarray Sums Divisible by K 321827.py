# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums)

        # building prefix sum
        for i in range(1, n):
            nums[i] += nums[i - 1]

        result = 0
        memo = defaultdict(int)
        memo[0] = 1

        # counting subarrays divisible by k
        for sum_ in nums:
            mod = sum_ % k

            # in case of negetive
            if mod < 0:
                mod = -mod

            result += memo[mod]
            memo[mod] += 1

        return result