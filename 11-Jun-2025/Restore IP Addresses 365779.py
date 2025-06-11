# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def backtrack(start, count, ints):
            if count == 4 and start >= n:
                res.append('.'.join(ints))
                return

            if count == 4:
                return

            for i in range(start, min(start + 3, n)):
                s_num = s[start:i + 1]
                if int(s_num) <= 255 and (len(s_num) == 1 or int(s_num[0]) > 0):
                    ints.append(s_num)
                    backtrack(i + 1, count + 1, ints)
                    ints.pop()

        if n <= 12:
            backtrack(0, 0, [])

        return res
