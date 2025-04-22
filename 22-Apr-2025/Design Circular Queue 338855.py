# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):

        self.k = k
        self.nodes = 0
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)
        prev = self.right.prev
        prev.next, node.prev = node, prev
        node.next, self.right.prev = self.right, node
        self.nodes += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        node = self.left.next
        self.left.next = node.next
        node.next.prev = self.left
        self.nodes -= 1

        # cleaning
        node.next = node.prev = None

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.nodes == 0

    def isFull(self) -> bool:
        return self.nodes == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()