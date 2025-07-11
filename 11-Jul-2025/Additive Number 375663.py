# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        def backtrack(start, curr):
            if start == n:
                return len(curr) >= 3

            for end in range(start + 1, n + 1):
                s_num = num[start:end]
                if len(s_num) > 1 and s_num[0] == '0':
                    continue

                i_num = int(s_num)
                if len(curr) < 2:
                    if backtrack(end, curr + [i_num]):
                        return True
                else:
                    if i_num == curr[-1] + curr[-2]:
                        if backtrack(end, curr + [i_num]):
                            return True

            return False

        return backtrack(0, [])