# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head or index < 0:
            return -1

        i = 0
        current = self.head
        while i < index and current.next:
            current = current.next
            i += 1

        if i == index:
            return current.val

        return -1

    def addAtHead(self, val: int) -> None:

        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:

        node = Node(val)
        current = self.head

        if not current:
            self.head = node
            return

        while current.next:
            current = current.next

        current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        node = Node(val)

        i = 0
        current = self.head
        while i < index - 1 and current:
            current = current.next
            i += 1

        if current:
            node.next = current.next
            current.next = node


    def deleteAtIndex(self, index: int) -> None:

        if self.head:
            if index == 0:
                next_ = self.head.next
                self.head.next = None
                self.head = next_
                return

            current = self.head
            i = 0
            while i < index - 1 and current.next:
                i += 1
                current = current.next

            if current.next:
                tmp = current.next
                current.next = current.next.next
                tmp.next = Node


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)