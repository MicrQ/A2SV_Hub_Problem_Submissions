# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def transpose(matrix):
            res = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    res[j][i] = matrix[i][j]
            return res

        def rotate(matrix):
            transposed = transpose(matrix)
            for row in transposed:
                row.reverse()
            return transposed

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)

        return False
