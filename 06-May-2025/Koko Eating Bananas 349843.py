# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_k = right

        while left <= right:
            hours = 0
            k = left + (right - left) // 2

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                min_k = min(min_k, k)
                right = k - 1

            else:
                left = k + 1

        return min_k