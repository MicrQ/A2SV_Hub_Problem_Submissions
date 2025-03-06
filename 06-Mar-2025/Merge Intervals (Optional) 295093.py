# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        result = [intervals[0]]

        for interval in intervals:

            # check if the end of the last interval is less or equal 
            # to the start of the new interval and merge
            if result[-1][1] >= interval[0]:
                result[-1][1] = max(interval[1], result[-1][1])

            else:
                # non-overlapping interval
                result.append(interval)

        return result
