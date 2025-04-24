# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.deque = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        
        if num == self.value:
            self.count += 1
        self.deque.append(num)

        if len(self.deque) > self.k:
            left = self.deque.popleft()

            if left == self.value:
                self.count -= 1

        return self.count == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)