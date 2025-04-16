# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head

        # counting number of nodes in the list
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n += 1

        tail = head
        temp = head
        i = 1

        k = k % n

        while temp.next:

            # checking if the new tail is reached
            if i < n - k:
                tail = tail.next
                i += 1

            temp = temp.next

        temp.next = head
        head = tail.next
        tail.next = None

        return head
