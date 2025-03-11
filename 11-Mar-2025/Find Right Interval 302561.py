# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        n = len(intervals)
        # creating a sorted version of tuple keeping the original index
        interval_pairs = sorted((start, end, idx) for idx, (start, end) in enumerate(intervals))

        # list of starts to use for binary search
        starts = [start for start, _, _ in interval_pairs]

        # build the result list
        result = [-1] * n

        # finding right interval for each intervals
        for start, end, idx in interval_pairs:

            index = bisect_left(starts, end)

            if index < n:
                result[idx] = interval_pairs[index][2]

        return result
