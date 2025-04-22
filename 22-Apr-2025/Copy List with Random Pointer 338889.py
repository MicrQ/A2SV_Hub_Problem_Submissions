# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        old_new_pair = {}
        temp = head

        # creating the moking map
        while temp:
            old_new_pair[temp] = Node(temp.val)
            temp = temp.next

        # linking the copy list now
        for old, new in old_new_pair.items():

            new.next = old_new_pair.get(old.next)
            new.random = old_new_pair.get(old.random)

        return old_new_pair.get(head)
