# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return (None, 0)

            lca_left, left_depth = dfs(node.left)
            lca_right, right_depth = dfs(node.right)

            if left_depth > right_depth: # the deepest lca is to the left
                return (lca_left, left_depth + 1)

            elif right_depth > left_depth: # the deepest lca is to the right
                return (lca_right, right_depth + 1)
            
            return (node, left_depth + 1) # the node itself is the deppest lca

        return dfs(root)[0]
