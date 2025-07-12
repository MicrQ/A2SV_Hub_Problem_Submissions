# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = [-num for num in stones]

        heapify(min_heap)
        while len(min_heap) > 1:
            stone1 = heappop(min_heap)
            stone2 = heappop(min_heap)

            if stone1 < stone2:
                heappush(min_heap, stone1 - stone2)

        return -min_heap[0] if min_heap else 0
