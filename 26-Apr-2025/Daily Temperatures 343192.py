# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        res = [0] * n
        mono_stack = []

        for i in range(n):
            while mono_stack and temperatures[mono_stack[-1]] < temperatures[i]:
                index = mono_stack.pop()
                res[index] = i - index
            mono_stack.append(i)

        return res

