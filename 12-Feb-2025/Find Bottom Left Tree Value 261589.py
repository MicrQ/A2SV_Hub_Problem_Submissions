# Problem: Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # base
        self.max_depth = -1
        self.leftmost_val = None

        self.DFS(root, 0)
        return self.leftmost_val
    
        
    def DFS(self, current, depth):
        # depth first search(modified)
        if not current:
            return

        # if new leftmost node is found
        if depth > self.max_depth:
            self.max_depth = depth
            self.leftmost_val = current.val

        # recursively going to the left then to right
        self.DFS(current.left, depth + 1)
        self.DFS(current.right, depth + 1)
