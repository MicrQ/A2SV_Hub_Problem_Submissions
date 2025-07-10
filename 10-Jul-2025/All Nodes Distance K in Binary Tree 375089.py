# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        parents = {}
        visited = set()
        queue = deque()
        self.targetNode = None

        def preorder(node, parent=None):
            """ to travers on the tree and map nods with their parent """
            if not node:
                return

            if node.val == target.val:
                self.targetNode = node

            parents[node] = parent
            preorder(node.left, node)
            preorder(node.right, node)

        # doing the traverse and mapping the parent for each node
        preorder(root)

        # BFS on the parents map and find the result
        visited.add(self.targetNode)
        queue.append((self.targetNode, 0))
        while queue:
            node, distance = queue.popleft()
            if distance == k:
                res.append(node.val)
                continue

            for neighbor in [node.left, node.right, parents[node]]:
                if neighbor and neighbor not in visited:
                    queue.append((neighbor, distance + 1))
                    visited.add(neighbor)

        return res
