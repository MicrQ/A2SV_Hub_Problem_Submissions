# Problem: Path Sum - https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        res = targetSum - root.val
        if res == 0 and (not root.left and not root.right):
            return True

        return self.hasPathSum(root.left, res) or self.hasPathSum(root.right, res)
            