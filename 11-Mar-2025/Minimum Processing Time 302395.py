# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        # sorting the processing time and sorting the tasks(reverse order)
        # will help to assign task for each process in efficient way

        processorTime.sort()
        tasks.sort(reverse=True)

        min_max = 0

        for i in range(len(processorTime)):

            # get the value of the slowest task from the group of four
            group_max = tasks[i * 4]

            min_max = max(min_max, processorTime[i] + group_max)

        return min_max
