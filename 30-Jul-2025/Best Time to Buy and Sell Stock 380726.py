# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def dp(i, min_price, max_profit):
            if i == n:
                return max_profit

            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

            return dp(i + 1, min_price, max_profit)

        return dp(0, float('inf'), 0)
