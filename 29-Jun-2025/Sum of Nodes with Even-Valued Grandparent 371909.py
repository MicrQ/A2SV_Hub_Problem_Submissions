# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0

            res = node.val if grandparent and grandparent.val % 2 == 0 else 0
            res += dfs(node.left, node, parent)
            res += dfs(node.right, node, parent)

            return res

        return dfs(root, None, None)