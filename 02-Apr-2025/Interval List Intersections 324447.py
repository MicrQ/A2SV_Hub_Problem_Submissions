# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        # ofc using two pointers
        answer = []
        i, j = 0, 0

        # looping through the intersections
        while i < len(firstList) and j < len(secondList):

            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # checking if the intersection is valid and appending
            if start <= end:
                answer.append([start, end])

            # moving the ptr to the interval ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1

            else:
                j += 1

        return answer
