# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.nodes = 0
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)
        node.next = self.left.next
        node.prev = self.left
        self.left.next.prev = node
        self.left.next = node
        self.nodes += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        self.nodes += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        node = self.left.next
        node.next.prev = node.prev
        node.prev.next = node.next
        self.nodes -= 1

        node.next = None
        node.prev = None

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        node = self.right.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.nodes -= 1

        node.next = None
        node.prev = None

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.left.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.nodes == 0

    def isFull(self) -> bool:
        return self.nodes == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()