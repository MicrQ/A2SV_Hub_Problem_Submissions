# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        res = 0
        costs.sort(key=lambda x: x[1] - x[0])

        for i in range(n):
            if i < n // 2:
                res += costs[i][1]
            else:
                res += costs[i][0]

        return res
