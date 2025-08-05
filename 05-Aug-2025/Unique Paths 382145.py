# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0] * (n + 1) for _ in range(m + 1)]
        mat[1][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                mat[i][j] += mat[i - 1][j] + mat[i][j - 1]

        return mat[m][n]