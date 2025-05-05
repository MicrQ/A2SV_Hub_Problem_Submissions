# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def recursive(self, nums, left, right, turn):
        if left == right:
            return nums[left] if turn == 1 else -nums[left]

        if turn == 1:
            took_left = nums[left] + self.recursive(nums, left + 1, right, 2)
            took_right = nums[right] + self.recursive(nums, left, right - 1, 2)

            return max(took_left, took_right)

        took_left = -nums[left] + self.recursive(nums, left + 1, right, 1)
        took_right = -nums[right] + self.recursive(nums, left, right - 1, 1)

        return min(took_left, took_right)

    def predictTheWinner(self, nums: List[int]) -> bool:

        result = self.recursive(nums, 0, len(nums) - 1, 1)

        return result >= 0