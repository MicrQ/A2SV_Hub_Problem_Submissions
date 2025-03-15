# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return False
        if s == "":
            return True

        key_val = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c not in key_val.keys():
                if len(stack) == 0 or key_val.get(stack[-1]) != c:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0