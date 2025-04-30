# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        temp = head
        stack = []

        while temp:
            if temp.child:
                if temp.next:
                    stack.append(temp.next)
                temp.next = temp.child
                temp.child.prev = temp
                temp.child = None

            if not temp.next and stack:
                top = stack.pop()
                temp.next = top
                top.prev = temp

            else:
                temp = temp.next

        return head

            
