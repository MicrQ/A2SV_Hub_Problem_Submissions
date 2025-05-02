# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 0:
            return 0
        if a == 1:
            return 1

        num_b = ''
        for num in b:
            num_b += str(num)

        return pow(a, int(num_b), 1337)
        