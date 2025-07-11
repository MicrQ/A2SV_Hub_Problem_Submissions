# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frqs = Counter(nums)

        heap = []
        for num, frq in frqs.items():
            if len(heap) < k:
                heappush(heap, (frq, num))
            else:
                if frq > heap[0][0]:
                    heappop(heap)
                    heappush(heap, (frq, num))

        return [num for frq, num in heap]
