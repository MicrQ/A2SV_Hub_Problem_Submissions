# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(arr, opn, clz):
            if opn == clz == 0:
                res.append(''.join(arr))
                return

            if opn:
                helper(arr + ['('], opn - 1, clz)

            if clz > opn:
                helper(arr + [')'], opn, clz - 1)

        helper([], n, n)

        return res
