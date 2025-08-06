# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1], [1, 1]]

        for i in range(2, rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, i):
                prev = triangle[-1]
                row[j] = prev[j] + prev[j - 1]
            triangle.append(row)

        return triangle[rowIndex]