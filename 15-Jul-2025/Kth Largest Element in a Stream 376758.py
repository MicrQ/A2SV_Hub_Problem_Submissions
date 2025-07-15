# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        self.count = 0

        for num in nums:
            self.add(num)


    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        self.count += 1

        if self.count > self.k:
            heappop(self.min_heap)
            self.count -= 1

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)