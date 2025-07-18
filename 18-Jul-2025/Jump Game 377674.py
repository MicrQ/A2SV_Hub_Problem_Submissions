# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1

        for i in range(end, -1, -1):
            if end <= nums[i] + i:
                end = i

        return True if end == 0 else False
