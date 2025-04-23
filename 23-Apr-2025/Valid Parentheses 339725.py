# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        closings = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for char in s:
            if stack and stack[-1] == closings.get(char, ''):
                stack.pop()

            else:
                stack.append(char)

        return not stack