# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        is_block = False
        a_line = []
        result = []

        for line in source:

            i = 0
            n = len(line)

            while i < n:

                if not is_block and line[i] == '/' and i + 1 < n and line[i + 1] == '*':
                    is_block = True
                    i += 1

                elif is_block and line[i] == '*' and i + 1 < n and line[i + 1] == '/':
                    is_block = False
                    i += 1

                elif not is_block and i + 1 < n and line[i] == '/' and line[i + 1] == '/':
                    break

                elif not is_block:
                    a_line.append(line[i])

                i += 1

            if not is_block and a_line:
                result.append(''.join(a_line))
                a_line = []

        return result