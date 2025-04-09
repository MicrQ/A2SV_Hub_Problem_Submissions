# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        boats = 0

        # sorting the people weights and using two colliding pointer
        people.sort()

        left, right = 0, len(people) - 1

        while left <= right:

            # if the sum of left and right doesnt surpass limit, move both pointers
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1

            else:
                # moving the right pointer alone
                right -= 1

            boats += 1

        return boats
