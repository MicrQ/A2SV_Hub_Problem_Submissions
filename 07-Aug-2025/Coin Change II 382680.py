# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}

        def dp(idx, total):
            if total == 0:
                return 1

            if total < 0 or idx >= n:
                return 0

            if (idx, total) not in memo:
                include = dp(idx, total - coins[idx])
                exclude = dp(idx + 1, total)

                memo[(idx, total)] = include + exclude

            return memo[(idx, total)]

        return dp(0, amount)
