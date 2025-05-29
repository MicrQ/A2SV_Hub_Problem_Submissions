# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        right = sum(weights)
        left = max(weights)
        weight = right

        def validWeight(weight):
            days_ = 1
            per_ship = 0

            for package in weights:
                if per_ship + package > weight:
                    days_ += 1
                    per_ship = 0
                per_ship += package

            return days >= days_

        while left <= right:
            mid = left + (right - left) // 2

            if validWeight(mid):
                weight = min(weight, mid)
                right = mid - 1
            else:
                left = mid + 1

        return weight 