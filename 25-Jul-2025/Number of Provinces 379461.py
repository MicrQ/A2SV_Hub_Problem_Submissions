# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1

        return count
