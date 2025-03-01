# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        abs_sum = 0
        ngtv_count = 0
        abs_min = None

        # loop through the matrix and sum the absolute value
        # count -ves
        # find the smallest absolute value

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                if matrix[row][col] < 0:
                    ngtv_count += 1

                val = abs(matrix[row][col])
                abs_min = val if abs_min is None else val if val < abs_min else abs_min

                abs_sum += val

        return abs_sum if ngtv_count % 2 == 0 else abs_sum - (2 * abs_min)
                