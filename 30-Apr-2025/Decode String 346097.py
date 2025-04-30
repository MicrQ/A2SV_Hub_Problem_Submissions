# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                inner_s = ''
                while stack and stack[-1] != '[':
                    inner_s = stack.pop() + inner_s
                stack.pop()

                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * inner_s)

            else:
                stack.append(char)

        return ''.join(stack)