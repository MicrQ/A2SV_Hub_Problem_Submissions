# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        res = 1

        for coin in coins:
            """ checking if there is a gap between the
                reachable and the current coin
            """
            if coin > res:
                break

            res += coin

        # making sure the count includes
        return res
