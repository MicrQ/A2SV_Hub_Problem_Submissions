# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        m = len(matrix)
        n = len(matrix[0])

        transposed = [[0] * m for _ in range(n)]

        # traversing throught the matrix and creating its transpose
        for row in range(m):
            for col in range(n):

                transposed[col][row] = matrix[row][col]

        return transposed