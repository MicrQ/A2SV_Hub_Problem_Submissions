# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(nums):
            if not nums:
                return None

            val = max(nums)
            idx = nums.index(val)
            node = TreeNode(val)

            node.left = helper(nums[:idx])
            node.right = helper(nums[idx + 1:])

            return node

        return helper(nums)