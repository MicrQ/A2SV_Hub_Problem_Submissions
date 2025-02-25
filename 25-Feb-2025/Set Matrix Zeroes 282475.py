# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # memorizing the row and column where 0 appears
        rows = set()
        cols = set()
        m =  len(matrix)
        n = len(matrix[0])

        # looping through the matrix and memorize position of 0
        for row in range(m):
            for col in range(n):

                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)

        # looping through the matrix again and changing marked cells to 0
        for row in range(m):
            for col in range(n):

                if row in rows or col in cols:
                    matrix[row][col] = 0
