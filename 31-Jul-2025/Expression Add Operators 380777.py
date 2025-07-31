# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)

        def backtrack(start, curr, total, prev):
            if start == n:
                if total == target:
                    res.append(''.join(curr))
                return

            for i in range(start, n):
                s = num[start:i + 1]
                int_s = int(s)

                if not curr:
                    backtrack(i + 1, [s], int_s, int_s)
                else:
                    backtrack(i + 1, curr + ['+'] + [s], total + int_s, int_s)
                    backtrack(i + 1, curr + ['-'] + [s], total - int_s, -int_s)
                    backtrack(i + 1, curr + ['*'] + [s], total - prev + int_s * prev, int_s * prev)

                if num[start] == '0':
                    break

        backtrack(0, [], 0, 0)
        return res
