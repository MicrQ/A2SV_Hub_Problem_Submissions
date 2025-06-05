# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        frqs = Counter(nums)

        def helper(perms, count):
            if count == n:
                res.append(perms[:])
                return

            for num in frqs:
                if frqs[num] > 0:
                    perms.append(num)
                    frqs[num] -= 1

                    helper(perms, count + 1)

                    perms.pop()
                    frqs[num] += 1

        helper([], 0)
        return res
