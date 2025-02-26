# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        """ preparing list of tuples to identify the indices of the hourglass """
        m = len(grid)
        n = len(grid[0])
        hourglass = {
            (0, 0), (0, 1), (0, 2),
                    (1, 1),
            (2, 0), (2, 1), (2, 2)
        }

        max_sum = 0
        # looping through the grid
        for row in range(m - 2):
            for col in range(n - 2):

                inner_sum = 0
                # calculating the summation of the hourglass
                for pair in hourglass:
                    cellx = row + pair[0]
                    celly = col + pair[1]

                    inner_sum += grid[cellx][celly]

                max_sum = max(max_sum, inner_sum)

        return max_sum
