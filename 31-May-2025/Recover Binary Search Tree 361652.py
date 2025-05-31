# Problem: Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nodes = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        # looking for node mistake
        first = second = None
        for i in range(len(nodes) - 1):
            if nodes[i].val >= nodes[i + 1].val:
                if not first:
                    first = nodes[i]
                second = nodes[i + 1]

        # checking if there is mistake at all
        if first and second:
            first.val, second.val = second.val, first.val