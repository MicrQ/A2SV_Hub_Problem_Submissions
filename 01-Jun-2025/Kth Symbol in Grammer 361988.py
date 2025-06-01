# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        left, right = 1, 2**(n - 1)
        bit = 0

        for i in range(n - 1):
            mid = left + (right - left) // 2
            if k > mid:
                left = mid + 1
                bit = 0 if bit == 1 else 1
            else:
                right = mid

        return bit