# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        
        commands = {
            'G': 'G',
            '()': 'o',
            '(al)': 'al'
        }

        i = 0
        result = ''

        while i < len(command):
            if command[i:i + 2] == '(a':
                result += commands['(al)']
                i += 3

            elif command[i: i + 2] == '()':
                result += commands['()']
                i += 1

            else:
                result += commands[command[i]]

            i += 1

        return result
            