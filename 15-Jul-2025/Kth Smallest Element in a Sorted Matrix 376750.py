# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        heap = []

        for i in range(n):
            for j in range(m):
                heappush(heap, matrix[i][j])

        while k > 1:
            heappop(heap)
            k -= 1

        return heappop(heap)