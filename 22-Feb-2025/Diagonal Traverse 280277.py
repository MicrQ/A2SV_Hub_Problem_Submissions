# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        # grouping diagonals
        groups = defaultdict(list)
        result = []

        for row in range(len(mat)):
            for col in range(len(mat[0])):

                groups[row + col].append(mat[row][col])

        # looping through the grouped diagonals
        for grp, elems in groups.items():

            # traverse from bottom to right top
            if grp % 2 == 0:
                result.extend(elems[::-1])

            # travese from top to left bottom
            else:
                result.extend(elems)

        return result
