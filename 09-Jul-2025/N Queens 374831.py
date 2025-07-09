# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        pos_diagonals = set()
        neg_diagonals = set()
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                valid = [''.join(board_row) for board_row in board]
                res.append(valid)
                return

            for col in range(n):
                if (col not in cols
                    and (row - col) not in pos_diagonals
                    and (row + col) not in neg_diagonals):

                    cols.add(col)
                    board[row][col] = 'Q'
                    pos_diagonals.add(row - col)
                    neg_diagonals.add(row + col)

                    backtrack(row + 1)

                    cols.remove(col)
                    board[row][col] = '.'
                    pos_diagonals.remove(row - col)
                    neg_diagonals.remove(row + col)

        backtrack(0)
        return res
