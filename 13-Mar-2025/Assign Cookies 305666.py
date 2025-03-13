# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()

        top = len(g) - 1
        btm = len(s) - 1

        count = 0

        while top >= 0 and btm >= 0:

            # checking if the size of the cookie satifies the kid
            if s[btm] >= g[top]:
                count += 1
                btm -= 1

            top -= 1

        return count