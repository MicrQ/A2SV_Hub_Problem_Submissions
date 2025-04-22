# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node():
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.count = 0

    def get(self, key: int) -> int:

        if not key in self.cache:
            return -1

        node = self.cache.get(key)
        self.deleteNode(node)
        self.insertNode(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.deleteNode(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insertNode(node)

        if self.count > self.capacity:
            del self.cache[self.left.next.key]
            self.deleteNode(self.left.next)

    def deleteNode(self, node: Node) -> None:

        prev, next_ = node.prev, node.next
        prev.next, next_.prev = next_, prev
        node.next = node.prev = None
        self.count -= 1

    def insertNode(self, node: Node) -> None:

        prev, next_ = self.right.prev, self.right
        prev.next = next_.prev = node
        node.next, node.prev = next_, prev
        self.count += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)