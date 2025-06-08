# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        chars = list(word)
        n, m = len(board), len(board[0])

        def backtrack(bi, bj, curr, visited):
            if chars == curr:
                return True
            if chars[:len(curr)] != curr:
                return False

            for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                di, dj = bi + x, bj + y
                if 0 <= di < n and 0 <= dj < m and (di, dj) not in visited:
                    curr.append(board[di][dj])
                    visited.add((di, dj))
                    if backtrack(di, dj, curr, visited):
                        return True
                    curr.pop()
                    visited.remove((di, dj))

            return False

        for i in range(n):
            for j in range(m):
                if backtrack(i, j, [board[i][j]], {(i, j)}):
                    return True

        return False