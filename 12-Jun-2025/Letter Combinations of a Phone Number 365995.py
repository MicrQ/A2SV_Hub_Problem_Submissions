# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        keys = {'2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        res = []

        def backtrack(start, arr):
            if start == n:
                res.append(''.join(arr))
                return

            for char in keys[digits[start]]:
                arr.append(char)
                backtrack(start + 1, arr)
                arr.pop()

        if digits:
            backtrack(0, [])

        return res
