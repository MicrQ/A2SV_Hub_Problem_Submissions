# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]

        for i in range(2, numRows):
            row = [1] * (i + 1)

            # building row based on the previous row
            for j in range(1, i):
                row[j] = res[-1][j] + res[-1][j - 1]
            res.append(row)

        return res[:numRows]
