# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        node = root
        tree_node = TreeNode(val)
        while node:
            if val < node.val:
                if not node.left:
                    node.left = tree_node
                    break

                node = node.left
            else:
                if not node.right:
                    node.right = tree_node
                    break
                node = node.right

        return root
