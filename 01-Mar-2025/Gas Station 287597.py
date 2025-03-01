# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # checking if the total gas is equal or greater than the total cost
        if sum(cost) > sum(gas):
            return -1

        start_idx = 0
        tank = 0
        # looping through the gas and cost to find the starting index
        for idx in range(len(gas)):
            tank += gas[idx] - cost[idx]

            if tank < 0:
                start_idx = idx + 1
                tank = 0

        return start_idx