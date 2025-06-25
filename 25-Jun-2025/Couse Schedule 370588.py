# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        visiting = set()

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for pre in graph[course]:
                if pre not in visited:
                    if not dfs(pre):
                        return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
