# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        mem = {}
        return self.helper(n, mem)

    def helper(self, n: int, mem: dict):
        """ recursively sums the digits of n """
        if n == 1:
            return True

        if mem.get(n) is not None:
            return False

        # memorizing n(to not cycle again)
        mem[n] = 1
        result = sum([int(i) ** 2 for i in str(n)])

        return self.helper(result, mem)
