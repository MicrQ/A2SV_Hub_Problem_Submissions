# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nextGreater = [-1] * n
        stack = []

        for i in range(n * 2 - 1):
            current = nums[i % n]

            while stack and nums[stack[-1] % n] < current:
                idx = stack.pop() % n
                if nextGreater[idx] == -1:
                    nextGreater[idx] = current

            stack.append(i)

        return nextGreater
