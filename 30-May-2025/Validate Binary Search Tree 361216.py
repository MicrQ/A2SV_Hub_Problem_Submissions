# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

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
