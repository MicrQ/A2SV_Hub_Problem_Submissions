# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
            sorting the skills in non-decreasing order
            and matching the small with the big.
        """
        skill.sort()

        left, right = 0, len(skill) - 1
        target_sum = skill[left] + skill[right]
        sum_ = 0

        while left < right:

            if skill[left] + skill[right] != target_sum:
                return -1

            sum_ += skill[left] * skill[right]
            left += 1
            right -= 1

        return sum_
