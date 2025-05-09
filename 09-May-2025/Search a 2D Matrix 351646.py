# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row_l, row_r = 0, m - 1
        col_l, col_r = 0, n - 1
        row = -1

        while row_l <= row_r:
            mid = row_l + (row_r - row_l) // 2

            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            elif matrix[mid][0] < target:
                row_l = mid + 1
            else:
                row_r = mid - 1

        if row == -1:
            return False

        while col_l <= col_r:
            col_mid = col_l + (col_r - col_l) // 2

            if matrix[row][col_mid] == target:
                return True
            elif matrix[row][col_mid] > target:
                col_r = col_mid - 1
            else:
                col_l = col_mid + 1

        return False