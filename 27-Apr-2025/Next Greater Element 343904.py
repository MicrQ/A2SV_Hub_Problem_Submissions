# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val_idx_pair = {val: idx for idx, val in enumerate(nums1)}
        n = len(nums1)
        res = [-1] * n
        stack = []

        for i in range(len(nums2)):
            current = nums2[i]

            while stack and stack[-1] < current:
                idx = val_idx_pair[stack.pop()]
                res[idx] = current

            if current in val_idx_pair:
                stack.append(current)

        return res
