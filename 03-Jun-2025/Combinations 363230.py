# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(start, pair):
            if len(pair) == k:
                ans.append(pair[:])
                return

            for i in range(start, n + 1):
                pair.append(i)
                backtrack(i + 1, pair)
                pair.pop()

        backtrack(1, [])

        return ans
