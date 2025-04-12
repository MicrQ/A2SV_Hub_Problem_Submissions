# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #using two pointers, one fast, one normal
        if head is None:
            return False

        fast = head
        normal = head

        while fast and fast.next:
            fast = fast.next.next
            normal = normal.next

            if fast == normal:
                return True

        return False