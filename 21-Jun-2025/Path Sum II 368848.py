# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []

        def backtrack(node, curr, target):
            if target - node.val == 0 and not(node.left or node.right):
                curr.append(node.val)
                res.append(curr[:])
                return

            new_target = target - node.val
            curr.append(node.val)
            if node.left:
                backtrack(node.left, curr, new_target)
                curr.pop()

            if node.right:
                backtrack(node.right, curr, new_target)
                curr.pop()

        backtrack(root, [], targetSum)
        return res
