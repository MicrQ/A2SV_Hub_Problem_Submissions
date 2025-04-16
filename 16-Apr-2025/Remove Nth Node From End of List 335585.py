# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return head

        temp = head
        nodes = 0

        # counting number of nodes
        while temp:
            temp = temp.next
            nodes += 1

        if n == nodes:
            return head.next
        
        temp = head
        i = 1
        while i < nodes - n:
            temp = temp.next
            i += 1

        if temp.next:
            temp.next = temp.next.next

        return head
