# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        grow = 1
        coins = 0
        count = 0

        while coins <= n:
            coins += grow
            grow += 1
            count += 1

        return count - 1