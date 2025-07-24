# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        res = []
        min_heap = []

        # appending index of each tast to it
        for i, task in enumerate(tasks):
            task.append(i)

        # sorting tasks with their enquing time
        tasks.sort(key=lambda x: x[0])

        # doing the process ...
        i = 0
        time = tasks[0][0]
        while i < n or min_heap:

            # adding all tasks whose enquing time is the current time range
            while i < n and time >= tasks[i][0]:
                heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1

            if min_heap:
                processing_time, idx = heappop(min_heap)
                time += processing_time
                res.append(idx)
            else:
                time = tasks[i][0]

        return res