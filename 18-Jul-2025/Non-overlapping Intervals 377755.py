# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        count = 0

        for interval in intervals[1:]:
            if prev_end <= interval[0]:
                prev_end = interval[1]
                continue
            count += 1

        return count
