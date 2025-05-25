# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff = 0

        self.helper(root, root.val, root.val)

        return self.max_diff

    def helper(self, node, min_, max_):
        if not node:
            return

        self.max_diff = max(self.max_diff, abs(node.val - min_), abs(node.val - max_))

        self.helper(node.left, min(min_, node.val), max(max_, node.val))
        self.helper(node.right, min(min_, node.val), max(max_, node.val))