# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        queue = deque()

        # building the prerequisite graph and counting in_degrees
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            in_degree[crs] += 1

        # identifying source nodes
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        order = []
        # constructing the order
        while queue:
            node = queue.popleft()
            order.append(node)

            # removing dependecy and possibly adding new node to the queue
            for nei in graph[node]:
                in_degree[nei] -= 1

                if in_degree[nei] == 0: # has nomore prerequisites
                    queue.append(nei)

        return order if len(order) == numCourses else []
