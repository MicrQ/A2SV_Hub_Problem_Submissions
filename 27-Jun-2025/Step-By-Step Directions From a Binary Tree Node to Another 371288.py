# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findNodePath(node, target, path):
            if node and node.val == target:
                return path
            if not node:
                return None

            path.append('L')
            left = findNodePath(node.left, target, path)
            if left:
                return left

            path.pop()
            path.append('R')
            right = findNodePath(node.right, target, path)
            if right:
                return right
            path.pop()

            return None

        startPath = findNodePath(root, startValue, [])
        destPath = findNodePath(root, destValue, [])


        i = 0
        slen, dlen = len(startPath), len(destPath)
        while i < slen and i < dlen and startPath[i] == destPath[i]:
            i += 1

        start = 'U' * (slen - i)
        return start + ''.join(destPath[i:])

# [L, L] ... [R, L]