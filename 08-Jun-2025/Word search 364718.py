# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        chars = list(word)
        n, m = len(board), len(board[0])
        word_len = len(word)

        def backtrack(bi, bj, idx, visited):
            if board[bi][bj] != word[idx]:
                return False
            if idx == word_len - 1:
                return True

            for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                di, dj = bi + x, bj + y
                if 0 <= di < n and 0 <= dj < m and (di, dj) not in visited:
                    visited.add((di, dj))
                    if backtrack(di, dj, idx + 1, visited):
                        return True
                    visited.remove((di, dj))

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0, {(i, j)}):
                        return True

        return False