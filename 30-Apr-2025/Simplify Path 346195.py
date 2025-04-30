# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        dir = ''
        for char in path + '/':
            if char != '/':
                dir += char

            else:
                if dir == '..':
                    if stack:
                        stack.pop()
                elif dir and dir != '.':
                    stack.append(dir)

                dir = ''

        return '/' + '/'.join(stack)
