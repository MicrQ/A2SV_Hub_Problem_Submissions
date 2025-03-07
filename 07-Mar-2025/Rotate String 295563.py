# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # if their length is not equal, it's not possible to match'em
        if len(s) != len(goal):
            return False

        return goal in (s + s)
