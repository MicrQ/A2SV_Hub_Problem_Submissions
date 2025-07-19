# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        res = n

        prev = points[0]
        for i in range(1, n):
            if points[i][0] <= prev[1]:
                res -= 1
                prev = [points[i][0], min(points[i][1], prev[1])]
            else:
                prev = points[i]

        return res
