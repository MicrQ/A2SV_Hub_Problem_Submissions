# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        i = 0
        seconds = 0

        while tickets[k] > 0:
            idx = i % n
            if tickets[idx] > 0:
                tickets[idx] -= 1
                seconds += 1
            i += 1

        return seconds
