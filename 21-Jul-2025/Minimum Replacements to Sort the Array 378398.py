# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n - 2, -1, -1):
            """ starting from the 2nd last number """

            if nums[i] > nums[i + 1]:
                """ calculating the minimal split (making the numbers
                    as close to equal as possible)
                """
                splits = ceil(nums[i] / nums[i + 1])
                res += splits - 1

                nums[i] //= splits

        return res
