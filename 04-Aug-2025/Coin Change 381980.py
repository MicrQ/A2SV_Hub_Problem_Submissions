# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(total):
            if total == amount:
                return 0

            if total > amount: # no need to continue the computation
                return float('inf')

            if total not in memo:
                curr_min = float('inf')
                for coin in coins: # checking for every possibility
                    curr_min = min(curr_min, 1 + dp(total + coin))

                memo[total] = curr_min

            return memo[total]

        res = dp(0)
        return res if res != float('inf') else -1
