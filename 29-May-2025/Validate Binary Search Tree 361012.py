# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        # checking if the arr is strictly increasing
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False

        return True
