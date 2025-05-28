# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ['0']

        def helper(n):
            if n == 0:
                return

            s.append('1')
            for i in range(len(s) - 2, -1, -1):
                s.append('1' if s[i] == '0' else '0')

            helper(n - 1)

        # calling the recursive func
        helper(n)
        return s[k - 1]