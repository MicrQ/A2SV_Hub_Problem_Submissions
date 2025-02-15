# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        total = 0

        # counting rabbit answer frequency
        for ans, frq in Counter(answers).items():
            rabits = ans + 1
            
            # grouping as many rabbits as possible in a group
            # and creating new group if they can't fit
            rabits_grp = ceil(frq / rabits)

            # multipling the number of rabit groups needed with
            # number of rabbit in a group and adding it to the total
            total += rabits_grp * rabits
            
        return total