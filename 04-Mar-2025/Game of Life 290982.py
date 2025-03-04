# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        neighbors = {
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        }

        # looping the matrix
        for row in range(m):
            for col in range(n):

                # count neighbors a live
                lives = 0
                for nbr in neighbors:
                    row_x, col_y = row + nbr[0], col + nbr[1]

                    if 0 <= row_x < m and 0 <= col_y < n and abs(board[row_x][col_y]) == 1:
                        lives += 1

                if board[row][col] == 1:
                    if lives < 2:
                        board[row][col] = -1

                    elif lives > 3:
                        board[row][col] = -1

                else:
                    if lives == 3:
                        board[row][col] = 2

        # modifiying it accordingly
        for row in range(m):
            for col in range(n):

                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
