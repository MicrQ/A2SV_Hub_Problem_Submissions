# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result = set()
        nums.sort()

        for i in range(n):
            target = -nums[i]

            # using twosum technique here
            checked = {}
            for j in range(i + 1, n):

                num = checked.get(target - nums[j])
                if num is not None:
                    result.add((nums[i], target - nums[j], nums[j]))
                else:
                    checked[nums[j]] = j

        return [list(triplet) for triplet in result]
