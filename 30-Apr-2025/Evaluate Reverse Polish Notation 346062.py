# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))

            else:
                top = stack.pop()

                if token == '+':
                    stack[-1] += top
                elif token == '*':
                    stack[-1] *= top
                elif token == '-':
                    stack[-1] -= top
                else:
                    stack[-1] = int(stack[-1] / top)

        return stack[0]