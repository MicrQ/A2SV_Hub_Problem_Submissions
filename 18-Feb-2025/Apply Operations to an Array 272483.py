# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        answer = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                answer.append(nums[i] * 2)
                nums[i + 1] = 0
            else:
                answer.append(nums[i])
        answer.append(nums[-1])

        left = 0

        for i in range(len(answer)):
            if answer[i] != 0:
                answer[left], answer[i] = answer[i], answer[left]
                left += 1

        return answer
