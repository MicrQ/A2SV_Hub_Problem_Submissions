# Problem: Search in a BST - https://leetcode.com/problems/search-in-a-binary-search-tree/description/

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)