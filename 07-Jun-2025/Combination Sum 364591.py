# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def helper(start, combs, total):
            if total == target:
                res.append(combs[:])
                return
            if start >= n or total > target:
                return

            combs.append(candidates[start])
            helper(start, combs, total + candidates[start])
            combs.pop()
            helper(start + 1, combs, total)

        helper(0, [], 0)
        return res
