# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(perms, num_s):
            if not num_s:
                res.append(perms[:])
                return

            for i in range(len(num_s)):
                perms.append(num_s[i])
                helper(perms, num_s[:i] + num_s[i + 1:])
                perms.pop()

        helper([], nums)
        return res