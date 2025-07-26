# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def backtrack(node, curr=[]):
            if not node.left and not node.right:
                curr.append(str(node.val))
                res.append('->'.join(curr))
                return

            curr.append(str(node.val))

            if node.left:
                backtrack(node.left, curr)
                curr.pop()

            if node.right:
                backtrack(node.right, curr)
                curr.pop()

        backtrack(root)
        return res
