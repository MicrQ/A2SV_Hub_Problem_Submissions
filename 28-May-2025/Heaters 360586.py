# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        n = len(heaters)
        radius = 0

        def helper(house):
            min_radius = float('inf')
            left, right = 0, n - 1

            while left <= right:
                mid = left + (right - left) // 2
                min_radius = min(min_radius, abs(heaters[mid] - house))

                if heaters[mid] > house:
                    right = mid - 1
                else:
                    left = mid + 1

            return min_radius

        for house in houses:
            radius = max(radius, helper(house))

        return radius