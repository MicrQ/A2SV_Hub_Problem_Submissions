# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """ building 2D prefix sum for optimal retrival is the best way """
        m, n = len(matrix), len(matrix[0])
        self.rangeSum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum_ = self.rangeSum[i - 1][j] + self.rangeSum[i][j - 1] - self.rangeSum[i - 1][j - 1] + matrix[i - 1][j - 1]
                self.rangeSum[i][j] = sum_

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1, col1, row2 + 1, col2 + 1
        print(r1, c1, r2,c2)

        return self.rangeSum[r2][c2] - self.rangeSum[r1][c2] - self.rangeSum[r2][c1] + self.rangeSum[r1][c1]
