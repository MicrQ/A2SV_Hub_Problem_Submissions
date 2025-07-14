# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        neg_piles = [-pile for pile in piles]
        heapify(neg_piles)

        while k > 0:
            pile = heappop(neg_piles)
            heappush(neg_piles, -(ceil(-pile / 2)))
            k -= 1

        return -sum(neg_piles)