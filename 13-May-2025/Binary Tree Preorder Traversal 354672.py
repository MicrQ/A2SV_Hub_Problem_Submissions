# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(parent, arr):
            if not parent:
                return

            arr.append(parent.val)
            helper(parent.left, arr)
            helper(parent.right, arr)

        result = []
        helper(root, result)

        return result


            