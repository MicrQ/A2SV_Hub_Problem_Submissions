# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ using the helper method """
        in_order = []
        self.helper(root, in_order)

        return in_order

    def helper(self, current: Optional[TreeNode], arr: List[int]) -> None:
        """ used for recurcive traverse """
        if not current:
            return

        # traversing to the left
        self.helper(current.left, arr)

        # storing elements in-order
        arr.append(current.val)

        # traverse to right
        self.helper(current.right, arr)