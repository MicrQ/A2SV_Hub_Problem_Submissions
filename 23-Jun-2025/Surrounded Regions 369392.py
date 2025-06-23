# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        def dfs(rw, cl):
            if not (0 <= rw < row and 0 <= cl < col) or board[rw][cl] != 'O':
                return

            board[rw][cl] = 'o'

            for dx, dy in neighbors:
                x, y = rw + dx, cl + dy
                dfs(x, y)

        for i in range(row):
            for j in range(col):
                if (i in (0, row - 1) or j in (0, col - 1)) and board[i][j] == 'O':
                    dfs(i, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'o':
                    board[i][j] = 'O'