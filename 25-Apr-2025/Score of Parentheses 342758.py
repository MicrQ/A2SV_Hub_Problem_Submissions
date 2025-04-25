# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                last = stack.pop()
                val = max(last * 2, 1)
                stack[-1] += val

        return stack[-1]

# ((()))((())) # Nested 
# [6]


# ()()() # Separate
# (())() # combined
# res =  = 8
# 2 * 2 => max(1, 4) => 4
# # []