# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        """
            since length of ranges will be <= 50, creating a list
            to store a boolean value for each covered num works best.
        """
        covered = [False] * 51

        for begin, end in ranges:
            # updating bool value of each covered num inclusively

            for num in range(begin, end + 1):
                covered[num] = True

        # checking if the required nums are covered
        return all(covered[left:right + 1])
        