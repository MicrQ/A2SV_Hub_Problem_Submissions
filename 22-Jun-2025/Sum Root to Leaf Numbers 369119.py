# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        def dfs(node, curr):
            if not node:
                return

            new_curr = curr * 10 + node.val

            if not node.left and not node.right:
                self.result += new_curr

            dfs(node.left, new_curr)
            dfs(node.right, new_curr)


        dfs(root, 0)
        return self.result
